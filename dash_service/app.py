import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from . import admin, create_dash, create_app
from .extensions import admin, db
from .layouts import main_default_layout, main_layout_header, main_layout_sidebar
from .models import Page
from .views import PageView

sentry_sdk.init(
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


# The Flask instance
server = create_app()

# Flask-Admin
admin.add_view(PageView(Page, db.session))

# The Dash instance
app = create_dash(server)

# configure the Dash instance's layout
app.layout = main_default_layout()
