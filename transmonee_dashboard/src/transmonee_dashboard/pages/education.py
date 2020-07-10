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
import plotly.io as pio
from mapbox import Geocoder

from ..app import app
from ..components import fa

mapbox_access_token = "pk.eyJ1IjoiamNyYW53ZWxsd2FyZCIsImEiOiJja2NkMW02aXcwYTl5MnFwbjdtdDB0M3oyIn0.zkIzPc4NSjLZvrY-DWrlZg"

sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv"

geocoder = Geocoder(access_token=mapbox_access_token)

pio.templates.default = "plotly_white"

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
            "EDUNF_NERA_L1_PT": "Adjusted net enrolment: primary education"
        },
    },
    "EDU_SDG_STU_L1_G2OR3_READING": {
        "name": "Proportion of children in grade 2 or 3 reaching minimum proficiency in math",
        "compare": {
            "EDUNF_ROFST_L1": "Out of school children rate: Primary education"
        },
    },
    "EDU_SDG_STU_L1_G2OR3_MATH": {
        "name": "Proportion of children in grade 2 or 3 reaching minimum proficiency in math",
        "compare": {
            "EDU_SDG_STU_L1_GLAST_READING": "Proportion of children at the end of primary education reaching minimum proficiency in reading"
        },
    },
    "EDU_SDG_GER_L01": {"compare": {}}
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

reading = go.Figure(go.Indicator(
    mode = "number",
    value = data.query("CODE == 'EDU_SDG_STU_L2_READING' & Sex == 'Total'").mean(),
    number = {'prefix': "$"},
px.bar(
    data.query("CODE == 'EDU_SDG_STU_L2_READING' & Sex == 'Total'").groupby(['Sex']).mean().reset_index(), 
    x='Sex', y='OBS_VALUE', color='Sex', range_y=[0, 100], le)

def get_layout(**kwargs):

    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Data Explorer Controls"),
                        dbc.CardBody(
                            [
                                html.P("Filter by year:",
                                       className="control_label",),
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
                                html.P("Filter by Country:",
                                       className="control_label"),
                                dcc.Dropdown(
                                    id="country_selector",
                                    options=county_options,
                                    multi=True,
                                    value=[item["value"]
                                        for item in county_options],
                                    className="dcc_control",
                                ),
                            ]
                        )]),
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
                                                dbc.CardHeader([fa('fa fa-book fa-2x')," Reading"]),
                                                dbc.CardBody(
                                                    [
                                                        html.H5(
                                                            "Card title",
                                                            className="card-title",
                                                        ),
                                                        dcc.Graph(figure=reading),
                                                        html.P(
                                                            "Proportion of children at the end of lower secondary education reaching minimum proficiency in reading",
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
                                            color="info",
                                            outline=True,
                                        )
                                    ),
                                ],
                                # className="mb-4",
                            ),
                            dbc.Row(
                                dbc.Col([
                                    html.Br(),
                                    dbc.Card(
                                        dbc.CardBody(dcc.Graph(id="count_graph")),
                                            # id="countGraphContainer",
                                            # className="pretty_container",
                                    ),
                                    html.Br()
                                ])
                            )
                        ],
                # className="row flex-display",
                        id="right-column",
                                # className="eight columns",
                        width=8
                    ),
                ]
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                        dbc.CardBody([
                            html.Div(
                                [dcc.Graph(id="maths_graph")],
                                className="pretty_container",
                            ),
                            dcc.Dropdown(
                                id="maths-xaxis-column",
                                options=[
                                    {"label": item["Indicator"],
                                        "value": item["CODE"]}
                                    for item in data[
                                        data["CODE"].isin(
                                            indicators_dict["EDU_SDG_STU_L2_MATH"]["compare"].keys(
                                            )
                                        )
                                    ][["CODE", "Indicator"]]
                                    .drop_duplicates()
                                    .to_dict("records")
                                ],
                                multi=True,
                                #                             value=[item for item in indicators],
                                className="dcc_control",
                            )])),
                        ],
                        # className="six columns",
                        width=6
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                        dbc.CardBody([
                            html.Div(
                                [dcc.Graph(id="reading_graph")],
                                className="pretty_container",
                            ),
                            dcc.Dropdown(
                                id="reading-xaxis-column",
                                options=[
                                    {"label": item["Indicator"],
                                        "value": item["CODE"]}
                                    for item in data[
                                        data["CODE"].isin(
                                            indicators_dict["EDU_SDG_STU_L2_READING"]["compare"].keys(
                                            )
                                        )
                                    ][["CODE", "Indicator"]]
                                    .drop_duplicates()
                                    .to_dict("records")
                                ],
                                multi=True,
                                #                             value=[item for item in indicators],
                                className="dcc_control",
                            )])),
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


def geocode_address(address):
    """Geocode street address into lat/long."""
    response = geocoder.forward(address)
    coords = response.json()['features'][0]['center']
    # coords = coords.replace(']', '')
    # coords = coords.replace('[', '')
    return coords

