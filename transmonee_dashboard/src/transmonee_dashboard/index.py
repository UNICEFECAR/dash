import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import education, page2, page3, character_counter
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", education.get_layout),
    ("character-counter", character_counter.get_layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items = (
    ("character-counter", html.Div([fa("fas fa-book"), "Education"])),
)

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
