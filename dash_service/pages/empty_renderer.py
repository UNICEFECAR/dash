from dash import callback, dcc, html
import dash_bootstrap_components as dbc
from dash_service.models import Page, DataExplorer
import unicodedata


def layout(project_slug=None, page_slug=None, lang="en", **query_params):
    def strip_accents(s):
        return "".join(
            c
            for c in unicodedata.normalize("NFD", s)
            if unicodedata.category(c) != "Mn"
        )

    all_dashboards = Page.query.all()
    all_dataexplorers = DataExplorer.query.all()

    # all_dashboards = [
    #     {
    #         "title": f"Project: {d.project.name} - Page: {d.title}",
    #         "qparams": f"prj={d.project.slug}&page={d.slug}",
    #     }
    #     for d in all_dashboards
    # ]
    # all_dataexplorers = [
    #     {
    #         "title": f"Project: {d.project.name} - Page: {d.title}",
    #         "qparams": f"prj={d.project.slug}&page={d.slug}",
    #     }
    #     for d in all_dataexplorers
    # ]

    all_dashboards.sort(key=lambda x: (x.project.name, strip_accents(x.title)))
    all_dataexplorers.sort(key=lambda x: (x.project.name, strip_accents(x.title)))

    # dashboards = [
    #     html.Div(dcc.Link(children=c["title"], href=c["qparams"]))
    #     for c in all_dashboards
    # ]

    # dataexplorers = [
    #     html.Div(dcc.Link(children=c["title"], href=c["qparams"]))
    #     for c in all_dataexplorers
    # ]

    dashboards_rows = [
        html.Tr(
            children=[
                html.Td(c.project.name),
                html.Td(
                    html.A(
                        href=f"?prj={c.project.slug}&page={c.slug}", children=[c.title]
                    )
                ),
            ]
        )
        for c in all_dashboards
    ]

    dataexplorers_rows = [
        html.Tr(
            children=[
                html.Td(c.project.name),
                html.Td(
                    html.A(
                        href=f"?prj={c.project.slug}&page={c.slug}", children=[c.title]
                    )
                ),
            ]
        )
        for c in all_dataexplorers
    ]

    # ret = html.Div(
    #     dbc.Col(
    #         [
    #             dbc.Row(html.H2("No page found")),
    #             dbc.Row(html.H4("Available Dashboards:")),
    #             html.Div(dashboards),
    #             dbc.Row(html.H4("Available Data explorers:")),
    #             html.Div(dataexplorers),
    #         ]
    #     )
    # )

    ret = html.Div(
        className="table table-striped",
        children=[
            html.H3("Dashboards"),
            html.Thead(
                html.Tr(
                    [
                        html.Th(scope="col", children=["Project"]),
                        html.Th(scope="col", children=["Page"]),
                    ]
                )
            ),
            html.Tbody(dashboards_rows),

            html.H3("Data explorers"),
            html.Thead(
                html.Tr(
                    [
                        html.Th(scope="col", children=["Project"]),
                        html.Th(scope="col", children=["Page"]),
                    ]
                )
            ),
            html.Tbody(dataexplorers_rows),
        ],
    )

    return ret


"""
def render_no_dashboard_cfg_found(all_configs):
    # pages = [f"prj={c.project.slug}&page={c.slug}" for c in all_configs]
    pages = [
        {
            "title": f"Project: {c.project.name} - Page: {c.title}",
            "qparams": f"?viz=ds&prj={c.project.slug}&page={c.slug}",
        }
        for c in all_configs
    ]
    pages.sort(key=lambda x: x["qparams"])

    html_elems = [
        html.Div(dcc.Link(children=c["title"], href=c["qparams"])) for c in pages
    ]

    template = html.Div(
        dbc.Col(
            [
                dbc.Row(html.H2("No dashboard found")),
                dbc.Row(html.H4("Available pages:")),
                # html.Div([html.href(p) for p in pages]),
                html.Div(html_elems),
            ]
        )
    )
    return template
"""
