import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app


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
                                        "External Resources",
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
                children=[
                    html.Div(
                        children=[html.H3("Data Availability")],
                        className="panel-header",
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.P(
                                        "This is a dashboard developed using Tableau to reflect the indicators' data availability in UNICEF Data Warehourse. For more info about this dashboard, please click on the button below."
                                    ),
                                ],
                                className="panel-content",
                            ),
                        ],
                        className="panel-body",
                    ),
                    html.Div(
                        children=[
                            html.A(
                                "Click to access the dashboard",
                                href="https://public.tableau.com/app/profile/alina.cherkas/viz/sdmx-dashboard-overview/Dashboard1",
                                target="_blank",
                                className="btn btn-primary",
                            ),
                        ],
                        className="panel-footer",
                    ),
                ],
                className="panel",
            ),
            html.Br(),
            html.Div(
                children=[
                    html.Div(
                        children=[html.H3("SDMX")],
                        className="panel-header",
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.P(
                                        "In this section you have access to the UNICEF Data Warehouse webservice where you can search and export raw data."
                                    ),
                                ],
                                className="panel-content",
                            ),
                        ],
                        className="panel-body",
                    ),
                    html.Div(
                        children=[
                            html.A(
                                "Click to access the SDMX",
                                href="https://sdmx.data.unicef.org/webservice/data.html",
                                target="_blank",
                                className="btn btn-primary",
                            ),
                        ],
                        className="panel-footer",
                    ),
                ],
                className="panel",
            ),
            html.Br(),
        ],
    )
