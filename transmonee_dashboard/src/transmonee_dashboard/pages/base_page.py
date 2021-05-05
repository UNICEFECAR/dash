import urllib
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
import numpy as np


import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash import callback_context
from dash.dependencies import Input, Output, State, ClientsideFunction


import plotly.io as pio
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
    eu_engagement,
)

# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = [
    "#1cabe2",
    "#80bd41",
    "#dda63a",
    "#e34e09",
    "#c5effc",
]
px.set_mapbox_access_token(mapbox_access_token)


AREA_KEYS = ["MAIN", "AREA_1", "AREA_2", "AREA_3", "AREA_4"]
DEFAULT_LABELS = {"Geographic area": "Country", "TIME_PERIOD": "Year"}
CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}


def get_base_layout(**kwargs):

    indicators_dict = kwargs.get("indicators")
    return html.Div(
        [
            dcc.Store(id="indicators", data=indicators_dict),
            dbc.Row(
                [
                    dbc.Col(
                        width=True,
                        children=[
                            dbc.Row(
                                [
                                    dbc.Form(
                                        [
                                            dbc.FormGroup(
                                                [
                                                    dbc.Label(
                                                        "Theme:",
                                                        html_for="theme_selector",
                                                    ),
                                                    dbc.RadioItems(
                                                        id="theme_selector",
                                                        options=[
                                                            {
                                                                "label": value["NAME"],
                                                                "value": key,
                                                            }
                                                            for key, value in indicators_dict.items()
                                                        ],
                                                        value=list(
                                                            indicators_dict.keys()
                                                        )[0],
                                                        className="mx-2",
                                                        inline=True,
                                                    ),
                                                ],
                                                className="mr-2 mb-3",
                                            ),
                                            dbc.FormGroup(
                                                [
                                                    dbc.Checkbox(
                                                        id="programme-toggle",
                                                        className="custom-control-input",
                                                    ),
                                                    dbc.Label(
                                                        "Programme Countries Only",
                                                        html_for="programme-toggle",
                                                        className="custom-control-label",
                                                    ),
                                                ],
                                                className="custom-control custom-switch mx-2 mb-3",
                                                check=True,
                                            ),
                                        ],
                                        inline=True,
                                    ),
                                ],
                                justify="center",
                            ),
                            dbc.Row(
                                [
                                    dbc.ButtonGroup(
                                        [
                                            dbc.Button(
                                                f"Years: {years[0]} - {years[-1]}",
                                                id="collapse-years-button",
                                                className="flex-fill",
                                                color="primary",
                                            ),
                                            dbc.Button(
                                                "Countires: All",
                                                id="collapse-countries-button",
                                                className="flex-fill",
                                                color="primary",
                                            ),
                                            dbc.Button(
                                                "EU Engagement: All",
                                                id="collapse-engagements-button",
                                                className="flex-fill",
                                                color="primary",
                                            ),
                                        ],
                                        className="d-flex",
                                    ),
                                ],
                                justify="center",
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.Collapse(
                                            dbc.Card(
                                                dcc.RangeSlider(
                                                    id="year_slider",
                                                    min=0,
                                                    max=len(years) - 1,
                                                    step=None,
                                                    marks={
                                                        index: str(year)
                                                        for index, year in enumerate(
                                                            years
                                                        )
                                                    },
                                                    value=[0, len(years) - 1],
                                                    className="dcc_control",
                                                ),
                                                body=True,
                                            ),
                                            id="collapse-years",
                                        ),
                                    ),
                                    dbc.Col(
                                        dbc.Collapse(
                                            dbc.Card(
                                                dash_treeview_antd.TreeView(
                                                    id="contry_selector",
                                                    multiple=True,
                                                    checkable=True,
                                                    checked=["0"],
                                                    # selected=[],
                                                    # expanded=["0"],
                                                    data={
                                                        "title": "Select All",
                                                        "key": "0",
                                                        "children": [
                                                            {
                                                                "title": region[
                                                                    "label"
                                                                ],
                                                                "key": f"0-{num1}",
                                                                "children": [
                                                                    {
                                                                        "title": name,
                                                                        "key": f"0-{num1}-{num2}",
                                                                    }
                                                                    for num2, name in enumerate(
                                                                        region[
                                                                            "value"
                                                                        ].split(",")
                                                                    )
                                                                ],
                                                            }
                                                            for num1, region in enumerate(
                                                                regions
                                                            )
                                                        ],
                                                    },
                                                ),
                                                body=True,
                                                style={"max-height": "200px"},
                                                className="overflow-auto position-relative",
                                            ),
                                            id="collapse-countries",
                                        ),
                                        style={"max-height": "200px"},
                                    ),
                                    dbc.Col(
                                        dbc.Collapse(
                                            dbc.Card(
                                                dash_treeview_antd.TreeView(
                                                    id="engagement_selector",
                                                    multiple=True,
                                                    checkable=True,
                                                    checked=["0"],
                                                    # selected=[],
                                                    # expanded=["0"],
                                                    data={
                                                        "title": "Select All",
                                                        "key": "0",
                                                        "children": [
                                                            {
                                                                "title": region[
                                                                    "label"
                                                                ],
                                                                "key": f"0-{num1}",
                                                                "children": [
                                                                    {
                                                                        "title": name,
                                                                        "key": f"0-{num1}-{num2}",
                                                                    }
                                                                    for num2, name in enumerate(
                                                                        region[
                                                                            "value"
                                                                        ].split(",")
                                                                    )
                                                                ],
                                                            }
                                                            for num1, region in enumerate(
                                                                eu_engagement
                                                            )
                                                        ],
                                                    },
                                                ),
                                                body=True,
                                            ),
                                            id="collapse-engagements",
                                        ),
                                    ),
                                ],
                                className="mb-3",
                            ),
                        ],
                    ),
                ],
                # align="start",
            ),
            dbc.Row(
                [
                    dbc.CardDeck(
                        id="cards_row",
                    ),
                ]
            ),
            html.Br(),
            # start first row
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    dcc.Dropdown(
                                        id="main_options",
                                        # className="dcc_control",
                                        style={
                                            "z-index": "11",
                                        },
                                    ),
                                    dcc.Graph(id="main_area"),
                                ]
                            ),
                        ),
                    ),
                    dbc.Col(
                        [
                            # start controls side bar
                        ],
                        className="position-absolute",
                    ),
                ],
                className="position-relative",
            ),
            # end first row
            html.Br(),
            dbc.CardDeck(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Dropdown(
                                    id="area_1_options",
                                    # style={"z-index": "15"},
                                ),
                                dcc.Graph(id="area_1"),
                                dbc.RadioItems(
                                    id="area_1_breakdowns",
                                    inline=True,
                                ),
                            ]
                        ),
                        id="area_1_parent",
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Dropdown(
                                    id="area_2_options",
                                    className="dcc_control",
                                ),
                                html.Div(
                                    [dcc.Graph(id="area_2")],
                                    className="pretty_container",
                                ),
                                dbc.RadioItems(
                                    id="area_2_types",
                                    options=[
                                        {"label": "Line", "value": "line"},
                                        {"label": "Bar", "value": "bar"},
                                    ],
                                    inline=True,
                                ),
                            ]
                        ),
                        id="area_2_parent",
                    ),
                ],
            ),
            html.Br(),
            dbc.CardDeck(
                [
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Dropdown(
                                    id="area_3_options",
                                    className="dcc_control",
                                ),
                                dcc.Graph(id="area_3"),
                            ]
                        ),
                        id="area_3_parent",
                    ),
                    dbc.Card(
                        dbc.CardBody(
                            [
                                dcc.Dropdown(
                                    id="area_4_options",
                                    className="dcc_control",
                                ),
                                dcc.Graph(id="area_4"),
                            ]
                        ),
                        id="area_4_parent",
                    ),
                ],
            ),
            html.Br(),
        ],
    )


