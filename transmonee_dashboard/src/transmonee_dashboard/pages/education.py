# Import required libraries
import urllib
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from ..app import app, cache, mapbox_access_token, geocoder, sdmx_url

CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}

# @cache.memoize
def geocode_address(address):
    """Geocode street address into lat/long."""
    response = geocoder.forward(address)
    coords = response.json()["features"][0]["center"]
    return dict(longitude=coords[0], latitude=coords[1])


px.set_mapbox_access_token(mapbox_access_token)
static_data = {
    "Country": [
        "Albania",
        "Belarus",
        "Bosnia and Herzegovina",
        "Bulgaria",
        "Croatia",
        "Georgia, Europe, Asia",
        "Kazakhstan",
        "Kosovo",
        "Moldova",
        "Montenegro",
        "North Macedonia",
        "Romania",
        "Serbia",
        "Turkey",
        "Ukraine",
    ],
    "Reading": [52, 23, 54, 47, 22, 64, 64, 79, 43, 44, 55, 41, 38, 26, 26],
    "Math": [42, 29, 58, 44, 31, 61, 49, 77, 50, 46, 61, 47, 40, 37, 36],
    "Science": [47, 24, 57, 47, 25, 64, 60, 77, 43, 48, 49, 44, 38, 25, 26],
}
main_graph_df = pd.DataFrame(
    static_data, columns=["Country", "Reading", "Math", "Science"]
)


def generate_map(title, data, options):
    return px.scatter_mapbox(data, title=title, **options)


codes = [
    "EDU_SDG_STU_L2_GLAST_MAT",
    "EDU_SDG_STU_L2_GLAST_REA",
    "EDU_SDG_STU_L1_GLAST_MAT",
    "EDU_SDG_STU_L1_G2OR3_MAT",
    "EDU_SDG_STU_L1_GLAST_REA",
    "EDU_SDG_STU_L1_G2OR3_REA",
    "EDU_SDG_GER_L01",
    "EDUNF_PRP_L02",
    "EDUNF_ROFST_L2",
    "EDU_SDG_QUTP_L02",
    "EDU_SDG_QUTP_L1",
    "EDU_SDG_QUTP_L2",
    "EDU_SDG_QUTP_L3",
    "EDU_SDG_TRTP_L02",
    "EDU_SDG_TRTP_L1",
    "EDU_SDG_TRTP_L2",
    "EDU_SDG_TRTP_L3",
    "EDUNF_ROFST_L1",
    "EDUNF_ROFST_L2",
    "EDUNF_ROFST_L3",
    "EDUNF_OFST_L1",
    "EDUNF_OFST_L2",
    "EDUNF_OFST_L3",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_NER_L02",
    "EDUNF_NERA_L1_UNDER1",
    "EDUNF_NERA_L1",
    "EDUNF_NERA_L2",
    "EDUNF_GER_L1",
    "EDUNF_GER_L2",
    "EDUNF_GER_L3",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_STU_L1_TOT",
    "EDUNF_STU_L2_TOT",
    "EDUNF_STU_L3_TOT",
    "EDU_SDG_SCH_L1",
    "EDU_SDG_SCH_L2",
    "EDU_SDG_SCH_L3",
    "EDUNF_PRP_L02",
    "EDUNF_CR_L1",
    "EDUNF_CR_L2",
    "EDUNF_CR_L3",
    "EDUNF_DR_L1",
    "EDUNF_DR_L2",
    "EDUNF_SAP_L02",
    "EDUNF_SAP_L1T3",
    "EDUNF_SAP_L2",
]


data = pd.DataFrame()
inds = set(codes)
for ind in inds:
    try:
        sdmx = pd.read_csv(sdmx_url.format(ind))
    except urllib.error.HTTPError as e:
        print(ind)
        raise e

    sdmx["CODE"] = ind
    data = data.append(sdmx)

countries = data["Geographic area"].unique()

data = data.merge(
    right=pd.DataFrame(
        [dict(country=country, **geocode_address(country)) for country in countries]
    ),
    left_on="Geographic area",
    right_on="country",
)

# Create controls
county_options = [
    {"label": str(country), "value": str(country)} for country in countries
]

years = [i for i in range(2008, 2020)]

indicators = data["Indicator"].unique()

