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

import dash_treeview_antd

from ..app import app, cache
from . import (
    mapbox_access_token,
    regions,
    years,
    indicators,
    data,
    county_options,
    countries,
)

CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}


px.set_mapbox_access_token(mapbox_access_token)


# TODO:
# _ use of chained callbacks to present list of countries as required by carlos

AREA_KEYS = ["MAIN", "AREA_1", "AREA_2", "AREA_3", "AREA_4"]


def get_base_layout(**kwargs):

    indicators_dict = kwargs.get("indicators")
    return html.Div(
        [
            dcc.Store(id="indicators", data=indicators_dict),
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
                                            # className="dcc_control",
                                        ),
                                        html.Br(),
                                        html.P(
                                            "Filter by year:",
                                            className="control_label",
                                        ),
                                        dcc.RangeSlider(
                                            id="year_slider",
                                            min=0,
                                            max=len(years) - 1,
                                            step=None,
                                            marks={
                                                index: str(year)
                                                for index, year in enumerate(years)
                                            },
                                            value=[0, len(years) - 1],
                                            className="dcc_control",
                                        ),
                                        html.Br(),
                                        html.P(
                                            "Filter by Region:",
                                            className="control_label",
                                        ),
                                        dcc.Dropdown(
                                            id="region_selector",
                                            options=regions,
                                            className="dcc_control",
                                            multi=True,
                                        ),
                                        # TODO: _ make dynamic based on indicators_dict
                                        # (eg: account for TMEE countries only for example --> child protection)
                                        # dbc.Checklist(
                                        #     id="country_selector",
                                        #     options=county_options,
                                        #     value=[
                                        #         item["value"] for item in county_options
                                        #     ],
                                        #     # className="custom-control-input",
                                        # ),
                                        dash_treeview_antd.TreeView(
                                            id="country_selector",
                                            multiple=True,
                                            checkable=True,
                                            checked=["0"],
                                            # selected=[],
                                            # expanded=["0"],
                                            data={
                                                "title": "Regions",
                                                "key": "0",
                                                "children": [
                                                    {
                                                        "title": region["label"],
                                                        "key": f"0-{num1}",
                                                        "children": [
                                                            {
                                                                "title": name,
                                                                "key": f"0-{num1}-{num2}",
                                                            }
                                                            for num2, name in enumerate(
                                                                region["value"].split(
                                                                    ","
                                                                )
                                                            )
                                                        ],
                                                    }
                                                    for num1, region in enumerate(
                                                        regions
                                                    )
                                                ],
                                            },
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
                                        dcc.Graph(id="main_area"),
                                        dcc.Dropdown(
                                            id="main_options",
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
                                            [dcc.Graph(id="area_1")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="area_1_options",
                                            className="dcc_control",
                                        ),
                                        dcc.RadioItems(
                                            id="area_1_breakdowns",
                                            className="dcc_control",
                                            labelStyle={"display": "inline-block"},
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        id="area_1_parent",
                        width=6,
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="area_2")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="area_2_options",
                                            className="dcc_control",
                                        ),
                                        dcc.RadioItems(
                                            id="area_2_types",
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
                        id="area_2_parent",
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
                                            id="area_3_options",
                                            className="dcc_control",
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                        id="area_3_parent",
                    ),
                    dbc.Col(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.Div(
                                            [dcc.Graph(id="area_4")],
                                            className="pretty_container",
                                        ),
                                        dcc.Dropdown(
                                            id="area_4_options",
                                            className="dcc_control",
                                        ),
                                    ]
                                )
                            ),
                        ],
                        # className="six columns",
                        width=6,
                        id="area_4_parent",
                    ),
                ],
            ),
            html.Br(),
        ],
    )


@app.callback(
    Output("area_1_parent", "hidden"),
    Output("area_2_parent", "hidden"),
    Output("area_3_parent", "hidden"),
    Output("area_4_parent", "hidden"),
    Input("theme_selector", "value"),
    State("indicators", "data"),
)
def display_areas(theme, indicators_dict):
    return [area not in indicators_dict[theme] for area in AREA_KEYS if area != "MAIN"]


@cache.memoize()  # will cache based on years and countries combo
def get_filtered_dataset(years, countires):
    print("CACHE BREAK!!")
    return data[
        (data["TIME_PERIOD"].isin(years)) & (data["Geographic area"].isin(countries))
    ]


@app.callback(
    Output("store", "data"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("country_selector", "value"),
    ],
)
def apply_filters(theme, years_slider, countries):
    # cache the data based on selected years and countries
    get_filtered_dataset(years[slice(*years_slider)], countries)
    return theme


