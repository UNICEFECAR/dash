from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

title_row = dbc.Container(
    dbc.Row(
        [
            dbc.Col(
                html.Img(src="./assets/logo-unicef-large.svg"),
                width=3,
                # width={"size": 3, "offset": 1},
                style={"paddingLeft": "20px", "paddingTop": "20px"},
            ),
            dbc.Col(
                html.Div(
                    [
                        html.H6(
                            "TransMonEE Dashboard Review",
                            style={
                                "fontWeight": "bold",
                                "textAlign": "center",
                                "paddingTop": "30px",
                                "color": "white",
                                "fontSize": "32px",
                            },
                        ),
                    ]
                ),
                # width='auto',
                width={"size": "auto", "offset": 1},
            ),
        ],
        justify="start",
        align="center",
    ),
    fluid=True,
)

layout = dbc.Container(
    [
        # title Div
        html.Div(
            [title_row],
            style={
                "height": "100px",
                "width": "100%",
                "backgroundColor": "DeepSkyBlue",
                "margin-left": "auto",
                "margin-right": "auto",
                "margin-top": "15px",
            },
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        html.H6(
                            "Health and Nutrition",
                            style={
                                "fontWeight": "bold",
                                "textAlign": "center",
                                "paddingTop": "25px",
                                "color": "#2c5996ff",
                                "fontSize": "32px",
                            },
                        ),
                    ]
                ),
            ],
            justify="center",
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/hhs.svg"),
                        ],
                        href="/hhs",
                    ),
                    width="auto",
                ),
                dbc.Col(
                    html.Img(src="./assets/mnh.svg"),
                    width="auto",
                ),
                dbc.Col(
                    html.Img(src="./assets/imm.svg"),
                    width="auto",
                ),
            ],
            justify="center",
            align="center",
        ),
    ],
    fluid=True,
)
