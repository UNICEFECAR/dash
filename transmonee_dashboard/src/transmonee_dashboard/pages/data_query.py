from enum import unique
import dash
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Br import Br
import dash_table
from dash.dependencies import ALL, MATCH, Input, State, Output
import pandas as pd
from pandas.io.formats import style
import re

from transmonee_dashboard.pages.base_page import indicator_card

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
                                        "Data Query",
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                    html.P(
                                        "Search Indicators and Country Data",
                                        id="sub_title",
                                        className="heading-subtitle",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                dcc.Tabs(
                    id="search-tabs",
                    children=[
                        dcc.Tab(
                            label="Search Indicators and Indicators' Data",
                            children=[
                                html.Br(),
                                html.Div(
                                    [
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
                                                            style={
                                                                "fontWeight": "bold"
                                                            },
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
                                                                    "Indicator",
                                                                    addon_type="prepend",
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
                                                                "maxWidth": 500,
                                                            },
                                                            placeholder="Select one or multiple sources",
                                                            options=get_sources(),
                                                            multi=True,
                                                        ),
                                                        dcc.Dropdown(
                                                            id={
                                                                "type": "sectors",
                                                                "index": 1,
                                                            },
                                                            style={
                                                                "zIndex": "11",
                                                                "minWidth": 400,
                                                                "maxWidth": 500,
                                                                "paddingLeft": 4,
                                                            },
                                                            placeholder="Select one or multiple sectors",
                                                            options=get_sectors(),
                                                            multi=True,
                                                        ),
                                                        dcc.Dropdown(
                                                            id={
                                                                "type": "sub_topics",
                                                                "index": 1,
                                                            },
                                                            style={
                                                                "zIndex": "11",
                                                                "minWidth": 400,
                                                                "maxWidth": 500,
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
                                                                    html.I(
                                                                        className="fas fa-search ml-2"
                                                                    ),
                                                                ],
                                                            ),
                                                            color="primary",
                                                            id="search",
                                                        ),
                                                        dbc.Button(
                                                            html.Span(
                                                                [
                                                                    "Clear",
                                                                    html.I(
                                                                        className="fas fa-eraser ml-2"
                                                                    ),
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
                                    style={
                                        "border-radius": "6px",
                                        "padding": 4,
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Div(
                                            id="tbl_indicators",
                                            style={
                                                "width": "100%",
                                                "paddingTop": 20,
                                            },
                                        ),
                                    ],
                                    id="indicators_result",
                                ),
                            ],
                            style={"fontWeight": "bold", "padding": 20},
                            selected_style={
                                "borderTop": "1px solid #d6d6d6",
                                "borderBottom": "1px solid #d6d6d6",
                                "backgroundColor": "#1cabe2",
                                "color": "white",
                                "fontWeight": "bold",
                                "padding": 20,
                            },
                            id="indicator-search",
                        ),
                        dcc.Tab(
                            label="Search Country Data",
                            children=[
                                html.Br(),
                                html.Div(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.P(
                                                            "Select Country:",
                                                            className="fix_label",
                                                            style={
                                                                "color": "black",
                                                                "margin-top": "6px",
                                                                "margin-right": "6px",
                                                                "fontWeight": "bold",
                                                            },
                                                        ),
                                                        dcc.Dropdown(
                                                            id="countries",
                                                            style={
                                                                "zIndex": "999",
                                                                "width": 300,
                                                            },
                                                            options=[
                                                                {
                                                                    "label": key,
                                                                    "value": countries_iso3_dict[
                                                                        key
                                                                    ],
                                                                }
                                                                for key in countries_iso3_dict.keys()
                                                            ],
                                                            placeholder="Select a country...",
                                                        ),
                                                    ],
                                                    className="my-2",
                                                    justify="center",
                                                ),
                                                dbc.Row(
                                                    [
                                                        dcc.Dropdown(
                                                            id={
                                                                "type": "sectors",
                                                                "index": 2,
                                                            },
                                                            style={
                                                                "zIndex": "11",
                                                                "minWidth": 400,
                                                                "maxWidth": 600,
                                                            },
                                                            placeholder="Select one or multiple sectors",
                                                            options=get_sectors(),
                                                            multi=True,
                                                        ),
                                                        dcc.Dropdown(
                                                            id={
                                                                "type": "sub_topics",
                                                                "index": 2,
                                                            },
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
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.Button(
                                                            "Generate Country Fact Sheet",
                                                            id="generate",
                                                            n_clicks=0,
                                                            className="btn btn-primary",
                                                        )
                                                    ],
                                                    className="my-2",
                                                    justify="center",
                                                ),
                                            ],
                                        ),
                                    ],
                                    className="bg-light",
                                    style={
                                        "border-radius": "6px",
                                        "padding": 6,
                                    },
                                ),
                                html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                html.H6(
                                                    id="table_title",
                                                    style={
                                                        "borderLeft": "5px solid #1cabe2",
                                                        "background": "#fff",
                                                        "padding": 10,
                                                        "marginTop": 10,
                                                        "marginBottom": 15,
                                                        "height": 40,
                                                    },
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            [
                                                html.Div(
                                                    id="tbl_country_profile",
                                                    style={"width": "100%"},
                                                ),
                                            ],
                                        ),
                                    ],
                                    id="country_profile",
                                ),
                            ],
                            style={"fontWeight": "bold"},
                            selected_style={
                                "borderTop": "1px solid #d6d6d6",
                                "borderBottom": "1px solid #d6d6d6",
                                "backgroundColor": "#1cabe2",
                                "color": "white",
                                "fontWeight": "bold",
                                "padding": 20,
                            },
                            id="country-search",
                        ),
                    ],
                ),
                style={"width": "100%"},
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
        Output("sources", "value"),
        Output({"type": "sectors", "index": 1}, "value"),
        Output({"type": "sub_topics", "index": 1}, "value"),
        Output({"type": "sectors", "index": 2}, "value"),
        Output({"type": "sub_topics", "index": 2}, "value"),
        Output("txtIndicator", "value"),
        Output("drpIndicators", "value"),
    ],
    Input("clear", "n_clicks"),
)
def reset_search_controls(n_clicks):
    return ["", "", "", "", "", "", ""]


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
        State("sources", "value"),
        State({"type": "sectors", "index": 1}, "value"),
        State({"type": "sub_topics", "index": 1}, "value"),
        State("drpIndicators", "value"),
        State("txtIndicator", "value"),
        State("search_type", "value"),
    ],
)
def search_indicators(
    n_clicks, sources, topics, sub_topics, indicators, keywords, type
):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "search":
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
            df_filtered_indicators_data = data[data["CODE"].isin(indicators)]
            if len(df_filtered_indicators_data) > 0:
                # group by indicator code and count the distinct count of disaggregation for the 4 dimensions
                df_dimensions_count = df_filtered_indicators_data.groupby("CODE").apply(
                    lambda ind: pd.Series(
                        {
                            "Sex_Count": ind["SEX"].nunique(),
                            "Age_Count": ind["AGE"].nunique(),
                            "Residence_Count": ind["RESIDENCE"].nunique(),
                            "Wealth_Count": ind["WEALTH_QUINTILE"].nunique(),
                        }
                    )
                )
                df_indicators_data = pd.merge(
                    df_filtered_indicators_data, df_dimensions_count, on=["CODE"]
                )
                # Filter the data to keep the total or the other dimension when there is only one disaggregation
                df_indicators_data = df_indicators_data[
                    (
                        (df_indicators_data["SEX"] == "_T")
                        | (df_indicators_data["Sex_Count"] == 1)
                    )
                    & (
                        (df_indicators_data["AGE"] == "_T")
                        | (df_indicators_data["Age_Count"] == 1)
                    )
                    & (
                        (df_indicators_data["RESIDENCE"] == "_T")
                        | (df_indicators_data["Residence_Count"] == 1)
                    )
                    & (
                        (df_indicators_data["WEALTH_QUINTILE"] == "_T")
                        | (df_indicators_data["Wealth_Count"] == 1)
                    )
                ]
                # merge to get the sector and sub-topic
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
                # keep only selected columns
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
            filtered_subtopics_groups = df_sources
            if sources != ["All"]:
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Source.isin(sources)
                ]
            if topics != ["All"]:
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Sector.isin(topics)
                ]
            if sub_topics != ["All"]:
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Subtopic.isin(sub_topics)
                ]
            df_indicators_data = filtered_subtopics_groups[
                filtered_subtopics_groups.Code.isin(filtered_subtopics_groups["Code"])
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


@app.callback(
    Output("table_title", "children"),
    Input("countries", "value"),
)
def get_selected_country(iso_code):
    key_list = list(countries_iso3_dict.keys())
    val_list = list(countries_iso3_dict.values())
    if iso_code is not None:
        position = val_list.index(iso_code)
        country_name = key_list[position]
        return f"{country_name} Fact Sheet"
    else:
        return ""


@app.callback(
    Output({"type": "sub_topics", "index": MATCH}, "options"),
    [
        Input({"type": "sectors", "index": MATCH}, "value"),
    ],
)
def get_subsectors(selected_sectors):
    topics_subtopics_keys = list(topics_subtopics.keys())
    del topics_subtopics_keys[0]
    all_sub_topics = []
    if (selected_sectors is not None) and (selected_sectors != ["All"]):
        all_sub_topics = [
            [
                {
                    "label": list(sub_topic.values())[0],
                    "value": list(sub_topic.values())[0],
                }
                for sub_topic in topics_subtopics[sector]
            ]
            for sector in selected_sectors
        ]
    elif selected_sectors == ["All"]:
        all_sub_topics = [
            [
                {
                    "label": list(sub_topic.values())[0],
                    "value": list(sub_topic.values())[0],
                }
                for sub_topic in topics_subtopics[sector]
            ]
            for sector in topics_subtopics_keys
        ]
    final_sub_topics = []
    if all_sub_topics is not None:
        final_sub_topics = [
            {
                "label": "All",
                "value": "All",
            }
        ]
        for sub_topics in all_sub_topics:
            final_sub_topics += sub_topics
    return final_sub_topics


@app.callback(
    Output("tbl_country_profile", "children"),
    Input("generate", "n_clicks"),
    [
        State("countries", "value"),
        State({"type": "sectors", "index": 2}, "value"),
        State({"type": "sub_topics", "index": 2}, "value"),
    ],
)
def generate_country_profile(n_clicks, country, sectors, sub_topics):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "generate":
        # filter data by selected country
        df_country_data = data[data["REF_AREA"] == country]
        if sub_topics != ["All"]:
            filtered_subtopics_groups = df_topics_subtopics[
                df_topics_subtopics.Issue.isin(sub_topics)
            ]
        else:
            filtered_subtopics_groups = df_topics_subtopics

        # Filter country data to keep only selected sectors and sub-topics
        df_country_data = df_country_data[
            df_country_data.CODE.isin(filtered_subtopics_groups["Code"])
        ]

        # group by indicator code and count the distinct count of disaggregation for the 4 dimensions
        df_dimensions_count = df_country_data.groupby("CODE").apply(
            lambda ind: pd.Series(
                {
                    "Sex_Count": ind["SEX"].nunique(),
                    "Age_Count": ind["AGE"].nunique(),
                    "Residence_Count": ind["RESIDENCE"].nunique(),
                    "Wealth_Count": ind["WEALTH_QUINTILE"].nunique(),
                }
            )
        )
        df_country_data = pd.merge(df_country_data, df_dimensions_count, on=["CODE"])
        # Filter the data to keep the total or the other dimension when there is only one disaggregation
        df_country_data = df_country_data[
            ((df_country_data["SEX"] == "_T") | (df_country_data["Sex_Count"] == 1))
            & ((df_country_data["AGE"] == "_T") | (df_country_data["Age_Count"] == 1))
            & (
                (df_country_data["RESIDENCE"] == "_T")
                | (df_country_data["Residence_Count"] == 1)
            )
            & (
                (df_country_data["WEALTH_QUINTILE"] == "_T")
                | (df_country_data["Wealth_Count"] == 1)
            )
        ]

        df_country_data.rename(
            columns={
                "Geographic area": "Country",
                "TIME_PERIOD": "Year",
                "OBS_VALUE": "Value",
                "CODE": "Code",
            },
            inplace=True,
        )

        df_country_data = pd.merge(df_country_data, df_topics_subtopics, on=["Code"])
        df_country_data.rename(
            columns={
                "Theme": "Sector",
                "Issue": "Subtopic",
            },
            inplace=True,
        )
        df_country_data = df_country_data[
            [
                "Country",
                "Sector",
                "Subtopic",
                "Indicator",
                "Year",
                "Value",
            ]
        ]

        # check if no data is available for the current user's selection
        if len(df_country_data) == 0:
            return html.Div(
                ["No data available..."],
                className="alert alert-danger fade show w-100",
            )
        else:
            # round the value to 2 decimal places
            df_country_data = df_country_data.round({"Value": 2})
            return dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_country_data.columns],
                data=df_country_data.to_dict("records"),
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
                    {"if": {"column_id": "Value"}, "fontWeight": "bold"},
                    {
                        "if": {
                            "filter_query": "{{Value}} = {}".format(
                                df_country_data["Value"].max()
                            ),
                            "column_id": "Value",
                        },
                        "backgroundColor": "#FF4136",
                        "color": "white",
                    },
                ],
                sort_action="native",
                sort_mode="multi",
                column_selectable="single",
                page_action="native",
                page_current=0,
                page_size=20,
                export_format="csv",
                export_columns="all",
                hidden_columns=["Country"],
                css=[{"selector": ".show-hide", "rule": "display: none"}],
            )
