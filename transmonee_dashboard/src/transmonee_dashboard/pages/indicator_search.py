from enum import unique
import dash
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Br import Br
import dash_table
from dash.dependencies import Input, State, Output
import pandas as pd
from pandas.io.formats import style
import re

from ..app import app
from . import (
    countries_iso3_dict,
    data,
    df_topics_subtopics,
    topics_subtopics,
    data_sources,
    df_sources,
)


def get_layout(**kwargs):
    return html.Div(
        children=[
            html.Div(
                className="heading",
                style={"padding": 36},
                children=[
                    html.Div(
                        className="heading-content",
                        children=[
                            html.Div(
                                className="heading-panel",
                                style={"padding": 20},
                                children=[
                                    html.H1(
                                        "Indicators Search",
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                    html.P(
                                        id="country_name",
                                        className="heading-subtitle",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.RadioItems(
                                        options=[
                                            {
                                                "label": "Search Indicators by Source and Sector",
                                                "value": "SEC",
                                            },
                                            {
                                                "label": "Search Indicators by Keyword",
                                                "value": "IND",
                                            },
                                            {
                                                "label": "Search Data by Indicator",
                                                "value": "DAT",
                                            },
                                        ],
                                        value="SEC",
                                        inline=True,
                                        style={"fontWeight": "bold"},
                                        id="search_type",
                                    ),
                                ],
                                justify="center",
                                style={"paddingTop": 8},
                            ),
                            dbc.Row(
                                [
                                    dbc.InputGroup(
                                        children=[
                                            dbc.InputGroupAddon(
                                                "Indicator", addon_type="prepend"
                                            ),
                                            dbc.Input(
                                                id="txtIndicator",
                                                style={
                                                    "height": "2.5rem",
                                                },
                                                placeholder="Enter search keyword...",
                                            ),
                                        ],
                                        style={
                                            "paddingLeft": 20,
                                            "paddingRight": 20,
                                        },
                                    ),
                                ],
                                className="my-2",
                                justify="center",
                                id="row_search_sources",
                            ),
                            dbc.Row(
                                [
                                    dcc.Dropdown(
                                        id="drpIndicators",
                                        style={
                                            "zIndex": "11",
                                            "minWidth": 800,
                                            "maxWidth": 1000,
                                        },
                                        placeholder="Select one or multiple indicators...",
                                        options=get_indicators(),
                                        multi=True,
                                    ),
                                ],
                                className="my-2",
                                justify="center",
                                id="row_search_data",
                            ),
                            dbc.Row(
                                [
                                    dcc.Dropdown(
                                        id="sources",
                                        style={
                                            "zIndex": "11",
                                            "minWidth": 400,
                                            "maxWidth": 600,
                                        },
                                        placeholder="Select one or multiple sources",
                                        options=get_sources(),
                                        multi=True,
                                    ),
                                    dcc.Dropdown(
                                        id="sectors",
                                        style={
                                            "zIndex": "11",
                                            "minWidth": 400,
                                            "maxWidth": 600,
                                            "paddingLeft": 4,
                                        },
                                        placeholder="Select one or multiple sectors",
                                        options=get_sectors(),
                                        multi=True,
                                    ),
                                    dcc.Dropdown(
                                        id="sub_topics",
                                        style={
                                            "zIndex": "11",
                                            "minWidth": 400,
                                            "maxWidth": 600,
                                            "paddingLeft": 4,
                                        },
                                        placeholder="Select one or multiple sub-topics",
                                        multi=True,
                                    ),
                                ],
                                className="my-2 mx-4",
                                justify="center",
                                id="row_search_indicators",
                            ),
                            dbc.Row(
                                [
                                    dbc.Button(
                                        html.Span(
                                            [
                                                "Search",
                                                html.I(className="fas fa-search ml-2"),
                                            ],
                                        ),
                                        color="primary",
                                        id="search",
                                    ),
                                    dbc.Button(
                                        html.Span(
                                            [
                                                "Clear",
                                                html.I(className="fas fa-eraser ml-2"),
                                            ],
                                        ),
                                        color="warning",
                                        id="clear",
                                        style={"marginLeft": 12},
                                    ),
                                ],
                                className="my-4",
                                justify="center",
                            ),
                        ],
                    ),
                ],
                className="bg-light",
            ),
            html.Div(
                [
                    dbc.Row(
                        [
                            html.Div(
                                id="tbl_indicators",
                                style={"width": "100%", "paddingTop": 20},
                            ),
                        ],
                    ),
                ],
                id="indicators_result",
            ),
        ],
    )


def get_sources():
    return [
        {
            "label": data_sources[key],
            "value": key,
        }
        for key in data_sources
    ]


def get_sectors():
    return [
        {
            "label": key,
            "value": key,
        }
        for key in topics_subtopics
    ]


def get_indicators():
    return [
        {
            "label": source["Indicator"],
            "value": source["Code"],
        }
        for index, source in df_sources.iterrows()
    ]


@app.callback(
    [
        Output("sectors", "value"),
        Output("sources", "value"),
        Output("sub_topics", "value"),
        Output("txtIndicator", "value"),
        Output("drpIndicators", "value"),
    ],
    Input("clear", "n_clicks"),
)
def reset_search_controls(type):
    return ["", "", "", "", ""]


@app.callback(
    [
        Output("row_search_sources", "hidden"),
        Output("row_search_indicators", "hidden"),
        Output("row_search_data", "hidden"),
    ],
    Input("search_type", "value"),
)
def show_hide_search_type(type):
    if type == "IND":
        return [False, True, True]
    elif type == "DAT":
        return [True, True, False]
    else:
        return [True, False, True]


@app.callback(
    Output("tbl_indicators", "children"),
    Input("search", "n_clicks"),
    [
        State("txtIndicator", "value"),
        State("sources", "value"),
        State("sectors", "value"),
        State("sub_topics", "value"),
        State("drpIndicators", "value"),
        State("search_type", "value"),
    ],
)
def search_indicators(
    n_clicks, keywords, sources, topics, sub_topics, indicators, type
):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "search":
        df_indicators_data = pd.DataFrame()
        if type == "IND":
            df_indicators_data = df_sources[
                (df_sources["Indicator"].str.contains(keywords, case=False, regex=True))
                | (
                    df_sources["Indicator"]
                    .str.replace("-", " ")
                    .str.contains(keywords, case=False, regex=True)
                )
            ]
            df_indicators_data = df_indicators_data[
                [
                    "Sector",
                    "Subtopic",
                    "Indicator",
                ]
            ]
        elif type == "DAT":
            # Filter the data to keep only selected indicators
            df_indicators_data = data[data["CODE"].isin(indicators)]
            # Filter the data to keep only Totals where more than diaggregation code is available
            df_indicators_data = df_indicators_data[
                (
                    (df_indicators_data["SEX"] == "_T")
                    | (len(df_indicators_data["SEX"].unique()) == 1)
                )
                & (
                    (df_indicators_data["AGE"] == "_T")
                    | (len(df_indicators_data["AGE"].unique()) == 1)
                )
                & (
                    (df_indicators_data["RESIDENCE"] == "_T")
                    | (len(df_indicators_data["RESIDENCE"].unique()) == 1)
                )
                & (
                    (df_indicators_data["WEALTH_QUINTILE"] == "_T")
                    | (len(df_indicators_data["WEALTH_QUINTILE"].unique()) == 1)
                )
            ]

            df_indicators_data = pd.merge(
                df_indicators_data,
                df_topics_subtopics,
                left_on=["CODE"],
                right_on=["Code"],
            )
            df_indicators_data.rename(
                columns={
                    "TIME_PERIOD": "Year",
                    "Theme": "Sector",
                    "Issue": "Subtopic",
                    "OBS_VALUE": "Value",
                    "Geographic area": "Country",
                },
                inplace=True,
            )
            df_indicators_data = df_indicators_data[
                [
                    "Sector",
                    "Subtopic",
                    "Indicator",
                    "Country",
                    "Year",
                    "Value",
                ]
            ]
        else:
            # filter data by selected sector/source
            if sources != ["All"]:
                filtered_subtopics_groups = df_sources[df_sources.Source.isin(sources)]
            elif sub_topics != ["All"]:
                filtered_subtopics_groups = df_sources[
                    df_sources.Issue.isin(sub_topics)
                ]
            else:
                filtered_subtopics_groups = df_sources
            df_indicators_data = df_sources[
                df_sources.Code.isin(filtered_subtopics_groups["Code"])
            ]
            df_indicators_data = df_indicators_data[
                [
                    "Sector",
                    "Subtopic",
                    "Indicator",
                ]
            ]

        # check if no data is available for the current user's selection
        if len(df_indicators_data) == 0:
            return html.Div(
                ["No data available..."],
                className="alert alert-danger fade show w-100",
            )
        else:
            # round the value to 2 decimal places
            return dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_indicators_data.columns],
                data=df_indicators_data.to_dict("records"),
                style_cell={
                    "textAlign": "center",
                    "paddingLeft": 2,
                    "fontWeight": "bold",
                },
                style_data={
                    "whiteSpace": "normal",
                    "height": "auto",
                    "textAlign": "left",
                    "fontWeight": "regular",
                },
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#c5effc"},
                ],
                sort_action="native",
                filter_action="native",
                sort_mode="multi",
                column_selectable="single",
                page_action="native",
                page_current=0,
                page_size=20,
                export_format="csv",
                export_columns="all",
                css=[{"selector": ".show-hide", "rule": "display: none"}],
            )