regions = [
    {
        "label": "Western Balkans",
        "value": "Albania,Bosnia and Herzegovina,Kosovo,North Macedonia,Montenegro,Serbia",
    },
    {"label": "EU countries of ECAR", "value": "Bulgaria,Croatia,Romania"},
    {"label": "B+M+U", "value": "Belarus,Moldova,Ukraine"},
    {"label": "Caucasus", "value": "Armenia,Azerbaijan,Georgia"},
    {"label": "Turkey", "value": "Turkey"},
    {
        "label": "Central Asia",
        "value": "Kazakhstan,Kyrgyzstan,Tajikistan,Turkmenistan,Uzbekistan",
    },
]


indicators_dict = {
    "PARTICIPATION": {
        "NAME": "Participation",
        "CARDS": [
            {
                "name": "Regional OOS rate (P+LS+US)",
                "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "%",
                "absolute": True,
            },
            {
                "name": "Participation in organized learning",
                "indicator": "EDUNF_NER_L02",
                "denominator": "EDUNF_SAP_L02",
                "suffix": "%",
            },
            {
                "name": "Entry to primary education",
                "indicator": "EDUNF_CR_L2",
                "denominator": "EDUNF_SAP_L2",
                "suffix": "%",
            },
            # {
            #     "name": "Out of school children rate",
            #     "indicator": "EDUNF_ROFST_L3",
            #     "suffix": "%",
            # },
        ],
        "MAIN": {
            "name": "Out of School Children",
            "data": data[
                data["CODE"].isin(
                    [
                        "EDUNF_ROFST_L1",
                        "EDUNF_ROFST_L2",
                        "EDUNF_ROFST_L3",
                        "EDUNF_OFST_L1",
                        "EDUNF_OFST_L2",
                        "EDUNF_OFST_L3",
                    ]
                )
                & data["TIME_PERIOD"].isin(years)
            ]
            .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
            .agg({"OBS_VALUE": "last", "longitude": "last", "latitude": "last"})
            .reset_index(),
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=3,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_OFST_L1",
                "EDUNF_OFST_L2",
                "EDUNF_OFST_L3",
            ],
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT",
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NERA_L1",
                "EDUNF_NERA_L2",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3",
                "EDUNF_NIR_L1_ENTRYAGE",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "RIGHT": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "line",
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT",
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NERA_L1",
                "EDUNF_NERA_L2",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3",
                "EDUNF_NIR_L1_ENTRYAGE",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_SCH_L1",
                "EDU_SDG_SCH_L2",
                "EDU_SDG_SCH_L3",
            ],
        },
        "AREA_4": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "indicators": [
                "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
            ],
            "default": "EDUNF_CR_L1",
        },
    },
    "QUALITY": {
        "NAME": "Learning Quality",
        "CARDS": [
            {
                "name": "Proficiency in Math",
                "indicator": "EDU_SDG_STU_L2_MATH",
                "suffix": "%",
            },
            {
                "name": "Proficiency in Reading",
                "indicator": "EDU_SDG_STU_L2_READING",
                "suffix": "%",
            },
            {
                "name": "Youth/adult literacy rate",
                "indicator": "EDUNF_LR_L02",
                "suffix": "%",
            },
            {
                "name": "Childhood Educational Development",
                "indicator": "EDU_SDG_GER_L01",
                "suffix": "%",
            },
        ],
        "MAIN": {
            "name": "Percentage of students performing below level 2/basic proficiency in all 3 subjects",
            "data": pd.DataFrame(
                {
                    "Country": [
                        "Albania",
                        "Belarus",
                        "Bosnia and Herzegovina",
                        "Bulgaria",
                        "Croatia",
                        "Georgia, Europe, Asia",
                        "Kazakhstan",
                        "Kosovo",
                        "Moldova",
                        "Montenegro",
                        "North Macedonia",
                        "Romania",
                        "Serbia",
                        "Turkey",
                        "Ukraine",
                    ],
                    "Reading": [
                        52,
                        23,
                        54,
                        47,
                        22,
                        64,
                        64,
                        79,
                        43,
                        44,
                        55,
                        41,
                        38,
                        26,
                        26,
                    ],
                    "Math": [
                        42,
                        29,
                        58,
                        44,
                        31,
                        61,
                        49,
                        77,
                        50,
                        46,
                        61,
                        47,
                        40,
                        37,
                        36,
                    ],
                    "Science": [
                        47,
                        24,
                        57,
                        47,
                        25,
                        64,
                        60,
                        77,
                        43,
                        48,
                        49,
                        44,
                        38,
                        25,
                        26,
                    ],
                },
                columns=["Country", "Reading", "Math", "Science"],
            ),
            "geo": "Country",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="Reading",
                text="Country",
                color="Reading",
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=2.5,
                height=750,
            ),
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_STU_L2_MATH",
                "EDU_SDG_STU_L2_READING",
                "EDU_SDG_STU_L1_GLAST_MATH",
                "EDU_SDG_STU_L1_G2OR3_MATH",
                "EDU_SDG_STU_L1_GLAST_READING",
                "EDU_SDG_STU_L1_G2OR3_READING",
            ],
        },
        "RIGHT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_ROFST_L2",
                "EDU_SDG_STU_L2_MATH",
                "EDU_SDG_STU_L1_GLAST_MATH",
                "EDU_SDG_STU_L1_G2OR3_READING",
                "EDUNF_NERA_L2",
            ],
            "data": data[data["Sex"] != "Total"]
            .groupby(["CODE", "Indicator", "Geographic area", "Sex"])
            .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
            .reset_index(),
        },
    },
}


