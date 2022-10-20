import textwrap

import dash
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import dash_treeview_antd
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash import callback, dcc, html
from dash.dependencies import MATCH, ALL, ClientsideFunction, Input, Output, State
from dash_service.components import fa
from dash_service.models import Page, Project

# from dash_service.pages import (
#     get_codelist,
#     get_col_unique,
#     get_dataset,
#     get_search_countries,
#     get_selection_tree,
#     years,
# )
from dash_service.pages import get_structure, get_data, years, get_geojson
from dash_service.pages import (
    add_structure,
    get_structure_id,
    get_dim_position,
    get_code_from_structure,
    get_col_name,
    merge_with_codelist,
)

from flask import abort

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 0)


# The store, data input/output used in callbacks is defined in "layouts.py", it holds the selection: years, country...


# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = px.colors.qualitative.Dark24

# TODO: language shouold be read from a param if forced or from the browser
lang = "en"
# move this elsewhere
translations = {
    "en": {"REF_AREA": "Geographic areas"},
    "pt": {"REF_AREA": "Geographic areas [PT]"},
}

# the configuration of the "Download plot" button in the charts
cfg_download_plot = {
    "toImageButtonOptions": {
        "format": "png",  # one of png, svg, jpeg, webp
        "filename": "plot",
        "width": 1200,
        "height": 800,
        "scale": 1,  # Multiply title/legend/axis/canvas sizes by this factor
    }
}

colours = [
    "primary",
    "success",
    "warning",
    "danger",
    "secondary",
    "info",
    "success",
    "danger",
]
AREA_KEYS = [
    "MAIN",
    "AREA_1",
    "AREA_2",
    "AREA_3",
    "AREA_4",
    "AREA_5",
    "AREA_6",
]

CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}

EMPTY_CHART = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No data is available for the selected filters",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 28},
            }
        ],
    }
}

# This hooks into Dash's multipage functionality and allows us to specify the URL pattern
# https://dash.plotly.com/urls
dash.register_page(
    __name__,
    path_template="/<project_slug>/<page_slug>",
    path="/brazil/child-education",  # this is the default path and working example
)


def make_page_nav(pages, vertical=False, **kwargs):
    return html.Header(
        id="header",
        className="header",
        children=[
            html.Div(
                className="container-fluid",
                children=[
                    html.Div(
                        className="row",
                        children=[
                            dbc.Nav(
                                [
                                    dbc.NavItem(
                                        [
                                            dbc.NavLink(
                                                page["name"],
                                                className="ms-2",
                                                href=page["path"],
                                                active="exact",
                                            ),
                                        ],
                                    )
                                    for page in pages
                                ],
                                vertical=vertical,
                                pills=True,
                                justified=True,
                                className="col-12",
                            )
                        ],
                    )
                ],
            ),
        ],
        **kwargs,
    )


def layout(project_slug=None, page_slug=None, **query_parmas):
    """
    Handler for Dash's multipage functionality.
    This function is called with the URL parameters and returns the layout for that page.
    TODO: This could also support query parameters if needed for addtional SDMX filters.

    Args:
        project_name (str): The name of the project in the admin
        page_slug (str): The slug of the page in the admin

    Returns:
        html.Div: The rendered page
    """
    if project_slug is None or page_slug is None:
        # project_slug and page_slug are None when this is called for validation
        # create a dummy page
        return render_page_template({}, "Validation Page", [], "")

    all_pages = Page.where(project___slug=project_slug).all()
    if all_pages is None or len(all_pages) == 0:
        abort(404, description="No pages found for project")
    all_pages = [{"name": p.title, "path": p.slug} for p in all_pages]

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    page = Page.where(project___slug=project_slug, slug=page_slug).first_or_404()

    config = page.content
    main_title = config["main_title"]

    return render_page_template(config, main_title, all_pages, page.geography)


