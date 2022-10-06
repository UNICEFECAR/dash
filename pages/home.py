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
                        html.A(
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
                            ],
                            href="/child-health",
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
                        href="/child-health#hsm",
                    ),
                    width="auto",
                    id="hhs-col",
                ),
                dbc.Tooltip(
                    "Health System",
                    target="hhs-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/mnh.svg"),
                        ],
                        href="/child-health#mnh",
                    ),
                    width="auto",
                    id="mnh-col",
                ),
                dbc.Tooltip(
                    "Maternal, newborn and child health",
                    target="mnh-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/imm.svg"),
                        ],
                        href="/child-health#imm",
                    ),
                    width="auto",
                    id="imm-col",
                ),
                dbc.Tooltip(
                    "Immunization",
                    target="imm-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/nut.svg"),
                        ],
                        href="/child-health#nut",
                    ),
                    width="auto",
                    id="nut-col",
                ),
                dbc.Tooltip(
                    "Nutrition",
                    target="nut-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/ado.svg"),
                        ],
                        href="/child-health#ado",
                    ),
                    width="auto",
                    id="ado-col",
                ),
                dbc.Tooltip(
                    "Adolescent physical, mental and reproductive health",
                    target="ado-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/hiv.svg"),
                        ],
                        href="/child-health#hiv",
                    ),
                    width="auto",
                    id="hiv-col",
                ),
                dbc.Tooltip(
                    "HIV and AIDS",
                    target="hiv-col",
                    placement="bottom",
                ),
            ],
            justify="center",
            align="center",
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        html.A(
                            [
                                html.H6(
                                    "Poverty and Adequate Standards of Living",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#2c5996ff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-poverty",
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
                            html.Img(src="./assets/mat.svg"),
                        ],
                        href="/child-poverty#mat",
                    ),
                    width="auto",
                    id="mat-col",
                ),
                dbc.Tooltip(
                    "Child poverty and material deprivation",
                    target="mat-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/sps.svg"),
                        ],
                        href="/child-poverty#sps",
                    ),
                    width="auto",
                    id="sps-col",
                ),
                dbc.Tooltip(
                    "Social protection system",
                    target="sps-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/wsh.svg"),
                        ],
                        href="/child-poverty#wsh",
                    ),
                    width="auto",
                    id="wsh-col",
                ),
                dbc.Tooltip(
                    "Water, sanitation and hygiene",
                    target="wsh-col",
                    placement="bottom",
                ),
            ],
            justify="center",
            align="center",
        ),
        dbc.Row(
            [
                html.Div(
                    [
                        html.A(
                            [
                                html.H6(
                                    "Participation and Civil Rights",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#2c5996ff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-participation",
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
                            html.Img(src="./assets/reg.svg"),
                        ],
                        href="/child-participation#reg",
                    ),
                    width="auto",
                    id="reg-col",
                ),
                dbc.Tooltip(
                    "Birth registration and identity",
                    target="reg-col",
                    placement="bottom",
                ),
                dbc.Col(
                    # html.A(
                    [
                        html.Img(src="./assets/par.svg"),
                    ],
                    # href="/child-participation#par",
                    # ),
                    width="auto",
                    id="par-col",
                ),
                dbc.Tooltip(
                    "Child participation",
                    target="par-col",
                    placement="bottom",
                ),
                dbc.Col(
                    # html.A(
                    [
                        html.Img(src="./assets/pol.svg"),
                    ],
                    # href="/child-participation#pol",
                    # ),
                    width="auto",
                    id="pol-col",
                ),
                dbc.Tooltip(
                    "Civil and political freedoms",
                    target="pol-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/ict.svg"),
                        ],
                        href="/child-participation#ict",
                    ),
                    width="auto",
                    id="ict-col",
                ),
                dbc.Tooltip(
                    "Information, internet and protection of privacy",
                    target="ict-col",
                    placement="bottom",
                ),
            ],
            justify="center",
            align="center",
        ),
        html.Br(),
    ],
    fluid=True,
)
