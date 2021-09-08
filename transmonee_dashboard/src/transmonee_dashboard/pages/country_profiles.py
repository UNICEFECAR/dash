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
from . import countries_iso3_dict, data

topics_subtopics = {
    "Education": [
        {"Participation": "Participation"},
        {"Quality": "Learning Quality"},
        {"Governance": "Governance"},
    ],
    "Family Environment and Protection": [
        {"Violence": "Violence against children and women"},
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
        {"Demography": "Demography about children"},
        {"Economy": "Political economy"},
        {"Migration": "Migration and displacement"},
        {"Risks": "Risks, humanitarian situation and impact of climate change"},
        {"Data": "Data and Public spending on Children"},
    ],
    "Participation": [
        {"Registration": "Birth registration and documentation"},
        {"Access": "Access to Justice"},
        {"Information": "Information, internet and right to privacy"},
        {"Leisure": "Leisure and culture"},
    ],
}

subtopics_indicators = {}


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
                                ["Country Data"],
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
    Output("country_name", "children"),
    [
        Input("countries", "value"),
    ],
)
def get_selected_country(iso_code):
    key_list = list(countries_iso3_dict.keys())
    val_list = list(countries_iso3_dict.values())
    if iso_code is not None:
        position = val_list.index(iso_code)
        return key_list[position]
    else:
        return ""


@app.callback(
    Output("sub_topics", "options"),
    [
        Input("sectors", "value"),
    ],
)
def get_subsectors(selected_sectors):
    all_sub_topics = []
    if selected_sectors is not None:
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
    final_sub_topics = []
    if all_sub_topics is not None:
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
        State("sub_topics", "value"),
    ],
)
def generate_country_profile(n_clicks, country, sub_topics):
    ctx = dash.callback_context
    changed_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if changed_id == "generate":
        # filter data by selected country
        df_country_data = data[data["REF_AREA"] == country]
        # filter on the selected sub-topics related indicators by using the data dictionary Indicator sheet
        data_dict_file = "/workspaces/dash/transmonee_dashboard/src/transmonee_dashboard/assets/indicator_dictionary_TM_v8.xlsx"
        # read indicators table from excel data-dictionary
        indicators_df = pd.read_excel(data_dict_file, sheet_name="Indicator")
        # subtopics_groups = indicators_df.groupby("Issue")
        filtered_subtopics_groups = indicators_df[indicators_df.Issue.isin(sub_topics)]
        df_country_data = df_country_data[
            df_country_data.CODE.isin(filtered_subtopics_groups["Code"])
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

        df_country_data = pd.merge(df_country_data, indicators_df, on=["Code"])
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
                "Code",
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
            return dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in df_country_data.columns],
                data=df_country_data.to_dict("records"),
                style_cell={"textAlign": "right", "paddingLeft": 2},
                style_data={
                    "whiteSpace": "normal",
                    "height": "auto",
                },
                style_data_conditional=[
                    {"if": {"row_index": "odd"}, "backgroundColor": "#c5effc"}
                ],
                sort_action="native",
                sort_mode="multi",
                column_selectable="single",
                page_action="native",
                page_current=0,
                page_size=10,
                export_format="csv",
            )
