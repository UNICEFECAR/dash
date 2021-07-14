import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
<<<<<<< HEAD
from .pages import education, child_protection, home, child_health
=======
from .pages import education, child_protection, home, child_poverty
>>>>>>> 8459ff20f77209da0fc85ba765f47c56a8e6e210
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", home.get_layout),
    ("education", education.get_layout),
    ("child-protection", child_protection.get_layout),
<<<<<<< HEAD
    ("child-health", child_health.get_layout),
=======
    ("child-poverty", child_poverty.get_layout),
>>>>>>> 8459ff20f77209da0fc85ba765f47c56a8e6e210
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items = (
    ("", html.Div([fa("fas fa-home"), "Home"])),
    ("education", html.Div([fa("fas fa-book"), "Education"])),
    ("child-protection", html.Div([fa("fas fa-child"), "Child Protection"])),
<<<<<<< HEAD
    ("child-health", html.Div([fa("fas fa-heartbeat"), "Health and Nutrition"])),
=======
    (
        "child-poverty",
        html.Div(
            [fa("fas fa-hand-holding-usd"), "Poverty and adequate standards of living"]
        ),
    ),
>>>>>>> 8459ff20f77209da0fc85ba765f47c56a8e6e210
)

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
