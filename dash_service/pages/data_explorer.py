import dash
from dash import callback, dcc, html
from dash.exceptions import PreventUpdate
from dash_service.models import DataExplorer, Project
from dash.dependencies import MATCH, Input, Output, State, ALL
import re
from dash_service.pages import get_data
from dash_service.pages import (
    add_structure,
    get_structure_id,
    get_code_from_structure_and_dq,
    get_col_name,
    merge_with_codelist,
    get_multilang_value,
    is_string_empty,
    get_structure,
)

from dash_service.components_aio.data_explorer.data_explorer_aio import DataExplorerAIO
from dash_service.components_aio.data_explorer.data_explore_filter_aio import (
    DataExplorerFilterAIO,
)

LABELS = {DataExplorerAIO._CFG_LASTN: "Show latest data only"}
ELEM_DATAEXPLORER = "ELEM_DATAEXPLORER"

dash.register_page(
    __name__,
    # path_template="/de/<project_slug>/<page_slug>",
    path_template="/de/<project_slug>/<dataexplorer_slug>",
    # path="/de/rosa/de_rosa",  # this is the default path and working example
)


def layout(project_slug=None, dataexplorer_slug=None, lang="en", **query_parmas):

    print("in de")
    print(project_slug, dataexplorer_slug)

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
            dcc.Store(id="lang", data=lang),
            dcc.Store(id="de_config", data=config),
            dcc.Store(id="de_data_structure", data={}, storage_type="session"),
            de,
            html.Div(id="div_loaded", children=["..."]),
        ],
    )

    return template


# Triggered when the config loaded from the database is stored in config dcc.store
@callback(
    Output("de_data_structure", "data"),
    [
        Input("de_config", "data"),
    ],
    [State("de_data_structure", "data"), State("lang", "data")],
)
# Downloads the DSD for the data.
def download_struct(de_config, de_data_structure, lang):
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
    [
        Input("de_data_structure", "data"),
        Input(DataExplorerFilterAIO.ids.dataexplorerfilter_button(ALL), "n_clicks"),
    ],
    [State("de_config", "data"), State("lang", "data")],
)
# Downloads the DSD for the data.
def struct_downloaded(de_data_structure, nclicks, de_config, lang):
    triggered = dash.callback_context.triggered[0]

    filter_id = ""
    #A button was clicked
    if triggered["prop_id"] != "de_data_structure.data":
        filter_id = re.findall(r"\"aio_id\":.+?(?=,)", triggered["prop_id"])[0]
        filter_id = filter_id.split(":")[1].replace('"', "")
    
    data_struct_id = get_structure_id(de_config["data"])
    struct = de_data_structure[data_struct_id]

    ret = []

    for dim in struct["dsd"]["dims"]:
        if not dim["is_time"]:
            expanded = False
            if filter_id == dim["id"]:
                expanded = True
            filter = DataExplorerFilterAIO(
                aio_id=dim["id"], label=dim["name"], expanded=expanded
            )
            ret.append(filter)

        # print(dim.keys())

    return ret


# # Output(ChartAIO.ids.card_title(MATCH), "children"),
# @callback(
#     [Output(DataExplorerFilterAIO.ids.dataexplorerfilter_accordion_b(MATCH), "className")],
#     [Input(DataExplorerFilterAIO.ids.dataexplorerfilter_accordion(MATCH), "n_clicks")],
#     [State(DataExplorerFilterAIO.ids.dataexplorerfilter_accordion(ALL), "id")],
# )
# def filters_accordion(nclicks, all_filters):
#     triggered = dash.callback_context.triggered[0]
#     if triggered["value"] is None:
#         raise PreventUpdate
#     print("all_filters")
#     print(all_filters)
#     print(triggered)
#     print(triggered["value"])
#     print(triggered["prop_id"])
#     print(type(triggered["prop_id"]))
#     filter_id = re.findall(r"\"aio_id\":.+?(?=,)", triggered["prop_id"])[0]
#     filter_id = filter_id.split(":")[1].replace('"', "")

#     print(filter_id)


#     print(nclicks)
#     # print(filter_id)
#     if nclicks is None:
#         raise PreventUpdate
#     return ["d-none"]

# # Output(ChartAIO.ids.card_title(MATCH), "children"),
# @callback(
#     [

#         #Output(DataExplorerFilterAIO.ids.dataexplorerfilter_body(ELEM_DATAEXPLORER), "children"),

#     ],
#     [Input(DataExplorerFilterAIO.ids.dataexplorerfilter_button(ALL), "n_clicks")],
#     [State("de_data_structure", "data")],
#     prevent_initial_call=True,
# )
# def filters_accordion(nclicks, de_data_structure):
#     triggered = dash.callback_context.triggered[0]
#     if triggered["value"] is None:
#         raise PreventUpdate
#     print(nclicks)

#     return [None, str(nclicks)]


# # Output(MapAIO.ids.card_title(ELEM_ID_MAIN), "children"),
