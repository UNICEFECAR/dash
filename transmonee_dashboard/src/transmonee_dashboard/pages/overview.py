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
                                        "TransMonEE Database Overview",
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
                        children=[html.H3("About TransMonEE")],
                        className="panel-header",
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.P(
                                        "Transformative Monitoring for Enhanced Equity (TransMonEE) is a research programme that was initiated by the UNICEF Innocenti Research Centre after the fall of the Berlin wall to systematically monitor indicators of child well-being as well as their economic and social determinants in the transition economies. UNICEF was already concerned about the impact of the “Lost Decade” of the 1980s on children, which was characterized by the debt crisis and was followed by structural adjustments in many developing countries. Fretting the additional consequences of the unprecedented social transformation in the transition economies for children, UNICEF started a research programme called “Impact of Transition”, later TransMonEE."
                                    ),
                                    html.P(
                                        "The TransMonEE programme evolved over the years. As the national averages started to bounce back towards their pre-transition periods, the focus has gradually shifted more towards the most disadvantaged children, who are usually invisible in statistics. Therefore, in an attempt to affect the policies and programmes on children. Thus, what was initiated as a programme to monitor transition (Transition Monitoring in Eastern Europe) has become a programme to monitor the situation of children who face inequities in the realization of their rights enshrined in the Convention on the Rights of the Child (Transformative Monitoring for Enhanced Equity)."
                                    ),
                                    html.P(
                                        "The programme was transferred to the UNICEF Regional Office for Central and Eastern Europe and Commonwealth of Independent States (ECA) in 2007 to strengthen those research-policy work linkages. The TransMonEE data represent a particularly useful tool for governments, civil society organizations, donors, and academia in considering their decisions, policies, programmes, and agendas. The database is updated in two ways. Firstly, every year thanks to National Statistical Offices (NSOs) collaboration, country-specific data collection templates are shared with the NSOs, filled in, and submitted by the countries by the end-September with the data for the previous year. Secondly, planned indicators/data are fetch using SDMX data classification structure through open data APIs from several international databases. This work is in progress. Still August 2021, 310 indicators data over years pulled into regional TransMonEE database."
                                    ),
                                ],
                                className="panel-content",
                            ),
                        ],
                        className="panel-body",
                    ),
                    html.Div(
                        # children=[html.H3("About TransMonEE")],
                        className="panel-footer",
                    ),
                ],
                className="panel",
            ),
            html.Br(),
            dbc.Card(
                [
                    dbc.CardHeader(html.H3("Architecture of TransMonEE Database")),
                    dbc.CardBody(
                        [
                            html.Img(
                                src="assets/architecture.png",
                                className="rounded mx-auto d-block",
                            ),
                        ]
                    ),
                ]
            ),
            html.Br(),
            html.Div(
                children=[
                    html.Div(
                        children=[html.H3("Contact Us")],
                        className="panel-header",
                    ),
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    html.P(
                                        [
                                            "UNICEF Europe and Central Asia Regional",
                                            html.Br(),
                                            "Office Planning, Monitoring and Evaluation Section",
                                        ],
                                    ),
                                    html.B("Postal address:"),
                                    html.P(
                                        [
                                            "UNICEF Europe and Central Asia Regional Office",
                                            html.Br(),
                                            "Planning, Monitoring and Evaluation Section",
                                            html.Br(),
                                            "Palais des Nations",
                                            html.Br(),
                                            "CH-1211 Geneva 10",
                                            html.Br(),
                                            "Switzerland",
                                        ],
                                    ),
                                ],
                                className="panel-content",
                            ),
                        ],
                        className="panel-body",
                    ),
                    html.Div(
                        className="panel-footer",
                    ),
                ],
                className="panel",
            ),
            html.Br(),
        ],
    )