@app.callback(
    Output("collapse-years", "is_open"),
    Output("collapse-countries", "is_open"),
    Output("collapse-engagements", "is_open"),
    [
        Input("collapse-years-button", "n_clicks"),
        Input("collapse-countries-button", "n_clicks"),
        Input("collapse-engagements-button", "n_clicks"),
    ],
    [
        State("collapse-years-button", "is_open"),
        State("collapse-countries-button", "is_open"),
        State("collapse-engagements-button", "is_open"),
    ],
)
def toggle_collapse(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "collapse-years-button" and n1:
        return not is_open1, False, False
    elif button_id == "collapse-countries-button" and n2:
        return False, not is_open2, False
    elif button_id == "collapse-engagements-button" and n3:
        return False, False, not is_open3
    return False, False, False


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
    print("RECACHING!!")
    return data[
        (data["TIME_PERIOD"].isin(years)) & (data["Geographic area"].isin(countries))
    ]


@app.callback(
    Output("store", "data"),
    [
        Input("theme_selector", "value"),
        Input("year_slider", "value"),
        Input("contry_selector", "value"),
    ],
)
def apply_filters(theme, years_slider, countries):
    trigger = callback_context.triggered[0]
    print(trigger)
    # cache the data based on selected years and countries
    get_filtered_dataset(years[slice(*years_slider)], countries)
    return theme


def indicator_card(
    card_id,
    name,
    numerator,
    suffix,
    denominator=None,
    absolute=False,
    sex_code=None,
):
    total_code = ["_T"]  # potentially move to this config
    sex_code = sex_code if sex_code else total_code
    query = "CODE in @indicator & SEX in @sex_code & RESIDENCE in @total_code & WEALTH_QUINTILE in @total_code"
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

    # check for denominator
    if denominator:

        # select the avalible denominators for countiries in selected years
        indicator = [denominator]
        denominator_values = data.query(query).set_index(
            ["Geographic area", "TIME_PERIOD"]
        )
        # select only those denominators that match avalible indicators
        index_intersect = numerator_pairs.index.intersection(denominator_values.index)

        denominators = denominator_values.loc[index_intersect]["OBS_VALUE"]

        indicator_sum = (
            numerator_pairs.loc[index_intersect]["OBS_VALUE"].to_numpy().sum()
            / denominators.to_numpy().sum()
            * 100
            if absolute
            else (
                numerator_pairs["OBS_VALUE"]
                * denominators
                / denominators.to_numpy().sum()
            )
            .dropna()  # will drop missing countires
            .to_numpy()
            .sum()
        )
        sources = index_intersect.tolist()

    elif suffix.lower() == "countries":
        # this is a hack to accomodate small cases (to discuss with James)
        if "FREE" in numerator:
            # trick to filter number of years of free education
            indicator_sum = (numerator_pairs.OBS_VALUE >= 1).to_numpy().sum()
            sources = numerator_pairs.index.tolist()
        elif absolute:
            # trick cards data availability among group of indicators and latest time_period
            # doesn't require filtering by count == len(numors)
            numerator_pairs = indicator_values.groupby(
                "Geographic area", as_index=False
            ).last()
            max_time_filter = (
                numerator_pairs.TIME_PERIOD < numerator_pairs.TIME_PERIOD.max()
            )
            numerator_pairs.drop(numerator_pairs[max_time_filter].index, inplace=True)
            numerator_pairs.set_index(["Geographic area", "TIME_PERIOD"], inplace=True)
            sources = numerator_pairs.index.tolist()
            indicator_sum = len(sources)
        else:
            # trick to accomodate cards for admin exams (AND for boolean indicators)
            # filter exams according to number of indicators
            indicator_sum = (numerator_pairs.OBS_VALUE == len(numors)).to_numpy().sum()
            sources = numerator_pairs.index.tolist()

    else:
        indicator_sum = numerator_pairs["OBS_VALUE"].to_numpy().sum()
        sources = numerator_pairs.index.tolist()

    label = (
        data[data["CODE"].isin(indicator)]["Indicator"].unique()[0]
        if len(data[data["CODE"].isin(indicator)]["Indicator"].unique())
        else "None"
    )
    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H1(
                        "{:,.0f}".format(indicator_sum),
                        className="display-4",
                        style={
                            # "fontSize": 50,
                            "textAlign": "center",
                            "color": "#1cabe2",
                        },
                    ),
                    html.H4(suffix, className="card-title"),
                    html.P(name, className="lead"),
                ],
                style={
                    # "fontSize": 50,
                    "textAlign": "center",
                },
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


