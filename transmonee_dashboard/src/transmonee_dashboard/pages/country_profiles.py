import dash
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Br import Br
import dash_table
from dash.dependencies import Input, State, Output
import pandas as pd

from ..app import app
from . import countries_iso3_dict, data, df_topics_subtopics, topics_subtopics


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
                                        "Country Profiles",
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
                                    dcc.Dropdown(
                                        id="countries",
                                        style={"zIndex": "999", "width": 300},
                                        options=[
                                            {
                                                "label": key,
                                                "value": countries_iso3_dict[key],
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
                                        id="sectors",
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
                            ),
                            dbc.Row(
                                [
                                    html.Button(
                                        "Generate Profile",
                                        id="generate",
                                        n_clicks=0,
                                        className="btn btn-primary",
                                    )
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
    )


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
        Output("country_name", "children"),
        Output("table_title", "children"),
    ],
    Input("countries", "value"),
)
def get_selected_country(iso_code):
    key_list = list(countries_iso3_dict.keys())
    val_list = list(countries_iso3_dict.values())
    if iso_code is not None:
        position = val_list.index(iso_code)
        country_name = key_list[position]
        return [country_name, f"{country_name} Fact Sheet"]
    else:
        return ["", ""]


@app.callback(
    Output("sub_topics", "options"),
    [
        Input("sectors", "value"),
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


# @app.callback(
#     Output("tbl_country_profile", "children"),
#     [
#         Input("sectors", "value"),
#         Input("sub_topics", "value"),
#     ],
# )
def generate_profile(topics, sub_topics):
    df_country_data = pd.DataFrame(
        columns=["Country", "Sector", "Sub-Topic", "Indicator", "Year", "Value"]
    )
    df_country_data = df_country_data.append(
        {
            "Country": "Lebanon",
            "Sector": "Poverty",
            "Sub-Topic": "Social Protection System",
            "Indicator": "Proportion of population covered by at least one social protection benefit (%)",
            "Year": "2020",
            "Value": "38",
        },
        ignore_index=True,
    )
    return make_html_table(df_country_data)


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
    Output("tbl_country_profile", "children"),
    Input("generate", "n_clicks"),
    [
        State("countries", "value"),
        State("sectors", "value"),
        State("sub_topics", "value"),
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
