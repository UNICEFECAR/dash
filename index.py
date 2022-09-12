# %%
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# %%
# Connect to main app.py file
from app import app, server

# %%
# Connect to your app pages
from pages import home

# %%
# display content using urls
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    match pathname:
        case "/apps/home":
            return home.layout
        case _:
            return home.layout

# actual page content
dcc.Loading(
    children=html.Div(
        id="page-content",
        children=[],
        style={
            "paddingTop": "20px",
        },
    ),
    id="loading-page-content",
    type="circle",
    fullscreen=True,
),
