data = {
    "REF_AREA": {
        0: "AFG",
        1: "AFG",
        2: "AFG",
        3: "AFG",
        4: "AFG",
        5: "AFG",
        6: "AFG",
        7: "AFG",
        8: "AFG",
        9: "AFG",
    },
    "INDICATOR": {
        0: "CME_MRY0",
        1: "CME_MRY0",
        2: "CME_MRY0",
        3: "CME_MRY0",
        4: "CME_MRY0",
        5: "CME_MRY0",
        6: "CME_MRY0",
        7: "CME_MRY0",
        8: "CME_MRY0",
        9: "CME_MRY0",
    },
    "SEX": {
        0: "F",
        1: "F",
        2: "F",
        3: "F",
        4: "M",
        5: "M",
        6: "M",
        7: "M",
        8: "_T",
        9: "_T",
    },
    "TIME_PERIOD": {
        0: "2017",
        1: "2018",
        2: "2019",
        3: "2020",
        4: "2017",
        5: "2018",
        6: "2019",
        7: "2020",
        8: "2017",
        9: "2018",
    },
    "OBS_VALUE": {
        0: "46.0829342751729",
        1: "44.4837490545669",
        2: "42.9395803768476",
        3: "41.5443563157238",
        4: "52.7800954536514",
        5: "51.137169991899",
        6: "49.572874943599",
        7: "48.1144505107554",
        8: "49.5415564554033",
        9: "47.9068911062223",
    },
    "UNIT_MULTIPLIER": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "UNIT_MEASURE": {
        0: "Deaths per 1,000 live births",
        1: "Deaths per 1,000 live births",
        2: "Deaths per 1,000 live births",
        3: "Deaths per 1,000 live births",
        4: "Deaths per 1,000 live births",
        5: "Deaths per 1,000 live births",
        6: "Deaths per 1,000 live births",
        7: "Deaths per 1,000 live births",
        8: "Deaths per 1,000 live births",
        9: "Deaths per 1,000 live births",
    },
    "OBS_STATUS": {
        0: "Normal value",
        1: "Normal value",
        2: "Normal value",
        3: "Normal value",
        4: "Normal value",
        5: "Normal value",
        6: "Normal value",
        7: "Normal value",
        8: "Normal value",
        9: "Normal value",
    },
    "OBS_CONF": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "LOWER_BOUND": {
        0: "38.8419005483455",
        1: "36.6532502815758",
        2: "34.5308930683924",
        3: "32.6043333061398",
        4: "44.4555594677152",
        5: "42.2099335793974",
        6: "39.9809203848206",
        7: "37.7385775089029",
        8: "41.8536125829257",
        9: "39.6267246673408",
    },
    "UPPER_BOUND": {
        0: "53.283595753738",
        1: "52.4718685846802",
        2: "51.8934410289596",
        3: "51.4090424041007",
        4: "61.0386549769029",
        5: "60.2957267814877",
        6: "59.8792247206643",
        7: "59.6485868095637",
        8: "57.0569547943752",
        9: "56.2793662327589",
    },
    "WGTD_SAMPL_SIZE": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "OBS_FOOTNOTE": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "SERIES_FOOTNOTE": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "DATA_SOURCE": {
        0: "UN_IGME",
        1: "UN_IGME",
        2: "UN_IGME",
        3: "UN_IGME",
        4: "UN_IGME",
        5: "UN_IGME",
        6: "UN_IGME",
        7: "UN_IGME",
        8: "UN_IGME",
        9: "UN_IGME",
    },
    "SOURCE_LINK": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "CUSTODIAN": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "TIME_PERIOD_METHOD": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "REF_PERIOD": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "COVERAGE_TIME": {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    },
    "AGE": {
        0: "Total",
        1: "Total",
        2: "Total",
        3: "Total",
        4: "Total",
        5: "Total",
        6: "Total",
        7: "Total",
        8: "Total",
        9: "Total",
    },
}


