from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/transmonee", order=0, title="TransMonEE Dashboard")


layout = dbc.Container(
    [
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
