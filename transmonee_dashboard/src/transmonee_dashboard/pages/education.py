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
import plotly.express as px

from ..app import app, mapbox_access_token, geocoder, sdmx_url


indicators_dict = {
    "EDU_SDG_STU_L2_MATH": {
        "name": "Proportion of children at the end of lower secondary education reaching minimum proficiency in math",
        "compare": {
            "EDU_SDG_STU_L2_READING": "Proportion of children at the end of lower secondary education reaching minimum proficiency in reading",
            "EDU_SDG_STU_L1_GLAST_MATH": "Proportion of children at the end of primary education reaching minimum proficiency in math",
            "EDU_SDG_STU_L1_G2OR3_MATH": "Proportion of children in grade 2 or 3 reaching minimum proficiency in math",
            "EDUNF_NERA_L2": "Adjusted net enrolment: lower secondary",
        },
    },
    "EDU_SDG_STU_L2_READING": {
        "name": "Proportion of children at the end of lower secondary education reaching minimum proficiency in reading",
        "compare": {
            "EDUNF_ROFST_L2": "Out of school children rate: Lower secondary education",
            "EDU_SDG_STU_L2_MATH": "Proportion of children at the end of lower secondary education reaching minimum proficiency in math",
            "EDU_SDG_STU_L1_GLAST_MATH": "Proportion of children at the end of primary education reaching minimum proficiency in math",
            "EDU_SDG_STU_L1_G2OR3_READING": "Proportion of children in grade 2 or 3 reaching minimum proficiency in reading",
            "EDUNF_NERA_L2": "Adjusted net enrolment: lower secondary",
        },
    },
    "EDU_SDG_STU_L1_GLAST_MATH": {
        "name": "Proportion of children at the end of primary education reaching minimum proficiency in math",
        "compare": {
            "EDU_SDG_STU_L1_GLAST_READING": "Proportion of children at the end of primary education reaching minimum proficiency in reading",
            "EDUNF_NERA_L1_PT": "Adjusted net enrolment: primary education",
        },
    },
    "EDU_SDG_STU_L1_G2OR3_READING": {
        "name": "Proportion of children in grade 2 or 3 reaching minimum proficiency in math",
        "compare": {"EDUNF_ROFST_L1": "Out of school children rate: Primary education"},
    },
    "EDU_SDG_STU_L1_G2OR3_MATH": {
        "name": "Proportion of children in grade 2 or 3 reaching minimum proficiency in math",
        "compare": {
            "EDU_SDG_STU_L1_GLAST_READING": "Proportion of children at the end of primary education reaching minimum proficiency in reading"
        },
    },
    "EDU_SDG_GER_L01": {"compare": {}},
}

codes = [
    "EDU_SDG_STU_L2_MATH",
    "EDU_SDG_STU_L2_READING",
    "EDU_SDG_STU_L1_GLAST_MATH",
    "EDU_SDG_STU_L1_G2OR3_MATH",
    "EDU_SDG_STU_L1_GLAST_READING",
    "EDU_SDG_STU_L1_G2OR3_READING",
    "EDUNF_NERA_L2",
    "EDUNF_NERA_L1_PT",
    "EDU_SDG_GER_L01",
    "EDUNF_LR_L02",
    "EDUNF_ROFST_L2",
    "EDU_SDG_QUTP_L02",
    "EDU_SDG_QUTP_L1",
    "EDU_SDG_QUTP_L2",
    "EDU_SDG_QUTP_L3",
    "EDU_SDG_TRTP_L02",
    "EDU_SDG_TRTP_L1",
    "EDU_SDG_TRTP_L2",
    "EDU_SDG_TRTP_L3",
]

data = pd.DataFrame()
inds = set()
for ind in codes:
    sdmx = pd.read_csv(sdmx_url.format(ind))
    sdmx["CODE"] = ind
    data = data.append(sdmx)

# Create controls
county_options = [
    {"label": str(country), "value": str(country)}
    for country in data["Geographic area"].unique()
]

years = [i for i in range(2008, 2020)]

indicators = data["Indicator"].unique()

regions = [
    {
        "label": "Western Balkans",
        "value": "Albania, Bosnia and Herzegovina, Kosovo, North Macedonia, Montenegro, Serbia",
    },
    {"label": "EU countries of ECAR", "value": "Bulgaria, Croatia, Romania"},
    {"label": "B+M+U", "value": "Belarus, Moldova, Ukraine"},
    {"label": "Caucasus", "value": "Armenia, Azerbaijan, Georgia"},
    {"label": "Turkey", "value": "Turkey"},
    {
        "label": "Central Asia",
        "value": "Kazakhstan, Kyrgyzstan, Tajikistan, Turkmenistan, Uzbekistan",
    },
]


