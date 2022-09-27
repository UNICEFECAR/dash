from dash import Dash, html, dcc, callback_context, ALL, Input, Output, State
import dash_bootstrap_components as dbc
import dash_treeview_antd

import json
import logging
import collections
from io import BytesIO

import numpy as np
import pandas as pd
import requests
from requests.exceptions import HTTPError

import pandasdmx as sdmx

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import textwrap

from components import fa

# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = px.colors.qualitative.Dark24

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
AREA_KEYS = ["MAIN", "AREA_1", "AREA_2", "AREA_3", "AREA_4", "AREA_5", "AREA_6"]
DEFAULT_LABELS = {
    "Country_name": "Country",
    "TIME_PERIOD": "Year",
    "Sex_name": "Sex",
    "Residence_name": "Residence",
    "Age_name": "Age",
    "Wealth_name": "Wealth Quintile",
}
CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}

EMPTY_CHART = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No data is available for the selected filters",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 28},
            }
        ],
    }
}

# TODO: Move all of these to env/setting vars from production
sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv&startPeriod={}&endPeriod={}"

geo_json_file = "./assets/countries.geo.json"
with open(geo_json_file) as shapes_file:
    geo_json_countries = json.load(shapes_file)

with open("./assets/indicator_config.json") as config_file:
    indicators_config = json.load(config_file)

unicef = sdmx.Request("UNICEF", timeout=5)

metadata = unicef.dataflow("TRANSMONEE", provider="ECARO", version="1.0")
dsd = metadata.structure["DSD_ECARO_TRANSMONEE"]

indicator_names = {
    code.id: code.name.en
    for code in dsd.dimensions.get("INDICATOR").local_representation.enumerated
}
# lbassil: get the age groups code list as it is not in the DSD
cl_age = unicef.codelist("CL_AGE", version="1.0")
age_groups = sdmx.to_pandas(cl_age)
dict_age_groups = age_groups["codelist"]["CL_AGE"].reset_index()
age_groups_names = {
    age["CL_AGE"]: age["name"]
    for index, age in dict_age_groups.iterrows()
    if age["CL_AGE"] != "_T"
}

units_names = {
    unit.id: str(unit.name)
    for unit in dsd.attributes.get("UNIT_MEASURE").local_representation.enumerated
}

# lbassil: get the names of the residence dimensions
residence_names = {
    residence.id: str(residence.name)
    for residence in dsd.dimensions.get("RESIDENCE").local_representation.enumerated
}

# lbassil: get the names of the wealth quintiles dimensions
wealth_names = {
    wealth.id: str(wealth.name)
    for wealth in dsd.dimensions.get("WEALTH_QUINTILE").local_representation.enumerated
}

gender_names = {"F": "Female", "M": "Male", "_T": "Total"}

dimension_names = {
    "SEX": "Sex_name",
    "AGE": "Age_name",
    "RESIDENCE": "Residence_name",
    "WEALTH_QUINTILE": "Wealth_name",
}

years = list(range(2010, 2022))

# a key:value dictionary of countries where the 'key' is the country name as displayed in the selection
# tree whereas the 'value' is the country name as returned by the sdmx list: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/codelist/UNICEF/CL_COUNTRY/1.0
countries_iso3_dict = {
    "Albania": "ALB",
    "Andorra": "AND",
    "Armenia": "ARM",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Bosnia and Herzegovina": "BIH",
    "Bulgaria": "BGR",
    "Croatia": "HRV",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Denmark": "DNK",
    "Estonia": "EST",
    "Finland": "FIN",
    "France": "FRA",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Greece": "GRC",
    "Holy See": "VAT",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "Ireland": "IRL",
    "Italy": "ITA",
    "Kazakhstan": "KAZ",
    "Kosovo (UN SC resolution 1244)": "XKX",  # UNDP defines it as KOS
    "Kyrgyzstan": "KGZ",
    "Latvia": "LVA",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Malta": "MLT",
    "Monaco": "MCO",
    "Montenegro": "MNE",
    "Netherlands": "NLD",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Poland": "POL",
    "Portugal": "PRT",
    "Republic of Moldova": "MDA",
    "Romania": "ROU",
    "Russian Federation": "RUS",
    "San Marino": "SMR",
    "Serbia": "SRB",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Spain": "ESP",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Tajikistan": "TJK",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Ukraine": "UKR",
    "United Kingdom": "GBR",
    "Uzbekistan": "UZB",
}

# create a list of country names in the same order as the countries_iso3_dict
countries = list(countries_iso3_dict.keys())

unicef_country_prog = [
    "Albania",
    "Armenia",
    "Azerbaijan",
    "Belarus",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Georgia",
    "Greece",
    "Kazakhstan",
    "Kosovo (UN SC resolution 1244)",
    "Kyrgyzstan",
    "Montenegro",
    "North Macedonia",
    "Republic of Moldova",
    "Romania",
    "Serbia",
    "Tajikistan",
    "Turkey",
    "Turkmenistan",
    "Ukraine",
    "Uzbekistan",
]

