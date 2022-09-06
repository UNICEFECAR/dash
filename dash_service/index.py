import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar

from .components import fa


nav_items = (
    ("", html.Div([fa("fas fa-info-circle"), "Education"]), []),
    ("health", html.Div([fa("fas fa-medkit"), "Health"]), []),
    # ("protection", html.Div([fa("fas fa-bullseye"), "Protection"]), []),
)


# router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
