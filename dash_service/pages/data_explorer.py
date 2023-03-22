# https://data.unicef.org/resources/data_explorer/unicef_f/?ag=UNICEF&df=GLOBAL_DATAFLOW&ver=1.0&dq=AFG+ITA.CME_MRY0T4+DM_POP_TOT+WS_PPL_W-SM+CME_MRY0.&startPeriod=2012&endPeriod=2022

import dash
from dash import callback, dcc, html
from dash.exceptions import PreventUpdate
from dash_service.models import DataExplorer, Project
from dash.dependencies import MATCH, Input, Output, State, ALL
from dash_service.pages import (
    get_data,
    get_structure_id,
    get_col_name,
    get_structure,
    parse_sdmx_data_query,
)
import pandas as pd
import dash_bootstrap_components as dbc

from dash_service.components_aio.data_explorer.data_explorer_aio import DataExplorerAIO
from dash_service.components_aio.data_explorer.data_explore_filter_aio import (
    DataExplorerFilterAIO,
)
from dash_service.components_aio.data_explorer.data_explorer_table_aio import (
    DataExplorerTableAIO,
)
from dash_service.components_aio.data_explorer.data_explorer_pivot_aio import (
    DataExplorerPivotAIO,
)
from dash_service.components_aio.data_explorer.downloads_tbl_aio import (
    Downloads_tbl_AIO,
)

from dash_service.components_aio.data_explorer.data_explorer_indic_meta import (
    DataExplorerIndicatorMetaAIO,
)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 0)

_STORE_LANG = "lang"
_STORE_CONFIG = "de_config"
_STORE_DSTRUCTS = "de_data_structure"
_STORE_REQUEST_CFG = "de_request_config"
_STORE_LASTNOBS_CFG = "de_lastnobs_config"


LABELS = {DataExplorerAIO._CFG_LASTN: "Show latest data only"}
ELEM_DATAEXPLORER = "ELEM_DATAEXPLORER"
ELEM_DATAEXPLORER_TABLE = "ELEM_DATAEXPLORER_TABLE"

# TODO Move this in a cfg
OBS_COUNT_LIMIT = 5000
ID_OBS_VALUE = "OBS_VALUE"

_CONCEPT_ID_INDICATOR = ["INDICATOR"]  # A list of possible indicaotrs' concept IDs

storeitem_sel_codes = "sel_codes"
# storeitem_exp_filter = "expanded_filter"


def layout(lang="en", **query_params):

    project_slug = query_params.get("prj", None)
    page_slug = query_params.get("page", None)

    if project_slug is None or page_slug is None:
        # return render_page_template({}, "Validation Page", [], "", lang)
        return render_no_de_cfg_found(project_slug, page_slug)

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    dataexpl = DataExplorer.where(
        project___slug=project_slug, slug=page_slug
    ).first_or_404()

    config = dataexpl.content
    t = dataexpl.title

    # override config from query params
    qp_ignore_case = {k.lower(): v for k, v in query_params.items()}

    if "ag" in qp_ignore_case:
        config["data"]["agency"] = qp_ignore_case["ag"]
    if "df" in qp_ignore_case:
        config["data"]["id"] = qp_ignore_case["df"]
    if "dfv" in qp_ignore_case:
        config["data"]["version"] = qp_ignore_case["dfv"]
    if "dq" in qp_ignore_case:
        config["data"]["dq"] = qp_ignore_case["dq"]
    if "startperiod" in qp_ignore_case:
        config["data"]["startperiod"] = qp_ignore_case["startperiod"]
    if "endperiod" in qp_ignore_case:
        config["data"]["endperiod"] = qp_ignore_case["endperiod"]

    return render_page_template(config, lang)


