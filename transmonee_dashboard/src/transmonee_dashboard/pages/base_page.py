from re import split
import re
import urllib
import pickle
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
import numpy as np
from itertools import cycle


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

from ..components import fa
from ..app import app, cache
from . import (
    mapbox_access_token,
    unicef_country_prog,
    programme_country_indexes,
    selection_index,
    selection_tree,
    countries,
    years,
    data,
    countries_dict_filter,
    countries_dict,
)
from flask import current_app as server

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

colours = [
    "primary",
    "success",
    "warning",
    "danger",
    "secondary",
    "info",
    "success",
    "danger",
]
AREA_KEYS = ["MAIN", "AREA_1", "AREA_2", "AREA_3", "AREA_4"]
DEFAULT_LABELS = {"Geographic area": "Country", "TIME_PERIOD": "Year"}
CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}


def get_base_layout(**kwargs):

    indicators_dict = kwargs.get("indicators")
    # I changed this to correctly read the hash as you were reading the name which is different
    url_hash = (
        kwargs.get("hash")
        if kwargs.get("hash")
        else "#{}".format((next(iter(indicators_dict.items())))[0].lower())
        # else "#{}".format(next(iter(indicators_dict.values()))["NAME"].lower())
    )

    return html.Div(
        [
            dcc.Store(id="indicators", data=indicators_dict),
            dcc.Location(id="theme"),
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.ButtonGroup(
                                        id="themes",
                                    ),
                                ],
                                id="theme-row",
                                # width=4,
                                className="my-2",
                                # no_gutters=True,
                                justify="center",
                            ),
                            dbc.Row(
                                [
                                    dbc.DropdownMenu(
                                        label=f"Years: {years[0]} - {years[-1]}",
                                        id="collapse-years-button",
                                        className="m-2",
                                        color="info",
                                        # block=True,
                                        children=[
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
                                                    value=[0, len(years)],
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                    "minWidth": "500px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                    dbc.DropdownMenu(
                                        label=f"Countries: {len(countries)}",
                                        id="collapse-countries-button",
                                        className="m-2",
                                        color="info",
                                        # block=True,
                                        children=[
                                            dbc.Card(
                                                dash_treeview_antd.TreeView(
                                                    id="country_selector",
                                                    multiple=True,
                                                    checkable=True,
                                                    checked=["0"],
                                                    # selected=[],
                                                    expanded=["0"],
                                                    data=selection_tree,
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                    # "maxWidth": "300px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                    dbc.FormGroup(
                                        [
                                            dbc.Checkbox(
                                                id="programme-toggle",
                                                className="custom-control-input",
                                            ),
                                            dbc.Label(
                                                "UNICEF Country Programmes",
                                                html_for="programme-toggle",
                                                className="custom-control-label",
                                                color="primary",
                                            ),
                                        ],
                                        className="custom-control custom-switch m-2",
                                        check=True,
                                        inline=True,
                                    ),
                                ],
                                id="filter-row",
                                no_gutters=True,
                                justify="center",
                            ),
                        ]
                    ),
                ],
                # sticky="top",
                className="sticky-top bg-light",
            ),
            dbc.Row(
                [
                    dbc.CardDeck(
                        id="cards_row",
                        className="mt-3",
                    ),
                ],
                justify="center",
            ),
            html.Br(),
            # start first row
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    id="main_area_title",
                                ),
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id="main_options",
                                            # className="dcc_control",
                                            style={
                                                "zIndex": "11",
                                            },
                                        ),
                                        dcc.Graph(id="main_area"),
                                        html.Div(
                                            fa("fas fa-info-circle"),
                                            id="main_area_info",
                                            className="float-right",
                                        ),
                                        dbc.Popover(
                                            [
                                                dbc.PopoverHeader("Sources"),
                                                dbc.PopoverBody(id="main_area_sources"),
                                            ],
                                            id="hover",
                                            target="main_area_info",
                                            trigger="hover",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            # end first row
            html.Br(),
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                id="area_1_title",
                            ),
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
                                    html.Div(
                                        fa("fas fa-info-circle"),
                                        id="area_1_info",
                                        className="float-right",
                                    ),
                                    dbc.Popover(
                                        [
                                            dbc.PopoverHeader("Sources"),
                                            dbc.PopoverBody(id="area_1_sources"),
                                        ],
                                        id="hover",
                                        target="area_1_info",
                                        trigger="hover",
                                    ),
                                ]
                            ),
                        ],
                        id="area_1_parent",
                    ),
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                id="area_2_title",
                            ),
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
                                    html.Div(
                                        fa("fas fa-info-circle"),
                                        id="area_2_info",
                                        className="float-right",
                                    ),
                                    dbc.Popover(
                                        [
                                            dbc.PopoverHeader("Sources"),
                                            dbc.PopoverBody(id="area_2_sources"),
                                        ],
                                        id="hover",
                                        target="area_2_info",
                                        trigger="hover",
                                    ),
                                ]
                            ),
                        ],
                        id="area_2_parent",
                    ),
                ],
            ),
            html.Br(),
            dbc.CardDeck(
                [
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                id="area_3_title",
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Dropdown(
                                        id="area_3_options",
                                        className="dcc_control",
                                    ),
                                    dcc.Graph(id="area_3"),
                                    html.Div(
                                        fa("fas fa-info-circle"),
                                        id="area_3_info",
                                        className="float-right",
                                    ),
                                    dbc.Popover(
                                        [
                                            dbc.PopoverHeader("Sources"),
                                            dbc.PopoverBody(id="area_3_sources"),
                                        ],
                                        id="hover",
                                        target="area_3_info",
                                        trigger="hover",
                                    ),
                                ]
                            ),
                        ],
                        id="area_3_parent",
                    ),
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                id="area_4_title",
                            ),
                            dbc.CardBody(
                                [
                                    dcc.Dropdown(
                                        id="area_4_options",
                                        className="dcc_control",
                                    ),
                                    dcc.Graph(id="area_4"),
                                    html.Div(
                                        fa("fas fa-info-circle"),
                                        id="area_4_info",
                                        className="float-right",
                                    ),
                                    dbc.Popover(
                                        [
                                            dbc.PopoverHeader("Sources"),
                                            dbc.PopoverBody(id="area_4_sources"),
                                        ],
                                        id="hover",
                                        target="area_4_info",
                                        trigger="hover",
                                    ),
                                ]
                            ),
                        ],
                        id="area_4_parent",
                    ),
                ],
            ),
            html.Br(),
        ],
    )


