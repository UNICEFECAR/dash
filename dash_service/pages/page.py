import textwrap

import dash
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash import callback, dcc, html
from dash.dependencies import MATCH, Input, Output, State, ALL
from dash_service.components import fa
from dash_service.models import Page, Project

from dash_service.pages import get_data, years, get_geojson
from dash_service.pages import (
    add_structure,
    get_structure_id,
    get_code_from_structure_and_dq,
    get_col_name,
    merge_with_codelist,
)

from flask import abort

# from ..components.card_aio import CardAIO
from dash_service.components_aio.card_aio import CardAIO
from dash_service.components_aio.map_aio import MapAIO
from dash_service.components_aio.chart_aio import ChartAIO
from dash_service.components_aio.downloads_aio import DownloadsAIO

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 0)

ID_INDICATOR = "INDICATOR"
ID_REF_AREA = "REF_AREA"
ID_OBS_VALUE = "OBS_VALUE"
ID_DATA_SOURCE = "DATA_SOURCE"
ID_TIME_PERIOD = "TIME_PERIOD"
LABEL_COL_PREFIX = "_L_"
DEFAULT_LABELS = {"OBS_VALUE": "Value", "TIME_PERIOD": "Time"}

ELEM_ID_MAIN = "MAIN"

CFG_N_THEMES = "THEMES"


# The store, data input/output used in callbacks is defined in "layouts.py", it holds the selection: years, country...


# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = px.colors.qualitative.Dark24

# TODO: language shouold be read from a param if forced or from the browser
lang = "en"
# move this elsewhere
translations = {
    "en": {"sources": "sources"},
    "pt": {"sources": "sources [PT]"},
}

# the configuration of the "Download plot" button in the charts
cfg_plot = {
    "toImageButtonOptions": {
        "format": "png",  # one of png, svg, jpeg, webp
        "filename": "plot",
        "width": 1200,
        "height": 800,
        "scale": 1,  # Multiply title/legend/axis/canvas sizes by this factor
    },
    "displayModeBar": True,
    "displaylogo": False,
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
                            [
                                MapAIO(
                                    ELEM_ID_MAIN,
                                    plot_cfg=cfg_plot,
                                    info_title=translations[lang]["sources"],
                                )
                            ],
                            style={"display": "block"},
                        ),
                        html.Br(),
                        html.Div(
                            id="div_charts", className="row row-cols-1 row-cols-lg-2"
                        ),
                        # Test automation (Selenium) handle
                        html.Div(
                            id="_page_load", children=[], style={"display": "none"}
                        ),
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


# Triggered when the theme or year slider changes
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
        theme[1:].upper()
        if theme
        else next(iter(store_page_config[CFG_N_THEMES].keys()))
    )

    selected_years = years[years_slider[0] : years_slider[1] + 1]

    selections = dict(theme=theme, years=selected_years)

    return (selections, f"Years: {selected_years[0]} - {selected_years[-1]}")


@callback(
    Output("data_structures", "data"),
    [Input("store", "data")],
    [State("page_config", "data")],
)
# Downloads all the DSD for the data.
# Tipically 1 dataflow per page but can handle data from multiple Dataflows in 1 page
def download_structures(selections, page_config):
    data_structures = {}

    theme_node = page_config[CFG_N_THEMES][selections["theme"]]

    # cards
    for card in theme_node["CARDS"]:
        add_structure(data_structures, card["data"])

    # Main
    if "MAIN" in theme_node and "data" in theme_node["MAIN"]:
        for data_node in theme_node["MAIN"]["data"]:
            add_structure(data_structures, data_node)

    # areas
    if "CHARTS" in theme_node:
        for chart in theme_node["CHARTS"]:
            if "data" in chart:
                for data_node in chart["data"]:
                    add_structure(data_structures, data_node)

    return data_structures