def render_no_de_cfg_found(prj, page):
    if prj is None:
        err = "No page found, prj parameter needed, e.g. prj=rosa"
    if page is None:
        err = "No page found, page parameter needed, e.g. page=rosa_de"
    if prj is not None and page is not None:
        err = f"No page found for parameters prj={prj}&page={page}"
    template = html.Div(
        dbc.Col(
            [
                dbc.Row(html.H3(err)),
            ]
        )
    )
    return template


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
        className="container-fluid",
        children=[
            dcc.Store(id=_STORE_LANG, data=lang),
            dcc.Store(id=_STORE_CONFIG, data=config),
            dcc.Store(id=_STORE_DSTRUCTS, data={}, storage_type="session"),
            dcc.Store(id=_STORE_REQUEST_CFG, data={}),
            dcc.Store(id=_STORE_LASTNOBS_CFG, data=None),
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
    Output(DataExplorerAIO.ids.de_table_title(ELEM_DATAEXPLORER), "children"),
    Output(DataExplorerAIO.ids.de_filters(ELEM_DATAEXPLORER), "children"),
    Output(DataExplorerAIO.ids.de_lastnobs(ELEM_DATAEXPLORER), "value"),
    [
        Input(_STORE_DSTRUCTS, "data"),
    ],
    [
        State(_STORE_CONFIG, "data"),
        State(_STORE_LANG, "data"),
    ],
)
# Downloads the DSD for the data.
def structure_and_filters(de_data_structure, de_config, lang):
    data_struct_id = get_structure_id(de_config["data"])

    sel_codes = {}

    dataflow_title = de_data_structure[data_struct_id]["name"]

    dims = de_data_structure[data_struct_id]["dsd"]["dims"]
    for dim in dims:
        if not dim["is_time"]:
            if ("dq") in de_config["data"]:
                sel_filter = parse_sdmx_data_query(de_config["data"]["dq"])
                # sel_filter = parse_sdmx_data_query(
                #     "AFG+UNICEF_EAPRO+UNICEF_EAP.CME_MRY0T4."
                # )
                ##sel_filter= parse_sdmx_data_query("AFG.CME_MRY0T4._T")
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

    #    ret_pvt_controls = []

    lastnobservations = []
    if "lastnobservations" in de_config and de_config["lastnobservations"] > 0:
        lastnobservations = ["lastn"]

    # return [dataflow_title], ret_filters, lastnobservations, ret_pvt_controls
    return [dataflow_title], ret_filters, lastnobservations


def pivot_data(df, on_rows, on_cols):

    df_p = pd.pivot_table(
        df,
        index=[d["id"] for d in on_rows],
        columns=[d["id"] for d in on_cols],
        fill_value="",
        values=ID_OBS_VALUE,
        aggfunc=lambda x: x,
    )

    # start createing the data_table data
    dim_names_at = []

    # the first rows contain the header (the dims on col), e.g. if 3 dims on col then 3 header rows
    numrows = len(on_rows)
    numcols = len(on_cols)

    for c_idx in range(numcols):
        # We need n empty cells where n=number of dimensions on the rows, the header starts at n+1
        to_add = {}
        for r in range(numrows):
            to_add["_c" + str(r)] = ""
        # Add the dimension name after the empty cols, and the tooltip (in case the label gets truncated)
        to_add["_c" + str(numrows)] = on_cols[c_idx]["name"]
        dim_names_at.append({"r": c_idx, "c": "_c" + str(numrows)})

    return df_p


def create_notes(row, cols_in_note, cols_in_note_names):
    ret = [
        f"**{cols_in_note_names[a]}:** {row[a]}" for a in cols_in_note if row[a] != ""
    ]
    return "  \n".join(ret)


def pivot_tooltips(df, on_rows, on_cols, struct, struct_id):
    # Drop the empty cols (sometimes the attrib can be completely empty)
    df_t = df.dropna(how="all", axis=1)
    df_t = df_t.fillna("")

    # Get all the ids of the attrib (if it is not empty and has been dropped from the df)
    cols_in_note = [a["id"] for a in struct[struct_id]["dsd"]["attribs"]]
    cols_in_note = [a for a in cols_in_note if a in df_t.columns]
    cols_in_note_names = {a: get_col_name(struct, struct_id, a) for a in cols_in_note}

    # create a dict struct to quickly replace the attrib codes with the label
    to_replace = {}
    for attr in struct[struct_id]["dsd"]["attribs"]:
        if "codes" in attr and attr["id"] in df.columns:
            to_replace[attr["id"]] = {c["id"]: c["name"] for c in attr["codes"]}
    df_t = df_t.replace(to_replace)

    df_t["tt"] = df_t.apply(
        lambda row: create_notes(row, cols_in_note, cols_in_note_names), axis=1
    )

    df_t = pd.pivot_table(
        df_t,
        index=[d["id"] for d in on_rows],
        columns=[d["id"] for d in on_cols],
        fill_value="",
        values="tt",
        aggfunc=lambda x: x,
    )

    return df_t


def create_unique_dims_attrs_text(uniq_vals):
    ret = []
    for idx, v in enumerate(uniq_vals.values()):
        ret.append(html.B(v["name"] + ": "))
        ret.append(v["value"])
        if idx != len(uniq_vals) - 1:
            ret.append(" - ")
    return ret


# Gets the default pvt cfg (it is now default, should get it from the SDMX annotations)
def get_default_pvt_config(struct):
    ret = {}
    for dim in struct["dsd"]["dims"]:
        if dim["is_time"]:
            ret[dim["id"]] = "C"
        else:
            ret[dim["id"]] = "R"
    return ret


