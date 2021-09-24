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
from . import countries_iso3_dict, data, df_topics_subtopics, data_sources, df_sources

pd.options.display.float_format = "{:,.2f}".format
topics_subtopics = {
    "All": ["All"],
    "Education": [
        {"Participation": "Participation"},
        {"Quality": "Learning Quality"},
        {"Governance": "Governance"},
    ],
    "Family Environment and Protection": [
        {"Violence": "Violence against Children and Women"},
        {"Care": "Children without parental care"},
        {"Justice": "Juvenile Justice"},
        {"Marriage": "Child marriage and other harmful practices"},
        {"Labour": "Child Labour"},
    ],
    "Health and Nutrition": [
        {"HS": "Health System"},
        {"MNCH": "Maternal, newborn and child health"},
        {"Immunization": "Immunization"},
        {"Nutrition": "Nutrition"},
        {"Adolescent": "Adolescent health"},
        {"HIVAIDS": "HIV and AIDS"},
        {"Wash": "Water, sanitation and hygiene"},
    ],
    "Poverty": [
        {"Poverty": "Poverty and multi-dimensional deprivation"},
        {"Protection": "Social protection system"},
    ],
    "Child Rights Landscape": [
        {"Demography": "Demography about Children"},
        {"Economy": "Political Economy"},
        {"Migration": "Migration and Displacement"},
        {"Risks": "Risks, humanitarian situation and impact of climate change"},
        {"Data": "Data and Public spending on Children"},
    ],
    "Participation": [
        {"Registration": "Birth registration and documentation"},
        {"Access": "Access to Justice"},
        {"Information": "Information, Internet and Right to privacy"},
        {"Leisure": "Leisure and Culture"},
    ],
}


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
                                                "label": "Search Indicator by Source and Sector",
                                                "value": "SEC",
                                            },
                                            {
                                                "label": "Search Indicator by Keyword",
                                                "value": "IND",
                                            },
                                        ],
                                        value="SEC",
                                        inline=True,
                                        id="search_type",
                                    ),
                                ],
                                justify="center",
                                style={"paddingTop": 4},
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
                                    # dcc.Dropdown(
                                    #     id="drpIndicators",
                                    #     style={
                                    #         "zIndex": "11",
                                    #         "minWidth": 400,
                                    #         "maxWidth": 600,
                                    #     },
                                    #     placeholder="Select one or multiple sources",
                                    #     options=get_indicators(),
                                    #     multi=True,
                                    # ),
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
                    # dbc.Row(
                    #     [
                    #         html.H6(
                    #             id="table_title",
                    #             style={
                    #                 "borderLeft": "5px solid #1cabe2",
                    #                 "background": "#fff",
                    #                 "padding": 10,
                    #                 "marginTop": 10,
                    #                 "marginBottom": 15,
                    #                 "height": 40,
                    #             },
                    #         ),
                    #     ],
                    # ),
                    dbc.Row(
                        [
                            html.Div(
                                id="tbl_indicators",
                                style={"width": "100%",
                                "paddingTop": 20},
                            ),
                        ],
                    ),
                ],
                id="country_profile",
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

@app.callback(
    [
        Output("sectors", "value"),
        Output("sources", "value"),
        Output("sub_topics", "value"),
        Output("txtIndicator", "value"),
    ],
    Input("clear", "n_clicks"),
)
def reset_search_controls(type):
    return ["","","",""]

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


# @app.callback(
#     [
#         Output("country_name", "children"),
#         Output("table_title", "children"),
#     ],
#     Input("countries", "value"),
# )
def get_selected_country(iso_code):
    key_list = list(countries_iso3_dict.keys())
    val_list = list(countries_iso3_dict.values())
    if iso_code is not None:
        position = val_list.index(iso_code)
        country_name = key_list[position]
        return [country_name, f"{country_name} Fact Sheet"]
    else:
        return ["", ""]


# @app.callback(
#     Output("sub_topics", "options"),
#     [
#         Input("sectors", "value"),
#     ],
# )
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


def make_html_table(df):
    """Return a dash definition of an HTML table for a Pandas dataframe"""
    table = []
    html_row = []
    # Add the columns
    for i in range(len(df.columns)):
        html_row.append(html.Td([df.columns[i]]))
    table.append(html.Tr(html_row))

    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table


@app.callback(
    Output("tbl_indicators", "children"),
    Input("search", "n_clicks"),
    [
        State("txtIndicator", "value"),
        State("sources", "value"),
        State("sectors", "value"),
        State("sub_topics", "value"),
        State("search_type", "value"),
    ],
)
def search_indicators(n_clicks, indicator, sources, topics, sub_topics, type):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "search":
        df_indicators_data = pd.DataFrame()
        if type == "IND":
            df_indicators_data = df_sources[
                df_sources["Indicator"].str.contains(indicator, case=False, regex=False)
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

        # df_indicators_data = pd.merge(
        #     df_indicators_data, df_topics_subtopics, on=["Code"]
        # )
        df_indicators_data = df_indicators_data[
            [
                # "Country",
                "Sector",
                "Subtopic",
                "Indicator",
                # "Year",
                # "Value",
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
                hidden_columns=["Country"],
                css=[{"selector": ".show-hide", "rule": "display: none"}],
            )
