import textwrap

import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash import callback, dcc, html
from dash.dependencies import MATCH, Input, Output, State, ALL
from dash_service.models import Page, Project, Dashboard

from dash_service.pages import get_data, years, get_geojson
from dash_service.pages import (
    add_structure,
    get_structure_id,
    get_code_from_structure_and_dq,
    get_col_name,
    merge_with_codelist,
    get_multilang_value,
    is_string_empty,
)

from flask import abort
from sqlalchemy import and_

from dash_service.components_aio.card_aio import CardAIO
from dash_service.components_aio.map_aio import MapAIO
from dash_service.components_aio.chart_aio import ChartAIO
from dash_service.components_aio.downloads_aio import DownloadsAIO
from dash_service.components_aio.heading_aio import HeadingAIO
from dash_service.components_aio.pages_navigation_aio import PagesNavigationAIO
from dash_service.components_aio.years_range_selector_aio import YearsRangeSelectorAIO

# pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)
# pd.set_option("display.width", 0)

# A few constant values
ID_INDICATOR = "INDICATOR"
ID_REF_AREA = "REF_AREA"
ID_OBS_VALUE = "OBS_VALUE"
ID_DATA_SOURCE = "DATA_SOURCE"
ID_TIME_PERIOD = "TIME_PERIOD"
LABEL_COL_PREFIX = "_L_"
DEFAULT_LABELS = ["OBS_VALUE", "TIME_PERIOD", "REF_AREA"]

ELEM_ID_PAGE_NAV = "PAGE_NAV"
ELEM_ID_YEARS_RANGE_SEL = "YEARS_RANGE_SEL"
ELEM_ID_CARDS = "CARDS"
ELEM_ID_MAIN = "MAIN"
ELEM_ID_CHARTS = "CHARTS"
ELEM_ID_HEADING = "HEADING"

CFG_N_THEMES = "THEMES"


# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = px.colors.qualitative.Dark24


# move this elsewhere
translations = {
    "sources": {"en": "Sources", "pt": "Fontes"},
    "years": {"en": "Years", "pt": "Anos"},
    "show_historical": {"en": "Show historical data", "pt": "Mostrar série histórica"},
    "bar": {"en": "Bar", "pt": "Gráfico em colunas"},
    "line": {"en": "Line", "pt": "Gráfico em linhas"},
    "scatter": {"en": "Scatter", "pt": "Scatter PT"},
    "download_excel": {"en": "Download Excel", "pt": "Download Excel"},
    "download_csv": {"en": "Download CSV", "pt": "Download CSV"},
    "OBS_VALUE": {"en": "Value", "pt": "Valores"},
    "TIME_PERIOD": {"en": "Time period", "pt": "Ano"},
    "REF_AREA": {"pt": "Estado"},
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

# Gets the element that will be rendered on the navigation bar
def get_page_nav_items(page_config, project_slug, lang):
    nav_type = None
    if "page_nav" in page_config and "type" in page_config["page_nav"]:
        nav_type = page_config["page_nav"]["type"]
    if nav_type is None:
        nav_type = "all"
    if nav_type == "all":
        nav_items = (
            Dashboard.query.with_entities(
                Dashboard.slug, Dashboard.title, Project.slug.label("prj_slug")
            )
            .join(Project)
            .filter(Project.slug == project_slug)
            .all()
        )

    ret = [
        {"name": ni.title, "prj_slug": ni.prj_slug, "slug": ni.slug, "lang": lang}
        for ni in nav_items
    ]
    return ret


# The entry point, retrieves the page from the storage and renderes the page
def layout(lang="en", **query_params):
    """
    Returns the page layout
    """

    project_slug = query_params.get("prj", None)
    page_slug = query_params.get("page", None)

    db_config = (
        Dashboard.query.join(Project)
        .filter(and_(Page.slug == page_slug, Project.slug == project_slug))
        .first()
    )

    page_config = db_config.content
    geography = db_config.geography

    nav_links = get_page_nav_items(page_config, project_slug, lang)

    return render_page_template(page_config, nav_links, geography, lang, query_params)


def render_themes() -> html.Div:
    return html.Div(
        className="d-flex justify-content-center",
        children=[dbc.ButtonGroup(id="theme_buttons")],
    )


def render_page_template(
    page_config: dict, nav_links: list, geojson: str, lang: str, query_params
) -> html.Div:

    elem_page_nav = None
    elem_main_title = None
    elem_years_selector = None

    if nav_links is not None and len(nav_links) > 0:
        elem_page_nav = PagesNavigationAIO(
            nav_links, query_params, aio_id=ELEM_ID_PAGE_NAV
        )

    if "main_title" in page_config:
        elem_main_title = HeadingAIO(page_config["main_title"], aio_id=ELEM_ID_HEADING)

    elem_years_selector = YearsRangeSelectorAIO(aio_id=ELEM_ID_YEARS_RANGE_SEL)

    ret = html.Div(
        [
            dcc.Store(id="lang", data=lang),  # stores the language
            dcc.Store(id="page_config", data=page_config),  # stores the page config
            dcc.Store(id="geoj", data=geojson),  # stores the geoJson
            dcc.Store(
                id="data_structures", data={}, storage_type="session"
            ),  # stores the data structure for caching
            dcc.Location(
                id="theme"
            ),  # controls the location hash (e.g. education#theme)
            elem_page_nav,
            elem_main_title,
            html.Div(
                className="bg-light mt-2",
                children=[
                    html.Div(className="p-2", children=[render_themes()]),
                    html.Div(
                        className="mt-2",
                        children=[
                            html.Span(
                                className="d-flex justify-content-center badge rounded-pill bg-primary",
                                children=get_multilang_value(
                                    translations["years"], lang
                                ),
                            ),
                            html.Span(children=elem_years_selector),
                        ],
                    ),
                ],
            ),
        ]
    )

    return ret


# Updates the Subtitle
@callback(
    Output(HeadingAIO.ids.subtitle(ELEM_ID_HEADING), "children"),
    Output("theme_buttons", "children"),
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