country_selections = [
    {
        "label": "Eastern Europe and Central Asia",
        "value": [
            {"label": "Caucasus", "value": ["Armenia", "Azerbaijan", "Georgia"]},
            {
                "label": "Western Balkans",
                "value": [
                    "Albania",
                    "Bosnia and Herzegovina",
                    "Croatia",
                    "Kosovo (UN SC resolution 1244)",
                    "North Macedonia",
                    "Montenegro",
                    "Serbia",
                ],
            },
            {
                "label": "Central Asia",
                "value": [
                    "Kazakhstan",
                    "Kyrgyzstan",
                    "Tajikistan",
                    "Turkmenistan",
                    "Uzbekistan",
                ],
            },
            {
                "label": "Eastern Europe",
                "value": [
                    "Bulgaria",
                    "Belarus",
                    "Republic of Moldova",
                    "Romania",
                    "Russian Federation",
                    "Turkey",
                    "Ukraine",
                ],
            },
        ],
    },
    {
        "label": "Western Europe",
        "value": [
            "Andorra",
            "Austria",
            "Belgium",
            "Cyprus",
            "Czech Republic",
            "Denmark",
            "Estonia",
            "Finland",
            "France",
            "Germany",
            "Greece",
            "Holy See",
            "Hungary",
            "Iceland",
            "Ireland",
            "Italy",
            "Latvia",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Malta",
            "Monaco",
            "Netherlands",
            "Norway",
            "Poland",
            "Portugal",
            "San Marino",
            "Slovakia",
            "Slovenia",
            "Spain",
            "Sweden",
            "Switzerland",
            "United Kingdom",
        ],
    },
    {
        "label": "By EU Engagement",
        "value": [
            {
                "label": "Central Asia",
                "value": [
                    "Kazakhstan",
                    "Kyrgyzstan",
                    "Tajikistan",
                    "Turkmenistan",
                    "Uzbekistan",
                ],
            },
            {
                "label": "Eastern Partnership",
                "value": [
                    "Armenia",
                    "Azerbaijan",
                    "Belarus",
                    "Georgia",
                    "Republic of Moldova",
                    "Ukraine",
                ],
            },
            {
                "label": "EFTA",
                "value": ["Iceland", "Liechtenstein", "Norway", "Switzerland"],
            },
            {
                "label": "EU Member States",
                "value": [
                    "Andorra",
                    "Austria",
                    "Belgium",
                    "Bulgaria",
                    "Croatia",
                    "Cyprus",
                    "Czech Republic",
                    "Denmark",
                    "Estonia",
                    "Finland",
                    "France",
                    "Germany",
                    "Greece",
                    "Hungary",
                    "Ireland",
                    "Italy",
                    "Latvia",
                    "Lithuania",
                    "Luxembourg",
                    "Malta",
                    "Netherlands",
                    "Poland",
                    "Portugal",
                    "Romania",
                    "Slovakia",
                    "Slovenia",
                    "Spain",
                    "Sweden",
                ],
            },
            {
                "label": "Other",
                "value": [
                    "Andorra",
                    "Monaco",
                    "Holy See",
                    "San Marino",
                ],
            },
            {
                "label": "Pre-accession countries",
                "value": [
                    "Albania",
                    "Bosnia and Herzegovina",
                    "Kosovo (UN SC resolution 1244)",
                    "North Macedonia",
                    "Montenegro",
                    "Serbia",
                    "Turkey",
                ],
            },
            {
                "label": "Russian Federation",
                "value": ["Russian Federation"],
            },
            {
                "label": "United Kingdom (left EU on January 31, 2020)",
                "value": ["United Kingdom"],
            },
        ],
    },
]

data_sources = {
    "CDDEM": "CountDown 2030",
    "CCRI": "Children's Climate Risk Index",
    "UN Treaties": "UN Treaties",
    "ESTAT": "Euro Stat",
    "Helix": " Health Entrepreneurship and LIfestyle Xchange",
    "ILO": "International Labour Organization",
    "WHO": "World Health Organization",
    "Immunization Monitoring (WHO)": "Immunization Monitoring (WHO)",
    "WB": "World Bank",
    "OECD": "Organisation for Economic Co-operation and Development",
    "SDG": "Sustainable Development Goals",
    "UIS": "UNESCO Institute for Statistics",
    "NEW_UIS": "UNESCO Institute for Statistics",
    "UNDP": "United Nations Development Programme",
    "TMEE": "Transformative Monitoring for Enhanced Equity",
}

topics_subtopics = {
    "All": ["All"],
    "Education, Leisure, and Culture": [
        {"Participation": "Education access and participation"},
        {"Quality": "Learning quality and skills"},
        {"System": "Education system"},
    ],
    "Family Environment and Protection": [
        {"Violence": "Violence against Children and Women"},
        {"Care": "Children without parental care"},
        {"Justice": "Justice for Children"},
        {"Marriage": "Child marriage and other harmful practices"},
        {"Labour": "Child labour and other forms of exploitation"},
    ],
    "Health and Nutrition": [
        {"HS": "Health System"},
        {"MNCH": "Maternal, newborn and child health"},
        {"Immunization": "Immunization"},
        {"Nutrition": "Nutrition"},
        {"Adolescent": "Adolescent physical, mental, and reproductive health"},
        {"HIVAIDS": "HIV/AIDS"},
        {"Wash": "Water, sanitation and hygiene"},
    ],
    "Poverty and Social Protection": [
        {"Poverty": "Child Poverty and Material Deprivation"},
        {"Protection": "Social protection system"},
    ],
    "Child Rights Landscape and Governance": [
        {"Demography": "Demographics"},
        {"Economy": "Political Economy"},
        {"Migration": "Migration and Displacement"},
        {"Access": "Access to Justice"},
        {"Data": "Data on Children"},
        {"Spending": "Public spending on Children"},
    ],
    "Participation and Civil Rights": [
        {"Registration": "Birth registration and identity"},
        {"Information": "Information, Internet and Protection of privacy"},
        {"Leisure": "Education, Leisure, and Culture"},
    ],
}

