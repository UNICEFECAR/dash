import json
import pathlib
from ..sdmx import data_access, data_access_sdmx
from datetime import datetime
import pandas as pd

years = list(range(2007, datetime.now().year))

# MOVE THIS IN CONFIG
data_endpoint_id = "UNICEF"
data_endpoint_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest"


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))


# def get_data(cfg_data, years=None, countries=[], last_n_obs=False, labels="id"):
def get_structure(cfg_data):
    api_access = data_access_sdmx.DataAccess_SDMX(data_endpoint_id, data_endpoint_url)

    ret = api_access.get_dataflow_info(
        cfg_data["agency"], cfg_data["id"], cfg_data["version"]
    )

    return ret


def get_data(cfg_data, years=None, lastnobservations=None, labels="id"):
    api_access = data_access_sdmx.DataAccess_SDMX(data_endpoint_id, data_endpoint_url)

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
        lastnobs=lastnobservations,
        startperiod=startperiod,
        endperiod=endperiod,
        labels=labels,
    )

    return df


# Get geoJson
def get_geojson(geoj_filename: str):
    geojson_path = (
        f"{pathlib.Path(__file__).parent.parent.absolute()}/assets/{geoj_filename}"
    )
    with open(geojson_path) as shapes_file:
        geo_json_data = json.load(shapes_file)
    return geo_json_data


"""
SDMX structure and data utils
"""

# composes the structure id as agency|id|version
def get_structure_id(data_node):
    return f"{data_node['agency']}|{data_node['id']}|{data_node['version']}"


# Downloads and adds the structure to the struct object if it doesn't exist, skips otherwise
def add_structure(data_node, structs):
    struct_id = get_structure_id(data_node)
    if not struct_id in structs:
        print("GETTING " + struct_id)
        structs[struct_id] = get_structure(data_node)
    else:
        print(">>SKIPPED " + struct_id)


# returns the codelist attached to a dataflow's column (dimension or attribute)
def get_dim_or_attrib_from_struct(struct_id, dim_or_attrib_id, structs):

    cl = next(
        (
            dim
            for dim in structs[struct_id]["dsd"]["dims"]
            if dim["id"] == dim_or_attrib_id
        ),
        None,
    )
    if cl is None:
        cl = next(
            (
                dim
                for dim in structs[struct_id]["dsd"]["attribs"]
                if dim["id"] == dim_or_attrib_id
            ),
            None,
        )

    return cl


def get_col_name(struct_id, dim_or_attrib_id, structs):
    item = get_dim_or_attrib_from_struct(struct_id, dim_or_attrib_id, structs)
    if item is None:
        return dim_or_attrib_id
    return item["name"]

# returns a single code from a codelist
def get_code_from_codelist(codelist, code_id):
    return next(c for c in codelist if c["id"] == code_id)


# returns a single code from a structure
def get_code_from_structure(struct_id, structs, dim_or_attrib_id, code_id):
    cl = get_dim_or_attrib_from_struct(struct_id, dim_or_attrib_id, structs)
    return get_code_from_codelist(cl["codes"], code_id)


# returns the position of a dimension, used to compose/decompose the data query
def get_dim_position(structs, struct_id, dim_id):
    for idx, d in enumerate(structs[struct_id]["dsd"]["dims"]):
        if d["id"] == dim_id:
            return idx
    return -1


# merge a codes-only dataflow with the codelist
def merge_with_codelist(df, structs, struct_id, column_id):
    if not column_id in df.columns:
        return
    cl = get_dim_or_attrib_from_struct(struct_id, column_id, structs)
    if "codes" in cl:  # it is coded
        df_cl = pd.DataFrame(cl["codes"])
        df = df.merge(df_cl, how="left", left_on=column_id, right_on="id")
        df = df.drop(columns=["id", "parent"])
        df = df.rename(columns={"name": "_L_" + column_id})
    else:
        df["_L_" + column_id] = df[column_id]
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
