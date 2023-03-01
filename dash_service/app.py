import sentry_sdk
from dash import Dash
from flask import Flask, render_template, request, redirect, flash, url_for
from sentry_sdk.integrations.flask import FlaskIntegration

from . import admin, default_settings, register_extensions
from .extensions import admin, db, login_manager
from .layouts import main_default_layout, main_layout_header, main_layout_sidebar
from .models import Page, Project, DataExplorer, User
from .views import PageView, ProjectView, DataExplorerView, UserView

from werkzeug.exceptions import HTTPException, InternalServerError

from flask_admin.menu import MenuLink

import flask_login
from urllib.parse import parse_qs

from dash import html, dcc, Input, Output, State

# from flask_login import UserMixin, login_user, login_required, logout_user, current_user


sentry_sdk.init(
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


server = Flask(__package__)

server.config.from_object(default_settings)

# register extensions
register_extensions(server)

# Flask-Admin
admin.add_view(ProjectView(Project, db.session))
admin.add_view(PageView(Page, db.session))
admin.add_view(DataExplorerView(DataExplorer, db.session))
admin.add_view(UserView(User, db.session))


@server.route("/login")
def page_login():
    req_args = request.args.to_dict(flat=False)
    message = ""
    if "msg" in req_args:
        if "err_cred" in req_args["msg"]:
            message = "Login error"
        elif "err_nocred" in req_args["msg"]:
            message = "Email or password cannot be empty"

    return render_template("login.html", message=message)


@server.route("/do_login", methods=["POST", "GET"])
def do_login():
    form_args = request.form.to_dict(flat=False)
    arg_email = ""
    arg_pwd = ""
    if "email" in form_args:
        arg_email = form_args["email"][0]
    if "pwd" in form_args:
        arg_pwd = form_args["pwd"][0]

    if arg_email.strip() == "" or arg_pwd.strip() == "":
        return redirect("/login?msg=err_nocred")

    user = User.query.filter(User.email == arg_email).first()
    if user.verify_password(arg_pwd):
        flask_login.login_user(user)
        return redirect("/admin")

    return redirect("/login?msg=err_cred")


@server.route("/logout")
def do_logout():
    flask_login.logout_user()

    return redirect("/login")


@server.route("/brazil/<path:page>")
def reroute_brazil(page):
    return redirect(f"/?viz=ds&prj=brazil&page={page}")


@server.route("/rosa/<path:page>")
def reroute_rosa(page):
    return redirect(f"/?viz=ds&prj=rosa&page={page}")


@server.route("/transmonee")
def reroute_transmonee_root():
    return redirect(f"/?viz=tm")


@server.route("/transmonee/<path:page>")
def reroute_transmonee(page):
    return redirect(f"/?viz=tm&page={page}")


app = Dash(
    server=server,
    # use_pages=True,
    use_pages=False,
    title=default_settings.TITLE,
    external_scripts=default_settings.EXTERNAL_SCRIPTS,
    external_stylesheets=default_settings.EXTERNAL_STYLESHEETS,
    suppress_callback_exceptions=True,
)

# configure the Dash instance's layout
# app.layout = main_default_layout()


@server.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


with server.app_context():
    db.create_all()
    # Check if there is at least one user
    first_user = User.query.first()
    # if not add the admin

    if first_user is None:
        first_admin = User(
            name="Deafult admin",
            email="admin@admin.com",
            password="admin",
            is_admin=True,
        )

        db.session.add(first_admin)
        db.session.commit()


class LogoutMenuLink(MenuLink):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


admin.add_link(LogoutMenuLink(name="Logout", category="", url="/logout"))


@server.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type, Authorization, Accept"
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS"
    )
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")

    return response


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


with server.app_context():
    app.layout = html.Div(
        [
            dcc.Store(id="store"),
            dcc.Location(id="dash-location", refresh=False),
            html.Div(id="MAIN_CONTAINER", children=[]),
        ],
        id="mainContainer",
    )


from dash_service.pages import child_health


@app.callback(
    [Output("MAIN_CONTAINER", "children")],
    [Input("dash-location", "pathname"), Input("dash-location", "search")],
    [State("dash-location", "hash")],
)
def display_page(pathname, search, url_hash):

    if pathname is None:
        raise PreventUpdate("Ignoring first Location.pathname callback")

    qparams = parse_qs(search.lstrip("?"))

    tm_layouts = {
        "": home.layout,
        "child-cross-cutting": child_cross_cutting.layout,
        "child-education": child_education.layout,
        "child-health": child_health.layout,
        "child-participation": child_participation.layout,
        "child-poverty": child_poverty.layout,
        "child-protection": child_protection.layout,
        "child-rights": child_rights.layout,
    }

    param_page = ""
    page_to_use = None
    if "page" in qparams:
        param_page = qparams["page"][0]
    if "viz" in qparams:
        param_viz = qparams["viz"][0]
        if param_viz == "de":
            page_to_use = data_explorer.layout
        elif param_viz == "ds":
            page_to_use = dashboard.layout
        elif param_viz == "tm":
            page_to_use = tm_layouts[param_page]
        else:
            page_to_use = empty_renderer.layout

        if isinstance(page_to_use, Component):
            layout = page_to_use
        elif callable(page_to_use):
            kwargs = MultiDict(qparams)
            kwargs["hash"] = url_hash
            layout = page_to_use(**kwargs)
            if not isinstance(layout, Component):
                msg = (
                    "Layout function must return a Dash Component.\n\n"
                    f"Function {page_to_use.__name__} from module {page_to_use.__module__} "
                    f"returned value of type {type(layout)} instead."
                )
                raise InvalidLayoutError(msg)
    return [layout]
