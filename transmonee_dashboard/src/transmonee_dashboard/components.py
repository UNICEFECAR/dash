import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import current_app as server

from .utils import get_url, component


def fa(className):
    """A convenience component for adding Font Awesome icons"""
    return html.I(className=f"{className} mx-1")


@component
def make_brand(**kwargs):
    return html.Div(
        className="unicef-logo",
        children=[
            html.Div(
                className="unicef-logo__image",
                children=html.Img(
                    src="assets/logo-unicef-large.svg",
                ),
            ),
            html.P(
                className="unicef-logo__heading",
                children=[
                    fa("far fa-chart-bar"),
                    html.Strong(
                        server.config["TITLE"],
                        style={"fontSize": "medium"},
                    ),
                    html.Span(server.config["SUB_TITLE"]),
                ],
            ),
        ],
    )


@component
def make_header(**kwargs):
    return html.Header(
        id="header",
        className="header",
        children=[
            html.Div(
                className="header__top",
                children=[
                    html.Div(
                        className="header__inner",
                        children=[
                            html.Div(
                                className="header__row",
                                children=[
                                    html.Div(
                                        className="header__col header__left",
                                        children=[
                                            html.Div(
                                                className="header__logo",
                                                children=[
                                                    make_brand(),
                                                ],
                                            ),
                                            html.Button(
                                                className="header__burger burger js-mobile-menu",
                                                children=[
                                                    html.Span(
                                                        "Menu",
                                                        className="screen-reader-text",
                                                    ),
                                                    html.Span(
                                                        className="burger__line burger__line--1"
                                                    ),
                                                    html.Span(
                                                        className="burger__line burger__line--2"
                                                    ),
                                                    html.Span(
                                                        className="burger__line burger__line--3"
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    html.Div(
                                        className="header__col header__right",
                                        children=[
                                            html.Div(
                                                className="header__back",
                                                children=[
                                                    html.A(
                                                        "Back to Unicef.org",
                                                        href="https://www.transmonee.org",
                                                        target="_blank",
                                                    )
                                                ],
                                            ),
                                            html.Button(
                                                id="btnInfo",
                                                title="How to use",
                                                className="btn btn-info",
                                                children=[
                                                    fa("fas fa-question"),
                                                ],
                                                style={
                                                    "border-radius": 50,
                                                    "right": 20,
                                                    "top": 80,
                                                    "z-index": 1101,
                                                    "width": 28,
                                                    "height": 28,
                                                    "padding": 4,
                                                    "font-size": 12,
                                                    "border": 0,
                                                },
                                            ),
                                            # html.Div(
                                            #     className="header__cta",
                                            #     children=[
                                            #         html.Div(
                                            #             className="header__search"
                                            #         ),
                                            #         html.A(
                                            #             "First Button",
                                            #             href="#",
                                            #             className="btn btn-outline btn-secondary",
                                            #         ),
                                            #         html.A(
                                            #             "Secound Button",
                                            #             href="#",
                                            #             className="btn btn-outline btn-secondary",
                                            #         ),
                                            #     ],
                                            # ),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    )
                ],
            ),
            html.Div(
                className="header__bottom",
                children=[
                    html.Div(
                        className="header__inner",
                        children=[
                            html.Nav(
                                className="header__navigation",
                                id=server.config["NAVBAR_CONTAINER_ID"],
                            )
                        ],
                    )
                ],
            ),
        ],
        **kwargs,
    )


@component
def make_footer(**kwargs):
    return html.Footer(
        id="footer",
        className="footer",
        children=[
            html.Div(
                className="footer__inner",
                children=[
                    html.Div(
                        className="footer__top",
                        children=[
                            html.Div(
                                className="footer__left",
                                children=[
                                    html.Div(
                                        className="footer__logo",
                                        children=[
                                            make_brand(),
                                        ],
                                    ),
                                ],
                            ),
                            html.Div(
                                className="footer__right",
                                children=[
                                    html.Div(
                                        className="footer__nav",
                                        children=[
                                            html.Ul(
                                                className="footer__menu",
                                                children=[
                                                    html.Li(
                                                        children=[
                                                            html.A(
                                                                "UNICEF Data",
                                                                href="/overview",
                                                            ),
                                                            html.Ul(
                                                                className="sub-menu",
                                                                children=[
                                                                    html.Li(
                                                                        html.A(
                                                                            "Contact Us",
                                                                            href="#",
                                                                        ),
                                                                    ),
                                                                    html.Li(
                                                                        html.A(
                                                                            "Legal",
                                                                            href="#",
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                    html.Div(
                                        className="footer__nav",
                                        children=[
                                            html.Ul(
                                                className="footer__menu",
                                                children=[
                                                    html.Li(
                                                        children=[
                                                            html.A(
                                                                "Support us",
                                                                href="#",
                                                            ),
                                                            html.Ul(
                                                                className="sub-menu",
                                                                children=[
                                                                    html.Li(
                                                                        html.A(
                                                                            "Twitter",
                                                                            href="https://twitter.com/UNICEFData",
                                                                            target="_blank",
                                                                        ),
                                                                    ),
                                                                    html.Li(
                                                                        html.A(
                                                                            "Support UNICEF",
                                                                            href="http://www.supportunicef.org/",
                                                                            target="_blank",
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                    html.Div(
                                        className="footer__nav footer__nav--last",
                                        children=[
                                            html.A(
                                                "Go back to UNICEF.org",
                                                href="https://www.unicef.org/",
                                                target="_blank",
                                            )
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            )
        ],
        **kwargs,
    )


@component
def make_sidebar(**kwargs):
    return html.Nav(
        id=f"sidebar",
        className="nav navbar-dark bg-dark flex-column align-items-start",
        children=[make_brand(), html.Div(id=server.config["NAVBAR_CONTAINER_ID"])],
        **kwargs,
    )
