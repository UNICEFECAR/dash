import urllib
import pickle
import copy
import pathlib
import dash
import math
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
    "EDU_SDG_STU_L2_GLAST_MAT",
    "EDU_SDG_STU_L2_GLAST_REA",
    "EDU_SDG_STU_L1_GLAST_MAT",
    "EDU_SDG_STU_L1_G2OR3_MAT",
    "EDU_SDG_STU_L1_GLAST_REA",
    "EDU_SDG_STU_L1_G2OR3_REA",
    "EDUNF_LR_YOUTH",
    "EDU_PISA_MAT2",
    "EDU_PISA_REA2",
    "EDU_PISA_SCI2",
    "EDU_SDG_GER_L01",
    "EDUNF_PRP_L02",
    "EDUNF_ROFST_L2",
    "EDU_SDG_QUTP_L02",
    "EDU_SDG_QUTP_L1",
    "EDU_SDG_QUTP_L2",
    "EDU_SDG_QUTP_L3",
    "EDU_SDG_TRTP_L02",
    "EDU_SDG_TRTP_L1",
    "EDU_SDG_TRTP_L2",
    "EDU_SDG_TRTP_L3",
    "EDUNF_ROFST_L1",
    "EDUNF_ROFST_L2",
    "EDUNF_ROFST_L3",
    "EDUNF_OFST_L1",
    "EDUNF_OFST_L2",
    "EDUNF_OFST_L3",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_NER_L02",
    "EDUNF_NERA_L1_UNDER1",
    "EDUNF_NERA_L1",
    "EDUNF_NERA_L2",
    "EDUNF_GER_L1",
    "EDUNF_GER_L2",
    "EDUNF_GER_L2_GEN",
    "EDUNF_GER_L2_VOC",
    "EDUNF_GER_L3",
    "EDUNF_GER_L3_GEN",
    "EDUNF_GER_L3_VOC",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_STU_L1_TOT",
    "EDUNF_STU_L2_TOT",
    "EDUNF_STU_L3_TOT",
    "EDU_SDG_SCH_L1",
    "EDU_SDG_SCH_L2",
    "EDU_SDG_SCH_L3",
    "EDUNF_PRP_L02",
    "EDUNF_CR_L1",
    "EDUNF_CR_L2",
    "EDUNF_CR_L3",
    "EDUNF_DR_L1",
    "EDUNF_DR_L2",
    "EDUNF_SAP_L02",
    "EDUNF_SAP_L1T3",
    "EDUNF_SAP_L2",
    "WS_SCH_H-B",
    "WS_SCH_S-B",
    "WS_SCH_W-B",
    "EDU_CHLD_DISAB",
    "EDU_CHLD_DISAB_GENERAL",
    "EDU_CHLD_DISAB_SPECIAL",
    "EDU_CHLD_DISAB_L02",
    "EDU_CHLD_DISAB_L1",
    "EDU_CHLD_DISAB_L2",
    "EDU_CHLD_DISAB_L3",
    "JJ_CHLD_CRIME",
    "JJ_CHLD_CRIMERT",
    "PT_CHLD_1-14_PS-PSY-V_CGVR",
    "PT_CHLD_INRESIDENTIAL",
    "PT_CHLD_DISAB_PUBLIC",
    "PT_CHLD_NO_PARENTAL_CARE_PUBLIC",
    "PT_CHLD_NONPUBLIC",
    "PT_CHLD_INRESIDENTIAL_RATE_A",
    "PT_CHLD_INRESIDENTIAL_RATE_B",
    "PT_CHLD_NO_PARENTAL_CARE_RATE",
    "PT_CHLD_INCARE_FOSTER",
    "PT_CHLD_INCARE_FOSTER_RATE",
    "PT_CHLD_CARED_BY_FOSTER",
    "PT_CHLD_DISAB_FOSTER",
    "PT_CHLD_CARED_BY_FOSTER_RATE",
    "PT_CHLD_CARED_GUARDIAN",
    "PT_CHLD_DISAB_CARED_GUARDIAN",
    "PT_CHLD_CARED_GUARDIAN_RATE",
    "PT_CHLD_ENTEREDFOSTER",
    "PT_CHLD_GUARDIAN",
    "PT_CHLD_LEFTRESCARE",
    "PT_CHLD_LEFTFOSTER",
    "PT_CHLD_GUARDIAN_LEFT",
    "PT_CHLD_ADOPTION",
    "PT_CHLD_ADOPTION_DISAB",
    "PT_CHLD_ADOPTION_INTERCOUNTRY",
    "PT_CHLD_ADOPTION_INTER_COUNTRY_DISAB",
    "PT_CHLD_ADOPTION_AVAILABLE",
    "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
    "PT_CHLD_ADOPTION_INTERCOUNTRY_RATE",
    "PT_CHLD_ADOPTION_RATE",
    "JJ_CHLD_DETENTION",
    "JJ_CHLD_CONVICTED",
    "JJ_CHLD_CONVICTED_VIOLENT",
    "JJ_CHLD_CONVICTED_PROPERTY",
    "JJ_CHLD_CONVICTED_OTHER",
    "JJ_CHLD_SENTENCERT",
    "JJ_CHLD_SENTENCE_PRISION",
    "JJ_CHLD_SENTENCE_CORRECTIONAL",
    "JJ_CHLD_SENTENCE_PROBATION",
    "JJ_CHLD_SENTENCE_CUSTODIAL",
    "JJ_CHLD_SENTENCE_FINANCIAL",
    "JJ_CHLD_SENTENCE_SERVICE",
    "JJ_CHLD_SENTENCE_LABOUR",
    "JJ_CHLD_SENTENCE_OTHER",
    "JJ_CHLD_PRISION",
    "JJ_CHLD_PRETRIAL",
    "JJ_CHLD_PRISION_ADJUDICATION",
    "DM_POP_TOT_AGE",
]

years = list(range(2008, 2021))

regions = [
    {"label": "Caucasus", "value": "Armenia,Azerbaijan,Georgia"},
    {
        "label": "Western Balkans",
        "value": "Albania,Bosnia and Herzegovina,Croatia,Kosovo,North Macedonia,Montenegro,Serbia",
    },
    {
        "label": "Central Asia",
        "value": "Kazakhstan,Kyrgyzstan,Tajikistan,Turkmenistan,Uzbekistan",
    },
    {
        "label": "Eastern Europe",
        "value": "Bulgaria,Belarus,Republic of Moldova,Romania,Russian Federation,Turkey,Ukraine",
    },
    {
        "label": "Western Europe",
        "value": "Andorra,Austria,Belgium,Cyprus,Czechia,Denmark,Estonia,Finland,France,Germany,Greece,Holy See,Hungary,Iceland,Ireland,Italy,Latvia,Liechtenstein,Lithuania,Luxembourg,Malta,Monaco,Netherlands,Norway,Poland,Portugal,San Marino,Slovakia,Slovenia,Spain,Sweden,Switzerland,United Kingdom",
    },
]

countries = []
for region in regions:
    for country in region["value"].split(","):
        countries.append(country)

# Create controls
county_options = [
    {"label": str(country), "value": str(country)} for country in sorted(countries)
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


