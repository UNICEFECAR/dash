import collections
import json
import logging
from io import BytesIO
from pathlib import Path

import numpy as np
import pandas as pd
import pandasdmx as sdmx
import plotly.express as px
import plotly.io as pio
import requests
import plotly.graph_objects as go
import textwrap


import dash_bootstrap_components as dbc
import dash_treeview_antd
from dash import dcc, html, get_asset_url, callback_context


from dash_service.components import fa
from dash_service.utils import get_geo_file

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


DEFAULT_LABELS = {
    "Country_name": "Country",
    "TIME_PERIOD": "Year",
    "Sex_name": "Sex",
    "Residence_name": "Residence",
    "Age_name": "Age",
    "Wealth_name": "Wealth Quintile",
    "OBS_FOOTNOTE": "Footnote",
    "DATA_SOURCE": "Primary Source",
}

EMPTY_CHART = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "Data request failed: reclick indicator button.<br>If this message keeps appearing,<br>then no data is available for the selected filters.",
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

parent = Path(__file__).resolve().parent
with open(parent / "../static/indicator_config.json") as config_file:
    indicators_config = json.load(config_file)

geo_json_countries = get_geo_file("ecaro.geo.json")

unicef = sdmx.Request("UNICEF", timeout=5)

metadata = unicef.dataflow("TRANSMONEE", provider="ECARO", version="1.0")
dsd = metadata.structure["DSD_ECARO_TRANSMONEE"]

indicator_names = {
    code.id: code.name.en
    for code in dsd.dimensions.get("INDICATOR").local_representation.enumerated
}
# customed names as requested by siraj: update thousands for consistency, packed indicators
customed_names = {
    # erase_name_thousands
    "DM_BRTS": "Number of births",
    "DM_POP_TOT_AGE": "Population by age",
    "HT_SN_STA_OVWGTN": "2.2.2. Number of children moderately or severely overweight",
    "DM_CHLD_POP": "Child population aged 0-17 years",
    "DM_ADOL_POP": "Adolescent population aged 10-19 years",
    "DM_TOT_POP_PROSP": "Population prospects",
    "DM_ADOL_YOUTH_POP": "Adolescent, young and youth population aged 10-24 years",
    "DM_ADULT_YOUTH_POP": "Adult youth population aged 20-29 years",
    "DM_REPD_AGE_POP": "Population of reproductive age 15-49 years",
    "MG_INTNL_MG_CNTRY_DEST_PS": "International migrant stock by country of destination",
    # customed plots
    "packed_CRG": "National Human Rights Institutions in compliance with the Paris Principles",
    "packed_EXP": "Expenditure on education levels as a percentage of government expenditure on education",
}
indicator_names.update(customed_names)
# lbassil: get the age groups code list as it is not in the DSD
cl_age = unicef.codelist("CL_AGE", version="1.0")
age_groups = sdmx.to_pandas(cl_age)
dict_age_groups = age_groups["codelist"]["CL_AGE"].reset_index()
age_groups_names = {age.iloc[0]: age.iloc[1] for _, age in dict_age_groups.iterrows()}

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

years = list(range(2000, 2023))

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
    "Türkiye": "TUR",
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
    "Türkiye",
    "Turkmenistan",
    "Ukraine",
    "Uzbekistan",
]