dict_topics_subtopics = {
    "Education, Leisure, and Culture": [
        "Education access and participation",
        "Learning quality and skills",
        "Education System",
    ],
    "Family Environment and Protection": [
        "Violence against Children and Women",
        "Children without parental care",
        "Justice for Children",
        "Child marriage and other harmful practices",
        "Child labour and other forms of exploitation",
    ],
    "Health and Nutrition": [
        "Health System",
        "Maternal, newborn and child health",
        "Immunization",
        "Nutrition",
        "Adolescent physical, mental, and reproductive health",
        "HIV/AIDS",
        "Water, sanitation and hygiene",
    ],
    "Poverty and Social Protection": [
        "Child Poverty and Material Deprivation",
        "Social protection system",
    ],
    "Child Rights Landscape and Governance": [
        "Demographics",
        "Political Economy",
        "Migration and Displacement",
        "Access to Justice",
        "Data on Children",
        "Public spending on Children",
    ],
    "Participation and Civil Rights": [
        "Birth registration and identity",
        "Information, Internet and Protection of privacy",
        "Leisure and Culture",
    ],
}


def get_search_countries(add_all):
    all_countries = {"label": "All", "value": "All"}
    countries_list = [
        {
            "label": key,
            "value": countries_iso3_dict[key],
        }
        for key in countries_iso3_dict.keys()
    ]
    if add_all:
        countries_list.insert(0, all_countries)
    return countries_list


def get_sector(subtopic):
    for key in dict_topics_subtopics.keys():
        if subtopic.strip() in dict_topics_subtopics.get(key):
            return key
    return ""


# function to check if the config of a certain indicator are only about its dtype
def only_dtype(config):
    return list(config.keys()) == ["DTYPE"]


def get_filtered_dataset(
    indicators: list,
    years: list,
    country_codes: list,
    breakdown: str = "TOTAL",  # send default breakdown as Total
    dimensions: dict = {},
    latest_data: bool = True,
) -> pd.DataFrame:

    # TODO: This is temporary, need to move to config
    # Add all dimensions by default to the keys
    keys = {
        "REF_AREA": country_codes,
        "INDICATOR": indicators,
        "SEX": [],
        "AGE": [],
        "RESIDENCE": [],
        "WEALTH_QUINTILE": [],
    }

    # get the first indicator of the list... we have more than one indicator in the cards
    indicator_config = (
        indicators_config[indicators[0]] if indicators[0] in indicators_config else {}
    )
    # check if the indicator has special config, update the keys from the config
    if indicator_config and not only_dtype(indicator_config):
        # TODO: need to confirm that a TOTAL is always available when a config is available for the indicator
        card_keys = indicator_config[breakdown].copy()
        if (
            dimensions
        ):  # if we are sending cards related filters, update the keys with the set values
            card_keys.update(dimensions)
        keys.update(card_keys)  # update the keys with the sent values

    try:
        data = unicef.data(
            "TRANSMONEE",
            provider="ECARO",
            key=keys,
            params=dict(
                startPeriod=years[0],
                endPeriod=years[-1],
                lastNObservations=1 if latest_data else 0,
            ),
            dsd=dsd,
        )
        logging.debug(f"URL: {data.response.url} CACHED: {data.response.from_cache}")
    except HTTPError as e:
        logging.exception(f"URL: {e.response}", e)
        # TODO: Maybe do something better here
        return pd.DataFrame()

    # lbassil: add sorting by Year to display the years in proper order on the x-axis
    dtype = (
        eval(indicator_config["DTYPE"]) if "DTYPE" in indicator_config else np.float64
    )
    data = (
        data.to_pandas(attributes="o", rtype="rows", dtype=dtype)
        .sort_values(by=["TIME_PERIOD"])
        .reset_index()
    )
    data.rename(columns={"value": "OBS_VALUE", "INDICATOR": "CODE"}, inplace=True)
    # replace Yes by 1 and No by 0
    data.OBS_VALUE.replace({"Yes": "1", "No": "0", "<": "", ">": ""}, inplace=True)

    # convert to numeric and round
    data["OBS_VALUE"] = pd.to_numeric(data.OBS_VALUE, errors="coerce")
    data.dropna(subset=["OBS_VALUE"], inplace=True)
    # round based on indicator unit: index takes 3 decimals
    ind_unit = data.UNIT_MEASURE.iloc[0].value
    data = data.round({"OBS_VALUE": 3 if ind_unit == "IDX" else 1})
    # round to whole number if values greater than one (and not index)
    if ind_unit != "IDX":
        data.loc[data.OBS_VALUE > 1, "OBS_VALUE"] = data[
            data.OBS_VALUE > 1
        ].OBS_VALUE.round()
    # converting TIME_PERIOD to numeric: we should get integers by default
    data["TIME_PERIOD"] = pd.to_numeric(data.TIME_PERIOD)

    # lbassil: add the code to fill the country names
    countries_val_list = list(countries_iso3_dict.values())

    def create_labels(row):
        row["Country_name"] = countries[countries_val_list.index(row["REF_AREA"])]
        row["Unit_name"] = str(units_names.get(str(row["UNIT_MEASURE"]), ""))
        row["Sex_name"] = str(gender_names.get(str(row["SEX"]), ""))
        row["Residence_name"] = str(residence_names.get(str(row["RESIDENCE"]), ""))
        row["Wealth_name"] = str(wealth_names.get(str(row["WEALTH_QUINTILE"]), ""))
        row["Age_name"] = str(age_groups_names.get(str(row["AGE"]), ""))
        return row

    data = data.apply(create_labels, axis="columns")

    return data