import dash
from dash import callback, dcc, html
from dash.exceptions import PreventUpdate
from dash_service.models import DataExplorer, Project
from dash.dependencies import MATCH, Input, Output, State, ALL
from dash_service.pages import (
    get_data,
    add_structure,
    get_structure_id,
    get_code_from_structure_and_dq,
    get_col_name,
    merge_with_codelist,
    get_multilang_value,
    is_string_empty,
    get_structure,
    parse_sdmx_data_query,
)
import pandas as pd
import re

from dash_service.components_aio.data_explorer.data_explorer_aio import DataExplorerAIO
from dash_service.components_aio.data_explorer.data_explore_filter_aio import (
    DataExplorerFilterAIO,
)
from dash_service.components_aio.data_explorer.data_explorer_table_aio import (
    DataExplorerTableAIO,
)

_STORE_LANG = "lang"
_STORE_CONFIG = "de_config"
_STORE_DSTRUCTS = "de_data_structure"
_STORE_TIME_PERIOD = "de_time_period"
_STORE_EXPANDED_FILTER = "de_expanded_filter"
_STORE_SELECTIONS = "de_selections"


LABELS = {DataExplorerAIO._CFG_LASTN: "Show latest data only"}
ELEM_DATAEXPLORER = "ELEM_DATAEXPLORER"
ELEM_DATAEXPLORER_TABLE = "ELEM_DATAEXPLORER_TABLE"

storeitem_sel_codes = "sel_codes"
# storeitem_exp_filter = "expanded_filter"

dash.register_page(
    __name__,
    # path_template="/de/<project_slug>/<page_slug>",
    path_template="/de/<project_slug>/<dataexplorer_slug>",
    # path="/de/rosa/de_rosa",  # this is the default path and working example
)


def layout(project_slug=None, dataexplorer_slug=None, lang="en", **query_parmas):

    if project_slug is None or dataexplorer_slug is None:
        # return render_page_template({}, "Validation Page", [], "", lang)
        return html.Div()

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    dataexpl = DataExplorer.where(
        project___slug=project_slug, slug=dataexplorer_slug
    ).first_or_404()

    print(dataexpl)

    config = dataexpl.content
    t = dataexpl.title

    print(config)

    return render_page_template(config, lang)


def render_page_template(
    config: dict,
    lang,
    **kwargs,
) -> html.Div:
    """Renders the page template based on the page config and other parameters

    Args:
        config (dict): config from the database

    Returns:
        html.Div: The dash Div representing the redenderd page against the config
    """
    # data_structures={}
    # add_structure(data_structures, config["data"], lang)

    de = DataExplorerAIO(ELEM_DATAEXPLORER, cfg=config, labels=LABELS)

    # return

    template = html.Div(
        className="container",
        children=[
            dcc.Store(id=_STORE_LANG, data=lang),
            dcc.Store(id=_STORE_CONFIG, data=config),
            dcc.Store(id=_STORE_DSTRUCTS, data={}, storage_type="session"),
            dcc.Store(id=_STORE_TIME_PERIOD, data=[]),
            dcc.Store(id=_STORE_EXPANDED_FILTER, data=""),
            dcc.Store(id=_STORE_SELECTIONS, data={}),
            de,
            html.Div(id="div_loaded", children=["..."]),
        ],
    )

    return template


# Triggered when the config loaded from the database is stored in config dcc.store
@callback(
    Output(_STORE_DSTRUCTS, "data"),
    [
        Input(_STORE_CONFIG, "data"),
    ],
    [State(_STORE_DSTRUCTS, "data"), State("lang", "data")],
)
# Downloads the DSD for the data.
def download_struct(de_config, de_data_structure, lang):
    # Storing by datastructure id makes it faster to jump between dataflows
    # and prevents using the wrong datastructure stored in the session
    data_struct_id = get_structure_id(de_config["data"])
    if not data_struct_id in de_data_structure:
        print("Downloading data structure " + data_struct_id)
        ret = {data_struct_id: get_structure(de_config["data"], lang)}
        return ret
    print("Skipping data structure download " + data_struct_id)

    return de_data_structure