# TODO: Move to client side call back
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
    Input("theme", "hash"),
    State("indicators", "data"),
)
def display_areas(theme, indicators_dict):
    theme = theme[1:].upper() if theme else next(iter(indicators_dict.keys()))
    return [area not in indicators_dict[theme] for area in AREA_KEYS if area != "MAIN"]


@cache.memoize()  # will cache based on years and countries combo
def get_filtered_dataset(theme, years, countries):

    print("RE-CACHING!!")

    return data[
        (data["TIME_PERIOD"].isin(years)) & (data["Geographic area"].isin(countries))
    ]


@app.callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    Output("programme-toggle", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
        Input("programme-toggle", "checked"),
    ],
    [
        State("indicators", "data"),
    ],
)
def apply_filters(theme, years_slider, country_selector, programme_toggle, indicators):
    ctx = dash.callback_context

    selected = ctx.triggered[0]["prop_id"].split(".")[0]

    countries_selected = set()
    if programme_toggle and selected == "programme-toggle":
        countries_selected = unicef_country_prog
        country_selector = programme_country_indexes
    elif not country_selector:
        countries_selected = countries
    else:
        for index in country_selector:
            countries_selected.update(selection_index[index])
            if countries_selected == countries:
                # if all countries are all selectred then stop
                break

    country_text = f"{len(list(countries_selected))} Selected"

    selected_years = years[slice(*years_slider)]

    # Use the dictionary to return the values of the selected countries based on the SDMX codes
    countries_selected = countries_dict_filter(countries_dict, countries_selected)

    # cache the data based on selected years and countries
    selections = dict(
        theme=theme[1:].upper() if theme else next(iter(indicators.keys())),
        years=selected_years,
        countries=list(
            countries_selected.values()
        ),  # use the values after the change done
    )

    get_filtered_dataset(**selections)

    return (
        selections,
        country_selector,
        countries_selected == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def indicator_card(
    selections,
    card_id,
    name,
    numerator,
    suffix,
    denominator=None,
    absolute=False,
    sex_code="Total",
):

    # indicator could be a list --> great use of " in " instead of " == " !!!
    query = "CODE in @indicator"

    numors = numerator.split(",")

    # build the (target + rest total) query
    # target code is Total unless is not None
    sex_code = sex_code if sex_code else "Total"
    # use one of the numerators if more than one --> assume all have the same disaggregation
    # other possibility could be to generalize more get_target_query function ...
    target_and_total_query = get_target_query(data, numors[0], "Sex", sex_code)
    query = query + " & " + target_and_total_query
    # query = "CODE in @indicator & SEX in @sex_code & RESIDENCE in @total_code & WEALTH_QUINTILE in @total_code"
    indicator = numors

    # use filtered chached dataset
    filtered_data = get_filtered_dataset(**selections)

    # select last value for each country
    indicator_values = (
        filtered_data.query(query)
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

        # select the available denominators for countries in selected years
        indicator = [denominator]
        # reset the query for denominator
        query = "CODE in @indicator"

        # so far denominator is thought to be a single one right?
        # possibly --> generalize to more than one --> as numerator
        # build the query for denominator, naturally --> uses same sex_code
        target_and_total_query = get_target_query(data, denominator, "Sex", sex_code)
        query = query + " & " + target_and_total_query

        denominator_values = filtered_data.query(query).set_index(
            ["Geographic area", "TIME_PERIOD"]
        )
        # select only those denominators that match available indicators
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
            .dropna()  # will drop missing countries
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
        filtered_data[filtered_data["CODE"].isin(indicator)]["Indicator"].unique()[0]
        if len(
            filtered_data[filtered_data["CODE"].isin(indicator)]["Indicator"].unique()
        )
        else "None"
    )
    print(name)
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
                    html.Div(
                        fa("fas fa-info-circle"),
                        id=f"{card_id}_info",
                        # className="float-right",
                        style={
                            "position": "absolute",
                            "bottom": "10px",
                            "right": "10px",
                        },
                    ),
                ],
                style={
                    # "fontSize": 50,
                    "textAlign": "center",
                },
            ),
            dbc.Popover(
                [
                    dbc.PopoverHeader(f"Sources: {indicator}"),
                    dbc.PopoverBody(
                        dcc.Markdown(get_card_popover_body(sources))
                    ),  # replace the tooltip with the desired bullet list layout),
                ],
                id="hover",
                target=f"{card_id}_info",
                trigger="hover",
            ),
        ],
        color="primary",
        outline=True,
        id=card_id,
    )
    return card


