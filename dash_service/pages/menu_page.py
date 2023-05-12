# https://dash.plotly.com/dash-ag-grid

from dash import callback, dcc, html
from dash.exceptions import PreventUpdate
from dash_service.models import MenuPage, Project
from dash.dependencies import MATCH, Input, Output, State, ALL


import dash_bootstrap_components as dbc

from dash_service.components_aio.pages_navigation_aio import PagesNavigationAIO
from dash_service.components_aio.heading_aio import HeadingAIO


def layout(lang="en", **query_params):

    project_slug = query_params.get("prj", None)
    page_slug = query_params.get("page", None)

    if project_slug is None or page_slug is None:
        # return render_page_template({}, "Validation Page", [], "", lang)
        return render_no_menupage_cfg_found(project_slug, page_slug)

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    menupage = MenuPage.where(
        project___slug=project_slug, slug=page_slug
    ).first_or_404()

    config = menupage.content
    t = menupage.title

    return render_page_template(config, lang)


def render_no_menupage_cfg_found(prj, page):
    if prj is None:
        err = "No page found, prj parameter needed, e.g. prj=rosa"
    if page is None:
        err = "No page found, page parameter needed, e.g. page=rosa_de"
    if prj is not None and page is not None:
        err = f"No page found for parameters prj={prj}&page={page}"
    template = html.Div(
        children=dbc.Col(
            [
                dbc.Row(html.H3(err)),
            ]
        ),
    )
    return template


_color_maps = {
    "purple": {"c": "#561e60", "s": "#eeeaf1"},
    "green": {"c": "#3e7c4b", "s": "#ebf2ed"},
    "light_blue": {"c": "#4d8bba", "s": "#ebeff2"},
    "red": {"c": "#861b3e", "s": "#f2ebed"},
    "blue": {"c": "#38558e", "s": "#ebedf2"},
    "yellow": {"c": "#e4af4f", "s": "#f2f0eb"},
    "orange": {"c": "#ec5e23", "s": "#f2edeb"},
}


def _create_button(link, color=None):
    icon_class = link["icon"] + " fa-lg mt-2 mb-3"
    href = ""
    if "link" in link:
        href=link["link"]

    btn = html.A(
        className="btn p-2 m-3 text-white",
        style={
            "width":"170px",
            "height":"130px",
            "backgroundColor": color,
        },
        children=[
            html.I(className=icon_class),
            # html.Div(className="text-truncate", children=link["title"]),
            html.Div(children=link["title"]),
        ],
        href=href
    )
    ret = html.Div(className="m-2 d-inline", children=btn)
    return ret


def create_links_row(row):
    ch = []
    color = "blue"
    secondary = "white"
    if "color" in row and row["color"] in _color_maps:
        color = _color_maps[row["color"]]["c"]
        secondary = _color_maps[row["color"]]["s"]

    cardHeader = None

    if "title" in row:
        cardHeader = html.Div(
            className="card-header fs-4 fw-bold",
            style={"backgroundColor": secondary, "color": color},
            children=row["title"],
        )

    if "links" in row:
        links_div = []
        for l in row["links"]:
            lnk = _create_button(l, color)
            links_div.append(lnk)
        ch.append(
            #html.Div(className="row col-sm-12 col-md-8 d-inline", children=links_div)
            html.Div(className="text-center", children=links_div)
        )

    row_card = html.Div(
        className="card mb-3",
        style={"backgroundColor": secondary},
        children=[cardHeader, html.Div(className="card-body", children=ch)],
    )

    return row_card


def render_page_template(
    page_config: dict,
    lang,
    **kwargs,
) -> html.Div:
    """Renders the page template based on the page config and other parameters

    Args:
        config (dict): config from the database

    Returns:
        html.Div: The dash Div representing the redenderd page against the config
    """

    print(page_config)

    if "main_title" in page_config:
        elem_main_title = HeadingAIO(page_config["main_title"], aio_id="menu_page_head")

    row_elems = []

    for row in page_config["ROWS"]:
        row_div = create_links_row(row)
        row_elems.append(row_div)

    #template = html.Div(className="row col-sm-12",children=[elem_main_title] + row_elems)
    template = html.Div(className="row justify-content-center",children=html.Div(className="col-sm-12 col-xxl-10",children=[elem_main_title] + row_elems))

    return template