def indicator_card(
    name, year_slider, countires, numerator, denominator, suffix, absolute=False
):
    time = years[slice(*year_slider)]
    query = (
        "CODE in @indicator & TIME_PERIOD in @time & `Geographic area` in @countries"
    )
    numors = numerator.split(",")
    indicator = numors
    # select last value for each country
    indicator_values = (
        data.query(query)
        .groupby(
            [
                "CODE",
                "Indicator",
                "Geographic area",
                "UNIT_MEASURE",
            ]
        )
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
        .set_index(["Geographic area", "TIME_PERIOD"])
    )
    # select the avalible denominators for countiries in selected years
    indicator = [denominator]
    denominator_values = (
        data.query(query)
        .groupby(
            [
                "CODE",
                "Indicator",
                "Geographic area",
                "UNIT_MEASURE",
            ]
        )
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
        .set_index(["Geographic area", "TIME_PERIOD"])
    )
    # select only those denominators that match avalible indicators
    denominators = denominator_values[
        denominator_values.index.isin(indicator_values.index)
    ]["OBS_VALUE"]

    denominator_sum = denominators.to_numpy().sum()

    indicator_sum = (
        (denominators / denominator_sum)
    ).dropna()  # will drop missing countires

    sources = indicator_sum.index.tolist()

    label = (
        data[data["CODE"].isin(indicator)]["Indicator"].unique()[0]
        if len(data[data["CODE"].isin(indicator)]["Indicator"].unique())
        else "None"
    )
    card = dbc.Card(
        [
            dbc.CardHeader(name),
            dbc.CardBody(
                [
                    html.H4(
                        "{:.0f}{}".format(indicator_sum.to_numpy().sum(), suffix),
                        style={
                            "fontSize": 40,
                            "textAlign": "center",
                            "color": "#0074D9",
                        },
                    ),
                    html.P(label, className="card-text", style=CARD_TEXT_STYLE),
                    # html.P("Sources: {}".format(sources)),
                ]
            ),
        ],
        color="primary",
        outline=True,
    )
    return card


def get_layout(**kwargs):

    return html.Div(
        [
            # start first row
            dbc.Row(
                [
                    # start controls side bar
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader("Data Explorer Controls"),
                                dbc.CardBody(
                                    [
                                        html.P(
                                            "Select theme:",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="theme_selector",
                                            options=[
                                                {"label": value["NAME"], "value": key}
                                                for key, value in indicators_dict.items()
                                            ],
                                            value=list(indicators_dict.keys())[0],
                                            className="dcc_control",
                                        ),
                                        html.P(
                                            "Filter by year:",
                                            className="control_label",
                                        ),
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
                                        html.P(
                                            "Filter by Region:",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="region_selector",
                                            options=regions,
                                            className="dcc_control",
                                        ),
                                        html.P(
                                            "Filter by Country:",
                                            className="control_label",
                                        ),
                                        dbc.Checklist(
                                            id="country_selector",
                                            options=county_options,
                                            value=[
                                                item["value"] for item in county_options
                                            ],
                                            className="dcc_control",
                                        ),
                                    ]
                                ),
                            ]
                        ),
                        # className="pretty_container four columns",
                        id="cross-filter-options",
                        width=4,
                    ),
                    # end controls
                    # start cards and main graph
                    dbc.Col(
                        [
                            dbc.Row(
                                [],
                                id="cards_row"
                                # className="mb-4",
                            ),
                            html.Br(),
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dcc.Graph(id="main_graph"),
                                        dcc.Dropdown(
                                            id="main_indicators",
                                            className="dcc_control",
                                        ),
                                    ]
                                ),
                                # id="countGraphContainer",
                                className="pretty_container",
                            ),
                        ],
                        id="right-column",
                        # className="eight columns",
                        width=8,
                    ),
                    # end cards
                ],
                className="row flex-display",
            ),
            # end first row
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="left_graph")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="left_xaxis_column",
                                            className="dcc_control",
                                        ),
                                        dcc.RadioItems(
                                            id="left_graph_options",
                                            className="dcc_control",
                                            labelStyle={"display": "inline-block"},
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="right_graph")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="right_xaxis_column",
                                            className="dcc_control",
                                        ),
                                        dcc.RadioItems(
                                            id="right_graph_options",
                                            className="dcc_control",
                                            labelStyle={"display": "inline-block"},
                                            options=[
                                                {"label": "Line", "value": "line"},
                                                {"label": "Bar", "value": "bar"},
                                            ],
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                    ),
                ],
                className="row flex-display",
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="area_3")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="area_3_xaxis_column",
                                            className="dcc_control",
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="area_4_graph")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="area_4_xaxis_column",
                                            className="dcc_control",
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                    ),
                ],
            ),
            html.Br(),
        ],
    )


