import dash
from dash import callback, dcc, html
from dash.exceptions import PreventUpdate
from dash_service.models import DataExplorer, Project
from dash.dependencies import MATCH, Input, Output, State, ALL
import re
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
#def structure_and_filters(de_data_structure, checked, de_config, lang, selections):
def structure_and_filters(de_data_structure,de_config, lang):
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


    data_struct_id = get_structure_id(de_config["data"])
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




 


    

#     return DataExplorerFilterAIO.CLASSNAME_VISIBLE

# Triggered when the codes selection changes
@callback(
    [Output(
        DataExplorerTableAIO.ids.dataexplorertable_summary(ELEM_DATAEXPLORER),
        "children",
    )],
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
def selection_change(selections, time_period, structs, de_cfg, lang):
    print("selections")
    print(selections)
    print("de_cfg")
    print(de_cfg)
    print("time")
    print(time_period)
    
    last_n_obs = None
    # prepare the data query
    # list comprehension for the list of lists just to remove the tree roots
    dq = [[code for code in group if not code.startswith("_root_")] for group in selections]
    dq = ["+".join(c) for c in dq]
    dq = ".".join(dq)

    request_cfg = {
        "agency": de_cfg["data"]["agency"],
        "id": de_cfg["data"]["id"],
        "version": de_cfg["data"]["version"],
        "dq": dq,
    }

    df = get_data(request_cfg, time_period, lastnobservations=last_n_obs)
    print(df.head())

    # # get_data()
    # summary = []
    # for sel_code in selections[storeitem_sel_codes]:
    #     summary.append(
    #         sel_code + ": " + ",".join(selections[storeitem_sel_codes][sel_code])
    #     )
    
    return [dq]
