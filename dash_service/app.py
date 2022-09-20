import sentry_sdk
from dash import Dash
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from . import admin, default_settings, register_extensions
from .extensions import admin, db
from .layouts import main_default_layout, main_layout_header, main_layout_sidebar
from .models import Page, Project
from .views import PageView, ProjectView

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

app = Dash(
    server=server,
    use_pages=True,
    title=default_settings.TITLE,
    external_stylesheets=default_settings.EXTERNAL_STYLESHEETS,
    suppress_callback_exceptions=True,
)

# configure the Dash instance's layout
app.layout = main_default_layout()
