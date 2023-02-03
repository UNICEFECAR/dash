from dash import html, register_page, dcc, callback
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash_service.models import User

# from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import flask_login
from flask import flash

register_page(__name__, path="/logout", order=0, title="Logout")

layout = html.Div(id="div_logout")


@callback(
    Output("div_logout", "children"),
    [
        Input("div_logout", "n_clicks"),
    ]
)
def do_logout(n_clicks):
    print("Do logout")
    # user = User.query.filter(User.email == email, User.password == pwd).first()
    # if user:
    #     flask_login.login_user(user)
    flask_login.logout_user()

    return dcc.Location(pathname="/login", id="any_id")
