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
    return render_template("login.html")

app = Dash(
    server=server,
    #use_pages=True,
    use_pages=False,
    title=default_settings.TITLE,
    external_scripts=default_settings.EXTERNAL_SCRIPTS,
    external_stylesheets=default_settings.EXTERNAL_STYLESHEETS,
    suppress_callback_exceptions=True,
)

# configure the Dash instance's layout
#app.layout = main_default_layout()


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

with server.app_context():
    from . import index
    app.layout = main_default_layout