@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("cards_row", "children"), State("indicators", "data")],
)
def show_cards(theme, current_cards, indicators_dict):
    cards = [
        indicator_card(
            f"card-{num}",
            card["name"],
            card["indicator"],
            card["suffix"],
            card.get("denominator"),
            card.get("absolute"),
            card.get("sex"),
        )
        for num, card in enumerate(indicators_dict[theme]["CARDS"])
    ]
    return cards


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
    # potentially only use cached version
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


def get_disag_total(data, indicator, dimension, default_total="Total"):
    data_disag_unique = data[data["CODE"] == indicator][dimension].unique()
    return data_disag_unique[0] if len(data_disag_unique) == 1 else default_total


@app.callback(
    Output("area_1_breakdowns", "options"),
    [
        Input("area_1_options", "value"),
    ],
)
def breakdown_options(indicator):

    options = [{"label": "Total", "value": "Total"}]

    for item in [
        {"label": "Sex", "value": "Sex"},
        {"label": "Age", "value": "Age"},
        {"label": "Residence", "value": "Residence"},
        {"label": "Wealth Quintile", "value": "Wealth Quintile"},
    ]:
        if not data[
            (data["CODE"] == indicator)
            & (data[item["value"]] != get_disag_total(data, indicator, item["value"]))
        ].empty:
            options.append(item)

    return options