# This function is used to generate the list of countries that are part of the card's displayed result;
# it displays the countries as a list, each on a separate line...
def get_card_popover_body(sources):
    countries = []
    for index, source_info in enumerate(sources):
        countries.append(f"- {source_info[0]}: {source_info[1]}")
    card_countries = "\n".join(countries)
    print(card_countries)
    return card_countries


@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("cards_row", "children"), State("indicators", "data")],
)
def show_cards(selections, current_cards, indicators_dict):
    cards = [
        indicator_card(
            selections,
            f"card-{num}",
            card["name"],
            card["indicator"],
            card["suffix"],
            card.get("denominator"),
            card.get("absolute"),
            card.get("sex"),
        )
        for num, card in enumerate(indicators_dict[selections["theme"]]["CARDS"])
    ]
    return cards


# Added this function to add the button group and set the correct active button
@app.callback(
    Output("themes", "children"),
    [
        Input("store", "data"),
    ],
    [State("themes", "children"), State("indicators", "data")],
)
def show_themes(selections, current_themes, indicators_dict):
    url_hash = "#{}".format((next(iter(selections.items())))[1].lower())

    buttons = [
        dbc.Button(
            value["NAME"],
            id=key,
            color=colours[num],
            className="theme mx-1",
            href=f"#{key.lower()}",
            active=url_hash == f"#{key.lower()}",
        )
        for num, (key, value) in enumerate(indicators_dict.items())
    ]
    return buttons


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
                data["CODE"].isin(indicators_dict[theme["theme"]][area]["indicators"])
            ][["CODE", "Indicator"]]
            .drop_duplicates()
            .to_dict("records")
        ]
        if area in indicators_dict[theme["theme"]]
        # empty string
        else [{"label": "", "value": ""}]
        for area in AREA_KEYS
    ]


