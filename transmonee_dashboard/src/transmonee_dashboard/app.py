import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from flask_caching import Cache

from . import create_flask, create_dash
from .layouts import main_layout_header, main_layout_sidebar, main_default_layout


sentry_sdk.init(
    dsn="https://5f42c982ec844b7ea35b62bef6e117cb@o33646.ingest.sentry.io/5874251",
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

# define a cache instance
cache = Cache(app.server)


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    from . import index

    # configure the Dash instance's layout
    app.layout = main_default_layout()
