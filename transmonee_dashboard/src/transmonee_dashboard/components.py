import base64
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


@component
def make_wheel(**kwargs):
    image_filename = "/workspaces/dash/transmonee_dashboard/src/transmonee_dashboard/assets/socr_diagram.svg"
    encoded_image = base64.b64encode(open(image_filename, "rb").read()).decode()
    return html.Div(
        # children=html.Img(src="data:image/svg+xml;base64,{}".format(encoded_image))
        [
            html.Iframe(
                srcDoc="""
                    <?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 26.0.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 1353.81 1308.66" style="enable-background:new 0 0 1353.81 1308.66;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#2C5895;}
	.st1{fill:#4AA4B6;}
	.st2{fill:#961A49;}
	.st3{fill:#00AEEF;}
	.st4{fill:#0078D4;}
	.st5{enable-background:new    ;}
	.st6{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7877;}
	.st7{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9822;}
	.st8{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st9{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0593;}
	.st10{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9811;}
	.st11{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st12{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9927;}
	.st13{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7863;}
	.st14{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9866;}
	.st15{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st16{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9821;}
	.st17{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9708;}
	.st18{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0533;}
	.st19{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3;}
	.st20{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9682;}
	.st21{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8944;}
	.st22{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8571;}
	.st23{fill:none;stroke:#961A49;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9873;}
	.st24{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0207;}
	.st25{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8015;}
	.st26{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9815;}
	.st27{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0287;}
	.st28{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st29{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9741;}
	.st30{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9305;}
	.st31{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st32{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9636;}
	.st33{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st34{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0185;}
	.st35{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9519;}
	.st36{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8747;}
	.st37{fill:none;stroke:#0078D4;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9728;}
	.st38{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9927;}
	.st39{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7863;}
	.st40{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9866;}
	.st41{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st42{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9821;}
	.st43{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9708;}
	.st44{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0533;}
	.st45{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3;}
	.st46{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9682;}
	.st47{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8944;}
	.st48{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8571;}
	.st49{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9873;}
	.st50{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9495;}
	.st51{fill:none;stroke:#2C5895;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9857;}
	.st52{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st53{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9861;}
	.st54{fill:#FFFFFF;}
	.st55{fill:#570D61;}
	.st56{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9808;}
	.st57{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8091;}
	.st58{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.949;}
	.st59{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st60{fill:none;stroke:#000000;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9602;}
	.st61{fill:none;stroke:#000000;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st62{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.142;}
	.st63{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.906;}
	.st64{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9908;}
	.st65{fill:none;stroke:#570D61;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9602;}
	.st66{fill:none;stroke:#570D61;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st67{fill:#F3F8F5;}
	.st68{fill:#0F732E;}
	.st69{fill:#E7F1EA;}
	.st70{fill:none;stroke:#0F732E;stroke-width:2.8347;stroke-miterlimit:10;}
	.st71{fill:none;stroke:#00AEEF;}
	.st72{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0557;}
	.st73{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9738;}
	.st74{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9748;}
</style>
<g>
      <a href="https://tm-dash-dev.azurewebsites.net/child-health#nutrition" target="_self">
        <path class="st0"
          d="M633.88,480.31c7.66-1.51,15.46-2.62,23.38-3.33c6.89-0.61,12.13-6.46,12.13-13.38v-49.51c0-7.72-6.54-13.88-14.25-13.32c-13.85,1.02-27.44,2.98-40.71,5.81c-7.56,1.61-12.1,9.37-9.93,16.79L618.48,471C620.44,477.61,627.11,481.64,633.88,480.31L633.88,480.31z" />
      </a>
      <a href="https://tm-dash-dev.azurewebsites.net/child-health#immunization" target="_self">
        <path class="st0"
          d="M573.57,501.52c6.97-3.65,14.16-6.94,21.54-9.85c6.39-2.52,9.74-9.56,7.81-16.15l-13.98-47.6c-2.18-7.42-10.2-11.48-17.43-8.76c-12.92,4.86-25.41,10.59-37.41,17.11c-6.78,3.68-8.95,12.4-4.78,18.9l26.84,41.76C559.9,502.74,567.45,504.72,573.57,501.52L573.57,501.52z" />
      </a>
      <a href="https://tm-dash-dev.azurewebsites.net/child-protection#violence" target="_self">
        <path class="st1" d="M458.88,648.9c1.83-7.73,4.05-15.3,6.65-22.69c2.29-6.52-0.74-13.7-7.02-16.57L413.32,589
		c-7.02-3.21-15.35,0.18-18.03,7.43c-4.72,12.78-8.6,25.96-11.57,39.48c-1.66,7.54,3.51,14.9,11.15,16l49.09,7.06
		C450.78,659.95,457.3,655.61,458.88,648.9L458.88,648.9z" />
      </a>
      <path class="st0" d="M420.09,574.26l45.16,20.63c6.24,2.85,13.67,0.54,17.07-5.42c3.93-6.88,8.21-13.53,12.82-19.93
		c4.04-5.61,3.15-13.36-2.07-17.88l-37.52-32.51c-5.83-5.06-14.77-4.15-19.39,2.04c-8.17,10.97-15.62,22.52-22.26,34.57
		C410.17,562.53,413.05,571.05,420.09,574.26L420.09,574.26z" />
      <a href="https://tm-dash-dev.azurewebsites.net/child-health#adolescents" target="_self">
        <path class="st0" d="M697.74,476.98c7.92,0.71,15.72,1.82,23.38,3.33c6.77,1.33,13.44-2.69,15.39-9.32l13.98-47.63
      c2.18-7.41-2.37-15.18-9.93-16.79c-13.27-2.83-26.86-4.79-40.71-5.81c-7.7-0.57-14.25,5.59-14.25,13.32v49.51
      C685.61,470.52,690.85,476.37,697.74,476.98L697.74,476.98z" />
      </a>
      <path class="st0" d="M766.06,427.91l-13.98,47.6c-1.93,6.59,1.42,13.63,7.81,16.15c7.38,2.91,14.57,6.2,21.54,9.85
		c6.12,3.2,13.67,1.23,17.41-4.59l26.84-41.76c4.17-6.49,2.01-15.21-4.78-18.9c-12-6.52-24.49-12.25-37.41-17.11
		C776.26,416.43,768.23,420.5,766.06,427.91L766.06,427.91z" />
      <path class="st1" d="M452.88,700.68c0-3.98,0.1-7.93,0.31-11.85c0.36-6.85-4.64-12.82-11.43-13.8l-49.15-7.07
		c-7.65-1.1-14.68,4.51-15.21,12.22c-0.46,6.79-0.69,13.64-0.69,20.55s0.23,13.76,0.69,20.55c0.52,7.71,7.55,13.32,15.21,12.22
		l49.16-7.07c6.79-0.98,11.79-6.95,11.43-13.8C452.99,708.68,452.88,704.69,452.88,700.68L452.88,700.68z" />
      <path class="st1" d="M465.56,775.24c-2.6-7.39-4.83-14.96-6.66-22.68c-1.59-6.7-8.1-11.04-14.92-10.06l-49.11,7.06
		c-7.65,1.1-12.81,8.45-11.15,16c2.97,13.52,6.85,26.71,11.57,39.48c2.68,7.24,11,10.63,18.03,7.43l45.22-20.65
		C464.83,788.95,467.86,781.76,465.56,775.24L465.56,775.24z" />
      <a href="https://tm-dash-dev.azurewebsites.net/child-participation#registration" target="_self">
        <path class="st2" d="M902.11,700.68c0,4.01-0.11,7.99-0.32,11.95c-0.36,6.85,4.64,12.82,11.43,13.8l49.16,7.07
		c7.65,1.1,14.68-4.51,15.2-12.22c0.46-6.79,0.69-13.64,0.69-20.55s-0.23-13.76-0.69-20.55c-0.52-7.71-7.55-13.32-15.2-12.22
		l-49.16,7.07c-6.79,0.98-11.79,6.95-11.43,13.8C902.01,692.76,902.11,696.71,902.11,700.68L902.11,700.68z" />
      </a>
      <a href="https://tm-dash-dev.azurewebsites.net/child-poverty#povertydeprivation" target="_self">
        <path class="st3" d="M941.68,589l-45.19,20.64c-6.28,2.87-9.32,10.05-7.03,16.57c2.6,7.39,4.83,14.96,6.65,22.69
		c1.58,6.71,8.1,11.04,14.92,10.06l49.1-7.06c7.64-1.1,12.81-8.45,11.15-16c-2.97-13.53-6.85-26.71-11.57-39.48
		C957.03,589.18,948.7,585.79,941.68,589L941.68,589z" />
      </a>
      <a href="https://tm-dash-dev.azurewebsites.net/child-poverty#socialprotection" target="_self">
        <path class="st3" d="M859.86,569.54c4.61,6.4,8.89,13.05,12.82,19.93c3.4,5.95,10.83,8.26,17.07,5.42l45.17-20.63
		c7.03-3.21,9.92-11.74,6.18-18.51c-6.64-12.05-14.09-23.6-22.26-34.57c-4.61-6.19-13.55-7.1-19.39-2.04l-37.52,32.51
		C856.7,556.18,855.82,563.93,859.86,569.54L859.86,569.54z" />
      </a>
      <path class="st4" d="M657.26,924.38c-7.91-0.7-15.7-1.82-23.36-3.32c-6.77-1.33-13.44,2.69-15.39,9.32L604.5,978.1
		c-2.18,7.42,2.37,15.18,9.93,16.79c13.27,2.83,26.86,4.79,40.71,5.81c7.7,0.56,14.25-5.59,14.25-13.32v-49.62
		C669.39,930.84,664.15,925,657.26,924.38L657.26,924.38z" />
      <path class="st0" d="M521.69,538.91c5.66-5.45,11.61-10.61,17.82-15.45c5.44-4.24,6.77-11.92,3.03-17.73l-26.84-41.76
		c-4.18-6.5-13.02-8.15-19.2-3.49c-10.96,8.27-21.33,17.27-31.05,26.93c-5.48,5.45-5.11,14.43,0.73,19.49l37.51,32.5
		C508.92,543.93,516.72,543.7,521.69,538.91L521.69,538.91z" />
      <path class="st2" d="M896.09,752.56c-1.83,7.72-4.05,15.29-6.66,22.68c-2.29,6.52,0.74,13.71,7.02,16.58l45.22,20.65
		c7.03,3.21,15.35-0.18,18.03-7.43c4.72-12.77,8.6-25.96,11.57-39.48c1.66-7.54-3.51-14.9-11.15-16L911,742.5
		C904.19,741.52,897.67,745.85,896.09,752.56L896.09,752.56z" />
      <path class="st0" d="M815.49,523.46c6.21,4.84,12.15,10,17.81,15.45c4.97,4.79,12.77,5.01,17.99,0.49l37.52-32.51
		c5.84-5.06,6.21-14.04,0.73-19.49c-9.72-9.66-20.09-18.66-31.05-26.93c-6.17-4.66-15.02-3.02-19.2,3.49l-26.84,41.76
		C808.73,511.54,810.05,519.22,815.49,523.46L815.49,523.46z" />
      <path class="st1" d="M539.55,877.94c-6.2-4.84-12.15-9.99-17.8-15.43c-4.98-4.79-12.77-5.01-17.99-0.49l-37.57,32.55
		c-5.84,5.06-6.21,14.04-0.73,19.49c9.72,9.66,20.09,18.66,31.05,26.93c6.17,4.66,15.02,3.02,19.2-3.49l26.88-41.83
		C546.32,889.86,544.99,882.18,539.55,877.94L539.55,877.94z" />
      <path class="st1" d="M495.18,831.89c-4.61-6.4-8.89-13.04-12.82-19.92c-3.4-5.95-10.83-8.26-17.06-5.41l-45.21,20.65
		c-7.03,3.21-9.92,11.73-6.18,18.51c6.64,12.05,14.09,23.6,22.26,34.57c4.61,6.19,13.55,7.1,19.39,2.04l37.57-32.55
		C498.34,845.25,499.22,837.49,495.18,831.89L495.18,831.89z" />
      <path class="st2" d="M833.26,862.5c-5.66,5.45-11.6,10.6-17.8,15.43c-5.44,4.24-6.77,11.92-3.04,17.73l26.88,41.83
		c4.18,6.5,13.02,8.14,19.2,3.49c10.96-8.27,21.33-17.27,31.05-26.93c5.48-5.45,5.11-14.43-0.73-19.49L851.25,862
		C846.02,857.49,838.23,857.71,833.26,862.5L833.26,862.5z" />
      <path class="st4" d="M588.94,973.55l14.01-47.7c1.93-6.59-1.42-13.63-7.8-16.14c-7.37-2.91-14.56-6.2-21.52-9.84
		c-6.12-3.2-13.67-1.22-17.41,4.59l-26.89,41.84c-4.17,6.49-2.01,15.21,4.78,18.9c12,6.52,24.49,12.25,37.41,17.11
		C578.74,985.03,586.77,980.97,588.94,973.55L588.94,973.55z" />
      <path class="st4" d="M721.09,921.06c-7.65,1.5-15.45,2.62-23.35,3.32c-6.89,0.61-12.13,6.46-12.13,13.38v49.62
		c0,7.73,6.54,13.88,14.25,13.32c13.85-1.02,27.44-2.98,40.71-5.81c7.56-1.61,12.1-9.37,9.93-16.79l-14.01-47.72
		C734.53,923.76,727.86,919.73,721.09,921.06L721.09,921.06z" />
      <path class="st2" d="M934.91,827.2l-45.21-20.65c-6.23-2.85-13.66-0.54-17.06,5.41c-3.93,6.88-8.21,13.52-12.82,19.92
		c-4.04,5.61-3.16,13.36,2.07,17.89l37.57,32.55c5.84,5.06,14.77,4.15,19.39-2.04c8.17-10.97,15.62-22.52,22.26-34.57
		C944.83,838.94,941.95,830.42,934.91,827.2L934.91,827.2z" />
      <path class="st4" d="M781.38,899.87c-6.97,3.64-14.15,6.93-21.52,9.84c-6.39,2.52-9.74,9.56-7.8,16.14l14.01,47.7
		c2.18,7.42,10.2,11.48,17.43,8.76c12.92-4.86,25.41-10.59,37.41-17.11c6.78-3.69,8.95-12.4,4.78-18.9l-26.89-41.84
		C795.05,898.65,787.5,896.67,781.38,899.87L781.38,899.87z" />
      <g class="st5">
        <path class="st0" d="M949.98,360.73h2.11l4.23,13h-1.86l-0.94-3.1h-5.02l-0.97,3.1h-1.67L949.98,360.73z M950.99,362.26h-0.04
			l-2.03,6.93h4.16L950.99,362.26z" />
        <path class="st0" d="M962.69,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M960.98,365.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C962.69,367.6,962.62,365.66,960.98,365.66z" />
        <path class="st0" d="M966.63,369.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			S966.63,373.33,966.63,369.32z M971.99,368.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01S971.99,371.64,971.99,368.69z" />
        <path class="st0" d="M977.32,373.73h-1.48v-13h1.48V373.73z" />
        <path class="st0" d="M981.32,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H981.32z M984.86,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H984.86z" />
        <path class="st0" d="M991.56,373.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C994.73,373.13,993.36,373.91,991.56,373.91z" />
        <path class="st0" d="M1001.62,367.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1001.62z" />
        <path class="st0" d="M1007.31,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1007.31z M1010.85,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1010.85z" />
        <path class="st0" d="M1019.8,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1019.8z" />
        <path class="st0"
          d="M1024.03,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1024.03z" />
        <path class="st0" d="M1034.47,365.71h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.5-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V365.71z M1037.98,369.03c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1037.76,372.7,1037.98,371.46,1037.98,369.03z" />
        <path class="st0" d="M1046.8,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1046.8z" />
        <path class="st0"
          d="M1053.6,372.03h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1053.6,372.03z" />
        <path class="st0" d="M1061.54,373.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57H1063c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1064.71,373.13,1063.34,373.91,1061.54,373.91z" />
        <path class="st0" d="M1066.72,360.73h1.66v1.58h-1.66V360.73z M1068.29,373.73h-1.48v-9.09h1.48V373.73z" />
        <path class="st0" d="M1075.6,367.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1075.6z" />
        <path class="st0" d="M1084.53,372.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.41z M1081.2,371.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1083.09,369.23,1081.2,369.1,1081.2,371.03z" />
        <path class="st0" d="M1090.29,373.73h-1.48v-13h1.48V373.73z" />
        <path class="st0" d="M1093.09,371.85h1.85l-1.64,4.16h-1.15L1093.09,371.85z" />
        <path class="st0" d="M1105.3,373.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1105.3z" />
        <path class="st0" d="M1115.27,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1115.27z M1118.82,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1118.82z" />
        <path class="st0" d="M1127.76,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1127.76z" />
        <path class="st0"
          d="M1131.99,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1131.99z" />
        <path class="st0" d="M1141.51,372.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.41z M1138.18,371.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1140.07,369.23,1138.18,369.1,1138.18,371.03z" />
        <path class="st0" d="M1147.27,373.73h-1.48v-13h1.48V373.73z" />
        <path class="st0" d="M1158.51,372.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.41z M1155.17,371.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1157.07,369.23,1155.17,369.1,1155.17,371.03z" />
        <path class="st0" d="M1167.76,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1167.76z" />
        <path class="st0" d="M1176.63,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M1174.92,365.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1176.63,367.6,1176.56,365.66,1174.92,365.66z" />
        <path class="st0" d="M1186.35,366h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366z" />
        <path class="st0" d="M1192.25,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1192.25z M1195.8,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1195.8z" />
        <path class="st0" d="M1201.42,365.71h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V365.71z M1204.93,369.03c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1204.71,372.7,1204.93,371.46,1204.93,369.03z" />
        <path class="st0" d="M1210.35,366h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366z" />
        <path class="st0" d="M1214.56,369.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1216.09,373.91,1214.56,373.33,1214.56,369.32z M1219.92,368.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1219.54,372.7,1219.92,371.64,1219.92,368.69z" />
        <path class="st0" d="M1228.62,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M1226.91,365.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1228.62,367.6,1228.54,365.66,1226.91,365.66z" />
        <path class="st0" d="M1237.67,364.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V364.63z" />
        <path class="st0" d="M1246.56,367.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1246.56z" />
        <path class="st0"
          d="M1250.97,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1250.97z" />
        <path class="st0" d="M1255.69,360.73h1.66v1.58h-1.66V360.73z M1257.25,373.73h-1.48v-9.09h1.48V373.73z" />
        <path class="st0" d="M1258.76,364.63h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1258.76,364.63z" />
        <path class="st0" d="M1269.24,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1269.24z M1272.79,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1272.79z" />
        <path class="st0" d="M1285.73,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1285.73z" />
        <path class="st0" d="M1291.24,369.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1291.24z M1294.78,368.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1294.78z" />
        <path class="st0" d="M1303.48,372.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.41z M1300.15,371.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1302.04,369.23,1300.15,369.1,1300.15,371.03z" />
        <path class="st0" d="M1309.24,373.73h-1.48v-13h1.48V373.73z" />
        <path class="st0"
          d="M1311.95,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1311.95z" />
        <path class="st0" d="M1321.73,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1321.73z" />
      </g>
      <g class="st5">
        <path class="st0"
          d="M40.96,360.73v13h-2.27l-5.13-11.27h-0.04v11.27h-1.48v-13h2.34l5.06,11.13h0.04v-11.13H40.96z" />
        <path class="st0" d="M48.66,364.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V364.63z" />
        <path class="st0"
          d="M52.96,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H52.96z" />
        <path class="st0" d="M59.34,366h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366z" />
        <path class="st0" d="M63.67,360.73h1.66v1.58h-1.66V360.73z M65.24,373.73h-1.48v-9.09h1.48V373.73z" />
        <path class="st0"
          d="M67.96,364.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H67.96z" />
        <path class="st0" d="M72.67,360.73h1.66v1.58h-1.66V360.73z M74.24,373.73h-1.48v-9.09h1.48V373.73z" />
        <path class="st0" d="M76.54,369.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C78.07,373.91,76.54,373.33,76.54,369.32z M81.91,368.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C81.53,372.7,81.91,371.64,81.91,368.69z" />
        <path class="st0" d="M90.73,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38H85.8v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H90.73z" />
      </g>
      <g class="st5">
        <path class="st0" d="M1258.04,440.73v-13h1.66v5.62h4.56v-5.62h1.66v13h-1.66v-5.94h-4.56v5.94H1258.04z" />
        <path class="st0" d="M1270.81,440.73h-1.66v-13h1.66V440.73z" />
        <path class="st0" d="M1278.46,440.73h-1.98l-3.76-13h1.8l2.97,11.43h0.04l3.04-11.43h1.69L1278.46,440.73z" />
        <path class="st0" d="M1283.26,442.46h-1.21l4.23-14.73h1.21L1283.26,442.46z" />
        <path class="st0" d="M1291.88,427.73h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L1291.88,427.73z M1292.89,429.26h-0.04
			l-2.03,6.93h4.16L1292.89,429.26z" />
        <path class="st0" d="M1301.82,440.73h-1.66v-13h1.66V440.73z" />
        <path class="st0" d="M1304.99,427.73h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24
			c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V427.73z M1306.64,439.29h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6
			h-2.18V439.29z" />
        <path class="st0" d="M1317.23,436.86v0.38c0,1.76,1.12,2.32,2.18,2.32c1.31,0,2.32-0.56,2.32-2.11c0-2.88-5.83-2.56-5.83-6.46
			c0-2.3,1.64-3.53,3.82-3.53c2.38,0,3.71,1.15,3.6,3.8h-1.73c0.02-1.42-0.43-2.36-2-2.36c-0.99,0-2,0.5-2,1.91
			c0,2.86,5.83,2.45,5.83,6.57c0,2.74-1.89,3.62-4.03,3.62c-3.83,0.04-3.83-2.9-3.8-4.14H1317.23z" />
      </g>
      <g class="st5">
        <path class="st0" d="M33.83,440.73h-1.66v-13h1.66V440.73z" />
        <path class="st0" d="M41.27,440.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91H45.8v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H41.27z" />
        <path class="st0" d="M54.26,440.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91H58.8v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H54.26z" />
        <path class="st0" d="M67.65,431.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H67.6c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V431.64z" />
        <path class="st0" d="M76.73,440.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H76.73z" />
        <path class="st0" d="M80.67,427.73h1.66v1.58h-1.66V427.73z M82.23,440.73h-1.48v-9.09h1.48V440.73z" />
        <path class="st0" d="M89.74,432.99l-4.02,6.54h4.14v1.21h-5.74v-1.39l3.96-6.46v-0.04h-3.76v-1.21h5.42V432.99z" />
        <path class="st0" d="M96.47,439.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V439.42z M93.14,438.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C95.03,436.23,93.14,436.11,93.14,438.03z" />
        <path class="st0"
          d="M100.95,431.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H100.95z" />
        <path class="st0" d="M105.67,427.73h1.66v1.58h-1.66V427.73z M107.23,440.73h-1.48v-9.09h1.48V440.73z" />
        <path class="st0" d="M109.54,436.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C111.07,440.91,109.54,440.34,109.54,436.32z M114.9,435.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C114.52,439.71,114.9,438.65,114.9,435.69z" />
        <path class="st0" d="M123.72,440.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H123.72z" />
      </g>
      <g class="st5">
        <path class="st0" d="M1110.44,494.73h1.77l2.45,11.27h0.04l2.61-11.27h2.14l2.36,11.27h0.04l2.65-11.27h1.73l-3.44,13h-2.02
			l-2.47-11.27h-0.04l-2.63,11.27h-2.02L1110.44,494.73z" />
      </g>
      <g class="st5">
        <path class="st0" d="M1131.77,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M1128.44,505.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1130.33,503.23,1128.44,503.11,1128.44,505.03z" />
        <path class="st0"
          d="M1136.26,498.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1136.26z" />
        <path class="st0" d="M1142.54,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1142.54z M1146.08,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1146.08z" />
        <path class="st0" d="M1151.63,500.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.01z" />
      </g>
      <g class="st5">
        <path class="st0" d="M1155.09,505.86h1.85l-1.64,4.16h-1.15L1155.09,505.86z" />
        <path class="st0" d="M1165.51,507.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1168.68,507.14,1167.31,507.91,1165.51,507.91z" />
        <path class="st0" d="M1175.5,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M1172.17,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C1174.06,503.23,1172.17,503.11,1172.17,505.03z" />
        <path class="st0" d="M1184.75,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1184.75z" />
        <path class="st0" d="M1188.69,494.73h1.66v1.58h-1.66V494.73z M1190.26,507.73h-1.48v-9.09h1.48V507.73z" />
        <path class="st0"
          d="M1192.98,498.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1192.98z" />
        <path class="st0" d="M1202.5,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M1199.17,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C1201.06,503.23,1199.17,503.11,1199.17,505.03z" />
        <path class="st0"
          d="M1206.98,498.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1206.98z" />
        <path class="st0" d="M1211.7,494.73h1.66v1.58h-1.66V494.73z M1213.26,507.73h-1.48v-9.09h1.48V507.73z" />
        <path class="st0" d="M1215.57,503.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1217.1,507.91,1215.57,507.34,1215.57,503.32z M1220.93,502.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1220.55,506.71,1220.93,505.65,1220.93,502.69z" />
        <path class="st0" d="M1229.75,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1229.75z" />
        <path class="st0" d="M1242.5,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M1239.16,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C1241.05,503.23,1239.16,503.11,1239.16,505.03z" />
        <path class="st0" d="M1251.75,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1251.75z" />
        <path class="st0" d="M1260.62,494.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V494.73z M1258.91,499.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1260.62,501.61,1260.55,499.67,1258.91,499.67z" />
        <path class="st0" d="M1273.74,507.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.86,1.19-1.86,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1273.74z" />
        <path class="st0"
          d="M1280.55,506.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1280.55,506.04z" />
        <path class="st0" d="M1290.61,498.64h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V498.64z M1288.88,499.69c-1.68,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1290.64,501.79,1290.73,499.69,1288.88,499.69z" />
        <path class="st0" d="M1294.68,494.73h1.66v1.58h-1.66V494.73z M1296.24,507.73h-1.48v-9.09h1.48V507.73z" />
        <path class="st0" d="M1300.24,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1300.24z M1303.78,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1303.78z" />
        <path class="st0" d="M1312.73,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1312.73z" />
        <path class="st0" d="M1318.24,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1318.24z M1321.78,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1321.78z" />
      </g>
      <g class="st5">
        <path class="st0" d="M33.52,507.73h-1.55v-13h2.68l3.28,10.91h0.04l3.31-10.91h2.74v13h-1.66v-11.56h-0.04l-3.64,11.56h-1.57
			l-3.56-11.56h-0.04V507.73z" />
        <path class="st0" d="M51.47,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M48.14,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C50.03,503.23,48.14,503.11,48.14,505.03z" />
        <path class="st0"
          d="M55.95,498.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H55.95z" />
        <path class="st0" d="M62.23,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H62.23z M65.78,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H65.78z" />
        <path class="st0" d="M71.32,500.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.01z" />
        <path class="st0" d="M80.72,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H80.72z" />
        <path class="st0" d="M89.47,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M86.14,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C88.03,503.23,86.14,503.11,86.14,505.03z" />
        <path class="st0" d="M95.23,507.73h-1.48v-13h1.48V507.73z" />
        <path class="st0" d="M98.04,505.86h1.85l-1.64,4.16H97.1L98.04,505.86z" />
        <path class="st0" d="M110.71,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H110.71z" />
        <path class="st0" d="M116.22,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H116.22z M119.76,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H119.76z" />
        <path class="st0" d="M122.64,498.64h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98
			l-1.94-7.74h-0.04l-2.03,7.74h-1.98L122.64,498.64z" />
        <path class="st0" d="M138.37,507.73h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88
			c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V507.73z M140.03,506.71c1.85,0,1.85-1.98,1.85-3.35
			c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C138.37,504.21,138.21,506.71,140.03,506.71z" />
        <path class="st0" d="M145.52,503.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C147.05,507.91,145.52,507.34,145.52,503.32z M150.88,502.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C150.51,506.71,150.88,505.65,150.88,502.69z" />
        <path class="st0" d="M156.3,500.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.01z" />
        <path class="st0" d="M165.7,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H165.7z" />
        <path class="st0" d="M178.44,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M175.11,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C177,503.23,175.11,503.11,175.11,505.03z" />
        <path class="st0" d="M187.69,507.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H187.69z" />
        <path class="st0" d="M196.57,494.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V494.73z M194.86,499.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C196.57,501.61,196.5,499.67,194.86,499.67z" />
        <path class="st0" d="M209.51,501.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H209.51z" />
        <path class="st0" d="M218.69,507.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H218.69z" />
        <path class="st0" d="M222.63,494.73h1.66v1.58h-1.66V494.73z M224.2,507.73h-1.48v-9.09h1.48V507.73z" />
        <path class="st0" d="M228.19,507.73h-1.48v-13h1.48V507.73z" />
        <path class="st0" d="M235.56,494.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V494.73z M233.84,499.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C235.56,501.61,235.48,499.67,233.84,499.67z" />
        <path class="st0" d="M248.68,507.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H248.68z" />
        <path class="st0" d="M254.18,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H254.18z M257.73,502.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H257.73z" />
        <path class="st0" d="M266.42,506.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.42z M263.09,505.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C264.98,503.23,263.09,503.11,263.09,505.03z" />
        <path class="st0" d="M272.18,507.73h-1.48v-13h1.48V507.73z" />
        <path class="st0"
          d="M274.9,498.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H274.9z" />
        <path class="st0" d="M284.68,507.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.86,1.19-1.86,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H284.68z" />
      </g>
      <a href="https://tm-dash-dev.azurewebsites.net/child-poverty#socialprotection" target="_self">
        <g class="st5">
          <path class="st3" d="M1149.28,570.86v0.38c0,1.76,1.12,2.32,2.18,2.32c1.31,0,2.32-0.56,2.32-2.11c0-2.88-5.83-2.56-5.83-6.46
			c0-2.3,1.64-3.53,3.82-3.53c2.38,0,3.71,1.15,3.6,3.8h-1.73c0.02-1.42-0.43-2.36-2-2.36c-0.99,0-2,0.5-2,1.91
			c0,2.86,5.83,2.45,5.83,6.57c0,2.74-1.89,3.62-4.03,3.62c-3.83,0.04-3.83-2.9-3.8-4.14H1149.28z" />
          <path class="st3" d="M1157.59,570.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1159.12,574.91,1157.59,574.34,1157.59,570.32z M1162.96,569.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1162.58,573.71,1162.96,572.65,1162.96,569.69z" />
          <path class="st3" d="M1171.6,568.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1171.6z" />
          <path class="st3" d="M1175.72,561.73h1.66v1.58h-1.66V561.73z M1177.28,574.73h-1.48v-9.09h1.48V574.73z" />
          <path class="st3" d="M1184.52,573.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.42z M1181.19,572.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1183.08,570.23,1181.19,570.11,1181.19,572.03z" />
          <path class="st3" d="M1190.28,574.73h-1.48v-13h1.48V574.73z" />
          <path class="st3" d="M1198.43,566.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.87,0-1.5-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V566.72z M1201.94,570.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1201.73,573.71,1201.94,572.47,1201.94,570.04z" />
          <path class="st3" d="M1207.36,567.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V567.01z" />
          <path class="st3" d="M1211.57,570.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1213.1,574.91,1211.57,574.34,1211.57,570.32z M1216.94,569.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1216.56,573.71,1216.94,572.65,1216.94,569.69z" />
          <path class="st3"
            d="M1220.99,565.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1220.99z" />
          <path class="st3" d="M1227.27,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1227.27z M1230.82,569.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1230.82z" />
          <path class="st3" d="M1239.58,568.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1239.58z" />
          <path class="st3"
            d="M1243.99,565.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1243.99z" />
          <path class="st3" d="M1248.71,561.73h1.66v1.58h-1.66V561.73z M1250.27,574.73h-1.48v-9.09h1.48V574.73z" />
          <path class="st3" d="M1252.58,570.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1254.11,574.91,1252.58,574.34,1252.58,570.32z M1257.94,569.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1257.56,573.71,1257.94,572.65,1257.94,569.69z" />
          <path class="st3" d="M1266.76,574.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1266.76z" />
          <path class="st3" d="M1277.51,574.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1280.68,574.14,1279.31,574.91,1277.51,574.91z" />
          <path class="st3"
            d="M1285.55,573.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1285.55,573.04z" />
          <path class="st3" d="M1293.49,574.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1296.66,574.14,1295.29,574.91,1293.49,574.91z" />
          <path class="st3"
            d="M1298.96,565.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1298.96z" />
          <path class="st3" d="M1305.24,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1305.24z M1308.79,569.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1308.79z" />
          <path class="st3" d="M1317.27,574.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1317.27z" />
        </g>
      </a>
      <g class="st5">
        <path class="st0" d="M32.07,574.73v-13h1.66v5.62h4.56v-5.62h1.66v13h-1.66v-5.94h-4.56v5.94H32.07z" />
        <path class="st0" d="M44.23,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H44.23z M47.78,569.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H47.78z" />
        <path class="st0" d="M56.48,573.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.42z M53.15,572.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C55.04,570.23,53.15,570.11,53.15,572.03z" />
        <path class="st0" d="M62.23,574.73h-1.48v-13h1.48V574.73z" />
        <path class="st0"
          d="M64.95,565.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H64.95z" />
        <path class="st0" d="M74.73,574.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H74.73z" />
        <path class="st0" d="M85.47,574.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C88.64,574.14,87.27,574.91,85.47,574.91z" />
        <path class="st0"
          d="M93.52,573.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L93.52,573.04z" />
        <path class="st0" d="M101.46,574.91c-1.96,0-3.19-0.86-3.13-2.95H100c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C104.62,574.14,103.26,574.91,101.46,574.91z" />
        <path class="st0"
          d="M106.93,565.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H106.93z" />
        <path class="st0" d="M113.21,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H113.21z M116.76,569.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H116.76z" />
        <path class="st0" d="M125.23,574.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H125.23z" />
      </g>
      <g class="st5">
        <path class="st3" d="M1058.75,632.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H1058.75z" />
        <path class="st3" d="M1067.81,641.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1067.81z" />
        <path class="st3" d="M1071.75,628.73h1.66v1.58h-1.66V628.73z M1073.31,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st3" d="M1077.31,641.73h-1.48v-13h1.48V641.73z" />
        <path class="st3" d="M1084.67,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M1082.96,633.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1084.67,635.61,1084.6,633.67,1082.96,633.67z" />
        <path class="st3" d="M1094.46,633.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.87,0-1.5-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V633.72z M1097.98,637.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1097.76,640.71,1097.98,639.47,1097.98,637.04z" />
        <path class="st3" d="M1101.61,637.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1103.14,641.91,1101.61,641.34,1101.61,637.32z M1106.98,636.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1106.6,640.71,1106.98,639.65,1106.98,636.69z" />
        <path class="st3" d="M1109.82,632.64h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1109.82,632.64z" />
        <path class="st3" d="M1120.29,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1120.29z M1123.84,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1123.84z" />
        <path class="st3" d="M1129.38,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.12-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z" />
        <path class="st3"
          d="M1134.01,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1134.01z" />
        <path class="st3"
          d="M1141.59,640.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1141.59,640.04z" />
        <path class="st3" d="M1155.52,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1152.19,639.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1154.08,637.23,1152.19,637.11,1152.19,639.03z" />
        <path class="st3" d="M1164.77,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1164.77z" />
        <path class="st3" d="M1173.65,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M1171.94,633.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1173.65,635.61,1173.57,633.67,1171.94,633.67z" />
        <path class="st3" d="M1186.3,641.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1186.3z" />
        <path class="st3" d="M1199.51,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1196.18,639.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1198.07,637.23,1196.18,637.11,1196.18,639.03z" />
        <path class="st3"
          d="M1203.99,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1203.99z" />
        <path class="st3" d="M1210.28,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1210.28z M1213.82,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1213.82z" />
        <path class="st3" d="M1219.37,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z" />
        <path class="st3" d="M1223.7,628.73h1.66v1.58h-1.66V628.73z M1225.27,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st3" d="M1232.5,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1229.17,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C1231.06,637.23,1229.17,637.11,1229.17,639.03z" />
        <path class="st3" d="M1238.26,641.73h-1.48v-13h1.48V641.73z" />
        <path class="st3" d="M1249.62,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M1247.91,633.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1249.62,635.61,1249.55,633.67,1247.91,633.67z" />
        <path class="st3" d="M1255.26,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1255.26z M1258.8,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1258.8z" />
        <path class="st3" d="M1264.42,633.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V633.72z M1267.93,637.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1267.71,640.71,1267.93,639.47,1267.93,637.04z" />
        <path class="st3" d="M1273.35,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z" />
        <path class="st3" d="M1277.68,628.73h1.66v1.58h-1.66V628.73z M1279.25,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st3" d="M1280.76,632.64h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1280.76,632.64z" />
        <path class="st3" d="M1294.48,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1291.15,639.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1293.04,637.23,1291.15,637.11,1291.15,639.03z" />
        <path class="st3"
          d="M1298.96,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1298.96z" />
        <path class="st3" d="M1303.67,628.73h1.66v1.58h-1.66V628.73z M1305.24,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st3" d="M1307.54,637.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1309.08,641.91,1307.54,641.34,1307.54,637.32z M1312.91,636.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1312.53,640.71,1312.91,639.65,1312.91,636.69z" />
        <path class="st3" d="M1321.73,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1321.73z" />
      </g>
      <g class="st5">
        <path class="st1" d="M36.48,641.73H34.5l-3.76-13h1.8l2.97,11.43h0.04l3.04-11.43h1.69L36.48,641.73z" />
        <path class="st1" d="M41.68,628.73h1.66v1.58h-1.66V628.73z M43.24,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st1" d="M45.55,637.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C47.08,641.91,45.55,641.34,45.55,637.32z M50.91,636.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C50.54,640.71,50.91,639.65,50.91,636.69z" />
        <path class="st1" d="M56.24,641.73h-1.48v-13h1.48V641.73z" />
        <path class="st1" d="M60.24,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H60.24z M63.78,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H63.78z" />
        <path class="st1" d="M72.73,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38H67.8v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H72.73z" />
        <path class="st1" d="M81.55,635.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H81.55z" />
        <path class="st1" d="M87.24,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H87.24z M90.78,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H90.78z" />
        <path class="st1" d="M103.47,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M100.14,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C102.03,637.23,100.14,637.11,100.14,639.03z" />
        <path class="st1" d="M112.6,632.64h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V632.64z M110.87,633.69c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C112.63,635.79,112.73,633.69,110.87,633.69z" />
        <path class="st1" d="M121.47,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M118.14,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C120.03,637.23,118.14,637.11,118.14,639.03z" />
        <path class="st1" d="M125.67,628.73h1.66v1.58h-1.66V628.73z M127.23,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st1" d="M134.72,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H134.72z" />
        <path class="st1" d="M141.47,641.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C144.64,641.14,143.27,641.91,141.47,641.91z" />
        <path class="st1"
          d="M146.94,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H146.94z" />
        <path class="st1" d="M160.53,635.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H160.53z" />
        <path class="st1" d="M169.71,641.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H169.71z" />
        <path class="st1" d="M173.65,628.73h1.66v1.58h-1.66V628.73z M175.22,641.73h-1.48v-9.09h1.48V641.73z" />
        <path class="st1" d="M179.21,641.73h-1.48v-13h1.48V641.73z" />
        <path class="st1" d="M186.58,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M184.87,633.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C186.58,635.61,186.51,633.67,184.87,633.67z" />
        <path class="st1" d="M192.3,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z" />
        <path class="st1" d="M198.2,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H198.2z M201.75,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H201.75z" />
        <path class="st1" d="M210.7,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H210.7z" />
        <path class="st1" d="M223.44,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M220.11,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C222,637.23,220.11,637.11,220.11,639.03z" />
        <path class="st1" d="M232.69,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H232.69z" />
        <path class="st1" d="M241.57,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M239.86,633.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C241.57,635.61,241.5,633.67,239.86,633.67z" />
        <path class="st1" d="M248.62,632.64h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98
			l-1.94-7.74h-0.04l-2.03,7.74h-1.98L248.62,632.64z" />
        <path class="st1" d="M262.5,637.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C264.03,641.91,262.5,641.34,262.5,637.32z M267.87,636.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C267.49,640.71,267.87,639.65,267.87,636.69z" />
        <path class="st1" d="M276.22,641.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H276.22z" />
        <path class="st1" d="M286.19,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H286.19z M289.73,636.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H289.73z" />
        <path class="st1" d="M298.68,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H298.68z" />
      </g>
      <g class="st5">
        <path class="st2" d="M1116.17,708.73v-13h4.23c1.8,0,2.41,0.61,2.9,1.33c0.45,0.7,0.52,1.48,0.52,1.73c0,1.62-0.56,2.7-2.23,3.08
			v0.09c1.85,0.22,2.67,1.33,2.67,3.11c0,3.33-2.43,3.66-3.91,3.66H1116.17z M1117.82,701.2h2.41c1.3-0.02,1.93-0.81,1.93-2.07
			c0-1.08-0.61-1.96-2-1.96h-2.34V701.2z M1117.82,707.29h2.34c1.77,0,2.39-1.26,2.39-2.21c0-2.07-1.28-2.43-2.97-2.43h-1.76V707.29
			z" />
        <path class="st2" d="M1126.71,695.73h1.66v1.58h-1.66V695.73z M1128.28,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st2" d="M1132.37,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st2"
          d="M1136.99,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1136.99z" />
        <path class="st2" d="M1146.77,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1146.77z" />
        <path class="st2" d="M1156.36,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st2" d="M1162.26,704.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1162.26z M1165.81,703.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1165.81z" />
        <path class="st2" d="M1174.63,699.63h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.76-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.84-4.45c0.96,0,1.71,0.41,2.12,1.3h0.04V699.63z M1172.9,700.68c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1174.67,702.79,1174.76,700.68,1172.9,700.68z" />
        <path class="st2" d="M1178.7,695.73h1.66v1.58h-1.66V695.73z M1180.26,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st2" d="M1185.5,708.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1188.67,708.13,1187.3,708.91,1185.5,708.91z" />
        <path class="st2"
          d="M1190.97,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1190.97z" />
        <path class="st2" d="M1197.35,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st2" d="M1206.49,707.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.41z M1203.16,706.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1205.05,704.23,1203.16,704.1,1203.16,706.03z" />
        <path class="st2"
          d="M1210.97,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1210.97z" />
        <path class="st2" d="M1215.69,695.73h1.66v1.58h-1.66V695.73z M1217.25,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st2" d="M1219.56,704.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			S1219.56,708.33,1219.56,704.32z M1224.92,703.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			S1224.92,706.64,1224.92,703.69z" />
        <path class="st2" d="M1233.74,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1233.74z" />
        <path class="st2" d="M1246.49,707.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.41z M1243.16,706.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1245.05,704.23,1243.16,704.1,1243.16,706.03z" />
        <path class="st2" d="M1255.74,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1255.74z" />
        <path class="st2" d="M1264.61,695.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V695.73z M1262.9,700.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1264.61,702.6,1264.54,700.66,1262.9,700.66z" />
        <path class="st2" d="M1272.67,695.73h1.66v1.58h-1.66V695.73z M1274.24,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st2" d="M1281.6,695.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V695.73z M1279.89,700.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1281.6,702.6,1281.53,700.66,1279.89,700.66z" />
        <path class="st2" d="M1287.24,704.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1287.24z M1290.78,703.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1290.78z" />
        <path class="st2" d="M1299.73,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1299.73z" />
        <path class="st2"
          d="M1303.96,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1303.96z" />
        <path class="st2" d="M1308.67,695.73h1.66v1.58h-1.66V695.73z M1310.24,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st2"
          d="M1312.96,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1312.96z" />
        <path class="st2"
          d="M1320.54,707.03h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1320.54,707.03z" />
      </g>
      <g class="st5">
        <path class="st1" d="M37.68,699.31c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.1-0.11-4.1-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z" />
        <path class="st1" d="M46.74,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z" />
        <path class="st1" d="M50.68,695.73h1.66v1.58h-1.66V695.73z M52.24,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st1" d="M56.24,708.73h-1.48v-13h1.48V708.73z" />
        <path class="st1" d="M63.6,695.73h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V695.73z M61.89,700.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,702.6,63.53,700.66,61.89,700.66z" />
        <path class="st1" d="M69.33,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st1" d="M75.23,704.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H75.23z M78.78,703.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H78.78z" />
        <path class="st1" d="M87.72,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H87.72z" />
        <path class="st1" d="M94.65,699.63h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98l-1.94-7.74
			h-0.04l-2.03,7.74h-1.98L94.65,699.63z" />
        <path class="st1" d="M108.66,695.73h1.66v1.58h-1.66V695.73z M110.22,708.73h-1.48v-9.09h1.48V708.73z" />
        <path class="st1"
          d="M112.94,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H112.94z" />
        <path class="st1" d="M122.71,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H122.71z" />
        <path class="st1" d="M126.53,704.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C128.06,708.91,126.53,708.33,126.53,704.32z M131.89,703.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C131.52,707.7,131.89,706.64,131.89,703.69z" />
        <path class="st1" d="M140.64,699.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V699.63z" />
        <path class="st1"
          d="M144.94,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H144.94z" />
        <path class="st1" d="M155.38,700.71h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V700.71z M158.89,704.03c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C158.68,707.7,158.89,706.46,158.89,704.03z" />
        <path class="st1" d="M167.46,707.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.41z M164.13,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C166.02,704.23,164.13,704.1,164.13,706.03z" />
        <path class="st1" d="M173.31,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st1" d="M179.21,704.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H179.21z M182.76,703.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H182.76z" />
        <path class="st1" d="M191.71,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H191.71z" />
        <path class="st1"
          d="M195.94,699.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H195.94z" />
        <path class="st1" d="M205.46,707.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.41z M202.13,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C204.02,704.23,202.13,704.1,202.13,706.03z" />
        <path class="st1" d="M211.22,708.73h-1.48v-13h1.48V708.73z" />
        <path class="st1" d="M222.52,702.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H222.52z" />
        <path class="st1" d="M231.45,707.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.41z M228.12,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C230.01,704.23,228.12,704.1,228.12,706.03z" />
        <path class="st1" d="M237.3,701h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701z" />
        <path class="st1" d="M243.2,704.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H243.2z M246.75,703.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H246.75z" />
      </g>
      <g class="st5">
        <path class="st2" d="M1200.71,766.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H1200.71z" />
        <path class="st2" d="M1209.76,775.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1209.76z" />
        <path class="st2" d="M1213.7,762.73h1.66v1.58h-1.66V762.73z M1215.27,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st2" d="M1219.26,775.73h-1.48v-13h1.48V775.73z" />
        <path class="st2" d="M1226.63,762.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V762.73z M1224.92,767.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1226.63,769.61,1226.55,767.67,1224.92,767.67z" />
        <path class="st2" d="M1236.42,767.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.87,0-1.5-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V767.72z M1239.93,771.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1239.71,774.71,1239.93,773.47,1239.93,771.04z" />
        <path class="st2" d="M1248.5,774.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V774.42z M1245.17,773.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C1247.06,771.23,1245.17,771.11,1245.17,773.03z" />
        <path class="st2" d="M1254.35,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z" />
        <path class="st2"
          d="M1258.97,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1258.97z" />
        <path class="st2" d="M1263.69,762.73h1.66v1.58h-1.66V762.73z M1265.25,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st2" d="M1272.56,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1272.56z" />
        <path class="st2" d="M1276.68,762.73h1.66v1.58h-1.66V762.73z M1278.25,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st2" d="M1282.41,767.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V767.72z M1285.92,771.04c0-1.37,0-3.37-1.86-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1285.7,774.71,1285.92,773.47,1285.92,771.04z" />
        <path class="st2" d="M1294.49,774.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V774.42z M1291.15,773.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1293.04,771.23,1291.15,771.11,1291.15,773.03z" />
        <path class="st2"
          d="M1298.97,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1298.97z" />
        <path class="st2" d="M1303.68,762.73h1.66v1.58h-1.66V762.73z M1305.25,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st2" d="M1307.55,771.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1309.08,775.91,1307.55,775.34,1307.55,771.32z M1312.92,770.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1312.54,774.71,1312.92,773.65,1312.92,770.69z" />
        <path class="st2" d="M1321.74,775.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1321.74z" />
      </g>
      <g class="st5">
        <path class="st1" d="M32.77,771.7c0.04,1.17-0.11,2.92,1.58,2.92c1.76,0,1.87-1.51,1.87-3.1v-8.79h1.66v9.78
			c0,0.7-0.02,3.49-3.58,3.49c-0.72,0-2.11-0.25-2.74-1.28c-0.52-0.87-0.52-1.98-0.52-3.03H32.77z" />
        <path class="st1" d="M45.66,766.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H45.6c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V766.64z" />
        <path class="st1" d="M52.48,775.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C55.65,775.14,54.28,775.91,52.48,775.91z" />
        <path class="st1"
          d="M57.95,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H57.95z" />
        <path class="st1" d="M62.67,762.73h1.66v1.58h-1.66V762.73z M64.23,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st1" d="M71.54,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H71.54z" />
        <path class="st1" d="M77.23,771.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H77.23z M80.77,770.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H80.77z" />
        <path class="st1" d="M89.05,766.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3
			v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H89.05z" />
        <path class="st1" d="M93.54,771.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C95.07,775.91,93.54,775.34,93.54,771.32z M98.9,770.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C98.52,774.71,98.9,773.65,98.9,770.69z" />
        <path class="st1" d="M104.32,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z" />
        <path class="st1" d="M117.53,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H117.53z" />
        <path class="st1" d="M126.71,775.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H126.71z" />
        <path class="st1" d="M130.65,762.73h1.66v1.58h-1.66V762.73z M132.22,775.73h-1.48v-9.09h1.48V775.73z" />
        <path class="st1" d="M136.21,775.73h-1.48v-13h1.48V775.73z" />
        <path class="st1" d="M143.58,762.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V762.73z M141.87,767.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C143.58,769.61,143.5,767.67,141.87,767.67z" />
        <path class="st1" d="M149.3,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z" />
        <path class="st1" d="M155.2,771.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H155.2z M158.75,770.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H158.75z" />
        <path class="st1" d="M167.7,775.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H167.7z" />
      </g>
      <g class="st5">
        <path class="st2" d="M1137.73,833.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H1137.73z" />
        <path class="st2" d="M1141.72,829.73h1.66v1.58h-1.66V829.73z M1143.29,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st2" d="M1144.8,833.64h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.85,9.09h-1.93L1144.8,833.64z" />
        <path class="st2" d="M1153.71,829.73h1.66v1.58h-1.66V829.73z M1155.28,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st2" d="M1159.28,842.73h-1.48v-13h1.48V842.73z" />
        <path class="st2" d="M1170.51,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M1167.18,840.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1169.07,838.23,1167.18,838.11,1167.18,840.03z" />
        <path class="st2" d="M1179.76,842.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1179.76z" />
        <path class="st2" d="M1188.63,829.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V829.73z M1186.92,834.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1188.63,836.61,1188.56,834.67,1186.92,834.67z" />
        <path class="st2" d="M1198.42,834.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V834.72z M1201.94,838.04c0-1.37,0-3.37-1.86-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1201.72,841.71,1201.94,840.47,1201.94,838.04z" />
        <path class="st2" d="M1205.57,838.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1207.1,842.91,1205.57,842.34,1205.57,838.32z M1210.94,837.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1210.56,841.71,1210.94,840.65,1210.94,837.69z" />
        <path class="st2" d="M1216.26,842.73h-1.48v-13h1.48V842.73z" />
        <path class="st2" d="M1218.69,829.73h1.66v1.58h-1.66V829.73z M1220.26,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st2"
          d="M1222.97,833.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1222.97z" />
        <path class="st2" d="M1227.69,829.73h1.66v1.58h-1.66V829.73z M1229.26,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st2" d="M1236.57,836.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1236.57z" />
        <path class="st2" d="M1245.49,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M1242.16,840.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1244.05,838.23,1242.16,838.11,1242.16,840.03z" />
        <path class="st2" d="M1251.25,842.73h-1.48v-13h1.48V842.73z" />
        <path class="st2" d="M1258.07,833.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06
			c-1.57-0.11-1.84,0.56-1.84,1.3v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1258.07z" />
        <path class="st2" d="M1264.34,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st2" d="M1270.24,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1270.24z M1273.79,837.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1273.79z" />
        <path class="st2" d="M1279.24,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1279.24z M1282.79,837.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1282.79z" />
        <path class="st2" d="M1291.61,829.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V829.73z M1289.9,834.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1291.61,836.61,1291.54,834.67,1289.9,834.67z" />
        <path class="st2" d="M1295.55,838.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1297.08,842.91,1295.55,842.34,1295.55,838.32z M1300.92,837.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1300.54,841.71,1300.92,840.65,1300.92,837.69z" />
        <path class="st2" d="M1309.27,842.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1309.27z" />
        <path class="st2" d="M1320.48,842.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1323.65,842.14,1322.28,842.91,1320.48,842.91z" />
      </g>
      <g class="st5">
        <path class="st1" d="M37.68,833.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.1-0.11-4.1-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z" />
        <path class="st1" d="M46.74,842.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z" />
        <path class="st1" d="M50.68,829.73h1.66v1.58h-1.66V829.73z M52.24,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st1" d="M56.24,842.73h-1.48v-13h1.48V842.73z" />
        <path class="st1" d="M63.6,829.73h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V829.73z M61.89,834.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,836.61,63.53,834.67,61.89,834.67z" />
        <path class="st1" d="M76.26,842.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H76.26z" />
        <path class="st1" d="M89.47,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M86.14,840.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C88.03,838.23,86.14,838.11,86.14,840.03z" />
        <path class="st1" d="M95.32,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st1" d="M101.31,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st1" d="M105.65,829.73h1.66v1.58h-1.66V829.73z M107.22,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st1" d="M114.45,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M111.12,840.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C113.01,838.23,111.12,838.11,111.12,840.03z" />
        <path class="st1" d="M123.58,833.64h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V833.64z M121.85,834.69c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C123.61,836.79,123.7,834.69,121.85,834.69z" />
        <path class="st1" d="M129.21,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H129.21z M132.76,837.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H132.76z" />
        <path class="st1" d="M145.45,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M142.12,840.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C144.01,838.23,142.12,838.11,142.12,840.03z" />
        <path class="st1" d="M154.7,842.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H154.7z" />
        <path class="st1" d="M163.57,829.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V829.73z M161.86,834.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C163.57,836.61,163.5,834.67,161.86,834.67z" />
        <path class="st1" d="M171.51,838.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C173.04,842.91,171.51,842.34,171.51,838.32z M176.88,837.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C176.5,841.71,176.88,840.65,176.88,837.69z" />
        <path class="st1"
          d="M180.92,833.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H180.92z" />
        <path class="st1" d="M190.7,842.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H190.7z" />
        <path class="st1" d="M196.21,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H196.21z M199.75,837.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H199.75z" />
        <path class="st1" d="M205.3,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st1" d="M218.69,842.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H218.69z" />
        <path class="st1" d="M227.44,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M224.11,840.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C226,838.23,224.11,838.11,224.11,840.03z" />
        <path class="st1" d="M233.29,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st1" d="M242.21,842.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H242.21z" />
        <path class="st1" d="M251.02,833.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3
			v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H251.02z" />
        <path class="st1" d="M260.61,833.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V833.64z" />
        <path class="st1" d="M266.19,842.73h-1.48v-13h1.48V842.73z" />
        <path class="st1" d="M274.34,834.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V834.72z M277.85,838.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C277.64,841.71,277.85,840.47,277.85,838.04z" />
        <path class="st1" d="M283.27,835.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.01z" />
        <path class="st1" d="M292.42,841.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.42z M289.08,840.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C290.98,838.23,289.08,838.11,289.08,840.03z" />
        <path class="st1" d="M301.49,836.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H301.49z" />
        <path class="st1"
          d="M305.9,833.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H305.9z" />
        <path class="st1" d="M310.61,829.73h1.66v1.58h-1.66V829.73z M312.18,842.73h-1.48v-9.09h1.48V842.73z" />
        <path class="st1" d="M319.49,836.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H319.49z" />
        <path class="st1" d="M325.18,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H325.18z M328.72,837.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H328.72z" />
        <path class="st1" d="M335.42,842.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C338.59,842.14,337.22,842.91,335.42,842.91z" />
      </g>
      <g class="st5">
        <path class="st2" d="M996.89,909.73h-1.66v-13h1.66V909.73z" />
        <path class="st2" d="M1004.8,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1004.8z" />
        <path class="st2" d="M1009.13,900.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06
			c-1.57-0.11-1.84,0.56-1.84,1.3v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1009.13z" />
        <path class="st2" d="M1013.62,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1015.14,909.91,1013.62,909.34,1013.62,905.32z M1018.98,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1018.6,908.71,1018.98,907.65,1018.98,904.69z" />
        <path class="st2" d="M1024.4,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st2" d="M1033.33,909.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1033.33z" />
        <path class="st2" d="M1046.54,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M1043.21,907.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1045.1,905.23,1043.21,905.11,1043.21,907.03z" />
        <path class="st2"
          d="M1051.02,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1051.02z" />
        <path class="st2" d="M1055.73,896.73h1.66v1.58h-1.66V896.73z M1057.3,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st2" d="M1059.6,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1061.13,909.91,1059.6,909.34,1059.6,905.32z M1064.97,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1064.59,908.71,1064.97,907.65,1064.97,904.69z" />
        <path class="st2" d="M1073.79,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1073.79z" />
        <path class="st2" d="M1078.11,907.86h1.86l-1.64,4.16h-1.15L1078.11,907.86z" />
        <path class="st2" d="M1085.72,896.73h1.66v1.58h-1.66V896.73z M1087.29,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st2" d="M1094.78,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1094.78z" />
        <path class="st2"
          d="M1099.01,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1099.01z" />
        <path class="st2" d="M1105.29,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1105.29z M1108.83,904.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1108.83z" />
        <path class="st2" d="M1114.38,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st2" d="M1123.78,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1123.78z" />
        <path class="st2" d="M1129.28,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1129.28z M1132.83,904.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1132.83z" />
        <path class="st2" d="M1137,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31c0.11,0,0.34-0.04,0.67-0.07
			v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1137z" />
        <path class="st2" d="M1150.52,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M1147.19,907.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1149.08,905.23,1147.19,905.11,1147.19,907.03z" />
        <path class="st2" d="M1159.77,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1159.77z" />
        <path class="st2" d="M1168.65,896.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V896.73z M1166.94,901.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1168.65,903.61,1168.58,901.67,1166.94,901.67z" />
        <path class="st2" d="M1178.44,901.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.72z M1181.95,905.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1181.73,908.71,1181.95,907.47,1181.95,905.04z" />
        <path class="st2" d="M1187.37,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st2" d="M1191.58,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1193.11,909.91,1191.58,909.34,1191.58,905.32z M1196.94,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1196.57,908.71,1196.94,907.65,1196.94,904.69z" />
        <path class="st2"
          d="M1200.99,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1200.99z" />
        <path class="st2" d="M1207.28,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1207.28z M1210.82,904.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1210.82z" />
        <path class="st2" d="M1219.59,903.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1219.59z" />
        <path class="st2" d="M1224,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31c0.11,0,0.34-0.04,0.67-0.07
			v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1224z" />
        <path class="st2" d="M1228.71,896.73h1.66v1.58h-1.66V896.73z M1230.28,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st2" d="M1232.58,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1234.11,909.91,1232.58,909.34,1232.58,905.32z M1237.95,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1237.57,908.71,1237.95,907.65,1237.95,904.69z" />
        <path class="st2" d="M1246.77,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1246.77z" />
        <path class="st2" d="M1254.58,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1256.11,909.91,1254.58,909.34,1254.58,905.32z M1259.94,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1259.57,908.71,1259.94,907.65,1259.94,904.69z" />
        <path class="st2" d="M1264.1,900.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3
			v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1264.1z" />
        <path class="st2" d="M1274.43,901.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.72z M1277.94,905.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1277.73,908.71,1277.94,907.47,1277.94,905.04z" />
        <path class="st2" d="M1283.36,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st2" d="M1287.7,896.73h1.66v1.58h-1.66V896.73z M1289.26,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st2" d="M1290.78,900.64h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1290.78,900.64z" />
        <path class="st2" d="M1304.49,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M1301.16,907.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1303.05,905.23,1301.16,905.11,1301.16,907.03z" />
        <path class="st2" d="M1313.56,903.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1313.56z" />
        <path class="st2"
          d="M1320.55,908.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1320.55,908.04z" />
      </g>
      <g class="st5">
        <path class="st1" d="M37.68,900.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.1-0.11-4.1-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z" />
        <path class="st1" d="M46.74,909.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z" />
        <path class="st1" d="M50.68,896.73h1.66v1.58h-1.66V896.73z M52.24,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st1" d="M56.24,909.73h-1.48v-13h1.48V909.73z" />
        <path class="st1" d="M63.6,896.73h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V896.73z M61.89,901.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,903.61,63.53,901.67,61.89,901.67z" />
        <path class="st1" d="M73.23,909.73h-1.48v-13h1.48V909.73z" />
        <path class="st1" d="M80.47,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M77.14,907.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C79.03,905.23,77.14,905.11,77.14,907.03z" />
        <path class="st1" d="M86.39,909.73h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88
			c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V909.73z M88.05,908.71c1.85,0,1.85-1.98,1.85-3.35
			c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C86.39,906.21,86.23,908.71,88.05,908.71z" />
        <path class="st1" d="M93.54,905.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C95.07,909.91,93.54,909.34,93.54,905.32z M98.9,904.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C98.52,908.71,98.9,907.65,98.9,904.69z" />
        <path class="st1" d="M107.65,900.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V900.64z" />
        <path class="st1" d="M113.32,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st1" d="M126.46,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M123.13,907.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C125.02,905.23,123.13,905.11,123.13,907.03z" />
        <path class="st1" d="M135.71,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H135.71z" />
        <path class="st1" d="M144.58,896.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V896.73z M142.87,901.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C144.58,903.61,144.51,901.67,142.87,901.67z" />
        <path class="st1" d="M152.52,905.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C154.05,909.91,152.52,909.34,152.52,905.32z M157.89,904.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C157.51,908.71,157.89,907.65,157.89,904.69z" />
        <path class="st1"
          d="M161.93,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H161.93z" />
        <path class="st1" d="M171.71,909.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07
			c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H171.71z" />
        <path class="st1" d="M177.22,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H177.22z M180.76,904.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H180.76z" />
        <path class="st1" d="M186.31,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st1" d="M195.04,900.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3
			v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H195.04z" />
        <path class="st1" d="M199.52,905.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C201.05,909.91,199.52,909.34,199.52,905.32z M204.88,904.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C204.51,908.71,204.88,907.65,204.88,904.69z" />
        <path class="st1" d="M210.3,902.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.01z" />
        <path class="st1" d="M219.23,909.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H219.23z" />
        <path class="st1" d="M230.44,909.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C233.61,909.14,232.24,909.91,230.44,909.91z" />
        <path class="st1" d="M239.5,905.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C241.03,909.91,239.5,909.34,239.5,905.32z M244.86,904.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C244.48,908.71,244.86,907.65,244.86,904.69z" />
        <path class="st1" d="M249.02,900.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3
			v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H249.02z" />
        <path class="st1" d="M259.19,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H259.19z M262.73,904.55
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H262.73z" />
        <path class="st1" d="M273.32,909.73h-1.94l-2.11-3.73l-1.96,3.73h-1.75l2.83-4.75l-2.59-4.34h1.89l1.73,3.26l1.84-3.26h1.78
			l-2.72,4.34L273.32,909.73z" />
        <path class="st1" d="M276.34,901.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.72z M279.85,905.04c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C279.64,908.71,279.85,907.47,279.85,905.04z" />
        <path class="st1" d="M285.18,909.73h-1.48v-13h1.48V909.73z" />
        <path class="st1" d="M287.48,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C289.01,909.91,287.48,909.34,287.48,905.32z M292.85,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C292.47,908.71,292.85,907.65,292.85,904.69z" />
        <path class="st1" d="M296.61,896.73h1.66v1.58h-1.66V896.73z M298.18,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st1"
          d="M300.89,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H300.89z" />
        <path class="st1" d="M310.42,908.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.42z M307.08,907.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C308.97,905.23,307.08,905.11,307.08,907.03z" />
        <path class="st1"
          d="M314.9,900.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H314.9z" />
        <path class="st1" d="M319.61,896.73h1.66v1.58h-1.66V896.73z M321.18,909.73h-1.48v-9.09h1.48V909.73z" />
        <path class="st1" d="M323.48,905.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C325.01,909.91,323.48,909.34,323.48,905.32z M328.85,904.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C328.47,908.71,328.85,907.65,328.85,904.69z" />
        <path class="st1" d="M337.67,909.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H337.67z" />
      </g>
      <g class="st5">
        <path class="st4" d="M1187,976.73v-13h1.66v11.56h4.77v1.44H1187z" />
        <path class="st4" d="M1196.27,972.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1196.27z M1199.81,971.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1199.81z" />
        <path class="st4" d="M1203.7,963.73h1.66v1.58h-1.66V963.73z M1205.27,976.73h-1.48v-9.09h1.48V976.73z" />
        <path class="st4" d="M1210.51,976.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1213.67,976.13,1212.31,976.91,1210.51,976.91z" />
        <path class="st4" d="M1220.68,967.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.63z" />
        <path class="st4" d="M1226.34,969h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.12-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V969z" />
        <path class="st4" d="M1232.25,972.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1232.25z M1235.8,971.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1235.8z" />
        <path class="st4" d="M1248.49,975.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V975.41z M1245.15,974.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1247.04,972.23,1245.15,972.1,1245.15,974.03z" />
        <path class="st4" d="M1257.74,976.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1257.74z" />
        <path class="st4" d="M1266.61,963.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V963.73z M1264.9,968.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1266.61,970.6,1266.54,968.66,1264.9,968.66z" />
        <path class="st4" d="M1279.55,970.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.86,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1279.55z" />
        <path class="st4" d="M1288.66,967.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.63z" />
        <path class="st4" d="M1294.24,976.73h-1.48v-13h1.48V976.73z" />
        <path class="st4"
          d="M1296.96,967.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1296.96z" />
        <path class="st4" d="M1306.66,967.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.63z" />
        <path class="st4" d="M1312.33,969h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V969z" />
        <path class="st4" d="M1318.23,972.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1318.23z M1321.78,971.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1321.78z" />
      </g>
      <g class="st5">
        <path class="st4" d="M31.96,976.73v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H31.96z" />
        <path class="st4" d="M45.6,963.73h1.48v13H45.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V963.73z M43.89,968.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C45.6,970.6,45.53,968.66,43.89,968.66z" />
        <path class="st4" d="M54.66,967.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H54.6c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.63z" />
        <path class="st4" d="M63.55,970.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H63.55z" />
        <path class="st4" d="M72.48,975.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V975.41z M69.15,974.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C71.04,972.23,69.15,972.1,69.15,974.03z" />
        <path class="st4"
          d="M76.96,967.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H76.96z" />
        <path class="st4" d="M81.67,963.73h1.66v1.58h-1.66V963.73z M83.24,976.73h-1.48v-9.09h1.48V976.73z" />
        <path class="st4" d="M85.54,972.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C87.07,976.91,85.54,976.33,85.54,972.32z M90.91,971.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C90.53,975.7,90.91,974.64,90.91,971.69z" />
        <path class="st4" d="M99.73,976.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38H94.8v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H99.73z" />
        <path class="st4" d="M110.47,976.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C113.64,976.13,112.28,976.91,110.47,976.91z" />
        <path class="st4"
          d="M118.52,975.03h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L118.52,975.03z" />
        <path class="st4" d="M126.46,976.91c-1.96,0-3.19-0.86-3.13-2.95H125c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C129.63,976.13,128.26,976.91,126.46,976.91z" />
        <path class="st4"
          d="M131.93,967.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H131.93z" />
        <path class="st4" d="M138.21,972.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H138.21z M141.76,971.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H141.76z" />
        <path class="st4" d="M150.24,976.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H150.24z" />
      </g>
      <g class="st5">
        <path class="st4" d="M1140.04,1043.73v-13h1.66v11.56h4.77v1.44H1140.04z" />
        <path class="st4" d="M1149.31,1039.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1149.31z M1152.85,1038.54c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1152.85z" />
        <path class="st4" d="M1161.55,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M1158.22,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1160.11,1039.23,1158.22,1039.1,1158.22,1041.03z" />
        <path class="st4" d="M1167.4,1036h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1036z" />
        <path class="st4" d="M1176.79,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1176.79z" />
        <path class="st4" d="M1180.73,1030.73h1.66v1.58h-1.66V1030.73z M1182.3,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M1189.79,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1189.79z" />
        <path class="st4" d="M1198.66,1034.63h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V1034.63z M1196.94,1035.68c-1.68,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1198.7,1037.79,1198.79,1035.68,1196.94,1035.68z" />
        <path class="st4" d="M1211.66,1034.63h1.48v12.53h-1.48v-4.36h-0.05c-0.5,0.72-1.13,1.1-2,1.1c-2.93,0-3.01-2.61-3.01-4.88
			c0-4,1.48-4.57,2.93-4.57c0.95,0,1.58,0.41,2.09,1.26h0.04V1034.63z M1211.66,1039.57c0-1.39,0.16-3.87-1.66-3.87
			c-1.85,0-1.85,1.96-1.85,3.33c0,2.43,0.22,3.67,1.8,3.67C1211.59,1042.7,1211.66,1040.77,1211.66,1039.57z" />
        <path class="st4" d="M1220.71,1034.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1034.63z" />
        <path class="st4" d="M1229.53,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M1226.2,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1228.09,1039.23,1226.2,1039.1,1226.2,1041.03z" />
        <path class="st4" d="M1235.29,1043.73h-1.48v-13h1.48V1043.73z" />
        <path class="st4" d="M1237.72,1030.73h1.66v1.58h-1.66V1030.73z M1239.29,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4"
          d="M1242.01,1034.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1242.01z" />
        <path class="st4"
          d="M1249.58,1042.03h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1249.58,1042.03z" />
        <path class="st4" d="M1263.52,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M1260.19,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1262.08,1039.23,1260.19,1039.1,1260.19,1041.03z" />
        <path class="st4" d="M1272.77,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1272.77z" />
        <path class="st4" d="M1281.64,1030.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1030.73z M1279.93,1035.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1281.64,1037.6,1281.57,1035.66,1279.93,1035.66z" />
        <path class="st4" d="M1292.51,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1295.68,1043.13,1294.31,1043.91,1292.51,1043.91z" />
        <path class="st4" d="M1299.3,1043.73h-1.48v-13h1.48v7.83h0.04l2.77-3.92h1.8l-3.03,3.91l3.56,5.19h-1.87l-3.24-5.1h-0.04V1043.73
			z" />
        <path class="st4" d="M1305.69,1030.73h1.66v1.58h-1.66V1030.73z M1307.25,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M1311.25,1043.73h-1.48v-13h1.48V1043.73z" />
        <path class="st4" d="M1315.25,1043.73h-1.48v-13h1.48V1043.73z" />
        <path class="st4" d="M1320.48,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1323.65,1043.13,1322.28,1043.91,1320.48,1043.91z" />
      </g>
      <g class="st5">
        <path class="st4" d="M31.96,1043.73v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H31.96z" />
        <path class="st4" d="M45.6,1030.73h1.48v13H45.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1030.73z M43.89,1035.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C45.6,1037.6,45.53,1035.66,43.89,1035.66z" />
        <path class="st4" d="M54.66,1034.63h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H54.6c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1034.63z" />
        <path class="st4" d="M63.55,1037.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H63.55z" />
        <path class="st4" d="M72.48,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M69.15,1041.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C71.04,1039.23,69.15,1039.1,69.15,1041.03z" />
        <path class="st4"
          d="M76.96,1034.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H76.96z" />
        <path class="st4" d="M81.67,1030.73h1.66v1.58h-1.66V1030.73z M83.24,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M85.54,1039.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C87.07,1043.91,85.54,1043.33,85.54,1039.32z M90.91,1038.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C90.53,1042.7,90.91,1041.64,90.91,1038.69z" />
        <path class="st4" d="M99.73,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38H94.8v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H99.73z" />
        <path class="st4" d="M112.47,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M109.14,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C111.03,1039.23,109.14,1039.1,109.14,1041.03z" />
        <path class="st4" d="M121.55,1037.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H121.55z" />
        <path class="st4" d="M130.55,1037.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H130.55z" />
        <path class="st4" d="M136.23,1039.66c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H136.23z M139.78,1038.54
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H139.78z" />
        <path class="st4" d="M146.47,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C149.64,1043.13,148.28,1043.91,146.47,1043.91z" />
        <path class="st4" d="M154.47,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C157.64,1043.13,156.27,1043.91,154.47,1043.91z" />
        <path class="st4" d="M168.45,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M165.12,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C167.01,1039.23,165.12,1039.1,165.12,1041.03z" />
        <path class="st4" d="M177.7,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H177.7z" />
        <path class="st4" d="M186.58,1030.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1030.73z M184.87,1035.66c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C186.58,1037.6,186.51,1035.66,184.87,1035.66z" />
        <path class="st4" d="M196.37,1035.71h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1035.71z M199.88,1039.03c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C199.66,1042.7,199.88,1041.46,199.88,1039.03z" />
        <path class="st4" d="M208.45,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M205.12,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C207.01,1039.23,205.12,1039.1,205.12,1041.03z" />
        <path class="st4" d="M214.3,1036h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1036z" />
        <path class="st4"
          d="M218.92,1034.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H218.92z" />
        <path class="st4" d="M223.64,1030.73h1.66v1.58h-1.66V1030.73z M225.21,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M232.51,1037.55c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H232.51z" />
        <path class="st4" d="M236.63,1030.73h1.66v1.58h-1.66V1030.73z M238.2,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M242.36,1035.71h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1035.71z M245.87,1039.03c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C245.65,1042.7,245.87,1041.46,245.87,1039.03z" />
        <path class="st4" d="M254.44,1042.41h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.41z M251.11,1041.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C253,1039.23,251.11,1039.1,251.11,1041.03z" />
        <path class="st4"
          d="M258.92,1034.63v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H258.92z" />
        <path class="st4" d="M263.63,1030.73h1.66v1.58h-1.66V1030.73z M265.2,1043.73h-1.48v-9.09h1.48V1043.73z" />
        <path class="st4" d="M267.5,1039.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C269.03,1043.91,267.5,1043.33,267.5,1039.32z M272.87,1038.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C272.49,1042.7,272.87,1041.64,272.87,1038.69z" />
        <path class="st4" d="M281.69,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H281.69z" />
      </g>
      <line class="st6" x1="724.09" y1="393.17" x2="724.09" y2="380.62" />
      <line class="st7" x1="727.07" y1="379.23" x2="1322.02" y2="379.23" />
      <path class="st8" d="M724.09,395.96L724.09,395.96 M724.09,379.23L724.09,379.23 M1323.51,379.23L1323.51,379.23" />
      <path class="st0" d="M724.09,398.73c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78s-2.78,1.24-2.78,2.78
		C721.31,397.49,722.55,398.73,724.09,398.73L724.09,398.73z" />
      <line class="st9" x1="721.32" y1="1008.47" x2="721.32" y2="1046.71" />
      <line class="st10" x1="724.3" y1="1048.24" x2="1322.02" y2="1048.24" />
      <path class="st11"
        d="M721.32,1005.41L721.32,1005.41 M721.32,1048.24L721.32,1048.24 M1323.51,1048.24L1323.51,1048.24" />
      <path class="st4" d="M721.32,1002.63c1.53,0,2.78,1.24,2.78,2.78c0,1.53-1.24,2.78-2.78,2.78c-1.53,0-2.78-1.25-2.78-2.78
		C718.54,1003.87,719.79,1002.63,721.32,1002.63L721.32,1002.63z" />
      <path class="st12" d="M884.35,934.73c9.93,0,42.27,0,61.35,0" />
      <line class="st13" x1="947.2" y1="931.95" x2="947.2" y2="916.62" />
      <line class="st14" x1="950.18" y1="915.23" x2="1322.02" y2="915.23" />
      <path class="st15" d="M881.35,934.73L881.35,934.73 M947.2,934.73L947.2,934.73 M947.2,915.23L947.2,915.23 M1323.51,915.23
		L1323.51,915.23" />
      <path class="st2" d="M881.35,937.51c1.53,0,2.78-1.24,2.78-2.78c0-1.54-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C878.58,936.27,879.82,937.51,881.35,937.51L881.35,937.51z" />
      <line class="st16" x1="940.02" y1="867.73" x2="1007.11" y2="867.73" />
      <line class="st13" x1="1008.6" y1="864.95" x2="1008.6" y2="849.62" />
      <line class="st17" x1="1011.57" y1="848.23" x2="1322.03" y2="848.23" />
      <path class="st15" d="M937.03,867.73L937.03,867.73 M1008.6,867.73L1008.6,867.73 M1008.6,848.23L1008.6,848.23 M1323.51,848.23
		L1323.51,848.23" />
      <path class="st2" d="M937.03,870.51c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C934.26,869.27,935.5,870.51,937.03,870.51L937.03,870.51z" />
      <line class="st18" x1="971.9" y1="798.73" x2="1019.23" y2="798.73" />
      <path class="st19" d="M1020.76,795.73c0-2.3,0-6.35,0-13.5" />
      <line class="st20" x1="1023.72" y1="780.73" x2="1322.03" y2="780.73" />
      <path class="st15" d="M968.85,798.73L968.85,798.73 M1020.76,798.73L1020.76,798.73 M1020.76,780.73L1020.76,780.73
		 M1323.51,780.73L1323.51,780.73" />
      <path class="st2" d="M968.85,801.51c1.53,0,2.78-1.24,2.78-2.78c0-1.54-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C966.07,800.27,967.32,801.51,968.85,801.51L968.85,801.51z" />
      <line class="st21" x1="990.64" y1="693.73" x2="1026.81" y2="693.73" />
      <line class="st22" x1="1028.26" y1="696.59" x2="1028.26" y2="712.3" />
      <line class="st23" x1="1031.25" y1="713.73" x2="1322.51" y2="713.73" />
      <path class="st15" d="M987.74,693.73L987.74,693.73 M1028.26,693.73L1028.26,693.73 M1028.26,713.73L1028.26,713.73 M1324,713.73
		L1324,713.73" />
      <path class="st2" d="M987.74,696.51c1.54,0,2.78-1.24,2.78-2.78c0-1.54-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C984.96,695.27,986.21,696.51,987.74,696.51L987.74,696.51z" />
      <line class="st24" x1="815.76" y1="423.32" x2="883.72" y2="423.32" />
      <line class="st25" x1="885.23" y1="426.12" x2="885.23" y2="444.33" />
      <line class="st26" x1="888.21" y1="445.73" x2="1322.02" y2="445.73" />
      <path class="st8" d="M812.73,423.32L812.73,423.32 M885.23,423.32L885.23,423.32 M885.23,445.73L885.23,445.73 M1323.51,445.73
		L1323.51,445.73" />
      <path class="st0" d="M812.73,426.1c1.53,0,2.78-1.24,2.78-2.78s-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		S811.2,426.1,812.73,426.1L812.73,426.1z" />
      <line class="st27" x1="888.36" y1="471.73" x2="965.59" y2="471.73" />
      <line class="st28" x1="967.11" y1="474.66" x2="967.11" y2="511.27" />
      <line class="st29" x1="970.08" y1="512.73" x2="1322.52" y2="512.73" />
      <path class="st8" d="M885.33,471.73L885.33,471.73 M967.11,471.73L967.11,471.73 M967.11,512.73L967.11,512.73 M1324,512.73
		L1324,512.73" />
      <path class="st0" d="M885.33,474.51c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C882.55,473.27,883.8,474.51,885.33,474.51L885.33,474.51z" />
      <line class="st30" x1="942.83" y1="538.8" x2="997.04" y2="538.8" />
      <line class="st31" x1="998.51" y1="541.73" x2="998.51" y2="578.34" />
      <line class="st32" x1="1001.47" y1="579.8" x2="1323.02" y2="579.8" />
      <path class="st33" d="M939.9,538.8L939.9,538.8 M998.51,538.8L998.51,538.8 M998.51,579.8L998.51,579.8 M1324.5,579.8L1324.5,579.8
		" />
      <path class="st3" d="M939.9,541.58c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C937.12,540.33,938.36,541.58,939.9,541.58L939.9,541.58z" />
      <line class="st34" x1="812.77" y1="982.53" x2="812.77" y2="1014.22" />
      <line class="st35" x1="815.72" y1="1015.73" x2="893.95" y2="1015.73" />
      <line class="st36" x1="895.42" y1="1012.86" x2="895.42" y2="982.67" />
      <line class="st37" x1="898.4" y1="981.24" x2="1322.02" y2="981.24" />
      <path class="st11" d="M812.77,979.51L812.77,979.51 M812.77,1015.73L812.77,1015.73 M895.42,1015.73L895.42,1015.73 M895.42,981.24
		L895.42,981.24 M1323.51,981.24L1323.51,981.24" />
      <path class="st4" d="M812.77,976.73c1.53,0,2.78,1.25,2.78,2.78c0,1.54-1.24,2.78-2.78,2.78c-1.53,0-2.78-1.24-2.78-2.78
		C809.99,977.98,811.24,976.73,812.77,976.73L812.77,976.73z" />
      <line class="st6" x1="631.14" y1="393.17" x2="631.14" y2="380.62" />
      <line class="st7" x1="628.16" y1="379.23" x2="33.2" y2="379.23" />
      <path class="st8" d="M631.14,395.96L631.14,395.96 M631.14,379.23L631.14,379.23 M31.71,379.23L31.71,379.23" />
      <path class="st0" d="M631.14,398.73c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78s2.78,1.24,2.78,2.78
		C633.91,397.49,632.67,398.73,631.14,398.73L631.14,398.73z" />
      <line class="st9" x1="633.9" y1="1008.47" x2="633.9" y2="1046.71" />
      <line class="st10" x1="630.92" y1="1048.24" x2="33.2" y2="1048.24" />
      <path class="st11" d="M633.9,1005.41L633.9,1005.41 M633.9,1048.24L633.9,1048.24 M31.71,1048.24L31.71,1048.24" />
      <path class="st4" d="M633.9,1002.63c-1.53,0-2.78,1.24-2.78,2.78c0,1.53,1.24,2.78,2.78,2.78c1.53,0,2.78-1.25,2.78-2.78
		C636.68,1003.87,635.43,1002.63,633.9,1002.63L633.9,1002.63z" />
      <path class="st38" d="M470.87,934.73c-9.93,0-42.26,0-61.35,0" />
      <line class="st39" x1="408.03" y1="931.95" x2="408.03" y2="916.62" />
      <line class="st40" x1="405.04" y1="915.23" x2="33.2" y2="915.23" />
      <path class="st41" d="M473.87,934.73L473.87,934.73 M408.03,934.73L408.03,934.73 M408.03,915.23L408.03,915.23 M31.71,915.23
		L31.71,915.23" />
      <path class="st1" d="M473.87,937.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.54,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		C476.64,936.27,475.4,937.51,473.87,937.51L473.87,937.51z" />
      <line class="st42" x1="415.21" y1="867.73" x2="348.11" y2="867.73" />
      <line class="st39" x1="346.62" y1="864.95" x2="346.62" y2="849.62" />
      <line class="st43" x1="343.65" y1="848.23" x2="33.2" y2="848.23" />
      <path class="st41" d="M418.19,867.73L418.19,867.73 M346.62,867.73L346.62,867.73 M346.62,848.23L346.62,848.23 M31.71,848.23
		L31.71,848.23" />
      <path class="st1" d="M418.19,870.51c-1.54,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		S419.72,870.51,418.19,870.51L418.19,870.51z" />
      <line class="st44" x1="383.32" y1="798.73" x2="335.99" y2="798.73" />
      <path class="st45" d="M334.47,795.73c0-2.3,0-6.35,0-13.5" />
      <line class="st46" x1="331.5" y1="780.73" x2="33.2" y2="780.73" />
      <path class="st41" d="M386.37,798.73L386.37,798.73 M334.47,798.73L334.47,798.73 M334.47,780.73L334.47,780.73 M31.71,780.73
		L31.71,780.73" />
      <path class="st1" d="M386.37,801.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.54,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		S387.91,801.51,386.37,801.51L386.37,801.51z" />
      <line class="st47" x1="364.59" y1="693.73" x2="328.41" y2="693.73" />
      <line class="st48" x1="326.96" y1="696.59" x2="326.96" y2="712.3" />
      <line class="st49" x1="323.97" y1="713.73" x2="32.71" y2="713.73" />
      <path class="st41" d="M367.48,693.73L367.48,693.73 M326.96,693.73L326.96,693.73 M326.96,713.73L326.96,713.73 M31.22,713.73
		L31.22,713.73" />
      <path class="st1" d="M367.48,696.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.54,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		S369.02,696.51,367.48,696.51L367.48,696.51z" />
      <line class="st24" x1="539.47" y1="423.32" x2="471.5" y2="423.32" />
      <line class="st25" x1="469.99" y1="426.12" x2="469.99" y2="444.33" />
      <line class="st26" x1="467.01" y1="445.73" x2="33.2" y2="445.73" />
      <path class="st8" d="M542.49,423.32L542.49,423.32 M469.99,423.32L469.99,423.32 M469.99,445.73L469.99,445.73 M31.71,445.73
		L31.71,445.73" />
      <path class="st0" d="M542.49,426.1c-1.53,0-2.78-1.24-2.78-2.78s1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		S544.02,426.1,542.49,426.1L542.49,426.1z" />
      <line class="st27" x1="466.86" y1="471.73" x2="389.63" y2="471.73" />
      <line class="st28" x1="388.11" y1="474.66" x2="388.11" y2="511.27" />
      <line class="st29" x1="385.14" y1="512.73" x2="32.71" y2="512.73" />
      <path class="st8" d="M469.89,471.73L469.89,471.73 M388.11,471.73L388.11,471.73 M388.11,512.73L388.11,512.73 M31.22,512.73
		L31.22,512.73" />
      <path class="st0" d="M469.89,474.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		C472.67,473.27,471.42,474.51,469.89,474.51L469.89,474.51z" />
      <line class="st50" x1="409.57" y1="538.24" x2="343.21" y2="538.24" />
      <line class="st28" x1="341.73" y1="541.17" x2="341.73" y2="577.77" />
      <line class="st51" x1="338.75" y1="579.24" x2="32.71" y2="579.24" />
      <path class="st8" d="M412.52,538.24L412.52,538.24 M341.73,538.24L341.73,538.24 M341.73,579.24L341.73,579.24 M31.22,579.24
		L31.22,579.24" />
      <path class="st0" d="M412.52,541.02c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		C415.3,539.77,414.05,541.02,412.52,541.02L412.52,541.02z" />
      <line class="st52" x1="376.4" y1="605.24" x2="316.36" y2="605.24" />
      <line class="st52" x1="314.9" y1="608.17" x2="314.9" y2="644.77" />
      <line class="st53" x1="311.91" y1="646.24" x2="32.71" y2="646.24" />
      <path class="st41" d="M379.33,605.24L379.33,605.24 M314.9,605.24L314.9,605.24 M314.9,646.24L314.9,646.24 M31.22,646.24
		L31.22,646.24" />
      <path class="st1" d="M379.33,608.02c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78
		C382.1,606.77,380.86,608.02,379.33,608.02L379.33,608.02z" />
      <line class="st34" x1="542.45" y1="982.53" x2="542.45" y2="1014.22" />
      <line class="st35" x1="539.5" y1="1015.73" x2="461.27" y2="1015.73" />
      <line class="st36" x1="459.8" y1="1012.86" x2="459.8" y2="982.67" />
      <line class="st37" x1="456.82" y1="981.24" x2="33.2" y2="981.24" />
      <path class="st11" d="M542.45,979.51L542.45,979.51 M542.45,1015.73L542.45,1015.73 M459.8,1015.73L459.8,1015.73 M459.8,981.24
		L459.8,981.24 M31.71,981.24L31.71,981.24" />
      <path class="st4" d="M542.45,976.73c-1.53,0-2.78,1.25-2.78,2.78c0,1.54,1.24,2.78,2.78,2.78c1.53,0,2.78-1.24,2.78-2.78
		C545.23,977.98,543.98,976.73,542.45,976.73L542.45,976.73z" />
      <path class="st54" d="M437.9,627.88h-0.65c-0.8,0-1.46,0.65-1.46,1.46v7.1l-3.29-3.7c-0.31-0.35-0.77-0.53-1.25-0.48
		c-0.47,0.05-0.89,0.33-1.12,0.74l-3.64,6.56c-0.39,0.7-0.14,1.59,0.57,1.98c0.22,0.12,0.47,0.18,0.71,0.18
		c0.51,0,1.01-0.27,1.28-0.75l2.65-4.77l4.47,5.02c0.01,0.01,0.02,0.02,0.03,0.03c0.03,0.04,0.07,0.07,0.11,0.1
		c0.04,0.03,0.07,0.06,0.11,0.09c0.04,0.03,0.08,0.05,0.12,0.07s0.08,0.05,0.12,0.07s0.09,0.03,0.13,0.05
		c0.05,0.01,0.09,0.03,0.14,0.04c0.04,0.01,0.09,0.02,0.13,0.02c0.05,0.01,0.1,0.01,0.15,0.01c0.01,0,0.03,0.01,0.04,0.01h3.65
		c0.81,0,1.46-0.65,1.46-1.46v-7.95C442.35,629.87,440.36,627.88,437.9,627.88L437.9,627.88z" />
      <path class="st54" d="M433.24,622.78c-1.41,0-2.55,1.14-2.55,2.55s1.14,2.55,2.55,2.55s2.55-1.14,2.55-2.55
		C435.79,623.92,434.65,622.78,433.24,622.78L433.24,622.78z" />
      <path class="st54" d="M416.83,614.03c-5.49,0-9.48,3.68-9.48,8.75c0,0.8,0.65,1.46,1.46,1.46s1.46-0.65,1.46-1.46
		c0-2.2,1.11-3.97,2.92-4.96v10.14c0,0.02,0.01,0.04,0.01,0.06s-0.01,0.04-0.01,0.06v12.2c0,0.81,0.65,1.46,1.46,1.46
		s1.46-0.65,1.46-1.46v-10.94h1.46v10.94c0,0.81,0.65,1.46,1.46,1.46s1.46-0.65,1.46-1.46v-12.2c0-0.02,0-0.04-0.01-0.06
		c0-0.02,0.01-0.04,0.01-0.06v-10.14c1.81,0.99,2.92,2.76,2.92,4.96c0,0.8,0.65,1.46,1.46,1.46s1.46-0.65,1.46-1.46
		C426.31,617.71,422.33,614.03,416.83,614.03L416.83,614.03z" />
      <path class="st54" d="M421.21,613.3c1.61,0,2.92-1.31,2.92-2.92s-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92
		C418.29,611.99,419.6,613.3,421.21,613.3L421.21,613.3z" />
      <path class="st54" d="M431.42,612.93c0,0.6,0.49,1.09,1.09,1.09h2.92c0.6,0,1.09-0.49,1.09-1.09c0-0.6-0.49-1.09-1.09-1.09h-2.92
		C431.91,611.84,431.42,612.33,431.42,612.93L431.42,612.93z" />
      <path class="st54" d="M429.11,611.72c0.16,0.08,0.32,0.12,0.49,0.12c0.4,0,0.79-0.22,0.98-0.6l1.46-2.92
		c0.27-0.54,0.05-1.2-0.49-1.47c-0.54-0.27-1.2-0.05-1.47,0.49l-1.46,2.92C428.35,610.79,428.56,611.45,429.11,611.72L429.11,611.72
		z" />
      <path class="st54" d="M430.07,618.53c0.19,0.38,0.58,0.6,0.98,0.6c0.17,0,0.33-0.04,0.49-0.12c0.54-0.27,0.76-0.93,0.49-1.47
		l-1.46-2.92c-0.27-0.54-0.93-0.76-1.47-0.49s-0.76,0.93-0.49,1.47L430.07,618.53L430.07,618.53z" />
      <path class="st54" d="M938.33,626.21c2.03,1.03,2.09-4.37,2.09-4.37C939.95,622.12,936.3,625.18,938.33,626.21 M938.13,628.8
		c1.91,0.97,4.45-2.79,4.45-3.36c0,0-0.52,1.38-2.77,1.27C937.28,626.58,937.28,628.36,938.13,628.8 M936.73,631.54
		c1.91,0.98,4.45-2.78,4.45-3.36c0,0-0.52,1.38-2.77,1.27C935.88,629.33,935.88,631.11,936.73,631.54 M935.28,634.38
		c1.91,0.97,4.45-2.79,4.45-3.36c0,0-0.52,1.37-2.77,1.27C934.43,632.16,934.43,633.94,935.28,634.38 M936.79,625.16
		c-1.41-1.76-0.6-2.98-0.6-2.98c-0.46,0.34-2.02,4.6-0.11,5.58C936.93,628.18,938.37,627.14,936.79,625.16 M935.39,627.91
		c-1.41-1.76-0.59-2.99-0.59-2.99c-0.47,0.34-2.02,4.6-0.11,5.58C935.53,630.94,936.97,629.89,935.39,627.91 M933.94,630.74
		c-1.41-1.76-0.6-2.98-0.6-2.98c-0.47,0.34-2.02,4.6-0.11,5.57C934.09,633.77,935.53,632.72,933.94,630.74 M933.17,637.05l1.46-2.35
		c0.12-0.23-0.29-0.18-0.66-0.37s-0.56-0.55-0.68-0.32l-1.03,2.64C932.14,636.91,932.9,637.59,933.17,637.05 M941.41,631.65
		c-0.23,0.36-0.47,0.69-0.71,1.02c1.28,0.54,2.08,1.22,2.08,1.97c0,1.73-4.11,3.14-9.17,3.14s-9.17-1.41-9.17-3.14
		c0-1.49,3.02-2.72,7.07-3.05c0-0.35,0.01-0.7,0.04-1.07c-5.16,0.24-9.09,1.56-9.09,5.63c0,4.57,4.95,9.57,11.04,9.57
		c6.1,0,11.04-5,11.04-9.57C944.55,633.91,943.34,632.51,941.41,631.65 M925.3,625.51v2.15c-0.22-0.09-0.42-0.23-0.6-0.43
		s-0.3-0.44-0.36-0.71l-1.59,0.14c0.12,0.67,0.4,1.19,0.84,1.56c0.43,0.37,1,0.59,1.71,0.66v0.93h0.88v-0.96
		c0.79-0.1,1.41-0.36,1.85-0.78c0.45-0.42,0.67-0.95,0.67-1.56c0-0.55-0.18-1.01-0.53-1.36c-0.35-0.36-1.01-0.64-1.98-0.87v-2
		c0.39,0.14,0.63,0.42,0.73,0.82l1.54-0.17c-0.1-0.51-0.35-0.92-0.73-1.23s-0.9-0.49-1.54-0.55v-0.51h-0.88v0.51
		c-0.7,0.06-1.26,0.28-1.67,0.66c-0.42,0.38-0.63,0.85-0.63,1.41s0.18,1.02,0.56,1.42C923.92,625.03,924.5,625.32,925.3,625.51
		 M922.33,632.42h-2.78c-2.84,0-3.46-2.37-3.46-2.37c-1.87-8.22,3.8-12.68,3.8-12.68h11.8c0,0,2.24,1.76,3.43,5.11
		c-0.79,0.91-1.51,1.99-2.12,3.22c-0.57,1.16-0.97,2.33-1.22,3.44C928.91,629.24,924.47,629.75,922.33,632.42 M930.01,610.76
		c-2.28-0.25-3.08,1.15-4.22,1.21c-1.15-0.06-1.94-1.46-4.23-1.21c-2.33,0.26-3.75,2.25-3.75,2.25l2.85,2.65h10.26l2.85-2.65
		C933.76,613.01,932.35,611.02,930.01,610.76 M924.51,623.4c0,0.18,0.07,0.35,0.19,0.5c0.13,0.16,0.33,0.28,0.59,0.38v-1.77
		c-0.24,0.07-0.43,0.18-0.57,0.35C924.58,623.03,924.51,623.2,924.51,623.4 M926.97,626.35c0.16,0.17,0.24,0.36,0.24,0.59
		c0,0.25-0.09,0.48-0.28,0.67s-0.43,0.31-0.74,0.35v-2C926.54,626.05,926.81,626.18,926.97,626.35" />
      <path class="st54"
        d="M459.13,544.52c-0.98-0.8-1.66-0.61-2.64,1.14c-0.65,1.16-1.68,1.3-2.31,1.26v-0.23
		c0.73-0.36,1.25-1.1,1.25-1.97c0-1.23-0.99-2.22-2.22-2.22s-2.22,0.99-2.22,2.22c0,0.87,0.52,1.61,1.25,1.97v0.23
		c-0.63,0.04-1.66-0.1-2.31-1.26c-0.98-1.75-1.66-1.94-2.63-1.14c-0.98,0.8-4.86,5.43-9.58,5.01c0,0,0.94,2.13,3.49,1.65
		c0,0,1.37,1.42,3.58,0.42c0,0,1.15,1.04,2.98,0.09c0,0,1.36,1.04,2.81,0.14c0,0,0.82,0.59,1.73,0.44l0.06,5.35
		c-0.1-0.02-0.19-0.04-0.29-0.06c0,0-1.59-0.34-3.26-0.81c-1.61-0.42-3.38-1.11-3.64-1.46c0.02-0.02,0.06-0.04,0.11-0.06
		c0.14-0.07,0.39-0.15,0.68-0.21c0.59-0.12,1.39-0.18,2.2-0.21c1.6-0.06,1.89,0.01,1.92,0.02c0-0.05,0.93,0.11,1.18-0.83
		c-0.01-0.01,0.02-0.05,0-0.07c-0.05-0.65-0.55-0.68-0.96-0.76c-0.66-0.09-0.32-0.05-1.21-0.04c-1.47,0.11-5.98-0.26-6.55,2.12
		c0,0.07-0.01,0.11-0.01,0.17c0.19,2.07,4.47,2.97,7.58,3.59c-1.05,0.72-1.62,1.66-1.84,2.87c-0.11,1.29,0.92,2.53,3.31,3.9
		c-1.81,1.28-3,2.49-2.91,3.94c0.17,1.19,1.22,2.77,3.27,3.77c0.01,0,0.01,0,0.01,0l0,0c0,0,0,0,0.01,0c0,0-1.44-2.2-1.54-3.4
		c-0.1-0.7,0.3-1.74,2.06-2.99l0.05,4.39h0.01c0.01,0.37,0.3,0.67,0.66,0.67c0.36,0,0.65-0.3,0.66-0.67h0.01l0.06-4.28
		c1.61,1.2,1.98,2.19,1.89,2.87c-0.1,1.2-1.53,3.4-1.53,3.4l0,0c0,0,0.01,0,0.02,0c2.06-1,3.11-2.59,3.27-3.77
		c0.1-1.46-1.09-2.66-2.9-3.94c2.38-1.38,3.41-2.61,3.31-3.9c-0.22-1.21-0.79-2.15-1.84-2.87c3.11-0.62,7.39-1.52,7.58-3.59
		c-0.01-0.06-0.01-0.1-0.01-0.17c-0.57-2.38-5.08-2.01-6.55-2.12c-0.89-0.01-0.55-0.05-1.21,0.04c-0.41,0.08-0.91,0.11-0.96,0.76
		c-0.02,0.02,0.01,0.06,0,0.07c0.25,0.94,1.18,0.78,1.18,0.83c0.03-0.01,0.31-0.08,1.92-0.02c0.8,0.03,1.6,0.09,2.2,0.21
		c0.29,0.06,0.53,0.14,0.68,0.21c0.05,0.02,0.08,0.04,0.11,0.06c-0.26,0.36-2.03,1.04-3.64,1.46c-1.67,0.47-3.26,0.81-3.26,0.81
		c-0.04,0.01-0.07,0.02-0.11,0.02l0.07-5.31c0.92,0.16,1.74-0.44,1.74-0.44c1.45,0.9,2.81-0.14,2.81-0.14
		c1.83,0.94,2.98-0.09,2.98-0.09c2.21,0.99,3.58-0.42,3.58-0.42c2.55,0.47,3.49-1.65,3.49-1.65
		C463.99,549.95,460.11,545.32,459.13,544.52L459.13,544.52z M450.32,562.28c0.03-0.47-0.13-1.58,2.08-2.39l0.05,4.41
		c-0.43-0.27-0.87-0.55-1.31-0.83C450.54,563.11,450.26,562.62,450.32,562.28L450.32,562.28z M455.1,563.48
		c-0.39,0.25-0.77,0.48-1.14,0.72l0.06-4.24c2.01,0.8,1.86,1.87,1.89,2.32C455.97,562.62,455.69,563.11,455.1,563.48L455.1,563.48z" />
      <path class="st54" d="M510.37,488.07c0,2.94-2.39,5.33-5.33,5.33c-2.94,0-5.33-2.39-5.33-5.33c0-2.94,2.39-5.33,5.33-5.33
		C507.99,482.74,510.37,485.12,510.37,488.07L510.37,488.07z" />
      <path class="st54" d="M517.17,503.44c0,0-2.03-4.06-3.35-6.19c-1.32-2.13-3.15-2.23-3.15-2.23h-10.15
		c-2.94,0.51-4.87,3.65-7.51,10.76c-2.64,7.1,5.48,9.74,9.23,9.95c3.75,0.2,5.08-1.52,4.87-3.25c-0.2-1.73-2.34-1.73-3.15-1.62
		c-0.81,0.1-4.36-0.41-5.68-1.12s-0.91-1.02,0.61-1.02s2.44-0.81,2.44-0.81c0.81-0.2-0.51-1.62-0.71-2.64
		c-0.2-1.02-0.41-2.03,0.91-2.33s1.12,0.41,3.35,3.25s4.97,2.23,4.97,2.23s-2.84,1.62-1.32,3.76c1.52,2.13,6.29,0,8.22-3.45
		C518.69,505.27,517.17,503.44,517.17,503.44L517.17,503.44z M509.21,507.6c-1.99,0-3.6-1.61-3.6-3.6c0-1.99,1.61-3.6,3.6-3.6
		c1.99,0,3.6,1.61,3.6,3.6C512.81,505.99,511.19,507.6,509.21,507.6L509.21,507.6z" />
      <path class="st54" d="M584.81,449.61h-13.75c-0.38,0-0.69,0.31-0.69,0.69v3.44c0,0.38,0.31,0.69,0.69,0.69h13.75
		c0.38,0,0.69-0.31,0.69-0.69v-3.44C585.5,449.92,585.19,449.61,584.81,449.61L584.81,449.61z" />
      <path class="st54" d="M571.75,475.05c0,0.38,0.31,0.69,0.69,0.69h11c0.38,0,0.69-0.31,0.69-0.69V455.8h-12.38V475.05L571.75,475.05
		z M573.81,459.92c0-0.38,0.31-0.69,0.69-0.69h6.88c0.38,0,0.69,0.31,0.69,0.69v4.81c0,0.38-0.31,0.69-0.69,0.69h-6.88
		c-0.38,0-0.69-0.31-0.69-0.69V459.92L573.81,459.92z M574.5,467.48h6.88c0.38,0,0.69,0.31,0.69,0.69s-0.31,0.69-0.69,0.69h-6.88
		c-0.38,0-0.69-0.31-0.69-0.69S574.12,467.48,574.5,467.48L574.5,467.48z" />
      <path class="st54" d="M565.91,448.23h-3.78v-3.44h1.72c0.57,0,1.03-0.46,1.03-1.03s-0.46-1.03-1.03-1.03h-8.25
		c-0.57,0-1.03,0.46-1.03,1.03s0.46,1.03,1.03,1.03h1.72v3.44h-3.78c-0.57,0-1.03,0.46-1.03,1.03s0.46,1.03,1.03,1.03h2.41v15.81
		c0,0.76,0.62,1.38,1.38,1.38v1.38c0,0.38,0.31,0.69,0.69,0.69h0.69v5.16c0,0.57,0.46,1.03,1.03,1.03s1.03-0.46,1.03-1.03v-5.16
		h0.69c0.38,0,0.69-0.31,0.69-0.69v-1.38c0.76,0,1.38-0.62,1.38-1.38v-15.8h2.41c0.57,0,1.03-0.46,1.03-1.03
		C566.94,448.69,566.48,448.23,565.91,448.23L565.91,448.23z M561.44,460.61H558v-8.94h3.44V460.61L561.44,460.61z" />
      <path class="st54" d="M642.1,451.27c2.82,0,4.53-1.85,4.65-4.43c0.01-0.12-0.11-0.22-0.23-0.22h-15.56h-6.29
		c-0.73,0-1.16,0.49-1.16,1.16c0,0.68,0.43,1.16,1.16,1.16h7.47h6.09C639.13,450.4,640.16,451.27,642.1,451.27" />
      <path class="st54"
        d="M650.85,439.27c-0.76,0.74-1.77,1.15-2.84,1.15s-2.08-0.4-2.84-1.15c-0.35-0.34-0.35-0.91,0-1.25
		c0.36-0.35,0.93-0.35,1.29,0c0.83,0.81,2.27,0.81,3.1,0c0.36-0.35,0.93-0.35,1.29,0C651.2,438.37,651.2,438.93,650.85,439.27
		 M640,439.27c-0.76,0.74-1.77,1.15-2.84,1.15s-2.08-0.4-2.84-1.15c-0.35-0.34-0.35-0.91,0-1.25c0.36-0.35,0.93-0.35,1.29,0
		c0.83,0.81,2.27,0.81,3.1,0c0.36-0.35,0.93-0.35,1.29,0C640.34,438.37,640.34,438.93,640,439.27 M655.63,437.38
		c-0.39-0.39-0.88-0.69-1.42-0.83V435c0-2.99-1.3-5.7-3.41-7.67c-2.08-1.94-4.94-3.15-8.11-3.18c-0.54,0.39-0.88,1.02-0.88,1.73
		c0,1.15,1.09,2.15,2.33,2.15c0.43,0,0.77,0.35,0.77,0.78s-0.35,0.77-0.77,0.77c-2.1,0-3.88-1.69-3.88-3.7
		c0-0.56,0.12-1.09,0.36-1.57c-5.49,0.87-9.66,5.33-9.66,10.7v1.55c-0.54,0.14-1.03,0.44-1.42,0.83c-0.56,0.58-0.91,1.39-0.91,2.27
		s0.35,1.68,0.91,2.27c0.39,0.39,0.88,0.69,1.42,0.83v1.55c0,0.25,0.02,0.5,0.06,0.77H647c0.49,0,0.96,0.2,1.3,0.56
		c0.33,0.34,0.5,0.81,0.48,1.28c-0.17,3.53-2.66,5.91-6.2,5.91c-2.42,0-3.79-1.13-4.69-2.33h-4.13c2.12,2.54,5.29,4.65,8.82,4.65
		c6.42,0,11.62-6.92,11.62-10.85v-1.55c0.54-0.14,1.03-0.44,1.42-0.83c0.56-0.59,0.91-1.39,0.91-2.27S656.19,437.96,655.63,437.38" />
      <path class="st54" d="M731.44,425.6v-0.04c-3.74-3.76-9.83-3.78-13.59-0.03c-0.01,0.01-0.02,0.02-0.03,0.03l-1.43,1.42l-1.42-1.42
		c-3.77-3.77-9.88-3.76-13.65,0.02c-3.76,3.77-3.76,9.88,0.02,13.65l14.19,14.14c0.46,0.48,1.22,0.49,1.7,0.03
		c0.01-0.01,0.02-0.02,0.03-0.03l14.19-14.14C735.2,435.46,735.2,429.37,731.44,425.6L731.44,425.6z M720.06,439.46h-2.45v2.45
		c0,0.67-0.55,1.22-1.22,1.22s-1.22-0.55-1.22-1.22v-2.45h-2.45c-0.67,0-1.22-0.55-1.22-1.22s0.55-1.22,1.22-1.22h2.45v-2.45
		c0-0.67,0.55-1.22,1.22-1.22s1.22,0.55,1.22,1.22v2.45h2.45c0.67,0,1.22,0.55,1.22,1.22C721.28,438.91,720.74,439.45,720.06,439.46
		L720.06,439.46z" />
      <path class="st54" d="M732.04,955.28L716,947.31l-16.04,7.97l-1.46-2.93l17.48-8.69l0.01-0.02l0.02,0.01l0.02-0.01l0.01,0.02
		l17.48,8.69L732.04,955.28L732.04,955.28z M731.17,958.53c0,0.06,0,1.04,0,2.54v16.94H718.6c-0.43,0.36-1.45,0.62-2.64,0.62
		s-2.21-0.26-2.64-0.62h-12.49v-16.94c0-1.5,0-2.49,0-2.54c8.24-3.55,14.27-0.06,15.32,0.94
		C716.95,958.74,723.26,955.05,731.17,958.53L731.17,958.53z M715.03,962.62c0-2.52-3.35-3.88-7.5-3.88c-1.99,0-3.8,0.47-5.14,1.24
		v16.52c6.77-4.26,12.63-0.36,12.63,0.31v-14.19H715.03z M729.7,959.97c-1.34-0.77-3.14-1.24-5.13-1.24c-4.14,0-7.49,1.36-7.49,3.88
		v14.18c0-0.67,5.86-4.57,12.63-0.31v-16.51H729.7z" />
      <path class="st54" d="M424.77,700.99v0.02c-0.12-0.01-0.24-0.02-0.37-0.02c-0.08,0-0.16,0.01-0.24,0.01
		c-0.04,0-0.08-0.01-0.12-0.01h-9.15c-1.42,0-2.56,1.15-2.56,2.56s1.15,2.56,2.56,2.56h2.81h1.21c0.81,0,1.46,0.65,1.46,1.46
		s-0.65,1.46-1.46,1.46h-1.37h-3.75h-1.46c-0.39,0-0.9-0.17-1.17-0.44l-9.94-9.68c-1.21-1.21-3.22-1.14-4.34,0.21
		c-0.97,1.18-0.8,2.94,0.28,4.02l11.14,10.88c0.55,0.55,1.3,0.86,2.07,0.86h13.66c0.06,0,0.11-0.01,0.17-0.02
		c0.07,0,0.13,0.01,0.2,0.01c0.12,0,0.25-0.01,0.37-0.02v0.03c3.64,0,6.58-2.95,6.58-6.59v-0.73
		C431.36,703.94,428.41,700.99,424.77,700.99L424.77,700.99z" />
      <path class="st54"
        d="M400.99,694.4c0.02,0,0.03,0,0.05,0c0.01,0,0.02,0,0.02,0h6.52c1.01,0,1.83-0.82,1.83-1.83
		s-0.82-1.83-1.83-1.83h-1.97v-0.01h-0.96c-0.61,0-1.1-0.49-1.1-1.1s0.49-1.1,1.1-1.1h0.96h1.78h1.93c0.27,0,0.63,0.12,0.82,0.31
		l6.78,7.15c0.84,0.84,2.24,0.79,3.02-0.15c0.68-0.82,0.55-2.04-0.2-2.8l-7.75-7.56c-0.38-0.38-0.9-0.6-1.44-0.6h-9.5
		c-0.02,0-0.03,0.01-0.05,0.01l0,0c-2.63,0-4.75,2.13-4.75,4.75C396.23,692.27,398.36,694.4,400.99,694.4L400.99,694.4z" />
      <path class="st54" d="M890.05,844.29c0.2-1.16,0.62-2.26,1.19-3.25c0.3-0.54,0.68-1.06,1.08-1.53c0.14-0.17,0.29-0.34,0.45-0.49
		c-1.32-0.86-2.89-1.35-4.57-1.35c-4.65,0-8.43,3.78-8.43,8.44c0,3.11,1.7,5.84,4.21,7.29v1.15c0,0.93,0.76,1.69,1.69,1.69h5.06
		c0.94,0,1.69-0.76,1.69-1.69v-1.14v-0.62c-0.46-0.51-0.84-1.05-1.17-1.62C890.06,849.15,889.61,846.73,890.05,844.29L890.05,844.29
		z M882.28,846.11c0-1.62,0.65-3.08,1.7-4.15v8.3C882.93,849.19,882.28,847.73,882.28,846.11L882.28,846.11z" />
      <path class="st54" d="M888.2,835.98c1.86,0,3.38-1.51,3.38-3.38s-1.51-3.38-3.38-3.38c-1.86,0-3.38,1.51-3.38,3.38
		S886.34,835.98,888.2,835.98L888.2,835.98z" />
      <path class="st54" d="M911.82,835.98c1.86,0,3.38-1.51,3.38-3.38s-1.51-3.38-3.38-3.38s-3.38,1.51-3.38,3.38
		S909.96,835.98,911.82,835.98L911.82,835.98z" />
      <path class="st54" d="M911.82,837.67c-1.7,0-3.27,0.5-4.59,1.36c0.16,0.16,0.32,0.34,0.46,0.51c0.4,0.46,0.76,0.97,1.07,1.5
		c0.86,1.49,1.36,3.22,1.36,5.06c0,1.8-0.49,3.53-1.36,5.05c-0.34,0.57-0.73,1.11-1.16,1.61v0.63v1.14c0,0.93,0.76,1.69,1.69,1.69
		h5.06c0.93,0,1.69-0.76,1.69-1.69v-1.15c2.51-1.45,4.21-4.18,4.21-7.29C920.25,841.45,916.47,837.67,911.82,837.67L911.82,837.67z
		 M916.04,850.26v-8.3c1.05,1.07,1.7,2.53,1.7,4.15C917.74,847.73,917.09,849.19,916.04,850.26L916.04,850.26z" />
      <path class="st54" d="M900.01,835.98c1.86,0,3.38-1.51,3.38-3.38s-1.51-3.38-3.38-3.38c-1.86,0-3.38,1.51-3.38,3.38
		C896.64,834.47,898.15,835.98,900.01,835.98L900.01,835.98z" />
      <path class="st54" d="M908.44,846.11c0-1.31-0.3-2.55-0.84-3.65c-0.05-0.11-0.1-0.21-0.16-0.32c-0.4-0.75-0.92-1.44-1.53-2.04
		c-1.52-1.49-3.6-2.42-5.91-2.42c-0.52,0-1.05,0.05-1.59,0.14c-1.65,0.3-3.16,1.11-4.32,2.27c-0.61,0.59-1.13,1.28-1.53,2.04
		c-0.06,0.1-0.11,0.2-0.15,0.3c-0.34,0.68-0.57,1.4-0.71,2.15c-0.33,1.87-0.03,3.66,0.71,5.19c0.05,0.1,0.1,0.21,0.16,0.31
		c0.4,0.75,0.92,1.43,1.53,2.03c0.51,0.49,1.07,0.93,1.69,1.28v0.39c0,0.03,0.01,0.05,0.01,0.08c0,0.02-0.01,0.04-0.01,0.07v0.62
		c0,0.93,0.76,1.69,1.69,1.69h5.06c0.93,0,1.69-0.76,1.69-1.69v-0.62c0-0.02-0.01-0.04-0.01-0.07s0.01-0.05,0.01-0.08v-0.39
		c0.62-0.35,1.18-0.78,1.69-1.28c0.61-0.6,1.12-1.28,1.53-2.04c0.06-0.1,0.11-0.21,0.16-0.32
		C908.14,848.65,908.44,847.41,908.44,846.11L908.44,846.11z M895.79,850.25c-0.05-0.05-0.11-0.11-0.15-0.17
		c-0.9-0.98-1.48-2.26-1.54-3.67c0.02-0.1,0.02-0.2,0.02-0.3s0-0.2-0.02-0.3c0.06-1.42,0.63-2.69,1.54-3.68
		c0.04-0.06,0.1-0.11,0.15-0.17v0.48v7.34V850.25L895.79,850.25z M904.38,850.07c-0.04,0.06-0.09,0.12-0.15,0.18v-0.47v-7.34v-0.47
		c0.05,0.05,0.11,0.11,0.15,0.17c0.91,0.99,1.49,2.3,1.53,3.75c-0.01,0.08-0.01,0.15-0.01,0.23c0,0.08,0,0.15,0.01,0.23
		C905.87,847.77,905.29,849.08,904.38,850.07L904.38,850.07z" />
      <path class="st54" d="M870.71,909.79h-1.86h-2.83h-8.4c0,0.45-0.18,0.86-0.48,1.15c-0.29,0.3-0.7,0.48-1.15,0.48h-8.18
		c-0.9,0-1.64-0.74-1.64-1.64h-8.18h-3.27h-1.64c-0.45,0-0.82,0.37-0.82,0.82v3.27c0,0.45,0.37,0.82,0.82,0.82h37.64
		c0.45,0,0.82-0.37,0.82-0.82v-3.27C871.52,910.16,871.16,909.79,870.71,909.79L870.71,909.79z" />
      <path class="st54" d="M837.98,907.34h0.82v-15.55h26.18v15.55h0.82h3.27v-18c0-0.22-0.05-0.44-0.13-0.64
		c-0.16-0.39-0.48-0.71-0.87-0.87c-0.19-0.08-0.41-0.13-0.64-0.13h-31.09c-0.9,0-1.64,0.73-1.64,1.64v0.82v17.18h2.45H837.98
		L837.98,907.34z" />
      <path class="st54" d="M434.35,790.32h-8.02v-26.98h7.53l-3.81,8.71c-0.28,0.72,0.25,1.49,1.02,1.49c0.45,0,0.85-0.27,1.01-0.69
		l3.36-8.06l3.36,8.06c0.16,0.42,0.57,0.69,1.02,0.69c0.77,0,1.3-0.78,1.02-1.49l-4.36-10.21c-0.16-0.42-0.56-0.69-1.01-0.69h-9.14
		v-1.46c0-0.81-0.63-1.46-1.44-1.46s-1.48,0.65-1.48,1.46v1.46h-9.09c-0.45,0-0.85,0.28-1.01,0.69l-4.4,10.21
		c-0.28,0.72,0.24,1.49,1.02,1.49c0.45,0,0.85-0.27,1.02-0.69l3.36-8.06l3.36,8.06c0.17,0.42,0.57,0.69,1.02,0.69
		c0.77,0,1.3-0.78,1.01-1.49l-3.77-8.71h7.49v26.98h-8.02c-0.81,0-1.46,0.65-1.46,1.46s0.65,1.46,1.46,1.46h18.96
		c0.8,0,1.46-0.65,1.46-1.46C435.81,790.97,435.15,790.32,434.35,790.32L434.35,790.32z" />
      <path class="st54" d="M421.22,775.96c0.03-0.12-0.06-0.23-0.18-0.23h-13.48c-0.12,0-0.21,0.11-0.18,0.23
		c0.74,3.11,3.54,5.61,6.88,5.61C417.58,781.57,420.48,779.07,421.22,775.96L421.22,775.96z" />
      <path class="st54" d="M442.36,775.96c0.03-0.12-0.06-0.23-0.18-0.23H428.7c-0.12,0-0.21,0.11-0.18,0.23
		c0.74,3.11,3.54,5.61,6.88,5.61C438.73,781.57,441.62,779.07,442.36,775.96L442.36,775.96z" />
      <path class="st54" d="M463.01,831.53c-5.4,0-9.48,3.76-9.48,8.75c0,0.8,0.65,1.46,1.46,1.46c0.8,0,1.46-0.65,1.46-1.46
		c0-2.2,1.23-4.03,3.15-5.03l-2.41,13.66c-0.07,0.44,0.27,0.85,0.72,0.85h1.46v8.02c0,0.81,0.65,1.46,1.46,1.46
		c0.8,0,1.46-0.65,1.46-1.46v-8.02h1.46v8.02c0,0.81,0.65,1.46,1.46,1.46c0.8,0,1.46-0.65,1.46-1.46v-8.02h1.46
		c0.45,0,0.79-0.41,0.72-0.85l-2.34-13.62c1.87,1,3.08,2.82,3.08,4.99c0,0.8,0.65,1.46,1.46,1.46s1.46-0.65,1.46-1.46
		C472.49,835.29,468.41,831.53,463.01,831.53L463.01,831.53z" />
      <path class="st54" d="M463.01,830.07c1.61,0,2.92-1.31,2.92-2.92s-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92
		S461.4,830.07,463.01,830.07L463.01,830.07z" />
      <path class="st54" d="M446.6,854.13c-0.6,0-1.09,0.49-1.09,1.09v2.92c0,0.6,0.49,1.09,1.09,1.09s1.09-0.49,1.09-1.09v-2.92
		C447.69,854.62,447.2,854.13,446.6,854.13L446.6,854.13z" />
      <path class="st54" d="M454.62,849.03h-2.92c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h2.92c0.6,0,1.09-0.49,1.09-1.09
		S455.22,849.03,454.62,849.03L454.62,849.03z" />
      <path class="st54" d="M446.6,841c-0.6,0-1.09,0.49-1.09,1.09V845c0,0.6,0.49,1.09,1.09,1.09s1.09-0.49,1.09-1.09v-2.91
		C447.7,841.49,447.21,841,446.6,841L446.6,841z" />
      <path class="st54" d="M442.59,850.12c0-0.6-0.49-1.09-1.09-1.09h-2.92c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h2.92
		C442.1,851.21,442.59,850.72,442.59,850.12L442.59,850.12z" />
      <path class="st54" d="M451.02,852.99c-0.43-0.43-1.12-0.43-1.55,0s-0.43,1.12,0,1.55l2.19,2.19c0.43,0.43,1.12,0.43,1.55,0
		s0.43-1.12,0-1.55L451.02,852.99L451.02,852.99z" />
      <path class="st54" d="M451.02,847.25l2.19-2.19c0.43-0.43,0.43-1.12,0-1.55s-1.12-0.43-1.55,0l-2.19,2.19
		c-0.43,0.43-0.43,1.12,0,1.55C449.9,847.67,450.59,847.67,451.02,847.25L451.02,847.25z" />
      <path class="st54" d="M442.18,847.25c0.43,0.43,1.12,0.43,1.55,0s0.43-1.12,0-1.55l-2.19-2.19c-0.43-0.43-1.12-0.43-1.55,0
		s-0.43,1.12,0,1.55L442.18,847.25L442.18,847.25z" />
      <path class="st54" d="M442.18,852.99l-2.19,2.19c-0.43,0.43-0.43,1.12,0,1.55s1.12,0.43,1.55,0l2.19-2.19
		c0.43-0.43,0.43-1.12,0-1.55S442.61,852.56,442.18,852.99L442.18,852.99z" />
      <path class="st54" d="M491.54,889.22c1.61,0,2.92-1.31,2.92-2.92s-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92
		C488.62,887.92,489.93,889.22,491.54,889.22L491.54,889.22z" />
      <path class="st54" d="M516.88,904.14l2.86-5.65c0.88-1.74,0.17-3.87-1.57-4.75l-0.92-0.46l-0.95-0.48
		c-0.09-0.04-0.18-0.08-0.28-0.1c-0.85-0.39-1.74-0.65-2.63-0.79c-3.62-0.59-7.33,0.74-9.64,3.62l-1.55-1.79
		c-2.19-2.4-5.32-3.78-8.57-3.78c-1.55,0-3.05,0.74-3.98,1.99c-1,1.33-1.27,3.07-0.71,4.65c0.01,0.04,0.03,0.07,0.04,0.1l2.1,4.81
		c0.15,0.56,0.53,1.76,1.11,3.58c1.04,3.28,1.75,6.67,2.09,10.08l0.19,1.92c0.07,0.75,0.71,1.31,1.45,1.31c0.04,0,0.09,0,0.15-0.01
		c0.8-0.08,1.38-0.79,1.3-1.6l-0.19-1.91c-0.33-3.24-0.96-6.47-1.89-9.61h2.9c0.83,2.22,1.37,4.6,1.37,8.75
		c0,0.68,0.47,1.25,1.09,1.41l1.77-3.47c-0.24-4.94-1.36-7.52-2.64-10.44c-0.29-0.67-0.6-1.36-0.9-2.12l-2.46-6.06
		c1.37,0.47,2.62,1.26,3.6,2.33l2.81,3.27c0.26,0.3,0.61,0.47,0.98,0.5c0.07,0,0.12,0.01,0.17,0.01c0.55,0,1.08-0.3,1.35-0.82
		c1.18-2.3,3.43-3.64,5.84-3.81c0.28-0.02,0.55-0.03,0.82-0.01c0.26,0.01,0.52,0.04,0.78,0.07l-10.86,21.31
		c-0.39,0.75-0.09,1.67,0.66,2.05c0.22,0.12,0.46,0.17,0.69,0.17c0.55,0,1.09-0.31,1.36-0.83l6.59-12.93l0.65,0.33l0.66,0.33
		l2.38,1.21c0.01,0.01,0.02,0.01,0.03,0.02c0.02,0.01,0.03,0.02,0.05,0.03l0.04,0.02c3.15,2.04,4.3,6.2,2.53,9.6
		c-0.39,0.75-0.1,1.66,0.65,2.05c0.37,0.19,0.79,0.22,1.16,0.1s0.7-0.38,0.89-0.75C522.72,912.83,521.18,907.07,516.88,904.14
		L516.88,904.14z" />
      <path class="st54" d="M523.47,889.04c-0.5-1.53-2.15-2.36-3.68-1.86c-1.53,0.5-2.36,2.15-1.86,3.68c0.5,1.53,2.15,2.36,3.68,1.86
		C523.15,892.22,523.98,890.57,523.47,889.04L523.47,889.04z" />
      <path class="st54" d="M583.63,954.06h-32.81c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h32.81c0.6,0,1.09-0.49,1.09-1.09
		S584.24,954.06,583.63,954.06L583.63,954.06z" />
      <path class="st54" d="M564.31,945.31c0-0.8,0.66-1.46,1.46-1.46h2.92c0.8,0,1.46,0.66,1.46,1.46v7.29h11.67v-18.23
		c0-0.4-0.33-0.73-0.73-0.73h-7.29l-5.1-3.83v-2.73h6.56v-4.38h-6.56c0-0.81-0.65-1.46-1.46-1.46c-0.8,0-1.46,0.65-1.46,1.46v7.11
		l-5.1,3.83h-7.29c-0.4,0-0.73,0.33-0.73,0.73v18.23h11.67v-7.29H564.31z M575.25,937.29c0-0.4,0.33-0.73,0.73-0.73h1.46
		c0.4,0,0.73,0.33,0.73,0.73v3.65c0,0.4-0.33,0.73-0.73,0.73h-1.46c-0.4,0-0.73-0.33-0.73-0.73V937.29L575.25,937.29z
		 M575.25,945.31c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73v3.65c0,0.4-0.33,0.73-0.73,0.73h-1.46
		c-0.4,0-0.73-0.33-0.73-0.73V945.31L575.25,945.31z M559.21,948.96c0,0.4-0.33,0.73-0.73,0.73h-1.46c-0.4,0-0.73-0.33-0.73-0.73
		v-3.65c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73V948.96L559.21,948.96z M559.21,940.94c0,0.4-0.33,0.73-0.73,0.73
		h-1.46c-0.4,0-0.73-0.33-0.73-0.73v-3.65c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73V940.94L559.21,940.94z
		 M570.14,936.57c0,1.61-1.3,2.92-2.92,2.92c-1.61,0-2.92-1.31-2.92-2.92s1.31-2.92,2.92-2.92
		C568.84,933.65,570.14,934.95,570.14,936.57L570.14,936.57z" />
      <path class="st54" d="M902.46,562.01l5.23-5.18c0.56-0.57,1.47-0.57,2.03,0c0.56,0.57,0.56,1.49,0,2.06l-2.61,2.51
		c-0.33,0.33-0.33,0.87,0,1.2s0.86,0.33,1.18,0l3.23-3.45v-11c0-1.14,0.94-2.06,2.06-2.06s2.06,0.92,2.06,2.06v11.96
		c0,0.55-0.21,1.07-0.59,1.46l-7.66,7.89v6.19h-6.19v-10.31C901.21,563.97,901.56,562.93,902.46,562.01L902.46,562.01z" />
      <path class="st54" d="M895.82,562.01l-5.23-5.18c-0.56-0.57-1.47-0.57-2.03,0c-0.56,0.57-0.56,1.49,0,2.06l2.61,2.51
		c0.33,0.33,0.33,0.87,0,1.2s-0.85,0.33-1.18,0l-3.23-3.45v-11c0-1.14-0.94-2.06-2.06-2.06s-2.06,0.92-2.06,2.06v11.96
		c0,0.55,0.21,1.07,0.6,1.46l7.65,7.89v6.19h6.19v-10.31C897.08,563.97,896.72,562.93,895.82,562.01L895.82,562.01z" />
      <path class="st54" d="M905.33,548.85c0-3.42-2.77-6.19-6.19-6.19s-6.19,2.77-6.19,6.19s2.77,6.19,6.19,6.19
		C902.56,555.03,905.33,552.26,905.33,548.85L905.33,548.85z" />
      <path class="st54" d="M939.72,707.87h-1.46c-0.4,0-0.73,0.33-0.73,0.73v0.73c0,0.4,0.33,0.73,0.73,0.73h1.46
		c0.4,0,0.73-0.33,0.73-0.73v-0.73C940.45,708.2,940.12,707.87,939.72,707.87L939.72,707.87z" />
      <path class="st54" d="M939.72,702.04h-1.46c-0.4,0-0.73,0.33-0.73,0.73v0.73c0,0.4,0.33,0.73,0.73,0.73h1.46
		c0.4,0,0.73-0.33,0.73-0.73v-0.73C940.45,702.36,940.12,702.04,939.72,702.04L939.72,702.04z" />
      <path class="st54" d="M944.1,694.02c0.81,0,1.46-0.65,1.46-1.46s-0.65-1.46-1.46-1.46c-0.8,0-1.46,0.65-1.46,1.46
		C942.64,693.36,943.29,694.02,944.1,694.02L944.1,694.02z" />
      <path class="st54" d="M949.57,707.87h-5.83c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h5.83c0.6,0,1.09-0.49,1.09-1.09
		C950.66,708.36,950.17,707.87,949.57,707.87L949.57,707.87z" />
      <path class="st54" d="M947.01,697.96c0-1.37-1.11-2.49-2.49-2.49h-0.86c-1.37,0-2.49,1.11-2.49,2.49v1.16H947L947.01,697.96
		L947.01,697.96z" />
      <path class="st54" d="M954.3,685.27h-3.65c0-0.8-0.66-1.46-1.46-1.46H947c0-0.8-0.33-1.53-0.85-2.06
		c-0.53-0.52-1.26-0.85-2.06-0.85c-1.61,0-2.92,1.3-2.92,2.92h-2.19c-0.8,0-1.46,0.66-1.46,1.46h-3.64c-0.8,0-1.46,0.71-1.46,1.57
		v27.49c0,0.86,0.66,1.57,1.46,1.57h20.42c0.8,0,1.46-0.71,1.46-1.57v-27.49C955.76,685.97,955.11,685.27,954.3,685.27L954.3,685.27
		z M944.1,683.81c0.4,0,0.73,0.33,0.73,0.73c0,0.4-0.33,0.73-0.73,0.73c-0.4,0-0.73-0.33-0.73-0.73
		C943.37,684.13,943.69,683.81,944.1,683.81L944.1,683.81z M952.85,712.97h-17.5v-24.79h2.19c0,0.8,0.66,1.46,1.46,1.46h10.21
		c0.8,0,1.46-0.66,1.46-1.46h2.19v24.79H952.85z" />
      <path class="st54" d="M949.57,702.04h-5.83c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h5.83c0.6,0,1.09-0.49,1.09-1.09
		C950.66,702.53,950.17,702.04,949.57,702.04L949.57,702.04z" />
      <path class="st54" d="M852.2,482.89c-0.16-0.2-0.47-0.2-0.63,0c-1.93,2.48-12.08,15.83-12.08,22.17c0,7,5.55,12.68,12.4,12.68
		s12.4-5.68,12.4-12.68C864.28,498.72,854.13,485.37,852.2,482.89L852.2,482.89z M855.17,512.64c-0.6,0-1.09-0.49-1.09-1.09
		s0.49-1.09,1.09-1.09c1.81,0,3.28-1.8,3.28-4.01c0-0.6,0.49-1.09,1.09-1.09s1.09,0.49,1.09,1.09
		C860.64,509.86,858.19,512.64,855.17,512.64L855.17,512.64z" />
      <path class="st54" d="M806.47,467.85l-18.89-9.48c0,0,0-0.04,0.01-0.1c0.02-0.11,0.02-0.21,0.02-0.26L787.6,458
		c0.04-1.42-0.03-6.67-2.92-9.86c0.12,0.13,0.25,0.25,0.36,0.4c0,0-3.53-5.18-6.95-5.36c-1.66-0.09-2.89,1.19-3.28,1.69
		s-2.07,3.32-1.96,7.4c0,0-0.02-1.57,0.84-3.22c-1.49,3.12-0.65,5.49,0.23,7.02c0.19,1.6,1.07,2.74,1.48,3.35
		c0.78,1.18,2.85,2.87,3.56,3.33c-0.36,1.48-1,4.18-1.26,5.95c-0.29,2.04-0.51,7.79-0.51,7.79l6.66,1.69c0,0,0.22-0.28,0.25-0.67
		c0.02-0.21,0.8-7.98,1.38-11.01c3.43,1.77,11.9,6.14,11.9,6.14l0.56-0.91c2.64,1.36,4.67,2.41,4.67,2.41L806.47,467.85
		L806.47,467.85z M784.57,448.02c-0.06-0.06-0.12-0.12-0.18-0.18C784.45,447.9,784.51,447.96,784.57,448.02L784.57,448.02z
		 M775.9,446.59c1.66-1.09,4.58-0.67,5.06-0.59c0.2,0.04,0.71,0.18,1.33,0.46c0.83,1.7,0.77,5.88-0.85,8.9c0,0-6.78-3.11-7.68-6.43
		C774.2,448.1,774.88,447.25,775.9,446.59L775.9,446.59z" />
      <path class="st54" d="M636.54,965.41l-1.5,2.76c-0.07,0.16-0.28,0.43-0.79,0.43c-0.62,0-1.67-0.39-2.35-0.68l-0.13,0.29l-1.02-0.47
		l0.13-0.28c-0.9-0.45-2.01-1.1-2.22-1.66l-0.08-0.31l0.08-0.22l1.15-2.96c-1.18,0.75-2.2,2.38-3.49,4.99l-1.46,3.07
		c-0.12,0.27-0.25,0.54-0.38,0.83l8.72,4.03c0.13-0.28,0.26-0.56,0.38-0.83l1.4-3.09C636.16,968.62,636.74,966.79,636.54,965.41
		L636.54,965.41z M633.74,972.14l-1.08,2.35l-7.26-3.36l1.09-2.35c0.31-0.66,1.11-1,2.12-1c0.75,0,1.62,0.19,2.48,0.59
		C633.09,969.3,634.29,970.98,633.74,972.14L633.74,972.14z M633.17,971.09c0.11,0.31,0.11,0.57,0.01,0.79l-0.83,1.79l-6.14-2.84
		l0.83-1.79c0.19-0.4,0.77-0.65,1.55-0.65c0.69,0,1.48,0.19,2.22,0.54C631.98,969.47,632.88,970.29,633.17,971.09L633.17,971.09z
		 M634.82,962.51c0.21,0.09,0.44,0.15,0.67,0.17c0.04,0.22,0.05,0.45,0.03,0.68c0.64,0.4,1.03,0.73,0.96,0.87l-2,3.69
		c-0.11,0.24-1.37-0.1-2.82-0.77c-1.44-0.67-2.52-1.41-2.41-1.66l1.51-3.91c0.07-0.14,0.57-0.06,1.28,0.17
		c0.44-0.45,1.03-0.7,1.6-0.7c0.04,0.2,0.1,0.41,0.23,0.63c-0.39-0.07-0.8,0.05-1.15,0.31c0.35,0.14,0.72,0.29,1.11,0.47
		s0.75,0.36,1.07,0.54C634.89,962.83,634.88,962.67,634.82,962.51C634.83,962.51,634.83,962.51,634.82,962.51L634.82,962.51z
		 M649.73,963.14c-0.09,0.47,0.02,1.36,0.22,1.8l5.13,11.13c0.26,0.56,0.56,1.21,0.11,1.91c-0.26,0.41-0.72,0.66-1.21,0.66l0,0
		c-0.86,0-1.25-0.65-1.56-1.17l-6.33-10.65l-1.72,3.49c-0.4,0.82-1.2,1.97-1.81,2.63l-3.46,3.73c-0.45,0.48-0.8,0.86-1.46,0.86
		c-0.55,0-1.05-0.32-1.29-0.82c-0.4-0.84,0.09-1.45,0.52-1.98l3.41-4.22c0.36-0.45,0.85-1.38,1.01-1.94l1.27-4.42
		c0.18-0.65,0.4-1.8,0.45-2.47l0.56-6.8c-2.76,0.91-5.46,4.52-6.38,6.03c-0.39,0.63-0.72,1.18-1.54,1.18h-0.01
		c-0.5,0-0.98-0.27-1.23-0.71c-0.42-0.72-0.11-1.28,0.25-1.93c0.21-0.38,5.31-9.37,12.19-8.83c2.97,0.26,3.92,2.49,4.55,3.97
		c0.15,0.34,0.29,0.68,0.45,0.98l3.92,7.09c0.37,0.68,0.15,1.56-0.52,1.95c-0.67,0.39-1.51,0.21-1.92-0.45l-2.92-4.66L649.73,963.14
		L649.73,963.14z M651.43,946.41c0.3,1.8-0.93,3.49-2.72,3.79c-1.8,0.3-3.49-0.92-3.79-2.72s0.92-3.49,2.72-3.79
		S651.13,944.61,651.43,946.41L651.43,946.41z" />
      <path class="st54" d="M799.94,923.23c-0.55-1.67-2.35-2.57-4.01-2.02c-1.67,0.55-2.57,2.34-2.03,4.01
		c0.55,1.67,2.35,2.57,4.01,2.02C799.58,926.7,800.49,924.9,799.94,923.23L799.94,923.23z" />
      <path class="st54" d="M792.74,939.72l3.12-6.19c0.96-1.9,0.2-4.22-1.71-5.18l-2.03-1.02c-0.11-0.06-0.22-0.09-0.34-0.12
		c-5.41-2.37-11.82-0.16-14.54,5.17c-0.41,0.81-0.09,1.8,0.72,2.21c0.81,0.41,1.8,0.09,2.21-0.71c1.57-3.07,4.86-4.68,8.1-4.27
		l-11.83,23.19c-0.42,0.82-0.09,1.81,0.72,2.23c0.24,0.12,0.5,0.18,0.75,0.18c0.6,0,1.19-0.33,1.48-0.91l7.18-14.09l3.56,1.79
		c3.84,2.09,5.32,6.88,3.3,10.77c-0.42,0.81-0.11,1.81,0.71,2.23c0.41,0.21,0.86,0.24,1.26,0.11s0.76-0.41,0.97-0.82
		C799.05,949.17,797.39,942.92,792.74,939.72L792.74,939.72z" />
      <path class="st54" d="M774.21,935.49h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.39,0.32-0.72,0.72-0.72h9.14
		c0.39,0,0.72,0.32,0.72,0.72l0,0C774.93,935.17,774.61,935.49,774.21,935.49L774.21,935.49z" />
      <path class="st54" d="M778.91,938.82h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.4,0.32-0.72,0.72-0.72h9.14
		c0.39,0,0.72,0.32,0.72,0.72l0,0C779.62,938.49,779.3,938.82,778.91,938.82L778.91,938.82z" />
      <path class="st54" d="M774.21,942.13h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.4,0.32-0.72,0.72-0.72h9.14
		c0.39,0,0.72,0.32,0.72,0.72l0,0C774.93,941.81,774.61,942.13,774.21,942.13L774.21,942.13z" />
      <path class="st54" d="M803.03,949.16c0.94,0,1.79,0.38,2.41,0.99c-0.84,1.05-1.85,2.02-3.05,2.9c-0.11-0.09-0.25-0.14-0.41-0.15
		c-0.44-1.21-0.52-2.37-0.25-3.48C802.13,949.26,802.57,949.16,803.03,949.16L803.03,949.16L803.03,949.16z" />
      <path class="st54" d="M801.41,949.57c-0.22,1.09-0.13,2.21,0.29,3.38c-0.15,0.06-0.28,0.17-0.36,0.32l-1.74-0.75
		C799.63,951.24,800.35,950.13,801.41,949.57L801.41,949.57L801.41,949.57z" />
      <path class="st54" d="M805.64,950.36c0.52,0.6,0.83,1.39,0.83,2.24c0,0.46-0.09,0.9-0.25,1.3c-1.18,0.08-2.36-0.01-3.55-0.28v-0.01
		c0-0.13-0.04-0.24-0.09-0.35C803.77,952.39,804.79,951.42,805.64,950.36L805.64,950.36L805.64,950.36z" />
      <path class="st54" d="M799.6,952.83l1.65,0.7c0,0.03-0.01,0.05-0.01,0.08c0,0.17,0.07,0.33,0.17,0.45l-0.71,1.06
		C800.07,954.55,799.66,953.74,799.6,952.83L799.6,952.83L799.6,952.83z" />
      <path class="st54" d="M801.95,953.18c0.24,0,0.43,0.19,0.43,0.43s-0.19,0.43-0.43,0.43s-0.43-0.19-0.43-0.43
		C801.53,953.37,801.72,953.18,801.95,953.18L801.95,953.18z" />
      <path class="st54" d="M802.61,953.9c1.16,0.26,2.32,0.36,3.47,0.3c-0.51,0.97-1.46,1.66-2.59,1.82c-0.5-0.56-0.83-1.2-1.02-1.91
		C802.53,954.04,802.58,953.97,802.61,953.9L802.61,953.9z" />
      <path class="st54" d="M801.63,954.25c0.1,0.05,0.21,0.08,0.32,0.08c0.1,0,0.19-0.02,0.27-0.05c0.18,0.65,0.48,1.24,0.91,1.77
		c-0.04,0-0.07,0.01-0.11,0.01c-0.8,0-1.53-0.27-2.12-0.73L801.63,954.25L801.63,954.25z" />
      <g class="st5">
        <path class="st0" d="M564.51,537.29l-3.35-4.71l2.46-1.75l8.36,11.78l-2.46,1.75l-3.73-5.25l-2.82,2l3.73,5.25l-2.46,1.75
			l-8.36-11.78l2.46-1.75l3.35,4.71L564.51,537.29z" />
      </g>
      <g class="st5">
        <path class="st0" d="M573.87,536c0.63,1.02,1.62,2.52,2.67,1.87c0.85-0.53,0.51-1.45,0.07-2.16l2.43-1.51
			c0.55,0.95,0.72,1.91,0.47,2.79c-0.23,0.88-0.89,1.71-2.01,2.41c-3.09,1.93-4.67,0.3-6.34-2.39c-1.46-2.34-2.37-4.56,0.79-6.53
			c3.22-2.01,4.88-0.15,6.51,2.66L573.87,536z M575.22,533.29c-0.52-0.83-1.22-2.04-2.36-1.33c-1.1,0.69-0.28,1.97,0.17,2.7
			L575.22,533.29z" />
      </g>
      <g class="st5">
        <path class="st0" d="M588.38,530.66c0.3,0.54,0.68,1.06,1.04,1.57l-2.29,1.28l-0.76-1.11l-0.04,0.02
			c-0.02,1.2-0.49,2.04-1.55,2.63c-1.71,0.96-3.05,0.03-3.91-1.5c-1.63-2.92,0.55-4.3,2.86-5.54l-0.38-0.68
			c-0.42-0.75-0.83-1.23-1.72-0.74c-0.86,0.48-0.56,1.16-0.17,1.86l-2.41,1.35c-0.59-1.06-0.64-1.93-0.29-2.65
			c0.32-0.73,1.04-1.34,1.98-1.87c3.12-1.75,4.28-0.63,5.18,0.98L588.38,530.66z M583.22,532.1c0.35,0.63,0.89,1.34,1.69,0.89
			c1.45-0.81,0.13-2.64-0.41-3.6C583.31,530.12,582.35,530.53,583.22,532.1z" />
      </g>
      <g class="st5">
        <path class="st0" d="M587.68,516.96l6.44,12.93l-2.52,1.26l-6.44-12.93L587.68,516.96z" />
      </g>
      <g class="st5">
        <path class="st0" d="M591.04,520.12l1.03-0.48l-0.68-1.45l2.02-2.34l1.21,2.59l1.32-0.62l0.74,1.58l-1.32,0.62l2.29,4.89
			c0.32,0.69,0.52,1.15,1.35,0.76c0.16-0.08,0.33-0.15,0.44-0.25l0.74,1.58c-0.33,0.2-0.66,0.42-1.28,0.71
			c-2.21,1.04-3.19-0.29-3.45-0.86l-2.64-5.63l-1.03,0.48L591.04,520.12z" />
      </g>
      <g class="st5">
        <path class="st0" d="M605.96,524.51l-2.73-6.41c-0.35-0.83-0.77-1.41-1.6-1.06c-0.83,0.35-0.7,1.06-0.35,1.89l2.73,6.41l-2.6,1.11
			l-5.66-13.29l2.6-1.11l2.1,4.93l0.04-0.02c0.08-0.53,0.27-0.94,0.55-1.26c0.29-0.34,0.68-0.59,1.16-0.8
			c1.23-0.53,2.63-0.25,3.18,1.04l3.18,7.45L605.96,524.51z" />
      </g>
      <g class="st5">
        <path class="st0" d="M621.48,516.85c0.19,0.59,0.47,1.17,0.72,1.74l-2.49,0.82l-0.53-1.23l-0.04,0.01
			c-0.24,1.18-0.87,1.91-2.02,2.29c-1.86,0.62-3-0.55-3.56-2.22c-1.05-3.17,1.36-4.12,3.86-4.9l-0.25-0.74
			c-0.27-0.82-0.58-1.37-1.55-1.05c-0.93,0.31-0.77,1.04-0.52,1.79l-2.62,0.87c-0.38-1.16-0.27-2.02,0.22-2.66
			c0.46-0.66,1.27-1.12,2.3-1.46c3.4-1.12,4.32,0.19,4.9,1.94L621.48,516.85z M616.15,517.29c0.23,0.68,0.62,1.48,1.49,1.19
			c1.58-0.52,0.63-2.57,0.28-3.61C616.61,515.36,615.58,515.58,616.15,517.29z" />
      </g>
      <g class="st5">
        <path class="st0" d="M624.58,508.42l0.04-0.01c0.15-0.52,0.39-0.9,0.71-1.17c0.33-0.3,0.75-0.5,1.25-0.64
			c1.29-0.36,2.64,0.09,3.02,1.44l2.17,7.8l-2.72,0.76l-1.87-6.71c-0.24-0.87-0.58-1.5-1.45-1.26c-0.87,0.24-0.83,0.96-0.59,1.83
			l1.87,6.71l-2.72,0.76l-2.71-9.73l2.72-0.76L624.58,508.42z" />
      </g>
      <g class="st5">
        <path class="st0" d="M638.87,514.18l-0.25-1.09l-0.04,0.01c-0.29,1.07-0.98,1.58-2.03,1.82c-2.85,0.65-3.47-2.54-3.93-4.56
			c-0.45-1.99-1.23-5.03,1.54-5.66c1-0.23,1.75-0.09,2.5,0.62l0.04-0.01l-1.18-5.17l2.75-0.62l3.2,14.08L638.87,514.18z
			 M637.59,509.2c-0.45-1.97-0.74-3.34-1.87-3.08c-1.19,0.27-0.86,1.63-0.41,3.6c0.56,2.48,0.97,3.47,1.97,3.25
			C638.22,512.75,638.16,511.68,637.59,509.2z" />
      </g>
      <g class="st5">
        <path class="st0" d="M648.25,512.34l-2-14.3l4.04-0.56l5.19,9.38l0.04-0.01l-1.38-9.91l2.79-0.39l2,14.3l-3.94,0.55l-5.36-9.92
			l-0.04,0.01l1.46,10.46L648.25,512.34z" />
      </g>
      <g class="st5">
        <path class="st0" d="M666.18,509.26l-0.04,0c-0.25,0.46-0.54,0.81-0.92,1.02c-0.38,0.23-0.82,0.34-1.35,0.39
			c-1.34,0.1-2.58-0.6-2.68-2l-0.63-8.08l2.81-0.22l0.54,6.98c0.07,0.9,0.28,1.54,1.18,1.47c0.9-0.07,1.01-0.74,0.94-1.64
			l-0.54-6.98l2.81-0.22l0.63,8.08c0.05,0.66,0.14,1.33,0.26,1.99l-2.91,0.23L666.18,509.26z" />
      </g>
      <g class="st5">
        <path class="st0" d="M669.88,499.92l1.14-0.03l-0.05-1.6l2.78-1.34l0.08,2.86l1.46-0.04l0.05,1.74l-1.46,0.04l0.15,5.4
			c0.02,0.76,0.02,1.26,0.94,1.24c0.18,0,0.36-0.01,0.5-0.05l0.05,1.74c-0.38,0.05-0.78,0.12-1.46,0.14
			c-2.44,0.07-2.81-1.54-2.82-2.16l-0.18-6.22l-1.14,0.03L669.88,499.92z" />
      </g>
      <g class="st5">
        <path class="st0" d="M679.5,499.73l0,1.3h0.04c0.52-1.16,1.47-1.51,2.62-1.51l0.01,2.52c-2.48-0.15-2.52,1.29-2.51,2.29l0.02,5.5
			l-2.82,0.01l-0.04-10.1L679.5,499.73z" />
      </g>
      <g class="st5">
        <path class="st0" d="M686.57,509.98l-2.82-0.09l0.34-10.1l2.82,0.09L686.57,509.98z M687.06,495.55l-0.07,2.22l-2.82-0.09
			l0.07-2.22L687.06,495.55z" />
      </g>
      <g class="st5">
        <path class="st0" d="M688.53,499.94l1.14,0.07l0.09-1.6l2.89-1.09l-0.17,2.86l1.46,0.09l-0.1,1.74l-1.46-0.09l-0.32,5.39
			c-0.04,0.76-0.09,1.26,0.82,1.31c0.18,0.01,0.36,0.02,0.5-0.01l-0.1,1.74c-0.38,0.02-0.79,0.05-1.46,0.01
			c-2.44-0.14-2.66-1.78-2.62-2.4l0.36-6.21l-1.14-0.07L688.53,499.94z" />
      </g>
      <g class="st5">
        <path class="st0" d="M697.67,510.74l-2.81-0.27l0.97-10.06l2.81,0.27L697.67,510.74z M699.06,496.37l-0.21,2.21l-2.81-0.27
			l0.21-2.21L699.06,496.37z" />
      </g>
      <g class="st5">
        <path class="st0" d="M700.63,505.8c0.37-2.74,1.08-5.02,4.77-4.52c3.69,0.5,3.77,2.89,3.4,5.63c-0.42,3.13-1.2,5.27-4.8,4.78
			C700.38,511.19,700.2,508.93,700.63,505.8z M706.02,506.36c0.28-2.08,0.32-3.15-0.87-3.31c-1.19-0.16-1.43,0.88-1.71,2.96
			c-0.41,3.05-0.24,3.74,0.79,3.88C705.26,510.04,705.61,509.42,706.02,506.36z" />
      </g>
      <g class="st5">
        <path class="st0" d="M714.51,503.95l0.04,0.01c0.36-0.4,0.75-0.63,1.16-0.74c0.43-0.12,0.9-0.12,1.41-0.02
			c1.32,0.25,2.33,1.25,2.07,2.63l-1.49,7.96l-2.77-0.52l1.28-6.84c0.17-0.88,0.14-1.6-0.75-1.77c-0.89-0.17-1.17,0.49-1.34,1.38
			l-1.28,6.84l-2.77-0.52l1.86-9.93l2.77,0.52L714.51,503.95z" />
      </g>
      <a href="https://tm-dash-dev.azurewebsites.net/child-poverty" target="_self">
        <g class="st5">
          <path class="st3" d="M843.95,580.86l3.05,4.5c1.55,2.28,0.76,4.12-1.42,5.6c-1.36,0.92-3.78,1.98-5.77-0.95l-1.26-1.85l-4.87,3.3
			l-1.7-2.5L843.95,580.86z M840.39,586.92l0.94,1.39c0.5,0.74,1.66,0.71,2.46,0.17c0.98-0.66,1.62-1.49,0.86-2.62l-0.85-1.26
			L840.39,586.92z" />
        </g>
        <g class="st5">
          <path class="st3" d="M842.4,595.23c2.38-1.41,4.61-2.27,6.51,0.93c1.9,3.2,0.07,4.75-2.3,6.16c-2.72,1.61-4.87,2.33-6.73-0.8
			C838.02,598.39,839.68,596.85,842.4,595.23z M845.3,599.81c1.81-1.07,2.67-1.7,2.06-2.73c-0.61-1.03-1.58-0.58-3.38,0.49
			c-2.65,1.57-3.08,2.13-2.55,3.03S842.65,601.38,845.3,599.81z" />
        </g>
        <g class="st5">
          <path class="st3"
            d="M851.61,601.15l1.34,2.53l-6.04,4.8l0.02,0.04l7.39-2.24l1.29,2.44l-10.23,2.27l-1.45-2.74L851.61,601.15z" />
        </g>
        <g class="st5">
          <path class="st3" d="M852.52,614.98c-1.09,0.51-2.7,1.31-2.17,2.43c0.43,0.91,1.38,0.68,2.14,0.32l1.21,2.59
			c-1.01,0.43-1.98,0.49-2.83,0.14c-0.84-0.33-1.59-1.09-2.15-2.28c-1.55-3.3,0.26-4.67,3.12-6.02c2.5-1.17,4.81-1.81,6.39,1.56
			c1.61,3.44-0.44,4.87-3.41,6.15L852.52,614.98z M855.05,616.65c0.89-0.42,2.17-0.97,1.6-2.19c-0.55-1.18-1.92-0.51-2.7-0.15
			L855.05,616.65z" />
        </g>
        <g class="st5">
          <path class="st3" d="M861.8,622.29l-1.2,0.49l0.02,0.04c1.27,0.04,1.95,0.8,2.38,1.85l-2.33,0.96c-0.8-2.35-2.14-1.84-3.07-1.46
			l-5.09,2.1l-1.07-2.61l9.34-3.85L861.8,622.29z" />
        </g>
        <g class="st5">
          <path class="st3" d="M862.96,625.15l0.41,1.06l1.49-0.57l2.19,2.18l-2.67,1.03l0.52,1.36l-1.63,0.62l-0.52-1.36l-5.04,1.94
			c-0.71,0.27-1.18,0.43-0.85,1.29c0.07,0.17,0.13,0.34,0.22,0.45l-1.62,0.62c-0.17-0.34-0.37-0.69-0.62-1.33
			c-0.88-2.28,0.52-3.16,1.1-3.38l5.81-2.23l-0.41-1.06L862.96,625.15z" />
        </g>
        <g class="st5">
          <path class="st3" d="M856.42,636.77l8.74-5.9l0.91,2.65l-6.25,3.67l0.01,0.04l7.21-0.87l0.88,2.57l-14.44,0.84l-0.96-2.8
			L856.42,636.77z" />
        </g>
      </a>
      <g class="st5">
        <path class="st1" d="M479.38,636.39l13.76,4.4l-2.29,7.14l-2.11-0.68l1.37-4.27l-3.53-1.13l-1.3,4.08l-2.11-0.68l1.31-4.08
			l-6-1.92L479.38,636.39z" />
      </g>
      <g class="st5">
        <path class="st1" d="M476.45,652.66c-0.6-0.17-1.24-0.26-1.85-0.37l0.71-2.52l1.32,0.25l0.01-0.04c-0.84-0.86-1.1-1.78-0.77-2.96
			c0.53-1.89,2.13-2.19,3.83-1.71c3.22,0.9,2.65,3.42,1.91,5.94l0.75,0.21c0.83,0.23,1.46,0.28,1.73-0.7
			c0.26-0.94-0.43-1.22-1.2-1.44l0.75-2.66c1.17,0.33,1.82,0.91,2.09,1.67c0.29,0.75,0.21,1.68-0.08,2.72
			c-0.97,3.45-2.57,3.48-4.34,2.98L476.45,652.66z M479.07,647.99c-0.69-0.19-1.57-0.32-1.82,0.57c-0.45,1.6,1.78,1.95,2.84,2.25
			C480.41,649.45,480.8,648.48,479.07,647.99z" />
      </g>
      <g class="st5">
        <path class="st1" d="M482.4,658.88l-0.01,0.04c0.76,0.74,0.92,1.55,0.69,2.58c-0.21,0.98-0.85,1.66-1.73,1.94
			c0.72,0.83,0.94,1.7,0.7,2.83c-0.28,1.31-1.31,2.3-2.68,2l-7.92-1.71l0.59-2.76l6.81,1.46c0.88,0.19,1.6,0.18,1.79-0.7
			s-0.46-1.18-1.34-1.37l-6.81-1.47l0.58-2.7l6.81,1.46c0.88,0.19,1.6,0.18,1.79-0.7c0.19-0.88-0.46-1.18-1.34-1.37l-6.81-1.46
			l0.59-2.76l9.88,2.13l-0.59,2.76L482.4,658.88z" />
      </g>
      <g class="st5">
        <path class="st1" d="M470.77,671.6l0.42-2.79l9.99,1.51l-0.42,2.79L470.77,671.6z M485.05,673.77l-2.2-0.33l0.42-2.79l2.2,0.33
			L485.05,673.77z" />
      </g>
      <g class="st5">
        <path class="st1" d="M484.35,678.92l-14.33-1.81l0.35-2.8l14.33,1.81L484.35,678.92z" />
      </g>
      <g class="st5">
        <path class="st1" d="M469.46,681.38l10.38-1.84l-0.25,2.79l-7.2,0.81l0,0.04l6.94,2.14l-0.24,2.71l-13.53-5.11l0.26-2.95
			L469.46,681.38z" />
      </g>
      <g class="st5">
        <path class="st1" d="M468.74,693.02l14.44,0.36l-0.2,7.88l-2.22-0.06l0.12-4.86l-3.56-0.09l-0.11,4.48l-2.22-0.05l0.11-4.48
			l-4.22-0.11l-0.12,5.02l-2.22-0.05L468.74,693.02z" />
      </g>
      <g class="st5">
        <path class="st1" d="M477.76,705.46l0,0.04c0.47,0.27,0.78,0.6,0.97,0.98c0.21,0.39,0.3,0.85,0.32,1.37
			c0.04,1.34-0.73,2.54-2.13,2.58l-8.1,0.21l-0.07-2.82l6.96-0.18c0.9-0.02,1.6-0.2,1.57-1.1c-0.02-0.9-0.73-1.04-1.63-1.02
			l-6.96,0.18l-0.07-2.82l10.1-0.26l0.07,2.82L477.76,705.46z" />
      </g>
      <g class="st5">
        <path class="st1"
          d="M478.97,711.13l0.22,2.85l-7.45,2l0,0.04l7.67,0.89l0.21,2.75l-10.29-1.99l-0.24-3.09L478.97,711.13z" />
      </g>
      <g class="st5">
        <path class="st1" d="M470.11,724.76l-0.33-2.8l10.03-1.17l0.33,2.8L470.11,724.76z M484.46,723.09l-2.21,0.26l-0.33-2.8l2.21-0.26
			L484.46,723.09z" />
      </g>
      <g class="st5">
        <path class="st1" d="M480.82,728.34l-1.29,0.2l0.01,0.04c1.23,0.33,1.71,1.23,1.89,2.36l-2.49,0.39
			c-0.22-2.48-1.65-2.29-2.64-2.14l-5.43,0.85l-0.44-2.79l9.98-1.56L480.82,728.34z" />
      </g>
      <g class="st5">
        <path class="st1" d="M476.46,732.58c2.71-0.53,5.1-0.6,5.82,3.06c0.72,3.65-1.52,4.5-4.23,5.03c-3.1,0.61-5.37,0.57-6.07-3.01
			S473.36,733.19,476.46,732.58z M477.67,737.86c2.06-0.41,3.08-0.71,2.85-1.89s-1.29-1.07-3.35-0.67c-3.02,0.59-3.62,0.98-3.42,2
			C473.95,738.33,474.65,738.46,477.67,737.86z" />
      </g>
      <g class="st5">
        <path class="st1" d="M482.91,744.14l0.01,0.04c0.51,0.16,0.89,0.42,1.16,0.74c0.29,0.34,0.48,0.77,0.61,1.27
			c0.33,1.3-0.16,2.64-1.52,2.98l-7.86,1.98l-0.69-2.74l6.75-1.7c0.87-0.22,1.51-0.55,1.29-1.42c-0.22-0.87-0.94-0.86-1.81-0.64
			l-6.75,1.7l-0.69-2.74l9.8-2.46l0.69,2.74L482.91,744.14z" />
      </g>
      <g class="st5">
        <path class="st1" d="M485.25,753.03l0.01,0.04c1.03,0.26,1.57,0.88,1.89,1.89c0.31,0.95,0.1,1.86-0.53,2.54
			c1.04,0.36,1.67,1,2.02,2.1c0.41,1.28,0.01,2.65-1.32,3.08l-7.71,2.49l-0.87-2.68l6.63-2.14c0.86-0.28,1.47-0.64,1.2-1.5
			c-0.28-0.86-0.99-0.79-1.85-0.52l-6.62,2.14l-0.85-2.63l6.62-2.14c0.86-0.28,1.47-0.64,1.2-1.5c-0.28-0.86-0.99-0.79-1.85-0.52
			l-6.62,2.14l-0.87-2.68l9.61-3.1l0.87,2.69L485.25,753.03z" />
      </g>
      <g class="st5">
        <path class="st1" d="M485.58,767.83c-1.12,0.43-2.79,1.11-2.35,2.27c0.36,0.93,1.32,0.78,2.11,0.48l1.02,2.67
			c-1.04,0.36-2.01,0.34-2.83-0.07c-0.82-0.4-1.51-1.2-1.98-2.44c-1.3-3.4,0.61-4.64,3.56-5.77c2.58-0.98,4.93-1.45,6.25,2.03
			c1.35,3.55-0.79,4.82-3.86,5.88L485.58,767.83z M487.98,769.68c0.92-0.35,2.24-0.81,1.76-2.06c-0.46-1.21-1.88-0.66-2.68-0.35
			L487.98,769.68z" />
      </g>
      <g class="st5">
        <path class="st1" d="M493.45,775.26l0.02,0.04c0.53,0.07,0.95,0.26,1.26,0.53c0.34,0.28,0.6,0.67,0.81,1.15
			c0.54,1.23,0.29,2.63-0.99,3.2l-7.41,3.28l-1.14-2.58l6.37-2.82c0.82-0.36,1.4-0.79,1.03-1.62s-1.07-0.69-1.89-0.32l-6.37,2.82
			l-1.14-2.58l9.24-4.09l1.14,2.58L493.45,775.26z" />
      </g>
      <g class="st5">
        <path class="st1" d="M496.73,779.98l0.5,1.02l1.44-0.71l2.37,1.98l-2.57,1.26l0.64,1.31l-1.56,0.77l-0.64-1.31l-4.85,2.38
			c-0.68,0.33-1.14,0.54-0.74,1.36c0.08,0.16,0.16,0.32,0.26,0.43l-1.56,0.77c-0.2-0.32-0.43-0.66-0.73-1.27
			c-1.07-2.19,0.24-3.19,0.8-3.47l5.58-2.74l-0.5-1.02L496.73,779.98z" />
      </g>
      <g class="st5">
        <path class="st1" d="M498.17,800.04c-0.54,0.31-1.05,0.7-1.56,1.06l-1.31-2.27l1.1-0.77l-0.02-0.04c-1.2,0-2.04-0.46-2.65-1.52
			c-0.98-1.7-0.07-3.05,1.46-3.93c2.9-1.66,4.3,0.51,5.57,2.8l0.68-0.39c0.75-0.43,1.22-0.84,0.72-1.73
			c-0.49-0.85-1.17-0.55-1.86-0.15l-1.38-2.39c1.06-0.61,1.92-0.67,2.65-0.32c0.74,0.31,1.35,1.02,1.89,1.96
			c1.78,3.11,0.68,4.27-0.92,5.19L498.17,800.04z M496.67,794.91c-0.62,0.36-1.33,0.9-0.87,1.7c0.83,1.44,2.64,0.1,3.59-0.45
			C498.65,794.97,498.23,794.01,496.67,794.91z" />
      </g>
      <g class="st5">
        <path class="st1" d="M506.94,800.42l0.02,0.03c0.54-0.01,0.97,0.11,1.33,0.33c0.39,0.23,0.7,0.57,0.98,1.01
			c0.73,1.13,0.69,2.55-0.48,3.31l-6.81,4.39l-1.53-2.37l5.85-3.77c0.76-0.49,1.26-1,0.77-1.76c-0.49-0.76-1.16-0.51-1.92-0.02
			l-5.85,3.77l-1.53-2.37l8.49-5.48l1.53,2.37L506.94,800.42z" />
      </g>
      <g class="st5">
        <path class="st1" d="M506.21,815.42l0.91-0.65l-0.02-0.03c-1.1,0.15-1.83-0.28-2.46-1.16c-1.71-2.37,0.98-4.18,2.67-5.4
			c1.66-1.19,4.16-3.09,5.82-0.79c0.6,0.83,0.76,1.57,0.4,2.54l0.02,0.03l4.3-3.1l1.65,2.29l-11.72,8.44L506.21,815.42z
			 M510.3,812.31c1.64-1.18,2.79-1.98,2.11-2.93c-0.71-0.99-1.84-0.16-3.48,1.03c-2.06,1.49-2.82,2.25-2.22,3.08
			C507.28,814.27,508.24,813.79,510.3,812.31z" />
      </g>
      <g class="st5">
        <path class="st1" d="M523.07,813.69l3.51,4.16c1.78,2.11,1.19,4.02-0.83,5.72c-1.25,1.06-3.55,2.37-5.83-0.34l-1.44-1.71
			l-4.5,3.79l-1.95-2.31L523.07,813.69z M520.17,820.08l1.08,1.29c0.58,0.69,1.73,0.53,2.46-0.09c0.9-0.76,1.46-1.65,0.58-2.69
			l-0.98-1.16L520.17,820.08z" />
      </g>
      <g class="st5">
        <path class="st1" d="M528.4,826.36l-0.95,0.89l0.03,0.03c1.2-0.41,2.11,0.06,2.89,0.89l-1.84,1.72c-1.58-1.92-2.66-0.97-3.39-0.29
			l-4.02,3.75l-1.92-2.06l7.38-6.89L528.4,826.36z" />
      </g>
      <g class="st5">
        <path class="st1" d="M527.23,832.31c1.95-1.96,3.89-3.35,6.53-0.73c2.64,2.62,1.26,4.58-0.69,6.54c-2.23,2.24-4.13,3.48-6.72,0.91
			S525.01,834.55,527.23,832.31z M531.19,836.01c1.48-1.49,2.16-2.31,1.31-3.16s-1.67-0.16-3.15,1.33
			c-2.17,2.19-2.45,2.84-1.71,3.57C528.37,838.48,529.02,838.2,531.19,836.01z" />
      </g>
      <g class="st5">
        <path class="st1" d="M536.94,834.92l0.84,0.77l1.08-1.18l2.93,0.98l-1.94,2.1l1.07,0.99l-1.18,1.28l-1.07-0.99l-3.66,3.97
			c-0.52,0.56-0.87,0.91-0.19,1.54c0.13,0.12,0.26,0.25,0.39,0.31l-1.18,1.28c-0.31-0.23-0.64-0.46-1.14-0.92
			c-1.79-1.65-0.93-3.06-0.51-3.52l4.22-4.57l-0.84-0.77L536.94,834.92z" />
      </g>
      <g class="st5">
        <path class="st1" d="M539.97,845.01c-0.77,0.92-1.89,2.33-0.94,3.12c0.77,0.64,1.54,0.03,2.07-0.61l2.2,1.83
			c-0.74,0.82-1.59,1.28-2.51,1.32c-0.9,0.05-1.9-0.31-2.92-1.16c-2.79-2.33-1.74-4.35,0.28-6.77c1.77-2.12,3.59-3.68,6.44-1.29
			c2.92,2.44,1.66,4.59-0.49,7.02L539.97,845.01z M542.97,845.45c0.63-0.75,1.56-1.8,0.53-2.66c-1-0.83-1.96,0.35-2.51,1.01
			L542.97,845.45z" />
      </g>
      <g class="st5">
        <path class="st1" d="M550.75,851.18c0.9-1.2,0.9-1.83,0.2-2.36c-0.96-0.72-1.68,0.06-2.94,1.74c-1.86,2.46-2.04,3.14-1.21,3.77
			c0.7,0.53,1.52,0.14,2.31-0.91l2.25,1.7c-1.65,2.19-3.54,2.24-5.65,0.65c-2.91-2.19-1.95-4.26-0.05-6.78
			c1.66-2.2,3.4-3.85,6.37-1.61c2.08,1.57,2.56,3.38,0.97,5.49L550.75,851.18z" />
      </g>
      <g class="st5">
        <path class="st1" d="M555.59,850.3l0.93,0.65l0.92-1.31l3.03,0.58l-1.64,2.34l1.2,0.84l-1,1.43l-1.2-0.84l-3.09,4.43
			c-0.44,0.62-0.74,1.02,0.02,1.55c0.15,0.1,0.3,0.21,0.43,0.25l-1,1.43c-0.33-0.19-0.7-0.37-1.25-0.75c-2-1.4-1.33-2.91-0.98-3.42
			l3.56-5.1l-0.93-0.65L555.59,850.3z" />
      </g>
      <g class="st5">
        <path class="st1" d="M557.87,864.09l-2.35-1.56l5.58-8.42l2.35,1.56L557.87,864.09z M565.86,852.05l-1.23,1.85l-2.35-1.56
			l1.23-1.85L565.86,852.05z" />
      </g>
      <g class="st5">
        <path class="st1" d="M562.47,860.91c1.44-2.35,3.02-4.16,6.19-2.21c3.17,1.94,2.28,4.17,0.84,6.52c-1.65,2.7-3.22,4.34-6.33,2.44
			C560.07,865.75,560.82,863.6,562.47,860.91z M567.18,863.6c1.1-1.79,1.57-2.75,0.54-3.38s-1.66,0.23-2.76,2.02
			c-1.61,2.63-1.73,3.33-0.84,3.87C565,866.66,565.57,866.23,567.18,863.6z" />
      </g>
      <g class="st5">
        <path class="st1" d="M575.29,863.92l0.04,0.02c0.46-0.27,0.9-0.38,1.33-0.36c0.45,0.01,0.89,0.16,1.35,0.4
			c1.18,0.63,1.85,1.89,1.19,3.13l-3.81,7.15l-2.49-1.33l3.27-6.14c0.42-0.79,0.61-1.49-0.18-1.91c-0.79-0.42-1.26,0.12-1.69,0.91
			l-3.27,6.14l-2.49-1.33l4.75-8.92l2.49,1.33L575.29,863.92z" />
      </g>
      <g class="st5">
        <path class="st4" d="M636.39,894.51l2.09-14.29l7.8,1.14l-0.32,2.2l-4.81-0.7l-0.52,3.52l4.43,0.65l-0.32,2.2l-4.43-0.65
			l-0.61,4.18l4.97,0.73l-0.32,2.2L636.39,894.51z" />
      </g>
      <g class="st5">
        <path class="st4" d="M651.18,896.41l0.11-1.11l-0.04,0c-0.61,0.92-1.42,1.19-2.5,1.08c-2.91-0.29-2.49-3.5-2.29-5.57
			c0.2-2.03,0.42-5.16,3.25-4.89c1.02,0.1,1.68,0.47,2.18,1.38l0.04,0l0.52-5.28l2.81,0.27l-1.41,14.37L651.18,896.41z
			 M651.54,891.28c0.2-2.01,0.35-3.4-0.8-3.52c-1.21-0.12-1.33,1.28-1.53,3.29c-0.25,2.53-0.17,3.6,0.84,3.7
			C651.01,894.84,651.3,893.81,651.54,891.28z" />
      </g>
      <g class="st5">
        <path class="st4" d="M661.09,896.07l-0.04,0c-0.3,0.43-0.64,0.73-1.05,0.89c-0.41,0.18-0.85,0.24-1.39,0.21
			c-1.34-0.07-2.48-0.92-2.41-2.32l0.4-8.09l2.82,0.14l-0.35,6.99c-0.04,0.9,0.08,1.57,0.98,1.61s1.09-0.61,1.14-1.51l0.35-6.99
			l2.82,0.14l-0.4,8.09c-0.03,0.66-0.03,1.34,0,2l-2.92-0.15L661.09,896.07z" />
      </g>
      <g class="st5">
        <path class="st4" d="M671.41,891c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.31,3.16c-0.01,3.08,0.25,3.74,1.29,3.74
			c0.88,0,1.3-0.8,1.3-2.12l2.82,0c-0.01,2.74-1.49,3.92-4.13,3.91c-3.64-0.01-4.12-2.23-4.11-5.39c0.01-2.76,0.41-5.12,4.13-5.11
			c2.6,0,4.08,1.17,4.07,3.81L671.41,891z" />
      </g>
      <g class="st5">
        <path class="st4" d="M683.67,895.09c0.03,0.62,0.14,1.26,0.23,1.87l-2.62,0.12l-0.18-1.33l-0.04,0c-0.55,1.07-1.35,1.6-2.57,1.66
			c-1.96,0.09-2.75-1.34-2.83-3.09c-0.15-3.34,2.42-3.6,5.04-3.68l-0.04-0.78c-0.04-0.86-0.19-1.47-1.21-1.43
			c-0.98,0.04-1.02,0.79-0.99,1.59l-2.76,0.13c-0.06-1.22,0.29-2.02,0.92-2.51c0.62-0.51,1.53-0.73,2.61-0.78
			c3.58-0.17,4.11,1.35,4.19,3.19L683.67,895.09z M678.42,894.07c0.03,0.72,0.19,1.59,1.11,1.55c1.66-0.08,1.29-2.3,1.24-3.4
			C679.38,892.35,678.33,892.27,678.42,894.07z" />
      </g>
      <g class="st5">
        <path class="st4" d="M684.13,886.83l1.14-0.09l-0.13-1.59l2.71-1.49l0.24,2.85l1.46-0.12l0.14,1.74l-1.46,0.12l0.44,5.38
			c0.06,0.76,0.08,1.26,1,1.18c0.18-0.01,0.36-0.03,0.5-0.08l0.14,1.73c-0.38,0.07-0.77,0.16-1.45,0.22c-2.43,0.2-2.88-1.39-2.94-2
			l-0.51-6.2l-1.14,0.09L684.13,886.83z" />
      </g>
      <g class="st5">
        <path class="st4" d="M693.14,881.65l0.24,2.21l-2.8,0.3l-0.24-2.21L693.14,881.65z M694.68,896.01l-2.8,0.3l-1.07-10.04l2.8-0.3
			L694.68,896.01z" />
      </g>
      <g class="st5">
        <path class="st4" d="M696.18,890.66c-0.39-2.73-0.33-5.13,3.35-5.66c3.68-0.53,4.42,1.75,4.81,4.48c0.45,3.13,0.29,5.39-3.31,5.91
			C697.42,895.91,696.63,893.78,696.18,890.66z M701.52,889.73c-0.3-2.08-0.55-3.11-1.74-2.94c-1.19,0.17-1.14,1.24-0.84,3.31
			c0.44,3.05,0.79,3.67,1.82,3.52C701.8,893.46,701.96,892.77,701.52,889.73z" />
      </g>
      <g class="st5">
        <path class="st4" d="M708.1,884.84l0.04-0.01c0.19-0.5,0.46-0.86,0.8-1.11c0.36-0.27,0.79-0.44,1.3-0.54
			c1.32-0.25,2.63,0.31,2.89,1.68l1.54,7.95l-2.77,0.54l-1.32-6.83c-0.17-0.88-0.46-1.54-1.35-1.37c-0.88,0.17-0.91,0.89-0.74,1.77
			l1.32,6.83l-2.77,0.54l-1.92-9.92l2.77-0.54L708.1,884.84z" />
      </g>
      <g class="st5">
        <path class="st2" d="M774.91,853.85l4.58-2.93c2.33-1.49,4.14-0.65,5.56,1.57c0.88,1.38,1.88,3.83-1.1,5.74l-1.89,1.21l3.17,4.95
			l-2.54,1.63L774.91,853.85z M780.87,857.57l1.42-0.91c0.76-0.49,0.75-1.65,0.23-2.45c-0.64-1-1.44-1.67-2.59-0.93l-1.28,0.82
			L780.87,857.57z" />
      </g>
      <g class="st5">
        <path class="st2" d="M797.04,854.09c0.36,0.51,0.79,0.98,1.2,1.45l-2.14,1.52l-0.87-1.02l-0.03,0.02c0.11,1.2-0.27,2.08-1.26,2.78
			c-1.6,1.13-3.03,0.36-4.05-1.08c-1.93-2.72,0.09-4.33,2.25-5.82l-0.45-0.64c-0.5-0.7-0.95-1.14-1.79-0.55
			c-0.8,0.57-0.44,1.22,0.03,1.87l-2.25,1.6c-0.71-1-0.85-1.85-0.58-2.61c0.24-0.76,0.89-1.44,1.77-2.07
			c2.92-2.07,4.19-1.08,5.25,0.42L797.04,854.09z M792.07,856.07c0.42,0.59,1.02,1.24,1.77,0.7c1.35-0.96-0.15-2.64-0.79-3.54
			C791.95,854.1,791.03,854.6,792.07,856.07z" />
      </g>
      <g class="st5">
        <path class="st2" d="M795.98,844.56l0.79,1.03l0.03-0.02c-0.29-1.24,0.26-2.09,1.17-2.78l1.53,2c-2.07,1.38-1.22,2.55-0.62,3.34
			l3.34,4.37l-2.24,1.71l-6.14-8.02L795.98,844.56z" />
      </g>
      <g class="st5">
        <path class="st2" d="M797.96,843.06l0.88-0.72l-1.02-1.23l1.38-2.77l1.82,2.21l1.13-0.93l1.11,1.34l-1.13,0.93l3.43,4.17
			c0.48,0.59,0.79,0.99,1.5,0.4c0.14-0.11,0.28-0.23,0.36-0.35l1.11,1.34c-0.27,0.27-0.54,0.57-1.06,1
			c-1.88,1.55-3.16,0.5-3.55,0.03l-3.96-4.8l-0.88,0.72L797.96,843.06z" />
      </g>
      <g class="st5">
        <path class="st2" d="M802.42,833.67l1.45,1.68l-2.13,1.85l-1.45-1.68L802.42,833.67z M811.87,844.6l-2.13,1.84l-6.61-7.64
			l2.13-1.85L811.87,844.6z" />
      </g>
      <g class="st5">
        <path class="st2" d="M813.1,834.7c-1.02-1.1-1.64-1.21-2.29-0.61c-0.88,0.82-0.23,1.66,1.2,3.2c2.1,2.26,2.74,2.56,3.5,1.85
			c0.64-0.6,0.41-1.47-0.49-2.44l2.07-1.92c1.87,2.01,1.58,3.88-0.35,5.68c-2.67,2.48-4.53,1.18-6.68-1.14
			c-1.88-2.02-3.19-4.02-0.47-6.56c1.91-1.77,3.78-1.93,5.58,0.01L813.1,834.7z" />
      </g>
      <g class="st5">
        <path class="st2" d="M812.99,823.71l1.57,1.57l-2,1.99l-1.57-1.57L812.99,823.71z M823.2,833.93l-2,1.99l-7.14-7.15l2-1.99
			L823.2,833.93z" />
      </g>
      <g class="st5">
        <path class="st2" d="M819.4,823.32l0.82,0.76l0.03-0.03c-0.36-1.05-0.08-1.85,0.66-2.64c1.99-2.14,4.29,0.15,5.82,1.57
			c1.49,1.39,3.84,3.48,1.91,5.55c-0.7,0.75-1.39,1.05-2.42,0.89l-0.03,0.03l3.88,3.62l-1.92,2.06l-10.56-9.85L819.4,823.32z
			 M824.72,824.89c-1.48-1.38-2.49-2.35-3.32-1.46c-0.79,0.85,0.25,1.79,1.72,3.17c1.86,1.73,2.76,2.32,3.41,1.62
			C827.23,827.48,826.58,826.62,824.72,824.89z" />
      </g>
      <g class="st5">
        <path class="st2" d="M835.25,817.74c0.47,0.4,1.01,0.75,1.53,1.11l-1.69,2l-1.1-0.78l-0.03,0.03c0.41,1.13,0.26,2.08-0.53,3.01
			c-1.27,1.5-2.85,1.1-4.19-0.04c-2.55-2.16-0.99-4.22,0.74-6.19l-0.6-0.5c-0.66-0.56-1.21-0.87-1.87-0.09
			c-0.63,0.75-0.12,1.29,0.49,1.8l-1.78,2.11c-0.93-0.79-1.28-1.58-1.21-2.38c0.05-0.8,0.51-1.62,1.21-2.44
			c2.31-2.73,3.79-2.09,5.19-0.9L835.25,817.74z M830.93,820.9c0.55,0.47,1.3,0.94,1.89,0.24c1.07-1.27-0.8-2.52-1.64-3.23
			C830.32,819.02,829.56,819.73,830.93,820.9z" />
      </g>
      <g class="st5">
        <path class="st2" d="M829.48,811.75l0.71-0.9l-1.26-0.99l0.76-3l2.25,1.77l0.9-1.15l1.37,1.08l-0.9,1.15l4.24,3.34
			c0.6,0.47,0.98,0.8,1.55,0.07c0.11-0.14,0.22-0.28,0.28-0.42l1.37,1.08c-0.2,0.32-0.4,0.67-0.83,1.21
			c-1.51,1.92-2.98,1.16-3.47,0.78l-4.89-3.85l-0.71,0.9L829.48,811.75z" />
      </g>
      <g class="st5">
        <path class="st2" d="M831.69,801.71l1.79,1.31l-1.67,2.28l-1.79-1.31L831.69,801.71z M843.34,810.25l-1.67,2.28l-8.15-5.97
			l1.67-2.28L843.34,810.25z" />
      </g>
      <g class="st5">
        <path class="st2" d="M840.44,805.55c-2.28-1.55-4.01-3.21-1.92-6.29c2.09-3.08,4.27-2.08,6.55-0.53c2.61,1.78,4.18,3.42,2.14,6.43
			C845.16,808.18,843.05,807.33,840.44,805.55z M843.35,800.98c-1.74-1.18-2.67-1.69-3.35-0.7c-0.67,0.99,0.15,1.67,1.88,2.85
			c2.55,1.73,3.24,1.88,3.83,1.02C846.3,803.29,845.9,802.71,843.35,800.98z" />
      </g>
      <g class="st5">
        <path class="st2" d="M844.17,792.82l0.02-0.03c-0.25-0.48-0.32-0.92-0.28-1.34c0.04-0.45,0.21-0.88,0.48-1.32
			c0.7-1.14,2-1.73,3.19-1l6.91,4.23l-1.47,2.41l-5.94-3.63c-0.77-0.47-1.45-0.7-1.92,0.07c-0.47,0.77,0.04,1.27,0.81,1.74
			l5.94,3.63l-1.47,2.41l-8.62-5.27l1.47-2.41L844.17,792.82z" />
      </g>
      <g class="st5">
        <path class="st2" d="M859.68,779.89c0.55,0.29,1.16,0.51,1.73,0.74l-1.21,2.33l-1.25-0.51l-0.02,0.04
			c0.65,1.01,0.71,1.97,0.15,3.05c-0.9,1.74-2.53,1.71-4.09,0.9c-2.97-1.54-1.9-3.89-0.66-6.2l-0.69-0.36
			c-0.76-0.4-1.37-0.57-1.84,0.33c-0.45,0.87,0.17,1.28,0.88,1.65l-1.27,2.45c-1.08-0.56-1.6-1.26-1.71-2.05
			c-0.13-0.79,0.13-1.69,0.63-2.65c1.65-3.18,3.23-2.88,4.86-2.03L859.68,779.89z M856.17,783.93c0.64,0.33,1.48,0.63,1.9-0.19
			c0.76-1.47-1.35-2.27-2.32-2.78C855.15,782.23,854.57,783.1,856.17,783.93z" />
      </g>
      <g class="st5">
        <path class="st2" d="M855.33,772.31l0.02-0.04c-0.3-0.45-0.43-0.88-0.44-1.3c-0.01-0.45,0.11-0.9,0.32-1.37
			c0.56-1.22,1.78-1.96,3.05-1.37l7.36,3.38l-1.18,2.56l-6.33-2.9c-0.82-0.38-1.52-0.52-1.9,0.3s0.19,1.26,1.01,1.63l6.33,2.9
			l-1.18,2.56l-9.18-4.21l1.18-2.56L855.33,772.31z" />
      </g>
      <g class="st5">
        <path class="st2" d="M868.44,764.88l-1.04-0.42l-0.02,0.04c0.72,0.85,0.74,1.7,0.34,2.7c-1.09,2.71-4.06,1.41-5.99,0.63
			c-1.89-0.76-4.84-1.86-3.78-4.49c0.38-0.95,0.92-1.48,1.94-1.7l0.01-0.04l-4.92-1.98l1.05-2.62l13.4,5.39L868.44,764.88z
			 M863.61,763.1c-1.88-0.75-3.17-1.29-3.6-0.22c-0.46,1.13,0.85,1.63,2.73,2.39c2.36,0.95,3.41,1.18,3.79,0.23
			C866.89,764.61,865.97,764.04,863.61,763.1z" />
      </g>
      <g class="st5">
        <path class="st2" d="M864.87,753.89c-3.64-1.16-7.11-2.27-5.59-7.02c0.94-2.94,2.94-3.6,5.85-2.54l-0.9,2.82
			c-1.83-0.58-2.62-0.48-2.89,0.38c-0.52,1.62,0.94,2.32,4.46,3.44s5.12,1.41,5.63-0.21c0.43-1.33-1.31-1.83-2.38-2.21l0.91-2.84
			c3.68,1.18,4.39,3.02,3.53,5.71C871.98,756.17,868.47,755.04,864.87,753.89z" />
      </g>
      <g class="st5">
        <path class="st2" d="M861.95,738.62l2.14,0.6l-0.76,2.72l-2.14-0.6L861.95,738.62z M875.86,742.52l-0.76,2.72l-9.73-2.73
			l0.76-2.72L875.86,742.52z" />
      </g>
      <g class="st5">
        <path class="st2"
          d="M866.44,738.67l0.67-2.78l7.7,0.4l0.01-0.04l-7.02-3.22l0.65-2.68l9.17,5.07l-0.73,3.01L866.44,738.67z" />
      </g>
      <g class="st5">
        <path class="st2" d="M864.91,725.58l2.18,0.44l-0.56,2.76l-2.18-0.44L864.91,725.58z M879.07,728.45l-0.56,2.76l-9.9-2.01
			l0.56-2.76L879.07,728.45z" />
      </g>
      <g class="st5">
        <path class="st2" d="M865.78,720.63l14.25,2.34l-0.46,2.78l-14.25-2.34L865.78,720.63z" />
      </g>
      <g class="st5">
        <path class="st2" d="M881.38,713.03l-0.3,3l-14.37-1.45l0.56-5.55c0.21-2.05,1.65-3.23,4.1-2.98c1.83,0.18,3.13,1.04,3.25,3.02
			l0.04,0c0.14-0.65,0.5-2.58,3.09-2.32c0.92,0.09,3.63,0.31,4.25,0.09l-0.3,2.95c-0.92,0.31-1.88,0.13-2.82,0.04
			c-1.71-0.17-3.15-0.48-3.38,1.83l-0.08,0.78L881.38,713.03z M873.22,712.21l0.13-1.33c0.12-1.19-1.04-1.65-1.96-1.75
			c-1.37-0.14-1.95,0.39-2.04,1.34l-0.13,1.33L873.22,712.21z" />
      </g>
      <g class="st5">
        <path class="st2" d="M867.87,701.08l2.22,0.14l-0.18,2.81l-2.22-0.14L867.87,701.08z M882.29,701.98l-0.18,2.81l-10.08-0.63
			l0.18-2.81L882.29,701.98z" />
      </g>
      <g class="st5">
        <path class="st2" d="M872.52,691.53l10.52,0.26c0.7,0.02,3.46,0.05,3.37,3.93c-0.05,2.1-0.64,3.89-3.1,3.88l0.07-2.76
			c0.42,0.01,0.78-0.04,1.03-0.21c0.26-0.17,0.41-0.49,0.42-0.93c0.02-0.7-0.63-1.06-1.65-1.08l-1.94-0.05l0,0.04
			c0.77,0.44,1.15,1.25,1.13,2.17c-0.08,3.1-2.91,2.89-5.19,2.83c-2.22-0.05-5.04-0.17-4.96-3.1c0.02-1,0.49-1.85,1.43-2.23l0-0.04
			l-1.18-0.03L872.52,691.53z M880.64,695.72c0.03-1.02-1.03-1.19-3.17-1.24c-2.22-0.05-3.48,0.01-3.51,1.05
			c-0.03,1.06,0.71,1.26,3.79,1.33C878.69,696.89,880.6,697.08,880.64,695.72z" />
      </g>
      <g class="st5">
        <path class="st2" d="M882.43,684.54l-6.96,0.18c-0.9,0.02-1.6,0.2-1.57,1.1c0.02,0.9,0.73,1.04,1.63,1.02l6.96-0.18l0.07,2.82
			l-14.44,0.38l-0.07-2.82l5.36-0.14l0-0.04c-0.47-0.27-0.78-0.6-0.97-0.98c-0.21-0.39-0.3-0.85-0.31-1.37
			c-0.04-1.34,0.73-2.54,2.13-2.58l8.1-0.21L882.43,684.54z" />
      </g>
      <g class="st5">
        <path class="st2" d="M872.2,681.42l-0.09-1.14l-1.59,0.12l-1.47-2.72l2.85-0.22l-0.11-1.46l1.74-0.13l0.11,1.46l5.38-0.42
			c0.76-0.06,1.26-0.08,1.19-1c-0.01-0.18-0.03-0.36-0.08-0.5l1.74-0.13c0.07,0.38,0.16,0.77,0.21,1.45
			c0.19,2.43-1.4,2.88-2.02,2.93l-6.2,0.48l0.09,1.14L872.2,681.42z" />
      </g>
      <g class="st5">
        <path class="st2" d="M878.29,672.07c0.46-0.03,0.89-0.09,1.2-0.26c0.3-0.19,0.43-0.51,0.37-1.06c-0.06-0.56-0.46-1-1.14-0.93
			c-2.13,0.22-1.14,5.11-4.35,5.44c-2.17,0.22-3.05-1.86-3.23-3.67c-0.2-1.91,0.54-3.74,2.72-3.8l0.29,2.75
			c-0.7,0.07-1.11,0.2-1.27,0.41c-0.16,0.2-0.18,0.44-0.14,0.74c0.06,0.62,0.5,0.91,1.17,0.84c1.59-0.16,1-5.09,4.22-5.42
			c1.75-0.18,3.21,1.12,3.45,3.44c0.25,2.45-0.19,4.14-3.02,4.27L878.29,672.07z" />
      </g>
      <path class="st54" d="M917.92,782.65c-0.64-1.22-1.1-2.53-1.39-3.93c-0.16-0.79-0.93-1.3-1.72-1.14s-1.3,0.93-1.14,1.72
		c0.4,1.93,1.08,3.73,2.03,5.36C916.21,783.77,916.99,783.06,917.92,782.65L917.92,782.65z" />
      <path class="st54" d="M928.16,790.34c-1.4-0.29-2.72-0.76-3.94-1.4c-0.42,0.94-1.13,1.72-2.02,2.23c1.64,0.95,3.45,1.64,5.38,2.04
		c0.1,0.02,0.2,0.03,0.29,0.03c0.68,0,1.29-0.48,1.43-1.17C929.46,791.28,928.95,790.5,928.16,790.34L928.16,790.34z" />
      <path class="st54" d="M934.13,761.12c1.39,0.28,2.71,0.75,3.92,1.39c0.42-0.94,1.14-1.71,2.03-2.22c-1.64-0.94-3.45-1.63-5.37-2.03
		c-0.79-0.16-1.56,0.35-1.72,1.14C932.83,760.19,933.33,760.96,934.13,761.12L934.13,761.12z" />
      <path class="st54"
        d="M944.35,768.82c0.64,1.22,1.12,2.54,1.4,3.93c0.14,0.69,0.75,1.17,1.43,1.17c0.09,0,0.19-0.01,0.29-0.03
		c0.79-0.16,1.3-0.93,1.14-1.71c-0.39-1.93-1.09-3.74-2.04-5.39C946.07,767.68,945.29,768.39,944.35,768.82L944.35,768.82z" />
      <path class="st54"
        d="M914.81,773.89c0.1,0.02,0.2,0.03,0.29,0.03c0.68,0,1.28-0.47,1.43-1.17c0.28-1.39,0.75-2.69,1.37-3.9
		c-0.94-0.41-1.73-1.11-2.24-1.98c-0.93,1.62-1.61,3.41-1.99,5.31C913.51,772.96,914.02,773.73,914.81,773.89L914.81,773.89z" />
      <path class="st54" d="M924.16,762.55c1.23-0.66,2.58-1.14,4-1.43c0.79-0.16,1.3-0.93,1.14-1.72s-0.93-1.3-1.72-1.14
		c-1.94,0.39-3.77,1.1-5.42,2.05C923.04,760.82,923.75,761.61,924.16,762.55L924.16,762.55z" />
      <path class="st54" d="M938.05,788.96c-1.21,0.63-2.53,1.1-3.92,1.39c-0.8,0.16-1.3,0.93-1.15,1.72c0.15,0.69,0.75,1.17,1.43,1.17
		c0.09,0,0.2-0.01,0.29-0.03c1.93-0.39,3.74-1.09,5.37-2.03C939.19,790.67,938.46,789.9,938.05,788.96L938.05,788.96z" />
      <path class="st54" d="M947.47,777.58c-0.79-0.16-1.56,0.35-1.72,1.14c-0.28,1.39-0.76,2.71-1.4,3.93c0.94,0.42,1.72,1.13,2.23,2.03
		c0.95-1.64,1.64-3.45,2.04-5.39C948.77,778.51,948.26,777.74,947.47,777.58L947.47,777.58z" />
      <path class="st54" d="M918.66,767.57c0.35,0.13,0.73,0.2,1.13,0.2c1.83,0,3.31-1.49,3.31-3.32c0-0.41-0.07-0.79-0.2-1.15
		c-0.36-0.99-1.17-1.75-2.2-2.04c-0.28-0.08-0.59-0.12-0.91-0.12c-1.83,0-3.32,1.48-3.32,3.31c0,0.33,0.05,0.64,0.14,0.94
		C916.91,766.41,917.67,767.22,918.66,767.57L918.66,767.57z" />
      <path class="st54" d="M939.09,764.45c0,1.83,1.49,3.32,3.32,3.32c0.42,0,0.83-0.08,1.2-0.23c0.99-0.38,1.74-1.21,2.01-2.25
		c0.07-0.27,0.11-0.55,0.11-0.85c0-1.83-1.48-3.31-3.31-3.31c-0.3,0-0.58,0.04-0.85,0.11c-1.03,0.28-1.86,1.03-2.24,2.01
		C939.17,763.63,939.09,764.03,939.09,764.45L939.09,764.45z" />
      <path class="st54" d="M923.17,787.02c0-1.83-1.49-3.32-3.32-3.32c-0.42,0-0.81,0.07-1.17,0.22c-0.99,0.37-1.74,1.2-2.02,2.23
		c-0.07,0.28-0.12,0.57-0.12,0.88c0,1.83,1.48,3.31,3.31,3.31c0.3,0,0.59-0.04,0.87-0.12c1.03-0.28,1.86-1.03,2.23-2.01
		C923.09,787.83,923.17,787.43,923.17,787.02L923.17,787.02z" />
      <path class="st54" d="M943.61,783.92c-0.37-0.15-0.77-0.23-1.2-0.23c-1.83,0-3.32,1.49-3.32,3.32c0,0.42,0.08,0.82,0.23,1.2
		c0.38,0.98,1.21,1.73,2.24,2.01c0.27,0.07,0.55,0.11,0.85,0.11c1.83,0,3.31-1.48,3.31-3.31c0-0.29-0.04-0.58-0.11-0.85
		C945.34,785.13,944.59,784.3,943.61,783.92L943.61,783.92z" />
      <path class="st54" d="M931.13,781.57c-3.09,0-5.62-2.42-5.82-5.46l0.62,0.71c0.22,0.25,0.52,0.37,0.82,0.37
		c0.26,0,0.51-0.09,0.72-0.27c0.46-0.4,0.5-1.09,0.1-1.55l-2.56-2.92c-0.21-0.24-0.51-0.37-0.82-0.37s-0.62,0.14-0.82,0.37
		l-2.56,2.92c-0.4,0.46-0.35,1.15,0.1,1.55c0.46,0.4,1.15,0.35,1.54-0.1l0.66-0.75c0.18,4.27,3.7,7.69,8.01,7.69
		c0.6,0,1.09-0.49,1.09-1.09C932.22,782.06,931.73,781.57,931.13,781.57L931.13,781.57z" />
      <path class="st54" d="M931.13,769.9c3.09,0,5.62,2.42,5.82,5.46l-0.62-0.71c-0.4-0.46-1.09-0.5-1.55-0.1
		c-0.45,0.4-0.5,1.09-0.1,1.55l2.56,2.92c0.21,0.24,0.51,0.37,0.82,0.37c0.32,0,0.62-0.14,0.82-0.37l2.56-2.92
		c0.4-0.46,0.35-1.15-0.1-1.54c-0.45-0.4-1.15-0.35-1.55,0.1l-0.66,0.75c-0.18-4.27-3.7-7.69-8.01-7.69c-0.61,0-1.1,0.49-1.1,1.1
		C930.03,769.4,930.52,769.9,931.13,769.9L931.13,769.9z" />
      <g class="st5">
        <path class="st55" d="M517.52,116.5c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64
			c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1
			C517.52,123.97,517.52,120.29,517.52,116.5z" />
        <path class="st55" d="M533.58,123.73v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-14.44h2.82v5.36h0.04
			c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1H533.58z" />
        <path class="st55" d="M541.7,109.28v2.22h-2.82v-2.22H541.7z M541.7,123.73h-2.82v-10.1h2.82V123.73z" />
        <path class="st55" d="M547.26,109.28v14.44h-2.82v-14.44H547.26z" />
        <path class="st55" d="M554.8,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32
			c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H554.8z M554.66,118.59c0-2.02,0.02-3.42-1.14-3.42
			c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C554.48,122.19,554.66,121.13,554.66,118.59z" />
        <path class="st55" d="M567.3,123.73h-3.02v-14.44h5.58c2.06,0,3.38,1.32,3.38,3.78c0,1.84-0.72,3.22-2.68,3.54v0.04
			c0.66,0.08,2.62,0.24,2.62,2.84c0,0.92,0.06,3.64,0.34,4.24h-2.96c-0.4-0.88-0.32-1.86-0.32-2.8c0-1.72,0.16-3.18-2.16-3.18h-0.78
			V123.73z M567.3,115.52h1.34c1.2,0,1.54-1.2,1.54-2.12c0-1.38-0.58-1.9-1.54-1.9h-1.34V115.52z" />
        <path class="st55" d="M578.38,109.28v2.22h-2.82v-2.22H578.38z M578.38,123.73h-2.82v-10.1h2.82V123.73z" />
        <path class="st55" d="M588.6,113.62v10.52c0,0.7,0.04,3.46-3.84,3.46c-2.1,0-3.9-0.54-3.96-3h2.76c0,0.42,0.06,0.78,0.24,1.02
			c0.18,0.26,0.5,0.4,0.94,0.4c0.7,0,1.04-0.66,1.04-1.68v-1.94h-0.04c-0.42,0.78-1.22,1.18-2.14,1.18c-3.1,0-2.96-2.84-2.96-5.12
			c0-2.22,0.04-5.04,2.98-5.04c1,0,1.86,0.44,2.26,1.38h0.04v-1.18H588.6z M584.62,121.85c1.02,0,1.16-1.06,1.16-3.2
			c0-2.22-0.1-3.48-1.14-3.48c-1.06,0-1.24,0.74-1.24,3.82C583.4,119.93,583.26,121.85,584.62,121.85z" />
        <path class="st55" d="M595.82,123.73v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-14.44h2.82v5.36h0.04
			c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1H595.82z" />
        <path class="st55" d="M599.74,113.62h1.14v-1.6l2.82-1.26v2.86h1.46v1.74h-1.46v5.4c0,0.76-0.02,1.26,0.9,1.26
			c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V113.62z" />
        <path class="st55" d="M608.66,120.49c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H608.66z" />
        <path class="st55" d="M619.92,123.73v-14.44h3.02v12.04h4.52v2.4H619.92z" />
        <path class="st55" d="M636.3,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54
			c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76
			c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M631.1,120.59
			c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C632.14,118.91,631.1,118.79,631.1,120.59z" />
        <path class="st55" d="M641.46,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1
			h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z" />
        <path class="st55" d="M653.68,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32
			c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H653.68z M653.54,118.59c0-2.02,0.02-3.42-1.14-3.42
			c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C653.36,122.19,653.54,121.13,653.54,118.59z" />
        <path class="st55" d="M660.86,120.49c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H660.86z" />
        <path class="st55" d="M672.66,117.23c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.3,3.16c0,3.08,0.26,3.74,1.3,3.74
			c0.88,0,1.3-0.8,1.3-2.12h2.82c0,2.74-1.48,3.92-4.12,3.92c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12
			c2.6,0,4.08,1.16,4.08,3.8H672.66z" />
        <path class="st55" d="M685.18,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54
			c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76
			c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M679.98,120.59
			c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C681.02,118.91,679.98,118.79,679.98,120.59z" />
        <path class="st55" d="M690.2,113.62v1.12h0.04c0.52-0.98,1.3-1.32,2.38-1.32c2.92,0,2.82,3.24,2.82,5.32
			c0,2.04,0.08,5.18-2.76,5.18c-1.02,0-1.72-0.3-2.3-1.16h-0.04v5.3h-2.82v-14.44H690.2z M692.68,118.59c0-2.02,0.02-3.42-1.2-3.42
			c-1.16,0-1.14,1.4-1.14,3.42c0,2.54,0.18,3.6,1.14,3.6C692.5,122.19,692.68,121.13,692.68,118.59z" />
        <path class="st55" d="M700.12,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62
			c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H700.12z
			 M702.7,117.54c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H702.7z" />
        <path class="st55" d="M719.62,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54
			c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76
			c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M714.42,120.59
			c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C715.46,118.91,714.42,118.79,714.42,120.59z" />
        <path class="st55" d="M724.78,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1
			h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z" />
        <path class="st55" d="M737,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32
			c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H737z M736.86,118.59c0-2.02,0.02-3.42-1.14-3.42
			c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C736.68,122.19,736.86,121.13,736.86,118.59z" />
        <path class="st55" d="M753.14,113.72c0.02-1.34-0.2-2.52-1.8-2.52c-1.88,0-1.88,2.54-1.88,5.34c0,4.52,0.44,5.32,2.16,5.32
			c0.5,0,1.04-0.12,1.5-0.28v-3.2h-1.64v-2.22h4.66v7.32c-0.82,0.16-2.88,0.48-4.08,0.48c-5.08,0-5.66-2.1-5.66-7.58
			c0-3.64,0.18-7.34,5.12-7.34c2.96,0,4.8,1.66,4.62,4.68H753.14z" />
        <path class="st55" d="M758.38,118.55c0-2.76,0.4-5.12,4.12-5.12c3.72,0,4.12,2.36,4.12,5.12c0,3.16-0.48,5.38-4.12,5.38
			C758.86,123.93,758.38,121.71,758.38,118.55z M763.8,118.39c0-2.1-0.1-3.16-1.3-3.16c-1.2,0-1.3,1.06-1.3,3.16
			c0,3.08,0.26,3.74,1.3,3.74C763.54,122.13,763.8,121.47,763.8,118.39z" />
        <path class="st55" d="M767.66,113.62h2.86l1.42,7.58h0.04l1.48-7.58h2.76l-2.78,10.1h-3.1L767.66,113.62z" />
        <path class="st55" d="M780.1,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62
			c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H780.1z
			 M782.68,117.54c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H782.68z" />
        <path class="st55" d="M790.18,113.62v1.3h0.04c0.52-1.16,1.48-1.5,2.62-1.5v2.52c-2.48-0.16-2.52,1.28-2.52,2.28v5.5h-2.82v-10.1
			H790.18z" />
        <path class="st55" d="M796.98,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1
			h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z" />
        <path class="st55" d="M811.82,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54
			c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76
			c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M806.62,120.59
			c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C807.66,118.91,806.62,118.79,806.62,120.59z" />
        <path class="st55" d="M816.98,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1
			h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z" />
        <path class="st55" d="M829.3,117.23c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.3,3.16c0,3.08,0.26,3.74,1.3,3.74
			c0.88,0,1.3-0.8,1.3-2.12h2.82c0,2.74-1.48,3.92-4.12,3.92c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12
			c2.6,0,4.08,1.16,4.08,3.8H829.3z" />
        <path class="st55" d="M836.76,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62
			c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H836.76z
			 M839.34,117.54c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H839.34z" />
      </g>
      <g class="st5">
        <path class="st55" d="M30.99,276.62h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24
			c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V276.62z M32.65,288.18h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6
			h-2.18V288.18z" />
        <path class="st55" d="M43.23,285.56c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H43.23z M46.78,284.44
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H46.78z" />
        <path class="st55" d="M55.26,289.62v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33
			v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17
			c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91H59.8v-6.3c0-0.92-0.25-1.76-1.44-1.76
			c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H55.26z" />
        <path class="st55" d="M63.54,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C65.07,289.8,63.54,289.23,63.54,285.21z M68.9,284.58c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C68.53,288.6,68.9,287.54,68.9,284.58z" />
        <path class="st55" d="M77.6,280.53h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M75.87,281.58c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C77.63,283.68,77.72,281.58,75.87,281.58z" />
        <path class="st55" d="M83.32,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z" />
        <path class="st55" d="M92.46,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83
			c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38
			c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M89.13,286.92c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49
			C91.02,285.12,89.13,285,89.13,286.92z" />
        <path class="st55" d="M98.39,281.61h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V281.61z M101.9,284.93c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C101.68,288.6,101.9,287.36,101.9,284.93z" />
        <path class="st55" d="M110.72,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H110.72z" />
        <path class="st55" d="M114.66,276.62h1.66v1.58h-1.66V276.62z M116.22,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M123.53,283.45c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H123.53z" />
        <path class="st55" d="M130.46,289.8c-1.96,0-3.19-0.86-3.13-2.95H129c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C133.63,289.03,132.26,289.8,130.46,289.8z" />
      </g>
      <path class="st56" d="M25.02,276.3c-4.35,0.61-7.75,2.51-8.74,4.92" />
      <line class="st57" x1="16" y1="285.48" x2="16" y2="303.74" />
      <path class="st56" d="M17.07,307.86c1.69,2.04,5.23,3.52,9.44,3.81" />
      <line class="st58" x1="30.94" y1="311.72" x2="135.63" y2="311.72" />
      <path class="st56" d="M140.08,311.52c4.35-0.61,7.74-2.51,8.73-4.92" />
      <line class="st57" x1="149.11" y1="302.34" x2="149.11" y2="284.08" />
      <path class="st56" d="M148.04,279.96c-1.69-2.04-5.23-3.52-9.44-3.81" />
      <line class="st58" x1="134.16" y1="276.1" x2="29.47" y2="276.1" />
      <path class="st59" d="M16,282.67L16,282.67 M16,305.15L16,305.15 M28,311.72L28,311.72 M137.11,311.72L137.11,311.72
		 M149.11,305.15L149.11,305.15 M149.11,282.67L149.11,282.67 M137.11,276.1L137.11,276.1 M28,276.1L28,276.1" />
      <path class="st55" d="M71.65,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.89-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87
		C59.63,230.08,65.33,234.81,71.65,234.48L71.65,234.48z" />
      <path class="st54" d="M98.41,205.04l-3.28-2.31l-7.82,11.12l-6.18-4.66l-5.36,7.27c-0.26,0.35-0.66,0.54-1.07,0.54
		c-0.28,0-0.55-0.08-0.79-0.26c-0.59-0.44-0.72-1.27-0.28-1.86l6.95-9.43l6.13,4.62l6.23-8.87l-3.23-2.27l9.63-4.47L98.41,205.04
		L98.41,205.04z M70.42,182.02c-0.93,0-1.68,0.75-1.68,1.68s0.75,1.68,1.68,1.68s1.68-0.75,1.68-1.68S71.35,182.02,70.42,182.02
		L70.42,182.02z M70.22,195.21l-0.34,6.2c0,0.22-0.18,0.4-0.4,0.4s-0.39-0.18-0.39-0.4l-0.34-6.2h-1.1l1.14-6.96l-2.29,4.55
		c-0.08,0.2-0.32,0.3-0.52,0.21s-0.29-0.32-0.21-0.52c0,0,1.68-4.53,2.09-5.37c0.41-0.84,0.82-1.35,2.39-1.35h0.32
		c1.57,0,1.98,0.51,2.39,1.35c0.42,0.84,2.09,5.37,2.09,5.37c0.09,0.2-0.01,0.43-0.21,0.52c-0.2,0.09-0.43-0.01-0.52-0.21
		l-2.28-4.55l1.13,6.96h-1.1l-0.34,6.2c0,0.22-0.18,0.4-0.39,0.4c-0.22,0-0.39-0.18-0.39-0.4l-0.36-6.2H70.22L70.22,195.21z
		 M85.69,183.69c0,0.93-0.75,1.68-1.68,1.68s-1.69-0.75-1.69-1.68s0.75-1.68,1.69-1.68C84.94,182.01,85.69,182.76,85.69,183.69
		L85.69,183.69z M85.75,191.91l0.33,9.2c0.02,0.36-0.25,0.68-0.61,0.7c-0.02,0-0.03,0-0.05,0c-0.34,0-0.64-0.26-0.66-0.61
		l-0.75-7.11l-0.75,7.11c-0.03,0.35-0.32,0.61-0.66,0.61c-0.01,0-0.03,0-0.05,0c-0.36-0.03-0.64-0.34-0.61-0.7l0.32-9.2l-0.11-3.66
		l-2.05,4.55c-0.08,0.2-0.32,0.3-0.52,0.21s-0.29-0.32-0.21-0.52c0,0,1.45-4.52,1.86-5.37c0.41-0.84,1.05-1.35,2.62-1.35h0.32
		c1.57,0,2.21,0.51,2.62,1.35c0.41,0.84,1.86,5.37,1.86,5.37c0.09,0.2-0.01,0.43-0.21,0.52c-0.2,0.08-0.43-0.01-0.52-0.21
		l-2.05-4.55L85.75,191.91L85.75,191.91L85.75,191.91z M78.25,193.27c0,0.57-0.46,1.03-1.03,1.03s-1.03-0.46-1.03-1.03
		c0-0.57,0.46-1.03,1.03-1.03C77.78,192.23,78.25,192.69,78.25,193.27L78.25,193.27z M77.21,198.31l-0.46,3.23
		c-0.06,0.16-0.21,0.27-0.39,0.27c-0.19,0-0.34-0.12-0.4-0.29c0-0.01-0.02-0.2,0-0.23l0.19-3.97l-0.06-1.36
		c-0.05-0.46-0.06-0.33-0.59-0.64c-0.54-0.32-1.45-1.74-1.5-1.81c-0.04-0.07-0.13-0.2-0.14-0.28c-0.03-0.14,0.07-0.28,0.21-0.31
		c0.11-0.02,0.2,0.04,0.26,0.11c0.07,0.08,1.13,1.48,1.91,1.61c0.18-0.03,0.37-0.12,0.87-0.12h0.2c0.5,0,0.69,0.09,0.87,0.12
		c0.79-0.13,1.84-1.54,1.91-1.61c0.07-0.07,0.16-0.13,0.26-0.11c0.14,0.03,0.24,0.16,0.21,0.31c-0.02,0.08-0.1,0.2-0.14,0.28
		c-0.04,0.07-0.96,1.48-1.5,1.81c-0.53,0.31-0.53,0.18-0.59,0.64l-0.06,1.36l0.19,3.97c0.01,0.03,0,0.22,0,0.23
		c-0.06,0.17-0.21,0.29-0.4,0.29c-0.18,0-0.33-0.11-0.39-0.27C77.68,201.54,77.21,198.31,77.21,198.31" />
      <line class="st60" x1="82.55" y1="244.49" x2="82.55" y2="260.77" />
      <path class="st61" d="M82.55,241.53L82.55,241.53 M82.55,262.25L82.55,262.25" />
      <path d="M82.55,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C79.77,243.06,81.02,244.31,82.55,244.31L82.55,244.31z" />
      <g class="st5">
        <path class="st55" d="M372.92,289.62h-1.55v-13h2.68l3.28,10.91h0.04l3.31-10.91h2.74v13h-1.66v-11.56h-0.04l-3.64,11.56h-1.57
			l-3.56-11.56h-0.04V289.62z" />
        <path class="st55" d="M386.05,276.62h1.66v1.58h-1.66V276.62z M387.62,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M394.98,280.53h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M393.26,281.58c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C395.02,283.68,395.11,281.58,393.26,281.58z" />
        <path class="st55" d="M400.71,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z" />
        <path class="st55" d="M409.85,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M406.52,286.92c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C408.41,285.12,406.52,285,406.52,286.92z" />
        <path class="st55"
          d="M414.33,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H414.33z" />
        <path class="st55" d="M419.05,276.62h1.66v1.58h-1.66V276.62z M420.61,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M422.92,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C424.45,289.8,422.92,289.23,422.92,285.21z M428.28,284.58c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C427.91,288.6,428.28,287.54,428.28,284.58z" />
        <path class="st55" d="M437.1,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H437.1z" />
        <path class="st55" d="M449.85,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M446.52,286.92c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C448.41,285.12,446.52,285,446.52,286.92z" />
        <path class="st55" d="M459.1,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H459.1z" />
        <path class="st55" d="M467.97,276.62h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V276.62z M466.26,281.56c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C467.97,283.5,467.9,281.56,466.26,281.56z" />
      </g>
      <g class="st5">
        <path class="st55" d="M377.99,298.23h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V298.23z M376.28,303.16c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C377.99,305.1,377.92,303.16,376.28,303.16z" />
        <path class="st55" d="M382.06,298.23h1.66v1.58h-1.66V298.23z M383.63,311.23h-1.48v-9.09h1.48V311.23z" />
        <path class="st55" d="M388.87,311.41c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C392.03,310.63,390.67,311.41,388.87,311.41z" />
        <path class="st55" d="M395.78,303.21h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V303.21z M399.29,306.53c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C399.07,310.2,399.29,308.96,399.29,306.53z" />
        <path class="st55" d="M404.61,311.23h-1.48v-13h1.48V311.23z" />
        <path class="st55" d="M411.85,309.91h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V309.91z M408.52,308.53c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C410.41,306.73,408.52,306.6,408.52,308.53z" />
        <path class="st55" d="M420.92,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H420.92z" />
        <path class="st55" d="M426.61,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H426.61z M430.16,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H430.16z" />
        <path class="st55" d="M438.64,311.23v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H438.64z" />
        <path class="st55" d="M448.61,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H448.61z M452.15,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H452.15z" />
        <path class="st55" d="M461.1,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H461.1z" />
        <path class="st55"
          d="M465.33,302.13v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H465.33z" />
      </g>
      <path class="st62" d="M363.28,276.5c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="354.39" y1="291" x2="354.39" y2="298.27" />
      <path class="st62" d="M354.8,302.83c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="369.34" y1="311.72" x2="474.02" y2="311.72" />
      <path class="st62" d="M478.61,311.32c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="487.5" y1="296.82" x2="487.5" y2="289.55" />
      <path class="st62" d="M487.09,284.99c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="472.55" y1="276.1" x2="367.86" y2="276.1" />
      <path class="st59"
        d="M354.39,288.1L354.39,288.1 M354.39,299.72L354.39,299.72 M366.39,311.72L366.39,311.72 M475.5,311.72
		L475.5,311.72 M487.5,299.72L487.5,299.72 M487.5,288.1L487.5,288.1 M475.5,276.1L475.5,276.1 M366.39,276.1L366.39,276.1" />
      <a href="https://tm-dash-dev.azurewebsites.net/child-rights#migration" target="_self">
        <path class="st55" d="M410.04,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.2,6.9-11.2,13.9l6.37,44.87
		C398.02,230.08,403.72,234.81,410.04,234.48L410.04,234.48z" />
      </a>
      <path class="st54" d="M425.26,187.08c-0.51-1.56-2.19-2.41-3.76-1.9c-1.56,0.51-2.41,2.2-1.9,3.76s2.2,2.41,3.76,1.9
		C424.92,190.32,425.77,188.64,425.26,187.08L425.26,187.08z" />
      <path class="st54" d="M418.52,202.52l2.92-5.79c0.9-1.78,0.18-3.95-1.6-4.85l-1.9-0.96c-0.1-0.05-0.21-0.09-0.32-0.11
		c-5.06-2.22-11.06-0.15-13.61,4.84c-0.39,0.76-0.09,1.68,0.67,2.07c0.76,0.39,1.68,0.09,2.07-0.67c1.47-2.87,4.55-4.38,7.59-4
		l-11.07,21.71c-0.39,0.76-0.09,1.7,0.68,2.09c0.22,0.11,0.47,0.17,0.7,0.17c0.57,0,1.11-0.31,1.39-0.85l6.73-13.19l3.33,1.68
		c3.59,1.95,4.98,6.44,3.09,10.09c-0.39,0.76-0.1,1.7,0.66,2.09c0.38,0.2,0.8,0.22,1.18,0.1s0.71-0.38,0.91-0.77
		C424.42,211.36,422.87,205.51,418.52,202.52L418.52,202.52z" />
      <path class="st54" d="M438.46,198.67l-5.17-5.17c-0.45-0.45-1.18-0.45-1.63,0s-0.45,1.18,0,1.63l3.24,3.23h-9.86
		c-0.62,0-1.11,0.5-1.11,1.12s0.5,1.12,1.11,1.12h9.86l-3.24,3.24c-0.45,0.45-0.45,1.18,0,1.63c0.23,0.23,0.52,0.34,0.82,0.34
		c0.29,0,0.59-0.11,0.82-0.34l5.17-5.17c0.22-0.22,0.34-0.51,0.34-0.82S438.67,198.89,438.46,198.67L438.46,198.67z" />
      <path class="st54" d="M428.01,202.84c-0.62,0-1.12,0.5-1.12,1.12v3.72c0,0.62,0.5,1.12,1.12,1.12s1.11-0.5,1.11-1.12v-3.72
		C429.13,203.34,428.63,202.84,428.01,202.84L428.01,202.84z" />
      <path class="st54" d="M428.01,196.14c0.62,0,1.11-0.5,1.11-1.12v-3.72c0-0.62-0.5-1.12-1.11-1.12c-0.62,0-1.12,0.5-1.12,1.12v3.72
		C426.89,195.64,427.39,196.14,428.01,196.14L428.01,196.14z" />
      <path class="st54" d="M428.01,187.96c0.62,0,1.11-0.5,1.11-1.11v-3.72c0-0.62-0.5-1.11-1.11-1.11c-0.62,0-1.12,0.5-1.12,1.11v3.72
		C426.89,187.46,427.39,187.96,428.01,187.96L428.01,187.96z" />
      <path class="st54" d="M428.01,211.02c-0.62,0-1.12,0.5-1.12,1.11v3.72c0,0.62,0.5,1.12,1.12,1.12s1.11-0.5,1.11-1.12v-3.72
		C429.13,211.52,428.63,211.02,428.01,211.02L428.01,211.02z" />
      <line class="st60" x1="420.94" y1="244.49" x2="420.94" y2="260.77" />
      <path class="st61" d="M420.94,241.53L420.94,241.53 M420.94,262.25L420.94,262.25" />
      <path d="M420.94,244.31c1.54,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C418.17,243.06,419.41,244.31,420.94,244.31L420.94,244.31z" />
      <g class="st5">
        <path class="st55" d="M223.86,289.62v-13h3.85c1.75,0,3.62,0.65,3.62,3.71c0,2.95-2.3,3.57-3.64,3.57h-2.18v5.73H223.86z
			 M225.52,282.46h1.82c0.68,0,2.3-0.18,2.3-2.21c0-1.98-1.48-2.18-1.84-2.18h-2.29V282.46z" />
        <path class="st55" d="M233.24,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C234.77,289.8,233.24,289.23,233.24,285.21z M238.61,284.58c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C238.23,288.6,238.61,287.54,238.61,284.58z" />
        <path class="st55" d="M243.93,289.62h-1.48v-13h1.48V289.62z" />
        <path class="st55" d="M246.36,276.62h1.66v1.58h-1.66V276.62z M247.93,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55"
          d="M250.65,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H250.65z" />
        <path class="st55" d="M255.36,276.62h1.66v1.58h-1.66V276.62z M256.93,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M264.24,283.45c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H264.24z" />
        <path class="st55" d="M273.16,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M269.83,286.92c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C271.72,285.12,269.83,285,269.83,286.92z" />
        <path class="st55" d="M278.92,289.62h-1.48v-13h1.48V289.62z" />
      </g>
      <g class="st5">
        <path class="st55" d="M220.93,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H220.93z M224.48,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H224.48z" />
        <path class="st55" d="M233.25,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H233.25z" />
        <path class="st55" d="M237.24,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C238.77,311.41,237.24,310.83,237.24,306.82z M242.61,306.19c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C242.23,310.2,242.61,309.14,242.61,306.19z" />
        <path class="st55" d="M251.43,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H251.43z" />
        <path class="st55" d="M255.24,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C256.77,311.41,255.24,310.83,255.24,306.82z M260.61,306.19c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C260.23,310.2,260.61,309.14,260.61,306.19z" />
        <path class="st55" d="M268.96,311.23v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H268.96z" />
        <path class="st55"
          d="M280.22,309.53h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L280.22,309.53z" />
      </g>
      <path class="st62" d="M194.09,276.5c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="185.19" y1="291" x2="185.19" y2="298.27" />
      <path class="st62" d="M185.6,302.83c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="200.14" y1="311.72" x2="304.83" y2="311.72" />
      <path class="st62" d="M309.41,311.32c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="318.3" y1="296.82" x2="318.3" y2="289.55" />
      <path class="st62" d="M317.9,284.99c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="303.36" y1="276.1" x2="198.67" y2="276.1" />
      <path class="st59"
        d="M185.19,288.1L185.19,288.1 M185.19,299.72L185.19,299.72 M197.19,311.72L197.19,311.72 M306.3,311.72
		L306.3,311.72 M318.3,299.72L318.3,299.72 M318.3,288.1L318.3,288.1 M306.3,276.1L306.3,276.1 M197.19,276.1L197.19,276.1" />
      <path class="st55" d="M240.85,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.96-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87
		C228.83,230.08,234.52,234.81,240.85,234.48L240.85,234.48z" />
      <line class="st60" x1="251.75" y1="244.49" x2="251.75" y2="260.77" />
      <path class="st61" d="M251.75,241.53L251.75,241.53 M251.75,262.25L251.75,262.25" />
      <path d="M251.75,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C248.97,243.06,250.21,244.31,251.75,244.31L251.75,244.31z" />
      <path class="st54" d="M268.15,214.82h-32.81c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h32.81c0.6,0,1.09-0.49,1.09-1.09
		S268.76,214.82,268.15,214.82L268.15,214.82z" />
      <path class="st54" d="M238.26,213.36h26.98c0.61,0,1.09-0.49,1.09-1.09s-0.49-1.09-1.09-1.09h-26.98c-0.6,0-1.09,0.49-1.09,1.09
		S237.65,213.36,238.26,213.36L238.26,213.36z" />
      <polygon class="st54" points="244.46,209.72 244.46,194.41 241.54,194.41 241.54,209.72 	" />
      <polygon class="st54" points="250.29,209.72 250.29,194.41 247.37,194.41 247.37,209.72 	" />
      <polygon class="st54" points="256.12,209.72 256.12,194.41 253.21,194.41 253.21,209.72 	" />
      <polygon class="st54" points="261.96,209.72 261.96,194.41 259.04,194.41 259.04,209.72 	" />
      <path class="st54" d="M240.08,192.95h23.33c0.8,0,1.46-0.65,1.46-1.46c0-0.81-0.65-1.46-1.46-1.46h-10.94v-2.19h6.56v-4.38h-6.56
		v-0.36c0-0.6-0.49-1.09-1.09-1.09s-1.09,0.49-1.09,1.09v6.93h-10.21c-0.8,0-1.46,0.65-1.46,1.46
		C238.62,192.29,239.28,192.95,240.08,192.95L240.08,192.95z" />
      <g class="st5">
        <path class="st55" d="M708.46,292.66v-13h3.85c1.75,0,3.62,0.65,3.62,3.71c0,2.95-2.3,3.57-3.64,3.57h-2.18v5.73H708.46z
			 M710.12,285.5h1.82c0.68,0,2.3-0.18,2.3-2.21c0-1.98-1.48-2.18-1.84-2.18h-2.29V285.5z" />
        <path class="st55" d="M722.96,283.57h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V283.57z" />
        <path class="st55" d="M728.7,292.66h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88
			c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V292.66z M730.35,291.64c1.85,0,1.85-1.98,1.85-3.35
			c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C728.7,289.13,728.53,291.64,730.35,291.64z" />
        <path class="st55" d="M737.53,292.66h-1.48v-13h1.48V292.66z" />
        <path class="st55" d="M739.96,279.66h1.66v1.58h-1.66V279.66z M741.53,292.66h-1.48v-9.09h1.48V292.66z" />
        <path class="st55" d="M748.84,286.49c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H748.84z" />
        <path class="st55" d="M759.76,292.84c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C762.93,292.07,761.56,292.84,759.76,292.84z" />
        <path class="st55" d="M766.67,284.65h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V284.65z M770.19,287.96c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C769.97,291.64,770.19,290.4,770.19,287.96z" />
        <path class="st55" d="M775.51,288.59c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H775.51z M779.06,287.48
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H779.06z" />
        <path class="st55" d="M788.01,292.66v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H788.01z" />
        <path class="st55" d="M796.88,279.66h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V279.66z M795.17,284.6c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C796.88,286.54,796.81,284.6,795.17,284.6z" />
        <path class="st55" d="M800.95,279.66h1.66v1.58h-1.66V279.66z M802.51,292.66h-1.48v-9.09h1.48V292.66z" />
        <path class="st55" d="M810,292.66v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H810z" />
        <path class="st55" d="M818.88,283.57h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V283.57z M817.15,284.62c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C818.91,286.72,819,284.62,817.15,284.62z" />
      </g>
      <g class="st5">
        <path class="st55" d="M724.33,309.85c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C725.86,314.45,724.33,313.87,724.33,309.85z M729.7,309.22c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C729.32,313.24,729.7,312.18,729.7,309.22z" />
        <path class="st55" d="M738.52,314.27v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H738.52z" />
        <path class="st55" d="M751.33,308.09c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H751.33z" />
        <path class="st55" d="M760.51,314.27v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H760.51z" />
        <path class="st55" d="M764.46,301.27h1.66v1.58h-1.66V301.27z M766.02,314.27h-1.48v-9.09h1.48V314.27z" />
        <path class="st55" d="M770.02,314.27h-1.48v-13h1.48V314.27z" />
        <path class="st55" d="M777.38,301.27h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V301.27z M775.67,306.2c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C777.38,308.14,777.31,306.2,775.67,306.2z" />
        <path class="st55" d="M783.1,306.54h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V306.54z" />
        <path class="st55" d="M789.01,310.2c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H789.01z M792.55,309.08
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H792.55z" />
        <path class="st55" d="M801.5,314.27v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H801.5z" />
      </g>
      <path class="st62" d="M701.67,279.54c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="692.78" y1="294.04" x2="692.78" y2="301.31" />
      <path class="st62" d="M693.19,305.87c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st64" x1="707.77" y1="314.76" x2="822.92" y2="314.76" />
      <path class="st62" d="M827.52,314.36c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="836.41" y1="299.86" x2="836.41" y2="292.59" />
      <path class="st62" d="M836.01,288.03c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st64" x1="821.42" y1="279.14" x2="706.28" y2="279.14" />
      <path class="st59" d="M692.78,291.14L692.78,291.14 M692.78,302.76L692.78,302.76 M704.78,314.76L704.78,314.76 M824.41,314.76
		L824.41,314.76 M836.41,302.76L836.41,302.76 M836.41,291.14L836.41,291.14 M824.41,279.14L824.41,279.14 M704.78,279.14
		L704.78,279.14" />
      <path class="st55" d="M753.7,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87
		C741.68,230.08,747.37,234.81,753.7,234.48L753.7,234.48z" />
      <line class="st60" x1="764.6" y1="247.53" x2="764.6" y2="263.81" />
      <path class="st61" d="M764.6,244.57L764.6,244.57 M764.6,265.29L764.6,265.29" />
      <path d="M764.6,247.35c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78s-2.78,1.24-2.78,2.78
		C761.82,246.1,763.06,247.35,764.6,247.35L764.6,247.35z" />
      <g class="st5">
        <path class="st55" d="M556.28,280.21c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.1-0.11-4.1-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H556.28z" />
        <path class="st55" d="M565.33,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H565.33z" />
        <path class="st55" d="M569.27,276.62h1.66v1.58h-1.66V276.62z M570.84,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M574.83,289.62h-1.48v-13h1.48V289.62z" />
        <path class="st55" d="M582.2,276.62h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V276.62z M580.49,281.56c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C582.2,283.5,582.12,281.56,580.49,281.56z" />
        <path class="st55" d="M591.92,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z" />
        <path class="st55" d="M596.25,276.62h1.66v1.58h-1.66V276.62z M597.82,289.62h-1.48v-9.09h1.48V289.62z" />
        <path class="st55" d="M605.18,280.53h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M603.45,281.58c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C605.22,283.68,605.31,281.58,603.45,281.58z" />
        <path class="st55" d="M614.31,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H614.31z" />
        <path class="st55"
          d="M618.54,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H618.54z" />
        <path class="st55" d="M626.06,289.8c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C629.23,289.03,627.86,289.8,626.06,289.8z" />
      </g>
      <g class="st5">
        <path class="st55" d="M552.69,302.13h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V302.13z M550.96,303.18c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C552.73,305.29,552.82,303.18,550.96,303.18z" />
        <path class="st55" d="M556.63,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C558.16,311.41,556.63,310.83,556.63,306.82z M562,306.19c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C561.62,310.2,562,309.14,562,306.19z" />
        <path class="st55" d="M564.84,302.13h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L564.84,302.13z" />
        <path class="st55" d="M575.31,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H575.31z M578.86,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H578.86z" />
        <path class="st55" d="M584.4,303.5h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V303.5z" />
        <path class="st55" d="M593.8,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H593.8z" />
        <path class="st55" d="M602.55,309.91h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V309.91z M599.22,308.53c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C601.11,306.73,599.22,306.6,599.22,308.53z" />
        <path class="st55" d="M611.8,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H611.8z" />
        <path class="st55" d="M620.62,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H620.62z" />
        <path class="st55" d="M626.31,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H626.31z M629.85,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H629.85z" />
      </g>
      <path class="st62" d="M532.48,276.5c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="523.59" y1="291" x2="523.59" y2="298.27" />
      <path class="st62" d="M523.99,302.83c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="538.53" y1="311.72" x2="643.22" y2="311.72" />
      <path class="st62" d="M647.8,311.32c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="656.7" y1="296.82" x2="656.7" y2="289.55" />
      <path class="st62" d="M656.29,284.99c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="641.75" y1="276.1" x2="537.06" y2="276.1" />
      <path class="st59"
        d="M523.59,288.1L523.59,288.1 M523.59,299.72L523.59,299.72 M535.59,311.72L535.59,311.72 M644.7,311.72
		L644.7,311.72 M656.7,299.72L656.7,299.72 M656.7,288.1L656.7,288.1 M644.7,276.1L644.7,276.1 M535.59,276.1L535.59,276.1" />
      <path class="st55" d="M579.24,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.06,0.48-12.2,6.9-11.2,13.9l6.37,44.87
		C567.22,230.08,572.91,234.81,579.24,234.48L579.24,234.48z" />
      <line class="st60" x1="590.14" y1="244.49" x2="590.14" y2="260.77" />
      <path class="st61" d="M590.14,241.53L590.14,241.53 M590.14,262.25L590.14,262.25" />
      <path d="M590.14,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C587.36,243.06,588.61,244.31,590.14,244.31L590.14,244.31z" />
      <path class="st54"
        d="M593.06,203.52v-5.47v-1.46v-4.15c0.79,0.61,1.33,1.47,1.47,2.48c0.08,0.55,0.55,0.94,1.08,0.94
		c0.05,0,0.1,0,0.15-0.01c0.6-0.08,1.01-0.64,0.93-1.24c-0.43-3.08-3.19-5.32-6.55-5.32s-6.12,2.24-6.55,5.32
		c-0.08,0.6,0.33,1.15,0.93,1.24s1.15-0.33,1.24-0.93c0.14-1,0.68-1.86,1.47-2.48v4.15v1.46v5.47c0,0.6,0.49,1.09,1.09,1.09
		s1.09-0.49,1.09-1.09v-5.47h1.46v5.47c0,0.6,0.49,1.09,1.09,1.09C592.57,204.61,593.06,204.12,593.06,203.52L593.06,203.52z" />
      <path class="st54" d="M590.14,187.84c1.61,0,2.92-1.31,2.92-2.92s-1.3-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92
		C587.22,186.54,588.53,187.84,590.14,187.84L590.14,187.84z" />
      <path class="st54" d="M581.07,200.69c-0.59-0.6-1.56-0.6-2.15,0s-0.59,1.58,0,2.19l2.77,2.66c0.35,0.35,0.35,0.92,0,1.27
		s-0.91,0.35-1.25,0l-3.42-3.66v-11.67c0-1.21-1-2.19-2.19-2.19s-2.19,0.98-2.19,2.19v12.69c0,0.58,0.23,1.14,0.63,1.55l8.12,8.37
		v2.92h6.56v-7.29c0-1.46-0.38-2.57-1.33-3.54L581.07,200.69L581.07,200.69z" />
      <path class="st54" d="M605.45,189.3c-1.19,0-2.19,0.98-2.19,2.19v11.67l-3.42,3.66c-0.35,0.35-0.91,0.35-1.25,0
		c-0.35-0.35-0.35-0.92,0-1.27l2.77-2.66c0.59-0.6,0.59-1.58,0-2.19c-0.59-0.6-1.56-0.6-2.15,0l-5.55,5.49
		c-0.95,0.97-1.33,2.08-1.33,3.54v7.29h6.56v-2.92l8.12-8.37c0.41-0.41,0.63-0.97,0.63-1.55v-12.69
		C607.64,190.28,606.64,189.3,605.45,189.3L605.45,189.3z" />
      <g class="st5">
        <path class="st55" d="M1230.03,288.1v-13h4.23c1.8,0,2.41,0.61,2.9,1.33c0.45,0.7,0.52,1.48,0.52,1.73c0,1.62-0.56,2.7-2.23,3.08
			v0.09c1.85,0.22,2.67,1.33,2.67,3.11c0,3.33-2.43,3.66-3.91,3.66H1230.03z M1231.68,280.58h2.41c1.3-0.02,1.93-0.81,1.93-2.07
			c0-1.08-0.61-1.96-2-1.96h-2.34V280.58z M1231.68,286.66h2.34c1.77,0,2.39-1.26,2.39-2.21c0-2.07-1.28-2.43-2.97-2.43h-1.76
			V286.66z" />
        <path class="st55" d="M1245.56,279.01h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57V287h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V279.01z" />
        <path class="st55" d="M1252.38,288.28c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1255.55,287.51,1254.18,288.28,1252.38,288.28z" />
        <path class="st55" d="M1257.57,275.1h1.66v1.58h-1.66V275.1z M1259.13,288.1h-1.48v-9.09h1.48V288.1z" />
        <path class="st55" d="M1266.62,288.1v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1266.62z" />
        <path class="st55" d="M1272.13,284.03c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1272.13z M1275.68,282.92c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1275.68z" />
        <path class="st55" d="M1282.37,288.28c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1285.54,287.51,1284.17,288.28,1282.37,288.28z" />
        <path class="st55" d="M1290.36,288.28c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1293.53,287.51,1292.16,288.28,1290.36,288.28z" />
        <path class="st55" d="M1304.35,286.79h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V286.79z M1301.02,285.4c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1302.91,283.6,1301.02,283.47,1301.02,285.4z" />
        <path class="st55" d="M1313.6,288.1v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1313.6z" />
        <path class="st55" d="M1322.47,275.1h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V275.1z M1320.76,280.04c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1322.47,281.98,1322.4,280.04,1320.76,280.04z" />
      </g>
      <g class="st5">
        <path class="st55" d="M1241.57,300.29c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01
			c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11
			c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H1241.57z" />
        <path class="st55" d="M1250.63,309.7v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1250.63z" />
        <path class="st55" d="M1254.57,296.7h1.66v1.58h-1.66V296.7z M1256.13,309.7h-1.48v-9.09h1.48V309.7z" />
        <path class="st55" d="M1260.13,309.7h-1.48v-13h1.48V309.7z" />
        <path class="st55" d="M1267.49,296.7h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V296.7z M1265.78,301.64c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.86,3.35c1.66,0,1.66-2.05,1.66-3.89C1267.49,303.58,1267.42,301.64,1265.78,301.64z" />
        <path class="st55" d="M1277.46,303.73v5.98h-1.66v-13h4.48c2.3,0,3.12,1.62,3.12,3.24c0,1.53-0.85,2.7-2.38,2.97v0.04
			c1.5,0.23,2.04,0.74,2.12,3.35c0.02,0.56,0.2,2.59,0.45,3.4h-1.73c-0.47-0.9-0.36-2.59-0.5-4.32c-0.13-1.58-1.41-1.66-1.96-1.66
			H1277.46z M1277.46,302.29h2.48c1.19,0,1.76-1.03,1.76-2.16c0-0.94-0.47-1.98-1.75-1.98h-2.5V302.29z" />
        <path class="st55" d="M1285.56,296.7h1.66v1.58h-1.66V296.7z M1287.13,309.7h-1.48v-9.09h1.48V309.7z" />
        <path class="st55" d="M1294.49,300.61h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V300.61z M1292.77,301.65c-1.68,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1294.53,303.76,1294.62,301.65,1292.77,301.65z" />
        <path class="st55" d="M1303.62,309.7v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1303.62z" />
        <path class="st55"
          d="M1307.85,300.61v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1307.85z" />
        <path class="st55" d="M1315.37,309.88c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1318.54,309.11,1317.17,309.88,1315.37,309.88z" />
      </g>
      <path class="st62" d="M1219.79,274.98c-4.64,1.24-8.16,5.18-8.8,10.03" />
      <line class="st63" x1="1210.89" y1="289.48" x2="1210.89" y2="296.75" />
      <path class="st62" d="M1211.3,301.31c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="1225.84" y1="310.2" x2="1330.53" y2="310.2" />
      <path class="st62" d="M1335.11,309.8c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="1344" y1="295.3" x2="1344" y2="288.03" />
      <path class="st62" d="M1343.6,283.47c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="1329.06" y1="274.58" x2="1224.37" y2="274.58" />
      <path class="st59"
        d="M1210.89,286.58L1210.89,286.58 M1210.89,298.2L1210.89,298.2 M1222.89,310.2L1222.89,310.2 M1332,310.2
		L1332,310.2 M1344,298.2L1344,298.2 M1344,286.58L1344,286.58 M1332,274.58L1332,274.58 M1222.89,274.58L1222.89,274.58" />
      <path class="st55" d="M1266.55,234.48c4.8-0.38,14.47-0.37,21.61,0.01c6.31,0.34,11.83-4.17,12.74-10.42l6.55-44.96
		c0.9-7.21-4.09-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87
		C1254.53,230.08,1260.22,234.81,1266.55,234.48L1266.55,234.48z" />
      <line class="st60" x1="1277.45" y1="242.97" x2="1277.45" y2="259.25" />
      <path class="st61" d="M1277.45,240.01L1277.45,240.01 M1277.45,260.73L1277.45,260.73" />
      <path d="M1277.45,242.79c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.25-2.78-2.78-2.78c-1.54,0-2.78,1.24-2.78,2.78
		C1274.67,241.54,1275.91,242.79,1277.45,242.79L1277.45,242.79z" />
      <path class="st54" d="M1294.95,197.01h-1.04c-0.42-2.73-1.49-5.24-3.06-7.37l0.74-0.74c0.98-0.97,0.98-2.56,0-3.53
		c-0.98-0.98-2.56-0.98-3.53,0l-0.75,0.74c-2.12-1.57-4.63-2.64-7.36-3.06v-1.04c0-1.38-1.12-2.5-2.5-2.5s-2.5,1.12-2.5,2.5v1.04
		c-2.73,0.41-5.24,1.49-7.37,3.06l-0.74-0.74c-0.98-0.98-2.56-0.98-3.53,0c-0.98,0.98-0.98,2.56,0,3.53l0.74,0.74
		c-1.57,2.13-2.65,4.64-3.06,7.37h-1.04c-1.38,0-2.5,1.12-2.5,2.5s1.12,2.5,2.5,2.5h1.04c0.41,2.73,1.49,5.24,3.06,7.37l-0.74,0.74
		c-0.98,0.98-0.98,2.56,0,3.54c0.48,0.49,1.12,0.73,1.76,0.73s1.28-0.24,1.77-0.73l0.74-0.74c2.13,1.57,4.64,2.64,7.37,3.06v1.04
		c0,1.38,1.12,2.5,2.5,2.5s2.5-1.12,2.5-2.5v-1.04c2.73-0.41,5.24-1.49,7.36-3.06l0.75,0.74c0.48,0.49,1.12,0.73,1.76,0.73
		s1.28-0.24,1.77-0.73c0.98-0.98,0.98-2.56,0-3.54l-0.74-0.74c1.57-2.13,2.64-4.64,3.06-7.37h1.04c1.38,0,2.5-1.12,2.5-2.5
		C1297.45,198.13,1296.33,197.01,1294.95,197.01L1294.95,197.01z M1277.45,211.18c-6.43,0-11.67-5.23-11.67-11.67
		s5.24-11.67,11.67-11.67s11.67,5.23,11.67,11.67S1283.88,211.18,1277.45,211.18L1277.45,211.18z" />
      <path class="st54" d="M1279.92,208.17v-4.64v-1.24v-3.52c0.67,0.52,1.13,1.25,1.25,2.1c0.06,0.46,0.46,0.8,0.91,0.8
		c0.05,0,0.09,0,0.13-0.01c0.51-0.07,0.87-0.54,0.79-1.05c-0.36-2.61-2.7-4.51-5.55-4.51c-2.85,0-5.19,1.9-5.56,4.51
		c-0.07,0.51,0.29,0.98,0.79,1.05c0.51,0.07,0.98-0.28,1.05-0.79c0.12-0.85,0.58-1.58,1.25-2.1v3.52v1.24v4.64
		c0,0.51,0.41,0.93,0.92,0.93c0.52,0,0.93-0.42,0.93-0.93v-4.64h1.24v4.64c0,0.51,0.41,0.93,0.92,0.93
		C1279.51,209.09,1279.92,208.68,1279.92,208.17L1279.92,208.17z" />
      <path class="st54" d="M1277.45,194.87c1.36,0,2.47-1.11,2.47-2.47s-1.11-2.47-2.47-2.47c-1.37,0-2.47,1.11-2.47,2.47
		C1274.98,193.77,1276.08,194.87,1277.45,194.87L1277.45,194.87z" />
      <g class="st5">
        <path class="st55" d="M911.99,276.62h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24
			c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V276.62z M913.65,288.18h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6
			h-2.18V288.18z" />
        <path class="st55" d="M927.48,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M924.14,286.92c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C926.04,285.12,924.14,285,924.14,286.92z" />
        <path class="st55"
          d="M931.96,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H931.96z" />
        <path class="st55" d="M941.48,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M938.15,286.92c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C940.04,285.12,938.15,285,938.15,286.92z" />
        <path class="st55" d="M949.54,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			S949.54,289.23,949.54,285.21z M954.91,284.58c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			S954.91,287.54,954.91,284.58z" />
        <path class="st55" d="M963.73,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H963.73z" />
      </g>
      <g class="st5">
        <path class="st55" d="M915.05,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H915.05z" />
        <path class="st55" d="M924.23,311.23v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H924.23z" />
        <path class="st55" d="M928.17,298.23h1.66v1.58h-1.66V298.23z M929.74,311.23h-1.48v-9.09h1.48V311.23z" />
        <path class="st55" d="M933.73,311.23h-1.48v-13h1.48V311.23z" />
        <path class="st55" d="M941.1,298.23h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V298.23z M939.38,303.16c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C941.1,305.1,941.02,303.16,939.38,303.16z" />
        <path class="st55" d="M946.82,303.5h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V303.5z" />
        <path class="st55" d="M952.72,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H952.72z M956.27,306.04
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H956.27z" />
        <path class="st55" d="M965.21,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H965.21z" />
      </g>
      <path class="st62" d="M881.39,276.5c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="872.5" y1="291" x2="872.5" y2="298.27" />
      <path class="st62" d="M872.91,302.83c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="887.45" y1="311.72" x2="992.14" y2="311.72" />
      <path class="st62" d="M996.72,311.32c4.63-1.24,8.16-5.18,8.79-10.03" />
      <line class="st63" x1="1005.61" y1="296.82" x2="1005.61" y2="289.55" />
      <path class="st62" d="M1005.21,284.99c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="990.66" y1="276.1" x2="885.97" y2="276.1" />
      <path class="st59" d="M872.5,288.1L872.5,288.1 M872.5,299.72L872.5,299.72 M884.5,311.72L884.5,311.72 M993.61,311.72
		L993.61,311.72 M1005.61,299.72L1005.61,299.72 M1005.61,288.1L1005.61,288.1 M993.61,276.1L993.61,276.1 M884.5,276.1L884.5,276.1
		" />
      <path class="st55" d="M928.15,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87
		C916.14,230.08,921.83,234.81,928.15,234.48L928.15,234.48z" />
      <line class="st60" x1="939.06" y1="244.49" x2="939.06" y2="260.77" />
      <path class="st61" d="M939.06,241.53L939.06,241.53 M939.06,262.25L939.06,262.25" />
      <path d="M939.06,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.54,0-2.78,1.24-2.78,2.78
		C936.28,243.06,937.52,244.31,939.06,244.31L939.06,244.31z" />
      <path class="st54" d="M927.67,206.66l-5.23,5.23c-1.17,1.17-1.17,3.08,0,4.24c1.17,1.17,3.08,1.17,4.24,0l5.24-5.24
		C930.26,209.74,928.83,208.3,927.67,206.66L927.67,206.66z" />
      <path class="st54" d="M937.6,196.59h-2.92c-0.4,0-0.73,0.33-0.73,0.73v3.6c0.96,1.78,2.51,3.21,4.38,4.03v-7.63
		C938.33,196.92,938,196.59,937.6,196.59L937.6,196.59z" />
      <path class="st54" d="M949.26,192.22h-2.92c-0.4,0-0.73,0.33-0.73,0.73v12c1.87-0.82,3.41-2.25,4.38-4.03v-7.98
		C949.99,192.55,949.66,192.22,949.26,192.22L949.26,192.22z" />
      <path class="st54" d="M943.43,194.41h-2.92c-0.4,0-0.73,0.33-0.73,0.73v10.31c0.7,0.17,1.43,0.26,2.19,0.26s1.49-0.09,2.19-0.26
		v-10.31C944.16,194.73,943.83,194.41,943.43,194.41L943.43,194.41z" />
      <path class="st54" d="M941.97,182.01c-8.06,0-14.58,6.53-14.58,14.58s6.53,14.58,14.58,14.58c8.06,0,14.58-6.53,14.58-14.58
		S950.03,182.01,941.97,182.01L941.97,182.01z M949.99,204.02c-1.19,1.29-2.68,2.3-4.38,2.89c-0.47,0.17-0.95,0.31-1.46,0.41
		c-0.71,0.15-1.44,0.22-2.19,0.22s-1.48-0.07-2.19-0.22c-0.5-0.1-0.98-0.24-1.46-0.41c-1.69-0.59-3.19-1.6-4.38-2.89
		c-1.82-1.95-2.92-4.56-2.92-7.42c0-6.04,4.9-10.94,10.94-10.94s10.94,4.9,10.94,10.94C952.91,199.46,951.81,202.07,949.99,204.02
		L949.99,204.02z" />
      <g class="st5">
        <path class="st55" d="M1076.1,278.15h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L1076.1,278.15z M1077.1,279.68h-0.04
			l-2.03,6.93h4.16L1077.1,279.68z" />
        <path class="st55" d="M1088.75,284.97c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1088.75z" />
        <path class="st55" d="M1097.75,284.97c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1097.75z" />
        <path class="st55" d="M1103.44,287.08c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1103.44z M1106.98,285.96c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1106.98z" />
        <path class="st55" d="M1113.68,291.33c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1116.85,290.55,1115.48,291.33,1113.68,291.33z" />
        <path class="st55" d="M1121.67,291.33c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1124.84,290.55,1123.47,291.33,1121.67,291.33z" />
        <path class="st55"
          d="M1131.14,282.06v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1131.14z" />
        <path class="st55" d="M1135.73,286.74c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C1137.26,291.33,1135.73,290.75,1135.73,286.74z M1141.09,286.11c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C1140.72,290.12,1141.09,289.06,1141.09,286.11z" />
      </g>
      <g class="st5">
        <path class="st55" d="M1084.96,303.65h1.48V314c0,1.44-0.41,2.18-2.57,2.18v-1.26c0.63,0,1.1-0.09,1.1-0.85V303.65z
			 M1084.87,299.74h1.66v1.58h-1.66V299.74z" />
        <path class="st55" d="M1093.86,303.65h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V303.65z" />
        <path class="st55" d="M1100.68,312.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1103.85,312.15,1102.48,312.92,1100.68,312.92z" />
        <path class="st55"
          d="M1106.15,303.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1106.15z" />
        <path class="st55" d="M1110.87,299.74h1.66v1.58h-1.66V299.74z M1112.43,312.74h-1.48v-9.09h1.48V312.74z" />
        <path class="st55" d="M1119.74,306.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1119.74z" />
        <path class="st55" d="M1125.43,308.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1125.43z M1128.97,307.56c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1128.97z" />
      </g>
      <path class="st62" d="M1050.59,278.02c-4.63,1.24-8.16,5.18-8.79,10.03" />
      <line class="st63" x1="1041.7" y1="292.52" x2="1041.7" y2="299.79" />
      <path class="st62" d="M1042.1,304.35c1.24,4.63,5.18,8.16,10.03,8.79" />
      <line class="st58" x1="1056.65" y1="313.24" x2="1161.33" y2="313.24" />
      <path class="st62" d="M1165.91,312.84c4.64-1.24,8.16-5.18,8.8-10.03" />
      <line class="st63" x1="1174.81" y1="298.34" x2="1174.81" y2="291.07" />
      <path class="st62" d="M1174.4,286.51c-1.24-4.63-5.18-8.16-10.03-8.79" />
      <line class="st58" x1="1159.86" y1="277.62" x2="1055.17" y2="277.62" />
      <path class="st59" d="M1041.7,289.62L1041.7,289.62 M1041.7,301.24L1041.7,301.24 M1053.7,313.24L1053.7,313.24 M1162.81,313.24
		L1162.81,313.24 M1174.81,301.24L1174.81,301.24 M1174.81,289.62L1174.81,289.62 M1162.81,277.62L1162.81,277.62 M1053.7,277.62
		L1053.7,277.62" />
      <path class="st55" d="M1097.35,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96
		c0.89-7.21-4.1-13.45-11.16-13.94c-8.1-0.87-24.95-0.89-37.63-0.03c-7.06,0.48-12.2,6.9-11.2,13.9l6.36,44.87
		C1085.33,230.08,1091.03,234.81,1097.35,234.48L1097.35,234.48z" />
      <line class="st65" x1="1108.25" y1="246.01" x2="1108.25" y2="262.29" />
      <path class="st66" d="M1108.25,243.05L1108.25,243.05 M1108.25,263.77L1108.25,263.77" />
      <path class="st55" d="M1108.25,245.83c1.54,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78
		C1105.47,244.58,1106.72,245.83,1108.25,245.83L1108.25,245.83z" />
      <path class="st54" d="M1109.84,191.45c0.31,0.31,0.31,0.81,0,1.12l-4.89,4.89c-0.31,0.31-0.81,0.31-1.12,0.01
		c-0.31-0.32-0.3-0.82,0-1.13l4.89-4.89C1109.03,191.14,1109.53,191.14,1109.84,191.45L1109.84,191.45z M1112.16,205.79
		c0.31,0.31,0.81,0.31,1.12,0l4.89-4.89c0.31-0.31,0.31-0.81,0-1.12c-0.3-0.31-0.81-0.31-1.12,0l-4.89,4.89
		C1111.85,204.98,1111.85,205.48,1112.16,205.79L1112.16,205.79z M1123.89,191.62v23.36h-25.4v-0.38l-2.25,2.41l-3.63-3.64l5.88-5.5
		v-25.86h16.15L1123.89,191.62L1123.89,191.62z M1115.07,190.84h4.36l-4.36-4.53V190.84L1115.07,190.84z M1121.22,192.84h-8.16
		v-8.16h-11.89v20.69l5.97-5.59l-1.79-1.79l5.02-5.03l6.29,6.29l-5.02,5.03l-1.8-1.8l-8.67,9.27v0.56h20.05L1121.22,192.84
		L1121.22,192.84z" />
      <path class="st67" d="M50.5,1086.52c-11.05,0-20,8.96-20,20v159.23c0,11.05,8.95,20,20,20h1254c11.05,0,20-8.95,20-20v-159.23
		c0-11.04-8.95-20-20-20H50.5L50.5,1086.52z" />
      <g class="st5">
        <path class="st68" d="M551.42,1237.87c0-1.53-0.63-2.36-2.3-2.36c-0.52,0-2.4,0.09-2.4,2.81v4.39c0,2.84,0.83,3.57,2.4,3.57
			c1.19,0,1.98-0.32,2.32-0.58v-3.89h-2.39v-1.44h4.05v6.32c-1.06,0.58-2.3,0.97-3.98,0.97c-2.75,0-4.09-1.42-4.09-5.02v-4.27
			c0-2.59,1.33-4.25,4.09-4.25c2.81,0,4.14,1.03,4.03,3.75H551.42z" />
        <path class="st68" d="M557.47,1243.32c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H557.47
			z M561.02,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H561.02z" />
        <path class="st68" d="M569.96,1247.39v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H569.96z" />
        <path class="st68" d="M578.84,1234.39h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1234.39z M577.13,1239.32c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C578.84,1241.27,578.76,1239.32,577.13,1239.32z" />
        <path class="st68" d="M584.47,1243.32c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H584.47
			z M588.02,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H588.02z" />
        <path class="st68" d="M593.56,1239.67h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1239.67z" />
      </g>
      <path class="st69" d="M538.06,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C552.46,1150.96,538.06,1165.36,538.06,1183.12L538.06,1183.12z" />
      <path class="st70" d="M538.06,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C552.46,1150.96,538.06,1165.36,538.06,1183.12L538.06,1183.12z" />
      <path class="st68" d="M583.23,1164.08c0-0.51-0.41-0.92-0.92-0.92h-7.79c-0.51,0-0.92,0.41-0.92,0.92v0.75
		c0,0.51,0.41,0.92,0.93,0.92l4.31-0.01l-5.98,5.98c-1.63-1.22-3.65-1.95-5.84-1.95c-5.41,0-9.81,4.39-9.81,9.8s4.4,9.81,9.81,9.81
		s9.81-4.4,9.81-9.81c0-2.29-0.79-4.39-2.12-6.06l5.95-5.95v4.18c0,0.59,0.48,1.07,1.08,1.07h0.59c0.51,0,0.93-0.41,0.92-0.92
		L583.23,1164.08L583.23,1164.08z M567.01,1187.38c-4.31,0-7.81-3.5-7.81-7.81s3.51-7.81,7.81-7.81c4.31,0,7.81,3.5,7.81,7.81
		C574.83,1183.88,571.32,1187.38,567.01,1187.38L567.01,1187.38z" />
      <path class="st68" d="M573.95,1186.53c3.82-3.83,3.82-10.05,0-13.87c-3.82-3.83-10.04-3.83-13.87,0c-3.82,3.82-3.82,10.04,0,13.87
		c1.58,1.58,3.57,2.49,5.63,2.77v6.62h-2.67c-0.52,0-0.95,0.43-0.95,0.95v0.72c0,0.53,0.42,0.95,0.95,0.95h2.67v2.68
		c0,0.52,0.42,0.94,0.94,0.94h0.74c0.52,0,0.94-0.42,0.94-0.94v-2.68H571c0.52,0,0.95-0.42,0.95-0.95v-0.72
		c0-0.52-0.42-0.95-0.95-0.95h-2.67v-6.62C570.38,1189.02,572.37,1188.11,573.95,1186.53L573.95,1186.53z M561.49,1185.12
		c-3.05-3.05-3.05-8.01,0-11.05c3.05-3.05,8-3.05,11.05,0c3.05,3.04,3.05,8,0,11.05C569.49,1188.16,564.54,1188.16,561.49,1185.12
		L561.49,1185.12z" />
      <g class="st5">
        <path class="st68" d="M322.55,1234.8h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24
			c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V1234.8z M324.21,1246.36h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6
			h-2.18V1246.36z" />
        <path class="st68" d="M333.22,1234.8h1.66v1.58h-1.66V1234.8z M334.79,1247.8h-1.48v-9.09h1.48V1247.8z" />
        <path class="st68" d="M340.03,1247.98c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C343.2,1247.2,341.83,1247.98,340.03,1247.98z" />
        <path class="st68" d="M350.02,1246.48h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1246.48z M346.69,1245.1c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C348.58,1243.3,346.69,1243.17,346.69,1245.1z" />
        <path class="st68" d="M355.94,1247.8h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88
			c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V1247.8z M357.6,1246.77c1.85,0,1.85-1.98,1.85-3.35
			c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C355.94,1244.27,355.78,1246.77,357.6,1246.77z" />
        <path class="st68" d="M363.21,1234.8h1.66v1.58h-1.66V1234.8z M364.78,1247.8h-1.48v-9.09h1.48V1247.8z" />
        <path class="st68" d="M368.77,1247.8h-1.48v-13h1.48V1247.8z" />
        <path class="st68" d="M371.2,1234.8h1.66v1.58h-1.66V1234.8z M372.77,1247.8h-1.48v-9.09h1.48V1247.8z" />
        <path class="st68"
          d="M375.49,1238.7v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H375.49z" />
        <path class="st68"
          d="M383.06,1246.1h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L383.06,1246.1z" />
      </g>
      <path class="st69" d="M321.88,1183.12c0,17.77,14.4,32.17,32.17,32.17c17.76,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16S321.88,1165.36,321.88,1183.12L321.88,1183.12z" />
      <path class="st70" d="M321.88,1183.12c0,17.77,14.4,32.17,32.17,32.17c17.76,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16S321.88,1165.36,321.88,1183.12L321.88,1183.12z" />
      <path class="st68" d="M355.04,1170.29c0,2.33-1.88,4.21-4.21,4.21c-2.32,0-4.21-1.88-4.21-4.21c0-2.32,1.88-4.21,4.21-4.21
		C353.15,1166.08,355.04,1167.97,355.04,1170.29L355.04,1170.29z" />
      <path class="st68" d="M365.33,1193.25h-2.29c0,0-1.39-3.97-1.78-5.02c-0.25-0.7-0.9-1.21-1.68-1.21h-5.56v-3.9h5.28
		c0.7,0,1.27-0.57,1.27-1.27c0-0.71-0.57-1.28-1.27-1.28h-5.28c0,0-0.3-4.64-2.92-4.64c-1.79,0-2.41,1.47-2.41,3.27v8.18
		c0,1.8,1.46,3.26,3.25,3.26c0.05,0,0.1-0.02,0.15-0.02s0.1,0.02,0.15,0.02h6.78l2.26,5.67h4.05c0.84,0,1.52-0.69,1.52-1.53
		C366.85,1193.94,366.17,1193.25,365.33,1193.25L365.33,1193.25z" />
      <path class="st68" d="M358.07,1192.62c-0.97,3.12-3.82,5.41-7.22,5.41c-4.19,0-7.6-3.45-7.6-7.7c0-2.86,1.57-5.34,3.86-6.66l0,0
		l0,0v-8.43h-0.71h-0.71h-3.53c-0.39,0-0.7,0.32-0.7,0.72c0,0.39,0.32,0.71,0.7,0.71h3.53v5.44c-2.68,1.73-4.47,4.76-4.47,8.22
		c0,5.38,4.32,9.75,9.63,9.75c3.52,0,6.58-1.95,8.26-4.82L358.07,1192.62L358.07,1192.62z" />
      <g class="st5">
        <path class="st68" d="M83.83,1240.61v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H83.83z" />
        <path class="st68" d="M97.34,1239.29h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1239.29z M94.01,1237.91c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C95.9,1236.11,94.01,1235.98,94.01,1237.91z" />
        <path class="st68" d="M103.19,1232.88h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1232.88z" />
        <path class="st68" d="M109.1,1240.61h-1.48v-13h1.48V1240.61z" />
        <path class="st68"
          d="M114.39,1238.92h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L114.39,1238.92z" />
        <path class="st68" d="M128.39,1234.43c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2H130c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H128.39z" />
        <path class="st68" d="M137.57,1240.61v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H137.57z" />
        <path class="st68" d="M141.51,1227.61h1.66v1.58h-1.66V1227.61z M143.08,1240.61h-1.48v-9.09h1.48V1240.61z" />
        <path class="st68" d="M147.08,1240.61h-1.48v-13h1.48V1240.61z" />
        <path class="st68" d="M154.44,1227.61h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1227.61z M152.73,1232.54c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C154.44,1234.49,154.37,1232.54,152.73,1232.54z" />
        <path class="st68" d="M163.57,1240.61v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H163.57z" />
        <path class="st68" d="M167.38,1236.2c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C168.91,1240.79,167.38,1240.21,167.38,1236.2z M172.75,1235.57c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C172.37,1239.58,172.75,1238.52,172.75,1235.57z" />
        <path class="st68" d="M176.38,1236.2c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C177.91,1240.79,176.38,1240.21,176.38,1236.2z M181.75,1235.57c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C181.37,1239.58,181.75,1238.52,181.75,1235.57z" />
        <path class="st68" d="M190.44,1227.61h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1227.61z M188.73,1232.54c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C190.44,1234.49,190.37,1232.54,188.73,1232.54z" />
      </g>
      <g class="st5">
        <path class="st68" d="M97.46,1249.2h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1249.2z M95.75,1254.14c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C97.46,1256.08,97.39,1254.14,95.75,1254.14z" />
        <path class="st68" d="M103.1,1258.13c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93
			c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H103.1z M106.64,1257.02
			c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H106.64z" />
        <path class="st68" d="M109.61,1253.11h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L109.61,1253.11z" />
        <path class="st68" d="M120.09,1258.13c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H120.09
			z M123.63,1257.02c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H123.63z" />
        <path class="st68" d="M129.09,1262.2h-1.48v-13h1.48V1262.2z" />
        <path class="st68" d="M131.39,1257.79c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C132.92,1262.38,131.39,1261.81,131.39,1257.79z M136.76,1257.16c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C136.38,1261.18,136.76,1260.11,136.76,1257.16z" />
        <path class="st68" d="M142.25,1254.19h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88
			c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1254.19z M145.76,1257.5c0-1.37,0-3.37-1.85-3.37
			c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C145.54,1261.18,145.76,1259.93,145.76,1257.5z" />
        <path class="st68" d="M154.11,1262.2v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H154.11z" />
        <path class="st68" d="M164.08,1258.13c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H164.08
			z M167.63,1257.02c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H167.63z" />
        <path class="st68" d="M176.57,1262.2v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H176.57z" />
        <path class="st68"
          d="M180.8,1253.11v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H180.8z" />
      </g>
      <path class="st69" d="M105.69,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.17-14.4,32.17-32.17c0-17.76-14.4-32.16-32.17-32.16
		S105.69,1165.36,105.69,1183.12L105.69,1183.12z" />
      <path class="st70" d="M105.69,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.17-14.4,32.17-32.17c0-17.76-14.4-32.16-32.17-32.16
		S105.69,1165.36,105.69,1183.12L105.69,1183.12z" />
      <path class="st68" d="M137.19,1190.06c0,0,3.34,3.35,3.36,3.35c1.07,1.08,0.79,2.96-0.22,3.99l-4.67,4.87
		c-1.8,1.79-4.21-0.7-2.46-2.44l2.96-2.96l-2.9-2.88L137.19,1190.06L137.19,1190.06L137.19,1190.06z M126.79,1190.06L126.79,1190.06
		l-3.34,3.35c-1.08,1.08-0.8,2.96,0.2,3.99l4.68,4.87c1.8,1.79,4.2-0.7,2.46-2.44l-2.96-2.96l2.88-2.88L126.79,1190.06
		L126.79,1190.06z M132.11,1177.6c2.68,0,4.85-2.17,4.85-4.86c0-2.68-2.17-4.85-4.85-4.85c-2.68,0-4.86,2.17-4.86,4.85
		C127.25,1175.43,129.42,1177.6,132.11,1177.6L132.11,1177.6z M137.37,1188.11l0.07-3.31l4.03,3.77c0.33,0.31,0.75,0.46,1.17,0.46
		c0.46,0,0.92-0.18,1.26-0.55c0.65-0.69,0.61-1.78-0.08-2.43c0,0-4.63-5.02-5.29-5.61c-1.23-1.09-3.04-1.71-5.97-1.71h-0.92
		c-2.93,0-4.73,0.62-5.97,1.71c-0.66,0.59-5.29,5.61-5.29,5.61c-0.69,0.65-0.73,1.74-0.08,2.43c0.34,0.37,0.8,0.55,1.26,0.55
		c0.42,0,0.84-0.15,1.17-0.46l4.03-3.77l0.07,3.31H137.37L137.37,1188.11z" />
      <path class="st68" d="M146.25,1176.03v5.36c0,0.66,0.54,1.2,1.2,1.2h5.36c0.66,0,1.2-0.54,1.2-1.2v-5.36c0-0.66-0.54-1.2-1.2-1.2
		h-5.36C146.79,1174.83,146.25,1175.37,146.25,1176.03L146.25,1176.03z M150.63,1180.63l-0.07-0.39h-0.02
		c-0.25,0.31-0.65,0.48-1.11,0.48c-0.78,0-1.25-0.57-1.25-1.19c0-1,0.9-1.48,2.26-1.47V1178c0-0.2-0.11-0.49-0.7-0.49
		c-0.4,0-0.81,0.13-1.07,0.29l-0.22-0.78c0.27-0.14,0.8-0.33,1.5-0.33c1.28,0,1.7,0.75,1.7,1.66v1.34c0,0.37,0.02,0.73,0.05,0.94
		H150.63L150.63,1180.63z" />
      <path class="st68"
        d="M148.1,1184.94v5.3c0,0.68,0.55,1.23,1.23,1.23h5.3c0.68,0,1.23-0.55,1.23-1.23v-5.3
		c0-0.68-0.55-1.23-1.23-1.23h-5.3C148.65,1183.71,148.1,1184.26,148.1,1184.94L148.1,1184.94z M152.38,1190.14
		c-0.45,0-0.88-0.16-1.16-0.62h-0.02l-0.05,0.54h-1.02c0.02-0.26,0.03-0.72,0.03-1.15v-4.45h1.2v2.2h0.02
		c0.23-0.33,0.63-0.55,1.17-0.55c0.92,0,1.6,0.77,1.59,1.95C154.14,1189.45,153.26,1190.14,152.38,1190.14L152.38,1190.14z" />
      <path class="st68" d="M145.8,1193.83v5.28c0,0.69,0.55,1.24,1.24,1.24h5.28c0.68,0,1.24-0.55,1.24-1.24v-5.28
		c0-0.68-0.56-1.24-1.24-1.24h-5.28C146.36,1192.59,145.8,1193.15,145.8,1193.83L145.8,1193.83z M149.9,1197.47
		c0.28,0,0.51-0.04,0.69-0.12l0.14,0.89c-0.21,0.09-0.62,0.18-1.07,0.18c-1.25,0-2.04-0.77-2.04-1.98c0-1.13,0.77-2.05,2.21-2.05
		c0.32,0,0.66,0.05,0.92,0.15l-0.19,0.89c-0.14-0.06-0.36-0.12-0.67-0.12c-0.63,0-1.04,0.45-1.03,1.08
		C148.84,1197.1,149.32,1197.47,149.9,1197.47L149.9,1197.47z" />
      <path class="st68"
        d="M152.48,1186.94c-0.32,0-0.62,0.25-0.7,0.59c-0.02,0.07-0.02,0.14-0.02,0.22v0.57c0,0.08,0.01,0.15,0.02,0.21
		c0.08,0.33,0.36,0.57,0.7,0.57c0.51,0,0.83-0.39,0.83-1.09C153.31,1187.41,153.04,1186.94,152.48,1186.94L152.48,1186.94z" />
      <path class="st68" d="M149.31,1179.48c0,0.31,0.2,0.46,0.47,0.46c0.3,0,0.54-0.2,0.62-0.44c0.02-0.06,0.02-0.14,0.02-0.21v-0.41
		C149.8,1178.87,149.31,1179.02,149.31,1179.48L149.31,1179.48z" />
      <g class="st5">
        <path class="st68" d="M745.82,1234.39h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L745.82,1234.39z M746.82,1235.92h-0.04
			l-2.03,6.93h4.16L746.82,1235.92z" />
        <path class="st68" d="M758.52,1234.39H760v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V1234.39z M756.81,1239.32c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C758.52,1241.27,758.45,1239.32,756.81,1239.32z" />
        <path class="st68" d="M762.46,1242.98c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C763.99,1247.57,762.46,1246.99,762.46,1242.98z M767.83,1242.35c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C767.45,1246.36,767.83,1245.3,767.83,1242.35z" />
        <path class="st68" d="M773.16,1247.39h-1.48v-13h1.48V1247.39z" />
        <path class="st68" d="M777.15,1243.32c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H777.15
			z M780.7,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H780.7z" />
        <path class="st68" d="M787.39,1247.57c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C790.56,1246.8,789.2,1247.57,787.39,1247.57z" />
        <path class="st68" d="M797.46,1241.21c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H797.46z" />
        <path class="st68" d="M803.14,1243.32c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H803.14
			z M806.69,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H806.69z" />
        <path class="st68" d="M815.64,1247.39v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H815.64z" />
        <path class="st68"
          d="M819.87,1238.3v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H819.87z" />
        <path class="st68" d="M827.39,1247.57c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C830.56,1246.8,829.19,1247.57,827.39,1247.57z" />
      </g>
      <path class="st69" d="M754.25,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.16-14.4,32.16-32.17c0-17.76-14.4-32.16-32.16-32.16
		S754.25,1165.36,754.25,1183.12L754.25,1183.12z" />
      <path class="st70" d="M754.25,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.16-14.4,32.16-32.17c0-17.76-14.4-32.16-32.16-32.16
		S754.25,1165.36,754.25,1183.12L754.25,1183.12z" />
      <path class="st68" d="M792.09,1195.83v-7.1v-1.89v-5.38c-1.02,0.79-1.72,1.91-1.91,3.21c-0.1,0.71-0.71,1.22-1.4,1.22
		c-0.07,0-0.13,0-0.2-0.01c-0.78-0.11-1.32-0.83-1.21-1.6c0.56-4,4.14-6.9,8.5-6.9s7.94,2.9,8.5,6.9c0.11,0.77-0.43,1.49-1.21,1.6
		s-1.49-0.43-1.6-1.21c-0.18-1.3-0.88-2.42-1.91-3.21v5.38v1.89v7.1c0,0.78-0.63,1.42-1.42,1.42c-0.78,0-1.42-0.64-1.42-1.42v-7.1
		h-1.89v7.1c0,0.78-0.64,1.42-1.42,1.42C792.72,1197.25,792.09,1196.61,792.09,1195.83L792.09,1195.83z" />
      <path class="st68" d="M795.87,1175.49c-2.09,0-3.78-1.69-3.78-3.78s1.69-3.79,3.78-3.79s3.78,1.7,3.78,3.79
		S797.96,1175.49,795.87,1175.49L795.87,1175.49z" />
      <path class="st68" d="M777.9,1171.72c5.39,0,9.46,3.84,9.46,8.97c0,0.79-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.63-1.42-1.42
		c0-2.35-1.28-4.28-3.25-5.32l2.18,11.35c0.07,0.57-0.37,1.07-0.94,1.07h-0.82v8.04c0,0.78-0.64,1.42-1.42,1.42
		c-0.78,0-1.42-0.64-1.42-1.42v-8.04h-1.89v8.04c0,0.78-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.64-1.42-1.42v-8.04h-0.82
		c-0.57,0-1.01-0.5-0.94-1.07l2.18-11.36c-1.98,1.05-3.26,2.97-3.26,5.33c0,0.79-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.63-1.42-1.42
		C768.45,1175.56,772.51,1171.72,777.9,1171.72L777.9,1171.72z" />
      <path class="st68" d="M777.91,1169.81c-2.09,0-3.78-1.69-3.78-3.78c0-2.09,1.69-3.78,3.78-3.78s3.78,1.69,3.78,3.78
		C781.69,1168.12,779.99,1169.81,777.91,1169.81L777.91,1169.81z" />
      <g class="st5">
        <path class="st68" d="M943.57,1239.73v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H943.57z" />
        <path class="st68" d="M957.34,1239.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H957.34z" />
        <path class="st68" d="M960.36,1230.64h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.85,9.09h-1.93L960.36,1230.64z" />
        <path class="st68" d="M969.27,1226.73h1.66v1.58h-1.66V1226.73z M970.84,1239.73h-1.48v-9.09h1.48V1239.73z" />
        <path class="st68" d="M974.92,1232.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1232.01z" />
        <path class="st68" d="M979.13,1235.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			C980.67,1239.91,979.13,1239.34,979.13,1235.32z M984.5,1234.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03
			c0,2.95,0.38,4.01,1.91,4.01C984.12,1238.71,984.5,1237.65,984.5,1234.69z" />
        <path class="st68" d="M993.32,1239.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.86,1.44-1.86,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H993.32z" />
        <path class="st68" d="M1001.85,1239.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1001.85z" />
        <path class="st68" d="M1011.82,1235.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1011.82z M1015.37,1234.55c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1015.37z" />
        <path class="st68" d="M1024.32,1239.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1024.32z" />
        <path class="st68"
          d="M1028.54,1230.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.41,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1028.54z" />
        <path class="st68" d="M1042.06,1238.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1238.42z M1038.73,1237.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1040.62,1235.23,1038.73,1235.11,1038.73,1237.03z" />
        <path class="st68" d="M1051.32,1239.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1051.32z" />
        <path class="st68" d="M1060.19,1226.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V1226.73z M1058.48,1231.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1060.19,1233.61,1060.12,1231.67,1058.48,1231.67z" />
      </g>
      <g class="st5">
        <path class="st68" d="M953.15,1255.16c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H953.15z" />
        <path class="st68" d="M958.84,1261.34h-1.48v-13h1.48V1261.34z" />
        <path class="st68" d="M961.27,1248.34h1.66v1.58h-1.66V1248.34z M962.83,1261.34h-1.48v-9.09h1.48V1261.34z" />
        <path class="st68" d="M969.85,1261.34v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H969.85z" />
        <path class="st68" d="M983.07,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M979.74,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C981.63,1256.83,979.74,1256.71,979.74,1258.63z" />
        <path class="st68"
          d="M987.55,1252.24v-1.75l1.48-0.67v2.41H991v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H987.55z" />
        <path class="st68" d="M993.83,1257.27c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H993.83
			z M997.38,1256.15c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H997.38z" />
        <path class="st68" d="M1010.14,1255.16c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86
			c1.82,0,2.88,1.06,2.79,3.1H1010.14z" />
        <path class="st68" d="M1019.32,1261.34v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1019.32z" />
        <path class="st68" d="M1028.07,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M1024.74,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1026.63,1256.83,1024.74,1256.71,1024.74,1258.63z" />
        <path class="st68" d="M1037.32,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1037.32z" />
        <path class="st68" d="M1046.19,1252.24h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66
			c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83
			c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V1252.24z M1044.46,1253.29c-1.67,0-1.73,2.02-1.73,3.22
			c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1046.23,1255.39,1046.32,1253.29,1044.46,1253.29z" />
        <path class="st68" d="M1051.83,1257.27c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62
			c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77
			H1051.83z M1055.37,1256.15c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1055.37z" />
      </g>
      <path class="st69" d="M968.61,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C983.01,1150.96,968.61,1165.36,968.61,1183.12L968.61,1183.12z" />
      <path class="st70" d="M968.61,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C983.01,1150.96,968.61,1165.36,968.61,1183.12L968.61,1183.12z" />
      <path class="st68" d="M989.67,1186.47l3.58-0.89l1.78-4.47l2.68-2.69l2.69,0.9l1.78-1.79l1.79,1.79l1.79,4.47l3.58,1.79l2.96,8.15
		c-0.09,0.01-0.18,0.02-0.29,0.02c-0.83,0-1.15-0.31-1.86-1c-0.84-0.8-2.1-2.01-4.39-2.01c-2.3,0-3.56,1.21-4.39,2.01
		c-0.71,0.69-1.04,1-1.87,1s-1.16-0.31-1.87-1c-0.81-0.77-2.03-1.94-4.21-2l-0.17-0.7l0.89-2.69l-3.58,0.9l-1.4,4.2
		c-0.11,0.1-0.21,0.2-0.31,0.29c-0.71,0.69-1.03,1-1.86,1c-0.08,0-0.16,0.01-0.24,0.02L989.67,1186.47L989.67,1186.47z
		 M997.71,1185.58l3.58,3.57v-2.68l-2.68-3.58v-2.68l-1.79,1.79l-1.79,3.58L997.71,1185.58L997.71,1185.58z" />
      <path class="st68" d="M986.99,1197.39c1.94,0,2.95-0.97,3.77-1.76c0.75-0.72,1.29-1.24,2.48-1.24s1.74,0.52,2.49,1.24
		c0.82,0.79,1.83,1.76,3.77,1.76s2.95-0.97,3.77-1.76c0.75-0.72,1.3-1.24,2.49-1.24s1.73,0.52,2.48,1.24
		c0.82,0.79,1.84,1.76,3.77,1.76c1.94,0,2.96-0.97,3.78-1.76c0.75-0.72,1.29-1.24,2.48-1.24s1.74,0.52,2.49,1.24
		c0.82,0.79,1.83,1.76,3.77,1.76c0.51,0,0.93-0.41,0.93-0.93c0-0.51-0.42-0.92-0.93-0.92c-1.19,0-1.73-0.53-2.49-1.25
		c-0.81-0.78-1.83-1.76-3.77-1.76s-2.95,0.98-3.77,1.76c-0.75,0.72-1.3,1.25-2.49,1.25s-1.73-0.53-2.48-1.25
		c-0.82-0.78-1.84-1.76-3.77-1.76c-1.94,0-2.96,0.98-3.77,1.76c-0.76,0.72-1.3,1.25-2.49,1.25s-1.73-0.53-2.49-1.25
		c-0.81-0.78-1.83-1.76-3.77-1.76c-1.93,0-2.95,0.98-3.77,1.76c-0.75,0.72-1.29,1.25-2.48,1.25c-0.51,0-0.93,0.41-0.93,0.92
		C986.06,1196.98,986.48,1197.39,986.99,1197.39L986.99,1197.39z" />
      <path class="st68" d="M986.99,1200.97c1.94,0,2.95-0.98,3.77-1.76c0.75-0.72,1.29-1.25,2.48-1.25s1.74,0.53,2.49,1.25
		c0.82,0.78,1.83,1.76,3.77,1.76s2.95-0.98,3.77-1.76c0.75-0.72,1.3-1.25,2.49-1.25s1.73,0.53,2.48,1.25
		c0.82,0.78,1.84,1.76,3.77,1.76c1.94,0,2.96-0.98,3.78-1.76c0.75-0.72,1.29-1.25,2.48-1.25s1.74,0.53,2.49,1.25
		c0.82,0.78,1.83,1.76,3.77,1.76c0.51,0,0.93-0.42,0.93-0.93s-0.42-0.93-0.93-0.93c-1.19,0-1.73-0.52-2.49-1.24
		c-0.81-0.79-1.83-1.76-3.77-1.76s-2.95,0.97-3.77,1.76c-0.75,0.72-1.3,1.24-2.49,1.24s-1.73-0.52-2.48-1.24
		c-0.82-0.79-1.84-1.76-3.77-1.76c-1.94,0-2.96,0.97-3.77,1.76c-0.76,0.72-1.3,1.24-2.49,1.24s-1.73-0.52-2.49-1.24
		c-0.81-0.79-1.83-1.76-3.77-1.76c-1.93,0-2.95,0.97-3.77,1.76c-0.75,0.72-1.29,1.24-2.48,1.24c-0.51,0-0.93,0.42-0.93,0.93
		S986.48,1200.97,986.99,1200.97L986.99,1200.97z" />
      <path class="st68" d="M991.41,1169.21c0.44,0,0.81-0.37,0.81-0.81v-1.62c0-0.45-0.37-0.81-0.81-0.81c-0.45,0-0.81,0.36-0.81,0.81
		v1.62C990.6,1168.84,990.96,1169.21,991.41,1169.21L991.41,1169.21z" />
      <path class="st68" d="M990.6,1177.03v1.62c0,0.45,0.36,0.81,0.81,0.81c0.44,0,0.81-0.36,0.81-0.81v-1.62
		c0-0.45-0.37-0.81-0.81-0.81C990.96,1176.22,990.6,1176.58,990.6,1177.03L990.6,1177.03z" />
      <path class="st68" d="M995.03,1170.23l1.15-1.14c0.31-0.32,0.31-0.83,0-1.15c-0.32-0.31-0.83-0.31-1.15,0l-1.14,1.15
		c-0.32,0.31-0.32,0.83,0,1.14C994.2,1170.55,994.72,1170.55,995.03,1170.23L995.03,1170.23z" />
      <path class="st68" d="M987.78,1175.19l-1.14,1.15c-0.32,0.31-0.32,0.83,0,1.14c0.31,0.32,0.83,0.32,1.14,0l1.15-1.14
		c0.31-0.32,0.31-0.83,0-1.15C988.61,1174.88,988.1,1174.88,987.78,1175.19L987.78,1175.19z" />
      <path class="st68" d="M994.92,1172.71c0,0.45,0.36,0.81,0.81,0.81h1.61c0.45,0,0.81-0.36,0.81-0.81c0-0.44-0.36-0.81-0.81-0.81
		h-1.61C995.28,1171.9,994.92,1172.27,994.92,1172.71L994.92,1172.71z" />
      <path class="st68" d="M985.47,1173.52h1.62c0.45,0,0.81-0.36,0.81-0.81c0-0.44-0.36-0.81-0.81-0.81h-1.62
		c-0.45,0-0.81,0.37-0.81,0.81C984.66,1173.16,985.02,1173.52,985.47,1173.52L985.47,1173.52z" />
      <path class="st68" d="M993.89,1175.19c-0.32,0.32-0.32,0.83,0,1.15l1.14,1.14c0.32,0.32,0.83,0.32,1.15,0
		c0.31-0.31,0.31-0.83,0-1.14l-1.15-1.15C994.72,1174.88,994.2,1174.88,993.89,1175.19L993.89,1175.19z" />
      <path class="st68" d="M987.78,1170.23c0.32,0.32,0.83,0.32,1.15,0c0.31-0.31,0.31-0.83,0-1.14l-1.15-1.15
		c-0.31-0.31-0.83-0.31-1.14,0c-0.32,0.32-0.32,0.83,0,1.15L987.78,1170.23L987.78,1170.23z" />
      <path class="st68" d="M991.41,1175.14c1.34,0,2.43-1.09,2.43-2.43c0-1.34-1.09-2.43-2.43-2.43c-1.34,0-2.43,1.09-2.43,2.43
		S990.07,1175.14,991.41,1175.14L991.41,1175.14z" />
      <path class="st68" d="M1018.65,1176.03c0-1.36-1.11-2.46-2.46-2.46c-1.36,0-2.46,1.1-2.46,2.46v9.49
		c-0.73,0.68-1.14,1.62-1.14,2.62c0,1.98,1.62,3.59,3.6,3.59s3.59-1.61,3.59-3.59c0-1-0.41-1.94-1.13-2.62L1018.65,1176.03
		L1018.65,1176.03z M1016.19,1190.6c-1.36,0-2.46-1.11-2.46-2.46c0-0.75,0.34-1.45,0.92-1.92l0.21-0.17v-10.02
		c0-0.73,0.6-1.33,1.33-1.33s1.32,0.6,1.32,1.33v10.02l0.22,0.17c0.58,0.47,0.92,1.17,0.92,1.92
		C1018.65,1189.49,1017.54,1190.6,1016.19,1190.6L1016.19,1190.6z" />
      <path class="st68"
        d="M1016.76,1186.74v-9.96c0-0.31-0.26-0.56-0.57-0.56s-0.57,0.25-0.57,0.56v9.96c-0.55,0.22-0.95,0.76-0.95,1.4
		c0,0.83,0.68,1.51,1.52,1.51c0.83,0,1.51-0.68,1.51-1.51C1017.7,1187.5,1017.31,1186.96,1016.76,1186.74L1016.76,1186.74z" />
      <path class="st68" d="M1024.89,1177.35h-1.7v-1.7c0-0.31-0.25-0.57-0.57-0.57c-0.31,0-0.57,0.26-0.57,0.57v1.7h-1.7
		c-0.31,0-0.57,0.26-0.57,0.57s0.26,0.57,0.57,0.57h1.7v1.7c0,0.31,0.26,0.57,0.57,0.57c0.32,0,0.57-0.26,0.57-0.57v-1.7h1.7
		c0.32,0,0.57-0.26,0.57-0.57S1025.21,1177.35,1024.89,1177.35L1024.89,1177.35z" />
      <g class="st5">
        <path class="st68" d="M1187.38,1233.76v5.98h-1.66v-13h4.48c2.3,0,3.11,1.62,3.11,3.24c0,1.53-0.85,2.7-2.38,2.97v0.04
			c1.49,0.23,2.03,0.74,2.12,3.35c0.02,0.56,0.2,2.59,0.45,3.4h-1.73c-0.47-0.9-0.36-2.59-0.5-4.32c-0.13-1.58-1.4-1.66-1.96-1.66
			H1187.38z M1187.38,1232.32h2.48c1.19,0,1.76-1.03,1.76-2.16c0-0.94-0.47-1.98-1.75-1.98h-2.5V1232.32z" />
        <path class="st68" d="M1195.47,1226.73h1.66v1.58h-1.66V1226.73z M1197.04,1239.73h-1.48v-9.09h1.48V1239.73z" />
        <path class="st68" d="M1202.28,1239.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1205.45,1239.14,1204.08,1239.91,1202.28,1239.91z" />
        <path class="st68" d="M1209.07,1239.73h-1.48v-13h1.48v7.83h0.04l2.77-3.92h1.8l-3.02,3.91l3.56,5.19h-1.87l-3.24-5.1h-0.04
			V1239.73z" />
        <path class="st68" d="M1218.26,1239.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1221.43,1239.14,1220.06,1239.91,1218.26,1239.91z" />
        <path class="st68" d="M1232.25,1238.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1238.42z M1228.92,1237.03c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1230.81,1235.23,1228.92,1235.11,1228.92,1237.03z" />
        <path class="st68" d="M1241.5,1239.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1241.5z" />
        <path class="st68" d="M1250.38,1226.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57
			c0-2.27,0.07-4.88,3.01-4.88c0.87,0,1.5,0.38,2,1.1h0.05V1226.73z M1248.67,1231.67c-1.58,0-1.8,1.26-1.8,3.69
			c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1250.38,1233.61,1250.3,1231.67,1248.67,1231.67z" />
      </g>
      <g class="st5">
        <path class="st68" d="M1144.53,1261.34v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08
			h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1144.53z" />
        <path class="st68" d="M1153.46,1252.24h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1252.24z" />
        <path class="st68" d="M1162.06,1261.34v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61
			c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31
			c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3
			c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1162.06z" />
        <path class="st68" d="M1175.27,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M1171.94,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1173.83,1256.83,1171.94,1256.71,1171.94,1258.63z" />
        <path class="st68" d="M1184.52,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1184.52z" />
        <path class="st68" d="M1188.46,1248.34h1.66v1.58h-1.66V1248.34z M1190.03,1261.34h-1.48v-9.09h1.48V1261.34z" />
        <path class="st68"
          d="M1192.75,1252.24v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1192.75z" />
        <path class="st68" d="M1202.27,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M1198.94,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1200.83,1256.83,1198.94,1256.71,1198.94,1258.63z" />
        <path class="st68" d="M1208.12,1253.61h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05
			c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1253.61z" />
        <path class="st68" d="M1212.46,1248.34h1.66v1.58h-1.66V1248.34z M1214.02,1261.34h-1.48v-9.09h1.48V1261.34z" />
        <path class="st68" d="M1221.26,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M1217.93,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1219.82,1256.83,1217.93,1256.71,1217.93,1258.63z" />
        <path class="st68" d="M1230.51,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.95,0,2.43,1.17,2.43,2.97v6.3H1230.51z" />
        <path class="st68" d="M1241.26,1261.52c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39
			c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46
			c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C1244.43,1260.74,1243.06,1261.52,1241.26,1261.52z" />
        <path class="st68" d="M1246.44,1248.34h1.66v1.58h-1.66V1248.34z M1248.01,1261.34h-1.48v-9.09h1.48V1261.34z" />
        <path class="st68"
          d="M1250.72,1252.24v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1250.72z" />
        <path class="st68" d="M1260.43,1252.24h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28
			c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1252.24z" />
        <path class="st68" d="M1269.25,1260.02h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99
			c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74
			c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.02z M1265.92,1258.63c0,0.88,0.43,1.67,1.42,1.67
			c0.9,0,2.02-0.56,1.87-3.49C1267.81,1256.83,1265.92,1256.71,1265.92,1258.63z" />
        <path class="st68"
          d="M1273.73,1252.24v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31
			c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.5v-1.12H1273.73z" />
        <path class="st68" d="M1278.44,1248.34h1.66v1.58h-1.66V1248.34z M1280.01,1261.34h-1.48v-9.09h1.48V1261.34z" />
        <path class="st68" d="M1282.31,1256.92c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59
			S1282.31,1260.94,1282.31,1256.92z M1287.68,1256.29c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01
			S1287.68,1259.25,1287.68,1256.29z" />
        <path class="st68" d="M1296.5,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2
			c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1296.5z" />
      </g>
      <path class="st69" d="M1184.8,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C1199.2,1150.96,1184.8,1165.36,1184.8,1183.12L1184.8,1183.12z" />
      <path class="st70" d="M1184.8,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17
		c0-17.76-14.4-32.16-32.17-32.16C1199.2,1150.96,1184.8,1165.36,1184.8,1183.12L1184.8,1183.12z" />
      <path class="st68" d="M1222.43,1199.85L1222.43,1199.85v-0.03v-0.3v-7.79c0-0.17,0.07-0.34,0.2-0.46l5.99-5.96
		c0.19-0.2,0.44-0.34,0.71-0.4c0.25-0.05,0.5-0.05,0.75,0.02c0.23,0.06,0.44,0.18,0.62,0.34c0.58,0.56,0.59,1.46,0.03,2.03
		l-2.64,2.62c-0.1,0.1-0.1,0.27,0.01,0.38c0.1,0.09,0.26,0.09,0.36-0.01l2.65-2.63c0.77-0.77,0.75-2-0.04-2.75
		c-0.16-0.16-0.35-0.28-0.56-0.36c-0.24-0.1-0.42-0.33-0.42-0.6v-5.41c0-0.8,0.67-1.45,1.49-1.45c0.83,0,1.49,0.65,1.49,1.45v10.19
		c0,0.33-0.13,0.63-0.34,0.88l-5.03,6.46c-0.09,0.11-0.14,0.25-0.14,0.4v3.12l0,0v0.26c0,0.43-0.35,0.77-0.78,0.77h-3.57
		C1222.78,1200.62,1222.43,1200.28,1222.43,1199.85L1222.43,1199.85z" />
      <path class="st68" d="M1211.49,1199.85L1211.49,1199.85v-0.03v-0.3v-7.79c0-0.17-0.07-0.34-0.19-0.46l-6-5.96
		c-0.19-0.2-0.44-0.34-0.71-0.4c-0.25-0.05-0.5-0.05-0.75,0.02c-0.23,0.06-0.44,0.18-0.62,0.34c-0.58,0.56-0.59,1.46-0.03,2.03
		l2.64,2.62c0.1,0.1,0.1,0.27-0.01,0.38c-0.1,0.09-0.26,0.09-0.36-0.01l-2.65-2.63c-0.77-0.77-0.75-2,0.04-2.75
		c0.17-0.16,0.36-0.28,0.56-0.36c0.25-0.1,0.42-0.33,0.42-0.6v-5.41c0-0.8-0.67-1.45-1.49-1.45s-1.49,0.65-1.49,1.45v10.19
		c0,0.33,0.13,0.63,0.34,0.88l5.04,6.46c0.09,0.11,0.14,0.25,0.14,0.4v3.12l0,0v0.26c0,0.43,0.34,0.77,0.77,0.77h3.57
		C1211.14,1200.62,1211.49,1200.28,1211.49,1199.85L1211.49,1199.85z" />
      <path class="st68" d="M1226.98,1174.54l0.04-0.03c0.01,0.05,0.02,0.11,0.04,0.17L1226.98,1174.54L1226.98,1174.54z
		 M1213.76,1171.87l0.1-0.09l0.15,0.09l-0.12,0.11L1213.76,1171.87L1213.76,1171.87z M1214.06,1172.15v0.2h-0.32l-0.09-0.13v-0.19
		h0.02L1214.06,1172.15L1214.06,1172.15z M1212.67,1171.81h0.34l-0.44,0.61l-0.18-0.1l0.04-0.25L1212.67,1171.81L1212.67,1171.81z
		 M1213.48,1172.22v0.2l-0.14,0.15h-0.33l0.05-0.23l0.16-0.01l0.03-0.08L1213.48,1172.22L1213.48,1172.22z M1213.39,1171.73v-0.25
		l0.21,0.19L1213.39,1171.73L1213.39,1171.73z M1213.56,1171.81v0.2l-0.15,0.1l-0.2,0.04v-0.34H1213.56L1213.56,1171.81z
		 M1213.28,1171.51v0.22h-0.62l-0.23-0.07l0.06-0.15l0.29-0.12h0.41v0.12H1213.28L1213.28,1171.51z M1211.84,1170.74l0.27-0.13
		l0.25,0.06l-0.09,0.33l-0.26,0.08L1211.84,1170.74L1211.84,1170.74z M1226.82,1174.02h-0.83l-0.5-0.37l-0.53,0.05v0.32h-0.17
		l-0.18-0.12l-0.91-0.24v-0.59l-1.16,0.09l-0.36,0.2h-0.46l-0.23-0.03l-0.56,0.31v0.59l-1.14,0.82l0.1,0.35h0.23l-0.06,0.34
		l-0.16,0.06l-0.01,0.87l0.98,1.13h0.43l0.03-0.07h0.77l0.22-0.21h0.44l0.24,0.24l0.66,0.07l-0.09,0.87l0.73,1.28l-0.39,0.73
		l0.03,0.34l0.3,0.3v0.83l0.39,0.53v0.69h0.35c-1.9,2.32-4.79,3.82-8.02,3.82c-5.7,0-10.33-4.64-10.33-10.34
		c0-1.43,0.29-2.8,0.82-4.04v-0.32l0.37-0.45c0.13-0.24,0.27-0.48,0.41-0.71l0.02,0.19l-0.43,0.52c-0.13,0.25-0.26,0.51-0.37,0.77
		v0.59l0.43,0.2v0.82l0.41,0.7l0.34,0.06l0.04-0.24l-0.39-0.61l-0.08-0.6h0.23l0.1,0.61l0.57,0.84l-0.15,0.26l0.36,0.56l0.91,0.22
		v-0.14l0.36,0.05l-0.04,0.26l0.29,0.05l0.43,0.12l0.62,0.7l0.79,0.06l0.08,0.65l-0.54,0.37l-0.02,0.58l-0.08,0.35l0.78,0.98
		l0.06,0.33c0,0,0.28,0.08,0.32,0.08c0.03,0,0.63,0.46,0.63,0.46v1.77l0.22,0.06l-0.15,0.81l0.36,0.48l-0.07,0.81l0.48,0.84
		l0.61,0.53l0.62,0.01l0.06-0.19l-0.45-0.38l0.02-0.19l0.08-0.24l0.02-0.23l-0.31-0.01l-0.15-0.19l0.25-0.25l0.04-0.18l-0.29-0.08
		l0.02-0.17l0.4-0.07l0.62-0.29l0.21-0.38l0.64-0.82l-0.15-0.65l0.2-0.34l0.59,0.02l0.4-0.32l0.13-1.24l0.44-0.56l0.08-0.36
		l-0.4-0.14l-0.27-0.43l-0.91-0.01l-0.72-0.27l-0.03-0.52l-0.25-0.42l-0.65-0.01l-0.38-0.59l-0.33-0.17l-0.02,0.18l-0.61,0.04
		l-0.22-0.31l-0.64-0.13l-0.52,0.61l-0.82-0.14l-0.06-0.93l-0.61-0.11l0.25-0.45l-0.07-0.26l-0.79,0.53l-0.5-0.06l-0.18-0.39
		l0.11-0.4l0.28-0.51l0.63-0.32h1.22l-0.01,0.37l0.44,0.21l-0.04-0.64l0.32-0.32l0.64-0.42l0.04-0.29l0.64-0.66l0.67-0.37
		l-0.06-0.05l0.46-0.43l0.17,0.04l0.07,0.1l0.18-0.2l0.04-0.02l-0.19-0.02l-0.19-0.07v-0.18l0.1-0.09h0.22l0.11,0.05l0.09,0.18
		l0.11-0.02v-0.01l0.03,0.01l0.32-0.05l0.04-0.16l0.18,0.05v0.17l-0.16,0.11l0.02,0.19l0.57,0.17v0.01l0.14-0.01v-0.25l-0.45-0.2
		l-0.03-0.13l0.38-0.12l0.02-0.37l-0.4-0.24l-0.02-0.6l-0.54,0.26h-0.2l0.05-0.46l-0.74-0.18l-0.3,0.23v0.71l-0.55,0.17l-0.22,0.46
		l-0.24,0.04v-0.59l-0.51-0.07l-0.26-0.17l-0.1-0.38l0.92-0.54l0.45-0.14l0.05,0.31l0.25-0.01l0.02-0.16l0.26-0.03v-0.06l-0.11-0.05
		l-0.03-0.16l0.33-0.02l0.19-0.21l0.01-0.01h0.01l0.05-0.06l0.68-0.09l0.3,0.26l-0.78,0.42l1,0.23l0.13-0.33h0.43l0.16-0.29
		l-0.31-0.08v-0.37l-0.97-0.43l-0.67,0.08l-0.38,0.2l0.03,0.48l-0.4-0.06l-0.06-0.27l0.38-0.34l-0.69-0.04l-0.19,0.06l-0.09,0.23
		l0.26,0.05l-0.05,0.25l-0.44,0.03l-0.07,0.17l-0.64,0.02c0,0-0.01-0.36-0.04-0.36c-0.02,0,0.5-0.01,0.5-0.01l0.38-0.37l-0.21-0.1
		l-0.27,0.27l-0.46-0.03l-0.27-0.38h-0.59l-0.61,0.46h0.56l0.05,0.16l-0.14,0.13l0.62,0.02l0.09,0.23l-0.7-0.03l-0.03-0.17
		l-0.44-0.1l-0.23-0.13l-0.52,0.01c1.71-1.24,3.8-1.98,6.07-1.98c2.61,0,5,0.98,6.82,2.58l-0.12,0.22l-0.48,0.19l-0.2,0.22
		l0.05,0.25l0.24,0.04l0.15,0.37l0.43-0.18l0.07,0.5h-0.13l-0.35-0.05l-0.38,0.06l-0.38,0.53l-0.53,0.09l-0.08,0.45l0.23,0.06
		l-0.07,0.29l-0.53-0.11l-0.49,0.11l-0.1,0.27l0.08,0.57l0.29,0.13h0.48l0.32-0.03l0.1-0.26l0.51-0.65l0.33,0.07l0.33-0.3l0.06,0.23
		l0.81,0.54l-0.1,0.14l-0.37-0.02l0.14,0.19l0.23,0.05l0.26-0.1v-0.32l0.11-0.06l-0.09-0.1l-0.54-0.3l-0.14-0.4h0.44l0.15,0.14
		l0.38,0.34l0.02,0.4l0.4,0.42l0.15-0.58l0.27-0.15l0.05,0.48l0.28,0.29l0.53-0.01c0.11,0.27,0.2,0.54,0.28,0.82L1226.82,1174.02
		L1226.82,1174.02z M1211.25,1169.55c0,0,0.22-0.03,0.24-0.03s0,0.22,0,0.22l-0.5,0.03l-0.1-0.11L1211.25,1169.55L1211.25,1169.55z
		 M1210.89,1169.05v-0.02h0.23l0.01-0.07h0.37v0.16l-0.1,0.14h-0.51V1169.05L1210.89,1169.05z M1224.47,1170.3v-0.5
		c0.18,0.19,0.35,0.38,0.51,0.58l-0.2,0.3h-0.71l-0.04-0.15L1224.47,1170.3L1224.47,1170.3z M1226.1,1172.27l0.07-0.08
		c0.08,0.17,0.16,0.34,0.24,0.51h-0.11l-0.2,0.02V1172.27L1226.1,1172.27z M1228.22,1176.77c0-0.33-0.02-0.66-0.05-0.98
		c-0.11-1.07-0.36-2.1-0.75-3.07c-0.03-0.07-0.05-0.14-0.08-0.21c-0.51-1.21-1.24-2.31-2.12-3.27c-0.05-0.06-0.11-0.12-0.17-0.18
		c-0.17-0.17-0.34-0.34-0.52-0.5c-2-1.82-4.66-2.94-7.57-2.94c-2.94,0-5.62,1.14-7.62,2.99c-0.47,0.43-0.9,0.9-1.29,1.4
		c-1.47,1.9-2.35,4.29-2.35,6.87c0,6.21,5.05,11.26,11.26,11.26c4.37,0,8.16-2.5,10.03-6.14c0.4-0.78,0.71-1.61,0.92-2.48
		c0.05-0.22,0.1-0.44,0.14-0.67c0.11-0.64,0.17-1.3,0.17-1.97C1228.22,1176.84,1228.22,1176.81,1228.22,1176.77" />
      <g class="st5">
        <path class="st68" d="M595.3,1112.32c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64
			c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1
			C595.3,1119.78,595.3,1116.1,595.3,1112.32z" />
        <path class="st68" d="M609.1,1109.44v1.3h0.04c0.52-1.16,1.48-1.5,2.62-1.5v2.52c-2.48-0.16-2.52,1.28-2.52,2.28v5.5h-2.82v-10.1
			H609.1z" />
        <path class="st68" d="M612.84,1114.36c0-2.76,0.4-5.12,4.12-5.12s4.12,2.36,4.12,5.12c0,3.16-0.48,5.38-4.12,5.38
			C613.32,1119.74,612.84,1117.52,612.84,1114.36z M618.26,1114.2c0-2.1-0.1-3.16-1.3-3.16s-1.3,1.06-1.3,3.16
			c0,3.08,0.26,3.74,1.3,3.74C618,1117.94,618.26,1117.28,618.26,1114.2z" />
        <path class="st68" d="M625.3,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H625.3z" />
        <path class="st68" d="M634.18,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H634.18z" />
        <path class="st68" d="M645.5,1113.12v2.04h-4.9v-2.04H645.5z" />
        <path class="st68" d="M647.5,1112.32c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64
			c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1
			C647.5,1119.78,647.5,1116.1,647.5,1112.32z" />
        <path class="st68"
          d="M663.56,1118.52h-0.04c-0.28,0.44-0.6,0.76-1,0.94c-0.4,0.2-0.84,0.28-1.38,0.28c-1.34,0-2.52-0.8-2.52-2.2
			v-8.1h2.82v7c0,0.9,0.16,1.56,1.06,1.56c0.9,0,1.06-0.66,1.06-1.56v-7h2.82v8.1c0,0.66,0.04,1.34,0.1,2h-2.92V1118.52z" />
        <path class="st68" d="M667.48,1109.44h1.14v-1.6l2.82-1.26v2.86h1.46v1.74h-1.46v5.4c0,0.76-0.02,1.26,0.9,1.26
			c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V1109.44z" />
        <path class="st68" d="M673.04,1109.44h1.14v-1.6l2.82-1.26v2.86h1.46v1.74H677v5.4c0,0.76-0.02,1.26,0.9,1.26
			c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V1109.44z" />
        <path class="st68" d="M682.8,1105.1v2.22h-2.82v-2.22H682.8z M682.8,1119.54h-2.82v-10.1h2.82V1119.54z" />
        <path class="st68" d="M688.12,1110.46h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1
			h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V1110.46z" />
        <path class="st68" d="M703.02,1109.44v10.52c0,0.7,0.04,3.46-3.84,3.46c-2.1,0-3.9-0.54-3.96-3h2.76c0,0.42,0.06,0.78,0.24,1.02
			c0.18,0.26,0.5,0.4,0.94,0.4c0.7,0,1.04-0.66,1.04-1.68v-1.94h-0.04c-0.42,0.78-1.22,1.18-2.14,1.18c-3.1,0-2.96-2.84-2.96-5.12
			c0-2.22,0.04-5.04,2.98-5.04c1,0,1.86,0.44,2.26,1.38h0.04v-1.18H703.02z M699.04,1117.66c1.02,0,1.16-1.06,1.16-3.2
			c0-2.22-0.1-3.48-1.14-3.48c-1.06,0-1.24,0.74-1.24,3.82C697.82,1115.74,697.68,1117.66,699.04,1117.66z" />
        <path class="st68" d="M709.88,1119.54v-14.44h3.02v14.44H709.88z" />
        <path class="st68" d="M717.52,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H717.52z" />
        <path class="st68" d="M726.4,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48c0.56,0,1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H726.4z" />
        <path class="st68" d="M738,1118.52h-0.04c-0.28,0.44-0.6,0.76-1,0.94c-0.4,0.2-0.84,0.28-1.38,0.28c-1.34,0-2.52-0.8-2.52-2.2
			v-8.1h2.82v7c0,0.9,0.16,1.56,1.06,1.56s1.06-0.66,1.06-1.56v-7h2.82v8.1c0,0.66,0.04,1.34,0.1,2H738V1118.52z" />
        <path class="st68" d="M745.66,1114.94c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8H751c-0.04,1.1-0.4,2-1.08,2.62
			c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H745.66z
			 M748.24,1113.36c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H748.24z" />
        <path class="st68" d="M755.28,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48c0.56,0,1.04-0.36,1.04-1.04
			c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3
			c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08
			c-2.46,0-4.1-0.62-3.94-3.44H755.28z" />
      </g>
      <path class="st71" d="M20,0C8.95,0,0,8.95,0,20v1270.5c0,11.05,8.95,20,20,20h1315c11.05,0,20-8.95,20-20V20c0-11.05-8.95-20-20-20
		H20L20,0z" />
      <g class="st5">
        <path class="st3" d="M140.58,58.84V33.56h13.79v3.88h-8.51v6.23h7.84v3.88h-7.84v7.39h8.79v3.89H140.58z" />
        <path class="st3" d="M166.48,57.05h-0.07c-0.49,0.77-1.05,1.33-1.75,1.65c-0.7,0.35-1.47,0.49-2.42,0.49
			c-2.35,0-4.41-1.4-4.41-3.85V41.16h4.94v12.25c0,1.58,0.28,2.73,1.86,2.73s1.85-1.16,1.85-2.73V41.16h4.94v14.18
			c0,1.15,0.07,2.34,0.18,3.5h-5.11V57.05z" />
        <path class="st3" d="M180.03,41.16v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94
			V41.16H180.03z" />
        <path class="st3" d="M186.57,49.77c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42
			S186.57,55.3,186.57,49.77z M196.06,49.49c0-3.68-0.18-5.53-2.28-5.53s-2.28,1.86-2.28,5.53c0,5.39,0.46,6.54,2.28,6.54
			S196.06,54.88,196.06,49.49z" />
        <path class="st3" d="M209.18,41.16v1.96h0.07c0.91-1.71,2.28-2.31,4.17-2.31c5.11,0,4.94,5.67,4.94,9.31
			c0,3.57,0.14,9.07-4.83,9.07c-1.79,0-3.01-0.52-4.03-2.03h-0.07v9.28h-4.94V41.16H209.18z M213.52,49.84
			c0-3.54,0.04-5.99-2.1-5.99c-2.03,0-2,2.45-2,5.99c0,4.45,0.32,6.3,2,6.3C213.21,56.14,213.52,54.29,213.52,49.84z" />
        <path class="st3" d="M226.54,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5.01c-0.07,1.92-0.7,3.5-1.89,4.58
			c-1.15,1.08-2.91,1.71-5.22,1.71c-6.37,0-7.21-3.88-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H226.54z
			 M231.06,48.02c0-1.71,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H231.06z" />
        <path class="st3" d="M260.67,55.55c0,1.08,0.14,2.21,0.25,3.29h-4.59l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7
			c-3.43,0-4.69-2.55-4.69-5.63c0-5.85,4.52-6.09,9.1-6.02v-1.36c0-1.51-0.21-2.59-2-2.59c-1.72,0-1.86,1.29-1.86,2.7h-4.83
			c0-2.13,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M251.56,53.34
			c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C253.39,50.4,251.56,50.19,251.56,53.34z" />
        <path class="st3" d="M269.69,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M291.08,58.84v-1.96h-0.07c-0.91,1.71-2.27,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31
			c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.53,4.03,2.03h0.07v-9.28h4.94v25.27H291.08z M290.84,49.84c0-3.54,0.04-5.99-2-5.99
			c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.31,6.3,2.1,6.3C290.52,56.14,290.84,54.29,290.84,49.84z" />
        <path class="st3" d="M307.53,46.2c0-6.69,0-13.06,8.72-13.06c5.39,0,7.56,2.97,7.35,8.4h-5.18c0-3.36-0.59-4.62-2.17-4.62
			c-2.98,0-3.36,2.8-3.36,9.28c0,6.48,0.38,9.28,3.36,9.28c2.45,0,2.35-3.15,2.42-5.15h5.22c0,6.76-2.7,8.93-7.63,8.93
			C307.53,59.26,307.53,52.82,307.53,46.2z" />
        <path class="st3" d="M331.54,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5.01c-0.07,1.92-0.7,3.5-1.89,4.58
			c-1.15,1.08-2.91,1.71-5.22,1.71c-6.37,0-7.21-3.88-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H331.54z
			 M336.06,48.02c0-1.71,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H336.06z" />
        <path class="st3" d="M349.42,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M359.99,41.16h2v-2.8l4.94-2.21v5.01h2.56v3.04h-2.56v9.45c0,1.33-0.03,2.21,1.58,2.21
			c0.32,0,0.63,0,0.88-0.07v3.04c-0.67,0.07-1.37,0.17-2.56,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.2h-2V41.16z" />
        <path class="st3" d="M376.41,41.16v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94
			V41.16H376.41z" />
        <path class="st3" d="M396.78,55.55c0,1.08,0.14,2.21,0.25,3.29h-4.59l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7
			c-3.43,0-4.69-2.55-4.69-5.63c0-5.85,4.52-6.09,9.1-6.02v-1.36c0-1.51-0.21-2.59-2-2.59c-1.71,0-1.85,1.29-1.85,2.7h-4.83
			c0-2.13,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M387.68,53.34
			c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C389.5,50.4,387.68,50.19,387.68,53.34z" />
        <path class="st3" d="M406.23,33.56v25.27h-4.94V33.56H406.23z" />
        <path class="st3" d="M416.69,58.84l7-25.27h6.97l6.86,25.27h-5.57l-1.4-5.6h-7.21l-1.44,5.6H416.69z M426.88,38.43h-0.07
			l-2.42,10.92h5.04L426.88,38.43z" />
        <path class="st3" d="M443.64,53.17c-0.04,0.81,0,1.58,0.25,2.14c0.28,0.56,0.8,0.84,1.79,0.84c0.98,0,1.82-0.63,1.82-1.82
			c0-3.75-8.68-2.91-8.68-8.54c0-3.82,3.78-4.97,6.97-4.97c3.36,0,6.41,1.61,6.13,5.43h-4.83c0-1.22-0.14-1.96-0.49-2.28
			c-0.32-0.31-0.74-0.38-1.26-0.38c-1.08,0-1.68,0.7-1.68,1.89c0,2.8,8.68,2.66,8.68,8.33c0,3.08-2.52,5.39-6.62,5.39
			c-4.31,0-7.18-1.08-6.9-6.02H443.64z" />
        <path class="st3" d="M460.65,33.56v3.88h-4.94v-3.88H460.65z M460.65,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3" d="M478.43,55.55c0,1.08,0.14,2.21,0.25,3.29h-4.58l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7
			c-3.43,0-4.69-2.55-4.69-5.63c0-5.85,4.51-6.09,9.1-6.02v-1.36c0-1.51-0.21-2.59-2-2.59c-1.71,0-1.86,1.29-1.86,2.7h-4.83
			c0-2.13,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M469.33,53.34
			c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C471.15,50.4,469.33,50.19,469.33,53.34z" />
        <path class="st3" d="M490.3,46.2c0-6.69,0-13.06,8.72-13.06c5.39,0,7.56,2.97,7.35,8.4h-5.18c0-3.36-0.6-4.62-2.17-4.62
			c-2.97,0-3.36,2.8-3.36,9.28c0,6.48,0.39,9.28,3.36,9.28c2.45,0,2.35-3.15,2.42-5.15h5.21c0,6.76-2.7,8.93-7.63,8.93
			C490.3,59.26,490.3,52.82,490.3,46.2z" />
        <path class="st3" d="M518.4,58.84V46.65c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V33.56h4.94v9.38h0.07
			c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85v14.18H518.4z" />
        <path class="st3" d="M532.61,33.56v3.88h-4.94v-3.88H532.61z M532.61,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3" d="M542.34,33.56v25.27h-4.94V33.56H542.34z" />
        <path class="st3" d="M555.54,58.84v-1.96h-0.07c-0.91,1.71-2.28,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31
			c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.53,4.03,2.03h0.07v-9.28h4.94v25.27H555.54z M555.29,49.84c0-3.54,0.04-5.99-2-5.99
			c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.32,6.3,2.1,6.3C554.98,56.14,555.29,54.29,555.29,49.84z" />
        <path class="st3" d="M577.41,58.84h-5.29V33.56h9.77c3.61,0,5.92,2.31,5.92,6.62c0,3.22-1.26,5.64-4.69,6.2v0.07
			c1.15,0.14,4.58,0.42,4.58,4.97c0,1.61,0.11,6.37,0.59,7.42h-5.18c-0.7-1.54-0.56-3.25-0.56-4.9c0-3.01,0.28-5.57-3.78-5.57h-1.37
			V58.84z M577.41,44.48h2.35c2.1,0,2.7-2.1,2.7-3.71c0-2.42-1.02-3.33-2.7-3.33h-2.35V44.48z" />
        <path class="st3" d="M596.8,33.56v3.88h-4.94v-3.88H596.8z M596.8,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3"
          d="M614.69,41.16v18.41c0,1.22,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.95-6.93-5.25h4.83
			c0,0.74,0.11,1.37,0.42,1.79c0.32,0.46,0.88,0.7,1.65,0.7c1.23,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.73,1.37-2.13,2.07-3.75,2.07
			c-5.43,0-5.18-4.97-5.18-8.96c0-3.89,0.07-8.82,5.22-8.82c1.75,0,3.25,0.77,3.96,2.42H610v-2.07H614.69z M607.72,55.55
			c1.79,0,2.03-1.86,2.03-5.6c0-3.89-0.17-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C605.59,52.19,605.34,55.55,607.72,55.55z" />
        <path class="st3" d="M627.32,58.84V46.65c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V33.56h4.94v9.38h0.07
			c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85v14.18H627.32z" />
        <path class="st3" d="M634.18,41.16h2v-2.8l4.94-2.21v5.01h2.56v3.04h-2.56v9.45c0,1.33-0.04,2.21,1.58,2.21
			c0.32,0,0.63,0,0.88-0.07v3.04c-0.67,0.07-1.37,0.17-2.55,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.2h-2V41.16z" />
        <path class="st3" d="M649.79,53.17c-0.04,0.81,0,1.58,0.25,2.14c0.28,0.56,0.8,0.84,1.79,0.84c0.98,0,1.82-0.63,1.82-1.82
			c0-3.75-8.68-2.91-8.68-8.54c0-3.82,3.78-4.97,6.97-4.97c3.36,0,6.41,1.61,6.13,5.43h-4.83c0-1.22-0.14-1.96-0.49-2.28
			c-0.32-0.31-0.74-0.38-1.26-0.38c-1.08,0-1.68,0.7-1.68,1.89c0,2.8,8.68,2.66,8.68,8.33c0,3.08-2.52,5.39-6.62,5.39
			c-4.31,0-7.18-1.08-6.9-6.02H649.79z" />
        <path class="st3" d="M682.62,55.55c0,1.08,0.14,2.21,0.25,3.29h-4.58l-0.21-2.35H678c-1.05,1.82-2.49,2.7-4.62,2.7
			c-3.43,0-4.69-2.55-4.69-5.63c0-5.85,4.51-6.09,9.1-6.02v-1.36c0-1.51-0.21-2.59-2-2.59c-1.71,0-1.86,1.29-1.86,2.7h-4.83
			c0-2.13,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M673.52,53.34
			c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C675.34,50.4,673.52,50.19,673.52,53.34z" />
        <path class="st3" d="M691.65,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M713.04,58.84v-1.96h-0.07c-0.91,1.71-2.28,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31
			c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.53,4.03,2.03h0.07v-9.28h4.94v25.27H713.04z M712.79,49.84c0-3.54,0.04-5.99-2-5.99
			c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.32,6.3,2.1,6.3C712.48,56.14,712.79,54.29,712.79,49.84z" />
        <path class="st3" d="M727.49,33.56h5.43l3.29,17.75h0.07l3.99-17.75h6.23l3.78,17.75h0.07l3.15-17.75h5.18l-5.6,25.27h-5.85
			l-3.96-18.48h-0.07l-4.38,18.48h-5.74L727.49,33.56z" />
      </g>
      <g class="st5">
        <path class="st3" d="M764.28,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5c-0.07,1.92-0.7,3.5-1.89,4.58
			c-1.16,1.08-2.91,1.71-5.22,1.71c-6.37,0-7.21-3.88-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H764.28z
			 M768.79,48.02c0-1.71,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H768.79z" />
        <path class="st3" d="M782.58,33.56v25.27h-4.94V33.56H782.58z" />
        <path class="st3" d="M792.31,33.56v25.27h-4.94V33.56H792.31z" />
        <path class="st3" d="M796.69,33.56h4.94v9.28h0.07c1.02-1.5,2.24-2.03,4.03-2.03c4.97,0,4.83,5.5,4.83,9.07
			c0,3.64,0.18,9.31-4.94,9.31c-1.89,0-3.25-0.59-4.17-2.31h-0.07v1.96h-4.69V33.56z M805.72,49.84c0-3.54,0.04-5.99-2.1-5.99
			c-2.03,0-2,2.45-2,5.99c0,4.45,0.32,6.3,2,6.3C805.4,56.14,805.72,54.29,805.72,49.84z" />
        <path class="st3" d="M818.74,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5.01c-0.07,1.92-0.7,3.5-1.89,4.58
			c-1.15,1.08-2.9,1.71-5.21,1.71c-6.37,0-7.21-3.88-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H818.74z
			 M823.25,48.02c0-1.71,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H823.25z" />
        <path class="st3" d="M837.04,33.56v3.88h-4.94v-3.88H837.04z M837.04,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3" d="M846.35,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.34,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.85-2.8c-1.58,0-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M872.43,41.16v18.41c0,1.22,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.95-6.93-5.25h4.83c0,0.74,0.1,1.37,0.42,1.79
			c0.32,0.46,0.88,0.7,1.65,0.7c1.22,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.74,1.37-2.13,2.07-3.75,2.07c-5.43,0-5.18-4.97-5.18-8.96
			c0-3.89,0.07-8.82,5.21-8.82c1.75,0,3.26,0.77,3.96,2.42h0.07v-2.07H872.43z M865.46,55.55c1.79,0,2.03-1.86,2.03-5.6
			c0-3.89-0.18-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C863.33,52.19,863.08,55.55,865.46,55.55z" />
        <path class="st3" d="M884.33,58.84V33.56h8.51l3.96,17.19h0.07l4.2-17.19h8.23v25.27h-5.15v-19.5h-0.07l-4.87,19.5h-5.04
			l-4.62-19.5h-0.07v19.5H884.33z" />
        <path class="st3" d="M912.92,49.77c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42
			S912.92,55.3,912.92,49.77z M922.41,49.49c0-3.68-0.18-5.53-2.28-5.53s-2.28,1.86-2.28,5.53c0,5.39,0.46,6.54,2.28,6.54
			S922.41,54.88,922.41,49.49z" />
        <path class="st3" d="M935.78,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.34,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M953.7,33.56v3.88h-4.94v-3.88H953.7z M953.7,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3" d="M956.07,41.16h2v-2.8l4.94-2.21v5.01h2.55v3.04h-2.55v9.45c0,1.33-0.04,2.21,1.57,2.21
			c0.32,0,0.63,0,0.88-0.07v3.04c-0.67,0.07-1.37,0.17-2.56,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.2h-2V41.16z" />
        <path class="st3" d="M967.38,49.77c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42
			S967.38,55.3,967.38,49.77z M976.87,49.49c0-3.68-0.17-5.53-2.28-5.53s-2.28,1.86-2.28,5.53c0,5.39,0.46,6.54,2.28,6.54
			S976.87,54.88,976.87,49.49z" />
        <path class="st3" d="M989.99,41.16v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94
			V41.16H989.99z" />
        <path class="st3" d="M1002.31,33.56v3.88h-4.94v-3.88H1002.31z M1002.31,58.84h-4.94V41.16h4.94V58.84z" />
        <path class="st3" d="M1011.62,42.94h0.07c0.49-0.8,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85
			v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3"
          d="M1037.7,41.16v18.41c0,1.22,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.95-6.93-5.25h4.83
			c0,0.74,0.11,1.37,0.42,1.79c0.32,0.46,0.88,0.7,1.65,0.7c1.23,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.73,1.37-2.13,2.07-3.75,2.07
			c-5.43,0-5.18-4.97-5.18-8.96c0-3.89,0.07-8.82,5.22-8.82c1.75,0,3.25,0.77,3.96,2.42h0.07v-2.07H1037.7z M1030.73,55.55
			c1.79,0,2.03-1.86,2.03-5.6c0-3.89-0.17-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C1028.6,52.19,1028.35,55.55,1030.73,55.55z" />
        <path class="st3" d="M1057.36,58.84V33.56h13.13v3.88h-7.84v6.48h7.49v3.88h-7.49v11.03H1057.36z" />
        <path class="st3" d="M1077.45,41.16v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94
			V41.16H1077.45z" />
        <path class="st3" d="M1097.82,55.55c0,1.08,0.14,2.21,0.25,3.29h-4.58l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7
			c-3.43,0-4.69-2.55-4.69-5.63c0-5.85,4.51-6.09,9.1-6.02v-1.36c0-1.51-0.21-2.59-2-2.59c-1.71,0-1.86,1.29-1.86,2.7h-4.83
			c0-2.13,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M1088.72,53.34
			c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C1090.54,50.4,1088.72,50.19,1088.72,53.34z" />
        <path class="st3"
          d="M1106.47,42.94h0.07c0.98-1.58,2.31-2.14,4.17-2.14c1.75,0,3.15,0.84,3.96,2.24
			c1.16-1.54,2.56-2.24,4.59-2.24c2.34,0,4.41,1.4,4.41,3.85v14.18h-4.94V46.65c0-1.58-0.28-2.8-1.85-2.8
			c-1.58,0-1.86,1.22-1.86,2.8v12.18h-4.83V46.65c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.22-1.86,2.8v12.18h-4.94V41.16h4.94V42.94z" />
        <path class="st3" d="M1131.74,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5c-0.07,1.92-0.7,3.5-1.89,4.58
			c-1.16,1.08-2.91,1.71-5.22,1.71c-6.37,0-7.21-3.88-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H1131.74z
			 M1136.25,48.02c0-1.71,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H1136.25z" />
        <path class="st3" d="M1143.11,41.16h4.9l2.42,13.3h0.07l3.4-13.3h5.11l3.12,13.3h0.07l2.66-13.3h4.73l-4.79,17.68h-5.18
			l-3.19-12.08h-0.07l-3.57,12.08h-5.25L1143.11,41.16z" />
        <path class="st3" d="M1171.5,49.77c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42
			C1172.34,59.19,1171.5,55.3,1171.5,49.77z M1180.98,49.49c0-3.68-0.17-5.53-2.28-5.53s-2.28,1.86-2.28,5.53
			c0,5.39,0.46,6.54,2.28,6.54S1180.98,54.88,1180.98,49.49z" />
        <path class="st3" d="M1194.11,41.16v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94
			V41.16H1194.11z" />
        <path class="st3" d="M1200.97,58.84V33.56h4.94v15.05h0.07l4.45-7.46h5.15l-5.01,7.88l5.57,9.8h-5.57l-4.59-9.63h-0.07v9.63
			H1200.97z" />
      </g>
      <path class="st54" d="M766.05,209.34c0.06-0.06,0.19-0.03,0.3-0.05c0.77-0.11,1.53-0.06,2.3-0.01c1.6,0.12,3.22,0.1,4.82,0.29
		c0.39,0.05,0.79,0.13,1.18,0.04c0.96-0.23,1.38-0.96,1.68-1.8c0.13-0.35,0.07-0.68-0.11-1.01c-0.35-0.62-0.91-0.95-1.56-1.16
		c-1.65-0.52-3.35-0.8-5.08-0.9c-1.4-0.08-2.73-0.3-3.98-1.02c-1.13-0.65-2.37-1.08-3.67-1.3c-3.04-0.52-5.98,0.05-8.89,0.88
		c-0.36,0.1-0.53,0.36-0.53,0.73c0,0.44,0,0.89,0,1.33c0,1.84,0,3.68,0,5.53c0,0.53,0.26,0.88,0.72,0.91
		c1.14,0.06,2.17,0.45,3.19,0.93c2.51,1.17,4.97,2.43,7.51,3.53c1,0.43,2,0.85,3.12,0.71c0.67-0.08,1.34-0.14,2.01-0.24
		c1.75-0.26,3.49-0.56,5.25-0.8c1.05-0.14,2.07-0.29,2.97-0.91c1.06-0.74,2.14-1.44,3.21-2.17c0.48-0.33,0.93-0.7,1.35-1.1
		c0.33-0.31,0.55-0.69,0.61-1.15c0.03-0.25-0.01-0.5-0.27-0.58c-0.37-0.11-0.29-0.23-0.08-0.45c0.58-0.63,0.45-1.34-0.31-1.74
		c-0.39-0.21-0.81-0.29-1.25-0.25c-1.17,0.09-2.13,0.64-2.96,1.42c-0.75,0.7-1.61,1.13-2.6,1.35c-0.78,0.17-1.57,0.22-2.35,0.32
		C770.28,210.98,768.08,210.52,766.05,209.34" />
      <path class="st54" d="M751.5,207.54L751.5,207.54c0-1.69,0-3.38,0-5.07c0-0.61-0.26-0.86-0.87-0.86c-0.77,0-1.54,0-2.31,0
		c-0.55,0-0.83,0.27-0.83,0.81c0,3.4,0,6.81,0,10.21c0,0.56,0.25,0.82,0.8,0.82c0.78,0.01,1.56,0,2.34,0c0.63,0,0.86-0.24,0.86-0.87
		C751.5,210.9,751.5,209.22,751.5,207.54" />
      <path class="st54" d="M781.89,189.96c-1.94-5.59-7.37-8.79-13.19-7.76c-5.55,0.98-9.69,6.1-9.49,11.74
		c0.1,2.77,1.04,5.21,2.83,7.32c0.14,0.17,0.3,0.27,0.52,0.31c1.17,0.23,2.29,0.62,3.33,1.21c1.18,0.67,2.45,0.92,3.78,1
		c1.65,0.09,3.27,0.35,4.85,0.79c0.15,0.04,0.27,0.02,0.4-0.03C780.73,202.45,783.91,195.79,781.89,189.96L781.89,189.96z
		 M770.85,202.84c-5.26,0-9.54-4.28-9.54-9.54s4.28-9.54,9.54-9.54s9.54,4.28,9.54,9.54S776.11,202.84,770.85,202.84L770.85,202.84z
		" />
      <path class="st54"
        d="M770.85,184.51c-4.85,0-8.79,3.94-8.79,8.79c0,4.85,3.94,8.79,8.79,8.79c4.84,0,8.79-3.94,8.79-8.79
		C779.64,188.46,775.69,184.51,770.85,184.51L770.85,184.51z M775.62,195.32h-9.54c-0.38,0-0.69-0.31-0.69-0.69s0.31-0.69,0.69-0.69
		h9.54c0.38,0,0.69,0.31,0.69,0.69C776.31,195.02,776,195.32,775.62,195.32L775.62,195.32z M775.62,192.65h-9.54
		c-0.38,0-0.69-0.31-0.69-0.69s0.31-0.69,0.69-0.69h9.54c0.38,0,0.69,0.31,0.69,0.69S776,192.65,775.62,192.65L775.62,192.65z" />
      <line class="st72" x1="977.95" y1="616.5" x2="1013.09" y2="616.5" />
      <line class="st73" x1="1014.62" y1="619.47" x2="1014.62" y2="644.75" />
      <line class="st74" x1="1017.6" y1="646.24" x2="1322.52" y2="646.24" />
      <path class="st33" d="M974.9,616.5L974.9,616.5 M1014.62,616.5L1014.62,616.5 M1014.62,646.24L1014.62,646.24 M1324,646.24
		L1324,646.24" />
      <path class="st3" d="M974.9,619.28c1.53,0,2.77-1.24,2.77-2.78s-1.24-2.78-2.77-2.78s-2.78,1.24-2.78,2.78
		S973.36,619.28,974.9,619.28L974.9,619.28z" />
    </g>
</svg>
                """,
                style={"height": "80rem", "display": "flex"},
            )
        ]
    )
    # return html.Img(src="data:image/svg+xml;base64,{}".format(encoded_image))
    # return html.Img(src="assets/socr_diagram.svg")
