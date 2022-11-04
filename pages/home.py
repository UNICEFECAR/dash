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
        # html.Div(
        #     [title_row],
        #     style={
        #         "height": "100px",
        #         "width": "100%",
        #         "backgroundColor": "DeepSkyBlue",
        #         "margin-left": "auto",
        #         "margin-right": "auto",
        #         "margin-top": "15px",
        #     },
        # ),
        dbc.Row(
            [
                html.Div(
                    [
                        html.ObjectEl(
                            html.Img(src="./assets/SOCR_Diagram_Oct_2022_href.svg"),
                            type="image/svg+xml",
                            data="./assets/SOCR_Diagram_Oct_2022_href.svg",
                            className="px-2",
                            style={
                                "width": "100%",
                                "height": "200vh",
                                # "height": "80rem",
                                "display": "flex",
                                "margin-top": "15px",
                                "margin-bottom": "15px",
                            },
                        ),
                    ]
                ),
            ],
            justify="center",
            align="center",
        ),
    ],
    fluid=True,
)