# Slider -> count graph
@ app.callback(Output("year_slider", "value"), [Input("count_graph", "selectedData")])
def update_year_slider(count_graph_selected):

    if count_graph_selected is None:
        return [years[0], years[-1]]

    nums = [int(point["pointNumber"]) for point in count_graph_selected["points"]]
    return [min(nums) + years[0], max(nums) + years[-1]]

@ app.callback(
    Output("count_graph", "figure"),
    [
        Input("year_slider", "value"),
        Input("country_selector", "value")
    ],
#     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_map(year_slider, country_selector):

    px.set_mapbox_access_token(mapbox_access_token)
    df = data[
        (data['CODE'] == 'EDUNF_ROFST_L2') &
        (data['Geographic area'].isin(country_selector))
    ].groupby(['Geographic area', 'CODE', 'Indicator']).agg(
        {'TIME_PERIOD': 'max', 'OBS_VALUE': 'max'}
    ).reset_index()
    # 2- - create location column
    df[['longitude', 'latitude']]= df.apply(lambda row: pd.Series(geocode_address(row['Geographic area'])), axis=1)

    fig=px.scatter_mapbox(
        df,
        lat='latitude',
        lon='longitude',
        size="OBS_VALUE",
        text="Geographic area",
        color="OBS_VALUE",
        color_continuous_scale=px.colors.sequential.Jet,
        size_max=25,
        zoom=2
    )

    return fig


# Selectors -> maths graph
@ app.callback(
    Output("maths_graph", "figure"),
    [
        Input("year_slider", "value"),
        Input("maths-xaxis-column", "value"),
    ],
#     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_maths_figure(year_slider, xaxis):
    indicator='EDU_SDG_STU_L2_MATH'
    dff=data
    fig=go.Figure()
    fig.add_trace(
            go.Bar(
                x=years,
                y=data[data['CODE'] == indicator]['OBS_VALUE'],
                name=indicators_dict[indicator]['name'],
            ),
        )
    if xaxis:
        for value in xaxis:
            fig.add_trace(
                go.Bar(
                    x=years,
                    y=data[data['CODE'] == value]['OBS_VALUE'],
                    name=indicators_dict[indicator]['compare'][value],
                ),
            )
    fig.update_layout(
        title='Maths',
#         xaxis_tickfont_size=14,
        yaxis=dict(
            title='Proportion in %',
#             titlefont_size=16,
#             tickfont_size=14,
        ),
        legend=dict(
            orientation="h",
            y=-0.2
        ),
        barmode='group',
#         bargap=0.15, # gap between bars of adjacent location coordinates.
#         bargroupgap=0.1 # gap between bars of the same location coordinate.
    )


#     figure = dict(data=traces, layout=layout)
    return fig


# Selectors -> reading graph
@ app.callback(
    Output("reading_graph", "figure"),
    [
        Input("year_slider", "value"),
        Input("reading-xaxis-column", "value"),
    ],
#     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_reading_figure(year_slider, xaxis):
    indicator='EDU_SDG_STU_L2_READING'
    dff=data
    fig=go.Figure()
    fig.add_trace(
            go.Scatter(
                mode="lines+markers",
                name=indicators_dict[indicator]['name'],
                x=years,
                y=data[data['CODE'] == indicator]['OBS_VALUE'],
                line=dict(shape="spline", smoothing=1.3,
                          width=1, color="#fac1b7"),
                marker=dict(symbol="diamond-open"),
            ),
        )
    if xaxis:
        for value in xaxis:
            fig.add_trace(
                go.Scatter(
                    mode="lines+markers",
                        name=data[data['CODE'] == value]['Indicator'].unique()[
                                                                             0],
                        x=years,
                        y=data[data['CODE'] == value]['OBS_VALUE'],
                        line=dict(shape="spline", smoothing=1.3, width=1),
                        marker=dict(symbol="diamond-open"),
                ),
            )
    fig.update_layout(
        title='Reading',
#         xaxis_tickfont_size=14,
        yaxis=dict(
            title='Proportion in %',
#             titlefont_size=16,
#             tickfont_size=14,
        ),
        legend=dict(
            orientation="h",
            y=-0.2
        ),
#         barmode='group',
#         bargap=0.15, # gap between bars of adjacent location coordinates.
#         bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
#     figure = dict(data=traces, layout=layout)
    return fig

# Selectors -> reading graph
@ app.callback(
    Output("pie_graph", "figure"),
    [
        Input("year_slider", "value"),
    ],
#     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_compare_figure(year_slider):
    import plotly.figure_factory as ff

    # Group data together
    hist_data=[
        data[data['CODE'] == 'EDU_SDG_STU_L1_GLAST_MATH']['OBS_VALUE'],
        data[data['CODE'] == 'EDU_SDG_STU_L1_GLAST_READING']['OBS_VALUE'],
    ]

    group_labels=[
        'Proportion of children at the end of primary education reaching minimum proficiency in math',
        'Proportion of children at the end of primary education reaching minimum proficiency in reading'
    ]

    # Create distplot with custom bin_size
    fig=ff.create_distplot(hist_data, group_labels, bin_size=5)

    return fig