country_selections = [
    {
        "label": "Eastern Europe and Central Asia",
        "value": [
            "Albania",
            "Armenia",
            "Azerbaijan",
            "Belarus",
            "Bosnia and Herzegovina",
            "Bulgaria",
            "Croatia",
            "Georgia",
            "Kazakhstan",
            "Kosovo (UN SC resolution 1244)",
            "Kyrgyzstan",
            "Montenegro",
            "North Macedonia",
            "Republic of Moldova",
            "Romania",
            "Russian Federation",
            "Serbia",
            "Tajikistan",
            "Türkiye",
            "Turkmenistan",
            "Uzbekistan",
            "Ukraine",
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
]

data_sources = {
    "CDDEM": "CountDown 2030",
    "CCRI": "Children's Climate Risk Index",
    "UN Treaties": "UN Treaties",
    "ESTAT": "Eurostat",
    "Helix": "UNICEF Data Warehouse",
    "ILO": "International Labour Organization",
    "WHO": "World Health Organization",
    "Immunization Monitoring (WHO)": "Immunization Monitoring (WHO)",
    "WB": "World Bank",
    "OECD": "Organisation for Economic Co-operation and Development",
    "OECD CWD": "OECD Child Wellbeing Dashboard",
    "INFORM": "Inform Risk Index",
    "SDG": "Sustainable Development Goals",
    "UIS": "UNESCO Institute for Statistics",
    "NEW_UIS": "UNESCO Institute for Statistics",
    "UNDP": "United Nations Development Programme",
    "TMEE": "Transformative Monitoring for Enhanced Equity",
}

dict_topics_subtopics = {
    "Education, Leisure, and Culture": [
        "Education access and participation",
        "Learning quality and skills",
        "Education system",
    ],
    "Family Environment and Protection": [
        "Violence against children and women",
        "Children without parental care",
        "Justice for children",
        "Child marriage and other harmful practices",
        "Child labour and other forms of exploitation",
    ],
    "Health and Nutrition": [
        "Health system",
        "Maternal, newborn and child health",
        "Immunization",
        "Nutrition",
        "Adolescent physical, mental, and reproductive health",
        "HIV/AIDS",
        "Water, sanitation and hygiene",
    ],
    "Poverty and Social Protection": [
        "Child poverty and material deprivation",
        "Social protection system",
    ],
    "Child Rights Landscape and Governance": [
        "Demographics",
        "Political economy",
        "Migration and displacement",
        "Access to Justice",
        "Data on children",
        "Public spending on children",
        "Child rights governance",
    ],
    "Participation and Civil Rights": [
        "Birth registration and identity",
        "Information, internet and protection of privacy",
        "Leisure and culture",
    ],
}


def get_card_popover_body(sources):
    """This function is used to generate the list of countries that are part of the card's
        displayed result; it displays the countries as a list, each on a separate line

    Args:
        sources (_type_): _description_

    Returns:
        _type_: _description_
    """
    country_list = []
    # lbassil: added this condition to stop the exception when sources is empty
    if len(sources) > 0:
        # sort by values if numeric else by country
        sort_col = (
            "OBS_VALUE" if sources.OBS_VALUE.dtype.kind in "iufc" else "Country_name"
        )
        for index, source_info in sources.sort_values(by=sort_col).iterrows():
            country_list.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
        card_countries = "\n".join(country_list)
        return card_countries
    else:
        return "NA"


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
    except Exception as e:
        print(f"Requests error: {e}")
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
    # if data has no footnotes or data source then pdsdmx erases column
    if "OBS_FOOTNOTE" in data.columns:
        data = data.astype({"OBS_FOOTNOTE": str})
        data.loc[:, "OBS_FOOTNOTE"] = data.OBS_FOOTNOTE.str.wrap(70).apply(
            lambda x: x.replace("\n", "<br>")
        )
    else:
        data["OBS_FOOTNOTE"] = "NA"

    if "DATA_SOURCE" in data.columns:
        data = data.astype({"DATA_SOURCE": str})
        data.loc[:, "DATA_SOURCE"] = data.DATA_SOURCE.str.wrap(70).apply(
            lambda x: x.replace("\n", "<br>")
        )
    else:
        data["DATA_SOURCE"] = "NA"

    # if unit multiplier present convert to integer
    if "UNIT_MULTIPLIER" in data.columns:
        data = data.astype({"UNIT_MULTIPLIER": str})
        # unit multiplier thousands flag (requested by siraj)
        is_thousand = "3" in data.UNIT_MULTIPLIER.values
    else:
        is_thousand = False

    data.rename(columns={"value": "OBS_VALUE", "INDICATOR": "CODE"}, inplace=True)
    # replace Yes by 1 and No by 0
    data.OBS_VALUE.replace(
        {"(?i)Yes": "1", "(?i)No": "0", "<": "", ">": ""}, inplace=True, regex=True
    )

    # convert to numeric
    data["OBS_VALUE"] = pd.to_numeric(data.OBS_VALUE, errors="coerce")
    data.dropna(subset=["OBS_VALUE"], inplace=True)

    # if unit multiplier thousands modify obs value (requested by siraj)
    if is_thousand:
        data["UNIT_MULTIPLIER"] = pd.to_numeric(data.UNIT_MULTIPLIER, errors="coerce")
        data["OBS_VALUE"] = data["OBS_VALUE"] * 10 ** data["UNIT_MULTIPLIER"]

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
    lambda x: data_sources[x] if not pd.isna(x) and x in data_sources else ""
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


### All code above this line should be refactored to use common SDMX access libs and config at some point


def get_base_layout(**kwargs):
    indicators_conf = kwargs.get("indicators")
    main_subtitle = kwargs.get("main_subtitle")
    themes_row_style = {"verticalAlign": "center", "display": "flex"}
    countries_filter_style = {"display": "block"}
    page_prefix = kwargs.get("page_prefix")
    domain_colour = kwargs.get("domain_colour")

    return html.Div(
        [
            dcc.Store(id=f"{page_prefix}-indicators", data=indicators_conf),
            dcc.Location(id=f"{page_prefix}-theme"),
            dbc.Row(
                dbc.Col(
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
                                            html.P(
                                                main_subtitle,
                                                id=f"{page_prefix}-subtitle",
                                                className="heading-subtitle",
                                                style={
                                                    "margin-bottom": "0px",
                                                },
                                            ),
                                            html.H1(
                                                id=f"{page_prefix}-main_title",
                                                className="heading-title",
                                                style={
                                                    "color": domain_colour,
                                                    "margin-top": "5px",
                                                },
                                            ),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                )
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            html.A(
                                html.Img(
                                    id="wheel-icon",
                                    src=get_asset_url("SOCR_Diagram_Oct_2022_href.svg"),
                                    style={"background-color": "white"},
                                ),
                                href="/transmonee",
                            ),
                            dbc.Tooltip(
                                "Return to ECA CRM Framework", target="wheel-icon"
                            ),
                        ],
                        width={"size": 1, "offset": 0},
                        style={
                            "paddingTop": 15,
                        },
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                dbc.Col(
                                    [
                                        dbc.ButtonGroup(
                                            id=f"{page_prefix}-themes",
                                        ),
                                    ],
                                    width="auto",
                                ),
                                id=f"{page_prefix}-theme-row",
                                className="my-2",
                                justify="center",
                                align="center",
                                style=themes_row_style,
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        dbc.DropdownMenu(
                                            label=f"Years: {years[0]} - {years[-1]}",
                                            id=f"{page_prefix}-collapse-years-button",
                                            className="m-2",
                                            color="secondary",
                                            # block=True,
                                            children=[
                                                dbc.Card(
                                                    dcc.RangeSlider(
                                                        id=f"{page_prefix}-year_slider",
                                                        min=0,
                                                        max=len(years) - 1,
                                                        step=1,
                                                        marks={
                                                            # display only even years
                                                            index: str(year)
                                                            for index, year in enumerate(
                                                                years
                                                            )
                                                            if index % 2 == 0
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
                                            id=f"{page_prefix}-collapse-countries-button",
                                            className="m-2",
                                            color="secondary",
                                            style=countries_filter_style,
                                            children=[
                                                dbc.Card(
                                                    dash_treeview_antd.TreeView(
                                                        id=f"{page_prefix}-country_selector",
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
                                            id=f"{page_prefix}-programme-toggle",
                                            switch=True,
                                        ),
                                        width="auto",
                                    ),
                                    dbc.Col(
                                        dbc.RadioItems(
                                            id={
                                                "type": "area_types",
                                                "index": f"{page_prefix}-AIO_AREA",
                                            },
                                            className="custom-control-input-crg",
                                            labelStyle={
                                                "paddingLeft": 0,
                                                "marginLeft": "-20px",
                                            },
                                            inline=True,
                                        ),
                                        width="auto",
                                    ),
                                    # removing button for moment
                                    # dbc.Col(
                                    # [
                                    # html.Button("Download CSV", id="btn_csv"),
                                    # dcc.Download(id="download-dataframe-csv"),
                                    # ],
                                    # width="auto",
                                    # ),
                                ],
                                id=f"{page_prefix}-filter-row",
                                justify="center",
                                align="center",
                                style={
                                    "paddingTop": 15,
                                },
                            ),
                        ],
                        width={"size": 10, "offset": 0},
                    ),
                    dbc.Col(
                        width={"size": 1, "offset": 0},
                    ),
                ],
                # sticky="top",
                className="sticky-top bg-light",
                justify="center",
                align="center",
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
                                                    [
                                                        html.Div(
                                                            [
                                                                dbc.ButtonGroup(
                                                                    id={
                                                                        "type": "button_group",
                                                                        "index": f"{page_prefix}-AIO_AREA",
                                                                    },
                                                                    vertical=True,
                                                                    style={
                                                                        "marginBottom": "20px",
                                                                        "width": "95%",
                                                                    },
                                                                ),
                                                            ],
                                                            style={
                                                                "maxHeight": "400px",
                                                                "overflowY": "scroll",
                                                            },
                                                        ),
                                                        html.Br(),
                                                        dbc.Card(
                                                            id=f"{page_prefix}-indicator_card",
                                                            color="primary",
                                                            outline=True,
                                                            style={
                                                                "width": "95%",
                                                            },
                                                        ),
                                                    ],
                                                    width=3,
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
                                                                                        "type": "area_breakdowns",
                                                                                        "index": f"{page_prefix}-AIO_AREA",
                                                                                    },
                                                                                    inputStyle={
                                                                                        "color": domain_colour
                                                                                    },
                                                                                    labelStyle={
                                                                                        "paddingLeft": 0,
                                                                                        "marginLeft": "-20px",
                                                                                    },
                                                                                    inline=True,
                                                                                ),
                                                                                width="auto",
                                                                            ),
                                                                        ],
                                                                    )
                                                                ],
                                                                style={
                                                                    "paddingBottom": 10,
                                                                    "display": "flex",
                                                                    "justify-content": "flex-end",
                                                                },
                                                            ),
                                                            dcc.Loading(
                                                                [
                                                                    dcc.Graph(
                                                                        id={
                                                                            "type": "area",
                                                                            "index": f"{page_prefix}-AIO_AREA",
                                                                        }
                                                                    )
                                                                ]
                                                            ),
                                                            html.Div(
                                                                dbc.Alert(
                                                                    color="secondary",
                                                                ),
                                                                id=f"{page_prefix}-aio_area_data_info",
                                                                className="float-left",
                                                            ),
                                                            dbc.Popover(
                                                                [
                                                                    dbc.PopoverHeader(
                                                                        html.P(
                                                                            "Countries without data"
                                                                        )
                                                                    ),
                                                                    dbc.PopoverBody(
                                                                        id=f"{page_prefix}-no-data-hover-body",
                                                                        style={
                                                                            "height": "200px",
                                                                            "overflowY": "auto",
                                                                            "whiteSpace": "pre-wrap",
                                                                        },
                                                                    ),
                                                                ],
                                                                id=f"{page_prefix}-no-data-hover",
                                                                target=f"{page_prefix}-aio_area_data_info",
                                                                placement="top-start",
                                                                trigger="hover",
                                                            ),
                                                            html.Div(
                                                                dbc.Alert(
                                                                    color="secondary",
                                                                ),
                                                                id=f"{page_prefix}-aio_area_area_info",
                                                                className="float-right",
                                                            ),
                                                        ],
                                                    ),
                                                    width=9,
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
                        id={"type": "area_parent", "index": f"{page_prefix}-AIO_AREA"},
                    )
                )
            ),
        ],
    )


