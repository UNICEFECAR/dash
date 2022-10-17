from ..sdmx import data_access, data_access_sdmx
from datetime import datetime
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

years = list(range(2007, datetime.now().year))

# MOVE THIS IN CONFIG
data_endpoint_id = "UNICEF"
data_endpoint_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))


# def get_data(cfg_data, years=None, countries=[], last_n_obs=False, labels="id"):
def get_data(cfg_data, years=None):
    api_access = data_access_sdmx.DataAccess_SDMX(data_endpoint_id, data_endpoint_url)

    lastnobs = None
    if "lastnobservations" in cfg_data:
        lastnobs = cfg_data["lastnobservations"]
    startperiod = None
    endperiod = None
    if years is not None:
        startperiod = years[0]
        endperiod = years[1]
    df = api_access.get_data(
        cfg_data["agency"],
        cfg_data["id"],
        cfg_data["version"],
        dq=cfg_data["dq"],
        lastnobs=lastnobs,
        startperiod=startperiod,
        endperiod=endperiod,
        labels="name"
    )

    return df


'''
import json
import logging
import pathlib

import dash_html_components as html
import numpy as np
import pandas as pd
import pandasdmx as sdmx
from requests.exceptions import HTTPError

from ..sdmx import Codelist, Dataflow, SdmxApi

endpoint_ids = {"UNICEF": "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/"}


def get_endpoint(endpoint_id="UNICEF"):
    return endpoint_ids[endpoint_id]


years = list(range(2007, 2022))


codelists = {}





def get_codelist(agency, id, version="latest"):
    """_summary_

    Args:
        agency (_type_): _description_
        id (_type_): _description_
        version (str, optional): _description_. Defaults to "latest".

    Returns:
        _type_: _description_
    """
    cl_id = f"{agency}|{id}|{version}"
    if cl_id in codelists:
        # print("CL " + id + " already downloaded")
        return codelists[cl_id]
    # print("CL " + id + " new downloaded")

    cl = Codelist.Codelist()
    cl.download_codelist(get_endpoint(), agency, id, version=version)
    codelists[cl_id] = cl.get_codes()
    return cl.get_codes()





def get_dataset(cfg_data, years=None, countries=[], recent_data=False, labels="id"):
    """_summary_

    Args:
        cfg_data (_type_): _description_
        years (_type_, optional): _description_. Defaults to None.
        countries (list, optional): _description_. Defaults to [].
        recent_data (bool, optional): _description_. Defaults to False.

    Returns:
        _type_: _description_
    """
    api = SdmxApi.SdmxApi(get_endpoint())

    # TODO The data query must reflect the data structure, FIX THAT
    query = [q for q in cfg_data["dq"].values()]
    if len(countries) > 0:
        query[0] = "+".join(countries)

    dq = ".".join(query)
    lastnobservations = cfg_data.get("lastnobservations")
    if recent_data:
        lastnobservations = 1

    df = api.get_dataflow_as_dataframe(
        cfg_data["agency"],
        cfg_data["id"],
        cfg_data["version"],
        dataquery=dq,
        lastnobservations=lastnobservations,
        time_period=years,
        labels=labels,
    )
    return df


def get_col_unique(df: Dataflow, col_id: str) -> list:
    """_summary_

    Args:
        df (Dataflow): _description_
        col_id (str): _description_

    Returns:
        list: _description_
    """
    if not col_id in df:
        return []
    # Unique and remove nans
    ret = df[col_id].unique()
    ret = ret[~pd.isnull(ret)]
    return ret

'''