# create two dicts, one for display tree and one with the index of all possible selections
selection_index = collections.OrderedDict({"0": countries})
selection_tree = dict(title="Select All", key="0", children=[])
for num1, group in enumerate(country_selections):
    parent = dict(title=group["label"], key=f"0-{num1}", children=[])
    group_countries = []

    for num2, region in enumerate(group["value"]):
        child_region = dict(
            title=region["label"] if "label" in region else region,
            key=f"0-{num1}-{num2}",
            children=[],
        )
        parent.get("children").append(child_region)
        if "value" in region:
            selection_index[f"0-{num1}-{num2}"] = (
                region["value"]
                if isinstance(region["value"], list)
                else [region["value"]]
            )
            for num3, country in enumerate(region["value"]):
                child_country = dict(title=country, key=f"0-{num1}-{num2}-{num3}")
                if len(region["value"]) > 1:
                    # only create child nodes for more then one child
                    child_region.get("children").append(child_country)
                    selection_index[f"0-{num1}-{num2}-{num3}"] = [country]
                group_countries.append(country)
        else:
            selection_index[f"0-{num1}-{num2}"] = [region]
            group_countries.append(region)

    selection_index[f"0-{num1}"] = group_countries
    selection_tree.get("children").append(parent)

programme_country_indexes = [
    next(
        key
        for key, value in selection_index.items()
        if value[0] == item and len(value) == 1
    )
    for item in unicef_country_prog
]

# path to excel data dictionary in repo
github_url = "https://github.com/UNICEFECAR/data-etl/raw/proto_API/tmee/data_in/data_dictionary/indicator_dictionary_TM_v8.xlsx"
data_dict_content = requests.get(github_url).content
# Reading the downloaded content and turning it into a pandas dataframe and read Snapshot sheet from excel data-dictionary
snapshot_df = pd.read_excel(BytesIO(data_dict_content), sheet_name="Snapshot")
snapshot_df.dropna(subset=["Source_name"], inplace=True)
snapshot_df["Source"] = snapshot_df["Source_name"].apply(lambda x: x.split(":")[0])
# read indicators table from excel data-dictionary
df_topics_subtopics = pd.read_excel(BytesIO(data_dict_content), sheet_name="Indicator")
df_topics_subtopics.dropna(subset=["Issue"], inplace=True)
df_sources = pd.merge(df_topics_subtopics, snapshot_df, how="outer", on=["Code"])
# assign source = TMEE to all indicators without a source since they all come from excel data collection files
df_sources.fillna("TMEE", inplace=True)
# Concatenate sectors/subtopics dictionary value lists (mapping str lower)
sitan_subtopics = list(map(str.lower, sum(dict_topics_subtopics.values(), [])))

df_sources.rename(
    columns={
        "Name_x": "Indicator",
        "Issue": "Subdomain",
    },
    inplace=True,
)
# filter the sources to keep only sitan related sectors and sub-topics
df_sources["Subdomain"] = df_sources["Subdomain"].str.strip()
df_sources["Domain"] = df_sources["Subdomain"].apply(
    lambda x: get_sector(x) if not pd.isna(x) else ""
)
df_sources["Source_Full"] = df_sources["Source"].apply(
    lambda x: data_sources[x] if not pd.isna(x) else ""
)

df_sources = df_sources[df_sources["Subdomain"].str.lower().isin(sitan_subtopics)]
# read source table from excel data-dictionary and merge
source_table_df = pd.read_excel(BytesIO(data_dict_content), sheet_name="Source")
df_sources = df_sources.merge(
    source_table_df[["Source_Id", "Source_Link"]],
    on="Source_Id",
    how="left",
    sort=False,
)
# assign source link for TMEE, url: UNICEF_RDM/indicator_code
tmee_source_link = df_sources.Source_Link.isnull()
unicef_rdm_url = "https://data.unicef.org/indicator-profile/{helix_code}/"
df_sources.loc[tmee_source_link, "Source_Link"] = df_sources[
    tmee_source_link
].Code.apply(lambda x: unicef_rdm_url.format(helix_code=x))
df_sources_groups = df_sources.groupby("Source")
df_sources_summary_groups = df_sources.groupby("Source_Full")