def indicator_card(indicator):
    mean_value = (
        data[data["CODE"] == indicator]
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])["OBS_VALUE"]
        .tail(1)
        .mean()
    )
    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    fig = go.Figure(
        go.Indicator(
            value=mean_value, number={"suffix": "%"}, domain={"x": [0, 1], "y": [0, 1]},
        )
    )
    fig.update_layout(height=200)
    card = dbc.Card(
        [
            dbc.CardHeader("Card header"),
            dbc.CardBody(
                [dcc.Graph(figure=fig), html.P(name, className="card-text",),]
            ),
        ],
        color="primary",
        outline=True,
    )
    return card


def get_layout(**kwargs):

    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader("Data Explorer Controls"),
                                dbc.CardBody(
                                    [
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
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(indicator_card("EDU_SDG_GER_L01")),
                                    dbc.Col(indicator_card("EDU_SDG_STU_L2_READING")),
                                    dbc.Col(indicator_card("EDUNF_LR_L02")),
                                    dbc.Col(indicator_card("EDU_SDG_GER_L01")),
                                ],
                                # className="mb-4",
                            ),
                            html.Br(),
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        dcc.Graph(id="count_graph"),
                                        dbc.ButtonGroup(
                                            [
                                                dbc.Button("Left"),
                                                dbc.Button("Middle"),
                                                dbc.Button("Right"),
                                            ],
                                            size="sm",
                                            style='p'
                                            
                                        )
                                    ]
                                ),
                                # id="countGraphContainer",
                                # className="pretty_container",
                            ),
                            html.Br(),
                        ],
                        # className="row flex-display",
                        id="right-column",
                        # className="eight columns",
                        width=8,
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="maths_graph")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="maths-xaxis-column",
                                            options=[
                                                {
                                                    "label": item["Indicator"],
                                                    "value": item["CODE"],
                                                }
                                                for item in data[
                                                    data["CODE"].isin(
                                                        [
                                                            "EDU_SDG_STU_L2_MATH",
                                                            "EDU_SDG_STU_L2_READING",
                                                            "EDU_SDG_STU_L1_GLAST_MATH",
                                                            "EDU_SDG_STU_L1_G2OR3_MATH",
                                                            "EDU_SDG_STU_L1_GLAST_READING",
                                                            "EDU_SDG_STU_L1_G2OR3_READING",
                                                        ]
                                                    )
                                                ][["CODE", "Indicator"]]
                                                .drop_duplicates()
                                                .to_dict("records")
                                            ],
                                            value="EDU_SDG_STU_L2_READING",
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
                                            [dcc.Graph(id="reading_graph")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="reading-xaxis-column",
                                            options=[
                                                {
                                                    "label": item["Indicator"],
                                                    "value": item["CODE"],
                                                }
                                                for item in data[
                                                    data["CODE"].isin(
                                                        indicators_dict[
                                                            "EDU_SDG_STU_L2_READING"
                                                        ]["compare"]
                                                    )
                                                ][["CODE", "Indicator"]]
                                                .drop_duplicates()
                                                .to_dict("records")
                                            ],
                                            multi=True,
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


def geocode_address(address):
    """Geocode street address into lat/long."""
    response = geocoder.forward(address)
    coords = response.json()["features"][0]["center"]
    # coords = coords.replace(']', '')
    # coords = coords.replace('[', '')
    return coords


# Slider -> count graph
@app.callback(Output("year_slider", "value"), [Input("count_graph", "selectedData")])
def update_year_slider(count_graph_selected):

    if count_graph_selected is None:
        return [years[0], years[-1]]

    nums = [int(point["pointNumber"]) for point in count_graph_selected["points"]]
    return [min(nums) + years[0], max(nums) + years[-1]]


@app.callback(
    Output("count_graph", "figure"),
    [Input("year_slider", "value"), ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_map(year_slider, country_selector):

    px.set_mapbox_access_token(mapbox_access_token)
    static = {
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
    df = pd.DataFrame(static, columns=["Country", "Reading", "Math", "Science"])
    # 2- - create location column
    df[["longitude", "latitude"]] = df.apply(
        lambda row: pd.Series(geocode_address(row["Country"])), axis=1
    )

    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        size="Reading",
        text="Country",
        color="Reading",
        color_continuous_scale=px.colors.sequential.Jet,
        size_max=30,
        zoom=2.5,
        title="Percentage of students performing below level 2/basic proficiency in all 3 subjects",
    )

    return fig


# Selectors -> maths graph
@app.callback(
    Output("maths_graph", "figure"),
    [Input("year_slider", "value"), Input("maths-xaxis-column", "value"),],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_maths_figure(year_slider, xaxis):
    indicator = xaxis

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        data[
            (data["CODE"] == indicator)
            & (data["Sex"] != "Total")
            & (data["TIME_PERIOD"].isin(years))
        ]
        .groupby(["CODE", "Indicator", "Geographic area", "Sex"])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )
    # fig = go.Figure()
    # fig.add_trace(
    #     go.Bar(
    #         x=years,
    #         y=data[data["CODE"] == indicator]["OBS_VALUE"],
    #         name=data[data["CODE"] == indicator]["Indicator"].unique()[0],
    #     ),
    # )
    # if xaxis:
    #     for value in xaxis:
    #         fig.add_trace(
    #             go.Bar(
    #                 x=years,
    #                 y=data[data["CODE"] == value]["OBS_VALUE"],
    #                 name=data[data["CODE"] == value]["Indicator"].unique()[0],
    #             ),
    #         )

    fig = px.bar(
        df,
        x="Geographic area",
        y="OBS_VALUE",
        color="Sex",
        barmode="group",
        title=name,
        text="TIME_PERIOD"
        # range_y=[0, 100]
        # height=400
    )

    # fig.update_layout(
    #     title="Maths",
    #     #         xaxis_tickfont_size=14,
    #     yaxis=dict(
    #         title="Proportion in %",
    #         #             titlefont_size=16,
    #         #             tickfont_size=14,
    #     ),
    #     legend=dict(orientation="h", y=-0.2),
    #     barmode="group",
    #     #         bargap=0.15, # gap between bars of adjacent location coordinates.
    #     #         bargroupgap=0.1 # gap between bars of the same location coordinate.
    # )

    #     figure = dict(data=traces, layout=layout)
    return fig


# Selectors -> reading graph
@app.callback(
    Output("reading_graph", "figure"),
    [Input("year_slider", "value"), Input("maths-xaxis-column", "value"),],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_reading_figure(year_slider, xaxis):
    indicator = xaxis
    compare = "Sex"

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        data[
            (data["CODE"] == indicator)
            & (data["Sex"] != "Total")
            & (data["TIME_PERIOD"].isin(years))
        ]
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
        .agg({"OBS_VALUE": "mean"})
        .reset_index()
    )
    # df = df.set_index('TIME_PERIOD')

    fig = go.Figure()
    for country in data["Geographic area"].unique():
        fig.add_trace(
            go.Scatter(
                mode="lines+markers",
                name=country,
                x=df[df["Geographic area"] == country]["TIME_PERIOD"],
                y=df[df["Geographic area"] == country]["OBS_VALUE"],
                line=dict(shape="spline", smoothing=1.3, width=1),
                marker=dict(symbol="diamond-open"),
            ),
        )
    fig.update_layout(
        title=name,
        # xaxis=dict(),
        #         xaxis_tickfont_size=14,
        yaxis=dict(
            title="Proportion in %",
            #             titlefont_size=16,
            #             tickfont_size=14,
        ),
        # legend=dict(orientation="h", y=-0.2),
        #         barmode='group',
        #         bargap=0.15, # gap between bars of adjacent location coordinates.
        #         bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    #     figure = dict(data=traces, layout=layout)
    return fig


# Selectors -> reading graph
@app.callback(
    Output("pie_graph", "figure"),
    [Input("year_slider", "value"),],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_compare_figure(year_slider):
    import plotly.figure_factory as ff

    # Group data together
    hist_data = [
        data[data["CODE"] == "EDU_SDG_STU_L1_GLAST_MATH"]["OBS_VALUE"],
        data[data["CODE"] == "EDU_SDG_STU_L1_GLAST_READING"]["OBS_VALUE"],
    ]

    group_labels = [
        "Proportion of children at the end of primary education reaching minimum proficiency in math",
        "Proportion of children at the end of primary education reaching minimum proficiency in reading",
    ]

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=5)

    return fig
