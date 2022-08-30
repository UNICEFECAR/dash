import sentry_sdk


from sentry_sdk.integrations.flask import FlaskIntegration

from . import create_dash, create_flask, admin
from .layouts import main_default_layout, main_layout_header, main_layout_sidebar

sentry_sdk.init(
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)


# The Flask instance
server = create_flask()

# The Dash instance
app = create_dash(server)

# Flask-Admin

# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    from . import index

    # configure the Dash instance's layout
    app.layout = main_default_layout()
