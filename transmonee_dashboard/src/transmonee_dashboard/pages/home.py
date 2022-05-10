import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app
from ..components import make_wheel


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
                            dbc.CardBody(
                                [
                                    make_wheel(className="px-2"),
                                    # html.Img(
                                    #     src="assets/home.png",
                                    #     className="rounded mx-auto d-block",
                                    # ),
                                    html.Br(),
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
