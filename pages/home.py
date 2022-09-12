from dash import get_asset_url, html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        [
                            html.Img(src=get_asset_url("india_color2.svg")),
                        ],
                        href="/district_gis",
                    ),
                    width=4,
                    # width={"size": 3, "offset": 1},
                    style={"paddingTop": "20px"},
                ),
            ],
            justify="evenly",
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        [
                            html.Img(src=get_asset_url("scatter_trend.svg")),
                        ],
                        href="/district_scatter",
                    ),
                    width=4,
                    # width={"size": 3, "offset": 1},
                    style={"paddingTop": "20px"},
                ),
            ],
            justify="evenly",
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        [
                            html.Img(src=get_asset_url("trend_line.svg")),
                        ],
                        href="/state_trend",
                    ),
                    width=4,
                    # width={"size": 3, "offset": 1},
                    style={"paddingTop": "20px"},
                ),
            ],
            justify="evenly",
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.A(
                        [
                            html.Img(src=get_asset_url("trend_bar_color2.svg")),
                        ],
                        href="/state_equity",
                    ),
                    width=4,
                    # width={"size": 3, "offset": 1},
                    style={"paddingTop": "20px"},
                ),
            ],
            justify="evenly",
            align="center",
        ),
    ],
    fluid=True,
)