def render_page_template(
    page_config: dict,
    main_title: str,
    all_pages: dict,
    geoj: str,
    **kwargs,
) -> html.Div:
    """Renders the page template based on the page config and other parameters

    Args:
        page_config (dict): page config from the database
        main_title (_type_): main title of the page
        all_pages (_dict_): the links to the page to add to the navbar

    Returns:
        html.Div: The dash Div representing the redenderd page against the config
    """
    template = html.Div(
        [
            dcc.Store(id="page_config", data=page_config),
            dcc.Store(id="geoj", data=geoj),
            dcc.Store(id="data_structures", data={}, storage_type="session"),
            dcc.Location(id="theme"),
            make_page_nav(all_pages),
            html.Br(),
            dbc.Col(
                html.Div(
                    [
                        render_heading(main_title),
                        dbc.Row(
                            children=[
                                dbc.Col(
                                    [
                                        render_themes(),
                                        render_years(),
                                    ]
                                ),
                            ],
                            # sticky="top",
                            className="bg-light",
                        ),
                        dbc.Row(
                            [
                                dbc.CardDeck(
                                    id="cards_row",
                                    className="mt-3",
                                ),
                            ],
                            justify="center",
                        ),
                        html.Br(),
                        dbc.CardDeck(
                            [make_area(area) for area in ["MAIN"]],
                            style={"display": "block"},
                        ),
                        html.Br(),
                        dbc.CardDeck(
                            [make_area(area) for area in ["AREA_1", "AREA_2"]],
                        ),
                        html.Br(),
                        dbc.CardDeck(
                            [make_area(area) for area in ["AREA_3", "AREA_4"]],
                        ),
                        html.Br(),
                        dbc.CardDeck(
                            [make_area(area) for area in ["AREA_5", "AREA_6"]],
                        ),
                        html.Br(),
                    ]
                )
            ),
        ],
    )
    return template


