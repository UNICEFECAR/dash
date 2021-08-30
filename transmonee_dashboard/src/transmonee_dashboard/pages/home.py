import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app


def get_layout(**kwargs):
    return html.Div(
        children=[
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
                                        "Home",
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            html.Br(),
            html.Div(
                children=[
                    dbc.Card(
                        [
                            dbc.CardHeader(html.H3("State of Children Rights")),
                            dbc.CardBody(
                                [
                                    html.Img(
                                        src="assets/home.png",
                                        className="rounded mx-auto d-block",
                                    ),
                                    html.Br(),
                                    html.H4(
                                        "What you can find here...",
                                        className="card-title",
                                    ),
                                ]
                            ),
                        ]
                    ),
                ],
                style={"textAlign": "center"},
            ),
            html.Br(),
        ],
    )