def make_card(
    name,
    suffix,
    indicator_sources,
    source_link,
    indicator_header,
    numerator_pairs,
    page_prefix,
    domain_colour,
):
    card = [
        dbc.CardBody(
            [
                html.H1(
                    indicator_header,
                    className="display-5",
                    style={
                        "textAlign": "center",
                        "color": domain_colour,
                    },
                ),
                html.H4(suffix, className="card-title"),
                html.P(name, className="lead"),
                html.Div(
                    fa("fas fa-info-circle"),
                    id=f"{page_prefix}-indicator_card_info",
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
                        html.P(f"Sources(s): {indicator_sources}"),
                        href=source_link,
                        target="_blank",
                    )
                ),
                dbc.PopoverBody(
                    dcc.Markdown(get_card_popover_body(numerator_pairs)),
                    style={
                        "height": "200px",
                        "overflowY": "auto",
                        "whiteSpace": "pre-wrap",
                    },
                ),
            ],
            id=f"{page_prefix}-hover",
            target=f"{page_prefix}-indicator_card_info",
            trigger="hover",
        ),
    ]

    return card


def indicator_card(
    selections,
    name,
    numerator,
    suffix,
    absolute=False,
    average=False,
    min_max=False,
    sex_code=None,
    age_group=None,
    page_prefix=None,
    domain_colour="#1cabe2",
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
            page_prefix,
            domain_colour,
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

    if "countries" in suffix.lower():
        # this is a hack to accomodate small cases (to discuss with James)
        if "FREE" in numerator or "COMP" in numerator:
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
        min_val = numerator_pairs["OBS_VALUE"].min()
        max_val = numerator_pairs["OBS_VALUE"].max()
        # string format for cards: thousands separator and number of decimals
        min_format = (
            "{:,."
            + (
                "0"
                if np.isnan(min_val) or "." not in str(min_val)
                else (
                    "0"
                    if str(min_val)[::-1][0] == "0"
                    else str(str(min_val)[::-1].find("."))
                )
            )
            + "f}"
        )
        max_format = (
            "{:,."
            + (
                "0"
                if np.isnan(max_val) or "." not in str(max_val)
                else (
                    "0"
                    if str(max_val)[::-1][0] == "0"
                    else str(str(max_val)[::-1].find("."))
                )
            )
            + "f}"
        )
        indicator_min = min_format.format(min_val)
        indicator_max = max_format.format(max_val)
        indicator_header = f"{indicator_min} - {indicator_max}"
    else:
        # string format for cards: thousands separator and number of decimals
        sum_format = (
            "{:,."
            + (
                "0"
                if np.isnan(indicator_sum) or "." not in str(indicator_sum)
                else (
                    "0"
                    if str(indicator_sum)[::-1][0] == "0"
                    else str(str(indicator_sum)[::-1].find("."))
                )
            )
            + "f}"
        )
        indicator_header = sum_format.format(indicator_sum)

    return make_card(
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
        page_prefix,
        domain_colour,
    )


graphs_dict = {
    "bar": {
        "options": dict(
            x="Country_name",
            y="OBS_VALUE",
            barmode="group",
            text="OBS_VALUE",
            hover_name="TIME_PERIOD",
            labels={
                "OBS_FOOTNOTE": "Footnote",
                "DATA_SOURCE": "Primary Source",
            },
            hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
            height=500,
        ),
        "layout_options": dict(
            xaxis_title={"standoff": 0},
            margin_t=30,
            margin_b=0,
        ),
    },
    "line": {
        "options": dict(
            x="TIME_PERIOD",
            y="OBS_VALUE",
            color="Country_name",
            hover_name="Country_name",
            labels={"OBS_FOOTNOTE": "Footnote"},
            hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
            # line_shape="spline",
            render_mode="svg",
            height=500,
        ),
        "trace_options": dict(mode="lines+markers", line=dict(width=0.8)),
        "layout_options": dict(
            xaxis_title={"standoff": 10},
            margin_t=40,
            margin_b=0,
        ),
    },
    "map": {
        "options": dict(
            locations="REF_AREA",
            featureidkey="id",
            color="OBS_VALUE",
            mapbox_style="carto-positron",
            geojson=geo_json_countries,
            zoom=2.5,
            center={"lat": 51.9194, "lon": 19.040236},
            opacity=0.6,
            labels={
                "OBS_VALUE": "Value",
                "Country_name": "Country",
                "TIME_PERIOD": "Year",
                "REF_AREA": "ISO3 Code",
                "OBS_FOOTNOTE": "Footnote",
            },
            hover_data={
                "OBS_VALUE": True,
                "REF_AREA": False,
                "Country_name": True,
                "TIME_PERIOD": True,
                "OBS_FOOTNOTE": True,
                "DATA_SOURCE": True,
            },
            height=500,
        ),
        "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 5}),
    },
}


def filters(theme, years_slider, country_selector, programme_toggle, indicators):
    ctx = callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    if programme_toggle and "programme-toggle" in selected:
        countries_selected = unicef_country_prog
        country_selector = programme_country_indexes
    # Add the condition to know when the user unchecks the UNICEF country programs!
    elif not country_selector or (
        not programme_toggle and "programme-toggle" in selected
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
    current_theme = theme[1:].upper() if theme else next(iter(indicators.keys()))
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
        count_names=countries_selected,
    )

    return (
        selections,
        country_selector,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def themes(selections, indicators_dict, page_prefix):
    title = indicators_dict[selections["theme"]].get("NAME")
    url_hash = "#{}".format((next(iter(selections.items())))[1].lower())
    # hide the buttons when only one option is available
    if len(indicators_dict.items()) == 1:
        return title, []
    buttons = [
        dbc.Button(
            value["NAME"],
            id=key,
            color=f"{page_prefix}-sub",
            className="theme mx-1",
            href=f"#{key.lower()}",
            active=url_hash == f"#{key.lower()}",
        )
        for num, (key, value) in enumerate(indicators_dict.items())
    ]
    return title, buttons


def aio_options(theme, indicators_dict, page_prefix):
    area = "AIO_AREA"
    area_types = []
    current_theme = theme["theme"]
    if area in indicators_dict[current_theme]:
        indicators = indicators_dict[current_theme][area].get("indicators")
        area_indicators = indicators.keys() if indicators is dict else indicators

        default_option = (
            indicators_dict[current_theme][area].get("default")
            if area in indicators_dict[current_theme]
            else ""
        )

        area_buttons = [
            dbc.Button(
                indicator_names[code],
                id={"type": f"{page_prefix}-indicator_button", "index": code},
                color=f"{page_prefix}",
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
            for name in indicators_dict[current_theme][area].get("graphs", {}).keys()
        ]

    default_graph = (
        indicators_dict[current_theme][area].get("default_graph")
        if area in indicators_dict[current_theme]
        else ""
    )

    return area_buttons, area_types, default_graph


def breakdown_options(is_active_button, fig_type, buttons_id, packed_config):

    indicator = [
        ind_code["index"]
        for ind_code, truth in zip(buttons_id, is_active_button)
        if truth
    ][0]

    # check if indicator is a packed config
    indicator = (
        indicator
        if indicator not in packed_config
        else packed_config[indicator]["card_key"]
    )

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


def active_button(_, buttons_id):

    # figure out which button was clicked
    ctx = callback_context
    button_code = eval(ctx.triggered[0]["prop_id"].split(".")[0])["index"]

    # return active properties accordingly
    return [button_code == id_button["index"] for id_button in buttons_id]


def default_compare(compare_options, selected_type, indicators_dict, theme):

    area = "AIO_AREA"
    current_theme = theme["theme"]

    config = indicators_dict[current_theme][area]["graphs"][selected_type]
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


def aio_area_figure(
    compare,
    selections,
    indicators_dict,
    buttons_properties,
    selected_type,
    page_prefix,
    packed_config,
    domain_colour,
    map_colour,
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
    fig_config = indicators_dict[selections["theme"]][area]["graphs"][fig_type].copy()
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")
    layout_opt = fig_config.get("layout_options")
    dimension = False if fig_type in ["line", "map"] or compare == "TOTAL" else compare
    indicator_name = str(indicator_names.get(indicator, ""))

    if indicator not in packed_config:

        # query one indicator
        data = get_filtered_dataset(
            [indicator],
            selections["years"],
            selections["countries"],
            compare,
            latest_data=False if fig_type == "line" else True,
        )

    else:

        # query packed indicators
        data = get_filtered_dataset(
            packed_config[indicator]["indicators"],
            selections["years"],
            selections["countries"],
            compare,
            latest_data=False if fig_type == "line" else True,
        )
        # map columns
        if "mapping" in packed_config[indicator]:
            for key_col in packed_config[indicator]["mapping"]:
                map_col = next(iter(packed_config[indicator]["mapping"][key_col]))
                data[map_col] = data[key_col].map(
                    packed_config[indicator]["mapping"][key_col][map_col]
                )
        if "agg" in packed_config[indicator]:
            # aggregation depends in different plot types
            if fig_type in packed_config[indicator]["agg"]:
                data = eval(packed_config[indicator]["agg"][fig_type])

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, "", [], [], []
    else:
        data.sort_values(
            "OBS_VALUE",
            ascending=False if data.OBS_VALUE.dtype.kind in "iufc" else True,
            inplace=True,
        )

    # indicator card
    card_key = (
        indicator
        if indicator not in packed_config
        else packed_config[indicator]["card_key"]
    )
    card_config = [
        elem
        for elem in indicators_dict[selections["theme"]]["CARDS"]
        if elem["indicator"] == card_key
    ]

    ind_card = (
        []
        if not card_config or "CARDS" not in indicators_dict[selections["theme"]]
        else indicator_card(
            selections,
            card_config[0]["name"],
            card_config[0]["indicator"],
            card_config[0]["suffix"],
            card_config[0].get("absolute"),
            card_config[0].get("average"),
            card_config[0].get("min_max"),
            card_config[0].get("sex"),
            card_config[0].get("age"),
            page_prefix,
            domain_colour,
        )
    )

    # lbassil: was UNIT_MEASURE
    name = (
        data[data["CODE"] == card_key]["Unit_name"].astype(str).unique()[0]
        if len(data[data["CODE"] == card_key]["Unit_name"].astype(str).unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == card_key]
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
        xaxis={
            "categoryorder": "total descending",
            "tickangle": -45,
            "tickmode": "linear",
            "tickfont_size": 10,
        },
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
        if data.OBS_VALUE.dtype.kind not in "iufc":
            layout["yaxis"] = dict(
                categoryorder="array", categoryarray=packed_config[indicator]["yaxis"]
            )

    if dimension:
        # lbassil: use the dimension name instead of the code
        dimension_name = str(dimension_names.get(dimension, ""))
        options["color"] = dimension_name

        if dimension_name == "Sex_name":
            options["color_discrete_map"] = {"Female": "#944a9d", "Male": "#1a9654"}

        # sort by the compare value to have the legend in the right ascending order
        data.sort_values(by=[dimension], inplace=True)

    # rename figure_type 'map': 'choropleth' (plotly express)
    if fig_type == "map":
        fig_type = "choropleth_mapbox"
        options["color_continuous_scale"] = map_colour
        options["range_color"] = [data.OBS_VALUE.min(), data.OBS_VALUE.max()]
    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)
    # remove x-axis title but keep space below
    fig.update_layout(xaxis_title="")
    if fig_type == "bar" and not dimension:
        fig.update_traces(marker_color=domain_colour)
    if fig_type == "line":
        fig.update_traces(**traces)

    # countries not reporting
    not_rep_count = np.setdiff1d(selections["count_names"], data.Country_name.unique())
    # number of countries from selection
    count_sel = len(selections["countries"])

    return (
        fig,
        [
            html.Div(
                [
                    html.P(
                        "Source: ",
                        style={
                            "display": "inline-block",
                            "textDecoration": "underline",
                            "fontWeight": "bold",
                        },
                    ),
                    html.A(
                        f" {source}",
                        href=source_link,
                        target="_blank",
                        id={
                            "type": "area_sources",
                            "index": f"{page_prefix}-AIO_AREA",
                        },
                        className="alert-link",
                        style={"color": domain_colour},
                    ),
                ],
            )
        ],
        ind_card,
        [
            html.Div(
                [
                    html.P(
                        "Countries without data: ",
                        style={
                            "display": "inline-block",
                            "textDecoration": "underline",
                            "fontWeight": "bold",
                        },
                    ),
                    html.P(
                        f" {len(not_rep_count)} / {count_sel}",
                        style={
                            "display": "inline-block",
                            "fontWeight": "bold",
                            "color": domain_colour,
                            "whiteSpace": "pre",
                        },
                    ),
                ]
            )
        ],
        dcc.Markdown(["- " + "\n- ".join(sorted(not_rep_count, key=str.lower))]),
    )
