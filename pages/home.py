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
                                    "Child Rights Landscape and Governance",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#562061ff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-rights",
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
                            html.Img(src="./assets/dem.svg"),
                        ],
                        href="/child-rights#dem",
                    ),
                    width="auto",
                    id="dem-col",
                ),
                dbc.Tooltip(
                    "Demographics",
                    target="dem-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/ple.svg"),
                        ],
                        href="/child-rights#ple",
                    ),
                    width="auto",
                    id="ple-col",
                ),
                dbc.Tooltip(
                    "Political economy",
                    target="ple-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/mig.svg"),
                        ],
                        href="/child-rights#mig",
                    ),
                    width="auto",
                    id="mig-col",
                ),
                dbc.Tooltip(
                    "Migration and displacement",
                    target="mig-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/crg.svg"),
                        ],
                        href="/child-rights#crg",
                    ),
                    width="auto",
                    id="crg-col",
                ),
                dbc.Tooltip(
                    "Child rights governance",
                    target="crg-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/spe.svg"),
                        ],
                        href="/child-rights#spe",
                    ),
                    width="auto",
                    id="spe-col",
                ),
                dbc.Tooltip(
                    "Public spending on children",
                    target="spe-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/dta.svg"),
                        ],
                        href="/child-rights#dta",
                    ),
                    width="auto",
                    id="dta-col",
                ),
                dbc.Tooltip(
                    "Data on children",
                    target="dta-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/rem.svg"),
                        ],
                        href="/child-rights#rem",
                    ),
                    width="auto",
                    id="rem-col",
                ),
                dbc.Tooltip(
                    "Right to remedy",
                    target="rem-col",
                    placement="bottom",
                ),
                dbc.Col(
                    # html.A(
                    [
                        html.Img(src="./assets/bus.svg"),
                    ],
                    # href="/child-rights#bus",
                    # ),
                    width="auto",
                    id="bus-col",
                ),
                dbc.Tooltip(
                    "Business and Child Rights",
                    target="bus-col",
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
                                        "color": "#00aeefff",
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
                                        "color": "#961b4aff",
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
        dbc.Row(
            [
                html.Div(
                    [
                        html.A(
                            [
                                html.H6(
                                    "Education",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#2e76bcff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-education",
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
                            html.Img(src="./assets/esy.svg"),
                        ],
                        href="/child-education#esy",
                    ),
                    width="auto",
                    id="esy-col",
                ),
                dbc.Tooltip(
                    "Education system",
                    target="esy-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/epa.svg"),
                        ],
                        href="/child-education#epa",
                    ),
                    width="auto",
                    id="epa-col",
                ),
                dbc.Tooltip(
                    "Education access and participation",
                    target="epa-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/equ.svg"),
                        ],
                        href="/child-education#equ",
                    ),
                    width="auto",
                    id="equ-col",
                ),
                dbc.Tooltip(
                    "Learning quality and skills",
                    target="equ-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/ele.svg"),
                        ],
                        href="/child-education#ele",
                    ),
                    width="auto",
                    id="ele-col",
                ),
                dbc.Tooltip(
                    "Leisure and culture",
                    target="ele-col",
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
                                    "Family Environment and Protection",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#4aa4b6ff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-protection",
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
                            html.Img(src="./assets/vio.svg"),
                        ],
                        href="/child-protection#vio",
                    ),
                    width="auto",
                    id="vio-col",
                ),
                dbc.Tooltip(
                    "Violence against children and women",
                    target="vio-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/cpc.svg"),
                        ],
                        href="/child-protection#cpc",
                    ),
                    width="auto",
                    id="cpc-col",
                ),
                dbc.Tooltip(
                    "Children without parental care",
                    target="cpc-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/jus.svg"),
                        ],
                        href="/child-protection#jus",
                    ),
                    width="auto",
                    id="jus-col",
                ),
                dbc.Tooltip(
                    "Justice for children",
                    target="jus-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/mar.svg"),
                        ],
                        href="/child-protection#mar",
                    ),
                    width="auto",
                    id="mar-col",
                ),
                dbc.Tooltip(
                    "Child marriage and other harmful practices",
                    target="mar-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/lab.svg"),
                        ],
                        href="/child-protection#lab",
                    ),
                    width="auto",
                    id="lab-col",
                ),
                dbc.Tooltip(
                    "Child labour and other forms of exploitation",
                    target="lab-col",
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
                                    "Cross-Cutting",
                                    style={
                                        "fontWeight": "bold",
                                        "textAlign": "center",
                                        "paddingTop": "25px",
                                        "color": "#13733bff",
                                        "fontSize": "32px",
                                    },
                                ),
                            ],
                            href="/child-cross-cutting",
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
                            html.Img(src="./assets/ecd.svg"),
                        ],
                        href="/child-cross-cutting#ecd",
                    ),
                    width="auto",
                    id="ecd-col",
                ),
                dbc.Tooltip(
                    "Early childhood development",
                    target="ecd-col",
                    placement="bottom",
                ),
                dbc.Col(
                    # html.A(
                    [
                        html.Img(src="./assets/dis.svg"),
                    ],
                    # href="/child-cross-cutting#dis",
                    # ),
                    width="auto",
                    id="dis-col",
                ),
                dbc.Tooltip(
                    "Disability",
                    target="dis-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/gnd.svg"),
                        ],
                        href="/child-cross-cutting#gnd",
                    ),
                    width="auto",
                    id="gnd-col",
                ),
                dbc.Tooltip(
                    "Gender",
                    target="gnd-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/oda.svg"),
                        ],
                        href="/child-cross-cutting#oda",
                    ),
                    width="auto",
                    id="oda-col",
                ),
                dbc.Tooltip(
                    "Adolescents",
                    target="oda-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/env.svg"),
                        ],
                        href="/child-cross-cutting#env",
                    ),
                    width="auto",
                    id="env-col",
                ),
                dbc.Tooltip(
                    "Environment and climate change",
                    target="env-col",
                    placement="bottom",
                ),
                dbc.Col(
                    html.A(
                        [
                            html.Img(src="./assets/rsk.svg"),
                        ],
                        href="/child-cross-cutting#rsk",
                    ),
                    width="auto",
                    id="rsk-col",
                ),
                dbc.Tooltip(
                    "Risks and humanitarian situation",
                    target="rsk-col",
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