@app.callback(
    # Output("main_options", "value"),
    Output("area_1_breakdowns", "value"),
    # Output("area_2_options", "value"),
    # Output("area_3_options", "value"),
    # Output("area_4_options", "value"),
    [
        Input("area_1_breakdowns", "options"),
    ],
    [
        State("indicators", "data"),
    ],
)
def set_default_compare(compare_options, indicators_dict):

    return (
        compare_options[1]["value"]
        if len(compare_options) > 1
        else compare_options[0]["value"]
    )


@app.callback(
    Output("main_area", "figure"),
    [
        Input("main_options", "value"),
        Input("store", "data"),
    ],
    [
        State("year_slider", "value"),
        State("contry_selector", "value"),
        State("indicators", "data"),
    ],
)
def main_figure(indicator, theme, years_slider, countries, indicators_dict):

    options = indicators_dict[theme]["MAIN"]["options"]
    compare = "Sex"

    total = "Total"  # potentially move to this config
    query = f"CODE in @indicator & {compare} == @total"

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    df = (
        get_filtered_dataset(years[slice(*years_slider)], countries)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
        .agg({"OBS_VALUE": "last", "longitude": "last", "latitude": "last"})
        .reset_index()
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name

    return px.scatter_mapbox(df, **options)


@app.callback(
    Output("area_1", "figure"),
    [
        Input("store", "data"),
        Input("area_1_options", "value"),
        Input("area_1_breakdowns", "value"),
    ],
    [
        State("year_slider", "value"),
        State("contry_selector", "value"),
        State("indicators", "data"),
    ],
)
def area_1_figure(theme, indicator, compare, year_slider, countries, indicators_dict):

    fig_type = indicators_dict[theme]["AREA_1"]["type"]
    options = indicators_dict[theme]["AREA_1"]["options"]
    compare = False if compare == "Total" else compare

    columns = [
        "CODE",
        "Indicator",
        "Geographic area",
    ]
    aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
    query = "CODE == @indicator"
    if compare:
        columns.append(compare)
        total = get_disag_total(data, indicator, compare)
        query = "{} & {} != '{}'".format(query, compare, total)

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
        .query(query)
        .groupby(columns)
        .agg(aggregates)
        .reset_index()
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
    if compare:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    # fig.update_layout(title_x=1)
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
        State("contry_selector", "value"),
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

    columns = ["CODE", "Indicator", "Geographic area"]
    aggregates = {"OBS_VALUE": "mean"}
    query = "CODE == @indicator"
    if compare:
        columns.append(compare)
        aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
        total = get_disag_total(data, indicator, compare)
        query = "{} & {} != '{}'".format(query, compare, total)
    else:
        # if no compare then get single value for the year
        columns.append("TIME_PERIOD")

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
        .query(query)
        .groupby(columns)
        .agg(aggregates)
        .reset_index()
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
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
        State("contry_selector", "value"),
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

    df = (
        get_filtered_dataset(years[slice(*year_slider)], countries)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

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
        State("contry_selector", "value"),
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