@app.callback(
    Output("main_area_title", "children"),
    Output("area_1_title", "children"),
    Output("area_2_title", "children"),
    Output("area_3_title", "children"),
    Output("area_4_title", "children"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def set_areas_titles(theme, indicators_dict):
    return [
        # use the get by key instead of [] to avoid keyerror exception when the name is not defined
        indicators_dict[theme["theme"]][area].get("name")
        if area in indicators_dict[theme["theme"]]
        # empty string
        else ""
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

    return [
        indicators_dict[theme["theme"]][area].get("default")
        if area in indicators_dict[theme["theme"]]
        else ""
        for area in AREA_KEYS
    ]


@app.callback(
    Output("area_2_types", "value"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def set_default_chart_types(theme, indicators_dict):
    # set the default chart type value for area 2 as by default nothing is selected and the chart is displayed by default
    area = AREA_KEYS[2]
    return indicators_dict[theme["theme"]][area].get("default_graph")


# does this function assume dimension is a disaggregation?
# should we call it only if dimension is a disaggregation?
def get_disag_total(data, indicator, dimension, default_total="Total"):

    data_disag_col = data[data["CODE"] == indicator][dimension]
    max_val_count = data_disag_col.value_counts().idxmax()

    # return max_val_count only if Total not in dimension
    return [default_total if default_total in data_disag_col.values else max_val_count]


# this could be a potential function to be decorated per indicator in each area?
# area_1 breakdown does the first part of this
def get_total_query(data, indicator, neq=False, dimension=None):

    dimensions = ["Sex", "Age", "Residence", "Wealth Quintile"]
    disag = []

    for item in dimensions:
        if len(data[data["CODE"] == indicator][item].unique()) > 1:
            disag.append(item)

    if not disag:
        return None
    elif neq:
        query_dim = " & ".join(
            f"`{dimension}` != '{total}'"
            for total in get_disag_total(data, indicator, dimension)
        )

        query_item = []
        for item in disag:
            if item != dimension:
                item_total = []
                # realized loop below could be replaced with query like:
                # f"`{item}` in @total" --> great use of this !!!
                for total in get_disag_total(data, indicator, item):
                    item_total.append(f"`{item}` == '{total}'")
                query_item.append(f"({' | '.join(item_total)})")
        query_rest = " & ".join(query_item)
        # return " & ".join(query_item)

        # query_rest = " & ".join(
        #     f"`{item}` == '{total}'"
        #     for item in disag
        #     for total in get_disag_total(data, indicator, item)
        #     if item != dimension
        # )

        return (query_dim + " & " + query_rest) if query_rest else query_dim

    else:

        query_item = []
        for item in disag:
            item_total = []
            for total in get_disag_total(data, indicator, item):
                item_total.append(f"`{item}` == '{total}'")
            query_item.append(f"({' | '.join(item_total)})")
        return " & ".join(query_item)

        # return " & ".join(
        #     f"({' | '.join([f"`{item}` == '{total}'"])})"
        #     for item in disag
        #     for total in get_disag_total(data, indicator, item)
        # )


# targets one dimension to a code and the remaining total
# assumes previous knowledge ON the EXISTANCE of the target_code for the dimension
def get_target_query(data, indicator, dimension="Sex", target_code="Total"):

    dimensions = ["Sex", "Age", "Residence", "Wealth Quintile"]
    disag = [
        item
        for item in dimensions
        if (
            (len(data[data["CODE"] == indicator][item].unique()) > 1)
            & (item != dimension)
        )
    ]

    query_dim = f"`{dimension}` == '{target_code}'"

    if not disag:
        return query_dim
    else:
        query_item = []
        for item in disag:
            item_total = []
            disag_total = get_disag_total(data, indicator, item)
            for total in disag_total:
                item_total.append(f"`{item}` == '{total}'")
            query_item.append(f"({' | '.join(item_total)})")
        return query_dim + " & " + " & ".join(query_item)


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

        # OR: compute data[data["CODE"] == indicator] once outside loop?
        if len(data[data["CODE"] == indicator][item["value"]].unique()) > 1:
            options.append(item)

    return options


# Beto's Note: does it make sense to have default compare in config?
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
    Output("main_area_sources", "children"),
    [
        Input("main_options", "value"),
        Input("store", "data"),
    ],
    [
        State("indicators", "data"),
    ],
)
def main_figure(indicator, selections, indicators_dict):

    options = indicators_dict[selections["theme"]]["MAIN"]["options"]
    # compare = "Sex"

    # total = "Total"  # potentially move to this config
    query = "CODE == @indicator"
    total_if_disag_query = get_total_query(data, indicator)
    query = (query + " & " + total_if_disag_query) if total_if_disag_query else query

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    source = data[data["CODE"] == indicator]["DATA_SOURCE"].unique()[0]

    df = (
        get_filtered_dataset(**selections)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", "TIME_PERIOD"])
        .agg({"OBS_VALUE": "last", "longitude": "last", "latitude": "last"})
        .sort_values(
            by=["TIME_PERIOD"]
        )  # Add sorting by Year to display the years in proper order
        .reset_index()
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
    main_figure = px.scatter_mapbox(df, **options)
    # check if this area's config has an animation frame and hence a slider
    if len(main_figure.layout["sliders"]) > 0:
        # set last frame as the active one; i.e. select the max year as the default displayed year
        main_figure.layout["sliders"][0]["active"] = len(main_figure.frames) - 1
        # assign the data of the last year to the map; without this line the data will show the first year;
        main_figure = go.Figure(
            data=main_figure["frames"][-1]["data"],
            frames=main_figure["frames"],
            layout=main_figure.layout,
        )
    return main_figure, source


@app.callback(
    Output("area_1", "figure"),
    Output("area_1_sources", "children"),
    [
        Input("store", "data"),
        Input("area_1_options", "value"),
        Input("area_1_breakdowns", "value"),
    ],
    [
        State("indicators", "data"),
    ],
)
def area_1_figure(selections, indicator, compare, indicators_dict):

    # only run if indicator not empty
    if not indicator:
        return {}, {}

    fig_type = indicators_dict[selections["theme"]]["AREA_1"]["type"]
    options = indicators_dict[selections["theme"]]["AREA_1"]["options"]
    compare = False if compare == "Total" else compare

    columns = ["CODE", "Indicator", "Geographic area"]
    aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
    query = "CODE == @indicator"

    if compare:
        columns.append(compare)
        # total = get_disag_total(data, indicator, compare)
        # query = "{} & `{}` != '{}'".format(query, compare, total)
        total_if_disag_query = get_total_query(data, indicator, True, compare)
    else:
        total_if_disag_query = get_total_query(data, indicator)

    query = (query + " & " + total_if_disag_query) if total_if_disag_query else query

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    source = data[data["CODE"] == indicator]["DATA_SOURCE"].unique()[0]
    df = (
        get_filtered_dataset(**selections)
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

    return fig, source


@app.callback(
    Output("area_2", "figure"),
    Output("area_2_sources", "children"),
    [
        Input("store", "data"),
        Input("area_1_options", "value"),
        Input("area_2_options", "value"),
        Input("area_2_types", "value"),
    ],
    [
        State("indicators", "data"),
    ],
)
def area_2_figure(
    selections,
    area_1_selected,
    area_2_selected,
    selected_type,
    indicators_dict,
):

    # only run if both areas (1 and 2) not empty
    if not area_1_selected and not area_2_selected:
        return {}, {}

    default = indicators_dict[selections["theme"]]["AREA_2"]["default_graph"]
    fig_type = selected_type if selected_type else default
    config = indicators_dict[selections["theme"]]["AREA_2"]["graphs"][fig_type]
    # compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")

    indicator = area_2_selected if area_2_selected else area_1_selected
    columns = ["CODE", "Indicator", "Geographic area"]
    # aggregates = {"OBS_VALUE": "mean"}
    query = "CODE == @indicator"

    # assuming area_2 is for totals, then use area_1 logic for totals
    total_if_disag_query = get_total_query(data, indicator)
    query = (query + " & " + total_if_disag_query) if total_if_disag_query else query

    # query data based on cache
    data_cached = get_filtered_dataset(**selections).query(query)

    # toggle time-series selection based on figure type
    if fig_type == "bar":
        # get rid of time-series for bar plot
        aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
        df = data_cached.groupby(columns).agg(aggregates).reset_index()
    else:
        # line plot: uses query directly keeping time series
        df = data_cached

    # if compare:
    #     columns.append(compare)
    #     aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
    #     total = get_disag_total(data, indicator, compare)
    #     query = "{} & `{}` != '{}'".format(query, compare, total)
    # else:
    #     # if no compare then get single value for the year
    #     columns.append("TIME_PERIOD")

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    source = data[data["CODE"] == indicator]["DATA_SOURCE"].unique()[0]

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name

    # if compare:
    #     options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)
    fig.update_xaxes(categoryorder="total descending")

    return fig, source


@app.callback(
    Output("area_3", "figure"),
    Output("area_3_sources", "children"),
    [
        Input("store", "data"),
        Input("area_3_options", "value"),
    ],
    [
        State("indicators", "data"),
    ],
)
def area_3_figure(selections, indicator, indicators_dict):

    # only run if indicator not empty
    if not indicator or not "AREA_3" in indicators_dict[selections["theme"]]:
        return {}, {}

    fig_type = indicators_dict[selections["theme"]]["AREA_3"]["type"]
    compare = indicators_dict[selections["theme"]]["AREA_3"]["compare"]
    options = indicators_dict[selections["theme"]]["AREA_3"]["options"]

    total = "Total"  # potentially move to this config
    cohorts = data[data["CODE"] == indicator][compare].unique()
    query = "CODE in @indicator"
    if len(cohorts) > 1:
        query = "{} & {} != @total".format(query, compare)

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    source = data[data["CODE"] == indicator]["DATA_SOURCE"].unique()[0]
    df = (
        get_filtered_dataset(**selections)
        .query(query)
        .groupby(["CODE", "Indicator", "Geographic area", compare])
        .agg({"TIME_PERIOD": "last", "OBS_VALUE": "last"})
        .reset_index()
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
    if len(cohorts) > 1:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    fig.update_xaxes(categoryorder="total descending")
    return fig, source


@app.callback(
    Output("area_4", "figure"),
    Output("area_4_sources", "children"),
    [
        Input("store", "data"),
        Input("area_4_options", "value"),
    ],
    [
        State("indicators", "data"),
    ],
)
def area_4_figure(selections, indicator, indicators_dict):

    # only run if indicator not empty
    if not indicator or not "AREA_4" in indicators_dict[selections["theme"]]:
        return {}, {}

    default = indicators_dict[selections["theme"]]["AREA_4"]["default_graph"]
    fig_type = default
    config = indicators_dict[selections["theme"]]["AREA_4"]["graphs"][fig_type]
    compare = config.get("compare")
    options = config.get("options")
    traces = config.get("trace_options")

    query = "CODE == @indicator"
    if compare:
        query = "{} & {} != 'Total'".format(query, compare)

    name = data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
    source = data[data["CODE"] == indicator]["DATA_SOURCE"].unique()[0]
    df = (
        get_filtered_dataset(**selections)
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

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
    if compare:
        options["color"] = compare

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)
    fig.update_xaxes(categoryorder="total descending")

    return fig, source


# Commented code below by James

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
