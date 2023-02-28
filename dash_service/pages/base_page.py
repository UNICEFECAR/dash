import dash
from dash import html, dcc


dash.register_page(
    __name__,
    title="Base page",
    # path_template="/<project_slug>/<page_slug>",
    path="/base",
    #redirect_from="/"
    # path="/brazil/child-education",  # this is the default path and working example
)

layout = html.Div(
    children=[
        html.H1(children="This is our Home page"),
        html.Div(
            children="""
        This is our Home page content.
    """
        ),
    ]
)
