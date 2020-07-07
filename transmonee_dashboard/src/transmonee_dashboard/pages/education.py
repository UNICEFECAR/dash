# Import required libraries
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from ..app import app

sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv"

indicators_dict = {
    "EDU_SDG_STU_L2_MATH": {
        "name": "Proportion of children at the end of lower secondary education reaching minimum proficiency in math",
        "compare": [
            "EDU_SDG_STU_L2_READING",
            "EDU_SDG_STU_L1_GLAST_MATH",
            "EDU_SDG_STU_L1_G2OR3_MATH",
            "EDUNF_NERA_L2",
        ],
    },
    "EDU_SDG_STU_L2_READING": {
        "name": "Proportion of children at the end of lower secondary education reaching minimum proficiency in reading",
        "compare": [
            "EDUNF_ROFST_L2",
            "EDU_SDG_STU_L2_MATH",
            "EDU_SDG_STU_L1_GLAST_READING",
            "EDU_SDG_STU_L1_G2OR3_READING",
            "EDUNF_NERA_L2",
        ],
    },
    "EDU_SDG_STU_L1_GLAST_MATH": {
        "name": "Proportion of children at the end of primary education reaching minimum proficiency in math",
        "compare": ["EDU_SDG_STU_L1_GLAST_READING", "EDUNF_NERA_L1_PT"],
    },
}

data = pd.DataFrame()
inds = set()
for key, value in indicators_dict.items():
    inds.add(key)
    inds.update(value["compare"])

for ind in inds:
    sdmx = pd.read_csv(sdmx_url.format(ind))
    sdmx["CODE"] = ind
    data = data.append(sdmx)

# Create controls
county_options = [
    {"label": str(country), "value": str(country)}
    for country in data["Geographic area"].unique()
]

years = [i for i in range(2010, 2020)]

indicators = data["Indicator"].unique()


def get_layout(**kwargs):

    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                        dbc.CardBody(
                            [
                                html.P("Filter by year:", className="control_label",),
                                dcc.RangeSlider(
                                    id="year_slider",
                                    min=0,
                                    max=len(years),
                                    step=None,
                                    marks={
                                        index: str(year)
                                        for index, year in enumerate(years)
                                    },
                                    value=[0, len(years)],
                                    className="dcc_control",
                                ),
                                html.P("Filter by Country:", className="control_label"),
                                dcc.Dropdown(
                                    id="country_selector",
                                    options=county_options,
                                    multi=True,
                                    value=[item["value"] for item in county_options],
                                    className="dcc_control",
                                ),
                            ]
                        )),
                        # className="pretty_container four columns",
                        id="cross-filter-options",
                        width=4,
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                dbc.CardHeader("Card header"),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            "Card title",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "This is some card content that we'll reuse",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            color="primary",
                                            outline=True,
                                        )
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                dbc.CardHeader("Card header"),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            "Card title",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "This is some card content that we'll reuse",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            color="secondary",
                                            outline=True,
                                        )
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                dbc.CardHeader("Card header"),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            "Card title",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "This is some card content that we'll reuse",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            color="info",
                                            outline=True,
                                        )
                                    ),
                                    dbc.Col(
                                        dbc.Card(
                                            [
                                                dbc.CardHeader("Card header"),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            "Card title",
                                                            className="card-title",
                                                        ),
                                                        html.P(
                                                            "This is some card content that we'll reuse",
                                                            className="card-text",
                                                        ),
                                                    ]
                                                ),
                                            ],
                                            color="info",
                                            outline=True,
                                        )
                                    ),
                                ],
                                # className="mb-4",
                            ),
                            html.Div(
                                [dcc.Graph(id="count_graph")],
                                id="countGraphContainer",
                                className="pretty_container",
                            ),
                        ],
                        id="right-column",
                        # className="eight columns",
                        width=8,
                    ),
                ],
                # className="row flex-display",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                [dcc.Graph(id="maths_graph")],
                                className="pretty_container",
                            ),
                            dcc.Dropdown(
                                id="maths-xaxis-column",
                                options=[
                                    {"label": item["Indicator"], "value": item["CODE"]}
                                    for item in data[
                                        data["CODE"].isin(
                                            indicators_dict["EDU_SDG_STU_L2_MATH"][
                                                "compare"
                                            ]
                                        )
                                    ][["CODE", "Indicator"]]
                                    .drop_duplicates()
                                    .to_dict("records")
                                ],
                                multi=True,
                                #                             value=[item for item in indicators],
                                className="dcc_control",
                            ),
                        ],
                        # className="six columns",
                        width=6
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [dcc.Graph(id="reading_graph")],
                                className="pretty_container",
                            ),
                            dcc.Dropdown(
                                id="reading-xaxis-column",
                                options=[
                                    {"label": item["Indicator"], "value": item["CODE"]}
                                    for item in data[
                                        data["CODE"].isin(
                                            indicators_dict["EDU_SDG_STU_L2_READING"][
                                                "compare"
                                            ]
                                        )
                                    ][["CODE", "Indicator"]]
                                    .drop_duplicates()
                                    .to_dict("records")
                                ],
                                multi=True,
                                #                             value=[item for item in indicators],
                                className="dcc_control",
                            ),
                        ],
                        # className="six columns",
                        width=6
                    ),
                ],
                # className="row flex-display",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [dcc.Graph(id="pie_graph")],
                        className="pretty_container seven columns",
                    ),
                    dbc.Col(
                        [dcc.Graph(id="aggregate_graph")],
                        className="pretty_container five columns",
                    ),
                ],
                # className="row flex-display",
            ),
        ],
    )

