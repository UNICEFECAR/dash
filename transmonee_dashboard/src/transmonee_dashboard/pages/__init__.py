import dash_html_components as html
import datetime
import collections
import pandas as pd
import urllib
from ..sdmx_utils import utils

years = list(range(2010, datetime.datetime.now().year))

sdmx_base_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/"
sdmx_cl_url = sdmx_base_url + "codelist/{}/{}/{}/"

url_ref_areas = sdmx_cl_url.format("BRAZIL_CO", "CL_BRAZIL_REF_AREAS", "latest")
cl_ref_areas = utils.get_codelist(sdmx_cl_url.format("BRAZIL_CO", "CL_BRAZIL_REF_AREAS", "latest"))


sel_ref_areas = [x["id"] for x in cl_ref_areas]
selection_tree = dict(title="Select All", key="0", children=[{"title":x["name"], "key":x["id"]} for x in cl_ref_areas])


# data = pd.DataFrame()
# data_query_inds = set(["REPROV_EFFINAL_MUNICIPAL"])

def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))