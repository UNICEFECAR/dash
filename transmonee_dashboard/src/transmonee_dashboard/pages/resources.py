import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app
import pandas as pd
from io import StringIO


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
                                        "This is a dashboard developed using Tableau to reflect the indicators' data availability in UNICEF TransMonEE Data Warehourse. For more info about this dashboard, please click on the button below."
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
                                        [
                                            "In this section you have access to the UNICEF Data Warehouse webservice where you can search and export raw data.",
                                            html.Br(),
                                            "Please make sure to filter the Dataflow dropdown and select 'TRANSMONEE - ECARO for TransMonEE' option.",
                                        ],
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
            html.Div(
                children=[
                    html.Div(
                        children=[html.H3("Data Sources")],
                        className="panel-header",
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=get_data_sources(),
                                className="panel-content",
                            ),
                        ],
                        className="panel-body",
                    ),
                    html.Div(
                        children=[],
                        className="panel-footer",
                    ),
                ],
                className="panel",
            ),
            html.Br(),
        ],
    )


def get_data_sources():
    # path to excel data dictionary in repo
    data_dict_file = "/workspaces/dash/transmonee_dashboard/src/transmonee_dashboard/assets/indicator_dictionary_TM_v8.xlsx"
    # read Snapshot sheet from excel data-dictionary
    snapshot_df = pd.read_excel(data_dict_file, sheet_name="Snapshot")
    snapshot_df["Source"] = snapshot_df["Source_name"].apply(lambda x: x.split(":")[0])
    df_sources = snapshot_df.groupby("Source")
    sources_tabs = dcc.Tabs(
        [
            dcc.Tab(
                label=f"{source} (" + str(len(group)) + ")",
                children=[
                    html.Ul(
                        children=[
                            html.Li(indicator, className="list-group-item")
                            for indicator in group["Name"]
                        ],
                        className="list-group",
                    )
                ],
                style={"fontWeight": "bold"},
            )
            for source, group in df_sources
        ]
    )
    return sources_tabs