def get_base_layout(**kwargs):
    indicators_conf = kwargs.get("indicators")
    theme = [*indicators_conf][0]
    title_main = indicators_conf[theme].get("NAME")
    themes_row_style = {"verticalAlign": "center", "display": "flex"}
    countries_filter_style = {"display": "block"}

    return html.Div(
        [
            dcc.Store(id="indicators", data=indicators_conf),
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
                                        title_main,
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
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
                                className="my-2",
                                justify="center",
                                style=themes_row_style,
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
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
                                                        value=[0, len(years) - 1],
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
                                        width="auto",
                                    ),
                                    dbc.Col(
                                        dbc.DropdownMenu(
                                            label=f"Countries: {len(countries)}",
                                            id="collapse-countries-button",
                                            className="m-2",
                                            color="info",
                                            style=countries_filter_style,
                                            children=[
                                                dbc.Card(
                                                    dash_treeview_antd.TreeView(
                                                        id="country_selector",
                                                        multiple=True,
                                                        checkable=True,
                                                        checked=["0"],
                                                        expanded=["0"],
                                                        data=selection_tree,
                                                    ),
                                                    className="overflow-auto",
                                                    body=True,
                                                ),
                                            ],
                                        ),
                                        width="auto",
                                    ),
                                    dbc.Col(
                                        dbc.Checklist(
                                            options=[
                                                {"label": "UNICEF Country Programmes"}
                                            ],
                                            style={"color": "DeepSkyBlue"},
                                            value=[],
                                            id="programme-toggle",
                                            switch=True,
                                        ),
                                        width="auto",
                                    ),
                                ],
                                id="filter-row",
                                justify="center",
                                align="center",
                            ),
                        ]
                    ),
                ],
                # sticky="top",
                className="sticky-top bg-light",
                style={
                    "paddingBottom": 15,
                },
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    dbc.Container(
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    html.Div(
                                                        [
                                                            dbc.ButtonGroup(
                                                                id={
                                                                    "type": "button_group",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                vertical=True,
                                                                style={
                                                                    "marginBottom": "20px"
                                                                },
                                                            ),
                                                            html.Br(),
                                                            dbc.Card(
                                                                id="indicator_card",
                                                                color="primary",
                                                                outline=True,
                                                            ),
                                                        ],
                                                    ),
                                                    width=4,
                                                ),
                                                dbc.Col(
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                [
                                                                    dbc.Row(
                                                                        [
                                                                            dbc.Col(
                                                                                dbc.RadioItems(
                                                                                    id={
                                                                                        "type": "area_types",
                                                                                        "index": "AIO_AREA",
                                                                                    },
                                                                                    inline=True,
                                                                                ),
                                                                                width="auto",
                                                                            ),
                                                                            dbc.Col(
                                                                                dbc.RadioItems(
                                                                                    id={
                                                                                        "type": "area_breakdowns",
                                                                                        "index": "AIO_AREA",
                                                                                    },
                                                                                    inline=True,
                                                                                ),
                                                                                width="auto",
                                                                            ),
                                                                        ],
                                                                        justify="around",
                                                                        align="center",
                                                                    )
                                                                ],
                                                                style={
                                                                    "paddingBottom": 10
                                                                },
                                                            ),
                                                            dcc.Loading(
                                                                [
                                                                    dcc.Graph(
                                                                        id={
                                                                            "type": "area",
                                                                            "index": "AIO_AREA",
                                                                        }
                                                                    )
                                                                ]
                                                            ),
                                                            html.Div(
                                                                fa(
                                                                    "fas fa-info-circle"
                                                                ),
                                                                id="aio_area_area_info",
                                                                className="float-right",
                                                            ),
                                                            dbc.Popover(
                                                                [
                                                                    dbc.PopoverHeader(
                                                                        "Sources"
                                                                    ),
                                                                    dbc.PopoverBody(
                                                                        id={
                                                                            "type": "area_sources",
                                                                            "index": "AIO_AREA",
                                                                        }
                                                                    ),
                                                                ],
                                                                id="hover",
                                                                target="aio_area_area_info",
                                                                trigger="hover",
                                                            ),
                                                        ],
                                                    ),
                                                    width=8,
                                                ),
                                            ],
                                            justify="evenly",
                                            align="start",
                                        ),
                                        fluid=True,
                                    ),
                                ]
                            ),
                        ],
                        id={"type": "area_parent", "index": "AIO_AREA"},
                    )
                )
            ),
            html.Br(),
        ],
    )


# create Dash application

app = Dash(
    __name__,
    external_stylesheets=[
        {
            "href": "https://fonts.gstatic.com",
            "rel": "preconnect",
        },
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap",
    ],
)

# to deploy using WSGI server
server = app.server
# app tittle for web browser
app.title = "TransMonee Dashboard"
app.sub_title = (
    "Monitoring the situation of children and women in Europe and Central Asia"
)

