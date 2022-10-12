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


geo_json_file = (
    pathlib.Path(__file__).parent.parent.absolute() / "assets/countries.geo.json"
)
with open(geo_json_file) as shapes_file:
    geo_json_countries = json.load(shapes_file)

codelists = {}


def get_search_countries(countries_cl):
    all_countries = {"label": "All", "value": "All"}
    countries_list = []
    # print(countries_cl)
    # countries_list = [
    #     {
    #         "label": key,
    #         "value": countries_iso3_dict[key],
    #     }
    #     for key in countries_iso3_dict.keys()
    # ]
    # if add_all:
    #     countries_list.insert(0, all_countries)
    return countries_list


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


def _add_tree_level(tree_node, parent_code, codes):
    for c in codes:
        if "parent" in c and c["parent"] == parent_code:
            if "children" not in tree_node:
                tree_node["children"] = []
            tree_node["children"].append({"key": c["id"], "title": c["name"]})
            _add_tree_level(tree_node["children"][-1], c["id"], codes)


def get_selection_tree(ref_area_cl):
    """_summary_

    Args:
        ref_area_cl (_type_): _description_

    Returns:
        _type_: _description_
    """
    codes = get_codelist(ref_area_cl["agency"], ref_area_cl["id"])

    all_checked_codes = [code["id"] for code in codes]

    # first loop: the codes without a parent then recursive
    children = []
    for code in codes:
        if "parent" not in code:
            children.append({"key": code["id"], "title": code["name"]})
            # recursion
            _add_tree_level(children[-1], code["id"], codes)

    return {
        "data": dict(title="Select All", key="0", children=children),
        "checked": all_checked_codes,
    }


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
        labels=labels
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


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))
