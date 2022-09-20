from dash import Dash
from flask import Flask


from .__version__ import __version__
from .utils import get_dash_args_from_flask_config
from .extensions import db, admin, cors, migrate


def register_extensions(app):
    """Register Flask extensions."""

    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    cors.init_app(app)
    # bcrypt.init_app(app)
    # cache.init_app(app)
    # csrf_protect.init_app(app)
    # login_manager.init_app(app)
    # debug_toolbar.init_app(app)
    # migrate.init_app(app, db)
    # flask_static_digest.init_app(app)
