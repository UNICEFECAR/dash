import urllib
import collections
import datetime as dt
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from mapbox import Geocoder
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots


mapbox_access_token = "pk.eyJ1IjoiamNyYW53ZWxsd2FyZCIsImEiOiJja2NkMW02aXcwYTl5MnFwbjdtdDB0M3oyIn0.zkIzPc4NSjLZvrY-DWrlZg"

sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv"

geocoder = Geocoder(access_token=mapbox_access_token)


def geocode_address(address):
    """Geocode street address into lat/long."""
    response = geocoder.forward(address)
    coords = response.json()["features"][0]["center"]
    return dict(longitude=coords[0], latitude=coords[1])


codes = [
    "EDUNF_OFST_L1_UNDER1",
    "EDUNF_OFST_L1",
    "EDUNF_OFST_L2",
    "EDUNF_OFST_L3",
    "EDUNF_ROFST_L1",
    "EDUNF_ROFST_L2",
    "EDUNF_ROFST_L3",
    "EDUNF_STU_L1_TOT",
    "EDUNF_STU_L2_TOT",
    "EDUNF_STU_L3_TOT",
    "EDUNF_NER_L02",
    "EDUNF_NERA_L1_UNDER1",
    "EDUNF_NERA_L1",
    "EDUNF_NERA_L2",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_TRANRA_L2",
    "EDUNF_GER_L1",
    "EDUNF_GER_L2",
    "EDUNF_GER_L2_GEN",
    "EDUNF_GER_L2_VOC",
    "EDUNF_GER_L3",
    "EDUNF_GER_L3_GEN",
    "EDUNF_GER_L3_VOC",
    "EDU_SDG_SCH_L1",
    "EDU_SDG_SCH_L2",
    "EDU_SDG_SCH_L3",
    "EDU_CHLD_DISAB",
    "EDU_CHLD_DISAB_GENERAL",
    "EDU_CHLD_DISAB_SPECIAL",
    "WS_SCH_H-B",
    "WS_SCH_S-B",
    "WS_SCH_W-B",
    "EDUNF_CR_L1",
    "EDUNF_CR_L2",
    "EDUNF_CR_L3",
    "EDUNF_DR_L1",
    "EDUNF_DR_L2",
    "EDUNF_RPTR_L1",
    "EDUNF_RPTR_L2",
    "EDUNF_ESL_L1",
    "EDUNF_ADMIN_L1_GLAST_REA",
    "EDUNF_ADMIN_L1_GLAST_MAT",
    "EDUNF_ADMIN_L2_REA",
    "EDUNF_ADMIN_L2_MAT",
    "EDUNF_ADMIN_L1_G2OR3_REA",
    "EDUNF_ADMIN_L1_G2OR3_MAT",
    "EDU_PISA_MAT",
    "EDU_PISA_REA",
    "EDU_PISA_SCI",
    "ECD_CHLD_36-59M_LMPSL",
    "EDU_SDG_STU_L2_GLAST_MAT",
    "EDU_SDG_STU_L2_GLAST_REA",
    "EDU_SDG_STU_L1_GLAST_MAT",
    "EDU_SDG_STU_L1_G2OR3_MAT",
    "EDU_SDG_STU_L1_GLAST_REA",
    "EDU_SDG_STU_L1_G2OR3_REA",
    "EDUNF_LR_YOUTH",
    "EDUNF_LR_ADULT",
    "EDU_SDG_TRTP_L02",
    "EDU_SDG_TRTP_L1",
    "EDU_SDG_TRTP_L2",
    "EDU_SDG_TRTP_L3",
    "EDU_SDG_QUTP_L02",
    "EDU_SDG_QUTP_L1",
    "EDU_SDG_QUTP_L2",
    "EDU_SDG_QUTP_L3",
    "EDU_SDG_FREE_EDU_L02",
    "EDU_SDG_COMP_EDU_L02",
    "EDUNF_STU_L01_PUB",
    "EDUNF_STU_L02_PUB",
    "EDUNF_STU_L1_PUB",
    "EDUNF_STU_L2_PUB",
    "EDUNF_STU_L3_PUB",
    "EDUNF_STU_L01_PRV",
    "EDUNF_STU_L02_PRV",
    "EDUNF_STU_L1_PRV",
    "EDUNF_STU_L2_PRV",
    "EDUNF_STU_L3_PRV",
    "EDUNF_TEACH_L1",
    "EDUNF_TEACH_L2",
    "EDUNF_TEACH_L3",
    "EDU_FIN_EXP_PT_GDP",
    "EDU_FIN_EXP_PT_TOT",
    "EDU_FIN_EXP_L02",
    "EDU_FIN_EXP_L1",
    "EDU_FIN_EXP_L2",
    "EDU_FIN_EXP_L3",
    "EDU_FIN_EXP_L4",
    "EDU_FIN_EXP_L5T8",
    "EDUNF_PRP_L02",
    "EDUNF_PRP_L1",
    "EDUNF_PRP_L2",
    "EDUNF_PRP_L3",
    # "EDU_PISA_MAT2",
    # "EDU_PISA_REA2",
    # "EDU_PISA_SCI2",
    # "EDU_SDG_GER_L01",
    # "EDUNF_SAP_L02",
    "EDUNF_SAP_L1T3",
    # "EDUNF_SAP_L2",
    # "EDU_CHLD_DISAB_L02",
    # "EDU_CHLD_DISAB_L1",
    # "EDU_CHLD_DISAB_L2",
    # "EDU_CHLD_DISAB_L3",
    "PT_CHLD_1-14_PS-PSY-V_CGVR",
    "PT_CHLD_INRESIDENTIAL",
    "PT_CHLD_DISAB_PUBLIC",
    # "PT_CHLD_NO_PARENTAL_CARE_PUBLIC",
    # "PT_CHLD_NONPUBLIC",
    # "PT_CHLD_INRESIDENTIAL_RATE_A",
    "PT_CHLD_INRESIDENTIAL_RATE_B",
    # "PT_CHLD_NO_PARENTAL_CARE_RATE",
    "PT_CHLD_INCARE_FOSTER",
    # "PT_CHLD_INCARE_FOSTER_RATE",
    "PT_CHLD_CARED_BY_FOSTER",
    "PT_CHLD_DISAB_FOSTER",
    "PT_CHLD_CARED_BY_FOSTER_RATE",
    "PT_CHLD_CARED_GUARDIAN",
    "PT_CHLD_DISAB_CARED_GUARDIAN",
    "PT_CHLD_CARED_GUARDIAN_RATE",
    "PT_CHLD_ENTEREDFOSTER",
    "PT_CHLD_GUARDIAN",
    "PT_CHLD_LEFTRESCARE",
    # "PT_CHLD_LEFTFOSTER",
    # "PT_CHLD_GUARDIAN_LEFT",
    "PT_CHLD_ADOPTION",
    "PT_CHLD_ADOPTION_DISAB",
    # "PT_CHLD_ADOPTION_INTERCOUNTRY",
    # "PT_CHLD_ADOPTION_INTER_COUNTRY_DISAB",
    "PT_CHLD_ADOPTION_AVAILABLE",
    "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
    # "PT_CHLD_ADOPTION_INTERCOUNTRY_RATE",
    "PT_CHLD_ADOPTION_RATE",
    "JJ_CHLD_CRIME",
    "JJ_CHLD_CRIMERT",
    "JJ_CHLD_DETENTION",
    "JJ_CHLD_CONVICTED",
    # "JJ_CHLD_CONVICTED_VIOLENT",
    # "JJ_CHLD_CONVICTED_PROPERTY",
    # "JJ_CHLD_CONVICTED_OTHER",
    "JJ_CHLD_SENTENCERT",
    # "JJ_CHLD_SENTENCE_PRISION",
    # "JJ_CHLD_SENTENCE_CORRECTIONAL",
    # "JJ_CHLD_SENTENCE_PROBATION",
    # "JJ_CHLD_SENTENCE_CUSTODIAL",
    # "JJ_CHLD_SENTENCE_FINANCIAL",
    # "JJ_CHLD_SENTENCE_SERVICE",
    # "JJ_CHLD_SENTENCE_LABOUR",
    # "JJ_CHLD_SENTENCE_OTHER",
    # "JJ_CHLD_PRISION",
    # "JJ_CHLD_PRETRIAL",
    # "JJ_CHLD_PRISION_ADJUDICATION",
    "JJ_CHLD_POLICE",
    "JJ_CHLD_OFFENCE",
    # "JJ_CHLD_CRIME_PERPETRATOR",
    # "JJ_CHLD_CRIME_PERSON",
    # "JJ_CHLD_CRIME_PROPERTY",
    # "JJ_CHLD_CRIME_OTHER",
    # "JJ_CHLD_ARRESTED",
    # "JJ_CHLD_VICTIM",
    # "JJ_CHLD_OFFENDER",
    "JJ_VC_PRS_UNSNT",
    "PT_ADLT_PS_NEC",
    "PT_CHLD_5-17_LBR_ECON",
    "PT_CHLD_5-17_LBR_ECON-HC",
    "PT_CHLD_LEFTRESCARE_ADOPTED",
    "PT_CHLD_LEFTRESCARE_DIED",
    "PT_CHLD_LEFTRESCARE_INDEPENDENT",
    "PT_CHLD_LEFTRESCARE_INFAMILY",
    "PT_CHLD_LEFTRESCARE_OTHER",
    "PT_CHLD_LEFTRESCARE_RETURNED",
    "PT_CHLD_LEFTRESCARE_TRANSFERED",
    "PT_F_15-19_MRD",
    "PT_F_15-49_W-BTNG",
    "PT_F_18-29_SX-V_AGE-18",
    "PT_F_20-24_MRD_U15",
    "PT_F_20-24_MRD_U18",
    "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
    "PT_F_GE15_SX_V_PTNR_12MNTH",
    "PT_M_15-19_MRD",
    "PT_M_15-49_W-BTNG",
    "PT_M_18-29_SX-V_AGE-18",
    "PT_M_20-24_MRD_U18",
    "PT_ST_13-15_BUL_30-DYS",
    "PT_VC_PRR_PHYV",
    "PT_VC_PRR_ROBB",
    "PT_VC_PRR_SEXV",
    "PT_VC_SNS_WALN",
    "PT_VC_VOV_PHYL",
    "PT_VC_VOV_ROBB",
    "PT_VC_VOV_SEXL",
    "HT_SH_XPD_OOPC_CH_ZS",
]

