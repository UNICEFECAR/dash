import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/", order=0)


def layout(**kwargs):
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
                            # dbc.CardHeader(html.H3("State of Children Rights")),
                            dbc.CardBody(
                                [
                                    html.Img(
                                        src="assets/architecture.png",
                                        className="rounded mx-auto d-block",
                                    ),
                                    html.Br(),
                                    # html.H4(
                                    #     "What you can find here...",
                                    #     className="card-title",
                                    # ),
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
