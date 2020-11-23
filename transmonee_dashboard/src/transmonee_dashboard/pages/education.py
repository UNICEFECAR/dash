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

from ..app import app, cache, mapbox_access_token, geocoder, sdmx_url

CARD_TEXT_STYLE = {
    'textAlign': 'center',
    'color': '#0074D9'
}

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
main_graph_df = pd.DataFrame(static_data, columns=["Country", "Reading", "Math", "Science"])


def generate_map(title, data, options):
    return px.scatter_mapbox(
        data,
        title=title,
        **options
    )


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
    "EDUNF_ROFST_L1", 
    "EDUNF_ROFST_L2", 
    "EDUNF_ROFST_L3", 
    "EDUNF_OFST_L1", 
    "EDUNF_OFST_L2", 
    "EDUNF_OFST_L3",
    "EDUNF_NERA_L1_GPIA",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_CR_L3",
    "EDUNF_NER_L02",
    "EDUNF_NERA_L1_GPIA",
    "EDUNF_NERA_L1_PT",
    "EDUNF_GER_L1",
    "EDUNF_GER_L2",
    "EDUNF_GER_L3_T",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_STU_L1_TOT",
    "EDUNF_STU_L2_TOT",
    "EDUNF_STU_L3_TOT"
]

data = pd.DataFrame()
inds = set(codes)
for ind in inds:
    sdmx = pd.read_csv(sdmx_url.format(ind))
    sdmx["CODE"] = ind
    data = data.append(sdmx)

countries = data["Geographic area"].unique()

data = data.merge(
    right=pd.DataFrame(
        [dict(country=country, **geocode_address(country)) for country in countries]
    ),
    left_on='Geographic area',
    right_on='country'
)

# Create controls
county_options = [
    {"label": str(country), "value": str(country)} for country in countries
]

years = [i for i in range(2008, 2019)]

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
            {"name": "Out of School Total", "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3", "suffix": ""},
            {"name": "Participation in organized learning", "indicator": "EDUNF_NERA_L1_GPIA", "suffix": "%"},
            {"name": "Net Intake Rate", "indicator": "EDUNF_NIR_L1_ENTRYAGE", "suffix": "%"},
            {"name": "Completion rate", "indicator": "EDUNF_CR_L3", "suffix": "%"}
        ],
        "MAIN": {
            "name": "Out of School Children",
            "data": data[
                data["CODE"].isin([
                    "EDUNF_ROFST_L1", 
                    "EDUNF_ROFST_L2", 
                    "EDUNF_ROFST_L3", 
                    "EDUNF_OFST_L1", 
                    "EDUNF_OFST_L2", 
                    "EDUNF_OFST_L3"]
                ) & data["TIME_PERIOD"].isin(years)
            ].groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"]
            ).agg({"OBS_VALUE": "last", "longitude": "last", "latitude": "last"}
            ).reset_index(),
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
                height=750
            ),
            "indicators": [
                "EDUNF_ROFST_L1", 
                "EDUNF_ROFST_L2", 
                "EDUNF_ROFST_L3", 
                "EDUNF_OFST_L1", 
                "EDUNF_OFST_L2", 
                "EDUNF_OFST_L3"
            ]
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT"
            ] 
        },
        "RIGHT": {
            "type": "line",
            "options": dict(
                x="TIME_PERIOD",
                y="OBS_VALUE",
                color="Geographic area", 
                hover_name="Geographic area",
                line_shape="spline",
                render_mode="svg"
            ),
            "trace_options": dict(
                mode="lines+markers"
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_GPIA",
                "EDUNF_NERA_L1_PT",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3_T",
                "EDUNF_NIR_L1_ENTRYAGE",
            ],
            "data": data
                .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
                .agg({"OBS_VALUE": "mean"})
                .reset_index() 
        }
    },
    "QUALITY": {
        "NAME": "Learning Quality",
        "CARDS": [
            {"name": "Proficiency in Math", "indicator": "EDU_SDG_STU_L2_MATH", "suffix": "%"},
            {"name": "Proficiency in Reading", "indicator": "EDU_SDG_STU_L2_READING", "suffix": "%"},
            {"name": "Youth/adult literacy rate", "indicator": "EDUNF_LR_L02", "suffix": "%"},
            {"name": "Childhood Educational Development", "indicator": "EDU_SDG_GER_L01", "suffix": "%"}
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
                    "Reading": [52, 23, 54, 47, 22, 64, 64, 79, 43, 44, 55, 41, 38, 26, 26],
                    "Math": [42, 29, 58, 44, 31, 61, 49, 77, 50, 46, 61, 47, 40, 37, 36],
                    "Science": [47, 24, 57, 47, 25, 64, 60, 77, 43, 48, 49, 44, 38, 25, 26],
                }, 
                columns=["Country", "Reading", "Math", "Science"]
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
                height=750
            ),
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_STU_L2_MATH",
                "EDU_SDG_STU_L2_READING",
                "EDU_SDG_STU_L1_GLAST_MATH",
                "EDU_SDG_STU_L1_G2OR3_MATH",
                "EDU_SDG_STU_L1_GLAST_READING",
                "EDU_SDG_STU_L1_G2OR3_READING",
            ] 
        },
        "RIGHT": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD"
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
                .agg({"TIME_PERIOD":"last", "OBS_VALUE": "last"})
                .reset_index() 
            
        }
    },
    
}

