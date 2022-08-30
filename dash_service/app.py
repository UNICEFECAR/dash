import sentry_sdk

# from flask_caching import Cache
from flask_admin import Admin
from sentry_sdk.integrations.flask import FlaskIntegration

from . import create_dash, create_flask
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

admin = Admin(app.server, name="Dash Service", template_mode="bootstrap3")

# define a cache instance
# TODO: Move configuration to settings
# TODO: for prod move to redis or similar
# cache = Cache(
#     app.server, config={"CACHE_TYPE": "filesystem", "CACHE_DIR": "cache-directory"}
# )

# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    from . import index

    # configure the Dash instance's layout
    app.layout = main_default_layout()
