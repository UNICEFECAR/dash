import dash
from dash_bootstrap_components._components.Row import Row
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Br import Br
import dash_table
from dash.dependencies import Input, State, Output
import pandas as pd

from ..app import app
from . import countries_iso3_dict, data, df_topics_subtopics, topics_subtopics


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
                                        "Country Profiles",
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                    html.P(
                                        "Country Name",
                                        id="country_name",
                                        className="heading-subtitle",
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
            html.Br(),
            html.Br(),
            html.Div(
                "Work in Progress - will be available soon",
                className="alert alert-info fade show",
                style={"textAlign": "center", "fontSize": 20},
            ),
            html.Br(),
        ],
    )
