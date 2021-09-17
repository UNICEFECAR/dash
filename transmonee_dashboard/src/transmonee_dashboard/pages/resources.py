import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output

from ..app import app
import pandas as pd
from io import StringIO
from . import df_sources, data_sources
import dash_table


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
                        children=[html.H3("Indicators by Data Sources")],
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
    sources_tabs = dcc.Tabs(
        [
            dcc.Tab(
                label=f"{source} (" + str(len(group)) + ")",
                children=[
                    html.Br(),
                    html.Div(
                        className="heading-panel",
                        style={"padding": 20},
                        children=[
                            html.H1(
                                data_sources[source],
                                id="source_title",
                                className="heading-title",
                                style={"fontSize": 24},
                            ),
                        ],
                    ),
                    html.Br(),
                    dash_table.DataTable(
                        columns=[
                            {"name": i, "id": i}
                            for i in [
                                "Sector",
                                "Subtopic",
                                "Indicator",
                                "Source_Full",
                            ]
                        ],
                        data=group.to_dict("records"),
                        style_cell={"textAlign": "center", "fontWeight": "bold"},
                        style_data={
                            "whiteSpace": "normal",
                            "height": "auto",
                            "textAlign": "left",
                            "fontWeight": "regular",
                        },
                        style_data_conditional=[
                            {"if": {"row_index": "odd"}, "backgroundColor": "#c5effc"},
                            {
                                "if": {"state": "active"},
                                "backgroundColor": "#808080",
                                "border": "1px solid #FFFFFF",
                            },
                        ],
                        sort_action="native",
                        sort_mode="multi",
                        column_selectable="single",
                        page_action="native",
                        page_current=0,
                        page_size=20,
                        export_format="xlsx",
                        export_headers="display",
                        hidden_columns=["Source_Full"],
                        export_columns="all",
                        css=[{"selector": ".show-hide", "rule": "display: none"}],
                    ),
                    dbc.Popover(
                        [
                            dbc.PopoverBody(data_sources[source]),
                        ],
                        id="hover",
                        target=f"source-{num}",
                        placement="bottom",
                        trigger="hover",
                    ),
                ],
                style={"fontWeight": "bold"},
                id=f"source-{num}",
            )
            for num, [source, group] in enumerate(df_sources)
        ]
    )
    return sources_tabs
