import dash
from dash import callback, dcc, html

from dash_service.models import DataExplorer, Project

# from dash_service.components_aio.card_aio import CardAIO
from dash_service.components_aio.data_explorer.data_explorer_aio import DataExplorerAIO

dash.register_page(
    __name__,
    # path_template="/de/<project_slug>/<page_slug>",
    path_template="/de/<project_slug>/<dataexplorer_slug>",
    # path="/de/rosa/de_rosa",  # this is the default path and working example
)


def layout(project_slug=None, dataexplorer_slug=None, lang="en", **query_parmas):

    # if project_slug is None or page_slug is None:
    #     # project_slug and page_slug are None when this is called for validation
    #     # create a dummy page
    #     return render_page_template({}, "Validation Page", [], "", lang)

    # all_pages = Page.where(project___slug=project_slug).all()
    # if all_pages is None or len(all_pages) == 0:
    #     abort(404, description="No pages found for project")

    # if lang == "en":
    #     all_pages = [{"name": p.title, "path": p.slug} for p in all_pages]
    # else:
    #     all_pages = [
    #         {"name": p.title, "path": p.slug + "?lang=" + lang} for p in all_pages
    #     ]

    print("Slugs")
    print(project_slug)
    print(dataexplorer_slug)

    if project_slug is None or dataexplorer_slug is None:
        # return render_page_template({}, "Validation Page", [], "", lang)
        return html.Div()

    # uses SmartQueryMixin documented here: https://github.com/absent1706/sqlalchemy-mixins#django-like-queries
    # dataexpl = DataExplorer.where(project___slug="rosa", slug="rosa_de").first_or_404()
    dataexpl = DataExplorer.where(
        project___slug=project_slug, slug=dataexplorer_slug
    ).first_or_404()

    print(dataexpl)

    config = dataexpl.content
    t = dataexpl.title

    print(config)

    labels = {DataExplorerAIO._CFG_LASTN: "Show latest data only"}

    de = DataExplorerAIO("data_explorer", cfg=config, labels=labels)

    return html.Div(className="container", children=[de])