# this callback updates on selection changed: it needs the selected page
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
        theme_key = list(config[CFG_N_THEMES].keys())[0]
        theme = config[CFG_N_THEMES][theme_key]
    else:
        theme_key = selections["theme"]
        theme = config[CFG_N_THEMES][selections["theme"]]

    subtitle = theme.get("NAME")

    # hide the buttons when only one option is available
    if len(config[CFG_N_THEMES].items()) == 1:
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
        for num, (key, value) in enumerate(config[CFG_N_THEMES].items())
    ]
    return subtitle, buttons


@callback(
    Output("cards_row", "children"),
    [Input("data_structures", "data")],
    [State("store", "data"), State("page_config", "data")],
)
def show_cards(data_struct, selections, page_config):
    selected_theme = selections["theme"]
    cards = []
    for num, card in enumerate(page_config[CFG_N_THEMES][selected_theme]["CARDS"]):
        config = card["data"]
        value = "-"
        data_source = ""

        # if suffix has not been overridden pull it from the indicator
        if card["suffix"] is None:
            suffix = get_code_from_structure_and_dq(data_struct, config, ID_INDICATOR)[
                "name"
            ]
        else:
            suffix = card["suffix"]

        # we jsut need the most recent datapoint, no labels, just the value
        df = get_data(config, lastnobservations=1, labels="id")
        if len(df) > 0:
            value = df.iloc[0][ID_OBS_VALUE]
            if ID_DATA_SOURCE in df.columns:
                data_source = df.iloc[0][ID_DATA_SOURCE]

        info_head = translations[lang]["sources"]
        cards.append(
            CardAIO(
                aio_id=f"card-{num}",
                value=value,
                suffix=suffix,
                info_head=info_head,
                info_body=data_source,
            )
        )

    return cards


@callback(
    Output("div_charts", "children"),
    [Input("data_structures", "data")],
    [State("store", "data"), State("page_config", "data")],
)
def show_charts(data_struct, selections, page_config):
    charts_count = 0
    selected_theme = selections["theme"]
    if "CHARTS" in page_config[CFG_N_THEMES][selected_theme]:
        charts_count = len(page_config[CFG_N_THEMES][selected_theme]["CHARTS"])

    charts = [
        ChartAIO(
            aio_id=f"CHART_{i}",
            plot_cfg=cfg_plot,
            info_title=translations[lang]["sources"],
        )
        for i in range(charts_count)
    ]

    return charts


# Triggered when the selection changes. Updates the main area ddl.
@callback(
    Output(MapAIO.ids.card_title(ELEM_ID_MAIN), "children"),
    Output(MapAIO.ids.ddl(ELEM_ID_MAIN), "options"),
    Output(MapAIO.ids.ddl(ELEM_ID_MAIN), "value"),
    Input("data_structures", "data"),
    [
        State("store", "data"),
        State("page_config", "data"),
    ],
)
def set_options_main(data_structures, selection, config):
    selected_theme = selection["theme"]

    # The main area title
    name = ""
    main_node = config[CFG_N_THEMES][selected_theme].get(ELEM_ID_MAIN, None)
    if main_node is not None and "name" in main_node:
        name = main_node["name"]

    # Find the data nodes to fill the ddl
    ddl_items = []
    default_item = ""
    if (
        ELEM_ID_MAIN in config[CFG_N_THEMES][selected_theme]
        and "data" in config[CFG_N_THEMES][selected_theme][ELEM_ID_MAIN]
    ):
        data_configs = config[CFG_N_THEMES][selected_theme][ELEM_ID_MAIN]["data"]
        for idx, data_cfg in enumerate(data_configs):
            # Is it there a label? Then override the title contained in the codelist
            if "label" in data_cfg:
                lbl = data_cfg["label"]
            else:
                lbl = get_code_from_structure_and_dq(
                    data_structures, data_cfg, ID_INDICATOR
                )["name"]
            # key = f"{selected_theme}|MAIN|{str(idx)}"
            key = str(idx)
            if idx == 0:
                default_item = key
            ddl_items.append({"label": lbl, "value": key})

    # return name, area_options, area_types, default_option, default_graph
    return name, ddl_items, default_item


