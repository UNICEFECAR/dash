from dash import html, dcc, Input, Output, State
from urllib.parse import parse_qs, urlparse
from .db_utils import db_utils

from dash_service.pages import empty_renderer, dashboard, data_explorer
from dash_service.pages import (
    child_cross_cutting,
    child_education,
    child_health,
    child_participation,
    child_poverty,
    child_protection,
    child_rights,
    home,
)
from dash.development.base_component import Component
from werkzeug.datastructures import MultiDict
from .exceptions import InvalidLayoutError
from dash.exceptions import PreventUpdate
from dash_service.pages import empty_renderer
from dash_service.pages import data_explorer
from dash_service.pages import dashboard
from flask import request


class CustomRouter:
    """Query string router for DASH multipage apps"""

    def _is_component(layout):
        if isinstance(layout, Component):
            return True
        return False

    tm_layouts = {
        "child-cross-cutting": child_cross_cutting.layout,
        "child-education": child_education.layout,
        "child-health": child_health.layout,
        "child-participation": child_participation.layout,
        "child-poverty": child_poverty.layout,
        "child-protection": child_protection.layout,
        "child-rights": child_rights.layout,
    }

    def __init__(self, app, html_container_id) -> None:
        """
        Initialize the router
        Params:
        app: A Dash instance to associate the router with
        html_container_id: the id of the HTML container where the page qill be injected
        """

        html_container_id

        @app.callback(
            [Output(html_container_id, "children")],
            [Input("dash-location", "pathname"), Input("dash-location", "search")],
            [State("dash-location", "hash")],
        )
        def custom_router_callb(pathname, search, url_hash):
            if pathname is None:
                raise PreventUpdate("Ignoring first Location. pathname callback")

            parsedurl = urlparse(request.base_url)
            parsed_scheme = parsedurl.scheme
            if request.is_secure and parsed_scheme == "http":
                parsed_scheme = "https"

            parsedurl = f"{parsed_scheme}://{parsedurl.netloc}"

            qparams = parse_qs(search.lstrip("?"))

            param_prj = ""
            param_page = ""
            layout_to_use = None
            layout = None
            if "page" in qparams and len(qparams["page"]) > 0:
                param_page = qparams["page"][0]
            if "prj" in qparams and len(qparams["prj"]) > 0:
                param_prj = qparams["prj"][0]

            if param_prj == "tm":
                if param_page == "":
                    layout_to_use = home.layout(parsedurl, request)
                else:
                    layout_to_use = CustomRouter.tm_layouts[param_page]
            else:
                page_type = db_utils().get_page_type(param_prj, param_page)
                if page_type == db_utils.TYPE_DASHBOARD:
                    layout_to_use = dashboard.layout
                elif page_type == db_utils.TYPE_DATAEXPLORER:
                    layout_to_use = data_explorer.layout

            if CustomRouter._is_component(layout_to_use):
                layout = layout_to_use
            elif callable(layout_to_use):
                kwargs = MultiDict(qparams)
                kwargs["hash"] = url_hash
                layout = layout_to_use(**kwargs)

                if not CustomRouter._is_component(layout):
                    msg = (
                        "Layout function must return a Dash Component.\n\n"
                        f"Function {layout_to_use.__name__} from module {layout_to_use.__module__} "
                        f"returned value of type {type(layout)} instead."
                    )
                    raise InvalidLayoutError(msg)

            if layout is None:
                layout = empty_renderer.layout()

            return [layout]
