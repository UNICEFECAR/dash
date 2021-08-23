import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import (
    education,
    child_protection,
    child_health,
    child_poverty,
    child_rights,
    child_participation,
    home,
    about,
    contact,
)
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", home.get_layout),
    ("about", about.get_layout),
    ("contact", contact.get_layout),
    ("education", education.get_layout),
    ("child-protection", child_protection.get_layout),
    ("child-health", child_health.get_layout),
    ("child-poverty", child_poverty.get_layout),
    ("child-rights", child_rights.get_layout),
    ("child-participation", child_participation.get_layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items = (
    ("", html.Div([fa("fas fa-home"), "Home"])),
    ("education", html.Div([fa("fas fa-book"), "Education"])),
    (
        "child-protection",
        html.Div(
            [
                fa("fas fa-child"),
                "Family environment and protection",
            ]
        ),
    ),
    ("child-health", html.Div([fa("fas fa-heartbeat"), "Health and Nutrition"])),
    (
        "child-poverty",
        html.Div([fa("fas fa-hand-holding-usd"), "Poverty"]),
    ),
    ("child-rights", html.Div([fa("fas fa-balance-scale"), "Child Rights"])),
    ("child-participation", html.Div([fa("fas fa-users"), "Participation"])),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items2 = (
    ("", html.Div([fa("fas fa-home"), "Home"]), []),
    ("about", html.Div([fa("fas fa-info-circle"), "About"]), []),
    (
        "sectors",
        "Sectors",
        [
            ("education", html.Div([fa("fas fa-book"), "Education"])),
            (
                "child-protection",
                html.Div([fa("fas fa-child"), "Family environment and protection"]),
            ),
            (
                "child-health",
                html.Div([fa("fas fa-heartbeat"), "Health and Nutrition"]),
            ),
            ("child-poverty", html.Div([fa("fas fa-hand-holding-usd"), "Poverty"])),
            (
                "child-rights",
                html.Div([fa("fas fa-balance-scale"), "Child Rights Landscape"]),
            ),
            ("child-participation", html.Div([fa("fas fa-users"), "Participation"])),
        ],
    ),
    (
        "cross-sectors",
        "Cross-Sectors",
        [
            ("adolescent", html.Div([fa("fas fa-user-friends"), "Adolescent"])),
            ("disability", html.Div([fa("fas fa-blind"), "Disability"])),
            ("gender", html.Div([fa("fas fa-venus-mars"), "Gender"])),
            ("ecd", html.Div([fa("fas fa-baby"), "ECD"])),
        ],
    ),
    ("contact", html.Div([fa("fas fa-address-book"), "Contact"]), []),
)

nav_items_full_names = {
    "education": "Education",
    "child-protection": "Family environment and protection from violence and harmful practices",
    "child-health": "Health and Nutrition",
    "child-poverty": "Poverty and adequate standards of living",
    "child-rights": "Child Rights Landscape",
    "participation": "Participation",
    "": "",
    "": "",
}

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items2)