@app.callback(
    Output("country_selector", "value"),
    [Input("region_selector", "value")],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def select_region(region):
    if region:
        return region.split(",")
    else:
        return [item["value"] for item in county_options]


@app.callback(
    Output("cards_row", "children"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def show_cards(theme, years, countires):

    return [
        dbc.Col(
            indicator_card(
                card["name"],
                years,
                countires,
                card["indicator"],
                card["denominator"],
                card["suffix"],
            )
        )
        for card in indicators_dict[theme]["CARDS"]
    ]


@app.callback(
    Output("main_indicators", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def main_options(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(indicators_dict[theme]["MAIN"]["indicators"])
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


@app.callback(
    Output("main_graph", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("main_indicators", "value"),
    ],
    # [State("main_graph", "figure")],
)
def make_map(theme, years, countries, indicator):

    name = indicators_dict[theme]["MAIN"]["name"]
    df = indicators_dict[theme]["MAIN"]["data"]
    geo = indicators_dict[theme]["MAIN"]["geo"]
    options = indicators_dict[theme]["MAIN"]["options"]
    indicators = indicators_dict[theme]["MAIN"].get("indicators")

    if indicators:
        indicator = indicator or indicators[0]

        df = df[df["CODE"] == indicator]

    return generate_map(name, df, options)


# Selectors -> left graph
@app.callback(
    Output("left_xaxis_column", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def left_indicators(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(indicators_dict[theme]["LEFT"]["indicators"])
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


@app.callback(
    Output("left_xaxis_column", "value"),
    [
        Input("theme_selector", "value"),
        Input("left_xaxis_column", "options"),
    ],
    # [State("left-xaxis-column", "value")],
)
def left_indicators_value(theme, options):

    code = indicators_dict[theme]["LEFT"]["default"]
    return next(item for item in options if item["value"] == code)["value"]


# Selectors -> left graph
@app.callback(
    Output("left_graph_options", "options"),
    [
        Input("left_xaxis_column", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def left_options(indicator):

    options = []

    for item in [
        {"label": "Sex", "value": "Sex"},
        {"label": "Residence", "value": "Residence"},
        {"label": "Wealth Quintile", "value": "Wealth Quintile"},
    ]:
        if not data[
            (data["CODE"] == indicator) & (data[item["value"]] != "Total")
        ].empty:
            options.append(item)

    return options


# Selectors -> left graph
@app.callback(
    Output("left_graph", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("left_xaxis_column", "value"),
        Input("left_graph_options", "value"),
    ],
    # [State("left_xaxis_column", "value")],
)
def left_figure(theme, year_slider, countries, xaxis, compare):

    fig_type = indicators_dict[theme]["LEFT"]["type"]
    options = indicators_dict[theme]["LEFT"]["options"]

    compare = compare if compare else indicators_dict[theme]["LEFT"]["compare"]
    indicator = xaxis if xaxis else indicators_dict[theme]["LEFT"]["default"]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        data[
            (data["CODE"] == indicator)
            & (data[compare] != "Total")
            & (data["TIME_PERIOD"].isin(years[slice(*year_slider)]))
            & (data["Geographic area"].isin(countries))
        ]
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

    options["title"] = name
    options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    fig.update_xaxes(categoryorder="total descending")
    return fig


@app.callback(
    Output("right_xaxis_column", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def right_options(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(indicators_dict[theme]["RIGHT"]["indicators"])
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


# Selectors -> reading graph
@app.callback(
    Output("right_graph", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("left_xaxis_column", "value"),
        Input("right_xaxis_column", "value"),
        Input("right_graph_options", "value"),
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def right_figure(
    theme, year_slider, countries, left_selected, right_selected, selected_type
):

    default = indicators_dict[theme]["RIGHT"]["default_graph"]
    fig_type = selected_type if selected_type else default
    config = indicators_dict[theme]["RIGHT"]["graphs"][fig_type]
    compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")
    indicators = indicators_dict[theme]["RIGHT"]["indicators"]

    indicator = right_selected if right_selected else left_selected or indicators[0]
    time = years[slice(*year_slider)]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    query = (
        "CODE == @indicator & TIME_PERIOD in @time & `Geographic area` in @countries"
    )
    if compare:
        query = "{} & {} != 'Total'".format(query, compare)
    df = (
        data.query(query)
        .groupby(
            [
                "CODE",
                "Indicator",
                "Geographic area",
                compare if compare else "TIME_PERIOD",
            ]
        )
        .agg(
            {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
            if compare
            else {"OBS_VALUE": "mean"}
        )
        .reset_index()
    )

    options["title"] = name
    if compare:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)
    fig.update_xaxes(categoryorder="total descending")
    return fig


# Selectors -> left graph
@app.callback(
    Output("area_3_xaxis_column", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def area_3_options(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(indicators_dict[theme]["AREA_3"]["indicators"])
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


# Selectors -> reading graph
@app.callback(
    Output("area_3", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("area_3_xaxis_column", "value"),
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def area_3_figure(theme, year_slider, countries, xaxis):

    fig_type = indicators_dict[theme]["AREA_3"]["type"]
    compare = indicators_dict[theme]["AREA_3"]["compare"]
    options = indicators_dict[theme]["AREA_3"]["options"]
    indicator = xaxis if xaxis else indicators_dict[theme]["AREA_3"]["indicators"][0]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        data[
            (data["CODE"] == indicator)
            # & (data[compare] != "Total")
            & (data["TIME_PERIOD"].isin(years[slice(*year_slider)]))
            & (data["Geographic area"].isin(countries))
        ]
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

    options["title"] = name
    # if not getattr(df, compare).empty:
    #     options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    fig.update_xaxes(categoryorder="total descending")
    return fig


# Selectors -> left graph
@app.callback(
    Output("area_4_xaxis_column", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def area_4_options(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(indicators_dict[theme]["AREA_4"]["indicators"])
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


@app.callback(
    Output("area_4_graph", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("area_4_xaxis_column", "value"),
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def area_4_figure(theme, year_slider, countries, xaxis):

    default = indicators_dict[theme]["AREA_4"]["default_graph"]
    fig_type = default
    config = indicators_dict[theme]["AREA_4"]["graphs"][fig_type]
    compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")
    indicator = xaxis if xaxis else indicators_dict[theme]["AREA_4"]["indicators"][0]
    time = years[slice(*year_slider)]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    query = (
        "CODE == @indicator & TIME_PERIOD in @time & `Geographic area` in @countries"
    )
    if compare:
        query = "{} & {} != 'Total'".format(query, compare)
    df = (
        data.query(query)
        .groupby(
            [
                "CODE",
                "Indicator",
                "Geographic area",
                compare if compare else "TIME_PERIOD",
            ]
        )
        .agg(
            {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
            if compare
            else {"OBS_VALUE": "mean"}
        )
        .reset_index()
    )

    options["title"] = name
    if compare:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)
    fig.update_xaxes(categoryorder="total descending")

    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    indicator = "EDUNF_DR_L1"
    line_data = (
        data.query(query)
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

    line = px.line(
        line_data,
        x="Geographic area",
        y="OBS_VALUE",
        color=compare,
        text="TIME_PERIOD",
        # labels={"Indicator": "Dropout Rate"},
    )
    line.update_traces(
        yaxis="y2",
        mode="markers",
        marker=dict(size=12, line=dict(width=2, color="DarkSlateGrey")),
        # selector=dict(mode="markers"),
    )

    subfig.add_traces(fig.data + line.data)

    return subfig