indicators_dict = {
    "HSM": {
        "NAME": "Health System",
        "CARDS": [
            {
                "name": "",
                "indicator": "HT_SH_XPD_CHEX_GD_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_GHED_GD_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_GHED_GE_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_GHED_PP_CD",
                "suffix": "Current PPP$ range among countries",
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_OOPC_CH_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_INS_COV",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "name": "Coverage index,  Expenditures, and Insurance",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        height=500,
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_INS_COV",
            ],
            "default_graph": "bar",
            "default": "HT_SH_XPD_CHEX_GD_ZS",
        },
    },
}

# configure the Dash instance's layout
app.layout = html.Div(
    [
        html.Br(),
        dcc.Store(id="store"),
        dbc.Container(
            fluid=True,
            children=get_base_layout(indicators=indicators_dict),
        ),
        html.Button(
            id="btnScroll",
            title="Scroll to top",
            className="btn btn-dark scroll-top",
            children=[
                fa("fas fa-chevron-up"),
            ],
            style={
                "position": "fixed",
                "right": 20,
                "bottom": 20,
                "width": 50,
                "height": 50,
                "padding": 12,
                "border": 0,
                "display": "none",
            },
        ),
    ],
    id="mainContainer",
)


def make_card(
    name,
    suffix,
    indicator_sources,
    source_link,
    indicator_header,
    numerator_pairs,
):
    card = [
        dbc.CardBody(
            [
                html.H1(
                    indicator_header,
                    className="display-5",
                    style={
                        "textAlign": "center",
                        "color": "#1cabe2",
                    },
                ),
                html.H4(suffix, className="card-title"),
                html.P(name, className="lead"),
                html.Div(
                    fa("fas fa-info-circle"),
                    id="indicator_card_info",
                    style={
                        "position": "absolute",
                        "bottom": "10px",
                        "right": "10px",
                    },
                ),
            ],
            style={
                "textAlign": "center",
            },
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader(
                    html.A(
                        html.P(f"Sources: {indicator_sources}"),
                        href=source_link,
                        target="_blank",
                    )
                ),
                dbc.PopoverBody(dcc.Markdown(get_card_popover_body(numerator_pairs))),
            ],
            id="hover",
            target="indicator_card_info",
            trigger="hover",
        ),
    ]

    return card


def get_card_popover_body(sources):
    """This function is used to generate the list of countries that are part of the card's
        displayed result; it displays the countries as a list, each on a separate line

    Args:
        sources (_type_): _description_

    Returns:
        _type_: _description_
    """
    countries = []
    # lbassil: added this condition to stop the exception when sources is empty
    if len(sources) > 0:
        for index, source_info in sources.sort_values(by="OBS_VALUE").iterrows():
            countries.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
        card_countries = "\n".join(countries)
        return card_countries
    else:
        return "NA"


@app.callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
        Input("programme-toggle", "value"),
    ],
    State("indicators", "data"),
)
def apply_filters(
    years_slider,
    country_selector,
    programme_toggle,
    indicators,
):
    ctx = callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    if programme_toggle and selected == "programme-toggle":
        countries_selected = unicef_country_prog
        country_selector = programme_country_indexes
    # Add the condition to know when the user unchecks the UNICEF country programs!
    elif not country_selector or (
        not programme_toggle and selected == "programme-toggle"
    ):
        countries_selected = countries
        # Add this to check all the items in the selection tree
        country_selector = ["0"]
    else:
        for index in country_selector:
            countries_selected.update(selection_index[index])
            if countries_selected == countries:
                # if all countries are all selected then stop
                break

    countries_selected = list(countries_selected)
    country_text = f"{len(countries_selected)} Selected"
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0] : years_slider[1] + 1]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    countries_selected_codes = [
        countries_iso3_dict[country] for country in countries_selected
    ]
    current_theme = [*indicators][0]
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
    )

    return (
        selections,
        country_selector,
        # countries_selected == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def indicator_card(
    selections,
    name,
    numerator,
    suffix,
    denominator=None,
    absolute=False,
    average=False,
    min_max=False,
    sex_code=None,
    age_group=None,
):
    indicators = numerator.split(",")

    # TODO: Change to use albertos config
    # lbassil: had to change this to cater for 2 dimensions set to the indicator card like age and sex
    breakdown = "TOTAL"
    # define the empty dimensions dict to be filled based on the card data filters
    dimensions = {}
    if age_group is not None:
        dimensions["AGE"] = [age_group]
    if sex_code is not None:
        dimensions["SEX"] = [sex_code]

    filtered_data = get_filtered_dataset(
        indicators,
        selections["years"],
        selections["countries"],
        breakdown,
        dimensions,
        latest_data=True,
    )

    df_indicator_sources = df_sources[df_sources["Code"].isin(indicators)]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    indicator_sources = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )
    source_link = (
        df_indicator_sources["Source_Link"].unique()[0]
        if len(unique_indicator_sources) > 0
        else ""
    )
    # lbassil: add this check because we are getting an exception where there is no data; i.e. no totals for all dimensions mostly age for the selected indicator
    if filtered_data.empty:
        indicator_header = "No data"
        indicator_sources = "NA"
        suffix = ""
        numerator_pairs = []
        return make_card(
            name,
            suffix,
            indicator_sources,
            source_link,
            indicator_header,
            numerator_pairs,
        )

    # select last value for each country
    indicator_values = (
        filtered_data.groupby(
            [
                "Country_name",
                "TIME_PERIOD",
            ]
        ).agg({"OBS_VALUE": "sum", "CODE": "count"})
    ).reset_index()

    numerator_pairs = (
        indicator_values[indicator_values.CODE == len(indicators)]
        .groupby("Country_name", as_index=False)
        .last()
        .set_index(["Country_name", "TIME_PERIOD"])
    )

    if suffix.lower() == "countries":
        # this is a hack to accomodate small cases (to discuss with James)
        if "FREE" in numerator:
            # trick to filter number of years of free education
            indicator_sum = (numerator_pairs.OBS_VALUE >= 1).to_numpy().sum()
            sources = numerator_pairs.index.tolist()
            numerator_pairs = numerator_pairs[numerator_pairs.OBS_VALUE >= 1]
        elif absolute:
            # trick cards data availability among group of indicators and latest time_period
            # doesn't require filtering by count == len(numors)
            numerator_pairs = indicator_values.groupby(
                "Country_name", as_index=False
            ).last()
            max_time_filter = (
                numerator_pairs.TIME_PERIOD < numerator_pairs.TIME_PERIOD.max()
            )
            numerator_pairs.drop(numerator_pairs[max_time_filter].index, inplace=True)
            numerator_pairs.set_index(["Country_name", "TIME_PERIOD"], inplace=True)
            sources = numerator_pairs.index.tolist()
            indicator_sum = len(sources)
        else:
            # trick to accomodate cards for admin exams (AND for boolean indicators)
            # filter exams according to number of indicators
            indicator_sum = (
                (numerator_pairs.OBS_VALUE == len(indicators)).to_numpy().sum()
            )
            sources = numerator_pairs.index.tolist()
            numerator_pairs = numerator_pairs[
                numerator_pairs.OBS_VALUE == len(indicators)
            ]

    else:
        indicator_sum = numerator_pairs["OBS_VALUE"].to_numpy().sum()
        sources = numerator_pairs.index.tolist()
        if average and len(sources) > 1:
            indicator_sum = indicator_sum / len(sources)

    # define indicator header text: the resultant number except for the min-max range
    if min_max and len(sources) > 1:
        # use string general format
        indicator_min = "{:g}".format(numerator_pairs["OBS_VALUE"].min())
        indicator_max = "{:g}".format(numerator_pairs["OBS_VALUE"].max())
        indicator_header = f"{indicator_min} - {indicator_max}"
    else:
        # use string general format
        indicator_header = "{:g}".format(indicator_sum)

    return make_card(
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
    )


