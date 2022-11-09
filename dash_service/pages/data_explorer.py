import dash
from dash import callback, dcc, html

from dash_service.models import DataExplorer, Project
from dash.dependencies import MATCH, Input, Output, State, ALL

from dash_service.pages import get_data
from dash_service.pages import (
    add_structure,
    get_structure_id,
    get_code_from_structure_and_dq,
    get_col_name,
    merge_with_codelist,
    get_multilang_value,
    is_string_empty,
)

from dash_service.components_aio.data_explorer.data_explorer_aio import DataExplorerAIO

LABELS = {DataExplorerAIO._CFG_LASTN: "Show latest data only"}

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
    data_structures={}
    add_structure(data_structures, config["data"], lang)


    de = DataExplorerAIO("data_explorer", cfg=config, labels=LABELS)

    # return

    template = html.Div(
        className="container",
        children=[
            dcc.Store(id="lang", data=lang),
            dcc.Store(id="config", data=config),
            dcc.Store(id="data_structures", data={}, storage_type="session"),
            de,
        ],
    )

    return template


# Triggered when the config loaded from the database is stored in config dcc.store
# @callback(
#     Output("data_structures", "data"),
#     [
#         Input("config", "data"),
#     ],
#     [State("data_structures", "data"), State("lang", "data")],
# )
# # Downloads the DSD for the data.
# def download_structures(config, data_structures, lang):
    
 
#     add_structure(data_structures, config["data"], lang)


#     return data_structures
    


# dcc.Store(id="data_structures", data={}, storage_type="session"),
