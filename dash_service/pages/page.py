import textwrap

import dash
import dash_bootstrap_components as dbc
import dash_treeview_antd
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash import callback, dcc, html
from dash.dependencies import MATCH, ClientsideFunction, Input, Output, State
from dash_service.components import fa
from dash_service.models import Page, Project
from dash_service.pages import (
    geo_json_countries,
    get_codelist,
    get_col_unique,
    get_dataset,
    get_search_countries,
    get_selection_tree,
    years,
)
from scipy.stats import zscore

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
    if project_slug is None and page_slug is None:
        # project_slug and page_slug are None when this is called for validation
        # create a dummy page
        return render_page_template(
            {},
            "Validation Page",
            {"data": dict(title="Select All", key="0", children=[]), "checked": [0]},
        )

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    page = Page.where(project___slug=project_slug, slug=page_slug).first_or_404()
    config = page.content
    main_title = config["main_title"]
    selection_tree = get_selection_tree(config["ddl_ref_areas_cl"])

    return render_page_template(config, main_title, selection_tree)


def render_page_template(
    page_config: dict, main_title: str, selection_tree: dict, **kwargs
) -> html.Div:
    """Renders the page template based on the page config and other parameters

    Args:
        page_config (dict): page config from the database
        main_title (_type_): main title of the page
        selection_tree (_type_): Geographical selection tree the user can select

    Returns:
        html.Div: The dash Div representing the redenderd page against the config
    """
    template = html.Div(
        [
            dcc.Store(id="page_config", data=page_config),
            dcc.Location(id="theme"),
            html.Div(
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
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            dbc.Row(
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
                                style={"verticalAlign": "center", "display": "flex"},
                            ),
                            dbc.Row(
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
                                                        index: str(year)
                                                        for index, year in enumerate(
                                                            years
                                                        )
                                                    },
                                                    value=[0, len(years) - 1],
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                    "minWidth": "500px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                    dbc.DropdownMenu(
                                        label=f"{translations[lang]['REF_AREA']}: {'len(countries)'}",
                                        id="collapse-countries-button",
                                        className="m-2",
                                        color="info",
                                        style={"display": "block"},
                                        children=[
                                            dbc.Card(
                                                dash_treeview_antd.TreeView(
                                                    id="country_selector",
                                                    multiple=True,
                                                    checkable=True,
                                                    checked=selection_tree["checked"],
                                                    expanded=selection_tree["checked"],
                                                    data=selection_tree["data"],
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                ],
                                id="filter-row",
                                justify="center",
                            ),
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
        ],
    )
    return template


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
                    dcc.Loading([dcc.Graph(id=area_id)]),
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
                    dbc.PopoverHeader(
                        html.A(
                            html.P(f"Sources: {indicator_sources}"),
                            href=source_link,
                            target="_blank",
                        )
                    ),
                    dbc.PopoverBody(
                        dcc.Markdown(get_card_popover_body(numerator_pairs))
                    ),
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


@callback(
    Output("store", "data"),
    # Output("country_selector", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
    ],
    State("page_config", "data"),
)
def apply_filters(
    theme,
    years_slider,
    country_selector,
    store_page_config,
):

    theme = (
        theme[1:].upper() if theme else next(iter(store_page_config["THEMES"].keys()))
    )

    selected_years = years[years_slider[0] : years_slider[1] + 1]
    selected_country_codes = [
        code for code in country_selector if code != "0"
    ]  # Exclude the Select all code

    selections = dict(
        theme=theme,
        years=selected_years,
        countries=selected_country_codes,
    )

    return (
        selections,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        f"{translations[lang]['REF_AREA']}: {str(len(selected_country_codes))} selected",
    )


def indicator_card(
    card_id,
    name,
    suffix,
    config,
):
    df_vals = get_dataset(config)
    card_value = ""
    if len(df_vals) > 0:
        card_value = df_vals.iloc[0]["OBS_VALUE"]

    return make_card(
        card_id, name, suffix, "Indicator sources", "Source link", card_value, []
    )


@callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("cards_row", "children"), State("page_config", "data")],
)
def show_cards(selections, current_cards, page_config):
    cards = [
        indicator_card(
            f"card-{num}",
            card["name"],
            card["suffix"],
            card["data"],
        )
        for num, card in enumerate(page_config["THEMES"][selections["theme"]]["CARDS"])
    ]

    return cards


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
    ],
)
def set_options(selection, config, id):
    area = id["index"]

    area_options = area_types = []

    cl_indicators = get_codelist("BRAZIL_CO", "CL_BRAZILCO_INDICATORS")
    area_options = []
    default_option = ""

    if area in config["THEMES"][selection["theme"]]:
        api_params = config["THEMES"][selection["theme"]][area].get("data")

        area_options = []

        for idx, ap in enumerate(api_params):
            if "label" in ap:
                lbl = ap["label"]
            else:
                indic = next(
                    item
                    for item in cl_indicators
                    if item["id"] == ap["dq"]["INDICATOR"]
                )
                lbl = indic["name"]
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
    ],
)
def main_figure(indicator, show_historical_data, selections, config):
    latest_data = not show_historical_data

    options = config["THEMES"][selections["theme"]]["MAIN"]["options"]

    series_id = indicator.split("|")
    series = config["THEMES"][series_id[0]][series_id[1]]["data"][int(series_id[2])]
    # series = config["THEMES"][selections["theme"]]["MAIN"]["data"]
    time_period = [min(selections["years"]), max(selections["years"])]
    ref_areas = selections["countries"]

    cl_countries = get_codelist("BRAZIL_CO", "CL_BRAZIL_REF_AREAS")
    cl_units = get_codelist("UNICEF", "CL_UNIT_MEASURE")

    if latest_data:
        data = get_dataset(series, recent_data=True, countries=ref_areas)
    else:
        data = get_dataset(series, years=time_period, countries=ref_areas)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, ""

    df_countries = pd.DataFrame(columns=["name", "id"], data=cl_countries)
    df_units = pd.DataFrame(columns=["name", "id"], data=cl_units)

    data = data.merge(df_countries, how="left", left_on="REF_AREA", right_on="id")
    # data = data.drop(columns=["id"])
    # data = data.rename(columns={"name":"REF_AREA_NAME"})
    # data = data.merge(cl_units, how="left", left_on="UNIT_MEASURE", right_on="id")

    DEFAULT_LABELS = {
        "REF_AREA": "Geographic area",
        "INDICATOR": "Indicator",
        "AGE": "Current age",
        "EDUCATION_LEVEL": "Education level",
        "TIME_PERIOD": "Time period",
    }

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = "Value"
    options["labels"]["text"] = "OBS_VALUE"
    options["geojson"] = geo_json_countries

    # TODO this code seems to be duplicated in area_figure, merge the code
    source = ""
    sources = get_col_unique(data, "DATA_SOURCE")
    if len(sources) > 0:
        source = ", ".join(sources)

    main_figure = px.choropleth_mapbox(data, **options)
    main_figure.update_layout(margin={"r": 0, "t": 1, "l": 2, "b": 1})

    source_link = ""
    return main_figure, html.A(html.P(source), href=source_link, target="_blank")


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
):
    # only run if indicator not empty
    if not indicator:
        return {}, {}

    area = id["index"]
    series_id = indicator.split("|")
    series = config["THEMES"][selections["theme"]][area]["data"][int(series_id[2])]
    time_period = [min(selections["years"]), max(selections["years"])]
    ref_areas = selections["countries"]

    default_graph = config["THEMES"][selections["theme"]][area].get(
        "default_graph", "line"
    )
    fig_type = selected_type if selected_type else default_graph
    fig_config = config["THEMES"][selections["theme"]][area]["graphs"][fig_type]
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")
    dimension = False if fig_type == "line" or compare == "TOTAL" else compare

    if fig_type == "line":
        data = get_dataset(series, years=time_period, countries=ref_areas)
    else:
        data = get_dataset(series, recent_data=True, countries=ref_areas)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, ""

    cl_countries = get_codelist("BRAZIL_CO", "CL_BRAZIL_REF_AREAS")
    df_countries = pd.DataFrame(columns=["name", "id"], data=cl_countries)
    df_countries = df_countries.rename(columns={"name": "REF_AREA_l"})

    data = data.merge(df_countries, how="left", left_on="REF_AREA", right_on="id")

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, ""

    # TODO this code seems to be duplicated in main_figure, merge the code
    source = ""
    sources = get_col_unique(data, "DATA_SOURCE")
    if len(sources) > 0:
        source = ", ".join(sources)

    source_link = ""

    DEFAULT_LABELS = {
        "REF_AREA": "Geographic area",
        "INDICATOR": "Indicator",
        "AGE": "Current age",
        "EDUCATION_LEVEL": "Education level",
        "TIME_PERIOD": "Time period",
        "REF_AREA_l": "Geographic area",
    }

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = "Value"
    options["labels"]["text"] = "OBS_VALUE"

    if (
        "label"
        in config["THEMES"][selections["theme"]][area]["data"][int(series_id[2])]
    ):
        indicator_name = config["THEMES"][selections["theme"]][area]["data"][
            int(series_id[2])
        ]["label"]
    else:
        cl_indicators = get_codelist("BRAZIL_CO", "CL_BRAZILCO_INDICATORS")
        ind = list(data["INDICATOR"].unique())[0]
        indicator_name = next(item for item in cl_indicators if item["id"] == ind)
        indicator_name = indicator_name["name"]

    # cl_countries = get_codelist("BRAZIL_CO", "CL_BRAZIL_REF_AREAS")
    # set the chart title, wrap the text when the indicator name is too long
    chart_title = textwrap.wrap(
        indicator_name,
        width=74,
    )
    chart_title = "<br>".join(chart_title)

    # set the layout to center the chart title and change its font size and color
    layout = go.Layout(
        title=chart_title,
        title_x=0.5,
        font=dict(family="Arial", size=12),
        legend=dict(x=0.9, y=0.5),
        xaxis={"categoryorder": "total descending"},
    )

    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)
    if traces:
        fig.update_traces(**traces)

    return fig, html.A(html.P(source), href=source_link, target="_blank")