years = list(range(2010, 2021))

countries = [
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
    "Kyrgyzstan",
    "Kosovo (UN SC resolution 1244)",
    "Montenegro",
    "North Macedonia",
    "Republic of Moldova",
    "Romania",
    "Serbia",
    "Tajikistan",
    "Turkmenistan",
    "Turkey",
    "Ukraine",
    "Uzbekistan",
    "Andorra",
    "Austria",
    "Belgium",
    "Cyprus",
    "Czechia",
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
]

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
    "Kyrgyzstan",
    "Kosovo (UN SC resolution 1244)",
    "Montenegro",
    "North Macedonia",
    "Republic of Moldova",
    "Romania",
    "Serbia",
    "Tajikistan",
    "Turkmenistan",
    "Turkey",
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
            "Czechia",
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
                    "Austria",
                    "Belgium",
                    "Bulgaria",
                    "Croatia",
                    "Cyprus",
                    "Czechia",
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
                "value": ["Andorra", "Monaco", "Holy See", "San Marino",],
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
            {"label": "Russian Federation", "value": ["Russian Federation"],},
            {
                "label": "United Kingdom (left EU on January 31, 2020)",
                "value": ["United Kingdom"],
            },
        ],
    },
]

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

data = pd.DataFrame()
inds = set(codes)

# column data types coerced
col_types = {
    "COVERAGE_TIME": str,
    "OBS_FOOTNOTE": str,
    "Frequency": str,
    "Unit multiplier": str,
}

# avoid a loop to query SDMX
try:
    sdmx = pd.read_csv(sdmx_url.format("+".join(inds)), dtype=col_types)
except urllib.error.HTTPError as e:
    raise e

# no need to create column CODE, just rename indicator
sdmx.rename(columns={"INDICATOR": "CODE"}, inplace=True)
data = data.append(sdmx)

# TODO: Replace to static list
data = data.merge(
    right=pd.DataFrame(
        [dict(country=country, **geocode_address(country)) for country in countries]
    ),
    left_on="Geographic area",
    right_on="country",
)

# TODO: calculations for children age population

indicators = data["Indicator"].unique()


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))
