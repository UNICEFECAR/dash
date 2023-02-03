from dash import html, register_page, dcc, callback
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
from dash_service.models import User
#from flask_login import UserMixin, login_user, login_required, logout_user, current_user
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
                        
                        html.Form(
                            children=[
                                html.Div(
                                    className="form-group",
                                    children=[
                                        html.Label(htmlFor="email", children=["Email"]),
                                        dcc.Input(
                                            type="email",
                                            id="email",
                                            placeholder="Enter email",
                                            className="form-control",
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
    Output("dummy_out", "children"),
    [
        Input("login_button", "n_clicks"),
    ],
    [State("email", "value"), State("password", "value")],
    prevent_initial_call=True,
)
def do_login(n_clicks, email, pwd):
    user = User.query.filter(User.email==email, User.password==pwd).first()
    if user:
        flask_login.login_user(user)

    return dcc.Location(pathname="/admin", id="any_id")
