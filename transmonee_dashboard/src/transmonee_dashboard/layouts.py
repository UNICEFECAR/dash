"""Contains layouts suitable for being the value of the 'layout' attribute of
Dash app instances.
"""

from flask import current_app as server
from dash import dcc, html
import dash_bootstrap_components as dbc

from .components import make_footer, make_header, make_sidebar
from .components import fa


def main_layout_header():
    """Dash layout with a top-header"""
    return html.Div(
        [
            make_header(),
            dbc.Container(
                dbc.Row(dbc.Col(id=server.config["CONTENT_CONTAINER_ID"])), fluid=True
            ),
            dcc.Location(id=server.config["LOCATION_COMPONENT_ID"], refresh=False),
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
                            make_sidebar(className="px-2"), width=2, className="px-0"
                        ),
                        dbc.Col(id=server.config["CONTENT_CONTAINER_ID"], width=10),
                    ]
                ),
            ),
            dcc.Location(id=server.config["LOCATION_COMPONENT_ID"], refresh=False),
        ]
    )


def main_default_layout():

    return html.Div(
        [
            # make_header(),
            html.Br(),
            dcc.Store(id="store"),
            dbc.Container(
                fluid=True,
                children=[
                    dbc.Col(id=server.config["CONTENT_CONTAINER_ID"]),
                    dcc.Location(
                        id=server.config["LOCATION_COMPONENT_ID"], refresh=False
                    ),
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
