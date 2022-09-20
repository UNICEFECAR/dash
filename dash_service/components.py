import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from . import default_settings
from .utils import component, get_url


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"{className} mx-1")


@component
def make_brand(**kwargs):
    return html.Header(
        className="unicef-logo",
        children=[
            html.Div(
                className="unicef-logo__image",
                children=html.Img(
                    src="assets/logo-unicef-large.svg",
                ),
            ),
            html.P(
                className="unicef-logo__heading",
                children=[
                    fa("far fa-chart-bar"),
                    html.Strong(
                        default_settings.TITLE,
                        style={"fontSize": "medium"},
                    ),
                    html.Span(default_settings.SUB_TITLE),
                ],
            ),
        ],
    )


@component
def make_nav(vertical=False, **kwargs):
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
                                    for page in dash.page_registry.values()
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
