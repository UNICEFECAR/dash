from dash import html, register_page, dcc, callback
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash_service.models import User

# from flask_login import UserMixin, login_user, login_required, logout_user, current_user
import flask_login
from flask import flash

register_page(__name__, path="/login", order=0, title="Login")

layout = html.Div(
    className="row",
    children=[
        # content
        html.Div(
            className="col-sm-12 col-md-6 col-lg-4 mx-auto",
            id="div_login",
            children=[
                html.Div(
                    className="text-center",
                    children=[
                        html.Br(),
                        html.Hr(),
                        html.H3("Log in"),
                        # login form
                        html.Div(
                            children=[
                                html.Div(
                                    className="form-group",
                                    children=[
                                        html.Label(htmlFor="email", children=["Email"]),
                                        dcc.Input(
                                            id="email",
                                            placeholder="Enter email",
                                            className="form-control",
                                            debounce=True,
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="form-group",
                                    children=[
                                        html.Label(
                                            htmlFor="password", children=["Password"]
                                        ),
                                        dcc.Input(
                                            type="password",
                                            id="password",
                                            placeholder="Enter password",
                                            className="form-control",
                                            debounce=True,
                                        ),
                                    ],
                                ),
                                html.Button(
                                    children=["Login"],
                                    type="submit",
                                    id="login_button",
                                    className="btn btn-primary",
                                ),
                                html.Br(),
                                html.Hr(),
                                html.Div(id="dummy_out", style={"display": "none"}),
                            ],
                            id="login_form",
                            hidden=False,
                        ),
                    ],
                )
            ],
        ),
    ],
)


@callback(
    [
        Output("dummy_out", "children"),
        Output("email", "n_submit"),
        Output("password", "n_submit"),
    ],
    [
        Input("login_button", "n_clicks"),
        Input("email", "value"),
        Input("password", "value"),
    ],
    [
        State("email", "n_submit"),
        State("password", "n_submit"),
    ],
    prevent_initial_call=True,
)
def do_login(n_clicks, email, pwd, email_n_sub, pwd_n_sub):
    user = User.query.filter(User.email == email).first()
    enter_clicked = email_n_sub is not None or pwd_n_sub is not None

    if enter_clicked and user and pwd and user.verify_password(pwd):
        flask_login.login_user(user)
        return [dcc.Location(pathname="/admin", id="any_id"), None, None]
    else:
        return [None, None, None]
