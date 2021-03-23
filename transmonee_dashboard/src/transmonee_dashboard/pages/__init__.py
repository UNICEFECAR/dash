import urllib
import dash_html_components as _html
import pandas as pd
from mapbox import Geocoder


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
    "EDUNF_GER_L3",
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
]

years = [i for i in range(2008, 2021)]

regions = [
    {"label": "Caucasus", "value": "Armenia,Azerbaijan,Georgia"},
    {
        "label": "Western Balkans",
        "value": "Albania,Bosnia and Herzegovina,North Macedonia,Montenegro,Serbia",
    },
    {
        "label": "Central Asia",
        "value": "Kazakhstan,Kyrgyzstan,Tajikistan,Turkmenistan,Uzbekistan",
    },
    {"label": "Eastern Europe", "value": "Bulgaria,Croatia,Romania,Turkey"},
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
for ind in inds:
    try:
        sdmx = pd.read_csv(sdmx_url.format(ind))
    except urllib.error.HTTPError as e:
        print(ind)
        raise e

    sdmx["CODE"] = ind
    data = data.append(sdmx)


data = data.merge(
    right=pd.DataFrame(
        [dict(country=country, **geocode_address(country)) for country in countries]
    ),
    left_on="Geographic area",
    right_on="country",
)

indicators = data["Indicator"].unique()


def page_not_found(pathname):
    return _html.P("No page '{}'".format(pathname))
