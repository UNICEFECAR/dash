import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import (
    child_education,
    health,
    home,
)
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    # ("", home.get_layout),
    ("", child_education.get_layout),
    ("health", health.get_layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items_old = (
    ("", html.Div([fa("fas fa-home"), "Home"]), []),
    ("overview", html.Div([fa("fas fa-info-circle"), "Overview"]), []),
    (
        "sectors",
        "Domains",
        [
            ("child-education", html.Div([fa("fas fa-book"), "Education"])),
            # (
            #     "child-protection",
            #     html.Div([fa("fas fa-child"), "Family Environment and Protection"]),
            # ),
            # (
            #     "child-health",
            #     html.Div([fa("fas fa-heartbeat"), "Health and Nutrition"]),
            # ),
            # (
            #     "child-poverty",
            #     html.Div([fa("fas fa-hand-holding-usd"), "Poverty"]),
            # ),
            # (
            #     "child-rights",
            #     html.Div(
            #         [
            #             fa("fas fa-balance-scale"),
            #             "Child Rights Landscape",
            #         ]
            #     ),
            # ),
            # (
            #     "child-participation",
            #     html.Div([fa("fas fa-users"), "Participation"]),
            # ),
        ],
    ),
    # (
    #     "cross-sectors",
    #     "Cross-Sectoral Issues",
    #     [
    #         ("adolescent", html.Div([fa("fas fa-user-friends"), "Adolescent"])),
    #         ("disability", html.Div([fa("fas fa-blind"), "Disability"])),
    #         ("gender", html.Div([fa("fas fa-venus-mars"), "Gender"])),
    #         ("ecd", html.Div([fa("fas fa-baby"), "ECD"])),
    #         (
    #             "risks",
    #             html.Div([fa("fas fa-exclamation-triangle"), "Risks and Humanitarian"]),
    #         ),
    #         ("climate", html.Div([fa("fas fa-sun"), "Climate Change"])),
    #     ],
    # ),
    # ("profiles", html.Div([fa("fas fa-globe"), "Country Snapshots"]), []),
    # ("data_query", html.Div([fa("fas fa-table"), "Query Data"]), []),
    # ("resources", html.Div([fa("fas fa-database"), "Resources"]), []),
)

nav_items = (
    ("", html.Div([fa("fas fa-info-circle"), "Education"]), []),
    ("health", html.Div([fa("fas fa-medkit"), "Health"]), []),
    # ("protection", html.Div([fa("fas fa-bullseye"), "Protection"]), []),
)


router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
