import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output
from .base_page import get_base_layout, geo_json_countries
import plotly.express as px


def get_layout(**kwargs):
    return html.Div(
        children=[
            html.Div(
                className="heading",
                style={"padding": 36},
                children=[
                    html.Div(
                        className="heading-content",
                        children=[
                            html.Div(
                                className="heading-panel",
                                style={"padding": 20},
                                children=[
                                    html.H1(
                                        "Adolescent",
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            html.Br(),
            html.Div(
                "Work in Progress - will be available soon",
                className="alert alert-info fade show",
                style={"textAlign": "center", "fontSize": 20},
            ),
            html.Br(),
        ],
    )