def indicator_card(name, indicator, suffix):
    
    indicator = indicator.split(',')
    mean_value = (
        data[data["CODE"].isin(indicator)]
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])["OBS_VALUE"]
        .tail(1)
        .mean().astype(int)
    )
    label = data[data["CODE"].isin(indicator)]["Indicator"].unique()[0] if len(data[data["CODE"].isin(indicator)]["Indicator"].unique()) else "None"
    card = dbc.Card(
        [
            dbc.CardHeader(name),
            dbc.CardBody(
                [
                    html.H4("{}{}".format(mean_value, suffix), style={
                        'fontSize': 40,
                        'textAlign': 'center',
                        'color': '#0074D9'
                    }), 
                    html.P(label, className="card-text", style=CARD_TEXT_STYLE)
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
                                                {"label": value['NAME'], "value": key} for key,value in indicators_dict.items()
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
                                [
                                    
                                ],
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
                            html.Br(),
                        ],
                        # className="row flex-display",
                        id="right-column",
                        # className="eight columns",
                        width=8,
                    ),
                    # end cards
                ]
            ),
            # end first row

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
                        [dcc.Graph(id="time_graph")],
                        # className="pretty_container seven columns",
                    ),
                ],
                # className="row flex-display",
            ),
        ],
    )


@app.callback(
    Output("country_selector", "value"),
    [Input("region_selector", "value")],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def select_region(region):
    if region:
        return region.split(',')
    else:
        return [item["value"] for item in county_options]


@app.callback(
    Output("cards_row", "children"),
    [Input("theme_selector", "value")],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def show_cards(theme):

    return [
        dbc.Col(indicator_card(card["name"], card["indicator"], card["suffix"])) 
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
            data["CODE"].isin(
                indicators_dict[theme]["MAIN"]["indicators"]
            )
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
        Input("main_indicators", "value")
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

    return generate_map(
        name,
        df,
        options
    )


# Selectors -> left graph
@app.callback(
    Output("left_xaxis_column", "options"),
    [
        Input("theme_selector", "value"),
    ],
    # [State("left-xaxis-column", "value")],
)
def left_options(theme):

    return [
        {
            "label": item["Indicator"],
            "value": item["CODE"],
        }
        for item in data[
            data["CODE"].isin(
                indicators_dict[theme]["LEFT"]["indicators"]
            )
        ][["CODE", "Indicator"]]
        .drop_duplicates()
        .to_dict("records")
    ]


# Selectors -> left graph
@app.callback(
    Output("left_graph", "figure"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
        Input("left_xaxis_column", "value"),
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def left_figure(theme, year_slider, countries, xaxis):
    
    fig_type = indicators_dict[theme]["LEFT"]["type"]
    compare = indicators_dict[theme]["LEFT"]["compare"]
    options = indicators_dict[theme]["LEFT"]["options"]
    indicator = xaxis if xaxis else indicators_dict[theme]["LEFT"]["indicators"][0]

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
            data["CODE"].isin(
                indicators_dict[theme]["RIGHT"]["indicators"]
            )
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
    ],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def right_figure(theme, year_slider, countries, left_selected, right_selected):
    
    fig_type = indicators_dict[theme]["RIGHT"]["type"]
    compare = indicators_dict[theme]["RIGHT"]["compare"]
    options = indicators_dict[theme]["RIGHT"]["options"]
    traces = indicators_dict[theme]["RIGHT"].get("trace_options")
    indicators = indicators_dict[theme]["RIGHT"]["indicators"]
    df = indicators_dict[theme]["RIGHT"]["data"]


    indicator = right_selected if right_selected else left_selected or indicators[0]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = df[
            (df["CODE"] == indicator)
            & (df["TIME_PERIOD"].isin(years[slice(*year_slider)]))
            & (df["Geographic area"].isin(countries))
        ]
        

    options["title"] = name

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)

    # fig = go.Figure()
    # for country in data["Geographic area"].unique():
    #     fig.add_trace(
    #         go.Scatter(
    #             mode="lines+markers",
    #             name=country,
    #             x=df[df["Geographic area"] == country]["TIME_PERIOD"],
    #             y=df[df["Geographic area"] == country]["OBS_VALUE"],
    #             line=dict(shape="spline", smoothing=1.3, width=1),
    #             marker=dict(symbol="diamond-open"),
    #         ),
    #     )
    # fig.update_layout(title=name)

    return fig


# Selectors -> reading graph
@app.callback(
    Output("time_graph", "figure"),
    [Input("year_slider", "value"),],
    #     [State("lock_selector", "value"), State("count_graph", "relayoutData")],
)
def make_compare_figure(year_slider):
    
    qutp = data[
    (data["CODE"].isin([
            "EDU_SDG_QUTP_L02",
            "EDU_SDG_QUTP_L1",
            "EDU_SDG_QUTP_L2",
            "EDU_SDG_QUTP_L3",
        ])) & (data["TIME_PERIOD"].isin(years))
    ].groupby(["TIME_PERIOD", "Geographic area"]
    ).agg({"OBS_VALUE": "mean"}
    ).reset_index()
    qutp['Indicator'] = 'Proportion of teachers qualified according to national standards'

    trtp = data[
        (data["CODE"].isin([
                "EDU_SDG_TRTP_L02",
                "EDU_SDG_TRTP_L1",
                "EDU_SDG_TRTP_L2",
                "EDU_SDG_TRTP_L3",
            ])) & (data["TIME_PERIOD"].isin(years))
    ].groupby(["TIME_PERIOD", "Geographic area"]
    ).agg({"OBS_VALUE": "mean"}
    ).reset_index()
    trtp['Indicator'] = 'Proportion of teachers who have received at least the minimum organized teacher training'

    df = qutp.append(trtp)
    df.sort_values('TIME_PERIOD')
    df.set_index('TIME_PERIOD')

    fig = px.bar(
        df, 
        x="Geographic area", 
        y="OBS_VALUE",
        color="Indicator",
        barmode="group",
        animation_frame="TIME_PERIOD", 
        animation_group="Geographic area",
        range_y=[0,100]
    )
    fig.update_layout(legend=dict(orientation="h", yanchor="bottom",))

    return fig
