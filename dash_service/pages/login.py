from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/login", order=0, title="Login")

layout = html.Div(
    className="container",
    children=[
        html.Form(
            className="login_form",
            method="post",
            action="do_login",
            children=[
                html.Div(
                    className="form-group",
                    children=[
                        html.Label(htmlFor="email", children="Email"),
                        dbc.Input(
                            id="email",
                            name="enail",
                            placeholder="Email",
                            className="form-control input-lg",
                        ),
                    ],
                ),
                html.Div(
                    className="form-group",
                    children=[
                        html.Label(htmlFor="password", children="Password"),
                        dbc.Input(
                            id="password",
                            name="password",
                            placeholder="password",
                            className="form-control input-lg",
                        ),
                    ],
                ),
                html.Div(
                    className="form-group",
                    children=[
                        dbc.Input(
                            type="submit",
                            id="submit",
                            name="submit",
                            className="btn btn-success btn-lg",
                            value="Login",
                        ),
                    ],
                ),
            ],
        )
    ],
)