# Triggered when the Map area changes: show historical data is changed or indicator selected
@callback(
    Output(MapAIO.ids.graph(ELEM_ID_MAIN), "figure"),
    Output(MapAIO.ids.info_text(ELEM_ID_MAIN), "children"),
    Output(MapAIO.ids.info_icon(ELEM_ID_MAIN), "style"),
    [
        Input(MapAIO.ids.ddl(ELEM_ID_MAIN), "value"),
        Input(MapAIO.ids.toggle_historical(ELEM_ID_MAIN), "value"),
        Input("data_structures", "data"),
    ],
    [
        State("store", "data"),
        State("page_config", "data"),
        State("geoj", "data"),
    ],
)
def main_figure(
    ddl_value, show_historical_data, data_structs, selections, config, geoj
):

    # find the data node in the configuration for the user's selection
    current_theme = selections["theme"]
    data_cfg = config[CFG_N_THEMES][current_theme][ELEM_ID_MAIN]["data"][int(ddl_value)]

    time_period = [min(selections["years"]), max(selections["years"])]

    lastnobs = None
    if not show_historical_data:
        lastnobs = 1

    df = get_data(data_cfg, years=time_period, lastnobservations=lastnobs)
    if df.empty:
        return EMPTY_CHART, ""

    # we need the ref_area and data source codelists (DATA_SOURCE can be coded)
    # get and merge the ref area labels
    struct_id = get_structure_id(data_cfg)
    df = merge_with_codelist(df, data_structs, struct_id, ID_REF_AREA)
    df = merge_with_codelist(df, data_structs, struct_id, ID_DATA_SOURCE)
    df[ID_OBS_VALUE] = pd.to_numeric(df[ID_OBS_VALUE])

    # The data sources
    source = ""
    display_source = {"display": "none"}
    if LABEL_COL_PREFIX + ID_DATA_SOURCE in df.columns:
        source = ", ".join(list(df[LABEL_COL_PREFIX + ID_DATA_SOURCE].unique()))
    if source != "":
        display_source = {"display": "visible"}

    # Add the labels for all the dimensions
    options = config[CFG_N_THEMES][current_theme][ELEM_ID_MAIN]["options"]
    options["labels"] = DEFAULT_LABELS.copy()
    for dim in data_structs[struct_id]["dsd"]["dims"]:
        dim_id = dim["id"]
        dim_lbl = get_col_name(data_structs, struct_id, dim_id)
        lbl_dim_id = dim_id
        # Is the column coded? Than get the label column (just ref_area)
        if LABEL_COL_PREFIX + dim_id in df.columns:
            lbl_dim_id = LABEL_COL_PREFIX + dim_id
            options["labels"][lbl_dim_id] = dim_lbl

    # the geoJson
    options["geojson"] = get_geojson(geoj)
    main_figure = px.choropleth_mapbox(df, **options)
    main_figure.update_layout(margin={"r": 0, "t": 1, "l": 2, "b": 1})

    return main_figure, source, display_source


# Triggered when the selection changes. Updates the charts ddls.
@callback(
    Output(ChartAIO.ids.card_title(MATCH), "children"),
    Output(ChartAIO.ids.ddl(MATCH), "options"),
    Output(ChartAIO.ids.ddl(MATCH), "value"),
    Output(ChartAIO.ids.chart_types(MATCH), "options"),
    Output(ChartAIO.ids.chart_types(MATCH), "value"),
    Input("data_structures", "data"),
    [
        State("store", "data"),
        State("page_config", "data"),
        State(ChartAIO.ids.card_title(MATCH), "id"),
    ],
)
def set_options_charts(data_structures, selection, config, component_id):
    selected_theme = selection["theme"]

    # The card index
    chart_idx = int(component_id["aio_id"].split("_")[1])
    chart_cfg = config[CFG_N_THEMES][selected_theme]["CHARTS"][chart_idx]
    card_title = chart_cfg["name"]

    # Find the data nodes to fill the ddl
    ddl_items = []
    default_item = ""
    if "data" in chart_cfg:
        data_configs = chart_cfg["data"]
        for idx, data_cfg in enumerate(data_configs):
            # Is it there a label? Then override the title contained in the codelist
            if "label" in data_cfg:
                lbl = data_cfg["label"]
            else:
                lbl = get_code_from_structure_and_dq(
                    data_structures, data_cfg, ID_INDICATOR
                )["name"]
            key = str(idx)
            if idx == 0:
                default_item = key
            ddl_items.append({"label": lbl, "value": key})
    # the chart types
    chart_types = []

    if "graphs" in chart_cfg:
        chart_types = [
            {"label": type_key.capitalize(), "value": type_key}
            for type_key in chart_cfg["graphs"].keys()
        ]
    default_graph = chart_cfg.get("default_graph", "")

    return card_title, ddl_items, default_item, chart_types, default_graph