@app.callback(
    Output({"type": "button_group", "index": "AIO_AREA"}, "children"),
    Output({"type": "area_types", "index": "AIO_AREA"}, "options"),
    Output({"type": "area_types", "index": "AIO_AREA"}, "value"),
    Input("indicators", "data"),
)
def set_aio_options(indicators_dict):

    area = "AIO_AREA"
    theme = [*indicators_dict][0]

    area_types = []
    if area in indicators_dict[theme]:
        indicators = indicators_dict[theme][area].get("indicators")
        area_indicators = indicators.keys() if indicators is dict else indicators

        default_option = (
            indicators_dict[theme][area].get("default")
            if area in indicators_dict[theme]
            else ""
        )

        area_butons = [
            dbc.Button(
                indicator_names[code],
                id={"type": "indicator_button", "index": code},
                color="info",
                className="my-1",
                active=code == default_option if default_option != "" else num == 0,
            )
            for num, code in enumerate(area_indicators)
        ]

        area_types = [
            {
                "label": name.capitalize(),
                "value": name,
            }
            for name in indicators_dict[theme][area].get("graphs", {}).keys()
        ]

    default_graph = (
        indicators_dict[theme][area].get("default_graph")
        if area in indicators_dict[theme]
        else ""
    )

    return area_butons, area_types, default_graph