def render_heading(main_title) -> html.Div:
    return html.Div(
        className="heading",
        style={"padding": 36},
        children=[
            html.Div(
                className="heading-content",
                children=[
                    html.Div(
                        className="heading-panel",
                        style={"padding": 20},
                        children=[
                            html.H1(
                                main_title,
                                id="main_title",
                                className="heading-title",
                            ),
                            html.P(
                                id="subtitle",
                                className="heading-subtitle",
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def render_themes() -> html.Div:
    return dbc.Row(
        [
            dbc.ButtonGroup(
                id="themes",
            ),
        ],
        id="theme-row",
        # width=4,
        className="my-2",
        # no_gutters=True,
        justify="center",
        style={
            "verticalAlign": "center",
            "display": "flex",
        },
    )


def render_years() -> html.Div:
    return dbc.Row(
        [
            dbc.DropdownMenu(
                label=f"Years: {years[0]} - {years[-1]}",
                id="collapse-years-button",
                className="m-2",
                color="info",
                # block=True,
                children=[
                    dbc.Card(
                        dcc.RangeSlider(
                            id="year_slider",
                            min=0,
                            max=len(years) - 1,
                            step=None,
                            marks={
                                index: str(year) for index, year in enumerate(years)
                            },
                            value=[
                                0,
                                len(years) - 1,
                            ],
                        ),
                        style={
                            "maxHeight": "250px",
                            "minWidth": "500px",
                        },
                        className="overflow-auto",
                        body=True,
                    ),
                ],
            )
        ],
        id="filter-row",
        justify="center",
    )


def make_area(area_name: str) -> dbc.Card:
    """Generates a single graph area "card" with a title and a graph
       with a menu for the graph type and indicators selection
    TODO: migrate to dash AIO component

    Args:
        area_name (str): Name fo this area tile

    Returns:
        dbc.Card: Returns a bootstrap card with the area title and graph
    """

    area_id = {"type": "area", "index": area_name}
    popover_id = {"type": "area_sources", "index": area_name}
    historical_data_style = {"display": "none"}
    breakdowns_style = {"display": "block"}
    down_csv_id = {"type": "down_csv", "index": area_name}
    down_csv_btn_id = {"type": "btn_down_csv", "index": area_name}
    down_exc_id = {"type": "down_exc", "index": area_name}
    down_exc_btn_id = {"type": "btn_down_exc", "index": area_name}

    # TODO: still differentiating main area id from other areas ids because the call backs are still not unified
    if area_name == "MAIN":
        area_id = f"{area_name.lower()}_area"
        popover_id = f"{area_name.lower()}_area_sources"
        historical_data_style = {"display": "block"}
        breakdowns_style = {"display": "none"}

    area = dbc.Card(
        [
            dbc.CardHeader(
                id={"type": "area_title", "index": area_name},
                style={"fontWeight": "bold"},
            ),
            dbc.CardBody(
                [
                    dcc.Dropdown(
                        id={"type": "area_options", "index": area_name},
                        className="dcc_control",
                    ),
                    html.Br(),
                    dbc.Checklist(
                        options=[
                            {
                                "label": "Show historical data",
                                "value": 1,
                            }
                        ],
                        value=[],
                        id={
                            "type": "historical_data_toggle",
                            "index": area_name,
                        },
                        switch=True,
                        style=historical_data_style,
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_types", "index": area_name},
                        inline=True,
                    ),
                    dcc.Loading([dcc.Graph(id=area_id, config=cfg_download_plot)]),
                    dbc.Checklist(
                        options=[
                            {
                                "label": "Exclude outliers ",
                                "value": 1,
                            }
                        ],
                        value=[1],
                        id={
                            "type": "exclude_outliers_toggle",
                            "index": area_name,
                        },
                        switch=True,
                        style={"display": "none"},
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_breakdowns", "index": area_name},
                        inline=True,
                        style=breakdowns_style,
                    ),
                    dbc.ButtonGroup(
                        className="float_left",
                        children=[
                            dbc.Button(
                                "Download Excel",
                                id=down_exc_btn_id,
                                className="btn-sm",
                            ),
                            dbc.Button(
                                "Download CSV",
                                id=down_csv_btn_id,
                                className="btn-sm",
                            ),
                        ],
                    ),
                    dcc.Download(id=down_csv_id),
                    dcc.Download(id=down_exc_id),
                    html.Div(
                        fa("fas fa-info-circle"),
                        id=f"{area_name.lower()}_area_info",
                        className="float-right",
                    ),
                    dbc.Popover(
                        [
                            dbc.PopoverHeader("Sources"),
                            dbc.PopoverBody(id=popover_id),
                        ],
                        id="hover",
                        target=f"{area_name.lower()}_area_info",
                        trigger="hover",
                    ),
                ]
            ),
        ],
        id={"type": "area_parent", "index": area_name},
    )
    return area


def make_card(
    card_id,
    name,
    suffix,
    indicator_sources,
    source_link,
    indicator_header,
    numerator_pairs,
) -> dbc.Card:
    """Generates a single card with a title, a value and a suffix

    Args:
        card_id (_type_): _description_
        name (_type_): _description_
        suffix (_type_): _description_
        indicator_sources (_type_): _description_
        source_link (_type_): _description_
        indicator_header (_type_): _description_
        numerator_pairs (_type_): _description_

    Returns:
        dbc.Card: The rendered static card
    """
    # popover_head = html.P(f"Sources: {indicator_sources}")

    # if source_link:
    #     popover_head = html.A(
    #         html.P(f"Sources: {indicator_sources}"),
    #         href=source_link,
    #         target="_blank",
    #     )

    popover_head = html.P("Sources")

    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H1(
                        indicator_header,
                        className="display-4",
                        style={
                            # "fontSize": 50,
                            "textAlign": "center",
                            "color": "#1cabe2",
                        },
                    ),
                    html.H4(suffix, className="card-title"),
                    html.P(name, className="lead"),
                    html.Div(
                        fa("fas fa-info-circle"),
                        id=f"{card_id}_info",
                        # className="float-right",
                        style={
                            "position": "absolute",
                            "bottom": "10px",
                            "right": "10px",
                        },
                    ),
                ],
                style={
                    # "fontSize": 50,
                    "textAlign": "center",
                },
            ),
            dbc.Popover(
                [
                    dbc.PopoverHeader(popover_head),
                    dbc.PopoverBody(indicator_sources),
                ],
                id="hover",
                target=f"{card_id}_info",
                trigger="hover",
            ),
        ],
        color="primary",
        outline=True,
        id=card_id,
    )

    return card


def get_card_popover_body(sources):
    """This function is used to generate the list of countries that are part of the card's
        displayed result; it displays the countries as a list, each on a separate line

    Args:
        sources (_type_): _description_

    Returns:
        _type_: _description_
    """
    countries = []
    # lbassil: added this condition to stop the exception when sources is empty
    if len(sources) > 0:
        for index, source_info in sources.sort_values(by="OBS_VALUE").iterrows():
            countries.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
        card_countries = "\n".join(countries)
        return card_countries

    return "NA"


# This callback is triggered on a "hash" change in the URL
# It hides areas when not defined: e.g. we have two areas in the cfg: hide area 3 and 4
@callback(
    Output({"type": "area_parent", "index": MATCH}, "hidden"),
    Input("theme", "hash"),
    [
        State("page_config", "data"),
        State({"type": "area_parent", "index": MATCH}, "id"),
    ],
)
def display_areas(theme, page_config, id):
    area = id["index"]
    theme = theme[1:].upper() if theme else next(iter(page_config["THEMES"].keys()))
    return area not in page_config["THEMES"][theme]


# Triggered when the theme, year slider or country change
# It only updates the state of the selection: theme and year
@callback(
    Output("store", "data"),
    Output("collapse-years-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
    ],
    State("page_config", "data"),
)
def apply_filters(
    theme,
    years_slider,
    store_page_config,
):

    theme = (
        theme[1:].upper() if theme else next(iter(store_page_config["THEMES"].keys()))
    )

    selected_years = years[years_slider[0] : years_slider[1] + 1]

    selections = dict(theme=theme, years=selected_years)

    return (selections, f"Years: {selected_years[0]} - {selected_years[-1]}")


@callback(
    Output("data_structures", "data"),
    [Input("store", "data")],
    [State("page_config", "data")],
)
def download_structures(selections, page_config):
    data_structures = {}

    # cards
    for card in page_config["THEMES"][selections["theme"]]["CARDS"]:
        add_structure(card["data"], data_structures)

    # Main
    if (
        "MAIN" in page_config["THEMES"][selections["theme"]]
        and "data" in page_config["THEMES"][selections["theme"]]["MAIN"]
    ):
        for data_node in page_config["THEMES"][selections["theme"]]["MAIN"]["data"]:
            add_structure(data_node, data_structures)

    # areas
    for area in AREA_KEYS:
        if (
            area in page_config["THEMES"][selections["theme"]]
            and "data" in page_config["THEMES"][selections["theme"]][area]
        ):
            for data_node in page_config["THEMES"][selections["theme"]][area]["data"]:
                add_structure(data_node, data_structures)

    return data_structures


# this function and the show_cards callback update the cards
# TODO: INDICATOR's label must be pulled!
def indicator_card(card_id, name, suffix, config):
    df = get_data(config, lastnobservations=1, labels="id")
    card_value = ""
    if len(df) > 0:
        card_value = df.iloc[0]["OBS_VALUE"]
        # if suffix has not been overridden pull it from the indicator
        print("This must be pulled from the structure")
        if suffix is None:
            suffix = df.iloc[0]["INDICATOR"]
        if "DATA_SOURCE" in df.columns:
            data_source = df.iloc[0]["DATA_SOURCE"]

    source_link = ""

    return make_card(card_id, name, suffix, data_source, source_link, card_value, [])


@callback(
    Output("cards_row", "children"),
    [Input("store", "data")],
    [State("page_config", "data")],
)
def show_cards(selections, page_config):
    cards = []
    for num, card in enumerate(page_config["THEMES"][selections["theme"]]["CARDS"]):
        name = None
        suffix = None
        if "name" in card and card["name"] != "":
            name = card["name"]
        if "suffix" in card and card["suffix"] != "":
            suffix = card["suffix"]
        to_add = indicator_card(f"card-{num}", name, suffix, card["data"])
        cards.append(to_add)

    return cards


# this callback updates the selection changed? It shouldn't be connected to the data but to the config load?
@callback(
    Output("subtitle", "children"),
    Output("themes", "children"),
    [
        Input("store", "data"),
    ],
    State("page_config", "data"),
)
def show_themes(selections, config):
    if (
        selections is None
        or selections["theme"] is None
        or selections["theme"].strip() == ""
    ):
        theme_key = list(config["THEMES"].keys())[0]
        theme = config["THEMES"][theme_key]
    else:
        theme_key = selections["theme"]
        theme = config["THEMES"][selections["theme"]]

    subtitle = theme.get("NAME")

    # hide the buttons when only one option is available
    if len(config["THEMES"].items()) == 1:
        return subtitle, []

    buttons = [
        dbc.Button(
            value["NAME"],
            id=key,
            color=colours[num],
            className="theme mx-1",
            href=f"#{key.lower()}",
            active=theme_key == key,
        )
        for num, (key, value) in enumerate(config["THEMES"].items())
    ]
    return subtitle, buttons


# Triggered when the selection changes. Updates the main area ddl, the area types?
# Todo: What is area_type?


@callback(
    Output({"type": "area_title", "index": MATCH}, "children"),
    Output({"type": "area_options", "index": MATCH}, "options"),
    Output({"type": "area_types", "index": MATCH}, "options"),
    Output({"type": "area_options", "index": MATCH}, "value"),
    Output({"type": "area_types", "index": MATCH}, "value"),
    Input("store", "data"),
    [
        State("page_config", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
        State("data_structures", "data"),
    ],
)
def set_options(selection, config, id, data_structures):

    area = id["index"]
    area_options = area_types = []

    default_option = ""

    # Find the data nodes (can be more than one) in the current theme and area(area id is aparam)
    if area in config["THEMES"][selection["theme"]]:
        api_params = config["THEMES"][selection["theme"]][area].get("data")

        area_options = []

        # Loop all the data calls for the area (it can contain multiple)
        for idx, ap in enumerate(api_params):

            # Is it there a label? Then override the title contained in the codelist
            if "label" in ap:
                lbl = ap["label"]
            else:
                struct_id = get_structure_id(ap)
                indic_position = get_dim_position(
                    data_structures, struct_id, "INDICATOR"
                )
                code_id = ap["dq"].split(".")[indic_position]

                lbl = get_code_from_structure(
                    struct_id, data_structures, "INDICATOR", code_id
                )["name"]

            key = selection["theme"] + "|" + area + "|" + str(idx)
            if idx == 0:
                default_option = key
            area_options.append({"label": lbl, "value": key})

        area_types = [
            {
                "label": name.capitalize(),
                "value": name,
            }
            for name in config["THEMES"][selection["theme"]][area]
            .get("graphs", {})
            .keys()
        ]

    name = (
        config["THEMES"][selection["theme"]][area].get("name")
        if area in config["THEMES"][selection["theme"]]
        else ""
    )

    default_graph = (
        config["THEMES"][selection["theme"]][area].get("default_graph")
        if area in config["THEMES"][selection["theme"]]
        else ""
    )

    return name, area_options, area_types, default_option, default_graph


# Triggered when the selection changes. Updates the main area graph
@callback(
    Output("main_area", "figure"),
    Output("main_area_sources", "children"),
    [
        Input({"type": "area_options", "index": "MAIN"}, "value"),
        Input({"type": "historical_data_toggle", "index": "MAIN"}, "value"),
        Input("store", "data"),
    ],
    [
        State("page_config", "data"),
        Input("geoj", "data"),
        State("data_structures", "data"),
    ],
)
def main_figure(
    indicator, show_historical_data, selections, config, geoj, data_structs
):
    latest_data = not show_historical_data

    options = config["THEMES"][selections["theme"]]["MAIN"]["options"]

    series_id = indicator.split("|")
    cfg_data = config["THEMES"][series_id[0]][series_id[1]]["data"][int(series_id[2])]
    struct_id = get_structure_id(cfg_data)
    # series = config["THEMES"][selections["theme"]]["MAIN"]["data"]
    time_period = [min(selections["years"]), max(selections["years"])]

    lastnobs = None
    if latest_data:
        lastnobs = 1
    data = get_data(cfg_data, years=time_period, lastnobservations=lastnobs)

    if data.empty:
        return EMPTY_CHART, ""

    geo_json_data = get_geojson(geoj)

    # we need the ref_area and data source codelists (DATA_SOURCE can be coded)
    # get and merge the ref area labels
    data = merge_with_codelist(data, data_structs, struct_id, "REF_AREA")
    data = merge_with_codelist(data, data_structs, struct_id, "DATA_SOURCE")

    source_link = ""
    source = ""
    if "_L_DATA_SOURCE" in data.columns:
        source = ", ".join(list(data["_L_DATA_SOURCE"].unique()))

    print("EDIT THE OPTIONS IN THE CFG")
    options["hover_data"]["_L_REF_AREA"] = True
    del options["hover_data"]["name"]
    del options["labels"]

    # Add the labels for all the dimensions
    options["labels"] = {"OBS_VALUE": "Value"}
    for dim in data_structs[struct_id]["dsd"]["dims"]:
        dim_id = dim["id"]
        dim_lbl = get_col_name(struct_id, dim_id, data_structs)
        lbl_dim_id = dim_id
        # Is the column coded? Than get the label column (just ref_area)
        if "_L_" + dim_id in data.columns:
            lbl_dim_id = "_L_" + dim_id
            options["labels"][lbl_dim_id] = dim_lbl

    options["geojson"] = geo_json_data

    data["OBS_VALUE"] = pd.to_numeric(data["OBS_VALUE"])

    main_figure = px.choropleth_mapbox(data, **options)
    main_figure.update_layout(margin={"r": 0, "t": 1, "l": 2, "b": 1})

    if not source_link:  # is it none or empty?
        return main_figure, html.P(source)
    else:
        return main_figure, html.A(html.P(source), href=source_link, target="_blank")


# triggered on selection change. Updates the areas
@callback(
    Output({"type": "area", "index": MATCH}, "figure"),
    Output({"type": "area_sources", "index": MATCH}, "children"),
    [
        Input("store", "data"),
        Input({"type": "area_options", "index": MATCH}, "value"),
        Input({"type": "area_breakdowns", "index": MATCH}, "value"),
        Input({"type": "area_types", "index": MATCH}, "value"),
        Input({"type": "exclude_outliers_toggle", "index": MATCH}, "value"),
    ],
    [
        State("page_config", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
        State("data_structures", "data"),
    ],
)
def area_figure(
    selections,
    indicator,
    compare,
    selected_type,
    exclude_outliers,
    config,
    id,
    data_structs,
):
    # only run if indicator not empty
    if not indicator:
        return {}, {}

    area = id["index"]
    series_id = indicator.split("|")
    series = config["THEMES"][selections["theme"]][area]["data"][int(series_id[2])]
    time_period = [min(selections["years"]), max(selections["years"])]
    # ref_areas = selections["countries"]
    struct_id = get_structure_id(series)

    default_graph = config["THEMES"][selections["theme"]][area].get(
        "default_graph", "line"
    )
    fig_type = selected_type if selected_type else default_graph
    fig_config = config["THEMES"][selections["theme"]][area]["graphs"][fig_type]
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")
    # dimension = False if fig_type == "line" or compare == "TOTAL" else compare

    if fig_type == "line":
        data = get_data(series, years=time_period)
    else:
        data = data = get_data(series, years=time_period, lastnobservations=1)

    data["OBS_VALUE"] = pd.to_numeric(data["OBS_VALUE"], errors="coerce")
    data["TIME_PERIOD"] = pd.to_numeric(data["TIME_PERIOD"], errors="coerce")

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, ""

    data = merge_with_codelist(data, data_structs, struct_id, "REF_AREA")
    data = merge_with_codelist(data, data_structs, struct_id, "DATA_SOURCE")

    source = ""
    if "_L_DATA_SOURCE" in data.columns:
        source = ", ".join(list(data["_L_DATA_SOURCE"].unique()))

    print("EDIT THE OPTIONS IN THE CFG OF AREAS")

    if fig_type == "bar":
        options["x"] = "_L_REF_AREA"
    elif fig_type == "line":
        options["color"] = "_L_REF_AREA"

    # TODO: Same code in MAIN: fix that
    options["labels"] = {"OBS_VALUE": "Value", "TIME_PERIOD": "Time"}
    for dim in data_structs[struct_id]["dsd"]["dims"]:
        dim_id = dim["id"]
        dim_lbl = get_col_name(struct_id, dim_id, data_structs)
        lbl_dim_id = dim_id
        # Is the column coded? Than get the label column (just ref_area)
        if "_L_" + dim_id in data.columns:
            lbl_dim_id = "_L_" + dim_id
            options["labels"][lbl_dim_id] = dim_lbl

    source_link = ""

    if (
        "label"
        in config["THEMES"][selections["theme"]][area]["data"][int(series_id[2])]
    ):
        indicator_name = config["THEMES"][selections["theme"]][area]["data"][
            int(series_id[2])
        ]["label"]
    else:

        indic_position = get_dim_position(data_structs, struct_id, "INDICATOR")
        code_id = series["dq"].split(".")[indic_position]

        indicator_name = get_code_from_structure(
            struct_id, data_structs, "INDICATOR", code_id
        )
        indicator_name = indicator_name["name"]

    # set the chart title, wrap the text when the indicator name is too long
    chart_title = textwrap.wrap(
        indicator_name,
        width=74,
    )
    chart_title = "<br>".join(chart_title)

    xaxis = {"categoryorder": "total descending"}
    if fig_type == "line":
        xaxis["tickformat"] = "d"
        # xaxis["dtick"]: 0
    # set the layout to center the chart title and change its font size and color
    layout = go.Layout(
        title=chart_title,
        title_x=0.5,
        font=dict(family="Arial", size=12),
        legend=dict(x=0.9, y=0.5),
        xaxis=xaxis,
    )

    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)

    if traces:
        fig.update_traces(**traces)

    if not source_link:  # is it none or empty?
        return fig, html.P(source)
    else:
        return fig, html.A(html.P(source), href=source_link, target="_blank")


# There is a lot of code shared with the area_figure function. Merge it!
# This callback is used to return data when the user clicks on the download CSV button
@callback(
    Output({"type": "down_csv", "index": MATCH}, "data"),
    [
        Input("store", "data"),
        Input({"type": "area_options", "index": MATCH}, "value"),
        Input({"type": "area_types", "index": MATCH}, "value"),
        Input({"type": "btn_down_csv", "index": MATCH}, "n_clicks"),
    ],
    [
        State("page_config", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def down_csv(
    selections,
    indicator,
    selected_type,
    n_clicks,
    config,
    id,
):

    # First render, do not trigger!
    if n_clicks is None:
        raise PreventUpdate

    data = download_data(selections, indicator, selected_type, config, id)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return dcc.send_data_frame(data.to_csv, "no_data.csv", index=False)

    return dcc.send_data_frame(data.to_csv, "data.csv", index=False)


"""
"""
# There is a lot of code shared with the area_figure function. Merge it!
# This callback is used to return data when the user clicks on the download CSV button
@callback(
    Output({"type": "down_exc", "index": MATCH}, "data"),
    [
        Input("store", "data"),
        Input({"type": "area_options", "index": MATCH}, "value"),
        Input({"type": "area_types", "index": MATCH}, "value"),
        Input({"type": "btn_down_exc", "index": MATCH}, "n_clicks"),
    ],
    [
        State("page_config", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def down_exc(
    selections,
    indicator,
    selected_type,
    n_clicks,
    config,
    id,
):
    # First render, do not trigger!
    if n_clicks is None:
        raise PreventUpdate

    data = download_data(selections, indicator, selected_type, config, id)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return dcc.send_data_frame(data.to_excel, "no_data.xlsx", index=False)

    return dcc.send_data_frame(data.to_excel, "data.xlsx", index=False)


def download_data(selections, indicator, selected_type, config, id):

    area = id["index"]
    series_id = indicator.split("|")
    series = config["THEMES"][selections["theme"]][area]["data"][int(series_id[2])]
    time_period = [min(selections["years"]), max(selections["years"])]

    default_graph = config["THEMES"][selections["theme"]][area].get(
        "default_graph", "line"
    )

    fig_type = selected_type if selected_type else default_graph

    lastnobs = None
    if fig_type == "bar":
        lastnobs = True
    data = get_data(
        series, years=time_period, labels="both", lastnobservations=lastnobs
    )

    return data