def update_pvt_controls(struct, uniq_dims_ids, selected_pvt_cfg):
    ret_pvt_controls = []

    for dim in struct["dsd"]["dims"]:
        visible = True
        if dim["id"] in uniq_dims_ids:
            visible = False
        on_row = False
        if selected_pvt_cfg[dim["id"]] == "R":
            on_row = True
        pvt_control = DataExplorerPivotAIO(
            aio_id=dim["id"], label=dim["name"], onrow=on_row, visible=visible
        )
        ret_pvt_controls.append(pvt_control)

    return ret_pvt_controls


def update_indicators_meta(indics):
    ret = DataExplorerIndicatorMetaAIO.render_indicators(indics)
    
    return ret


def get_code_name(code, dim_or_attrib):
    if "codes" in dim_or_attrib:
        return next(c for c in dim_or_attrib["codes"] if c["id"] == code)["name"]
    else:
        return code


# Triggered when the codes selection changes
@callback(
    [
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER), "data"
        ),
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER), "columns"
        ),
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER),
            "tooltip_data",
        ),
        Output(
            DataExplorerTableAIO.ids.dataexplorertable_tbl(ELEM_DATAEXPLORER),
            "style_data_conditional",
        ),
        Output(DataExplorerAIO.ids.de_unique_dims(ELEM_DATAEXPLORER), "children"),
        Output(DataExplorerAIO.ids.de_unique_attribs(ELEM_DATAEXPLORER), "children"),
        Output(DataExplorerAIO.ids.de_pvt_control(ELEM_DATAEXPLORER), "children"),
        Output(DataExplorerIndicatorMetaAIO.ids.dataexplorer_indic_meta(ELEM_DATAEXPLORER), "children"),
        Output(_STORE_REQUEST_CFG, "data"),
        Output(_STORE_LASTNOBS_CFG, "data"),
    ],
    [
        Input({"type": "filter_tree", "index": ALL}, "checked"),
        Input(DataExplorerAIO.ids.de_lastnobs(ELEM_DATAEXPLORER), "value"),
        Input(DataExplorerAIO.ids.de_time_period(ELEM_DATAEXPLORER), "value"),
        Input({"type": "pvt_control", "index": ALL}, "value"),
        Input({"type": "pvt_control", "index": ALL}, "id"),
    ],
    [
        State(_STORE_DSTRUCTS, "data"),
        State(_STORE_CONFIG, "data"),
        State(_STORE_LANG, "data"),
    ],
)
def selection_change(
    selections,
    lastnobs,
    time_period,
    selected_pvt_cfg,
    pvt_ids,
    de_data_structure,
    de_config,
    lang,
):
    if len(selections) == 0:
        raise PreventUpdate

    if len(lastnobs) > 0 and lastnobs[0] == "lastn":
        lastn = 1
    else:
        lastn = None

    # prepare the data query
    data_struct_id = get_structure_id(de_config["data"])
    dims = de_data_structure[data_struct_id]["dsd"]["dims"]
    dims_no_time = [d for d in dims if not d["is_time"]]
    attribs = de_data_structure[data_struct_id]["dsd"]["attribs"]
    # remove the roots from the selection nested (list comprehension)
    selections_clean = [
        [code for code in group if not code.startswith("_root_")]
        for group in selections
    ]
    # If all codes have been selected just send an empty selecition
    for i in range(len(dims_no_time)):
        if len(selections_clean[i]) == len(dims_no_time[i]["codes"]):
            selections_clean[i] = []

    # Did the user selected all?
    sel_all = True
    for sel in selections_clean:
        if len(sel) > 0:
            sel_all = False
    if sel_all:
        dq = "all"
    else:
        dq = ["+".join(c) for c in selections_clean]
        dq = ".".join(dq)

    request_cfg = {
        "agency": de_config["data"]["agency"],
        "id": de_config["data"]["id"],
        "version": de_config["data"]["version"],
        "dq": dq,
    }

    # Get the data
    df = get_data(request_cfg, time_period, lastnobservations=lastn, labels="id")

    print(f"Datapoint count: {str(len(df))}")
    # Truncate the df if an obs num limit has been defined
    """TODO Create a warning if the daset has been truncated"""
    """TODO Should we even show the truncated data? Should we just show the download + API link?"""
    print("Create a warning if the dataset has been truncated")
    if OBS_COUNT_LIMIT > 0:
        if len(df) > OBS_COUNT_LIMIT:
            print("Dataframe limited to " + str(OBS_COUNT_LIMIT) + " data points")
            df = df[0:OBS_COUNT_LIMIT]

    # Check if the dataflow contains columns (dims or attribs) containing just one value or no value at all
    unique_dims = {}
    unique_attribs = {}

    # store the dimension uniques, will be used later
    tmp_dim_uniques = {}
    for dim in dims:
        tmp_dim_uniques[dim["id"]] = list(df[dim["id"]].unique())
    # create a dictionary: {DIM_ID:{CODE_ID:CODE_LABEL}} will be used to replace the dimension codes by the labels
    code_lbl_replace = {}
    for dim in dims:
        if "codes" in dim:
            code_lbl_replace[dim["id"]] = {
                c["id"]: c["name"]
                for c in dim["codes"]
                if c["id"] in tmp_dim_uniques[dim["id"]]
            }

    cols_to_drop = []
    for dim in dims:
        if len(tmp_dim_uniques[dim["id"]]) == 1:
            cols_to_drop.append(dim["id"])
            unique_dims[dim["id"]] = {
                "name": dim["name"],
                "value": code_lbl_replace[dim["id"]][tmp_dim_uniques[dim["id"]][0]],
            }
    for attr in attribs:
        col_uniq = df[attr["id"]].unique()
        # remove None
        col_uniq = [u for u in col_uniq if u is not None]
        if len(col_uniq) == 0:
            cols_to_drop.append(attr["id"])
        elif len(col_uniq) == 1:
            unique_attribs[attr["id"]] = {
                "name": attr["name"],
                "value": get_code_name(col_uniq[0], attr),
            }
    df = df.drop(columns=cols_to_drop)

    # the pivot configuration
    if selected_pvt_cfg is None or len(selected_pvt_cfg) == 0:
        pvt_cfg = get_default_pvt_config(de_data_structure[data_struct_id])
    else:
        pvt_cfg = {}
        for idx, pvt_id in enumerate(pvt_ids):
            pvt_cfg[pvt_id["index"]] = selected_pvt_cfg[idx]

    uniq_dims_ids = [d for d in unique_dims.keys()]
    pvt_controls = update_pvt_controls(
        de_data_structure[data_struct_id], uniq_dims_ids, pvt_cfg
    )
    on_rows = [
        {"id": d["id"], "name": d["name"]}
        for d in dims
        if pvt_cfg[d["id"]] == "R" and d["id"] not in unique_dims
    ]
    on_cols = [
        {"id": d["id"], "name": d["name"]}
        for d in dims
        if pvt_cfg[d["id"]] == "C" and d["id"] not in unique_dims
    ]

    df_tooltips = pivot_tooltips(
        df, on_rows, on_cols, de_data_structure, data_struct_id
    )

    df = pivot_data(df, on_rows, on_cols)

    # The dash table needs a dictionary: col:value.
    # We're building the list of columns to be passed to the table
    tbl_cols_to_show = []
    # A column for each dimension on rows
    if len(on_rows) > 0:
        for r in on_rows:
            tbl_cols_to_show.append({"id": r["id"], "name": r["id"]})
    else:
        tbl_cols_to_show.append({"id": "OBS_VALUE", "name": "OBS_VALUE"})
    # A column for all the dimensions on cols
    tbl_cols_to_show.append({"id": "cols", "name": "cols"})
    # A column for each column in the dataframe (will contain the values)
    tbl_cols_to_show = tbl_cols_to_show + [
        {"id": "v" + str(i), "name": "v" + str(i)} for i in range(len(df.columns))
    ]

    # The pivoted dataframe can return a multiindex (>1 dim on col) or a single index (no cols, or 1 col)
    # Extract the information from both cases so that we can handle both with the same code
    col_levels_count = 0
    cols_index = []
    if isinstance(df.columns, pd.MultiIndex):
        cols_index = list(df.columns)
        col_levels_count = len(df.columns.names)
    else:
        if len(df.columns) > 1:
            col_levels_count = 1
            # convert to 1 elem tuple to match the multi index case
            cols_index = [(c,) for c in df.columns]

    tbl_data = []
    tooltip_data = []
    # create the header for the columns (first rows in the table, 1 row per dim to be visualized on cols)
    for col_level in range(col_levels_count):
        # search for the dimension we're creating the header for in the structure
        dim_on_col = next(dim for dim in dims if dim["id"] == on_cols[col_level]["id"])
        # Is it coded? (TIME_PERIOD is not)
        if "codes" in dim_on_col:
            # loop the codes created in the pivot and replace them by the label
            header_row = {
                "v"
                + str(i): code_lbl_replace[dim_on_col["id"]][cols_index[i][col_level]]
                for i in range(len(cols_index))
            }
        else:
            header_row = {
                "v" + str(i): cols_index[i][col_level] for i in range(len(cols_index))
            }
        header_row["cols"] = on_cols[col_level]["name"]
        tbl_data.append(header_row)
        tooltip_data.append(header_row)

    # Create the row for the row's titles (1 row after all the col headers)
    if len(on_rows) > 0:
        rows_header = {r["id"]: r["name"] for r in on_rows}
        tbl_data.append(rows_header)
        tooltip_data.append(rows_header)

    # now reset the multiindex and replace the row names with the labels
    df = df.reset_index()
    # replace the column names with: ROW_ID_1, ROW_ID_2..., v1, v2, v3...
    df.columns = [r["id"] for r in on_rows] + [
        "v" + str(i) for i in range(len(df.columns) - len(on_rows))
    ]

    # Replace the code for rows by the label (the dimensions)
    df = df.replace(code_lbl_replace)
    # Fill the tbl_data with the rows/values
    tbl_data = tbl_data + df.to_dict(orient="records")

    # Now create the tooltips for the rows/data
    df_tooltips = df_tooltips.reset_index()
    df_tooltips = df_tooltips.replace(code_lbl_replace)
    col_ids = [c["id"] for c in tbl_cols_to_show if c["id"] != "cols"]
    for data_row in df_tooltips.to_records(index=False):
        to_add = {
            col_ids[i]: {"value": data_row[i], "type": "markdown"}
            for i in range(len(data_row))
        }
        tooltip_data.append(to_add)

    # The table styles
    style_data_conditional = []
    # The header values (cols and rows)
    for r in on_rows:
        style_data_conditional.append(
            {
                # "if": {"column_id": r["id"]},
                # "filter_query": "{row_index} > {6}",
                "if": {"column_id": r["id"]},
                "backgroundColor": "WhiteSmoke",
            }
        )

    for c in range(col_levels_count):
        style_data_conditional.append(
            {
                "if": {"row_index": c},
                # "fontWeight": "bold",
                "backgroundColor": "WhiteSmoke",
            }
        )

    # Restore the normal color for the rows left blank for the Column header (top left ones)
    for r in on_rows:
        for c in range(col_levels_count):
            style_data_conditional.append(
                {
                    "if": {"row_index": c, "column_id": r["id"]},
                    "backgroundColor": "White",
                }
            )

    # The headers (cols and rows)
    for r in on_rows:
        style_data_conditional.append(
            {
                "if": {"column_id": r["id"], "row_index": col_levels_count},
                "backgroundColor": "lightgrey",
                "fontWeight": "bold",
            }
        )
    for c in range(col_levels_count):
        style_data_conditional.append(
            {
                "if": {"column_id": "cols", "row_index": c},
                "backgroundColor": "lightgrey",
                "fontWeight": "bold",
            }
        )

    unique_dims_html = create_unique_dims_attrs_text(unique_dims)
    unique_attrs_html = create_unique_dims_attrs_text(unique_attribs)

    indic_idx = -1
    sel_indics = None
    for idx, d in enumerate(dims):
        if d["id"] in _CONCEPT_ID_INDICATOR:
            indic_idx = idx
            break
    if indic_idx >=0:
        sel_indics = [{"id":ind, "name":get_code_name(ind, dims[indic_idx])} for ind in selections[idx]]

    indicators_meta = update_indicators_meta(sel_indics)

    return [
        tbl_data,
        tbl_cols_to_show,
        tooltip_data,
        style_data_conditional,
        unique_dims_html,
        unique_attrs_html,
        pvt_controls,
        indicators_meta,
        request_cfg,
        {"lastn": lastn},
    ]


# Data downloads
@callback(
    Output(Downloads_tbl_AIO.ids.dcc_down_excel(MATCH), "data"),
    [
        Input(Downloads_tbl_AIO.ids.btn_down_excel(MATCH), "n_clicks"),
    ],
    [
        State(_STORE_REQUEST_CFG, "data"),
        State(DataExplorerAIO.ids.de_time_period(ELEM_DATAEXPLORER), "value"),
        State(_STORE_LASTNOBS_CFG, "data"),
    ],
    prevent_initial_call=True,
)
# Downloads the DSD for the data.
def download_excel(n_clicks, request_cfg, time_period, lastn):

    df = get_data(request_cfg, time_period, lastnobservations=lastn, labels="both")

    return dcc.send_data_frame(df.to_excel, "data.xlsx", index=False)
