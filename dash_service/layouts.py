"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances.
"""

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from .components import make_brand, make_nav
from .components import fa


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(make_brand(), width="auto"),
                    dbc.Col(make_nav(vertical=False), width="auto"),
                ],
                id="header",
                className="bg-dark justify-content-between align-items-center",
            ),
            dbc.Container(dbc.Row(dbc.Col(dash.page_container)), fluid=True),
        ]
    )


def main_layout_sidebar():
    """Dash layout with a sidebar"""
    return html.Div(
        [
            dbc.Container(
                fluid=True,
                children=dbc.Row(
                    [
                        dbc.Col(
                            [make_brand(), make_nav(vertical=True)],
                            width=2,
                            className="px-0 bg-dark",
                            style={"height": "100vh"},
                            id="sidebar",
                        ),
                        dbc.Col(dash.page_container, width=10),
                    ]
                ),
            ),
        ]
    )


def main_default_layout():

    return html.Div(
        [
            make_nav(),
            html.Br(),
            dcc.Store(id="store"),
            dbc.Container(
                fluid=True,
                children=[
                    dbc.Col(dash.page_container),
                ],
            ),
            # make_footer(),
            html.Button(
                id="btnScroll",
                title="Scroll to top",
                className="btn btn-dark scroll-top",
                children=[
                    fa("fas fa-chevron-up"),
                ],
                style={
                    "border-radius": 50,
                    "position": "fixed",
                    "right": 20,
                    "bottom": 20,
                    "z-index": 1101,
                    "width": 50,
                    "height": 50,
                    "padding": 12,
                    "border": 0,
                    "display": "none",
                },
            ),
        ],
        id="mainContainer",
    )