# Triggered when the selection changes. Updates the charts.
@callback(
    Output(ChartAIO.ids.chart(MATCH), "figure"),
    Output(ChartAIO.ids.info_text(MATCH), "children"),
    Output(ChartAIO.ids.info_icon(MATCH), "style"),
    [
        Input(ChartAIO.ids.ddl(MATCH), "value"),
        Input(ChartAIO.ids.chart_types(MATCH), "value"),
    ],
    [
        State("data_structures", "data"),
        State("store", "data"),
        State("page_config", "data"),
        State(ChartAIO.ids.card_title(MATCH), "id"),
    ],
)
def update_charts(
    ddl_value, chart_type, data_structures, selection, config, component_id
):
    selected_theme = selection["theme"]
    chart_idx = int(component_id["aio_id"].split("_")[1])
    chart_cfg = config[CFG_N_THEMES][selected_theme]["CHARTS"][chart_idx]

    # find the data node in the configuration for the user's selection
    data_cfg = chart_cfg["data"][int(ddl_value)]
    time_period = [min(selection["years"]), max(selection["years"])]
    if chart_type is None or chart_type == "":
        chart_type = chart_cfg.get(["default_graph"], "bar")

    fig_config = chart_cfg["graphs"][chart_type]
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")

    struct_id = get_structure_id(data_cfg)
    if chart_type == "line":
        df = get_data(data_cfg, years=time_period)
    else:
        df = get_data(data_cfg, years=time_period, lastnobservations=1)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if df.empty:
        return EMPTY_CHART, ""

    df[ID_OBS_VALUE] = pd.to_numeric(df[ID_OBS_VALUE], errors="coerce")
    df[ID_TIME_PERIOD] = pd.to_numeric(df[ID_TIME_PERIOD], errors="coerce")

    df = merge_with_codelist(df, data_structures, struct_id, ID_REF_AREA)
    df = merge_with_codelist(df, data_structures, struct_id, ID_DATA_SOURCE)

    source = ""
    display_source = {"display": "none"}
    if LABEL_COL_PREFIX + ID_DATA_SOURCE in df.columns:
        source = ", ".join(list(df[LABEL_COL_PREFIX + ID_DATA_SOURCE].unique()))
    if source != "":
        display_source = {"display": "visible"}

    options_to_check_for_label = ["x", "y", "text", "color", "hover_name"]
    for o in options_to_check_for_label:
        if o in options and LABEL_COL_PREFIX + options[o] in df.columns:
            options[o] = LABEL_COL_PREFIX + options[o]

    options["labels"] = options["labels"] = DEFAULT_LABELS.copy()
    for dim in data_structures[struct_id]["dsd"]["dims"]:
        dim_id = dim["id"]
        dim_lbl = get_col_name(data_structures, struct_id, dim_id)
        lbl_dim_id = dim_id
        # Is the column coded? Than get the label column (just ref_area)
        if LABEL_COL_PREFIX + dim_id in df.columns:
            lbl_dim_id = LABEL_COL_PREFIX + dim_id
            options["labels"][lbl_dim_id] = dim_lbl

    if "label" in chart_cfg["data"][int(ddl_value)]:
        indicator_name = chart_cfg["data"][int(ddl_value)]["label"]
    else:
        indicator_name = get_code_from_structure_and_dq(
            data_structures, data_cfg, ID_INDICATOR
        )["name"]

    # set the chart title, wrap the text when the indicator name is too long
    chart_title = textwrap.wrap(
        indicator_name,
        width=74,
    )
    chart_title = "<br>".join(chart_title)
    xaxis = {"categoryorder": "total descending"}
    if chart_type == "line":
        xaxis["tickformat"] = "d"
        # xaxis["dtick"]: 0
    # set the layout to center the chart title and change its font size and color
    layout = go.Layout(
        title=chart_title,
        title_x=0.5,
        font=dict(family="Arial", size=12),
        legend=dict(x=0.9, y=0.5),
        xaxis=xaxis,
        modebar={"orientation": "v"},
    )

    fig = getattr(px, chart_type)(df, **options)
    fig.update_layout(layout)

    if traces:
        fig.update_traces(**traces)

    chart_idx = int(component_id["aio_id"].split("_")[1])

    return fig, source, display_source


