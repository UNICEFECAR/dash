import dash_html_components as html
import datetime
import collections
import pandas as pd
import urllib
from ..sdmx_utils import utils

years = list(range(2010, datetime.datetime.now().year))

sdmx_base_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/"
sdmx_cl_url = sdmx_base_url + "codelist/{}/{}/{}/"

url_countries = sdmx_cl_url.format("BRAZIL_CO", "CL_BRAZIL_REF_AREAS", "latest")
cl_countries = utils.get_codelist(sdmx_cl_url.format("BRAZIL_CO", "CL_BRAZIL_REF_AREAS", "latest"))

# do we need this? Can we reshape the dictionary in get_search_countries?
countries_iso3_dict = {c["name"]: c["id"] for c in cl_countries}


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


# create a list of country names in the same order as the countries_iso3_dict
countries = list(countries_iso3_dict.keys())

# Hierarchical cl?
# country_selections = [
#     {
#         "label": "Eastern Europe and Central Asia",
#         "value": [x["name"] for x in cl_countries]
#     }
# ]

# print(country_selections)

selection_index = collections.OrderedDict({"0": countries})
selection_tree = dict(title="Select All", key="0", children=[{"title":x["name"], "key":x["id"]} for x in cl_countries])

# {"title": "Subchild1", "key": "0-0-1"},

#max 3 levels? Can we make it recursive?
# for num1, group in enumerate(country_selections):
#     parent = dict(title=group["label"], key=f"0-{num1}", children=[])
#     group_countries = []
#
#     for num2, region in enumerate(group["value"]):
#         child_region = dict(
#             title=region["label"] if "label" in region else region,
#             key=f"0-{num1}-{num2}",
#             children=[],
#         )
#         parent.get("children").append(child_region)
#         if "value" in region:
#             selection_index[f"0-{num1}-{num2}"] = (
#                 region["value"]
#                 if isinstance(region["value"], list)
#                 else [region["value"]]
#             )
#             for num3, country in enumerate(region["value"]):
#                 child_country = dict(title=country, key=f"0-{num1}-{num2}-{num3}")
#                 if len(region["value"]) > 1:
#                     # only create child nodes for more then one child
#                     child_region.get("children").append(child_country)
#                     selection_index[f"0-{num1}-{num2}-{num3}"] = [country]
#                 group_countries.append(country)
#         else:
#             selection_index[f"0-{num1}-{num2}"] = [region]
#             group_countries.append(region)
#
#     selection_index[f"0-{num1}"] = group_countries
#     selection_tree.get("children").append(parent)

data = pd.DataFrame()
data_query_inds = set(["REPROV_EFFINAL_MUNICIPAL"])

# column data types coerced
'''
col_types = {
    "COVERAGE_TIME": str,
    "OBS_FOOTNOTE": str,
    "OBS_VALUE": str,
    "Frequency": str,
    "Unit multiplier": str,
    "OBS_STATUS": str,
    "Observation Status": str,
    "TIME_PERIOD": int,
}
'''

# avoid a loop to query SDMX
sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/BRAZIL_CO,BRAZIL_CO,1.0/.{}..?format=csv&startPeriod={}&endPeriod={}"
to_call = sdmx_url.format("+".join(data_query_inds), years[0], years[-1])

try:
    data_query_sdmx = pd.read_csv(to_call,
        # dtype=col_types,
        storage_options={"Accept-Encoding": "gzip"},
        low_memory=False,
    )
except urllib.error.HTTPError as e:
    raise e

data = data.append(data_query_sdmx)
# no need to create column CODE, just rename indicator
data.rename(columns={"INDICATOR": "CODE"}, inplace=True)

print(data.head())

indicators = data["Indicator"].unique()

def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))