def indicator_card(
    card_id,
    name,
    numerator,
    denominator,
    suffix,
    absolute=False,
):
    total_code = ["_T"]  # potentially move to this config
    query = "CODE in @indicator & SEX in @total_code & RESIDENCE in @total_code & WEALTH_QUINTILE in @total_code"
    numors = numerator.split(",")
    indicator = numors
    # select last value for each country
    indicator_values = (
        data.query(query)
        .groupby(
            [
                "Geographic area",
                "TIME_PERIOD",
            ]
        )
        .agg({"OBS_VALUE": "sum", "DATA_SOURCE": "count"})
    ).reset_index()

    numerator_pairs = (
        indicator_values[indicator_values.DATA_SOURCE == len(numors)]
        .groupby("Geographic area", as_index=False)
        .last()
        .set_index(["Geographic area", "TIME_PERIOD"])
    )

    # select the avalible denominators for countiries in selected years
    indicator = [denominator]
    denominator_values = data.query(query).set_index(["Geographic area", "TIME_PERIOD"])
    # select only those denominators that match avalible indicators
    index_intersect = numerator_pairs.index.intersection(denominator_values.index)

    denominators = denominator_values.loc[index_intersect]["OBS_VALUE"]

    indicator_sum = (
        numerator_pairs.loc[index_intersect]["OBS_VALUE"].to_numpy().sum()
        / denominators.to_numpy().sum()
        * 100
        if absolute
        else (
            numerator_pairs["OBS_VALUE"] * denominators / denominators.to_numpy().sum()
        )
        .dropna()  # will drop missing countires
        .to_numpy()
        .sum()
    )
    sources = index_intersect.tolist()

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
                    html.H1(
                        "{:.0f}{}".format(indicator_sum, suffix),
                        className="display-4",
                        style={
                            # "fontSize": 50,
                            "textAlign": "center",
                            "color": "#0074D9",
                        },
                    ),
                    html.P(label, className="card-text"),
                ]
            ),
            dbc.Popover(
                [
                    dbc.PopoverHeader("Sources"),
                    dbc.PopoverBody(str(sources)),
                ],
                id="hover",
                target=card_id,
                trigger="hover",
            ),
        ],
        color="primary",
        outline=True,
        id=card_id,
    )
    return card


def generate_map(title, data, options):
    return px.scatter_mapbox(data, title=title, **options)


@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def show_cards(theme, indicators_dict):
    return [
        dbc.Col(
            indicator_card(
                f"card-{num}",
                card["name"],
                card["indicator"],
                card["denominator"],
                card["suffix"],
                card.get("absolute"),
            )
        )
        for num, card in enumerate(indicators_dict[theme]["CARDS"])
    ]