# Data downloads

# TODO There is a lot of code shared with the area_figure function. Merge it!
# This callback is used to return data when the user clicks on the download CSV button
@callback(
    Output(DownloadsAIO.ids.dcc_down_excel(MATCH), "data"),
    # reset the n_clicks after each click to prevent triggering at each theme change
    Output(DownloadsAIO.ids.btn_down_excel(MATCH), "n_clicks"),
    Output(DownloadsAIO.ids.btn_down_csv(MATCH), "n_clicks"),
    [
        Input(DownloadsAIO.ids.btn_down_excel(MATCH), "n_clicks"),
        Input(DownloadsAIO.ids.btn_down_csv(MATCH), "n_clicks"),
    ],
    [
        Input("store", "data"),
        State("page_config", "data"),
        State(DownloadsAIO.ids.btn_down_excel(MATCH), "id"),
        State(MapAIO.ids.ddl(ELEM_ID_MAIN), "value"),
        State(ChartAIO.ids.ddl(ALL), "value"),
        State(ChartAIO.ids.chart_types(ALL), "value"),
    ],
)
def download_data(
    n_clicks_excel,
    n_clicks_csv,
    selections,
    page_cfg,
    source_element,
    map_selection,
    chart_selection,
    chart_type,
):

    source_id = source_element["aio_id"]
    # # First render, do not trigger!
    if n_clicks_excel is None and n_clicks_csv is None:
        raise PreventUpdate

    df = download_data(
        selections, page_cfg, source_id, map_selection, chart_selection, chart_type
    )
    print("n_clicks_excel")
    print(n_clicks_excel)
    print("n_clicks_csv")
    print(n_clicks_csv)

    #Excel clicked
    if n_clicks_excel is not None:
        return dcc.send_data_frame(df.to_excel, "data.xlsx", index=False), None, None
    elif n_clicks_csv is not None:
        return dcc.send_data_frame(df.to_csv, "data.csv", index=False), None, None
    


# def download_data(selections, indicator, selected_type, config, id):
def download_data(selections, page_cfg, source_id, map_sel, chart_sel, chart_type):

    data_node = None
    if source_id.startswith("CHART_"):
        chart_idx = int(source_id.split("_")[1])
        theme_node = page_cfg[CFG_N_THEMES][selections["theme"]]["CHARTS"][chart_idx]
        data_node_idx = int(chart_sel[chart_idx])
        data_node = theme_node["data"][data_node_idx]
        chart_type = chart_type[chart_idx]
    elif source_id == (ELEM_ID_MAIN):
        theme_node = page_cfg[CFG_N_THEMES][selections["theme"]][ELEM_ID_MAIN]
        data_node = theme_node["data"][int(map_sel)]

    time_period = [min(selections["years"]), max(selections["years"])]

    lastnobs = None
    if chart_type == "bar":
        lastnobs = True
    data = get_data(
        data_node, years=time_period, labels="both", lastnobservations=lastnobs
    )

    return data


@callback(
    Output("_page_load", "children"),
    [Input("data_structures", "data")],
)
def page_loaded(data_struct):
    return [html.Div(id="_page_load_ok")]