@app.callback(
    Output({"type": "indicator_button", "index": ALL}, "active"),
    Input({"type": "indicator_button", "index": ALL}, "n_clicks"),
    State({"type": "indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_active_button(_, buttons_id):

    # figure out which button was clicked
    ctx = callback_context
    button_code = eval(ctx.triggered[0]["prop_id"].split(".")[0])["index"]

    # return active properties accordingly
    return [button_code == id_button["index"] for id_button in buttons_id]


@app.callback(
    Output({"type": "area_breakdowns", "index": "AIO_AREA"}, "options"),
    [
        Input({"type": "indicator_button", "index": ALL}, "active"),
        Input({"type": "area_types", "index": "AIO_AREA"}, "value"),
    ],
    State({"type": "indicator_button", "index": ALL}, "id"),
)
def breakdown_options(is_active_button, fig_type, buttons_id):

    indicator = [
        ind_code["index"]
        for ind_code, truth in zip(buttons_id, is_active_button)
        if truth
    ][0]

    options = [{"label": "Total", "value": "TOTAL"}]
    # lbassil: change the disaggregation to use the names of the dimensions instead of the codes
    all_breakdowns = [
        {"label": "Sex", "value": "SEX"},
        {"label": "Age", "value": "AGE"},
        {"label": "Residence", "value": "RESIDENCE"},
        {"label": "Wealth Quintile", "value": "WEALTH_QUINTILE"},
    ]
    dimensions = indicators_config.get(indicator, {}).keys()
    # disaggregate only bar charts
    if dimensions and fig_type == "bar":
        for breakdown in all_breakdowns:
            if breakdown["value"] in dimensions:
                options.append(breakdown)
    return options


@app.callback(
    Output({"type": "area_breakdowns", "index": "AIO_AREA"}, "value"),
    Input({"type": "area_breakdowns", "index": "AIO_AREA"}, "options"),
    [
        State({"type": "area_types", "index": "AIO_AREA"}, "value"),
        State("indicators", "data"),
    ],
)
def set_default_compare(compare_options, selected_type, indicators_dict):

    area = "AIO_AREA"
    theme = [*indicators_dict][0]

    config = indicators_dict[theme][area]["graphs"][selected_type]
    default_compare = config.get("compare")

    return (
        "TOTAL"
        if selected_type != "bar" or default_compare is None
        else default_compare
        if default_compare in compare_options
        else compare_options[1]["value"]
        if len(compare_options) > 1
        else compare_options[0]["value"]
    )


@app.callback(
    [
        Output({"type": "area", "index": "AIO_AREA"}, "figure"),
        Output({"type": "area_sources", "index": "AIO_AREA"}, "children"),
        Output("indicator_card", "children"),
    ],
    [
        Input("store", "data"),
        Input({"type": "area_breakdowns", "index": "AIO_AREA"}, "value"),
    ],
    [
        State("indicators", "data"),
        State({"type": "button_group", "index": "AIO_AREA"}, "children"),
        State({"type": "area_types", "index": "AIO_AREA"}, "value"),
    ],
)
def aio_area_figure(
    selections,
    compare,
    indicators_dict,
    buttons_properties,
    selected_type,
):

    # assumes indicator is not empty
    indicator = [
        but_prop["props"]["id"]["index"]
        for but_prop in buttons_properties
        if but_prop["props"]["active"] is True
    ][0]

    area = "AIO_AREA"
    default_graph = indicators_dict[selections["theme"]][area].get(
        "default_graph", "line"
    )

    fig_type = selected_type if selected_type else default_graph
    fig_config = indicators_dict[selections["theme"]][area]["graphs"][fig_type]
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")
    layout_opt = fig_config.get("layout_options")
    dimension = False if fig_type in ["line", "map"] or compare == "TOTAL" else compare
    indicator_name = str(indicator_names.get(indicator, ""))

    data = get_filtered_dataset(
        [indicator],
        selections["years"],
        selections["countries"],
        compare,
        latest_data=False if fig_type in ["line", "map"] else True,
    ).sort_values("OBS_VALUE", ascending=False)

    # indicator card
    card_config = [
        elem
        for elem in indicators_dict[selections["theme"]]["CARDS"]
        if elem["indicator"] == indicator
    ]

    ind_card = (
        []
        if not card_config or "CARDS" not in indicators_dict[selections["theme"]]
        else indicator_card(
            selections,
            card_config[0]["name"],
            card_config[0]["indicator"],
            card_config[0]["suffix"],
            card_config[0].get("denominator"),
            card_config[0].get("absolute"),
            card_config[0].get("average"),
            card_config[0].get("min_max"),
            card_config[0].get("sex"),
            card_config[0].get("age"),
        )
    )

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, "", ind_card

    # lbassil: was UNIT_MEASURE
    name = (
        data[data["CODE"] == indicator]["Unit_name"].astype(str).unique()[0]
        if len(data[data["CODE"] == indicator]["Unit_name"].astype(str).unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == indicator]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    source = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )
    source_link = (
        df_indicator_sources["Source_Link"].unique()[0]
        if len(unique_indicator_sources) > 0
        else ""
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name

    # set the chart title, wrap the text when the indicator name is too long
    chart_title = textwrap.wrap(
        indicator_name,
        width=74,
    )
    chart_title = "<br>".join(chart_title)

    # set the layout to center the chart title and change its font size and color
    layout = go.Layout(
        title=chart_title,
        title_x=0.5,
        font=dict(family="Arial", size=12),
        legend=dict(x=1, y=0.5),
        xaxis={"categoryorder": "total descending"},
    )
    if layout_opt:
        layout.update(layout_opt)

    # Add this code to avoid having decimal year on the x-axis for time series charts
    if fig_type == "line":
        data.sort_values(by=["TIME_PERIOD", "Country_name"], inplace=True)
        layout["xaxis"] = dict(
            tickmode="linear",
            tick0=selections["years"][0],
            dtick=1,
            categoryorder="total ascending",
        )

    if dimension:
        # lbassil: use the dimension name instead of the code
        dimension_name = str(dimension_names.get(dimension, ""))
        options["color"] = dimension_name

        # sort by the compare value to have the legend in the right ascending order
        data.sort_values(by=[dimension], inplace=True)

    # rename figure_type 'map': 'choropleth' (plotly express)
    fig_type = "choropleth_mapbox" if fig_type == "map" else fig_type
    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)
    if traces:
        fig.update_traces(**traces)

    return fig, html.A(html.P(source), href=source_link, target="_blank"), ind_card


# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
