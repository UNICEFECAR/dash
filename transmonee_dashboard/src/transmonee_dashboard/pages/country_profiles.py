import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output
import pandas as pd

from ..app import app
from . import countries_iso3_dict

topics_subtopics = {
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
                                    ),
                                ],
                                className="my-2",
                                justify="center",
                            ),
                            dbc.Row(
                                [
                                    dcc.Dropdown(
                                        id="sectors",
                                        style={"zIndex": "11", "minWidth": 400},
                                        options=get_sectors(),
                                        multi=True,
                                    ),
                                    dcc.Dropdown(
                                        id="sub_topics",
                                        style={
                                            "zIndex": "11",
                                            "minWidth": 400,
                                            "paddingLeft": 4,
                                        },
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
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.H6(
                                ["Country Data"],
                                className="subtitle padded",
                            ),
                            html.Div(
                                [
                                    html.Table(
                                        id="tbl_country_profile",
                                        className="tiny-header",
                                    )
                                ],
                                style={"overflow-x": "auto"},
                            ),
                        ],
                        className=" twelve columns",
                    )
                ],
                className="row ",
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
    position = val_list.index(iso_code)
    return key_list[position]


@app.callback(
    Output("sub_topics", "options"),
    [
        Input("sectors", "value"),
    ],
)
def get_subsectors(selected_sectors):
    all_sub_topics = [
        [
            {
                "label": list(sub_topic.values())[0],
                "value": list(sub_topic.keys())[0],
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


@app.callback(
    Output("tbl_country_profile", "children"),
    [
        Input("sectors", "value"),
        Input("sub_topics", "value"),
    ],
)
def generate_profile(topics, sub_topics):
    print(topics)
    print(sub_topics)
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

    print(df_country_data)
    return make_dash_table(df_country_data)


def make_dash_table(df):
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