# Triggered when the config loaded from the database is stored in config dcc.store
@callback(
    Output(DataExplorerAIO.ids.de_filters(ELEM_DATAEXPLORER), "children"),
    # Output(_STORE_SELECTIONS, "data"),
    [
        Input(_STORE_DSTRUCTS, "data"),
        # Input({"type": "filter_tree", "index": ALL}, "checked"),
    ],
    [
        State(_STORE_CONFIG, "data"),
        State(_STORE_LANG, "data"),
        # State(_STORE_SELECTIONS, "data"),
        # State(_STORE_EXPANDED_FILTER, "data"),
    ],
)
# Downloads the DSD for the data.
# def structure_and_filters(de_data_structure, checked, de_config, lang, selections):
def structure_and_filters(de_data_structure, de_config, lang):
    data_struct_id = get_structure_id(de_config["data"])

    sel_codes = {}

    dims = de_data_structure[data_struct_id]["dsd"]["dims"]
    for dim in dims:
        if not dim["is_time"]:
            if ("dq") in de_config["data"]:
                sel_filter = parse_sdmx_data_query(de_config["data"]["dq"])
                # loop the parsed filter to make it resistant to missing dots in the dataquery
                for i in range(len(sel_filter)):
                    sel_codes[dims[i]["id"]] = sel_filter[i]

    struct = de_data_structure[data_struct_id]

    ret_filters = []

    for dim in struct["dsd"]["dims"]:
        if not dim["is_time"]:
            filter = DataExplorerFilterAIO(
                aio_id=dim["id"],
                label=dim["name"],
                expanded=False,
                items=dim["codes"],
                selected=sel_codes[dim["id"]],
            )
            ret_filters.append(filter)

    return ret_filters


# Triggered when the codes selection changes
@callback(
    [
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_summary(ELEM_DATAEXPLORER),
            "children",
        ),
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER), "data"
        ),
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER), "columns"
        ),
    ],
    [
        # Input(_STORE_SELECTIONS, "data"),
        Input({"type": "filter_tree", "index": ALL}, "checked"),
        Input(DataExplorerAIO.ids.de_time_period(ELEM_DATAEXPLORER), "value"),
    ],
    [
        State(_STORE_DSTRUCTS, "data"),
        State(_STORE_CONFIG, "data"),
        State(_STORE_LANG, "data"),
    ],
)
def selection_change(selections, time_period, de_data_structure, de_config, lang):
    # print("selections")
    # print(selections)
    # print("de_cfg")
    # print(de_cfg)
    # print("time")
    # print(time_period)

    if len(selections) == 0:
        raise PreventUpdate

    last_n_obs = None

    # prepare the data query
    data_struct_id = get_structure_id(de_config["data"])
    dims = de_data_structure[data_struct_id]["dsd"]["dims"]
    cols_to_show = dims + [{"id":"OBS_VALUE", "name":"Value"}]
    dims_no_time = [
        d for d in dims if not d["is_time"]
    ]
    #remove the roots from the selection nested (list comprehension)
    selections_clean = [
        [code for code in group if not code.startswith("_root_")]
        for group in selections
    ]
    #If all codes have been selected just sebd an empty selecition
    for i in range(len(dims_no_time)):
        if len(selections_clean[i]) == len(dims_no_time[i]["codes"]):
            selections_clean[i] = []

    dq = ["+".join(c) for c in selections_clean]
    dq = ".".join(dq)

    request_cfg = {
        "agency": de_config["data"]["agency"],
        "id": de_config["data"]["id"],
        "version": de_config["data"]["version"],
        "dq": dq,
    }

    # df = get_data(request_cfg, time_period, lastnobservations=last_n_obs)
    df = pd.DataFrame(data)
    tbl_data = df.to_dict("records")
    #tbl_cols_to_show = [{"name": c, "id": c} for c in df.columns]
    tbl_cols_to_show = [{"name": d["name"], "id": d["id"]} for d in cols_to_show]
    # print(df.head())

    return [dq, tbl_data, tbl_cols_to_show]
