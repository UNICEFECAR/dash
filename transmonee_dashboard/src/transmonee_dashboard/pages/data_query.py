from enum import unique
import dash
from dash_bootstrap_components._components.Row import Row
from dash_bootstrap_components._components.Tooltip import Tooltip
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Br import Br
import dash_table
from dash.dependencies import ALL, MATCH, Input, State, Output
from numpy import isin
import pandas as pd
from pandas.io.formats import style
import re

from transmonee_dashboard.pages.base_page import indicator_card

from ..app import app
from . import (
    countries_iso3_dict,
    data,
    years,
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
                                        "Query Data",
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
                            label="Search Indicators",
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
                                                                # {
                                                                #     "label": "Search Data by Indicator",
                                                                #     "value": "DAT",
                                                                # },
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
                            label="Search Data by Country and Indicator",
                            children=[
                                html.Br(),
                                html.Div(
                                    [
                                        dbc.Col(
                                            [
                                                dbc.Row(
                                                    [
                                                        html.P(
                                                            "Select one or more Country:",
                                                            className="fix_label",
                                                            style={
                                                                "color": "rgba(0, 0, 0, 0.65)",
                                                                "margin-top": "13px",
                                                                "fontWeight": "bold",
                                                            },
                                                        ),
                                                        dcc.Dropdown(
                                                            id="countries",
                                                            style={
                                                                "zIndex": "999",
                                                                "minWidth": 400,
                                                                "maxWidth": 600,
                                                            },
                                                            options=get_search_countries(),
                                                            multi=True,
                                                            placeholder="Select one or more country...",
                                                            className="m-2",
                                                        ),
                                                        dbc.DropdownMenu(
                                                            label=f"Years: {years[0]} - {years[-1]}",
                                                            id="collapse-years-search",
                                                            className="m-2",
                                                            color="info",
                                                            children=[
                                                                dbc.Card(
                                                                    dcc.RangeSlider(
                                                                        id="year_slider_search",
                                                                        min=0,
                                                                        max=len(years)
                                                                        - 1,
                                                                        step=None,
                                                                        marks={
                                                                            index: str(
                                                                                year
                                                                            )
                                                                            for index, year in enumerate(
                                                                                years
                                                                            )
                                                                        },
                                                                        value=[
                                                                            0,
                                                                            len(years)
                                                                            - 1,
                                                                        ],
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
                                                        dcc.Dropdown(
                                                            id="drpIndicators",
                                                            style={
                                                                "minWidth": 800,
                                                                "maxWidth": 1000,
                                                            },
                                                            placeholder="Select one or multiple indicators...",
                                                            multi=True,
                                                        ),
                                                    ],
                                                    className="my-2",
                                                    justify="center",
                                                    style={"borderWidth": 2},
                                                ),
                                                dbc.Row(
                                                    [
                                                        html.P(
                                                            "Select disaggregation dimensions:",
                                                            className="fix_label",
                                                            style={
                                                                "color": "rgba(0, 0, 0, 0.65)",
                                                                "margin-top": "6px",
                                                                "margin-right": "6px",
                                                                "fontWeight": "bold",
                                                            },
                                                        ),
                                                        dbc.Checklist(
                                                            options=[
                                                                {
                                                                    "label": "Sex",
                                                                    "value": 0,
                                                                },
                                                                {
                                                                    "label": "Age",
                                                                    "value": 1,
                                                                },
                                                                {
                                                                    "label": "Residence",
                                                                    "value": 2,
                                                                },
                                                                {
                                                                    "label": "Wealth Quintile",
                                                                    "value": 3,
                                                                },
                                                            ],
                                                            id="disaggregation_toggle",
                                                            switch=True,
                                                            inline=True,
                                                            style={
                                                                "paddingRight": 20,
                                                                "paddingTop": 6,
                                                            },
                                                        ),
                                                        dbc.Tooltip(
                                                            "This toggle is used to select the dimensions that you want to show the detailed related disaggregation where applicable",
                                                            target="disaggregation_toggle",
                                                            placement="bottom",
                                                        ),
                                                    ],
                                                    className="my-2",
                                                    justify="center",
                                                    style={"borderWidth": 2},
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Checklist(
                                                            options=[
                                                                {
                                                                    "label": "Show latest data points",
                                                                    "value": 1,
                                                                }
                                                            ],
                                                            id="latest_data_toggle",
                                                            switch=True,
                                                            style={
                                                                "paddingRight": 20,
                                                            },
                                                        ),
                                                        dbc.Tooltip(
                                                            "This toggle is used to show only the latest data points of the selected country",
                                                            target="latest_data_toggle",
                                                            placement="bottom",
                                                        ),
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
                                                            id="search-data",
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
                                                            id="clear-data",
                                                            style={"marginLeft": 12},
                                                        ),
                                                    ],
                                                    className="my-2",
                                                    justify="center",
                                                    style={"verticalAlign": "center"},
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
                                                html.Div(
                                                    id="tbl_country_profile",
                                                    style={
                                                        "width": "100%",
                                                        "paddingTop": 10,
                                                    },
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


def get_search_countries():
    all_countries = {"label": "All", "value": "All"}
    countries_list = [
        {
            "label": key,
            "value": countries_iso3_dict[key],
        }
        for key in countries_iso3_dict.keys()
    ]
    countries_list.insert(0, all_countries)
    return countries_list


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
    Output("drpIndicators", "options"),
    [
        Input({"type": "sectors", "index": 2}, "value"),
        Input({"type": "sub_topics", "index": 2}, "value"),
    ],
)
def get_indicators(sectors, sub_sectors):
    if (sectors is not None) & (len(sectors) > 0) & (sectors != ["All"]):
        df_indicators = df_sources[df_sources["Sector"].isin(sectors)]
    else:
        df_indicators = df_sources
    if (sub_sectors is not None) & (len(sub_sectors) > 0) & (sub_sectors != ["All"]):
        df_indicators = df_indicators[df_indicators["Subtopic"].isin(sub_sectors)]
    return [
        {
            "label": indicator["Indicator"],
            "value": indicator["Code"],
        }
        for index, indicator in df_indicators.iterrows()
    ]


@app.callback(
    [
        Output("sources", "value"),
        Output("countries", "value"),
        Output({"type": "sectors", "index": 1}, "value"),
        Output({"type": "sub_topics", "index": 1}, "value"),
        Output({"type": "sectors", "index": 2}, "value"),
        Output({"type": "sub_topics", "index": 2}, "value"),
        Output("txtIndicator", "value"),
        Output("drpIndicators", "value"),
        Output("disaggregation_toggle", "value"),
    ],
    [
        Input("clear", "n_clicks"),
        Input("clear-data", "n_clicks"),
    ],
)
def reset_search_controls(clear_click, clear_data_click):
    return ["", "", "", "", "", "", "", "", []]


@app.callback(
    [
        Output("row_search_sources", "hidden"),
        Output("row_search_indicators", "hidden"),
    ],
    Input("search_type", "value"),
)
def show_hide_search_type(type):
    if type == "IND":
        return [False, True]
    else:
        return [True, False]


@app.callback(
    Output("tbl_indicators", "children"),
    Input("search", "n_clicks"),
    [
        State("sources", "value"),
        State({"type": "sectors", "index": 1}, "value"),
        State({"type": "sub_topics", "index": 1}, "value"),
        State("txtIndicator", "value"),
        State("search_type", "value"),
    ],
)
def search_indicators(n_clicks, sources, topics, sub_topics, keywords, type):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "search":
        df_indicators_data = []
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
                    "Source_Full",
                    "Sector",
                    "Subtopic",
                    "Indicator",
                ]
            ].rename(columns={"Source_Full": "Source"})
        # elif type == "DAT":
        #     # Filter the data to keep only selected indicators
        #     df_filtered_indicators_data = data[data["CODE"].isin(indicators)]
        #     if len(df_filtered_indicators_data) > 0:
        #         # group by indicator code and count the distinct count of disaggregation for the 4 dimensions
        #         df_dimensions_count = df_filtered_indicators_data.groupby("CODE").apply(
        #             lambda ind: pd.Series(
        #                 {
        #                     "Sex_Count": ind["SEX"].nunique(),
        #                     "Age_Count": ind["AGE"].nunique(),
        #                     "Residence_Count": ind["RESIDENCE"].nunique(),
        #                     "Wealth_Count": ind["WEALTH_QUINTILE"].nunique(),
        #                 }
        #             )
        #         )
        #         df_indicators_data = pd.merge(
        #             df_filtered_indicators_data, df_dimensions_count, on=["CODE"]
        #         )
        #         # Filter the data to keep the total or the other dimension when there is only one disaggregation
        #         df_indicators_data = df_indicators_data[
        #             (
        #                 (df_indicators_data["SEX"] == "_T")
        #                 | (df_indicators_data["Sex_Count"] == 1)
        #             )
        #             & (
        #                 (df_indicators_data["AGE"] == "_T")
        #                 | (df_indicators_data["Age_Count"] == 1)
        #             )
        #             & (
        #                 (df_indicators_data["RESIDENCE"] == "_T")
        #                 | (df_indicators_data["Residence_Count"] == 1)
        #             )
        #             & (
        #                 (df_indicators_data["WEALTH_QUINTILE"] == "_T")
        #                 | (df_indicators_data["Wealth_Count"] == 1)
        #             )
        #         ]
        #         # merge to get the sector and sub-topic
        #         df_indicators_data = pd.merge(
        #             df_indicators_data,
        #             df_topics_subtopics,
        #             left_on=["CODE"],
        #             right_on=["Code"],
        #         )
        #         df_indicators_data.rename(
        #             columns={
        #                 "TIME_PERIOD": "Year",
        #                 "Theme": "Sector",
        #                 "Issue": "Subtopic",
        #                 "OBS_VALUE": "Value",
        #                 "Geographic area": "Country",
        #             },
        #             inplace=True,
        #         )
        #         # keep only selected columns
        #         df_indicators_data = df_indicators_data[
        #             [
        #                 "Sector",
        #                 "Subtopic",
        #                 "Indicator",
        #                 "Country",
        #                 "Year",
        #                 "Value",
        #             ]
        #         ]
        else:
            # filter data by selected sector/source
            filtered_subtopics_groups = df_sources
            if (sources is not None) & (len(sources) > 0) & (sources != ["All"]):
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Source.isin(sources)
                ]
            if (topics is not None) & (len(topics) > 0) & (topics != ["All"]):
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Sector.isin(topics)
                ]
            if (
                (sub_topics is not None)
                & (len(sub_topics) > 0)
                & (sub_topics != ["All"])
            ):
                filtered_subtopics_groups = filtered_subtopics_groups[
                    filtered_subtopics_groups.Subtopic.isin(sub_topics)
                ]
            df_indicators_data = filtered_subtopics_groups[
                filtered_subtopics_groups.Code.isin(filtered_subtopics_groups["Code"])
            ]
            df_indicators_data = df_indicators_data[
                [
                    "Source_Full",
                    "Sector",
                    "Subtopic",
                    "Indicator",
                ]
            ].rename(columns={"Source_Full": "Source"})

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


# @app.callback(
#     Output("table_title", "children"),
#     Input("countries", "value"),
# )
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
    Output("collapse-years-search", "label"),
    Input("year_slider_search", "value"),
)
def get_selected_years(years_slider):
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0] : years_slider[1] + 1]
    return f"Years: {selected_years[0]} - {selected_years[-1]}"


@app.callback(
    Output("tbl_country_profile", "children"),
    Input("search-data", "n_clicks"),
    [
        State("countries", "value"),
        State("year_slider_search", "value"),
        State("latest_data_toggle", "value"),
        State({"type": "sectors", "index": 2}, "value"),
        State({"type": "sub_topics", "index": 2}, "value"),
        State("drpIndicators", "value"),
        State("disaggregation_toggle", "value"),
    ],
)
def generate_country_profile(
    n_clicks,
    countries,
    years_slider,
    latest_data,
    sectors,
    sub_topics,
    indicators,
    dis_toggles,
):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "search-data":
        # filter data by selected countries
        if (countries is not None) & (len(countries) > 0) & (countries != ["All"]):
            df_country_data = data[data["REF_AREA"].isin(countries)]
        else:
            df_country_data = data
        # need to include the last selected year as it was exluded in the previous method
        selected_years = years[years_slider[0] : years_slider[1] + 1]
        # filter data based on the selected years
        df_country_data = df_country_data[
            df_country_data["TIME_PERIOD"].isin(selected_years)
        ]
        # Inner join in order to filter country data to keep only selected sectors and sub-topics
        df_country_data = pd.merge(
            df_country_data,
            df_sources,
            how="inner",
            left_on=["CODE"],
            right_on=["Code"],
        )
        # keep only needed columns in the dataframe
        df_country_data = df_country_data[
            [
                "Geographic area",
                "TIME_PERIOD",
                "OBS_VALUE",
                "Indicator_x",
                "CODE",
                "Sex",
                "SEX",
                "AGE",
                "Age",
                "RESIDENCE",
                "Residence",
                "WEALTH_QUINTILE",
                "Wealth Quintile",
                "Sector",
                "Subtopic",
            ]
        ]
        df_country_data.rename(
            columns={
                "Geographic area": "Country",
                "TIME_PERIOD": "Year",
                "OBS_VALUE": "Value",
                "Indicator_x": "Indicator",
                "CODE": "Code",
            },
            inplace=True,
        )
        # filter selected sectors
        if (sectors is not None) & (len(sectors) > 0) & (sectors != ["All"]):
            df_country_data = df_country_data[df_country_data.Sector.isin(sectors)]
        # filter selected sub-sectors
        if (sub_topics is not None) & (len(sub_topics) > 0) & (sub_topics != ["All"]):
            df_country_data = df_country_data[df_country_data.Subtopic.isin(sub_topics)]
        # filter selected indicators
        if (indicators is not None) & (len(indicators) > 0) & (indicators != ["All"]):
            df_country_data = df_country_data[df_country_data.Code.isin(indicators)]

        # check if data is available for the current user's selection
        if len(df_country_data) > 0:
            # group by indicator code and count the distinct count of disaggregation for the 4 dimensions
            df_dimensions_count = df_country_data.groupby("Code").apply(
                lambda ind: pd.Series(
                    {
                        "Sex_Count": ind["SEX"].nunique(),
                        "Age_Count": ind["AGE"].nunique(),
                        "Residence_Count": ind["RESIDENCE"].nunique(),
                        "Wealth_Count": ind["WEALTH_QUINTILE"].nunique(),
                    }
                )
            )
            df_country_data = pd.merge(
                df_country_data, df_dimensions_count, on=["Code"]
            )

            # define the hidden columns based on the selected disaggregations
            all_disag_columns = ["Sex", "Age", "Residence", "Wealth Quintile"]
            selected_disag_columns = [all_disag_columns[i] for i in dis_toggles]
            hidden_columns = list(
                set(all_disag_columns).symmetric_difference(set(selected_disag_columns))
            )

            # Filter the data to keep the total or the other dimension when there is only one disaggregation
            df_country_data = df_country_data[
                (
                    (
                        (df_country_data["SEX"] == "_T")
                        & ("Sex" not in selected_disag_columns)
                    )
                    | (df_country_data["Sex_Count"] == 1)
                    | ("Sex" in selected_disag_columns)
                )
                & (
                    (
                        (df_country_data["AGE"] == "_T")
                        & ("Age" not in selected_disag_columns)
                    )
                    | (df_country_data["Age_Count"] == 1)
                    | ("Age" in selected_disag_columns)
                )
                & (
                    (
                        (df_country_data["RESIDENCE"] == "_T")
                        & ("Residence" not in selected_disag_columns)
                    )
                    | (df_country_data["Residence_Count"] == 1)
                    | ("Residence" in selected_disag_columns)
                )
                & (
                    (
                        (df_country_data["WEALTH_QUINTILE"] == "_T")
                        & ("Wealth Quintile" not in selected_disag_columns)
                    )
                    | (df_country_data["Wealth_Count"] == 1)
                    | ("Wealth Quintile" in selected_disag_columns)
                )
            ]

            df_country_data = df_country_data[
                [
                    "Country",
                    "Sector",
                    "Subtopic",
                    "Indicator",
                    "Sex",
                    "Age",
                    "Residence",
                    "Wealth Quintile",
                    "Year",
                    "Value",
                ]
            ]

            # check if the toggle of the latest data is checked to filter only latest data points
            if latest_data:
                # keep only the latest value of every country
                df_country_data = df_country_data.sort_values(
                    ["Country", "Indicator", "Year"]
                ).drop_duplicates(
                    [
                        "Country",
                        "Indicator",
                        "Sex",
                        "Age",
                        "Residence",
                        "Wealth Quintile",
                    ],
                    keep="last",
                )

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
                hidden_columns=hidden_columns,
                css=[{"selector": ".show-hide", "rule": "display: none"}],
            )
        else:
            # check if no data is available for the current user's selection
            return html.Div(
                ["No data available..."],
                className="alert alert-danger fade show w-100",
            )