@app.callback(
    Output("main_options", "options"),
    Output("area_1_options", "options"),
    Output("area_2_options", "options"),
    Output("area_3_options", "options"),
    Output("area_4_options", "options"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def set_options(theme, indicators_dict):

    return [
        [
            {
                "label": item["Indicator"],
                "value": item["CODE"],
            }
            for item in data[
                data["CODE"].isin(indicators_dict[theme][area]["indicators"])
            ][["CODE", "Indicator"]]
            .drop_duplicates()
            .to_dict("records")
        ]
        for area in AREA_KEYS
    ]


@app.callback(
    Output("main_options", "value"),
    Output("area_1_options", "value"),
    Output("area_2_options", "value"),
    Output("area_3_options", "value"),
    Output("area_4_options", "value"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def set_default_values(theme, indicators_dict):

    return [indicators_dict[theme][area].get("default") for area in AREA_KEYS]


@app.callback(
    Output("area_1_breakdowns", "options"),
    [
        Input("area_1_options", "value"),
    ],
)
def breakdown_options(indicator):

    options = []

    for item in [
        {"label": "Sex", "value": "Sex"},
        {"label": "Age", "value": "Age"},
        {"label": "Residence", "value": "Residence"},
        {"label": "Wealth Quintile", "value": "Wealth Quintile"},
    ]:
        if not data[
            (data["CODE"] == indicator) & (data[item["value"]] != "Total")
        ].empty:
            options.append(item)

    return options


@app.callback(
    Output("main_area", "figure"),
    [
        Input("main_options", "value"),
        Input("store", "data"),
    ],
    [
        State("year_slider", "value"),
        State("country_selector", "value"),
        State("indicators", "data"),
    ],
)
def main_figure(indicator, theme, years_slider, countries, indicators_dict):

    name = indicators_dict[theme]["MAIN"]["name"]
    options = indicators_dict[theme]["MAIN"]["options"]
    compare = "Sex"

    total = "Total"  # potentially move to this config
    query = f"CODE in @indicator & {compare} == @total"

    df = (
        get_filtered_dataset(years[slice(*years_slider)], countries)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
        .agg({"OBS_VALUE": "last", "longitude": "last", "latitude": "last"})
        .reset_index()
    )

    return generate_map(name, df, options)


@app.callback(
    Output("area_1", "figure"),
    [
        Input("store", "data"),
        Input("area_1_options", "value"),
        Input("area_1_breakdowns", "value"),
    ],
    [
        State("year_slider", "value"),
        State("country_selector", "value"),
        State("indicators", "data"),
    ],
)
def area_1_figure(theme, indicator, compare, year_slider, countries, indicators_dict):

    fig_type = indicators_dict[theme]["AREA_1"]["type"]
    options = indicators_dict[theme]["AREA_1"]["options"]
    compare = compare or indicators_dict[theme]["AREA_1"]["compare"]

    # data disaggregation unique values
    data_disag_unique = data[compare].unique()

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)[
            (data["CODE"] == indicator)
            & (
                data[compare]
                != (data_disag_unique[0] if len(data_disag_unique) == 1 else "Total")
            )
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
    Output("area_2", "figure"),
    [
        Input("store", "data"),
        Input("area_1_options", "value"),
        Input("area_2_options", "value"),
        Input("area_2_types", "value"),
    ],
    [
        State("year_slider", "value"),
        State("country_selector", "value"),
        State("indicators", "data"),
    ],
)
def area_2_figure(
    theme,
    area_1_selected,
    area_2_selected,
    selected_type,
    year_slider,
    countries,
    indicators_dict,
):

    default = indicators_dict[theme]["AREA_2"]["default_graph"]
    fig_type = selected_type if selected_type else default
    config = indicators_dict[theme]["AREA_2"]["graphs"][fig_type]
    compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")

    indicator = area_2_selected if area_2_selected else area_1_selected
    time = years[slice(*year_slider)]

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    query = "CODE == @indicator"
    if compare:
        query = "{} & {} != 'Total'".format(query, compare)
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
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


@app.callback(
    Output("area_3", "figure"),
    [
        Input("store", "data"),
        Input("area_3_options", "value"),
    ],
    [
        State("year_slider", "value"),
        State("country_selector", "value"),
        State("indicators", "data"),
    ],
)
def area_3_figure(theme, indicator, year_slider, countries, indicators_dict):

    fig_type = indicators_dict[theme]["AREA_3"]["type"]
    compare = indicators_dict[theme]["AREA_3"]["compare"]
    options = indicators_dict[theme]["AREA_3"]["options"]

    total = "Total"  # potentially move to this config
    cohorts = data[data["CODE"] == indicator][compare].unique()
    query = "CODE in @indicator"
    if len(cohorts) > 1:
        query = "{} & {} != @total".format(query, compare)

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

    options["title"] = name
    if len(cohorts) > 1:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    fig.update_xaxes(categoryorder="total descending")
    return fig


@app.callback(
    Output("area_4", "figure"),
    [
        Input("store", "data"),
        Input("area_4_options", "value"),
    ],
    [
        State("year_slider", "value"),
        State("country_selector", "value"),
        State("indicators", "data"),
    ],
)
def area_4_figure(theme, indicator, year_slider, countries, indicators_dict):

    default = indicators_dict[theme]["AREA_4"]["default_graph"]
    fig_type = default
    config = indicators_dict[theme]["AREA_4"]["graphs"][fig_type]
    compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")

    name = data[data["CODE"] == indicator]["Indicator"].unique()[0]
    query = "CODE == @indicator"
    if compare:
        query = "{} & {} != 'Total'".format(query, compare)
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
        .query(query)
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

    # subfig = make_subplots(specs=[[{"secondary_y": True}]])

    # indicator = "EDUNF_DR_L1"
    # line_data = (
    #     data.query(query)
    #     .groupby(["CODE", "Indicator", "Geographic area", compare])
    #     .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
    #     .reset_index()
    # )

    # line = px.line(
    #     line_data,
    #     x="Geographic area",
    #     y="OBS_VALUE",
    #     color=compare,
    #     text="TIME_PERIOD",
    #     # labels={"Indicator": "Dropout Rate"},
    # )
    # line.update_traces(
    #     yaxis="y2",
    #     mode="markers",
    #     marker=dict(size=12, line=dict(width=2, color="DarkSlateGrey")),
    #     # selector=dict(mode="markers"),
    # )

    # subfig.add_traces(fig.data + line.data)

    return fig
