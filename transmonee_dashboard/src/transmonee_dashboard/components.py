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
    encoded_image = base64.b64encode(open(image_filename, "rb").read())
    decoded_image = base64.b64encode(open(image_filename, "rb").read()).decode()

    return html.Div(
        # children=html.Img(src="data:image/svg+xml;base64,{}".format(encoded_image))
        [
            html.Iframe(
                srcDoc="""
                  <?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Generator: Adobe Illustrator 26.3.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->

<svg
   version="1.1"
   id="Layer_1"
   x="0px"
   y="0px"
   viewBox="0 0 1355 1310.5"
   style="enable-background:new 0 0 1355 1310.5;"
   xml:space="preserve"
   sodipodi:docname="SOCR_Diagram_[UPDATED v2]-01.svg"
   inkscape:version="1.2 (dc2aedaf03, 2022-05-15)"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"><defs
   id="defs3055" /><sodipodi:namedview
   id="namedview3053"
   pagecolor="#ffffff"
   bordercolor="#000000"
   borderopacity="0.25"
   inkscape:showpageshadow="2"
   inkscape:pageopacity="0.0"
   inkscape:pagecheckerboard="0"
   inkscape:deskcolor="#d1d1d1"
   showgrid="false"
   inkscape:zoom="2.4845479"
   inkscape:cx="485.80267"
   inkscape:cy="270.67299"
   inkscape:window-width="1920"
   inkscape:window-height="1001"
   inkscape:window-x="-9"
   inkscape:window-y="-9"
   inkscape:window-maximized="1"
   inkscape:current-layer="g3050"><inkscape:grid
     type="xygrid"
     id="grid9661" /></sodipodi:namedview>
<style
   type="text/css"
   id="style2">
	.st0{fill:#2C5996;}
	.st1{fill:#4AA4B6;}
	.st2{fill:#961B4A;}
	.st3{fill:#00AEEF;}
	.st4{fill:#2E76BC;}
	.st5{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7877;}
	.st6{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9822;}
	.st7{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st8{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0593;}
	.st9{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9811;}
	.st10{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st11{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9927;}
	.st12{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7863;}
	.st13{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9866;}
	.st14{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st15{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9821;}
	.st16{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9708;}
	.st17{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0533;}
	.st18{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3;}
	.st19{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9682;}
	.st20{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8944;}
	.st21{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8571;}
	.st22{fill:none;stroke:#961B4A;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9873;}
	.st23{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0207;}
	.st24{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8015;}
	.st25{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9815;}
	.st26{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0287;}
	.st27{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st28{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9741;}
	.st29{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st30{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9305;}
	.st31{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9636;}
	.st32{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0185;}
	.st33{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9519;}
	.st34{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8747;}
	.st35{fill:none;stroke:#2E76BC;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9728;}
	.st36{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9927;}
	.st37{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.7863;}
	.st38{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9866;}
	.st39{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st40{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9821;}
	.st41{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9708;}
	.st42{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0533;}
	.st43{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3;}
	.st44{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9682;}
	.st45{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8944;}
	.st46{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8571;}
	.st47{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9873;}
	.st48{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0287;}
	.st49{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st50{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9741;}
	.st51{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9495;}
	.st52{fill:none;stroke:#2C5996;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9857;}
	.st53{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9286;}
	.st54{fill:none;stroke:#4AA4B6;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9861;}
	.st55{fill:#FFFFFF;}
	.st56{fill:#562061;}
	.st57{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9808;}
	.st58{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.8091;}
	.st59{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.949;}
	.st60{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st61{fill:none;stroke:#000000;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9602;}
	.st62{fill:none;stroke:#000000;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st63{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.142;}
	.st64{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.906;}
	.st65{fill:none;stroke:#FFFFFF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9908;}
	.st66{fill:none;stroke:#562061;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9602;}
	.st67{fill:none;stroke:#562061;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;}
	.st68{fill:#F3F8F5;}
	.st69{fill:#13733B;}
	.st70{fill:#E7F1EA;}
	.st71{fill:none;stroke:#13733B;stroke-width:2.8347;stroke-miterlimit:10;}
	.st72{fill:none;stroke:#00AEEF;}
	.st73{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,3.0557;}
	.st74{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9738;}
	.st75{fill:none;stroke:#00AEEF;stroke-width:0.9921;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:0,2.9748;}
</style>
<g
   id="g3050">
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a45984"
   xlink:title="Adolescent physical, mental, and reproductive health"
   xlink:show="Adolescent physical, mental, and reproductive health"
   target="blank"
   xlink:href="/child-health#adolescents"><g
     id="g140">
		<path
   class="st0"
   d="M949.98,360.73h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L949.98,360.73z M950.99,362.27h-0.04    l-2.03,6.93h4.16L950.99,362.27z"
   id="path48" />
		<path
   class="st0"
   d="M962.69,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M960.98,365.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C962.69,367.61,962.61,365.67,960.98,365.67z"
   id="path50" />
		<path
   class="st0"
   d="M966.63,369.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C968.16,373.91,966.63,373.34,966.63,369.32z M971.99,368.69c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C971.61,372.71,971.99,371.65,971.99,368.69z"
   id="path52" />
		<path
   class="st0"
   d="M977.32,373.73h-1.48v-13h1.48V373.73z"
   id="path54" />
		<path
   class="st0"
   d="M981.31,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H981.31z M984.86,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H984.86z"
   id="path56" />
		<path
   class="st0"
   d="M991.56,373.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C994.73,373.14,993.36,373.91,991.56,373.91z"
   id="path58" />
		<path
   class="st0"
   d="M1001.62,367.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1001.62z"
   id="path60" />
		<path
   class="st0"
   d="M1007.31,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1007.31z M1010.85,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1010.85z"
   id="path62" />
		<path
   class="st0"
   d="M1019.8,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1019.8z"
   id="path64" />
		<path
   class="st0"
   d="M1024.03,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1024.03z"
   id="path66" />
		<path
   class="st0"
   d="M1034.47,365.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V365.72z M1037.98,369.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1037.76,372.71,1037.98,371.47,1037.98,369.04z"
   id="path68" />
		<path
   class="st0"
   d="M1046.8,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1046.8z"
   id="path70" />
		<path
   class="st0"
   d="M1053.6,372.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1053.6,372.04z"
   id="path72" />
		<path
   class="st0"
   d="M1061.54,373.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57H1063c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1064.71,373.14,1063.34,373.91,1061.54,373.91z"
   id="path74" />
		<path
   class="st0"
   d="M1066.72,360.73h1.66v1.58h-1.66V360.73z M1068.29,373.73h-1.48v-9.09h1.48V373.73z"
   id="path76" />
		<path
   class="st0"
   d="M1075.6,367.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1075.6z"
   id="path78" />
		<path
   class="st0"
   d="M1084.53,372.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.42z M1081.19,371.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1083.08,369.23,1081.19,369.11,1081.19,371.03z"
   id="path80" />
		<path
   class="st0"
   d="M1090.29,373.73h-1.48v-13h1.48V373.73z"
   id="path82" />
		<path
   class="st0"
   d="M1093.09,371.86h1.85l-1.64,4.16h-1.15L1093.09,371.86z"
   id="path84" />
		<path
   class="st0"
   d="M1105.3,373.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1105.3z"
   id="path86" />
		<path
   class="st0"
   d="M1115.27,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1115.27z M1118.82,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1118.82z"
   id="path88" />
		<path
   class="st0"
   d="M1127.76,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1127.76z"
   id="path90" />
		<path
   class="st0"
   d="M1131.99,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1131.99z"
   id="path92" />
		<path
   class="st0"
   d="M1141.51,372.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.42z M1138.18,371.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1140.07,369.23,1138.18,369.11,1138.18,371.03z"
   id="path94" />
		<path
   class="st0"
   d="M1147.27,373.73h-1.48v-13h1.48V373.73z"
   id="path96" />
		<path
   class="st0"
   d="M1158.5,372.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.42z M1155.17,371.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1157.06,369.23,1155.17,369.11,1155.17,371.03z"
   id="path98" />
		<path
   class="st0"
   d="M1167.76,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1167.76z"
   id="path100" />
		<path
   class="st0"
   d="M1176.63,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M1174.92,365.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1176.63,367.61,1176.56,365.67,1174.92,365.67z"
   id="path102" />
		<path
   class="st0"
   d="M1186.35,366.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366.01z"
   id="path104" />
		<path
   class="st0"
   d="M1192.25,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1192.25z M1195.8,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1195.8z"
   id="path106" />
		<path
   class="st0"
   d="M1201.42,365.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V365.72z M1204.93,369.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1204.71,372.71,1204.93,371.47,1204.93,369.04z"
   id="path108" />
		<path
   class="st0"
   d="M1210.34,366.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366.01z"
   id="path110" />
		<path
   class="st0"
   d="M1214.55,369.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1216.08,373.91,1214.55,373.34,1214.55,369.32z M1219.92,368.69c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1219.54,372.71,1219.92,371.65,1219.92,368.69z"
   id="path112" />
		<path
   class="st0"
   d="M1228.61,360.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V360.73z M1226.9,365.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1228.61,367.61,1228.54,365.67,1226.9,365.67z"
   id="path114" />
		<path
   class="st0"
   d="M1237.67,364.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V364.64z"
   id="path116" />
		<path
   class="st0"
   d="M1246.56,367.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1246.56z"
   id="path118" />
		<path
   class="st0"
   d="M1250.97,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1250.97z"
   id="path120" />
		<path
   class="st0"
   d="M1255.68,360.73h1.66v1.58h-1.66V360.73z M1257.25,373.73h-1.48v-9.09h1.48V373.73z"
   id="path122" />
		<path
   class="st0"
   d="M1258.76,364.64h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1258.76,364.64z"
   id="path124" />
		<path
   class="st0"
   d="M1269.24,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1269.24z M1272.79,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1272.79z"
   id="path126" />
		<path
   class="st0"
   d="M1285.73,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1285.73z"
   id="path128" />
		<path
   class="st0"
   d="M1291.23,369.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1291.23z M1294.78,368.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1294.78z"
   id="path130" />
		<path
   class="st0"
   d="M1303.47,372.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V372.42z M1300.14,371.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1302.03,369.23,1300.14,369.11,1300.14,371.03z"
   id="path132" />
		<path
   class="st0"
   d="M1309.23,373.73h-1.48v-13h1.48V373.73z"
   id="path134" />
		<path
   class="st0"
   d="M1311.95,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1311.95z"
   id="path136" />
		<path
   class="st0"
   d="M1321.73,373.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1321.73z"
   id="path138" />
	</g></a>
	<a
   id="a6541"
   xlink:href="/child-health#nutrition"
   target="blank"
   xlink:title="Nutrition"
   xlink:show="Nutrition"><g
     id="g160">
		<path
   class="st0"
   d="M40.96,360.73v13h-2.27l-5.13-11.27h-0.04v11.27h-1.48v-13h2.34l5.06,11.13h0.04v-11.13H40.96z"
   id="path142" />
		<path
   class="st0"
   d="M48.66,364.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V364.64z"
   id="path144" />
		<path
   class="st0"
   d="M52.96,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H52.96z"
   id="path146" />
		<path
   class="st0"
   d="M59.33,366.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V366.01z"
   id="path148" />
		<path
   class="st0"
   d="M63.67,360.73h1.66v1.58h-1.66V360.73z M65.24,373.73h-1.48v-9.09h1.48V373.73z"
   id="path150" />
		<path
   class="st0"
   d="M67.96,364.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H67.96z"
   id="path152" />
		<path
   class="st0"
   d="M72.67,360.73h1.66v1.58h-1.66V360.73z M74.24,373.73h-1.48v-9.09h1.48V373.73z"
   id="path154" />
		<path
   class="st0"
   d="M76.54,369.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C78.07,373.91,76.54,373.34,76.54,369.32z M81.91,368.69c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C81.53,372.71,81.91,371.65,81.91,368.69z"
   id="path156" />
		<path
   class="st0"
   d="M90.73,373.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H90.73z"
   id="path158" />
	</g></a>
	<a
   id="a49142"
   xlink:href="/child-health#hivaids"
   target="blank"
   xlink:title="HIV/AIDS"
   xlink:show="HIV/AIDS"><g
     id="g178">
		<path
   class="st0"
   d="M1258.04,440.73v-13h1.66v5.62h4.56v-5.62h1.66v13h-1.66v-5.94h-4.56v5.94H1258.04z"
   id="path162" />
		<path
   class="st0"
   d="M1270.8,440.73h-1.66v-13h1.66V440.73z"
   id="path164" />
		<path
   class="st0"
   d="M1278.45,440.73h-1.98l-3.76-13h1.8l2.97,11.43h0.04l3.04-11.43h1.69L1278.45,440.73z"
   id="path166" />
		<path
   class="st0"
   d="M1283.26,442.46h-1.21l4.23-14.73h1.21L1283.26,442.46z"
   id="path168" />
		<path
   class="st0"
   d="M1291.88,427.73h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L1291.88,427.73z M1292.89,429.27h-0.04    l-2.03,6.93h4.16L1292.89,429.27z"
   id="path170" />
		<path
   class="st0"
   d="M1301.82,440.73h-1.66v-13h1.66V440.73z"
   id="path172" />
		<path
   class="st0"
   d="M1304.98,427.73h4c1.66,0,2.85,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24    c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V427.73z M1306.64,439.29h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6    h-2.18V439.29z"
   id="path174" />
		<path
   class="st0"
   d="M1317.22,436.86v0.38c0,1.76,1.12,2.32,2.18,2.32c1.31,0,2.32-0.56,2.32-2.11c0-2.88-5.83-2.56-5.83-6.46    c0-2.3,1.64-3.53,3.82-3.53c2.38,0,3.71,1.15,3.6,3.8h-1.73c0.02-1.42-0.43-2.36-2-2.36c-0.99,0-2,0.5-2,1.91    c0,2.86,5.83,2.45,5.83,6.57c0,2.74-1.89,3.62-4.03,3.62c-3.83,0.04-3.83-2.9-3.8-4.14H1317.22z"
   id="path176" />
	</g></a>
	<a
   id="a9653"
   xlink:href="/child-health#immunization"
   target="blank"
   xlink:title="Immunization"
   xlink:show="Immunization"><g
     id="g204">
		<path
   class="st0"
   d="M33.83,440.73h-1.66v-13h1.66V440.73z"
   id="path180" />
		<path
   class="st0"
   d="M41.26,440.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91H45.8v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H41.26z"
   id="path182" />
		<path
   class="st0"
   d="M54.26,440.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91H58.8v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H54.26z"
   id="path184" />
		<path
   class="st0"
   d="M67.65,431.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H67.6c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V431.64z"
   id="path186" />
		<path
   class="st0"
   d="M76.72,440.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H76.72z"
   id="path188" />
		<path
   class="st0"
   d="M80.66,427.73h1.66v1.58h-1.66V427.73z M82.23,440.73h-1.48v-9.09h1.48V440.73z"
   id="path190" />
		<path
   class="st0"
   d="M89.74,432.99l-4.02,6.54h4.14v1.21h-5.74v-1.39l3.96-6.46v-0.04h-3.76v-1.21h5.42V432.99z"
   id="path192" />
		<path
   class="st0"
   d="M96.47,439.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V439.42z M93.14,438.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C95.03,436.23,93.14,436.11,93.14,438.03z"
   id="path194" />
		<path
   class="st0"
   d="M100.95,431.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H100.95z"
   id="path196" />
		<path
   class="st0"
   d="M105.67,427.73h1.66v1.58h-1.66V427.73z M107.23,440.73h-1.48v-9.09h1.48V440.73z"
   id="path198" />
		<path
   class="st0"
   d="M109.54,436.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C111.07,440.91,109.54,440.34,109.54,436.32z M114.9,435.69c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C114.52,439.71,114.9,438.65,114.9,435.69z"
   id="path200" />
		<path
   class="st0"
   d="M123.72,440.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H123.72z"
   id="path202" />
	</g></a>
	<a
   id="a53909"
   xlink:href="/child-poverty#socialprotection"
   target="blank"
   xlink:title="Social protection system"
   xlink:show="Social protection system"><g
     id="g250">
		<path
   class="st3"
   d="M1149.27,503.87v0.38c0,1.76,1.12,2.32,2.18,2.32c1.31,0,2.32-0.56,2.32-2.11c0-2.88-5.83-2.56-5.83-6.46    c0-2.3,1.64-3.53,3.82-3.53c2.38,0,3.71,1.15,3.6,3.8h-1.73c0.02-1.42-0.43-2.36-2-2.36c-0.99,0-2,0.5-2,1.91    c0,2.86,5.83,2.45,5.83,6.57c0,2.74-1.89,3.62-4.03,3.62c-3.83,0.04-3.83-2.9-3.8-4.14H1149.27z"
   id="path206" />
		<path
   class="st3"
   d="M1157.59,503.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1159.12,507.92,1157.59,507.35,1157.59,503.33z M1162.96,502.7c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1162.58,506.72,1162.96,505.65,1162.96,502.7z"
   id="path208" />
		<path
   class="st3"
   d="M1171.59,501.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1171.59z"
   id="path210" />
		<path
   class="st3"
   d="M1175.71,494.74h1.66v1.58h-1.66V494.74z M1177.28,507.74h-1.48v-9.09h1.48V507.74z"
   id="path212" />
		<path
   class="st3"
   d="M1184.52,506.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.43z M1181.19,505.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1183.08,503.24,1181.19,503.11,1181.19,505.04z"
   id="path214" />
		<path
   class="st3"
   d="M1190.28,507.74h-1.48v-13h1.48V507.74z"
   id="path216" />
		<path
   class="st3"
   d="M1198.43,499.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V499.73z M1201.94,503.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1201.73,506.72,1201.94,505.47,1201.94,503.04z"
   id="path218" />
		<path
   class="st3"
   d="M1207.36,500.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V500c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.02z"
   id="path220" />
		<path
   class="st3"
   d="M1211.57,503.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1213.1,507.92,1211.57,507.35,1211.57,503.33z M1216.94,502.7c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1216.56,506.72,1216.94,505.65,1216.94,502.7z"
   id="path222" />
		<path
   class="st3"
   d="M1220.98,498.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1220.98z"
   id="path224" />
		<path
   class="st3"
   d="M1227.27,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1227.27z M1230.81,502.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1230.81z"
   id="path226" />
		<path
   class="st3"
   d="M1239.58,501.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1239.58z"
   id="path228" />
		<path
   class="st3"
   d="M1243.99,498.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1243.99z"
   id="path230" />
		<path
   class="st3"
   d="M1248.7,494.74h1.66v1.58h-1.66V494.74z M1250.27,507.74h-1.48v-9.09h1.48V507.74z"
   id="path232" />
		<path
   class="st3"
   d="M1252.57,503.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1254.11,507.92,1252.57,507.35,1252.57,503.33z M1257.94,502.7c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1257.56,506.72,1257.94,505.65,1257.94,502.7z"
   id="path234" />
		<path
   class="st3"
   d="M1266.76,507.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1266.76z"
   id="path236" />
		<path
   class="st3"
   d="M1277.5,507.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1280.67,507.15,1279.3,507.92,1277.5,507.92z"
   id="path238" />
		<path
   class="st3"
   d="M1285.55,506.05h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1285.55,506.05z"
   id="path240" />
		<path
   class="st3"
   d="M1293.49,507.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1296.66,507.15,1295.29,507.92,1293.49,507.92z"
   id="path242" />
		<path
   class="st3"
   d="M1298.96,498.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1298.96z"
   id="path244" />
		<path
   class="st3"
   d="M1305.24,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1305.24z M1308.79,502.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1308.79z"
   id="path246" />
		<path
   class="st3"
   d="M1317.27,507.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1317.27z"
   id="path248" />
	</g></a>
	<a
   id="a12786"
   xlink:href="/child-health#mnch"
   xlink:title="Maternal, newborn and child health"
   xlink:show="Maternal, newborn and child health"
   target="blank"><g
     id="g312">
		<path
   class="st0"
   d="M33.52,507.74h-1.55v-13h2.68l3.28,10.91h0.04l3.31-10.91h2.74v13h-1.66v-11.56h-0.04l-3.64,11.56h-1.57    l-3.56-11.56h-0.04V507.74z"
   id="path252" />
		<path
   class="st0"
   d="M51.47,506.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.43z M48.14,505.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C50.03,503.24,48.14,503.11,48.14,505.04z"
   id="path254" />
		<path
   class="st0"
   d="M55.95,498.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H55.95z"
   id="path256" />
		<path
   class="st0"
   d="M62.23,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H62.23z M65.78,502.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H65.78z"
   id="path258" />
		<path
   class="st0"
   d="M71.32,500.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V500c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.02z"
   id="path260" />
		<path
   class="st0"
   d="M80.72,507.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H80.72z"
   id="path262" />
		<path
   class="st0"
   d="M89.47,506.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.43z M86.14,505.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C88.03,503.24,86.14,503.11,86.14,505.04z"
   id="path264" />
		<path
   class="st0"
   d="M95.23,507.74h-1.48v-13h1.48V507.74z"
   id="path266" />
		<path
   class="st0"
   d="M98.03,505.87h1.85l-1.64,4.16H97.1L98.03,505.87z"
   id="path268" />
		<path
   class="st0"
   d="M110.71,507.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H110.71z"
   id="path270" />
		<path
   class="st0"
   d="M116.21,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H116.21z M119.76,502.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H119.76z"
   id="path272" />
		<path
   class="st0"
   d="M122.64,498.65h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98    l-1.94-7.74h-0.04l-2.03,7.74h-1.98L122.64,498.65z"
   id="path274" />
		<path
   class="st0"
   d="M138.37,507.74h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88    c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V507.74z M140.03,506.72c1.85,0,1.85-1.98,1.85-3.35    c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C138.37,504.21,138.21,506.72,140.03,506.72z"
   id="path276" />
		<path
   class="st0"
   d="M145.52,503.33c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C147.05,507.92,145.52,507.35,145.52,503.33z M150.88,502.7c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C150.5,506.72,150.88,505.65,150.88,502.7z"
   id="path278" />
		<path
   class="st0"
   d="M156.3,500.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V500c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V500.02z"
   id="path280" />
		<path
   class="st0"
   d="M165.7,507.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H165.7z"
   id="path282" />
		<path
   class="st0"
   d="M178.44,506.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.43z M175.11,505.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C177,503.24,175.11,503.11,175.11,505.04z"
   id="path284" />
		<path
   class="st0"
   d="M187.69,507.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H187.69z"
   id="path286" />
		<path
   class="st0"
   d="M196.57,494.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V494.74z M194.86,499.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C196.57,501.62,196.49,499.68,194.86,499.68z"
   id="path288" />
		<path
   class="st0"
   d="M209.51,501.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H209.51z"
   id="path290" />
		<path
   class="st0"
   d="M218.69,507.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H218.69z"
   id="path292" />
		<path
   class="st0"
   d="M222.63,494.74h1.66v1.58h-1.66V494.74z M224.19,507.74h-1.48v-9.09h1.48V507.74z"
   id="path294" />
		<path
   class="st0"
   d="M228.19,507.74h-1.48v-13h1.48V507.74z"
   id="path296" />
		<path
   class="st0"
   d="M235.55,494.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V494.74z M233.84,499.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C235.55,501.62,235.48,499.68,233.84,499.68z"
   id="path298" />
		<path
   class="st0"
   d="M248.68,507.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H248.68z"
   id="path300" />
		<path
   class="st0"
   d="M254.18,503.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H254.18z M257.73,502.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H257.73z"
   id="path302" />
		<path
   class="st0"
   d="M266.42,506.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V506.43z M263.09,505.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C264.98,503.24,263.09,503.11,263.09,505.04z"
   id="path304" />
		<path
   class="st0"
   d="M272.18,507.74h-1.48v-13h1.48V507.74z"
   id="path306" />
		<path
   class="st0"
   d="M274.9,498.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H274.9z"
   id="path308" />
		<path
   class="st0"
   d="M284.67,507.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H284.67z"
   id="path310" />
	</g></a>
	<a
   id="a55528"
   xlink:href="/child-poverty#povertydeprivation"
   target="blank"
   xlink:title="Child Poverty and Material Deprivation"
   xlink:show="Child Poverty and Material Deprivation"><g
     id="g382">
		<path
   class="st3"
   d="M1058.75,565.33c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.1-2.83,4.1-3.67,4.1    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.58,0,3.57,1.33,3.4,3.85H1058.75z"
   id="path314" />
		<path
   class="st3"
   d="M1067.81,574.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1067.81z"
   id="path316" />
		<path
   class="st3"
   d="M1071.75,561.74h1.66v1.58h-1.66V561.74z M1073.31,574.74h-1.48v-9.09h1.48V574.74z"
   id="path318" />
		<path
   class="st3"
   d="M1077.31,574.74h-1.48v-13h1.48V574.74z"
   id="path320" />
		<path
   class="st3"
   d="M1084.67,561.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V561.74z M1082.96,566.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1084.67,568.62,1084.6,566.68,1082.96,566.68z"
   id="path322" />
		<path
   class="st3"
   d="M1094.46,566.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V566.73z M1097.97,570.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1097.76,573.72,1097.97,572.47,1097.97,570.04z"
   id="path324" />
		<path
   class="st3"
   d="M1101.61,570.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1103.14,574.92,1101.61,574.35,1101.61,570.33z M1106.97,569.7c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1106.6,573.72,1106.97,572.65,1106.97,569.7z"
   id="path326" />
		<path
   class="st3"
   d="M1109.82,565.65h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1109.82,565.65z"
   id="path328" />
		<path
   class="st3"
   d="M1120.29,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1120.29z M1123.84,569.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1123.84z"
   id="path330" />
		<path
   class="st3"
   d="M1129.38,567.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V567c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V567.02z"
   id="path332" />
		<path
   class="st3"
   d="M1134.01,565.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1134.01z"
   id="path334" />
		<path
   class="st3"
   d="M1141.59,573.05h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1141.59,573.05z"
   id="path336" />
		<path
   class="st3"
   d="M1155.52,573.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.43z M1152.19,572.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1154.08,570.24,1152.19,570.11,1152.19,572.04z"
   id="path338" />
		<path
   class="st3"
   d="M1164.77,574.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1164.77z"
   id="path340" />
		<path
   class="st3"
   d="M1173.64,561.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V561.74z M1171.93,566.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1173.64,568.62,1173.57,566.68,1171.93,566.68z"
   id="path342" />
		<path
   class="st3"
   d="M1186.3,574.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1186.3z"
   id="path344" />
		<path
   class="st3"
   d="M1199.51,573.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.43z M1196.18,572.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1198.07,570.24,1196.18,570.11,1196.18,572.04z"
   id="path346" />
		<path
   class="st3"
   d="M1203.99,565.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1203.99z"
   id="path348" />
		<path
   class="st3"
   d="M1210.27,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1210.27z M1213.82,569.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1213.82z"
   id="path350" />
		<path
   class="st3"
   d="M1219.36,567.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V567c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V567.02z"
   id="path352" />
		<path
   class="st3"
   d="M1223.7,561.74h1.66v1.58h-1.66V561.74z M1225.27,574.74h-1.48v-9.09h1.48V574.74z"
   id="path354" />
		<path
   class="st3"
   d="M1232.5,573.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.43z M1229.17,572.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1231.06,570.24,1229.17,570.11,1229.17,572.04z"
   id="path356" />
		<path
   class="st3"
   d="M1238.26,574.74h-1.48v-13h1.48V574.74z"
   id="path358" />
		<path
   class="st3"
   d="M1249.62,561.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V561.74z M1247.91,566.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1249.62,568.62,1249.55,566.68,1247.91,566.68z"
   id="path360" />
		<path
   class="st3"
   d="M1255.25,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1255.25z M1258.8,569.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1258.8z"
   id="path362" />
		<path
   class="st3"
   d="M1264.42,566.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V566.73z M1267.93,570.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1267.71,573.72,1267.93,572.47,1267.93,570.04z"
   id="path364" />
		<path
   class="st3"
   d="M1273.34,567.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V567c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V567.02z"
   id="path366" />
		<path
   class="st3"
   d="M1277.68,561.74h1.66v1.58h-1.66V561.74z M1279.25,574.74h-1.48v-9.09h1.48V574.74z"
   id="path368" />
		<path
   class="st3"
   d="M1280.76,565.65h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1280.76,565.65z"
   id="path370" />
		<path
   class="st3"
   d="M1294.48,573.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.43z M1291.14,572.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1293.04,570.24,1291.14,570.11,1291.14,572.04z"
   id="path372" />
		<path
   class="st3"
   d="M1298.96,565.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1298.96z"
   id="path374" />
		<path
   class="st3"
   d="M1303.67,561.74h1.66v1.58h-1.66V561.74z M1305.24,574.74h-1.48v-9.09h1.48V574.74z"
   id="path376" />
		<path
   class="st3"
   d="M1307.54,570.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1309.07,574.92,1307.54,574.35,1307.54,570.33z M1312.91,569.7c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1312.53,573.72,1312.91,572.65,1312.91,569.7z"
   id="path378" />
		<path
   class="st3"
   d="M1321.73,574.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1321.73z"
   id="path380" />
	</g></a>
	<g
   id="g408">
		<path
   class="st0"
   d="M32.06,574.74v-13h1.66v5.62h4.56v-5.62h1.66v13h-1.66v-5.94h-4.56v5.94H32.06z"
   id="path384" />
		<path
   class="st0"
   d="M44.23,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H44.23z M47.78,569.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H47.78z"
   id="path386" />
		<path
   class="st0"
   d="M56.47,573.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V573.43z M53.14,572.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C55.03,570.24,53.14,570.11,53.14,572.04z"
   id="path388" />
		<path
   class="st0"
   d="M62.23,574.74h-1.48v-13h1.48V574.74z"
   id="path390" />
		<path
   class="st0"
   d="M64.95,565.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H64.95z"
   id="path392" />
		<path
   class="st0"
   d="M74.73,574.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H74.73z"
   id="path394" />
		<path
   class="st0"
   d="M85.47,574.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C88.64,574.15,87.27,574.92,85.47,574.92z"
   id="path396" />
		<path
   class="st0"
   d="M93.52,573.05h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L93.52,573.05z"
   id="path398" />
		<path
   class="st0"
   d="M101.45,574.92c-1.96,0-3.19-0.86-3.13-2.95H100c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C104.62,574.15,103.25,574.92,101.45,574.92z"
   id="path400" />
		<path
   class="st0"
   d="M106.93,565.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H106.93z"
   id="path402" />
		<path
   class="st0"
   d="M113.21,570.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H113.21z M116.75,569.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H116.75z"
   id="path404" />
		<path
   class="st0"
   d="M125.23,574.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H125.23z"
   id="path406" />
	</g>
	
	
	<a
   id="a58715"
   xlink:href="/child-health#wash"
   target="blank"
   xlink:title="Water, sanitation and hygiene"
   xlink:show="Water, sanitation and hygiene"><g
     id="g412">
		<path
   class="st3"
   d="M1110.44,628.73h1.76l2.45,11.27h0.04l2.61-11.27h2.14l2.36,11.27h0.04l2.65-11.27h1.73l-3.44,13h-2.02    l-2.47-11.27h-0.04l-2.63,11.27h-2.02L1110.44,628.73z"
   id="path410" />
	</g><g
     id="g422">
		<path
   class="st3"
   d="M1131.78,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1128.45,639.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1130.34,637.23,1128.45,637.11,1128.45,639.03z"
   id="path414" />
		<path
   class="st3"
   d="M1136.26,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1136.26z"
   id="path416" />
		<path
   class="st3"
   d="M1142.54,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1142.54z M1146.09,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1146.09z"
   id="path418" />
		<path
   class="st3"
   d="M1151.63,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z"
   id="path420" />
	</g><g
     id="g466">
		<path
   class="st3"
   d="M1155.09,639.86h1.85l-1.64,4.16h-1.15L1155.09,639.86z"
   id="path424" />
		<path
   class="st3"
   d="M1165.51,641.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1168.68,641.14,1167.31,641.91,1165.51,641.91z"
   id="path426" />
		<path
   class="st3"
   d="M1175.5,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1172.17,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1174.06,637.23,1172.17,637.11,1172.17,639.03z"
   id="path428" />
		<path
   class="st3"
   d="M1184.75,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1184.75z"
   id="path430" />
		<path
   class="st3"
   d="M1188.69,628.73h1.66v1.58h-1.66V628.73z M1190.26,641.73h-1.48v-9.09h1.48V641.73z"
   id="path432" />
		<path
   class="st3"
   d="M1192.97,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1192.97z"
   id="path434" />
		<path
   class="st3"
   d="M1202.5,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1199.17,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1201.06,637.23,1199.17,637.11,1199.17,639.03z"
   id="path436" />
		<path
   class="st3"
   d="M1206.98,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1206.98z"
   id="path438" />
		<path
   class="st3"
   d="M1211.69,628.73h1.66v1.58h-1.66V628.73z M1213.26,641.73h-1.48v-9.09h1.48V641.73z"
   id="path440" />
		<path
   class="st3"
   d="M1215.56,637.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1217.09,641.91,1215.56,641.34,1215.56,637.32z M1220.93,636.69c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1220.55,640.71,1220.93,639.65,1220.93,636.69z"
   id="path442" />
		<path
   class="st3"
   d="M1229.75,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1229.75z"
   id="path444" />
		<path
   class="st3"
   d="M1242.49,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M1239.16,639.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1241.05,637.23,1239.16,637.11,1239.16,639.03z"
   id="path446" />
		<path
   class="st3"
   d="M1251.75,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1251.75z"
   id="path448" />
		<path
   class="st3"
   d="M1260.62,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V628.73z M1258.91,633.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1260.62,635.61,1260.55,633.67,1258.91,633.67z"
   id="path450" />
		<path
   class="st3"
   d="M1273.74,641.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1273.74z"
   id="path452" />
		<path
   class="st3"
   d="M1280.54,640.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1280.54,640.04z"
   id="path454" />
		<path
   class="st3"
   d="M1290.61,632.64h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V632.64z M1288.88,633.69c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1290.64,635.79,1290.73,633.69,1288.88,633.69z"
   id="path456" />
		<path
   class="st3"
   d="M1294.67,628.73h1.66v1.58h-1.66V628.73z M1296.24,641.73h-1.48v-9.09h1.48V641.73z"
   id="path458" />
		<path
   class="st3"
   d="M1300.24,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1300.24z M1303.78,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1303.78z"
   id="path460" />
		<path
   class="st3"
   d="M1312.73,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1312.73z"
   id="path462" />
		<path
   class="st3"
   d="M1318.24,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1318.24z M1321.78,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1321.78z"
   id="path464" />
	</g></a>
	<a
   id="a15929"
   xlink:title="Violence against Children and Women"
   xlink:show="Violence against Children and Women"
   target="blank"
   xlink:href="/child-protection#violence"><g
     id="g530">
		<path
   class="st1"
   d="M36.48,641.73H34.5l-3.76-13h1.8l2.97,11.43h0.04l3.04-11.43h1.69L36.48,641.73z"
   id="path468" />
		<path
   class="st1"
   d="M41.68,628.73h1.66v1.58h-1.66V628.73z M43.24,641.73h-1.48v-9.09h1.48V641.73z"
   id="path470" />
		<path
   class="st1"
   d="M45.55,637.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C47.08,641.91,45.55,641.34,45.55,637.32z M50.91,636.69c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C50.53,640.71,50.91,639.65,50.91,636.69z"
   id="path472" />
		<path
   class="st1"
   d="M56.24,641.73h-1.48v-13h1.48V641.73z"
   id="path474" />
		<path
   class="st1"
   d="M60.23,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H60.23z M63.78,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H63.78z"
   id="path476" />
		<path
   class="st1"
   d="M72.73,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H72.73z"
   id="path478" />
		<path
   class="st1"
   d="M81.55,635.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H81.55z"
   id="path480" />
		<path
   class="st1"
   d="M87.23,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H87.23z M90.78,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H90.78z"
   id="path482" />
		<path
   class="st1"
   d="M103.47,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M100.14,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C102.03,637.23,100.14,637.11,100.14,639.03z"
   id="path484" />
		<path
   class="st1"
   d="M112.6,632.64h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V632.64z M110.87,633.69c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C112.63,635.79,112.72,633.69,110.87,633.69z"
   id="path486" />
		<path
   class="st1"
   d="M121.47,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M118.14,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C120.03,637.23,118.14,637.11,118.14,639.03z"
   id="path488" />
		<path
   class="st1"
   d="M125.66,628.73h1.66v1.58h-1.66V628.73z M127.23,641.73h-1.48v-9.09h1.48V641.73z"
   id="path490" />
		<path
   class="st1"
   d="M134.72,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H134.72z"
   id="path492" />
		<path
   class="st1"
   d="M141.47,641.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C144.64,641.14,143.27,641.91,141.47,641.91z"
   id="path494" />
		<path
   class="st1"
   d="M146.94,632.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H146.94z"
   id="path496" />
		<path
   class="st1"
   d="M160.53,635.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H160.53z"
   id="path498" />
		<path
   class="st1"
   d="M169.71,641.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H169.71z"
   id="path500" />
		<path
   class="st1"
   d="M173.65,628.73h1.66v1.58h-1.66V628.73z M175.22,641.73h-1.48v-9.09h1.48V641.73z"
   id="path502" />
		<path
   class="st1"
   d="M179.21,641.73h-1.48v-13h1.48V641.73z"
   id="path504" />
		<path
   class="st1"
   d="M186.58,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M184.87,633.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C186.58,635.61,186.5,633.67,184.87,633.67z"
   id="path506" />
		<path
   class="st1"
   d="M192.3,634.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V634.01z"
   id="path508" />
		<path
   class="st1"
   d="M198.2,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H198.2z M201.75,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H201.75z"
   id="path510" />
		<path
   class="st1"
   d="M210.7,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H210.7z"
   id="path512" />
		<path
   class="st1"
   d="M223.44,640.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V640.42z M220.11,639.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C222,637.23,220.11,637.11,220.11,639.03z"
   id="path514" />
		<path
   class="st1"
   d="M232.69,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H232.69z"
   id="path516" />
		<path
   class="st1"
   d="M241.57,628.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V628.73z M239.85,633.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C241.57,635.61,241.49,633.67,239.85,633.67z"
   id="path518" />
		<path
   class="st1"
   d="M248.62,632.64h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98    l-1.94-7.74h-0.04l-2.03,7.74h-1.98L248.62,632.64z"
   id="path520" />
		<path
   class="st1"
   d="M262.5,637.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C264.03,641.91,262.5,641.34,262.5,637.32z M267.86,636.69c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C267.48,640.71,267.86,639.65,267.86,636.69z"
   id="path522" />
		<path
   class="st1"
   d="M276.21,641.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H276.21z"
   id="path524" />
		<path
   class="st1"
   d="M286.19,637.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H286.19z M289.73,636.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H289.73z"
   id="path526" />
		<path
   class="st1"
   d="M298.68,641.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H298.68z"
   id="path528" />
	</g></a>
	<a
   id="a63489"
   xlink:title="Birth registration and identity"
   xlink:show="Birth registration and identity"
   target="blank"
   xlink:href="/child-participation#registration"><g
     id="g588">
		<path
   class="st2"
   d="M1116.17,708.73v-13h4.23c1.8,0,2.41,0.61,2.9,1.33c0.45,0.7,0.52,1.48,0.52,1.73c0,1.62-0.56,2.7-2.23,3.08    v0.09c1.85,0.22,2.67,1.33,2.67,3.11c0,3.33-2.43,3.66-3.91,3.66H1116.17z M1117.83,701.21h2.41c1.3-0.02,1.93-0.81,1.93-2.07    c0-1.08-0.61-1.96-2-1.96h-2.34V701.21z M1117.83,707.29h2.34c1.76,0,2.4-1.26,2.4-2.21c0-2.07-1.28-2.43-2.97-2.43h-1.76V707.29z    "
   id="path532" />
		<path
   class="st2"
   d="M1126.72,695.73h1.66v1.58h-1.66V695.73z M1128.29,708.73h-1.48v-9.09h1.48V708.73z"
   id="path534" />
		<path
   class="st2"
   d="M1132.37,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path536" />
		<path
   class="st2"
   d="M1137,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31c0.11,0,0.34-0.04,0.67-0.07    v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1137z"
   id="path538" />
		<path
   class="st2"
   d="M1146.77,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1146.77z"
   id="path540" />
		<path
   class="st2"
   d="M1156.37,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path542" />
		<path
   class="st2"
   d="M1162.27,704.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1162.27z M1165.82,703.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1165.82z"
   id="path544" />
		<path
   class="st2"
   d="M1174.64,699.64h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V699.64z M1172.91,700.69c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1174.67,702.79,1174.76,700.69,1172.91,700.69z"
   id="path546" />
		<path
   class="st2"
   d="M1178.7,695.73h1.66v1.58h-1.66V695.73z M1180.27,708.73h-1.48v-9.09h1.48V708.73z"
   id="path548" />
		<path
   class="st2"
   d="M1185.51,708.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1188.68,708.14,1187.31,708.91,1185.51,708.91z"
   id="path550" />
		<path
   class="st2"
   d="M1190.98,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1190.98z"
   id="path552" />
		<path
   class="st2"
   d="M1197.35,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path554" />
		<path
   class="st2"
   d="M1206.5,707.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.42z M1203.17,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1205.06,704.23,1203.17,704.11,1203.17,706.03z"
   id="path556" />
		<path
   class="st2"
   d="M1210.98,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1210.98z"
   id="path558" />
		<path
   class="st2"
   d="M1215.69,695.73h1.66v1.58h-1.66V695.73z M1217.26,708.73h-1.48v-9.09h1.48V708.73z"
   id="path560" />
		<path
   class="st2"
   d="M1219.56,704.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1221.09,708.91,1219.56,708.34,1219.56,704.32z M1224.93,703.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1224.55,707.71,1224.93,706.65,1224.93,703.69z"
   id="path562" />
		<path
   class="st2"
   d="M1233.75,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1233.75z"
   id="path564" />
		<path
   class="st2"
   d="M1246.49,707.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.42z M1243.16,706.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1245.05,704.23,1243.16,704.11,1243.16,706.03z"
   id="path566" />
		<path
   class="st2"
   d="M1255.74,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1255.74z"
   id="path568" />
		<path
   class="st2"
   d="M1264.62,695.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V695.73z M1262.91,700.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1264.62,702.61,1264.55,700.67,1262.91,700.67z"
   id="path570" />
		<path
   class="st2"
   d="M1272.68,695.73h1.66v1.58h-1.66V695.73z M1274.25,708.73h-1.48v-9.09h1.48V708.73z"
   id="path572" />
		<path
   class="st2"
   d="M1281.61,695.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V695.73z M1279.9,700.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1281.61,702.61,1281.54,700.67,1279.9,700.67z"
   id="path574" />
		<path
   class="st2"
   d="M1287.24,704.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1287.24z M1290.79,703.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1290.79z"
   id="path576" />
		<path
   class="st2"
   d="M1299.74,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1299.74z"
   id="path578" />
		<path
   class="st2"
   d="M1303.96,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1303.96z"
   id="path580" />
		<path
   class="st2"
   d="M1308.68,695.73h1.66v1.58h-1.66V695.73z M1310.25,708.73h-1.48v-9.09h1.48V708.73z"
   id="path582" />
		<path
   class="st2"
   d="M1312.96,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1312.96z"
   id="path584" />
		<path
   class="st2"
   d="M1320.54,707.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1320.54,707.04z"
   id="path586" />
	</g></a>
	<a
   id="a17515"
   xlink:href="/child-protection#care"
   target="blank"
   xlink:title="Children without parental care"
   xlink:show="Children without parental care"><g
     id="g644">
		<path
   class="st1"
   d="M37.68,699.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z"
   id="path590" />
		<path
   class="st1"
   d="M46.74,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z"
   id="path592" />
		<path
   class="st1"
   d="M50.68,695.73h1.66v1.58h-1.66V695.73z M52.24,708.73h-1.48v-9.09h1.48V708.73z"
   id="path594" />
		<path
   class="st1"
   d="M56.24,708.73h-1.48v-13h1.48V708.73z"
   id="path596" />
		<path
   class="st1"
   d="M63.6,695.73h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V695.73z M61.89,700.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,702.61,63.53,700.67,61.89,700.67z"
   id="path598" />
		<path
   class="st1"
   d="M69.32,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path600" />
		<path
   class="st1"
   d="M75.23,704.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H75.23z M78.77,703.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H78.77z"
   id="path602" />
		<path
   class="st1"
   d="M87.72,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H87.72z"
   id="path604" />
		<path
   class="st1"
   d="M94.65,699.64h1.64l1.64,7.83h0.04l2.02-7.83h2.09l1.85,7.83h0.04l1.8-7.83h1.57l-2.43,9.09h-1.98l-1.94-7.74    h-0.04l-2.03,7.74h-1.98L94.65,699.64z"
   id="path606" />
		<path
   class="st1"
   d="M108.65,695.73h1.66v1.58h-1.66V695.73z M110.22,708.73h-1.48v-9.09h1.48V708.73z"
   id="path608" />
		<path
   class="st1"
   d="M112.94,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H112.94z"
   id="path610" />
		<path
   class="st1"
   d="M122.71,708.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H122.71z"
   id="path612" />
		<path
   class="st1"
   d="M126.53,704.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C128.06,708.91,126.53,708.34,126.53,704.32z M131.89,703.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C131.51,707.71,131.89,706.65,131.89,703.69z"
   id="path614" />
		<path
   class="st1"
   d="M140.64,699.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V699.64z"
   id="path616" />
		<path
   class="st1"
   d="M144.94,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H144.94z"
   id="path618" />
		<path
   class="st1"
   d="M155.38,700.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V700.72z M158.89,704.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C158.68,707.71,158.89,706.47,158.89,704.04z"
   id="path620" />
		<path
   class="st1"
   d="M167.46,707.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.42z M164.13,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C166.02,704.23,164.13,704.11,164.13,706.03z"
   id="path622" />
		<path
   class="st1"
   d="M173.31,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path624" />
		<path
   class="st1"
   d="M179.21,704.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H179.21z M182.76,703.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H182.76z"
   id="path626" />
		<path
   class="st1"
   d="M191.71,708.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H191.71z"
   id="path628" />
		<path
   class="st1"
   d="M195.93,699.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H195.93z"
   id="path630" />
		<path
   class="st1"
   d="M205.46,707.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.42z M202.13,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C204.02,704.23,202.13,704.11,202.13,706.03z"
   id="path632" />
		<path
   class="st1"
   d="M211.22,708.73h-1.48v-13h1.48V708.73z"
   id="path634" />
		<path
   class="st1"
   d="M222.52,702.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H222.52z"
   id="path636" />
		<path
   class="st1"
   d="M231.45,707.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V707.42z M228.12,706.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C230.01,704.23,228.12,704.11,228.12,706.03z"
   id="path638" />
		<path
   class="st1"
   d="M237.3,701.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V701.01z"
   id="path640" />
		<path
   class="st1"
   d="M243.2,704.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H243.2z M246.75,703.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H246.75z"
   id="path642" />
	</g></a>
	<a
   id="a63510"><g
     id="g682">
		<path
   class="st2"
   d="M1200.71,766.32c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.58,0,3.57,1.33,3.4,3.85H1200.71z"
   id="path646" />
		<path
   class="st2"
   d="M1209.76,775.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1209.76z"
   id="path648" />
		<path
   class="st2"
   d="M1213.7,762.73h1.66v1.58h-1.66V762.73z M1215.27,775.73h-1.48v-9.09h1.48V775.73z"
   id="path650" />
		<path
   class="st2"
   d="M1219.26,775.73h-1.48v-13h1.48V775.73z"
   id="path652" />
		<path
   class="st2"
   d="M1226.62,762.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V762.73z M1224.91,767.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1226.62,769.61,1226.55,767.67,1224.91,767.67z"
   id="path654" />
		<path
   class="st2"
   d="M1236.42,767.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V767.72z M1239.93,771.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1239.71,774.71,1239.93,773.47,1239.93,771.04z"
   id="path656" />
		<path
   class="st2"
   d="M1248.49,774.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V774.42z M1245.16,773.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1247.05,771.23,1245.16,771.11,1245.16,773.03z"
   id="path658" />
		<path
   class="st2"
   d="M1254.34,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z"
   id="path660" />
		<path
   class="st2"
   d="M1258.97,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1258.97z"
   id="path662" />
		<path
   class="st2"
   d="M1263.68,762.73h1.66v1.58h-1.66V762.73z M1265.25,775.73h-1.48v-9.09h1.48V775.73z"
   id="path664" />
		<path
   class="st2"
   d="M1272.56,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1272.56z"
   id="path666" />
		<path
   class="st2"
   d="M1276.68,762.73h1.66v1.58h-1.66V762.73z M1278.25,775.73h-1.48v-9.09h1.48V775.73z"
   id="path668" />
		<path
   class="st2"
   d="M1282.4,767.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V767.72z M1285.92,771.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1285.7,774.71,1285.92,773.47,1285.92,771.04z"
   id="path670" />
		<path
   class="st2"
   d="M1294.48,774.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V774.42z M1291.15,773.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1293.04,771.23,1291.15,771.11,1291.15,773.03z"
   id="path672" />
		<path
   class="st2"
   d="M1298.96,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1298.96z"
   id="path674" />
		<path
   class="st2"
   d="M1303.68,762.73h1.66v1.58h-1.66V762.73z M1305.25,775.73h-1.48v-9.09h1.48V775.73z"
   id="path676" />
		<path
   class="st2"
   d="M1307.55,771.32c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1309.08,775.91,1307.55,775.34,1307.55,771.32z M1312.92,770.69c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1312.54,774.71,1312.92,773.65,1312.92,770.69z"
   id="path678" />
		<path
   class="st2"
   d="M1321.74,775.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1321.74z"
   id="path680" />
	</g></a>
	<a
   id="a23755"
   xlink:title="Justice for children"
   xlink:show="Justice for children"
   target="blank"
   xlink:href="/child-protection#justice"><g
     id="g720">
		<path
   class="st1"
   d="M32.77,771.7c0.04,1.17-0.11,2.92,1.58,2.92c1.76,0,1.87-1.51,1.87-3.1v-8.79h1.66v9.78    c0,0.7-0.02,3.49-3.58,3.49c-0.72,0-2.11-0.25-2.74-1.28c-0.52-0.87-0.52-1.98-0.52-3.03H32.77z"
   id="path684" />
		<path
   class="st1"
   d="M45.66,766.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H45.6c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V766.64z"
   id="path686" />
		<path
   class="st1"
   d="M52.48,775.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C55.65,775.14,54.28,775.91,52.48,775.91z"
   id="path688" />
		<path
   class="st1"
   d="M57.95,766.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H57.95z"
   id="path690" />
		<path
   class="st1"
   d="M62.66,762.73h1.66v1.58h-1.66V762.73z M64.23,775.73h-1.48v-9.09h1.48V775.73z"
   id="path692" />
		<path
   class="st1"
   d="M71.54,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H71.54z"
   id="path694" />
		<path
   class="st1"
   d="M77.23,771.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H77.23z M80.77,770.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H80.77z"
   id="path696" />
		<path
   class="st1"
   d="M89.05,766.64v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3    v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H89.05z"
   id="path698" />
		<path
   class="st1"
   d="M93.53,771.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C95.06,775.91,93.53,775.34,93.53,771.32z M98.9,770.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C98.52,774.71,98.9,773.65,98.9,770.69z"
   id="path700" />
		<path
   class="st1"
   d="M104.32,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z"
   id="path702" />
		<path
   class="st1"
   d="M117.53,769.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H117.53z"
   id="path704" />
		<path
   class="st1"
   d="M126.71,775.73v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H126.71z"
   id="path706" />
		<path
   class="st1"
   d="M130.65,762.73h1.66v1.58h-1.66V762.73z M132.22,775.73h-1.48v-9.09h1.48V775.73z"
   id="path708" />
		<path
   class="st1"
   d="M136.21,775.73h-1.48v-13h1.48V775.73z"
   id="path710" />
		<path
   class="st1"
   d="M143.57,762.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V762.73z M141.86,767.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C143.57,769.61,143.5,767.67,141.86,767.67z"
   id="path712" />
		<path
   class="st1"
   d="M149.3,768.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V768.01z"
   id="path714" />
		<path
   class="st1"
   d="M155.2,771.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H155.2z M158.75,770.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H158.75z"
   id="path716" />
		<path
   class="st1"
   d="M167.69,775.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H167.69z"
   id="path718" />
	</g></a>
	<a
   id="a63538"><g
     id="g772">
		<path
   class="st2"
   d="M1137.73,833.33c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.58,0,3.57,1.33,3.4,3.85H1137.73z"
   id="path722" />
		<path
   class="st2"
   d="M1141.72,829.74h1.66v1.58h-1.66V829.74z M1143.29,842.74h-1.48v-9.09h1.48V842.74z"
   id="path724" />
		<path
   class="st2"
   d="M1144.8,833.65h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1144.8,833.65z"
   id="path726" />
		<path
   class="st2"
   d="M1153.71,829.74h1.66v1.58h-1.66V829.74z M1155.28,842.74h-1.48v-9.09h1.48V842.74z"
   id="path728" />
		<path
   class="st2"
   d="M1159.27,842.74h-1.48v-13h1.48V842.74z"
   id="path730" />
		<path
   class="st2"
   d="M1170.5,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M1167.17,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C1169.06,838.24,1167.17,838.12,1167.17,840.04z"
   id="path732" />
		<path
   class="st2"
   d="M1179.76,842.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1179.76z"
   id="path734" />
		<path
   class="st2"
   d="M1188.63,829.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V829.74z M1186.92,834.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1188.63,836.62,1188.56,834.68,1186.92,834.68z"
   id="path736" />
		<path
   class="st2"
   d="M1198.42,834.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V834.73z M1201.93,838.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1201.72,841.72,1201.93,840.47,1201.93,838.04z"
   id="path738" />
		<path
   class="st2"
   d="M1205.57,838.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1207.1,842.92,1205.57,842.35,1205.57,838.33z M1210.93,837.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1210.56,841.72,1210.93,840.65,1210.93,837.7z"
   id="path740" />
		<path
   class="st2"
   d="M1216.26,842.74h-1.48v-13h1.48V842.74z"
   id="path742" />
		<path
   class="st2"
   d="M1218.69,829.74h1.66v1.58h-1.66V829.74z M1220.26,842.74h-1.48v-9.09h1.48V842.74z"
   id="path744" />
		<path
   class="st2"
   d="M1222.97,833.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1222.97z"
   id="path746" />
		<path
   class="st2"
   d="M1227.69,829.74h1.66v1.58h-1.66V829.74z M1229.26,842.74h-1.48v-9.09h1.48V842.74z"
   id="path748" />
		<path
   class="st2"
   d="M1236.56,836.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1236.56z"
   id="path750" />
		<path
   class="st2"
   d="M1245.49,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M1242.16,840.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1244.05,838.24,1242.16,838.12,1242.16,840.04z"
   id="path752" />
		<path
   class="st2"
   d="M1251.25,842.74h-1.48v-13h1.48V842.74z"
   id="path754" />
		<path
   class="st2"
   d="M1258.07,833.65v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06    c-1.57-0.11-1.84,0.56-1.84,1.3v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1258.07z"
   id="path756" />
		<path
   class="st2"
   d="M1264.34,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path758" />
		<path
   class="st2"
   d="M1270.24,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1270.24z M1273.79,837.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1273.79z"
   id="path760" />
		<path
   class="st2"
   d="M1279.24,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1279.24z M1282.79,837.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1282.79z"
   id="path762" />
		<path
   class="st2"
   d="M1291.61,829.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V829.74z M1289.9,834.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1291.61,836.62,1291.54,834.68,1289.9,834.68z"
   id="path764" />
		<path
   class="st2"
   d="M1295.55,838.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1297.08,842.92,1295.55,842.35,1295.55,838.33z M1300.91,837.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1300.54,841.72,1300.91,840.65,1300.91,837.7z"
   id="path766" />
		<path
   class="st2"
   d="M1309.27,842.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1309.27z"
   id="path768" />
		<path
   class="st2"
   d="M1320.48,842.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1323.65,842.15,1322.28,842.92,1320.48,842.92z"
   id="path770" />
	</g></a>
	<a
   id="a25350"
   xlink:href="/child-protection#marriage"
   target="blank"
   xlink:title="Child marriage and other harmful practices"
   xlink:show="Child marriage and other harmful practices"><g
     id="g848">
		<path
   class="st1"
   d="M37.68,833.33c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z"
   id="path774" />
		<path
   class="st1"
   d="M46.74,842.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z"
   id="path776" />
		<path
   class="st1"
   d="M50.68,829.74h1.66v1.58h-1.66V829.74z M52.24,842.74h-1.48v-9.09h1.48V842.74z"
   id="path778" />
		<path
   class="st1"
   d="M56.24,842.74h-1.48v-13h1.48V842.74z"
   id="path780" />
		<path
   class="st1"
   d="M63.6,829.74h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V829.74z M61.89,834.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,836.62,63.53,834.68,61.89,834.68z"
   id="path782" />
		<path
   class="st1"
   d="M76.25,842.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H76.25z"
   id="path784" />
		<path
   class="st1"
   d="M89.47,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M86.14,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C88.03,838.24,86.14,838.12,86.14,840.04z"
   id="path786" />
		<path
   class="st1"
   d="M95.32,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path788" />
		<path
   class="st1"
   d="M101.31,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path790" />
		<path
   class="st1"
   d="M105.65,829.74h1.66v1.58h-1.66V829.74z M107.21,842.74h-1.48v-9.09h1.48V842.74z"
   id="path792" />
		<path
   class="st1"
   d="M114.45,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M111.12,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C113.01,838.24,111.12,838.12,111.12,840.04z"
   id="path794" />
		<path
   class="st1"
   d="M123.58,833.65h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V833.65z M121.85,834.69c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C123.61,836.8,123.7,834.69,121.85,834.69z"
   id="path796" />
		<path
   class="st1"
   d="M129.21,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H129.21z M132.76,837.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H132.76z"
   id="path798" />
		<path
   class="st1"
   d="M145.45,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M142.12,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C144.01,838.24,142.12,838.12,142.12,840.04z"
   id="path800" />
		<path
   class="st1"
   d="M154.7,842.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H154.7z"
   id="path802" />
		<path
   class="st1"
   d="M163.57,829.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V829.74z M161.86,834.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C163.57,836.62,163.5,834.68,161.86,834.68z"
   id="path804" />
		<path
   class="st1"
   d="M171.51,838.33c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C173.04,842.92,171.51,842.35,171.51,838.33z M176.87,837.7c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C176.5,841.72,176.87,840.65,176.87,837.7z"
   id="path806" />
		<path
   class="st1"
   d="M180.92,833.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H180.92z"
   id="path808" />
		<path
   class="st1"
   d="M190.7,842.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H190.7z"
   id="path810" />
		<path
   class="st1"
   d="M196.2,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H196.2z M199.75,837.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H199.75z"
   id="path812" />
		<path
   class="st1"
   d="M205.29,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path814" />
		<path
   class="st1"
   d="M218.69,842.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H218.69z"
   id="path816" />
		<path
   class="st1"
   d="M227.44,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M224.1,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C226,838.24,224.1,838.12,224.1,840.04z"
   id="path818" />
		<path
   class="st1"
   d="M233.28,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path820" />
		<path
   class="st1"
   d="M242.21,842.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H242.21z"
   id="path822" />
		<path
   class="st1"
   d="M251.01,833.65v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3    v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H251.01z"
   id="path824" />
		<path
   class="st1"
   d="M260.61,833.65h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V833.65z"
   id="path826" />
		<path
   class="st1"
   d="M266.19,842.74h-1.48v-13h1.48V842.74z"
   id="path828" />
		<path
   class="st1"
   d="M274.34,834.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V834.73z M277.85,838.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C277.64,841.72,277.85,840.47,277.85,838.04z"
   id="path830" />
		<path
   class="st1"
   d="M283.27,835.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V835c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V835.02z"
   id="path832" />
		<path
   class="st1"
   d="M292.41,841.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V841.43z M289.08,840.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C290.97,838.24,289.08,838.12,289.08,840.04z"
   id="path834" />
		<path
   class="st1"
   d="M301.49,836.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H301.49z"
   id="path836" />
		<path
   class="st1"
   d="M305.9,833.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H305.9z"
   id="path838" />
		<path
   class="st1"
   d="M310.61,829.74h1.66v1.58h-1.66V829.74z M312.18,842.74h-1.48v-9.09h1.48V842.74z"
   id="path840" />
		<path
   class="st1"
   d="M319.49,836.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H319.49z"
   id="path842" />
		<path
   class="st1"
   d="M325.17,838.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H325.17z M328.72,837.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H328.72z"
   id="path844" />
		<path
   class="st1"
   d="M335.42,842.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C338.58,842.15,337.22,842.92,335.42,842.92z"
   id="path846" />
	</g></a>
	<a
   id="a63583"
   xlink:href="/child-participation#information"
   target="blank"
   xlink:title="Information, Internet and Protection of privacy"
   xlink:show="Information, Internet and Protection of privacy"><g
     id="g934">
		<path
   class="st2"
   d="M996.89,909.74h-1.66v-13h1.66V909.74z"
   id="path850" />
		<path
   class="st2"
   d="M1004.79,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1004.79z"
   id="path852" />
		<path
   class="st2"
   d="M1009.13,900.65v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06    c-1.57-0.11-1.84,0.56-1.84,1.3v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1009.13z"
   id="path854" />
		<path
   class="st2"
   d="M1013.61,905.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1015.14,909.92,1013.61,909.35,1013.61,905.33z M1018.98,904.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1018.6,908.72,1018.98,907.65,1018.98,904.7z"
   id="path856" />
		<path
   class="st2"
   d="M1024.4,902.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V902c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.02z"
   id="path858" />
		<path
   class="st2"
   d="M1033.32,909.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1033.32z"
   id="path860" />
		<path
   class="st2"
   d="M1046.54,908.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.43z M1043.21,907.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1045.1,905.24,1043.21,905.12,1043.21,907.04z"
   id="path862" />
		<path
   class="st2"
   d="M1051.02,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1051.02z"
   id="path864" />
		<path
   class="st2"
   d="M1055.73,896.74h1.66v1.58h-1.66V896.74z M1057.3,909.74h-1.48v-9.09h1.48V909.74z"
   id="path866" />
		<path
   class="st2"
   d="M1059.6,905.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1061.13,909.92,1059.6,909.35,1059.6,905.33z M1064.97,904.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1064.59,908.72,1064.97,907.65,1064.97,904.7z"
   id="path868" />
		<path
   class="st2"
   d="M1073.79,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1073.79z"
   id="path870" />
		<path
   class="st2"
   d="M1078.11,907.87h1.85l-1.64,4.16h-1.15L1078.11,907.87z"
   id="path872" />
		<path
   class="st2"
   d="M1085.72,896.74h1.66v1.58h-1.66V896.74z M1087.29,909.74h-1.48v-9.09h1.48V909.74z"
   id="path874" />
		<path
   class="st2"
   d="M1094.77,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1094.77z"
   id="path876" />
		<path
   class="st2"
   d="M1099,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31c0.11,0,0.34-0.04,0.67-0.07    v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1099z"
   id="path878" />
		<path
   class="st2"
   d="M1105.29,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1105.29z M1108.83,904.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1108.83z"
   id="path880" />
		<path
   class="st2"
   d="M1114.38,902.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V902c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.02z"
   id="path882" />
		<path
   class="st2"
   d="M1123.77,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1123.77z"
   id="path884" />
		<path
   class="st2"
   d="M1129.28,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1129.28z M1132.83,904.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1132.83z"
   id="path886" />
		<path
   class="st2"
   d="M1137,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31c0.11,0,0.34-0.04,0.67-0.07    v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1137z"
   id="path888" />
		<path
   class="st2"
   d="M1150.52,908.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.43z M1147.19,907.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1149.08,905.24,1147.19,905.12,1147.19,907.04z"
   id="path890" />
		<path
   class="st2"
   d="M1159.77,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1159.77z"
   id="path892" />
		<path
   class="st2"
   d="M1168.65,896.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V896.74z M1166.94,901.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1168.65,903.62,1168.58,901.68,1166.94,901.68z"
   id="path894" />
		<path
   class="st2"
   d="M1178.44,901.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.73z M1181.95,905.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1181.73,908.72,1181.95,907.47,1181.95,905.04z"
   id="path896" />
		<path
   class="st2"
   d="M1187.37,902.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V902c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.02z"
   id="path898" />
		<path
   class="st2"
   d="M1191.58,905.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1193.11,909.92,1191.58,909.35,1191.58,905.33z M1196.94,904.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1196.56,908.72,1196.94,907.65,1196.94,904.7z"
   id="path900" />
		<path
   class="st2"
   d="M1200.99,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1200.99z"
   id="path902" />
		<path
   class="st2"
   d="M1207.27,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1207.27z M1210.82,904.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1210.82z"
   id="path904" />
		<path
   class="st2"
   d="M1219.59,903.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1219.59z"
   id="path906" />
		<path
   class="st2"
   d="M1223.99,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1223.99z"
   id="path908" />
		<path
   class="st2"
   d="M1228.71,896.74h1.66v1.58h-1.66V896.74z M1230.28,909.74h-1.48v-9.09h1.48V909.74z"
   id="path910" />
		<path
   class="st2"
   d="M1232.58,905.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1234.11,909.92,1232.58,909.35,1232.58,905.33z M1237.95,904.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1237.57,908.72,1237.95,907.65,1237.95,904.7z"
   id="path912" />
		<path
   class="st2"
   d="M1246.77,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1246.77z"
   id="path914" />
		<path
   class="st2"
   d="M1254.58,905.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1256.11,909.92,1254.58,909.35,1254.58,905.33z M1259.94,904.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1259.56,908.72,1259.94,907.65,1259.94,904.7z"
   id="path916" />
		<path
   class="st2"
   d="M1264.1,900.65v-1.76c0-1.84,1.3-2.2,2.61-2.2c0.31,0,0.49,0.02,0.7,0.05v1.06c-1.57-0.11-1.84,0.56-1.84,1.3    v1.55h1.84v1.12h-1.84v7.98h-1.48v-7.98h-1.4v-1.12H1264.1z"
   id="path918" />
		<path
   class="st2"
   d="M1274.43,901.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.73z M1277.94,905.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C1277.72,908.72,1277.94,907.47,1277.94,905.04z"
   id="path920" />
		<path
   class="st2"
   d="M1283.36,902.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55V902c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V902.02z"
   id="path922" />
		<path
   class="st2"
   d="M1287.7,896.74h1.66v1.58h-1.66V896.74z M1289.26,909.74h-1.48v-9.09h1.48V909.74z"
   id="path924" />
		<path
   class="st2"
   d="M1290.77,900.65h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L1290.77,900.65z"
   id="path926" />
		<path
   class="st2"
   d="M1304.49,908.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.43z M1301.16,907.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1303.05,905.24,1301.16,905.12,1301.16,907.04z"
   id="path928" />
		<path
   class="st2"
   d="M1313.56,903.57c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1313.56z"
   id="path930" />
		<path
   class="st2"
   d="M1320.55,908.05h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1320.55,908.05z"
   id="path932" />
	</g></a>
	<a
   id="a30125"
   xlink:href="/child-protection#labour"
   xlink:title="Child exploitation"
   xlink:show="Child exploitation"
   target="blank"><g
     id="g970">
		<path
   class="st1"
   d="M37.68,900.33c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.11-2.83,4.11-3.67,4.11    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H37.68z"
   id="path936" />
		<path
   class="st1"
   d="M46.74,909.74v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08h0.07    c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H46.74z"
   id="path938" />
		<path
   class="st1"
   d="M50.68,896.74h1.66v1.58h-1.66V896.74z M52.24,909.74h-1.48v-9.09h1.48V909.74z"
   id="path940" />
		<path
   class="st1"
   d="M56.24,909.74h-1.48v-13h1.48V909.74z"
   id="path942" />
		<path
   class="st1"
   d="M63.6,896.74h1.48v13H63.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V896.74z M61.89,901.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C63.6,903.62,63.53,901.68,61.89,901.68z"
   id="path944" />
		<path
   class="st1"
   d="M73.23,905.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H73.23z M76.78,904.56    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H76.78z"
   id="path946" />
		<path
   class="st1"
   d="M87.36,909.74h-1.94l-2.11-3.73l-1.96,3.73H79.6l2.83-4.75l-2.59-4.34h1.89l1.73,3.26l1.84-3.26h1.78    l-2.72,4.34L87.36,909.74z"
   id="path948" />
		<path
   class="st1"
   d="M90.38,901.73h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V901.73z M93.89,905.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C93.68,908.72,93.89,907.47,93.89,905.04z"
   id="path950" />
		<path
   class="st1"
   d="M99.22,909.74h-1.48v-13h1.48V909.74z"
   id="path952" />
		<path
   class="st1"
   d="M101.52,905.33c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C103.06,909.92,101.52,909.35,101.52,905.33z M106.89,904.7c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C106.51,908.72,106.89,907.65,106.89,904.7z"
   id="path954" />
		<path
   class="st1"
   d="M110.65,896.74h1.66v1.58h-1.66V896.74z M112.22,909.74h-1.48v-9.09h1.48V909.74z"
   id="path956" />
		<path
   class="st1"
   d="M114.94,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H114.94z"
   id="path958" />
		<path
   class="st1"
   d="M124.46,908.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V908.43z M121.13,907.04c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C123.02,905.24,121.13,905.12,121.13,907.04z"
   id="path960" />
		<path
   class="st1"
   d="M128.94,900.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H128.94z"
   id="path962" />
		<path
   class="st1"
   d="M133.65,896.74h1.66v1.58h-1.66V896.74z M135.22,909.74h-1.48v-9.09h1.48V909.74z"
   id="path964" />
		<path
   class="st1"
   d="M137.52,905.33c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C139.05,909.92,137.52,909.35,137.52,905.33z M142.89,904.7c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C142.51,908.72,142.89,907.65,142.89,904.7z"
   id="path966" />
		<path
   class="st1"
   d="M151.71,909.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H151.71z"
   id="path968" />
	</g></a>
	<a
   id="a42792"
   xlink:href="/child-participation#leisure"
   target="blank"
   xlink:title="Leisure and culture"
   xlink:show="Leisure and culture"><g
     id="g1006">
		<path
   class="st4"
   d="M1187,976.73v-13h1.66v11.56h4.77v1.44H1187z"
   id="path972" />
		<path
   class="st4"
   d="M1196.27,972.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1196.27z M1199.81,971.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1199.81z"
   id="path974" />
		<path
   class="st4"
   d="M1203.7,963.73h1.66v1.58h-1.66V963.73z M1205.27,976.73h-1.48v-9.09h1.48V976.73z"
   id="path976" />
		<path
   class="st4"
   d="M1210.5,976.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1213.67,976.14,1212.3,976.91,1210.5,976.91z"
   id="path978" />
		<path
   class="st4"
   d="M1220.67,967.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.64z"
   id="path980" />
		<path
   class="st4"
   d="M1226.34,969.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V969.01z"
   id="path982" />
		<path
   class="st4"
   d="M1232.25,972.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1232.25z M1235.79,971.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1235.79z"
   id="path984" />
		<path
   class="st4"
   d="M1248.48,975.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V975.42z M1245.15,974.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1247.04,972.23,1245.15,972.11,1245.15,974.03z"
   id="path986" />
		<path
   class="st4"
   d="M1257.74,976.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1257.74z"
   id="path988" />
		<path
   class="st4"
   d="M1266.61,963.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V963.73z M1264.9,968.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1266.61,970.61,1266.54,968.67,1264.9,968.67z"
   id="path990" />
		<path
   class="st4"
   d="M1279.55,970.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1279.55z"
   id="path992" />
		<path
   class="st4"
   d="M1288.66,967.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.64z"
   id="path994" />
		<path
   class="st4"
   d="M1294.24,976.73h-1.48v-13h1.48V976.73z"
   id="path996" />
		<path
   class="st4"
   d="M1296.96,967.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1296.96z"
   id="path998" />
		<path
   class="st4"
   d="M1306.66,967.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.64z"
   id="path1000" />
		<path
   class="st4"
   d="M1312.33,969.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V969.01z"
   id="path1002" />
		<path
   class="st4"
   d="M1318.23,972.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1318.23z M1321.78,971.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1321.78z"
   id="path1004" />
	</g></a>
	<a
   id="a31703"
   xlink:title="Education system"
   xlink:show="Education system"
   xlink:href="/child-education#system"
   target="blank"><g
     id="g1038">
		<path
   class="st4"
   d="M31.96,976.73v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H31.96z"
   id="path1008" />
		<path
   class="st4"
   d="M45.6,963.73h1.48v13H45.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V963.73z M43.89,968.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C45.6,970.61,45.53,968.67,43.89,968.67z"
   id="path1010" />
		<path
   class="st4"
   d="M54.66,967.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H54.6c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V967.64z"
   id="path1012" />
		<path
   class="st4"
   d="M63.55,970.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H63.55z"
   id="path1014" />
		<path
   class="st4"
   d="M72.48,975.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V975.42z M69.15,974.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C71.04,972.23,69.15,972.11,69.15,974.03z"
   id="path1016" />
		<path
   class="st4"
   d="M76.96,967.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H76.96z"
   id="path1018" />
		<path
   class="st4"
   d="M81.67,963.73h1.66v1.58h-1.66V963.73z M83.24,976.73h-1.48v-9.09h1.48V976.73z"
   id="path1020" />
		<path
   class="st4"
   d="M85.54,972.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C87.07,976.91,85.54,976.34,85.54,972.32z M90.91,971.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C90.53,975.71,90.91,974.65,90.91,971.69z"
   id="path1022" />
		<path
   class="st4"
   d="M99.73,976.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H99.73z"
   id="path1024" />
		<path
   class="st4"
   d="M110.47,976.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C113.64,976.14,112.27,976.91,110.47,976.91z"
   id="path1026" />
		<path
   class="st4"
   d="M118.52,975.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L118.52,975.04z"
   id="path1028" />
		<path
   class="st4"
   d="M126.46,976.91c-1.96,0-3.19-0.86-3.13-2.95H125c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C129.62,976.14,128.26,976.91,126.46,976.91z"
   id="path1030" />
		<path
   class="st4"
   d="M131.93,967.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H131.93z"
   id="path1032" />
		<path
   class="st4"
   d="M138.21,972.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H138.21z M141.76,971.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H141.76z"
   id="path1034" />
		<path
   class="st4"
   d="M150.23,976.73v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H150.23z"
   id="path1036" />
	</g></a>
	<a
   id="a36486"
   xlink:href="/child-education#quality"
   target="blank"
   xlink:title="Learning quality and skills"
   xlink:show="Learning quality and skills"><g
     id="g1088">
		<path
   class="st4"
   d="M1140.03,1043.73v-13h1.66v11.56h4.77v1.44H1140.03z"
   id="path1040" />
		<path
   class="st4"
   d="M1149.3,1039.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H1149.3z M1152.85,1038.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1152.85z"
   id="path1042" />
		<path
   class="st4"
   d="M1161.55,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M1158.21,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1160.11,1039.23,1158.21,1039.11,1158.21,1041.03z"
   id="path1044" />
		<path
   class="st4"
   d="M1167.4,1036.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1036.01z"
   id="path1046" />
		<path
   class="st4"
   d="M1176.79,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1176.79z"
   id="path1048" />
		<path
   class="st4"
   d="M1180.73,1030.73h1.66v1.58h-1.66V1030.73z M1182.3,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1050" />
		<path
   class="st4"
   d="M1189.79,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1189.79z"
   id="path1052" />
		<path
   class="st4"
   d="M1198.66,1034.64h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V1034.64z M1196.93,1035.69c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1198.7,1037.79,1198.79,1035.69,1196.93,1035.69z"
   id="path1054" />
		<path
   class="st4"
   d="M1211.66,1034.64h1.48v12.53h-1.48v-4.36h-0.05c-0.5,0.72-1.13,1.1-2,1.1c-2.93,0-3.01-2.61-3.01-4.88    c0-4,1.48-4.57,2.94-4.57c0.95,0,1.58,0.41,2.09,1.26h0.04V1034.64z M1211.66,1039.58c0-1.39,0.16-3.87-1.66-3.87    c-1.85,0-1.85,1.96-1.85,3.33c0,2.43,0.22,3.67,1.8,3.67C1211.58,1042.71,1211.66,1040.78,1211.66,1039.58z"
   id="path1056" />
		<path
   class="st4"
   d="M1220.71,1034.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1034.64z"
   id="path1058" />
		<path
   class="st4"
   d="M1229.53,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M1226.2,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1228.09,1039.23,1226.2,1039.11,1226.2,1041.03z"
   id="path1060" />
		<path
   class="st4"
   d="M1235.29,1043.73h-1.48v-13h1.48V1043.73z"
   id="path1062" />
		<path
   class="st4"
   d="M1237.72,1030.73h1.66v1.58h-1.66V1030.73z M1239.29,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1064" />
		<path
   class="st4"
   d="M1242,1034.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1242z"
   id="path1066" />
		<path
   class="st4"
   d="M1249.58,1042.04h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1249.58,1042.04z"
   id="path1068" />
		<path
   class="st4"
   d="M1263.51,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M1260.18,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1262.07,1039.23,1260.18,1039.11,1260.18,1041.03z"
   id="path1070" />
		<path
   class="st4"
   d="M1272.77,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1272.77z"
   id="path1072" />
		<path
   class="st4"
   d="M1281.64,1030.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V1030.73z M1279.93,1035.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1281.64,1037.61,1281.57,1035.67,1279.93,1035.67z"
   id="path1074" />
		<path
   class="st4"
   d="M1292.51,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1295.68,1043.14,1294.31,1043.91,1292.51,1043.91z"
   id="path1076" />
		<path
   class="st4"
   d="M1299.3,1043.73h-1.48v-13h1.48v7.83h0.04l2.77-3.92h1.8l-3.02,3.91l3.56,5.19h-1.87l-3.24-5.1h-0.04V1043.73    z"
   id="path1078" />
		<path
   class="st4"
   d="M1305.69,1030.73h1.66v1.58h-1.66V1030.73z M1307.25,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1080" />
		<path
   class="st4"
   d="M1311.25,1043.73h-1.48v-13h1.48V1043.73z"
   id="path1082" />
		<path
   class="st4"
   d="M1315.24,1043.73h-1.48v-13h1.48V1043.73z"
   id="path1084" />
		<path
   class="st4"
   d="M1320.48,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1323.65,1043.14,1322.28,1043.91,1320.48,1043.91z"
   id="path1086" />
	</g></a>
	<a
   id="a33329"
   xlink:href="/child-education#participation"
   target="blank"
   xlink:title="Education access and participation"
   xlink:show="Education access and participation"><g
     id="g1152">
		<path
   class="st4"
   d="M31.96,1043.73v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H31.96z"
   id="path1090" />
		<path
   class="st4"
   d="M45.6,1030.73h1.48v13H45.6v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1030.73z M43.89,1035.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C45.6,1037.61,45.53,1035.67,43.89,1035.67z"
   id="path1092" />
		<path
   class="st4"
   d="M54.66,1034.64h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1H54.6c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1034.64z"
   id="path1094" />
		<path
   class="st4"
   d="M63.55,1037.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H63.55z"
   id="path1096" />
		<path
   class="st4"
   d="M72.48,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M69.15,1041.03c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C71.04,1039.23,69.15,1039.11,69.15,1041.03z"
   id="path1098" />
		<path
   class="st4"
   d="M76.96,1034.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H76.96z"
   id="path1100" />
		<path
   class="st4"
   d="M81.67,1030.73h1.66v1.58h-1.66V1030.73z M83.24,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1102" />
		<path
   class="st4"
   d="M85.54,1039.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C87.07,1043.91,85.54,1043.34,85.54,1039.32z M90.91,1038.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C90.53,1042.71,90.91,1041.65,90.91,1038.69z"
   id="path1104" />
		<path
   class="st4"
   d="M99.73,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H99.73z"
   id="path1106" />
		<path
   class="st4"
   d="M112.47,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M109.14,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C111.03,1039.23,109.14,1039.11,109.14,1041.03z"
   id="path1108" />
		<path
   class="st4"
   d="M121.54,1037.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H121.54z"
   id="path1110" />
		<path
   class="st4"
   d="M130.54,1037.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H130.54z"
   id="path1112" />
		<path
   class="st4"
   d="M136.23,1039.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.93-3.17,2.93    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H136.23z M139.78,1038.55    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H139.78z"
   id="path1114" />
		<path
   class="st4"
   d="M146.47,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C149.64,1043.14,148.27,1043.91,146.47,1043.91z"
   id="path1116" />
		<path
   class="st4"
   d="M154.46,1043.91c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C157.63,1043.14,156.27,1043.91,154.46,1043.91z"
   id="path1118" />
		<path
   class="st4"
   d="M168.45,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M165.12,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C167.01,1039.23,165.12,1039.11,165.12,1041.03z"
   id="path1120" />
		<path
   class="st4"
   d="M177.7,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H177.7z"
   id="path1122" />
		<path
   class="st4"
   d="M186.58,1030.73h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1030.73z M184.87,1035.67c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C186.58,1037.61,186.5,1035.67,184.87,1035.67z"
   id="path1124" />
		<path
   class="st4"
   d="M196.37,1035.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1035.72z M199.88,1039.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C199.66,1042.71,199.88,1041.47,199.88,1039.04z"
   id="path1126" />
		<path
   class="st4"
   d="M208.45,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M205.12,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C207.01,1039.23,205.12,1039.11,205.12,1041.03z"
   id="path1128" />
		<path
   class="st4"
   d="M214.29,1036.01h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1036.01z"
   id="path1130" />
		<path
   class="st4"
   d="M218.92,1034.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H218.92z"
   id="path1132" />
		<path
   class="st4"
   d="M223.64,1030.73h1.66v1.58h-1.66V1030.73z M225.2,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1134" />
		<path
   class="st4"
   d="M232.51,1037.56c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H232.51z"
   id="path1136" />
		<path
   class="st4"
   d="M236.63,1030.73h1.66v1.58h-1.66V1030.73z M238.2,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1138" />
		<path
   class="st4"
   d="M242.36,1035.72h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1035.72z M245.87,1039.04c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C245.65,1042.71,245.87,1041.47,245.87,1039.04z"
   id="path1140" />
		<path
   class="st4"
   d="M254.44,1042.42h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1042.42z M251.1,1041.03c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C253,1039.23,251.1,1039.11,251.1,1041.03z"
   id="path1142" />
		<path
   class="st4"
   d="M258.92,1034.64v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H258.92z"
   id="path1144" />
		<path
   class="st4"
   d="M263.63,1030.73h1.66v1.58h-1.66V1030.73z M265.2,1043.73h-1.48v-9.09h1.48V1043.73z"
   id="path1146" />
		<path
   class="st4"
   d="M267.5,1039.32c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C269.03,1043.91,267.5,1043.34,267.5,1039.32z M272.87,1038.69c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C272.49,1042.71,272.87,1041.65,272.87,1038.69z"
   id="path1148" />
		<path
   class="st4"
   d="M281.69,1043.73v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H281.69z"
   id="path1150" />
	</g></a>
	<line
   class="st5"
   x1="724.09"
   y1="393.17"
   x2="724.09"
   y2="380.62"
   id="line1154" />
	<line
   class="st6"
   x1="727.07"
   y1="379.23"
   x2="1322.02"
   y2="379.23"
   id="line1156" />
	<path
   class="st7"
   d="M724.09,395.96L724.09,395.96 M724.09,379.23L724.09,379.23 M1323.51,379.23L1323.51,379.23"
   id="path1158" />
	<path
   class="st0"
   d="M724.09,398.73c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78s-2.78,1.24-2.78,2.78   C721.31,397.49,722.55,398.73,724.09,398.73L724.09,398.73z"
   id="path1160" />
	<line
   class="st8"
   x1="721.32"
   y1="1008.47"
   x2="721.32"
   y2="1046.71"
   id="line1162" />
	<line
   class="st9"
   x1="724.3"
   y1="1048.24"
   x2="1322.02"
   y2="1048.24"
   id="line1164" />
	<path
   class="st10"
   d="M721.32,1005.41L721.32,1005.41 M721.32,1048.24L721.32,1048.24 M1323.51,1048.24L1323.51,1048.24"
   id="path1166" />
	<path
   class="st4"
   d="M721.32,1002.63c1.53,0,2.78,1.24,2.78,2.78c0,1.53-1.24,2.78-2.78,2.78c-1.53,0-2.78-1.25-2.78-2.78   C718.54,1003.87,719.79,1002.63,721.32,1002.63L721.32,1002.63z"
   id="path1168" />
	<path
   class="st11"
   d="M884.35,934.73c9.93,0,42.27,0,61.35,0"
   id="path1170" />
	<line
   class="st12"
   x1="947.2"
   y1="931.95"
   x2="947.2"
   y2="916.62"
   id="line1172" />
	<line
   class="st13"
   x1="950.18"
   y1="915.23"
   x2="1322.02"
   y2="915.23"
   id="line1174" />
	<path
   class="st14"
   d="M881.35,934.73L881.35,934.73 M947.2,934.73L947.2,934.73 M947.2,915.23L947.2,915.23 M1323.51,915.23   L1323.51,915.23"
   id="path1176" />
	<path
   class="st2"
   d="M881.35,937.51c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C878.58,936.27,879.82,937.51,881.35,937.51L881.35,937.51z"
   id="path1178" />
	<line
   class="st15"
   x1="940.02"
   y1="867.73"
   x2="1007.11"
   y2="867.73"
   id="line1180" />
	<line
   class="st12"
   x1="1008.6"
   y1="864.95"
   x2="1008.6"
   y2="849.62"
   id="line1182" />
	<line
   class="st16"
   x1="1011.57"
   y1="848.23"
   x2="1322.03"
   y2="848.23"
   id="line1184" />
	<path
   class="st14"
   d="M937.03,867.73L937.03,867.73 M1008.6,867.73L1008.6,867.73 M1008.6,848.23L1008.6,848.23 M1323.51,848.23   L1323.51,848.23"
   id="path1186" />
	<path
   class="st2"
   d="M937.03,870.51c1.53,0,2.78-1.24,2.78-2.78s-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   S935.5,870.51,937.03,870.51L937.03,870.51z"
   id="path1188" />
	<line
   class="st17"
   x1="971.9"
   y1="798.73"
   x2="1019.23"
   y2="798.73"
   id="line1190" />
	<path
   class="st18"
   d="M1020.76,795.73c0-2.3,0-6.35,0-13.5"
   id="path1192" />
	<line
   class="st19"
   x1="1023.72"
   y1="780.73"
   x2="1322.03"
   y2="780.73"
   id="line1194" />
	<path
   class="st14"
   d="M968.85,798.73L968.85,798.73 M1020.76,798.73L1020.76,798.73 M1020.76,780.73L1020.76,780.73    M1323.51,780.73L1323.51,780.73"
   id="path1196" />
	<path
   class="st2"
   d="M968.85,801.51c1.53,0,2.78-1.24,2.78-2.78c0-1.54-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C966.07,800.27,967.32,801.51,968.85,801.51L968.85,801.51z"
   id="path1198" />
	<line
   class="st20"
   x1="990.64"
   y1="693.73"
   x2="1026.81"
   y2="693.73"
   id="line1200" />
	<line
   class="st21"
   x1="1028.26"
   y1="696.59"
   x2="1028.26"
   y2="712.3"
   id="line1202" />
	<line
   class="st22"
   x1="1031.25"
   y1="713.73"
   x2="1322.51"
   y2="713.73"
   id="line1204" />
	<path
   class="st14"
   d="M987.74,693.73L987.74,693.73 M1028.26,693.73L1028.26,693.73 M1028.26,713.73L1028.26,713.73 M1324,713.73   L1324,713.73"
   id="path1206" />
	<path
   class="st2"
   d="M987.74,696.51c1.54,0,2.78-1.24,2.78-2.78c0-1.54-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C984.96,695.27,986.21,696.51,987.74,696.51L987.74,696.51z"
   id="path1208" />
	<line
   class="st23"
   x1="815.76"
   y1="423.32"
   x2="883.72"
   y2="423.32"
   id="line1210" />
	<line
   class="st24"
   x1="885.23"
   y1="426.12"
   x2="885.23"
   y2="444.33"
   id="line1212" />
	<line
   class="st25"
   x1="888.21"
   y1="445.73"
   x2="1322.02"
   y2="445.73"
   id="line1214" />
	<path
   class="st7"
   d="M812.73,423.32L812.73,423.32 M885.23,423.32L885.23,423.32 M885.23,445.73L885.23,445.73 M1323.51,445.73   L1323.51,445.73"
   id="path1216" />
	<path
   class="st0"
   d="M812.73,426.1c1.53,0,2.78-1.24,2.78-2.78s-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   S811.2,426.1,812.73,426.1L812.73,426.1z"
   id="path1218" />
	<line
   class="st26"
   x1="888.36"
   y1="471.73"
   x2="965.59"
   y2="471.73"
   id="line1220" />
	<line
   class="st27"
   x1="967.11"
   y1="474.66"
   x2="967.11"
   y2="511.27"
   id="line1222" />
	<line
   class="st28"
   x1="970.08"
   y1="512.73"
   x2="1322.52"
   y2="512.73"
   id="line1224" />
	<path
   class="st29"
   d="M885.33,471.73L885.33,471.73 M967.11,471.73L967.11,471.73 M967.11,512.73L967.11,512.73 M1324,512.73   L1324,512.73"
   id="path1226" />
	<path
   class="st3"
   d="M885.33,474.51c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C882.55,473.27,883.8,474.51,885.33,474.51L885.33,474.51z"
   id="path1228" />
	<line
   class="st30"
   x1="942.83"
   y1="538.8"
   x2="997.04"
   y2="538.8"
   id="line1230" />
	<line
   class="st27"
   x1="998.51"
   y1="541.73"
   x2="998.51"
   y2="578.34"
   id="line1232" />
	<line
   class="st31"
   x1="1001.47"
   y1="579.8"
   x2="1323.02"
   y2="579.8"
   id="line1234" />
	<path
   class="st29"
   d="M939.9,538.8L939.9,538.8 M998.51,538.8L998.51,538.8 M998.51,579.8L998.51,579.8 M1324.5,579.8L1324.5,579.8   "
   id="path1236" />
	<path
   class="st3"
   d="M939.9,541.58c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C937.12,540.33,938.36,541.58,939.9,541.58L939.9,541.58z"
   id="path1238" />
	<line
   class="st32"
   x1="812.77"
   y1="982.53"
   x2="812.77"
   y2="1014.22"
   id="line1240" />
	<line
   class="st33"
   x1="815.72"
   y1="1015.73"
   x2="893.95"
   y2="1015.73"
   id="line1242" />
	<line
   class="st34"
   x1="895.42"
   y1="1012.86"
   x2="895.42"
   y2="982.67"
   id="line1244" />
	<line
   class="st35"
   x1="898.4"
   y1="981.24"
   x2="1322.02"
   y2="981.24"
   id="line1246" />
	<path
   class="st10"
   d="M812.77,979.51L812.77,979.51 M812.77,1015.73L812.77,1015.73 M895.42,1015.73L895.42,1015.73 M895.42,981.24   L895.42,981.24 M1323.51,981.24L1323.51,981.24"
   id="path1248" />
	<path
   class="st4"
   d="M812.77,976.73c1.53,0,2.78,1.25,2.78,2.78c0,1.54-1.24,2.78-2.78,2.78c-1.53,0-2.78-1.24-2.78-2.78   C809.99,977.98,811.24,976.73,812.77,976.73L812.77,976.73z"
   id="path1250" />
	<line
   class="st5"
   x1="631.14"
   y1="393.17"
   x2="631.14"
   y2="380.62"
   id="line1252" />
	<line
   class="st6"
   x1="628.16"
   y1="379.23"
   x2="33.2"
   y2="379.23"
   id="line1254" />
	<path
   class="st7"
   d="M631.14,395.96L631.14,395.96 M631.14,379.23L631.14,379.23 M31.71,379.23L31.71,379.23"
   id="path1256" />
	<path
   class="st0"
   d="M631.14,398.73c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78s2.78,1.24,2.78,2.78   C633.91,397.49,632.67,398.73,631.14,398.73L631.14,398.73z"
   id="path1258" />
	<line
   class="st8"
   x1="633.9"
   y1="1008.47"
   x2="633.9"
   y2="1046.71"
   id="line1260" />
	<line
   class="st9"
   x1="630.92"
   y1="1048.24"
   x2="33.2"
   y2="1048.24"
   id="line1262" />
	<path
   class="st10"
   d="M633.9,1005.41L633.9,1005.41 M633.9,1048.24L633.9,1048.24 M31.71,1048.24L31.71,1048.24"
   id="path1264" />
	<path
   class="st4"
   d="M633.9,1002.63c-1.53,0-2.78,1.24-2.78,2.78c0,1.53,1.24,2.78,2.78,2.78c1.53,0,2.78-1.25,2.78-2.78   C636.68,1003.87,635.43,1002.63,633.9,1002.63L633.9,1002.63z"
   id="path1266" />
	<path
   class="st36"
   d="M470.87,934.73c-9.93,0-42.26,0-61.35,0"
   id="path1268" />
	<line
   class="st37"
   x1="408.03"
   y1="931.95"
   x2="408.03"
   y2="916.62"
   id="line1270" />
	<line
   class="st38"
   x1="405.04"
   y1="915.23"
   x2="33.2"
   y2="915.23"
   id="line1272" />
	<path
   class="st39"
   d="M473.87,934.73L473.87,934.73 M408.03,934.73L408.03,934.73 M408.03,915.23L408.03,915.23 M31.71,915.23   L31.71,915.23"
   id="path1274" />
	<path
   class="st1"
   d="M473.87,937.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C476.64,936.27,475.4,937.51,473.87,937.51L473.87,937.51z"
   id="path1276" />
	<line
   class="st40"
   x1="415.21"
   y1="867.73"
   x2="348.11"
   y2="867.73"
   id="line1278" />
	<line
   class="st37"
   x1="346.62"
   y1="864.95"
   x2="346.62"
   y2="849.62"
   id="line1280" />
	<line
   class="st41"
   x1="343.65"
   y1="848.23"
   x2="33.2"
   y2="848.23"
   id="line1282" />
	<path
   class="st39"
   d="M418.19,867.73L418.19,867.73 M346.62,867.73L346.62,867.73 M346.62,848.23L346.62,848.23 M31.71,848.23   L31.71,848.23"
   id="path1284" />
	<path
   class="st1"
   d="M418.19,870.51c-1.54,0-2.78-1.24-2.78-2.78s1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   S419.72,870.51,418.19,870.51L418.19,870.51z"
   id="path1286" />
	<line
   class="st42"
   x1="383.32"
   y1="798.73"
   x2="335.99"
   y2="798.73"
   id="line1288" />
	<path
   class="st43"
   d="M334.47,795.73c0-2.3,0-6.35,0-13.5"
   id="path1290" />
	<line
   class="st44"
   x1="331.5"
   y1="780.73"
   x2="33.2"
   y2="780.73"
   id="line1292" />
	<path
   class="st39"
   d="M386.37,798.73L386.37,798.73 M334.47,798.73L334.47,798.73 M334.47,780.73L334.47,780.73 M31.71,780.73   L31.71,780.73"
   id="path1294" />
	<path
   class="st1"
   d="M386.37,801.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.54,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C389.15,800.27,387.91,801.51,386.37,801.51L386.37,801.51z"
   id="path1296" />
	<line
   class="st45"
   x1="364.59"
   y1="693.73"
   x2="328.41"
   y2="693.73"
   id="line1298" />
	<line
   class="st46"
   x1="326.96"
   y1="696.59"
   x2="326.96"
   y2="712.3"
   id="line1300" />
	<line
   class="st47"
   x1="323.97"
   y1="713.73"
   x2="32.71"
   y2="713.73"
   id="line1302" />
	<path
   class="st39"
   d="M367.48,693.73L367.48,693.73 M326.96,693.73L326.96,693.73 M326.96,713.73L326.96,713.73 M31.22,713.73   L31.22,713.73"
   id="path1304" />
	<path
   class="st1"
   d="M367.48,696.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.54,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C370.26,695.27,369.02,696.51,367.48,696.51L367.48,696.51z"
   id="path1306" />
	<line
   class="st23"
   x1="539.47"
   y1="423.32"
   x2="471.5"
   y2="423.32"
   id="line1308" />
	<line
   class="st24"
   x1="469.99"
   y1="426.12"
   x2="469.99"
   y2="444.33"
   id="line1310" />
	<line
   class="st25"
   x1="467.01"
   y1="445.73"
   x2="33.2"
   y2="445.73"
   id="line1312" />
	<path
   class="st7"
   d="M542.49,423.32L542.49,423.32 M469.99,423.32L469.99,423.32 M469.99,445.73L469.99,445.73 M31.71,445.73   L31.71,445.73"
   id="path1314" />
	<path
   class="st0"
   d="M542.49,426.1c-1.53,0-2.78-1.24-2.78-2.78s1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   S544.02,426.1,542.49,426.1L542.49,426.1z"
   id="path1316" />
	<line
   class="st48"
   x1="466.86"
   y1="471.73"
   x2="389.63"
   y2="471.73"
   id="line1318" />
	<line
   class="st49"
   x1="388.11"
   y1="474.66"
   x2="388.11"
   y2="511.27"
   id="line1320" />
	<line
   class="st50"
   x1="385.14"
   y1="512.73"
   x2="32.71"
   y2="512.73"
   id="line1322" />
	<path
   class="st7"
   d="M469.89,471.73L469.89,471.73 M388.11,471.73L388.11,471.73 M388.11,512.73L388.11,512.73 M31.22,512.73   L31.22,512.73"
   id="path1324" />
	<path
   class="st0"
   d="M469.89,474.51c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C472.67,473.27,471.42,474.51,469.89,474.51L469.89,474.51z"
   id="path1326" />
	<line
   class="st51"
   x1="409.57"
   y1="538.24"
   x2="343.21"
   y2="538.24"
   id="line1328" />
	<line
   class="st49"
   x1="341.73"
   y1="541.17"
   x2="341.73"
   y2="577.77"
   id="line1330" />
	<line
   class="st52"
   x1="338.75"
   y1="579.24"
   x2="32.71"
   y2="579.24"
   id="line1332" />
	<path
   class="st7"
   d="M412.52,538.24L412.52,538.24 M341.73,538.24L341.73,538.24 M341.73,579.24L341.73,579.24 M31.22,579.24   L31.22,579.24"
   id="path1334" />
	<path
   class="st0"
   d="M412.52,541.02c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C415.3,539.77,414.05,541.02,412.52,541.02L412.52,541.02z"
   id="path1336" />
	<line
   class="st53"
   x1="376.4"
   y1="605.24"
   x2="316.36"
   y2="605.24"
   id="line1338" />
	<line
   class="st53"
   x1="314.9"
   y1="608.17"
   x2="314.9"
   y2="644.77"
   id="line1340" />
	<line
   class="st54"
   x1="311.91"
   y1="646.24"
   x2="32.71"
   y2="646.24"
   id="line1342" />
	<path
   class="st39"
   d="M379.33,605.24L379.33,605.24 M314.9,605.24L314.9,605.24 M314.9,646.24L314.9,646.24 M31.22,646.24   L31.22,646.24"
   id="path1344" />
	<path
   class="st1"
   d="M379.33,608.02c-1.53,0-2.78-1.24-2.78-2.78c0-1.53,1.24-2.78,2.78-2.78c1.53,0,2.78,1.24,2.78,2.78   C382.1,606.77,380.86,608.02,379.33,608.02L379.33,608.02z"
   id="path1346" />
	<line
   class="st32"
   x1="542.45"
   y1="982.53"
   x2="542.45"
   y2="1014.22"
   id="line1348" />
	<line
   class="st33"
   x1="539.5"
   y1="1015.73"
   x2="461.27"
   y2="1015.73"
   id="line1350" />
	<line
   class="st34"
   x1="459.8"
   y1="1012.86"
   x2="459.8"
   y2="982.67"
   id="line1352" />
	<line
   class="st35"
   x1="456.82"
   y1="981.24"
   x2="33.2"
   y2="981.24"
   id="line1354" />
	<path
   class="st10"
   d="M542.45,979.51L542.45,979.51 M542.45,1015.73L542.45,1015.73 M459.8,1015.73L459.8,1015.73 M459.8,981.24   L459.8,981.24 M31.71,981.24L31.71,981.24"
   id="path1356" />
	<path
   class="st4"
   d="M542.45,976.73c-1.53,0-2.78,1.25-2.78,2.78c0,1.54,1.24,2.78,2.78,2.78c1.53,0,2.78-1.24,2.78-2.78   C545.23,977.98,543.98,976.73,542.45,976.73L542.45,976.73z"
   id="path1358" />
	
	
	
	
	
	
	<a
   id="a14345"
   xlink:href="/child-protection#violence"
   target="blank"
   xlink:title="Violence against Children and Women"
   xlink:show="Violence against Children and Women"><path
     class="st1"
     d="M458.88,648.9c1.83-7.73,4.05-15.3,6.65-22.69c2.29-6.52-0.74-13.7-7.02-16.57L413.32,589   c-7.02-3.21-15.35,0.18-18.03,7.43c-4.72,12.78-8.6,25.96-11.57,39.48c-1.66,7.54,3.51,14.9,11.15,16l49.09,7.06   C450.78,659.95,457.3,655.61,458.88,648.9L458.88,648.9z"
     id="path8" /><path
     class="st55"
     d="M437.9,627.88h-0.65c-0.8,0-1.46,0.65-1.46,1.46v7.1l-3.29-3.7c-0.31-0.35-0.77-0.53-1.25-0.48   c-0.47,0.05-0.89,0.33-1.12,0.74l-3.64,6.56c-0.39,0.7-0.14,1.59,0.57,1.98c0.22,0.12,0.47,0.18,0.71,0.18   c0.51,0,1.01-0.27,1.28-0.75l2.65-4.77l4.47,5.02c0.01,0.01,0.02,0.02,0.03,0.03c0.03,0.04,0.07,0.07,0.11,0.1   c0.04,0.03,0.07,0.06,0.11,0.09c0.04,0.03,0.08,0.05,0.12,0.07c0.04,0.02,0.08,0.05,0.12,0.07c0.04,0.02,0.09,0.03,0.13,0.05   c0.05,0.01,0.09,0.03,0.14,0.04c0.04,0.01,0.09,0.02,0.13,0.02c0.05,0.01,0.1,0.01,0.15,0.01c0.01,0,0.03,0.01,0.04,0.01h3.65   c0.81,0,1.46-0.65,1.46-1.46v-7.95C442.35,629.87,440.36,627.88,437.9,627.88L437.9,627.88z"
     id="path1360" /><path
     class="st55"
     d="M433.24,622.78c-1.41,0-2.55,1.14-2.55,2.55c0,1.41,1.14,2.55,2.55,2.55s2.55-1.14,2.55-2.55   C435.79,623.92,434.65,622.78,433.24,622.78L433.24,622.78z"
     id="path1362" /><path
     class="st55"
     d="M416.83,614.03c-5.49,0-9.48,3.68-9.48,8.75c0,0.8,0.65,1.46,1.46,1.46c0.81,0,1.46-0.65,1.46-1.46   c0-2.2,1.11-3.97,2.92-4.96v10.14c0,0.02,0.01,0.04,0.01,0.06c0,0.02-0.01,0.04-0.01,0.06v12.2c0,0.81,0.65,1.46,1.46,1.46   c0.81,0,1.46-0.65,1.46-1.46v-10.94h1.46v10.94c0,0.81,0.65,1.46,1.46,1.46s1.46-0.65,1.46-1.46v-12.2c0-0.02,0-0.04-0.01-0.06   c0-0.02,0.01-0.04,0.01-0.06v-10.14c1.81,0.99,2.92,2.76,2.92,4.96c0,0.8,0.65,1.46,1.46,1.46c0.81,0,1.46-0.65,1.46-1.46   C426.31,617.71,422.33,614.03,416.83,614.03L416.83,614.03z"
     id="path1364" /><path
     class="st55"
     d="M421.21,613.3c1.61,0,2.92-1.31,2.92-2.92c0-1.61-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92   C418.29,611.99,419.6,613.3,421.21,613.3L421.21,613.3z"
     id="path1366" /><path
     class="st55"
     d="M431.42,612.93c0,0.6,0.49,1.09,1.09,1.09h2.92c0.6,0,1.09-0.49,1.09-1.09c0-0.6-0.49-1.09-1.09-1.09h-2.92   C431.91,611.84,431.42,612.33,431.42,612.93L431.42,612.93z"
     id="path1368" /><path
     class="st55"
     d="M429.11,611.72c0.16,0.08,0.32,0.12,0.49,0.12c0.4,0,0.79-0.22,0.98-0.6l1.46-2.92   c0.27-0.54,0.05-1.2-0.49-1.47c-0.54-0.27-1.2-0.05-1.47,0.49l-1.46,2.92C428.35,610.79,428.56,611.45,429.11,611.72L429.11,611.72   z"
     id="path1370" /><path
     class="st55"
     d="M430.07,618.53c0.19,0.38,0.58,0.6,0.98,0.6c0.17,0,0.33-0.04,0.49-0.12c0.54-0.27,0.76-0.93,0.49-1.47   l-1.46-2.92c-0.27-0.54-0.93-0.76-1.47-0.49c-0.54,0.27-0.76,0.93-0.49,1.47L430.07,618.53L430.07,618.53z"
     id="path1372" /></a>
	<a
   id="a60298"
   xlink:show="Water, sanitation and hygiene"
   xlink:title="Water, sanitation and hygiene"
   target="blank"
   xlink:href="/child-health#wash"><path
     class="st3"
     d="M941.68,589l-45.19,20.64c-6.28,2.87-9.32,10.05-7.03,16.57c2.6,7.39,4.83,14.96,6.65,22.69   c1.58,6.71,8.1,11.04,14.92,10.06l49.1-7.06c7.64-1.1,12.81-8.45,11.15-16c-2.97-13.53-6.85-26.71-11.57-39.48   C957.03,589.18,948.7,585.79,941.68,589L941.68,589z"
     id="path22" /><path
     class="st55"
     d="M938.33,626.21c2.03,1.03,2.09-4.37,2.09-4.37C939.95,622.12,936.3,625.18,938.33,626.21 M938.13,628.8   c1.91,0.97,4.45-2.79,4.45-3.36c0,0-0.52,1.38-2.77,1.27C937.28,626.58,937.28,628.36,938.13,628.8 M936.73,631.54   c1.91,0.98,4.45-2.78,4.45-3.36c0,0-0.52,1.38-2.77,1.27C935.88,629.33,935.88,631.11,936.73,631.54 M935.28,634.38   c1.91,0.97,4.45-2.79,4.45-3.36c0,0-0.52,1.37-2.77,1.27C934.43,632.16,934.43,633.94,935.28,634.38 M936.79,625.16   c-1.41-1.76-0.6-2.98-0.6-2.98c-0.46,0.34-2.02,4.6-0.11,5.58C936.93,628.18,938.37,627.14,936.79,625.16 M935.39,627.91   c-1.41-1.76-0.59-2.99-0.59-2.99c-0.47,0.34-2.02,4.6-0.11,5.58C935.53,630.94,936.97,629.89,935.39,627.91 M933.94,630.74   c-1.41-1.76-0.6-2.98-0.6-2.98c-0.47,0.34-2.02,4.6-0.11,5.57C934.09,633.77,935.53,632.72,933.94,630.74 M933.17,637.05l1.46-2.35   c0.12-0.23-0.29-0.18-0.66-0.37c-0.37-0.19-0.56-0.55-0.68-0.32l-1.03,2.64C932.14,636.91,932.9,637.59,933.17,637.05    M941.41,631.65c-0.23,0.36-0.47,0.69-0.71,1.02c1.28,0.54,2.08,1.22,2.08,1.97c0,1.73-4.11,3.14-9.17,3.14   c-5.06,0-9.17-1.41-9.17-3.14c0-1.49,3.02-2.72,7.07-3.05c0-0.35,0.01-0.7,0.04-1.07c-5.16,0.24-9.09,1.56-9.09,5.63   c0,4.57,4.95,9.57,11.04,9.57c6.1,0,11.04-5,11.04-9.57C944.55,633.91,943.34,632.51,941.41,631.65 M925.3,625.51v2.15   c-0.22-0.09-0.42-0.23-0.6-0.43c-0.18-0.2-0.3-0.44-0.36-0.71l-1.59,0.14c0.12,0.67,0.4,1.19,0.84,1.56c0.43,0.37,1,0.59,1.71,0.66   v0.93h0.88v-0.96c0.79-0.1,1.41-0.36,1.85-0.78c0.45-0.42,0.67-0.95,0.67-1.56c0-0.55-0.18-1.01-0.53-1.36   c-0.35-0.36-1.01-0.64-1.98-0.87v-2c0.39,0.14,0.63,0.42,0.73,0.82l1.54-0.17c-0.1-0.51-0.35-0.92-0.73-1.23   c-0.38-0.31-0.9-0.49-1.54-0.55v-0.51h-0.88v0.51c-0.7,0.06-1.26,0.28-1.67,0.66c-0.42,0.38-0.63,0.85-0.63,1.41   c0,0.56,0.18,1.02,0.56,1.42C923.92,625.03,924.5,625.32,925.3,625.51 M922.33,632.42h-2.78c-2.84,0-3.46-2.37-3.46-2.37   c-1.87-8.22,3.8-12.68,3.8-12.68h11.8c0,0,2.24,1.76,3.43,5.11c-0.79,0.91-1.51,1.99-2.12,3.22c-0.57,1.16-0.97,2.33-1.22,3.44   C928.91,629.24,924.47,629.75,922.33,632.42 M930.01,610.76c-2.28-0.25-3.08,1.15-4.22,1.21c-1.15-0.06-1.94-1.46-4.23-1.21   c-2.33,0.26-3.75,2.25-3.75,2.25l2.85,2.65h10.26l2.85-2.65C933.76,613.01,932.35,611.02,930.01,610.76 M924.51,623.4   c0,0.18,0.07,0.35,0.19,0.5c0.13,0.16,0.33,0.28,0.59,0.38v-1.77c-0.24,0.07-0.43,0.18-0.57,0.35   C924.58,623.03,924.51,623.2,924.51,623.4 M926.97,626.35c0.16,0.17,0.24,0.36,0.24,0.59c0,0.25-0.09,0.48-0.28,0.67   c-0.19,0.19-0.43,0.31-0.74,0.35v-2C926.54,626.05,926.81,626.18,926.97,626.35"
     id="path1374" /></a>
	<a
   id="a3281"
   xlink:href="/child-health#hs"
   target="blank"
   xlink:title="Health System"
   xlink:show="Health System"><path
     class="st0"
     d="M420.09,574.26l45.16,20.63c6.24,2.85,13.67,0.54,17.07-5.42c3.93-6.88,8.21-13.53,12.82-19.93   c4.04-5.61,3.15-13.36-2.07-17.88l-37.52-32.51c-5.83-5.06-14.77-4.15-19.39,2.04c-8.17,10.97-15.62,22.52-22.26,34.57   C410.17,562.53,413.05,571.05,420.09,574.26L420.09,574.26z"
     id="path10" /><path
     class="st55"
     d="M459.13,544.52c-0.98-0.8-1.66-0.61-2.64,1.14c-0.65,1.16-1.68,1.3-2.31,1.26l0-0.23   c0.73-0.36,1.25-1.1,1.25-1.97c0-1.23-0.99-2.22-2.22-2.22s-2.22,0.99-2.22,2.22c0,0.87,0.52,1.61,1.25,1.97l0,0.23   c-0.63,0.04-1.66-0.1-2.31-1.26c-0.98-1.75-1.66-1.94-2.63-1.14c-0.98,0.8-4.86,5.43-9.58,5.01c0,0,0.94,2.13,3.49,1.65   c0,0,1.37,1.42,3.58,0.42c0,0,1.15,1.04,2.98,0.09c0,0,1.36,1.04,2.81,0.14c0,0,0.82,0.59,1.73,0.44l0.06,5.35   c-0.1-0.02-0.19-0.04-0.29-0.06c0,0-1.59-0.34-3.26-0.81c-1.61-0.42-3.38-1.11-3.64-1.46c0.02-0.02,0.06-0.04,0.11-0.06   c0.14-0.07,0.39-0.15,0.68-0.21c0.59-0.12,1.39-0.18,2.2-0.21c1.6-0.06,1.89,0.01,1.92,0.02c0-0.05,0.93,0.11,1.18-0.83   c-0.01-0.01,0.02-0.05,0-0.07c-0.05-0.65-0.55-0.68-0.96-0.76c-0.66-0.09-0.32-0.05-1.21-0.04c-1.47,0.11-5.98-0.26-6.55,2.12   c0,0.07-0.01,0.11-0.01,0.17c0.19,2.07,4.47,2.97,7.58,3.59c-1.05,0.72-1.62,1.66-1.84,2.87c-0.11,1.29,0.92,2.53,3.31,3.9   c-1.81,1.28-3,2.49-2.91,3.94c0.17,1.19,1.22,2.77,3.27,3.77c0.01,0,0.01,0,0.01,0l0,0c0,0,0,0,0.01,0c0,0-1.44-2.2-1.54-3.4   c-0.1-0.7,0.3-1.74,2.06-2.99l0.05,4.39h0.01c0.01,0.37,0.3,0.67,0.66,0.67c0.36,0,0.65-0.3,0.66-0.67h0.01l0.06-4.28   c1.61,1.2,1.98,2.19,1.89,2.87c-0.1,1.2-1.53,3.4-1.53,3.4c0,0,0,0,0,0c0,0,0.01,0,0.02,0c2.06-1,3.11-2.59,3.27-3.77   c0.1-1.46-1.09-2.66-2.9-3.94c2.38-1.38,3.41-2.61,3.31-3.9c-0.22-1.21-0.79-2.15-1.84-2.87c3.11-0.62,7.39-1.52,7.58-3.59   c-0.01-0.06-0.01-0.1-0.01-0.17c-0.57-2.38-5.08-2.01-6.55-2.12c-0.89-0.01-0.55-0.05-1.21,0.04c-0.41,0.08-0.91,0.11-0.96,0.76   c-0.02,0.02,0.01,0.06,0,0.07c0.25,0.94,1.18,0.78,1.18,0.83c0.03-0.01,0.31-0.08,1.92-0.02c0.8,0.03,1.6,0.09,2.2,0.21   c0.29,0.06,0.53,0.14,0.68,0.21c0.05,0.02,0.08,0.04,0.11,0.06c-0.26,0.36-2.03,1.04-3.64,1.46c-1.67,0.47-3.26,0.81-3.26,0.81   c-0.04,0.01-0.07,0.02-0.11,0.02l0.07-5.31c0.92,0.16,1.74-0.44,1.74-0.44c1.45,0.9,2.81-0.14,2.81-0.14   c1.83,0.94,2.98-0.09,2.98-0.09c2.21,0.99,3.58-0.42,3.58-0.42c2.55,0.47,3.49-1.65,3.49-1.65   C463.99,549.95,460.11,545.32,459.13,544.52L459.13,544.52z M450.32,562.28c0.03-0.47-0.13-1.58,2.08-2.39l0.05,4.41   c-0.43-0.27-0.87-0.55-1.31-0.83C450.54,563.11,450.26,562.62,450.32,562.28L450.32,562.28z M455.1,563.48   c-0.39,0.25-0.77,0.48-1.14,0.72l0.06-4.24c2.01,0.8,1.86,1.87,1.89,2.32C455.97,562.62,455.69,563.11,455.1,563.48L455.1,563.48z"
     id="path1376" /></a>
	
	<a
   id="a11205"
   xlink:href="/child-health#mnch"
   target="blank"
   xlink:title="Maternal, newborn and child health"
   xlink:show="Maternal, newborn and child health"><path
     class="st0"
     d="M521.69,538.91c5.66-5.45,11.61-10.61,17.82-15.45c5.44-4.24,6.77-11.92,3.03-17.73l-26.84-41.76   c-4.18-6.5-13.02-8.15-19.2-3.49c-10.96,8.27-21.33,17.27-31.05,26.93c-5.48,5.45-5.11,14.43,0.73,19.49l37.51,32.5   C508.92,543.93,516.72,543.7,521.69,538.91L521.69,538.91z"
     id="path28" /><path
     class="st55"
     d="M510.37,488.07c0,2.94-2.39,5.33-5.33,5.33c-2.94,0-5.33-2.39-5.33-5.33c0-2.94,2.39-5.33,5.33-5.33   C507.99,482.74,510.37,485.12,510.37,488.07L510.37,488.07z"
     id="path1378" /><path
     class="st55"
     d="M517.17,503.44c0,0-2.03-4.06-3.35-6.19c-1.32-2.13-3.15-2.23-3.15-2.23h-10.15   c-2.94,0.51-4.87,3.65-7.51,10.76c-2.64,7.1,5.48,9.74,9.23,9.95c3.75,0.2,5.08-1.52,4.87-3.25c-0.2-1.73-2.34-1.73-3.15-1.62   c-0.81,0.1-4.36-0.41-5.68-1.12c-1.32-0.71-0.91-1.02,0.61-1.02c1.52,0,2.44-0.81,2.44-0.81c0.81-0.2-0.51-1.62-0.71-2.64   c-0.2-1.02-0.41-2.03,0.91-2.33c1.32-0.3,1.12,0.41,3.35,3.25c2.23,2.84,4.97,2.23,4.97,2.23s-2.84,1.62-1.32,3.76   c1.52,2.13,6.29,0,8.22-3.45C518.69,505.27,517.17,503.44,517.17,503.44L517.17,503.44z M509.21,507.6c-1.99,0-3.6-1.61-3.6-3.6   c0-1.99,1.61-3.6,3.6-3.6c1.99,0,3.6,1.61,3.6,3.6C512.81,505.99,511.19,507.6,509.21,507.6L509.21,507.6z"
     id="path1380" /></a>
	
	
	<a
   id="a8092"
   xlink:href="/child-health#immunization"
   target="blank"
   xlink:title="Immunization"
   xlink:show="Immunization"><path
     class="st0"
     d="M573.57,501.52c6.97-3.65,14.16-6.94,21.54-9.85c6.39-2.52,9.74-9.56,7.81-16.15l-13.98-47.6   c-2.18-7.42-10.2-11.48-17.43-8.76c-12.92,4.86-25.41,10.59-37.41,17.11c-6.78,3.68-8.95,12.4-4.78,18.9l26.84,41.76   C559.9,502.74,567.45,504.72,573.57,501.52L573.57,501.52z"
     id="path6" /><path
     class="st55"
     d="M584.81,449.61h-13.75c-0.38,0-0.69,0.31-0.69,0.69v3.44c0,0.38,0.31,0.69,0.69,0.69h13.75   c0.38,0,0.69-0.31,0.69-0.69v-3.44C585.5,449.92,585.19,449.61,584.81,449.61L584.81,449.61z"
     id="path1382" /><path
     class="st55"
     d="M571.75,475.05c0,0.38,0.31,0.69,0.69,0.69h11c0.38,0,0.69-0.31,0.69-0.69V455.8h-12.38V475.05L571.75,475.05   z M573.81,459.92c0-0.38,0.31-0.69,0.69-0.69h6.88c0.38,0,0.69,0.31,0.69,0.69v4.81c0,0.38-0.31,0.69-0.69,0.69h-6.88   c-0.38,0-0.69-0.31-0.69-0.69V459.92L573.81,459.92z M574.5,467.48h6.88c0.38,0,0.69,0.31,0.69,0.69c0,0.38-0.31,0.69-0.69,0.69   h-6.88c-0.38,0-0.69-0.31-0.69-0.69C573.81,467.79,574.12,467.48,574.5,467.48L574.5,467.48z"
     id="path1384" /><path
     class="st55"
     d="M565.91,448.23h-3.78v-3.44h1.72c0.57,0,1.03-0.46,1.03-1.03c0-0.57-0.46-1.03-1.03-1.03h-8.25   c-0.57,0-1.03,0.46-1.03,1.03c0,0.57,0.46,1.03,1.03,1.03h1.72v3.44h-3.78c-0.57,0-1.03,0.46-1.03,1.03c0,0.57,0.46,1.03,1.03,1.03   h2.41v15.81c0,0.76,0.62,1.38,1.38,1.38v1.38c0,0.38,0.31,0.69,0.69,0.69h0.69v5.16c0,0.57,0.46,1.03,1.03,1.03   c0.57,0,1.03-0.46,1.03-1.03v-5.16h0.69c0.38,0,0.69-0.31,0.69-0.69v-1.38c0.76,0,1.38-0.62,1.38-1.38V450.3h2.41   c0.57,0,1.03-0.46,1.03-1.03C566.94,448.69,566.48,448.23,565.91,448.23L565.91,448.23z M561.44,460.61H558v-8.94h3.44V460.61   L561.44,460.61z"
     id="path1386" /></a>
	
	<a
   id="a6477"
   xlink:href="/child-health#nutrition"
   target="blank"
   xlink:title="Nutrition"
   xlink:show="Nutrition"><path
     class="st0"
     d="M633.88,480.31c7.66-1.51,15.46-2.62,23.38-3.33c6.89-0.61,12.13-6.46,12.13-13.38v-49.51   c0-7.72-6.54-13.88-14.25-13.32c-13.85,1.02-27.44,2.98-40.71,5.81c-7.56,1.61-12.1,9.37-9.93,16.79l13.98,47.63   C620.44,477.61,627.11,481.64,633.88,480.31L633.88,480.31z"
     id="path4" /><path
     class="st55"
     d="M642.1,451.27c2.82,0,4.53-1.85,4.65-4.43c0.01-0.12-0.11-0.22-0.23-0.22h-15.56h-6.29   c-0.73,0-1.16,0.49-1.16,1.16c0,0.68,0.43,1.16,1.16,1.16h7.47h6.09C639.13,450.4,640.16,451.27,642.1,451.27"
     id="path1388" /><path
     class="st55"
     d="M650.85,439.27c-0.76,0.74-1.77,1.15-2.84,1.15c-1.07,0-2.08-0.4-2.84-1.15c-0.35-0.34-0.35-0.91,0-1.25   c0.36-0.35,0.93-0.35,1.29,0c0.83,0.81,2.27,0.81,3.1,0c0.36-0.35,0.93-0.35,1.29,0C651.2,438.37,651.2,438.93,650.85,439.27    M640,439.27c-0.76,0.74-1.77,1.15-2.84,1.15c-1.07,0-2.08-0.4-2.84-1.15c-0.35-0.34-0.35-0.91,0-1.25c0.36-0.35,0.93-0.35,1.29,0   c0.83,0.81,2.27,0.81,3.1,0c0.36-0.35,0.93-0.35,1.29,0C640.34,438.37,640.34,438.93,640,439.27 M655.63,437.38   c-0.39-0.39-0.88-0.69-1.42-0.83V435c0-2.99-1.3-5.7-3.41-7.67c-2.08-1.94-4.94-3.15-8.11-3.18c-0.54,0.39-0.88,1.02-0.88,1.73   c0,1.15,1.09,2.15,2.33,2.15c0.43,0,0.77,0.35,0.77,0.78c0,0.43-0.35,0.77-0.77,0.77c-2.1,0-3.88-1.69-3.88-3.7   c0-0.56,0.12-1.09,0.36-1.57c-5.49,0.87-9.66,5.33-9.66,10.7v1.55c-0.54,0.14-1.03,0.44-1.42,0.83c-0.56,0.58-0.91,1.39-0.91,2.27   s0.35,1.68,0.91,2.27c0.39,0.39,0.88,0.69,1.42,0.83v1.55c0,0.25,0.02,0.5,0.06,0.77H647c0.49,0,0.96,0.2,1.3,0.56   c0.33,0.34,0.5,0.81,0.48,1.28c-0.17,3.53-2.66,5.91-6.2,5.91c-2.42,0-3.79-1.13-4.69-2.33h-4.13c2.12,2.54,5.29,4.65,8.82,4.65   c6.42,0,11.62-6.92,11.62-10.85v-1.55c0.54-0.14,1.03-0.44,1.42-0.83c0.56-0.59,0.91-1.39,0.91-2.27S656.19,437.96,655.63,437.38"
     id="path1390" /></a>
	<a
   id="a44365"
   xlink:href="/child-health#adolescents"
   target="blank"
   xlink:title="Adolescent physical, mental, and reproductive health"
   xlink:show="Adolescent physical, mental, and reproductive health"><path
     class="st0"
     d="M697.74,476.98c7.92,0.71,15.72,1.82,23.38,3.33c6.77,1.33,13.44-2.69,15.39-9.32l13.98-47.63   c2.18-7.41-2.37-15.18-9.93-16.79c-13.27-2.83-26.86-4.79-40.71-5.81c-7.7-0.57-14.25,5.59-14.25,13.32v49.51   C685.61,470.52,690.85,476.37,697.74,476.98L697.74,476.98z"
     id="path12" /><path
     class="st55"
     d="M731.44,425.6v-0.04c-3.74-3.76-9.83-3.78-13.59-0.03c-0.01,0.01-0.02,0.02-0.03,0.03l-1.43,1.42l-1.42-1.42   c-3.77-3.77-9.88-3.76-13.65,0.02c-3.76,3.77-3.76,9.88,0.02,13.65l14.19,14.14c0.46,0.48,1.22,0.49,1.7,0.03   c0.01-0.01,0.02-0.02,0.03-0.03l14.19-14.14C735.2,435.46,735.2,429.37,731.44,425.6L731.44,425.6z M720.06,439.46h-2.45v2.45   c0,0.67-0.55,1.22-1.22,1.22c-0.67,0-1.22-0.55-1.22-1.22v-2.45h-2.45c-0.67,0-1.22-0.55-1.22-1.22c0-0.67,0.55-1.22,1.22-1.22   h2.45v-2.45c0-0.67,0.55-1.22,1.22-1.22c0.67,0,1.22,0.55,1.22,1.22v2.45h2.45c0.67,0,1.22,0.55,1.22,1.22   C721.28,438.91,720.74,439.45,720.06,439.46L720.06,439.46z"
     id="path1392" /></a>
	<a
   id="a39622"
   xlink:title="Learning quality and skills"
   xlink:show="Learning quality and skills"
   target="blank"
   xlink:href="/child-education#quality"><path
     class="st4"
     d="M721.09,921.06c-7.65,1.5-15.45,2.62-23.35,3.32c-6.89,0.61-12.13,6.46-12.13,13.38v49.62   c0,7.73,6.54,13.88,14.25,13.32c13.85-1.02,27.44-2.98,40.71-5.81c7.56-1.61,12.1-9.37,9.93-16.79l-14.01-47.72   C734.53,923.75,727.86,919.73,721.09,921.06L721.09,921.06z"
     id="path42" /><path
     class="st55"
     d="M732.04,955.28L716,947.31l-16.04,7.97l-1.46-2.93l17.48-8.69l0.01-0.02l0.02,0.01l0.02-0.01l0.01,0.02   l17.48,8.69L732.04,955.28L732.04,955.28z M731.17,958.53c0,0.06,0,1.04,0,2.54v16.94H718.6c-0.43,0.36-1.45,0.62-2.64,0.62   c-1.19,0-2.21-0.26-2.64-0.62h-12.49v-16.94c0-1.5,0-2.49,0-2.54c8.24-3.55,14.27-0.06,15.32,0.94   C716.95,958.74,723.26,955.05,731.17,958.53L731.17,958.53z M715.03,962.62c0-2.52-3.35-3.88-7.5-3.88c-1.99,0-3.8,0.47-5.14,1.24   v16.52c6.77-4.26,12.63-0.36,12.63,0.31V962.62L715.03,962.62z M729.7,959.97c-1.34-0.77-3.14-1.24-5.13-1.24   c-4.14,0-7.49,1.36-7.49,3.88v14.18c0-0.67,5.86-4.57,12.63-0.31V959.97L729.7,959.97z"
     id="path1394" /></a>
	
	<a
   id="a17485"
   xlink:href="/child-protection#care"
   target="blank"
   xlink:title="Children without parental care"
   xlink:show="Children without parental care"><path
     class="st1"
     d="M452.88,700.68c0-3.98,0.1-7.93,0.31-11.85c0.36-6.85-4.64-12.82-11.43-13.8l-49.15-7.07   c-7.65-1.1-14.68,4.51-15.21,12.22c-0.46,6.79-0.69,13.64-0.69,20.55c0,6.91,0.23,13.76,0.69,20.55   c0.52,7.71,7.55,13.32,15.21,12.22l49.16-7.07c6.79-0.98,11.79-6.95,11.43-13.8C452.99,708.68,452.88,704.69,452.88,700.68   L452.88,700.68z"
     id="path16" /><path
     class="st55"
     d="M424.77,700.99v0.02c-0.12-0.01-0.24-0.02-0.37-0.02c-0.08,0-0.16,0.01-0.24,0.01   c-0.04,0-0.08-0.01-0.12-0.01h-9.15c-1.42,0-2.56,1.15-2.56,2.56c0,1.41,1.15,2.56,2.56,2.56h2.81h1.21c0.81,0,1.46,0.65,1.46,1.46   c0,0.81-0.65,1.46-1.46,1.46h-1.37h-3.75h-1.46c-0.39,0-0.9-0.17-1.17-0.44l-9.94-9.68c-1.21-1.21-3.22-1.14-4.34,0.21   c-0.97,1.18-0.8,2.94,0.28,4.02l11.14,10.88c0.55,0.55,1.3,0.86,2.07,0.86h13.66c0.06,0,0.11-0.01,0.17-0.02   c0.07,0,0.13,0.01,0.2,0.01c0.12,0,0.25-0.01,0.37-0.02v0.03c3.64,0,6.58-2.95,6.58-6.59v-0.73   C431.36,703.94,428.41,700.99,424.77,700.99L424.77,700.99z"
     id="path1396" /><path
     class="st55"
     d="M400.99,694.4c0.02,0,0.03,0,0.05,0c0.01,0,0.02,0,0.02,0h6.52c1.01,0,1.83-0.82,1.83-1.83   c0-1.01-0.82-1.83-1.83-1.83h-1.97c0,0,0-0.01,0-0.01h-0.96c-0.61,0-1.1-0.49-1.1-1.1c0-0.61,0.49-1.1,1.1-1.1h0.96h1.78h1.93   c0.27,0,0.63,0.12,0.82,0.31l6.78,7.15c0.84,0.84,2.24,0.79,3.02-0.15c0.68-0.82,0.55-2.04-0.2-2.8l-7.75-7.56   c-0.38-0.38-0.9-0.6-1.44-0.6h-9.5c-0.02,0-0.03,0.01-0.05,0.01c0,0,0,0,0,0c-2.63,0-4.75,2.13-4.75,4.75   C396.23,692.27,398.36,694.4,400.99,694.4L400.99,694.4z"
     id="path1398" /></a>
	
	
	
	
	
	<a
   id="a63619"><path
     class="st2"
     d="M934.91,827.2l-45.21-20.65c-6.23-2.85-13.66-0.54-17.06,5.41c-3.93,6.88-8.21,13.52-12.82,19.92   c-4.04,5.61-3.16,13.36,2.07,17.89l37.57,32.55c5.84,5.06,14.77,4.15,19.39-2.04c8.17-10.97,15.62-22.52,22.26-34.57   C944.83,838.94,941.95,830.42,934.91,827.2L934.91,827.2z"
     id="path44" /><path
     class="st55"
     d="M890.05,844.29c0.2-1.16,0.62-2.26,1.19-3.25c0.3-0.54,0.68-1.06,1.08-1.53c0.14-0.17,0.29-0.34,0.45-0.49   c-1.32-0.86-2.89-1.35-4.57-1.35c-4.65,0-8.43,3.78-8.43,8.44c0,3.11,1.7,5.84,4.21,7.29v1.15c0,0.93,0.76,1.69,1.69,1.69h5.06   c0.94,0,1.69-0.76,1.69-1.69v-1.14v-0.62c-0.46-0.51-0.84-1.05-1.17-1.62C890.06,849.15,889.61,846.73,890.05,844.29L890.05,844.29   z M882.28,846.11c0-1.62,0.65-3.08,1.7-4.15v8.3C882.93,849.19,882.28,847.73,882.28,846.11L882.28,846.11z"
     id="path1400" /><path
     class="st55"
     d="M888.2,835.98c1.86,0,3.38-1.51,3.38-3.38s-1.51-3.38-3.38-3.38c-1.86,0-3.38,1.51-3.38,3.38   S886.34,835.98,888.2,835.98L888.2,835.98z"
     id="path1402" /><path
     class="st55"
     d="M911.82,835.98c1.86,0,3.38-1.51,3.38-3.38s-1.51-3.38-3.38-3.38s-3.38,1.51-3.38,3.38   S909.96,835.98,911.82,835.98L911.82,835.98z"
     id="path1404" /><path
     class="st55"
     d="M911.82,837.67c-1.7,0-3.27,0.5-4.59,1.36c0.16,0.16,0.32,0.34,0.46,0.51c0.4,0.46,0.76,0.97,1.07,1.5   c0.86,1.49,1.36,3.22,1.36,5.06c0,1.8-0.49,3.53-1.36,5.05c-0.34,0.57-0.73,1.11-1.16,1.61v0.63v1.14c0,0.93,0.76,1.69,1.69,1.69   h5.06c0.93,0,1.69-0.76,1.69-1.69v-1.15c2.51-1.45,4.21-4.18,4.21-7.29C920.25,841.45,916.47,837.67,911.82,837.67L911.82,837.67z    M916.04,850.26v-8.3c1.05,1.07,1.7,2.53,1.7,4.15C917.74,847.73,917.09,849.19,916.04,850.26L916.04,850.26z"
     id="path1406" /><path
     class="st55"
     d="M900.01,835.98c1.86,0,3.38-1.51,3.38-3.38c0-1.87-1.51-3.38-3.38-3.38c-1.86,0-3.38,1.51-3.38,3.38   C896.64,834.47,898.15,835.98,900.01,835.98L900.01,835.98z"
     id="path1408" /><path
     class="st55"
     d="M908.44,846.11c0-1.31-0.3-2.55-0.84-3.65c-0.05-0.11-0.1-0.21-0.16-0.32c-0.4-0.75-0.92-1.44-1.53-2.04   c-1.52-1.49-3.6-2.42-5.91-2.42c-0.52,0-1.05,0.05-1.59,0.14c-1.65,0.3-3.16,1.11-4.32,2.27c-0.61,0.59-1.13,1.28-1.53,2.04   c-0.06,0.1-0.11,0.2-0.15,0.3c-0.34,0.68-0.57,1.4-0.71,2.15c-0.33,1.87-0.03,3.66,0.71,5.19c0.05,0.1,0.1,0.21,0.16,0.31   c0.4,0.75,0.92,1.43,1.53,2.03c0.51,0.49,1.07,0.93,1.69,1.28v0.39c0,0.02,0.01,0.05,0.01,0.08c0,0.02-0.01,0.04-0.01,0.07v0.62   c0,0.93,0.76,1.69,1.69,1.69h5.06c0.93,0,1.69-0.76,1.69-1.69v-0.62c0-0.02-0.01-0.04-0.01-0.07c0-0.03,0.01-0.05,0.01-0.08v-0.39   c0.62-0.35,1.18-0.79,1.69-1.28c0.61-0.6,1.12-1.28,1.53-2.04c0.06-0.1,0.11-0.21,0.16-0.32   C908.14,848.65,908.44,847.41,908.44,846.11L908.44,846.11z M895.79,850.25c-0.05-0.05-0.11-0.11-0.15-0.17   c-0.9-0.98-1.48-2.26-1.54-3.67c0.02-0.1,0.02-0.2,0.02-0.3c0-0.1,0-0.2-0.02-0.3c0.06-1.42,0.63-2.69,1.54-3.68   c0.04-0.06,0.1-0.11,0.15-0.17v0.48v7.34V850.25L895.79,850.25z M904.38,850.07c-0.04,0.06-0.09,0.12-0.15,0.18v-0.47v-7.34v-0.47   c0.05,0.05,0.11,0.11,0.15,0.17c0.91,0.99,1.49,2.3,1.53,3.75c-0.01,0.08-0.01,0.15-0.01,0.23c0,0.08,0,0.15,0.01,0.23   C905.87,847.77,905.29,849.08,904.38,850.07L904.38,850.07z"
     id="path1410" /></a>
	
	<a
   id="a63624"
   xlink:href="/child-participation#information"
   target="blank"
   xlink:title="Information, Internet and Protection of privacy"
   xlink:show="Information, Internet and Protection of privacy"><path
     class="st2"
     d="M833.26,862.5c-5.66,5.45-11.6,10.6-17.8,15.43c-5.44,4.24-6.77,11.92-3.04,17.73l26.88,41.83   c4.18,6.5,13.02,8.14,19.2,3.49c10.96-8.27,21.33-17.27,31.05-26.93c5.48-5.45,5.11-14.43-0.73-19.49l-37.57-32.56   C846.02,857.49,838.23,857.71,833.26,862.5L833.26,862.5z"
     id="path38" /><path
     class="st55"
     d="M870.71,909.79h-1.86h-2.83h-8.4c0,0.45-0.18,0.86-0.48,1.15c-0.29,0.3-0.7,0.48-1.15,0.48h-8.18   c-0.9,0-1.64-0.74-1.64-1.64h-8.18h-3.27h-1.64c-0.45,0-0.82,0.37-0.82,0.82v3.27c0,0.45,0.37,0.82,0.82,0.82h37.64   c0.45,0,0.82-0.37,0.82-0.82v-3.27C871.52,910.16,871.16,909.79,870.71,909.79L870.71,909.79z"
     id="path1412" /><path
     class="st55"
     d="M837.98,907.34h0.82v-15.54h26.18v15.54h0.82h3.27v-18c0-0.22-0.05-0.44-0.13-0.63   c-0.16-0.39-0.48-0.71-0.87-0.87c-0.19-0.08-0.41-0.13-0.64-0.13h-31.09c-0.9,0-1.64,0.73-1.64,1.64v0.82v17.18h2.45H837.98   L837.98,907.34z"
     id="path1414" /></a>
	
	
	<a
   id="a22180"
   xlink:href="/child-protection#justice"
   target="blank"
   xlink:title="Justice for children"
   xlink:show="Justice for children"><path
     class="st1"
     d="M465.56,775.24c-2.6-7.39-4.83-14.96-6.66-22.68c-1.59-6.7-8.1-11.04-14.92-10.06l-49.11,7.06   c-7.65,1.1-12.81,8.45-11.15,16c2.97,13.52,6.85,26.71,11.57,39.48c2.68,7.24,11,10.63,18.03,7.43l45.22-20.65   C464.83,788.95,467.86,781.76,465.56,775.24L465.56,775.24z"
     id="path18" /><path
     class="st55"
     d="M434.35,790.32h-8.02v-26.98h7.53l-3.81,8.71c-0.28,0.72,0.25,1.49,1.02,1.49c0.45,0,0.85-0.27,1.01-0.69   l3.36-8.06l3.36,8.06c0.16,0.42,0.57,0.69,1.02,0.69c0.77,0,1.3-0.78,1.02-1.49l-4.36-10.21c-0.16-0.42-0.56-0.69-1.01-0.69h-9.14   v-1.46c0-0.81-0.63-1.46-1.44-1.46c-0.81,0-1.48,0.65-1.48,1.46v1.46h-9.09c-0.45,0-0.85,0.28-1.01,0.69l-4.4,10.21   c-0.28,0.72,0.24,1.49,1.02,1.49c0.45,0,0.85-0.27,1.02-0.69l3.36-8.06l3.36,8.06c0.17,0.42,0.57,0.69,1.02,0.69   c0.77,0,1.3-0.78,1.01-1.49l-3.77-8.71h7.49v26.98h-8.02c-0.81,0-1.46,0.65-1.46,1.46c0,0.81,0.65,1.46,1.46,1.46h18.96   c0.8,0,1.46-0.65,1.46-1.46C435.81,790.97,435.15,790.32,434.35,790.32L434.35,790.32z"
     id="path1416" /><path
     class="st55"
     d="M421.22,775.96c0.03-0.12-0.06-0.23-0.18-0.23h-13.48c-0.12,0-0.21,0.11-0.18,0.23   c0.74,3.11,3.54,5.61,6.88,5.61C417.58,781.57,420.48,779.07,421.22,775.96L421.22,775.96z"
     id="path1418" /><path
     class="st55"
     d="M442.36,775.96c0.03-0.12-0.06-0.23-0.18-0.23H428.7c-0.12,0-0.21,0.11-0.18,0.23   c0.74,3.11,3.54,5.61,6.88,5.61C438.73,781.57,441.62,779.07,442.36,775.96L442.36,775.96z"
     id="path1420" /></a>
	
	
	
	
	
	
	
	
	
	<a
   id="a25363"
   xlink:href="/child-protection#marriage"
   target="blank"
   xlink:title="Child marriage and other harmful practices"
   xlink:show="Child marriage and other harmful practices"><path
     class="st1"
     d="M495.18,831.89c-4.61-6.4-8.89-13.04-12.82-19.92c-3.4-5.95-10.83-8.26-17.06-5.41l-45.21,20.65   c-7.03,3.21-9.92,11.73-6.18,18.51c6.64,12.05,14.09,23.6,22.26,34.57c4.61,6.19,13.55,7.1,19.39,2.04l37.57-32.55   C498.34,845.25,499.22,837.49,495.18,831.89L495.18,831.89z"
     id="path36" /><path
     class="st55"
     d="M463.01,831.53c-5.4,0-9.48,3.76-9.48,8.75c0,0.8,0.65,1.46,1.46,1.46c0.8,0,1.46-0.65,1.46-1.46   c0-2.2,1.23-4.03,3.15-5.03l-2.41,13.66c-0.07,0.44,0.27,0.85,0.72,0.85h1.46v8.02c0,0.81,0.65,1.46,1.46,1.46   c0.8,0,1.46-0.65,1.46-1.46v-8.02h1.46v8.02c0,0.81,0.65,1.46,1.46,1.46c0.8,0,1.46-0.65,1.46-1.46v-8.02h1.46   c0.45,0,0.79-0.41,0.72-0.85l-2.34-13.62c1.87,1,3.08,2.82,3.08,4.99c0,0.8,0.65,1.46,1.46,1.46c0.81,0,1.46-0.65,1.46-1.46   C472.49,835.29,468.41,831.53,463.01,831.53L463.01,831.53z"
     id="path1422" /><path
     class="st55"
     d="M463.01,830.07c1.61,0,2.92-1.31,2.92-2.92c0-1.61-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92   C460.09,828.76,461.4,830.07,463.01,830.07L463.01,830.07z"
     id="path1424" /><path
     class="st55"
     d="M446.6,854.13c-0.6,0-1.09,0.49-1.09,1.09v2.92c0,0.6,0.49,1.09,1.09,1.09s1.09-0.49,1.09-1.09v-2.92   C447.69,854.62,447.2,854.13,446.6,854.13L446.6,854.13z"
     id="path1426" /><path
     class="st55"
     d="M454.62,849.03h-2.92c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h2.92c0.6,0,1.09-0.49,1.09-1.09   C455.71,849.52,455.22,849.03,454.62,849.03L454.62,849.03z"
     id="path1428" /><path
     class="st55"
     d="M446.6,841c-0.6,0-1.09,0.49-1.09,1.09v2.91c0,0.6,0.49,1.09,1.09,1.09s1.09-0.49,1.09-1.09v-2.91   C447.7,841.49,447.21,841,446.6,841L446.6,841z"
     id="path1430" /><path
     class="st55"
     d="M442.59,850.12c0-0.6-0.49-1.09-1.09-1.09h-2.92c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h2.92   C442.1,851.21,442.59,850.72,442.59,850.12L442.59,850.12z"
     id="path1432" /><path
     class="st55"
     d="M451.02,852.99c-0.43-0.43-1.12-0.43-1.55,0c-0.43,0.43-0.43,1.12,0,1.55l2.19,2.19   c0.43,0.43,1.12,0.43,1.55,0c0.43-0.43,0.43-1.12,0-1.55L451.02,852.99L451.02,852.99z"
     id="path1434" /><path
     class="st55"
     d="M451.02,847.25l2.19-2.19c0.43-0.43,0.43-1.12,0-1.55s-1.12-0.43-1.55,0l-2.19,2.19   c-0.43,0.43-0.43,1.12,0,1.55C449.9,847.67,450.59,847.67,451.02,847.25L451.02,847.25z"
     id="path1436" /><path
     class="st55"
     d="M442.18,847.25c0.43,0.43,1.12,0.43,1.55,0s0.43-1.12,0-1.55l-2.19-2.19c-0.43-0.43-1.12-0.43-1.55,0   c-0.43,0.43-0.43,1.12,0,1.55L442.18,847.25L442.18,847.25z"
     id="path1438" /><path
     class="st55"
     d="M442.18,852.99l-2.19,2.19c-0.43,0.43-0.43,1.12,0,1.55c0.43,0.43,1.12,0.43,1.55,0l2.19-2.19   c0.43-0.43,0.43-1.12,0-1.55C443.3,852.56,442.61,852.56,442.18,852.99L442.18,852.99z"
     id="path1440" /></a>
	
	
	<a
   id="a28546"
   xlink:href="/child-protection#labour"
   target="blank"
   xlink:title="Child exploitation"
   xlink:show="Child exploitation"><path
     class="st1"
     d="M539.55,877.94c-6.2-4.84-12.15-9.99-17.8-15.43c-4.98-4.79-12.77-5.01-17.99-0.49l-37.57,32.55   c-5.84,5.06-6.21,14.04-0.73,19.49c9.72,9.66,20.09,18.66,31.05,26.93c6.17,4.66,15.02,3.02,19.2-3.49l26.88-41.83   C546.32,889.86,544.99,882.18,539.55,877.94L539.55,877.94z"
     id="path34" /><path
     class="st55"
     d="M491.54,889.22c1.61,0,2.92-1.31,2.92-2.92c0-1.61-1.31-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92   C488.62,887.92,489.93,889.22,491.54,889.22L491.54,889.22z"
     id="path1442" /><path
     class="st55"
     d="M516.88,904.14l2.86-5.65c0.88-1.74,0.17-3.87-1.57-4.75l-0.92-0.46l-0.95-0.48   c-0.09-0.04-0.18-0.08-0.28-0.1c-0.85-0.39-1.74-0.65-2.63-0.79c-3.62-0.59-7.33,0.74-9.64,3.62l-1.55-1.79   c-2.19-2.4-5.32-3.78-8.57-3.78c-1.55,0-3.05,0.74-3.98,1.99c-1,1.33-1.27,3.07-0.71,4.65c0.01,0.04,0.03,0.07,0.04,0.1l2.1,4.81   c0.15,0.55,0.53,1.76,1.11,3.58c1.04,3.28,1.75,6.67,2.09,10.08l0.19,1.92c0.07,0.75,0.71,1.31,1.45,1.31c0.04,0,0.09,0,0.15-0.01   c0.8-0.08,1.38-0.79,1.3-1.6l-0.19-1.91c-0.33-3.24-0.96-6.47-1.89-9.61h2.9c0.83,2.22,1.37,4.6,1.37,8.75   c0,0.68,0.47,1.25,1.09,1.41l1.77-3.47c-0.24-4.94-1.36-7.52-2.64-10.44c-0.29-0.67-0.6-1.36-0.9-2.12l-2.46-6.06   c1.37,0.47,2.62,1.26,3.6,2.33l2.81,3.27c0.26,0.3,0.61,0.47,0.98,0.5c0.07,0,0.12,0.01,0.17,0.01c0.55,0,1.08-0.3,1.35-0.82   c1.18-2.3,3.43-3.64,5.84-3.81c0.28-0.02,0.55-0.03,0.82-0.01c0.26,0.01,0.52,0.04,0.78,0.07l-10.86,21.31   c-0.39,0.75-0.09,1.67,0.66,2.05c0.22,0.12,0.46,0.17,0.69,0.17c0.55,0,1.09-0.31,1.36-0.83l6.59-12.93l0.65,0.33l0.66,0.33   l2.38,1.21c0.01,0.01,0.02,0.01,0.03,0.02c0.02,0.01,0.03,0.02,0.05,0.03l0.04,0.02c3.15,2.04,4.3,6.2,2.53,9.6   c-0.39,0.75-0.1,1.66,0.65,2.05c0.37,0.19,0.79,0.22,1.16,0.1c0.37-0.12,0.7-0.38,0.89-0.75   C522.72,912.83,521.18,907.07,516.88,904.14L516.88,904.14z"
     id="path1444" /><path
     class="st55"
     d="M523.47,889.04c-0.5-1.53-2.15-2.36-3.68-1.86c-1.53,0.5-2.36,2.15-1.86,3.68c0.5,1.53,2.15,2.36,3.68,1.86   C523.15,892.22,523.98,890.57,523.47,889.04L523.47,889.04z"
     id="path1446" /></a>
	
	<a
   id="a31708"
   xlink:href="/child-education#system"
   target="blank"
   xlink:title="Education system"
   xlink:show="Education system"><path
     class="st4"
     d="M588.94,973.55l14.01-47.7c1.93-6.59-1.42-13.63-7.8-16.14c-7.37-2.91-14.56-6.2-21.52-9.84   c-6.12-3.2-13.67-1.22-17.41,4.59l-26.89,41.84c-4.17,6.49-2.01,15.21,4.78,18.9c12,6.52,24.49,12.25,37.41,17.11   C578.74,985.03,586.77,980.97,588.94,973.55L588.94,973.55z"
     id="path40" /><path
     class="st55"
     d="M583.63,954.06h-32.81c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h32.81c0.6,0,1.09-0.49,1.09-1.09   S584.24,954.06,583.63,954.06L583.63,954.06z"
     id="path1448" /><path
     class="st55"
     d="M564.31,945.32c0-0.8,0.66-1.46,1.46-1.46h2.92c0.8,0,1.46,0.66,1.46,1.46v7.29h11.67v-18.23   c0-0.4-0.33-0.73-0.73-0.73h-7.29l-5.1-3.83v-2.73h6.56v-4.38h-6.56c0-0.81-0.65-1.46-1.46-1.46c-0.8,0-1.46,0.65-1.46,1.46v7.11   l-5.1,3.83h-7.29c-0.4,0-0.73,0.33-0.73,0.73v18.23h11.67V945.32L564.31,945.32z M575.25,937.29c0-0.4,0.33-0.73,0.73-0.73h1.46   c0.4,0,0.73,0.33,0.73,0.73v3.65c0,0.4-0.33,0.73-0.73,0.73h-1.46c-0.4,0-0.73-0.33-0.73-0.73V937.29L575.25,937.29z    M575.25,945.32c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73v3.65c0,0.4-0.33,0.73-0.73,0.73h-1.46   c-0.4,0-0.73-0.33-0.73-0.73V945.32L575.25,945.32z M559.21,948.96c0,0.4-0.33,0.73-0.73,0.73h-1.46c-0.4,0-0.73-0.33-0.73-0.73   v-3.65c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73V948.96L559.21,948.96z M559.21,940.94c0,0.4-0.33,0.73-0.73,0.73   h-1.46c-0.4,0-0.73-0.33-0.73-0.73v-3.65c0-0.4,0.33-0.73,0.73-0.73h1.46c0.4,0,0.73,0.33,0.73,0.73V940.94L559.21,940.94z    M570.14,936.57c0,1.61-1.3,2.92-2.92,2.92c-1.61,0-2.92-1.31-2.92-2.92c0-1.61,1.31-2.92,2.92-2.92   C568.84,933.65,570.14,934.95,570.14,936.57L570.14,936.57z"
     id="path1450" /></a>
	
	
	<a
   id="a55491"
   xlink:href="/child-poverty#povertydeprivation"
   target="blank"
   xlink:title="Child Poverty and Material Deprivation"
   xlink:show="Child Poverty and Material Deprivation"><path
     class="st3"
     d="M859.86,569.54c4.61,6.4,8.89,13.05,12.82,19.93c3.4,5.95,10.83,8.26,17.07,5.42l45.17-20.63   c7.03-3.21,9.92-11.74,6.18-18.51c-6.64-12.05-14.09-23.6-22.26-34.57c-4.61-6.19-13.55-7.1-19.39-2.04l-37.52,32.51   C856.7,556.18,855.82,563.93,859.86,569.54L859.86,569.54z"
     id="path24" /><path
     class="st55"
     d="M902.46,562.01l5.23-5.18c0.56-0.57,1.47-0.57,2.03,0c0.56,0.57,0.56,1.49,0,2.06l-2.61,2.51   c-0.33,0.33-0.33,0.87,0,1.2c0.33,0.33,0.86,0.33,1.18,0l3.23-3.45v-11c0-1.14,0.94-2.06,2.06-2.06c1.12,0,2.06,0.92,2.06,2.06   v11.96c0,0.55-0.21,1.07-0.59,1.46l-7.66,7.89v6.19h-6.19v-10.31C901.21,563.97,901.56,562.93,902.46,562.01L902.46,562.01z"
     id="path1452" /><path
     class="st55"
     d="M895.82,562.01l-5.23-5.18c-0.56-0.57-1.47-0.57-2.03,0c-0.56,0.57-0.56,1.49,0,2.06l2.61,2.51   c0.33,0.33,0.33,0.87,0,1.2c-0.33,0.33-0.85,0.33-1.18,0l-3.23-3.45v-11c0-1.14-0.94-2.06-2.06-2.06c-1.12,0-2.06,0.92-2.06,2.06   v11.96c0,0.55,0.21,1.07,0.6,1.46l7.65,7.89v6.19h6.19v-10.31C897.08,563.97,896.72,562.93,895.82,562.01L895.82,562.01z"
     id="path1454" /><path
     class="st55"
     d="M905.33,548.85c0-3.42-2.77-6.19-6.19-6.19c-3.42,0-6.19,2.77-6.19,6.19c0,3.42,2.77,6.19,6.19,6.19   C902.56,555.03,905.33,552.26,905.33,548.85L905.33,548.85z"
     id="path1456" /></a>
	
	
	
	
	
	
	<a
   id="a63593"
   xlink:title="Birth registration and identity"
   xlink:show="Birth registration and identity"
   target="blank"
   xlink:href="/child-participation#registration"><path
     class="st2"
     d="M902.11,700.68c0,4.01-0.11,7.99-0.32,11.95c-0.36,6.85,4.64,12.82,11.43,13.8l49.16,7.07   c7.65,1.1,14.68-4.51,15.2-12.22c0.46-6.79,0.69-13.64,0.69-20.55c0-6.91-0.23-13.76-0.69-20.55c-0.52-7.71-7.55-13.32-15.2-12.22   l-49.16,7.07c-6.79,0.98-11.79,6.95-11.43,13.8C902.01,692.76,902.11,696.71,902.11,700.68L902.11,700.68z"
     id="path20" /><path
     class="st55"
     d="M939.72,707.87h-1.46c-0.4,0-0.73,0.33-0.73,0.73v0.73c0,0.4,0.33,0.73,0.73,0.73h1.46   c0.4,0,0.73-0.33,0.73-0.73v-0.73C940.45,708.2,940.12,707.87,939.72,707.87L939.72,707.87z"
     id="path1458" /><path
     class="st55"
     d="M939.72,702.04h-1.46c-0.4,0-0.73,0.33-0.73,0.73v0.73c0,0.4,0.33,0.73,0.73,0.73h1.46   c0.4,0,0.73-0.33,0.73-0.73v-0.73C940.45,702.36,940.12,702.04,939.72,702.04L939.72,702.04z"
     id="path1460" /><path
     class="st55"
     d="M944.1,694.02c0.81,0,1.46-0.65,1.46-1.46c0-0.81-0.65-1.46-1.46-1.46c-0.8,0-1.46,0.65-1.46,1.46   C942.64,693.36,943.29,694.02,944.1,694.02L944.1,694.02z"
     id="path1462" /><path
     class="st55"
     d="M949.57,707.87h-5.83c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h5.83c0.6,0,1.09-0.49,1.09-1.09   C950.66,708.36,950.17,707.87,949.57,707.87L949.57,707.87z"
     id="path1464" /><path
     class="st55"
     d="M947.01,697.96c0-1.37-1.11-2.49-2.49-2.49h-0.86c-1.37,0-2.49,1.11-2.49,2.49v1.16h5.83V697.96   L947.01,697.96z"
     id="path1466" /><path
     class="st55"
     d="M954.3,685.27h-3.65c0-0.8-0.66-1.46-1.46-1.46h-2.19c0-0.8-0.33-1.53-0.85-2.06   c-0.53-0.52-1.26-0.85-2.06-0.85c-1.61,0-2.92,1.3-2.92,2.92h-2.19c-0.8,0-1.46,0.66-1.46,1.46h-3.64c-0.8,0-1.46,0.71-1.46,1.57   v27.49c0,0.86,0.66,1.57,1.46,1.57h20.42c0.8,0,1.46-0.71,1.46-1.57v-27.49C955.76,685.97,955.11,685.27,954.3,685.27L954.3,685.27   z M944.1,683.81c0.4,0,0.73,0.33,0.73,0.73c0,0.4-0.33,0.73-0.73,0.73c-0.4,0-0.73-0.33-0.73-0.73   C943.37,684.13,943.69,683.81,944.1,683.81L944.1,683.81z M952.85,712.97h-17.5v-24.79h2.19c0,0.8,0.66,1.46,1.46,1.46h10.21   c0.8,0,1.46-0.66,1.46-1.46h2.19V712.97L952.85,712.97z"
     id="path1468" /><path
     class="st55"
     d="M949.57,702.04h-5.83c-0.6,0-1.09,0.49-1.09,1.09c0,0.6,0.49,1.09,1.09,1.09h5.83c0.6,0,1.09-0.49,1.09-1.09   C950.66,702.53,950.17,702.04,949.57,702.04L949.57,702.04z"
     id="path1470" /></a>
	<a
   id="a52309"
   xlink:title="Social protection system"
   xlink:show="Social protection system"
   target="blank"
   xlink:href="/child-poverty#socialprotection"><path
     class="st3"
     d="M815.49,523.46c6.21,4.84,12.15,10,17.81,15.45c4.97,4.79,12.77,5.01,17.99,0.49l37.52-32.51   c5.84-5.06,6.21-14.04,0.73-19.49c-9.72-9.66-20.09-18.66-31.05-26.93c-6.17-4.66-15.02-3.02-19.2,3.49l-26.84,41.76   C808.73,511.54,810.05,519.22,815.49,523.46L815.49,523.46z"
     id="path32" /><path
     class="st55"
     d="M852.2,482.89c-0.16-0.2-0.47-0.2-0.63,0c-1.93,2.48-12.08,15.83-12.08,22.17c0,7,5.55,12.68,12.4,12.68   s12.4-5.68,12.4-12.68C864.28,498.72,854.13,485.37,852.2,482.89L852.2,482.89z M855.17,512.64c-0.6,0-1.09-0.49-1.09-1.09   s0.49-1.09,1.09-1.09c1.81,0,3.28-1.8,3.28-4.01c0-0.6,0.49-1.09,1.09-1.09s1.09,0.49,1.09,1.09   C860.64,509.86,858.19,512.64,855.17,512.64L855.17,512.64z"
     id="path1472" /></a>
	<a
   id="a47559"
   xlink:title="HIV/AIDS"
   xlink:show="HIV/AIDS"
   target="blank"
   xlink:href="/child-health#hivaids"><path
     class="st0"
     d="M766.06,427.91l-13.98,47.6c-1.93,6.59,1.42,13.63,7.81,16.15c7.38,2.91,14.57,6.2,21.54,9.85   c6.12,3.2,13.67,1.23,17.41-4.59l26.84-41.76c4.17-6.49,2.01-15.21-4.78-18.9c-12-6.52-24.49-12.25-37.41-17.11   C776.26,416.43,768.23,420.5,766.06,427.91L766.06,427.91z"
     id="path14" /><path
     class="st55"
     d="M806.47,467.85l-18.89-9.48c0,0,0-0.04,0.01-0.1c0.02-0.11,0.02-0.21,0.02-0.26c0,0-0.01-0.01-0.01-0.01   c0.04-1.42-0.03-6.67-2.92-9.86c0.12,0.13,0.25,0.25,0.36,0.4c0,0-3.53-5.18-6.95-5.36c-1.66-0.09-2.89,1.19-3.28,1.69   c-0.39,0.5-2.07,3.32-1.96,7.4c0,0-0.02-1.57,0.84-3.22c-1.49,3.12-0.65,5.49,0.23,7.02c0.19,1.6,1.07,2.74,1.48,3.35   c0.78,1.18,2.85,2.87,3.56,3.33c-0.36,1.48-1,4.18-1.26,5.95c-0.29,2.04-0.51,7.79-0.51,7.79l6.66,1.69c0,0,0.22-0.28,0.25-0.67   c0.02-0.21,0.8-7.98,1.38-11.01c3.43,1.77,11.9,6.14,11.9,6.14l0.56-0.91c2.64,1.36,4.67,2.41,4.67,2.41L806.47,467.85   L806.47,467.85z M784.57,448.02c-0.06-0.06-0.12-0.12-0.18-0.18C784.45,447.9,784.51,447.96,784.57,448.02L784.57,448.02z    M775.9,446.59c1.66-1.09,4.58-0.67,5.06-0.59c0.2,0.04,0.71,0.18,1.33,0.46c0.83,1.7,0.77,5.88-0.85,8.9c0,0-6.78-3.11-7.68-6.43   C774.2,448.1,774.88,447.25,775.9,446.59L775.9,446.59z"
     id="path1474" /></a>
	<a
   id="a33295"
   xlink:href="/child-education#participation"
   target="blank"
   xlink:title="Education access and participation"
   xlink:show="Education access and participation"><path
     class="st4"
     d="M657.26,924.38c-7.91-0.7-15.7-1.82-23.36-3.32c-6.77-1.33-13.44,2.69-15.39,9.32l-14.01,47.72   c-2.18,7.42,2.37,15.18,9.93,16.79c13.27,2.83,26.86,4.79,40.71,5.81c7.7,0.56,14.25-5.59,14.25-13.32v-49.62   C669.39,930.84,664.15,925,657.26,924.38L657.26,924.38z"
     id="path26" /><path
     class="st55"
     d="M636.54,965.41l-1.5,2.76c-0.07,0.16-0.28,0.43-0.79,0.43c-0.62,0-1.67-0.39-2.35-0.68l-0.13,0.29l-1.02-0.47   l0.13-0.28c-0.9-0.45-2.01-1.1-2.22-1.66l-0.08-0.31l0.08-0.22l1.15-2.96c-1.18,0.75-2.2,2.38-3.49,4.99l-1.46,3.07   c-0.12,0.27-0.25,0.54-0.38,0.83l8.72,4.03c0.13-0.28,0.26-0.56,0.38-0.83l1.4-3.09C636.16,968.62,636.74,966.79,636.54,965.41   L636.54,965.41z M633.74,972.14l-1.08,2.35l-7.26-3.36l1.09-2.35c0.31-0.66,1.11-1,2.12-1c0.75,0,1.62,0.19,2.48,0.59   C633.09,969.3,634.29,970.98,633.74,972.14L633.74,972.14z M633.17,971.09c0.11,0.31,0.11,0.57,0.01,0.79l-0.83,1.79l-6.14-2.84   l0.83-1.79c0.19-0.4,0.77-0.65,1.55-0.65c0.69,0,1.48,0.19,2.22,0.54C631.98,969.47,632.88,970.29,633.17,971.09L633.17,971.09z    M634.82,962.51c0.21,0.09,0.44,0.15,0.67,0.17c0.04,0.22,0.05,0.45,0.03,0.68c0.64,0.4,1.03,0.73,0.96,0.87l-2,3.69   c-0.11,0.24-1.37-0.1-2.82-0.77c-1.44-0.67-2.52-1.41-2.41-1.66l1.51-3.91c0.07-0.14,0.57-0.06,1.28,0.17   c0.44-0.45,1.03-0.7,1.6-0.7c0.04,0.2,0.1,0.41,0.23,0.63c-0.39-0.07-0.8,0.05-1.15,0.31c0.35,0.14,0.72,0.29,1.11,0.47   c0.39,0.18,0.75,0.36,1.07,0.54C634.89,962.83,634.88,962.67,634.82,962.51C634.83,962.51,634.83,962.51,634.82,962.51   L634.82,962.51z M649.73,963.14c-0.09,0.47,0.02,1.36,0.22,1.8l5.13,11.13c0.26,0.56,0.56,1.21,0.11,1.91   c-0.26,0.41-0.72,0.66-1.21,0.66l0,0c-0.86,0-1.25-0.65-1.56-1.17l-6.33-10.65l-1.72,3.49c-0.4,0.82-1.2,1.97-1.81,2.63l-3.46,3.73   c-0.45,0.48-0.8,0.86-1.46,0.86c-0.55,0-1.05-0.32-1.29-0.82c-0.4-0.84,0.09-1.45,0.52-1.98l3.41-4.22   c0.36-0.45,0.85-1.38,1.01-1.94l1.27-4.42c0.18-0.65,0.4-1.8,0.45-2.47l0.56-6.8c-2.76,0.91-5.46,4.52-6.38,6.03   c-0.39,0.63-0.72,1.18-1.54,1.18h-0.01c-0.5,0-0.98-0.27-1.23-0.71c-0.42-0.72-0.11-1.28,0.25-1.93c0.21-0.38,5.31-9.37,12.19-8.83   c2.97,0.26,3.92,2.49,4.55,3.97c0.15,0.34,0.29,0.68,0.45,0.98l3.92,7.09c0.37,0.68,0.15,1.56-0.52,1.95   c-0.67,0.39-1.51,0.21-1.92-0.45l-2.92-4.66L649.73,963.14L649.73,963.14z M651.43,946.41c0.3,1.8-0.93,3.49-2.72,3.79   c-1.8,0.3-3.49-0.92-3.79-2.72c-0.3-1.8,0.92-3.49,2.72-3.79C649.44,943.39,651.13,944.61,651.43,946.41L651.43,946.41z"
     id="path1476" /></a>
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a41204"
   target="blank"
   xlink:title="Leisure and culture"
   xlink:show="Leisure and culture"
   xlink:href="/child-participation#leisure"><path
     class="st4"
     d="M781.38,899.87c-6.97,3.64-14.15,6.93-21.52,9.84c-6.39,2.52-9.74,9.56-7.8,16.14l14.01,47.7   c2.18,7.42,10.2,11.48,17.43,8.76c12.92-4.86,25.41-10.59,37.41-17.11c6.78-3.69,8.95-12.4,4.78-18.9l-26.89-41.84   C795.05,898.65,787.5,896.67,781.38,899.87L781.38,899.87z"
     id="path46" /><path
     class="st55"
     d="M799.94,923.23c-0.55-1.67-2.35-2.57-4.01-2.02s-2.57,2.35-2.03,4.01c0.55,1.67,2.35,2.57,4.01,2.02   C799.58,926.7,800.49,924.9,799.94,923.23L799.94,923.23z"
     id="path1478" /><path
     class="st55"
     d="M792.74,939.72l3.12-6.19c0.96-1.9,0.2-4.22-1.71-5.18l-2.03-1.02c-0.11-0.06-0.22-0.09-0.34-0.12   c-5.41-2.37-11.82-0.16-14.54,5.17c-0.41,0.81-0.09,1.8,0.72,2.21c0.81,0.41,1.8,0.09,2.21-0.71c1.57-3.07,4.86-4.68,8.1-4.27   l-11.83,23.19c-0.42,0.82-0.09,1.81,0.72,2.23c0.24,0.12,0.5,0.18,0.75,0.18c0.6,0,1.19-0.33,1.48-0.91l7.18-14.09l3.56,1.79   c3.84,2.09,5.32,6.88,3.3,10.77c-0.42,0.81-0.11,1.81,0.71,2.23c0.41,0.21,0.86,0.24,1.26,0.11c0.4-0.13,0.76-0.41,0.97-0.82   C799.05,949.17,797.39,942.92,792.74,939.72L792.74,939.72z"
     id="path1480" /><path
     class="st55"
     d="M774.21,935.49h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.39,0.32-0.72,0.72-0.72h9.14   c0.39,0,0.72,0.32,0.72,0.72l0,0C774.93,935.17,774.61,935.49,774.21,935.49L774.21,935.49z"
     id="path1482" /><path
     class="st55"
     d="M778.91,938.82h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.4,0.32-0.72,0.72-0.72h9.14   c0.39,0,0.72,0.32,0.72,0.72l0,0C779.62,938.49,779.3,938.82,778.91,938.82L778.91,938.82z"
     id="path1484" /><path
     class="st55"
     d="M774.21,942.13h-9.14c-0.39,0-0.72-0.32-0.72-0.72l0,0c0-0.4,0.32-0.72,0.72-0.72h9.14   c0.39,0,0.72,0.32,0.72,0.72l0,0C774.93,941.81,774.61,942.13,774.21,942.13L774.21,942.13z"
     id="path1486" /><path
     class="st55"
     d="M803.03,949.16c0.94,0,1.79,0.38,2.41,0.99c-0.84,1.06-1.85,2.02-3.05,2.9c-0.11-0.09-0.25-0.14-0.41-0.15   c-0.44-1.21-0.52-2.37-0.25-3.48C802.13,949.25,802.57,949.16,803.03,949.16L803.03,949.16L803.03,949.16z"
     id="path1488" /><path
     class="st55"
     d="M801.41,949.57c-0.22,1.09-0.13,2.21,0.29,3.38c-0.15,0.06-0.28,0.17-0.36,0.32l-1.74-0.75   C799.63,951.24,800.35,950.13,801.41,949.57L801.41,949.57L801.41,949.57z"
     id="path1490" /><path
     class="st55"
     d="M805.64,950.36c0.52,0.6,0.83,1.39,0.83,2.24c0,0.46-0.09,0.9-0.25,1.29c-1.18,0.08-2.36-0.01-3.55-0.28   c0,0,0-0.01,0-0.01c0-0.13-0.04-0.24-0.09-0.35C803.77,952.39,804.79,951.42,805.64,950.36L805.64,950.36L805.64,950.36z"
     id="path1492" /><path
     class="st55"
     d="M799.6,952.83l1.65,0.7c0,0.03-0.01,0.05-0.01,0.08c0,0.17,0.07,0.33,0.17,0.45l-0.71,1.06   C800.07,954.55,799.66,953.74,799.6,952.83L799.6,952.83L799.6,952.83z"
     id="path1494" /><path
     class="st55"
     d="M801.95,953.18c0.24,0,0.43,0.19,0.43,0.43c0,0.24-0.19,0.43-0.43,0.43c-0.24,0-0.43-0.19-0.43-0.43   C801.53,953.37,801.72,953.18,801.95,953.18L801.95,953.18z"
     id="path1496" /><path
     class="st55"
     d="M802.61,953.9c1.16,0.26,2.32,0.36,3.47,0.3c-0.51,0.97-1.46,1.66-2.59,1.82c-0.5-0.56-0.83-1.2-1.02-1.91   C802.53,954.04,802.58,953.97,802.61,953.9L802.61,953.9z"
     id="path1498" /><path
     class="st55"
     d="M801.63,954.25c0.1,0.05,0.21,0.08,0.32,0.08c0.1,0,0.19-0.02,0.27-0.05c0.18,0.65,0.48,1.24,0.91,1.77   c-0.04,0-0.07,0.01-0.11,0.01c-0.8,0-1.53-0.27-2.12-0.73L801.63,954.25L801.63,954.25z"
     id="path1500" /></a>
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a1736"
   xlink:href="/child-health"
   target="blank"
   xlink:show="Child Health"
   xlink:title="Child Health"><g
     id="g1504">
		<path
   class="st0"
   d="M564.51,537.29l-3.35-4.71l2.46-1.75l8.36,11.78l-2.46,1.75l-3.73-5.25l-2.82,2l3.73,5.25l-2.46,1.75    l-8.36-11.78l2.46-1.75l3.35,4.71L564.51,537.29z"
   id="path1502" />
	</g><g
     id="g1508">
		<path
   class="st0"
   d="M573.86,536c0.64,1.02,1.62,2.52,2.67,1.87c0.85-0.53,0.51-1.45,0.07-2.16l2.43-1.51    c0.55,0.96,0.72,1.91,0.47,2.8c-0.23,0.88-0.89,1.71-2.01,2.41c-3.09,1.93-4.67,0.3-6.34-2.39c-1.46-2.34-2.37-4.56,0.79-6.53    c3.23-2.01,4.88-0.15,6.51,2.66L573.86,536z M575.22,533.29c-0.52-0.83-1.22-2.04-2.36-1.33c-1.1,0.69-0.28,1.97,0.17,2.7    L575.22,533.29z"
   id="path1506" />
	</g><g
     id="g1512">
		<path
   class="st0"
   d="M588.38,530.67c0.3,0.54,0.68,1.06,1.04,1.57l-2.29,1.28l-0.76-1.11l-0.04,0.02    c-0.02,1.2-0.49,2.04-1.55,2.63c-1.71,0.96-3.05,0.03-3.91-1.5c-1.63-2.92,0.55-4.3,2.86-5.54l-0.38-0.68    c-0.42-0.75-0.83-1.23-1.72-0.74c-0.86,0.48-0.56,1.16-0.17,1.86l-2.41,1.35c-0.59-1.06-0.64-1.93-0.29-2.65    c0.32-0.73,1.04-1.34,1.98-1.86c3.13-1.75,4.28-0.63,5.18,0.98L588.38,530.67z M583.22,532.11c0.35,0.63,0.89,1.34,1.69,0.89    c1.45-0.81,0.13-2.64-0.41-3.6C583.31,530.13,582.35,530.54,583.22,532.11z"
   id="path1510" />
	</g><g
     id="g1516">
		<path
   class="st0"
   d="M587.68,516.96l6.44,12.93l-2.52,1.26l-6.44-12.93L587.68,516.96z"
   id="path1514" />
	</g><g
     id="g1520">
		<path
   class="st0"
   d="M591.05,520.13l1.03-0.48l-0.68-1.45l2.02-2.34l1.21,2.59l1.32-0.62l0.74,1.58l-1.32,0.62l2.29,4.89    c0.32,0.69,0.52,1.15,1.35,0.76c0.16-0.08,0.33-0.15,0.44-0.25l0.74,1.58c-0.33,0.2-0.66,0.42-1.28,0.71    c-2.21,1.04-3.19-0.29-3.45-0.86l-2.64-5.63l-1.03,0.48L591.05,520.13z"
   id="path1518" />
	</g><g
     id="g1524">
		<path
   class="st0"
   d="M605.96,524.5l-2.73-6.4c-0.35-0.83-0.77-1.41-1.6-1.06c-0.83,0.35-0.7,1.06-0.35,1.89l2.73,6.4l-2.59,1.11    l-5.66-13.29l2.6-1.11l2.1,4.93l0.04-0.02c0.08-0.53,0.27-0.94,0.55-1.26c0.29-0.34,0.68-0.59,1.16-0.8    c1.23-0.53,2.63-0.25,3.18,1.04l3.18,7.45L605.96,524.5z"
   id="path1522" />
	</g><g
     id="g1528">
		<path
   class="st0"
   d="M621.48,516.84c0.19,0.59,0.47,1.17,0.72,1.74l-2.49,0.82l-0.53-1.23l-0.04,0.01    c-0.24,1.18-0.86,1.91-2.02,2.29c-1.86,0.62-3-0.55-3.56-2.22c-1.05-3.17,1.36-4.11,3.86-4.9l-0.25-0.74    c-0.27-0.82-0.58-1.37-1.55-1.05c-0.93,0.31-0.77,1.04-0.52,1.79l-2.62,0.87c-0.38-1.16-0.27-2.02,0.21-2.66    c0.46-0.66,1.27-1.12,2.3-1.46c3.4-1.12,4.32,0.19,4.9,1.94L621.48,516.84z M616.15,517.27c0.23,0.68,0.62,1.48,1.49,1.19    c1.58-0.52,0.63-2.57,0.28-3.61C616.61,515.35,615.59,515.56,616.15,517.27z"
   id="path1526" />
	</g><g
     id="g1532">
		<path
   class="st0"
   d="M624.58,508.43l0.04-0.01c0.15-0.52,0.39-0.9,0.71-1.17c0.33-0.3,0.75-0.5,1.25-0.64    c1.29-0.36,2.64,0.09,3.02,1.44l2.17,7.8l-2.72,0.76l-1.87-6.71c-0.24-0.87-0.58-1.5-1.45-1.26c-0.87,0.24-0.83,0.96-0.59,1.83    l1.87,6.71l-2.72,0.76l-2.71-9.73l2.72-0.76L624.58,508.43z"
   id="path1530" />
	</g><g
     id="g1536">
		<path
   class="st0"
   d="M638.87,514.2l-0.25-1.09l-0.04,0.01c-0.29,1.07-0.98,1.58-2.03,1.82c-2.85,0.65-3.47-2.54-3.93-4.56    c-0.45-1.99-1.23-5.03,1.54-5.66c1-0.23,1.74-0.09,2.5,0.62l0.04-0.01l-1.18-5.17l2.75-0.62l3.2,14.08L638.87,514.2z     M637.6,509.21c-0.45-1.97-0.74-3.34-1.87-3.08c-1.19,0.27-0.86,1.63-0.41,3.6c0.56,2.48,0.97,3.47,1.97,3.25    C638.22,512.77,638.16,511.69,637.6,509.21z"
   id="path1534" />
	</g><g
     id="g1540">
		<path
   class="st0"
   d="M648.25,512.34l-2-14.3l4.04-0.56l5.19,9.38l0.04-0.01l-1.38-9.91l2.79-0.39l2,14.3l-3.94,0.55l-5.36-9.92    l-0.04,0.01l1.46,10.46L648.25,512.34z"
   id="path1538" />
	</g><g
     id="g1544">
		<path
   class="st0"
   d="M666.17,509.26l-0.04,0c-0.25,0.46-0.54,0.8-0.92,1.02c-0.38,0.23-0.82,0.34-1.35,0.39    c-1.34,0.1-2.58-0.6-2.68-2l-0.63-8.08l2.81-0.22l0.54,6.98c0.07,0.9,0.28,1.54,1.18,1.47s1.01-0.74,0.94-1.64l-0.54-6.98    l2.81-0.22l0.63,8.08c0.05,0.66,0.14,1.33,0.25,1.99l-2.91,0.23L666.17,509.26z"
   id="path1542" />
	</g><g
     id="g1548">
		<path
   class="st0"
   d="M669.87,499.92l1.14-0.03l-0.05-1.6l2.78-1.34l0.08,2.86l1.46-0.04l0.05,1.74l-1.46,0.04l0.15,5.4    c0.02,0.76,0.02,1.26,0.94,1.24c0.18,0,0.36-0.01,0.5-0.05l0.05,1.74c-0.38,0.05-0.78,0.12-1.46,0.14    c-2.44,0.07-2.81-1.54-2.82-2.16l-0.18-6.22l-1.14,0.03L669.87,499.92z"
   id="path1546" />
	</g><g
     id="g1552">
		<path
   class="st0"
   d="M679.5,499.73l0,1.3l0.04,0c0.52-1.16,1.48-1.51,2.62-1.51l0.01,2.52c-2.48-0.15-2.52,1.29-2.51,2.29    l0.02,5.5l-2.82,0.01l-0.04-10.1L679.5,499.73z"
   id="path1550" />
	</g><g
     id="g1556">
		<path
   class="st0"
   d="M686.58,509.97l-2.82-0.09l0.34-10.1l2.82,0.09L686.58,509.97z M687.06,495.54l-0.08,2.22l-2.82-0.09    l0.08-2.22L687.06,495.54z"
   id="path1554" />
	</g><g
     id="g1560">
		<path
   class="st0"
   d="M688.53,499.94l1.14,0.07l0.09-1.6l2.89-1.09l-0.17,2.86l1.46,0.09l-0.1,1.74l-1.46-0.09l-0.32,5.39    c-0.04,0.76-0.09,1.26,0.83,1.31c0.18,0.01,0.36,0.02,0.5-0.01l-0.1,1.74c-0.38,0.02-0.79,0.05-1.46,0.01    c-2.44-0.14-2.66-1.78-2.62-2.4l0.36-6.21l-1.14-0.07L688.53,499.94z"
   id="path1558" />
	</g><g
     id="g1564">
		<path
   class="st0"
   d="M697.67,510.73l-2.81-0.27l0.97-10.06l2.81,0.27L697.67,510.73z M699.06,496.35l-0.21,2.21l-2.81-0.27    l0.21-2.21L699.06,496.35z"
   id="path1562" />
	</g><g
     id="g1568">
		<path
   class="st0"
   d="M700.62,505.8c0.37-2.74,1.08-5.02,4.77-4.52c3.69,0.5,3.77,2.89,3.4,5.63c-0.42,3.13-1.2,5.27-4.8,4.78    C700.37,511.2,700.19,508.93,700.62,505.8z M706.01,506.37c0.28-2.08,0.32-3.15-0.87-3.31c-1.19-0.16-1.43,0.88-1.71,2.96    c-0.41,3.05-0.24,3.74,0.79,3.88C705.25,510.04,705.6,509.42,706.01,506.37z"
   id="path1566" />
	</g><g
     id="g1572">
		<path
   class="st0"
   d="M714.5,503.95l0.04,0.01c0.36-0.4,0.75-0.63,1.16-0.74c0.43-0.12,0.9-0.12,1.41-0.02    c1.32,0.25,2.33,1.25,2.07,2.63l-1.49,7.96l-2.77-0.52l1.28-6.84c0.17-0.89,0.14-1.6-0.75-1.77c-0.89-0.17-1.17,0.49-1.34,1.38    l-1.28,6.84l-2.77-0.52l1.86-9.93l2.77,0.52L714.5,503.95z"
   id="path1570" />
	</g></a>
	
	
	
	
	
	
	<a
   id="a50731"
   xlink:href="/child-poverty"
   target="blank"
   xlink:title="Poverty and Social Protection"
   xlink:show="Poverty and Social Protection"><g
     id="g1576">
		<path
   class="st3"
   d="M829.15,562.23l3.53,4.14c1.79,2.1,1.22,4.01-0.79,5.73c-1.25,1.07-3.54,2.39-5.84-0.3l-1.46-1.7l-4.47,3.82    l-1.96-2.3L829.15,562.23z M826.29,568.64l1.09,1.28c0.58,0.68,1.73,0.52,2.46-0.1c0.9-0.77,1.45-1.66,0.57-2.69l-0.99-1.16    L826.29,568.64z"
   id="path1574" />
	</g><g
     id="g1580">
		<path
   class="st3"
   d="M829.19,576.63c2.19-1.69,4.3-2.81,6.57,0.13s0.65,4.71-1.54,6.39c-2.5,1.93-4.55,2.91-6.78,0.03    C825.23,580.3,826.69,578.56,829.19,576.63z M832.63,580.83c1.66-1.28,2.44-2.01,1.71-2.96c-0.73-0.95-1.63-0.38-3.3,0.9    c-2.44,1.88-2.8,2.49-2.17,3.31C829.51,582.91,830.19,582.71,832.63,580.83z"
   id="path1578" />
	</g><g
     id="g1584">
		<path
   class="st3"
   d="M839.01,581.41l1.63,2.35l-5.41,5.5l0.02,0.03l7.07-3.12l1.58,2.27l-9.88,3.49l-1.77-2.54L839.01,581.41z"
   id="path1582" />
	</g><g
     id="g1588">
		<path
   class="st3"
   d="M841.54,595.06c-1.02,0.64-2.52,1.63-1.86,2.68c0.53,0.85,1.45,0.51,2.16,0.06l1.52,2.42    c-0.95,0.55-1.91,0.72-2.79,0.47c-0.88-0.23-1.71-0.89-2.41-2.01c-1.93-3.08-0.3-4.67,2.37-6.35c2.34-1.47,4.55-2.38,6.53,0.77    c2.02,3.22,0.16,4.88-2.65,6.52L841.54,595.06z M844.25,596.41c0.83-0.52,2.04-1.23,1.33-2.37c-0.69-1.1-1.97-0.28-2.7,0.18    L844.25,596.41z"
   id="path1586" />
	</g><g
     id="g1592">
		<path
   class="st3"
   d="M851.6,601.23l-1.13,0.64l0.02,0.03c1.27-0.11,2.03,0.56,2.59,1.55l-2.2,1.23c-1.07-2.24-2.35-1.57-3.22-1.08    l-4.8,2.69l-1.38-2.46l8.81-4.94L851.6,601.23z"
   id="path1590" />
	</g><g
     id="g1596">
		<path
   class="st3"
   d="M853.17,604.04l0.52,1.01l1.42-0.73l2.41,1.93l-2.54,1.31l0.67,1.3l-1.55,0.8l-0.67-1.3l-4.8,2.47    c-0.68,0.35-1.13,0.56-0.71,1.38c0.08,0.16,0.17,0.32,0.26,0.43l-1.55,0.79c-0.21-0.32-0.45-0.65-0.76-1.25    c-1.12-2.17,0.18-3.2,0.73-3.48l5.53-2.84l-0.52-1.01L853.17,604.04z"
   id="path1594" />
	</g><g
     id="g1600">
		<path
   class="st3"
   d="M847.95,616.27l8.05-6.81l1.19,2.54l-5.82,4.32l0.02,0.04l7.08-1.64l1.15,2.46l-14.26,2.38l-1.26-2.68    L847.95,616.27z"
   id="path1598" />
	</g></a>
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a26982"
   xlink:href="/child-protection"
   target="blank"
   xlink:title="Family environment and protection from violence and harmful practices"
   xlink:show="Family environment and protection from violence and harmful practices"><g
     id="g1604">
		<path
   class="st1"
   d="M479.36,636.4l13.76,4.4l-2.29,7.14l-2.11-0.68l1.37-4.27l-3.53-1.13l-1.3,4.08l-2.11-0.68l1.3-4.08l-6-1.92    L479.36,636.4z"
   id="path1602" />
	</g><g
     id="g1608">
		<path
   class="st1"
   d="M476.44,652.66c-0.6-0.17-1.24-0.26-1.85-0.37l0.71-2.52l1.32,0.25l0.01-0.04c-0.84-0.86-1.1-1.78-0.77-2.96    c0.53-1.89,2.13-2.19,3.83-1.71c3.22,0.9,2.66,3.42,1.91,5.94l0.75,0.21c0.83,0.23,1.46,0.28,1.73-0.7    c0.26-0.94-0.43-1.22-1.2-1.44l0.75-2.66c1.17,0.33,1.82,0.91,2.09,1.67c0.29,0.75,0.21,1.68-0.08,2.72    c-0.97,3.45-2.57,3.48-4.34,2.98L476.44,652.66z M479.06,647.99c-0.69-0.19-1.57-0.32-1.82,0.57c-0.45,1.6,1.78,1.95,2.84,2.25    C480.4,649.45,480.79,648.48,479.06,647.99z"
   id="path1606" />
	</g><g
     id="g1612">
		<path
   class="st1"
   d="M482.41,658.88l-0.01,0.04c0.76,0.74,0.92,1.55,0.69,2.58c-0.21,0.98-0.85,1.66-1.73,1.94    c0.72,0.83,0.94,1.7,0.7,2.83c-0.28,1.31-1.31,2.29-2.68,2l-7.92-1.71l0.59-2.76l6.81,1.46c0.88,0.19,1.6,0.18,1.79-0.7    c0.19-0.88-0.46-1.18-1.34-1.37l-6.81-1.47l0.58-2.7l6.81,1.47c0.88,0.19,1.6,0.18,1.79-0.7c0.19-0.88-0.46-1.18-1.34-1.37    l-6.81-1.47l0.59-2.76l9.88,2.13l-0.59,2.76L482.41,658.88z"
   id="path1610" />
	</g><g
     id="g1616">
		<path
   class="st1"
   d="M470.78,671.62l0.42-2.79l9.99,1.51l-0.42,2.79L470.78,671.62z M485.06,673.78l-2.2-0.33l0.42-2.79l2.2,0.33    L485.06,673.78z"
   id="path1614" />
	</g><g
     id="g1620">
		<path
   class="st1"
   d="M484.35,678.93l-14.33-1.81l0.35-2.8l14.33,1.81L484.35,678.93z"
   id="path1618" />
	</g><g
     id="g1624">
		<path
   class="st1"
   d="M469.46,681.39l10.38-1.84l-0.25,2.79l-7.2,0.81l0,0.04l6.94,2.14l-0.24,2.71l-13.53-5.11l0.26-2.95    L469.46,681.39z"
   id="path1622" />
	</g><g
     id="g1628">
		<path
   class="st1"
   d="M468.73,693.01l14.44,0.36l-0.2,7.88l-2.22-0.05l0.12-4.86l-3.56-0.09l-0.11,4.48l-2.22-0.06l0.11-4.48    l-4.22-0.1l-0.12,5.02l-2.22-0.06L468.73,693.01z"
   id="path1626" />
	</g><g
     id="g1632">
		<path
   class="st1"
   d="M477.75,705.47l0,0.04c0.47,0.27,0.78,0.6,0.97,0.98c0.21,0.39,0.3,0.85,0.32,1.37    c0.04,1.34-0.73,2.54-2.13,2.58l-8.1,0.21l-0.07-2.82l6.96-0.18c0.9-0.02,1.6-0.2,1.57-1.1c-0.02-0.9-0.73-1.04-1.63-1.02    l-6.96,0.18l-0.07-2.82l10.1-0.26l0.07,2.82L477.75,705.47z"
   id="path1630" />
	</g><g
     id="g1636">
		<path
   class="st1"
   d="M478.97,711.14l0.22,2.85l-7.45,2l0,0.04l7.67,0.89l0.21,2.75l-10.29-1.99l-0.24-3.09L478.97,711.14z"
   id="path1634" />
	</g><g
     id="g1640">
		<path
   class="st1"
   d="M470.11,724.75l-0.33-2.8l10.03-1.17l0.33,2.8L470.11,724.75z M484.45,723.08l-2.21,0.26l-0.33-2.8l2.21-0.26    L484.45,723.08z"
   id="path1638" />
	</g><g
     id="g1644">
		<path
   class="st1"
   d="M480.82,728.32l-1.28,0.2l0.01,0.04c1.23,0.33,1.71,1.23,1.89,2.36l-2.49,0.39    c-0.22-2.48-1.65-2.29-2.64-2.14l-5.44,0.85l-0.44-2.79l9.98-1.56L480.82,728.32z"
   id="path1642" />
	</g><g
     id="g1648">
		<path
   class="st1"
   d="M476.47,732.59c2.71-0.53,5.1-0.59,5.82,3.06c0.72,3.65-1.52,4.5-4.23,5.03c-3.1,0.61-5.37,0.57-6.08-3    S473.37,733.2,476.47,732.59z M477.68,737.88c2.06-0.4,3.08-0.71,2.85-1.89c-0.23-1.18-1.29-1.07-3.35-0.67    c-3.02,0.59-3.62,0.98-3.42,2S474.65,738.47,477.68,737.88z"
   id="path1646" />
	</g><g
     id="g1652">
		<path
   class="st1"
   d="M482.9,744.14l0.01,0.04c0.51,0.16,0.89,0.42,1.16,0.74c0.29,0.34,0.48,0.77,0.61,1.27    c0.33,1.3-0.16,2.64-1.52,2.98l-7.86,1.98l-0.69-2.74l6.75-1.7c0.87-0.22,1.51-0.55,1.29-1.42c-0.22-0.87-0.94-0.86-1.81-0.64    l-6.75,1.7l-0.69-2.73l9.8-2.46l0.69,2.73L482.9,744.14z"
   id="path1650" />
	</g><g
     id="g1656">
		<path
   class="st1"
   d="M485.25,753.02l0.01,0.04c1.03,0.26,1.57,0.88,1.89,1.89c0.31,0.95,0.1,1.86-0.53,2.54    c1.04,0.36,1.67,1,2.02,2.1c0.41,1.28,0.01,2.64-1.32,3.07l-7.71,2.49l-0.87-2.68l6.63-2.14c0.86-0.28,1.47-0.64,1.2-1.5    c-0.28-0.86-0.99-0.79-1.85-0.52l-6.62,2.14l-0.85-2.63l6.63-2.14c0.86-0.28,1.47-0.64,1.2-1.5c-0.28-0.86-0.99-0.79-1.85-0.52    l-6.63,2.14l-0.87-2.68l9.61-3.1l0.87,2.68L485.25,753.02z"
   id="path1654" />
	</g><g
     id="g1660">
		<path
   class="st1"
   d="M485.57,767.84c-1.12,0.43-2.79,1.11-2.35,2.27c0.36,0.93,1.32,0.78,2.11,0.48l1.02,2.67    c-1.04,0.36-2.01,0.34-2.83-0.08c-0.82-0.39-1.51-1.2-1.98-2.43c-1.3-3.4,0.61-4.64,3.56-5.77c2.58-0.98,4.93-1.45,6.25,2.03    c1.35,3.55-0.79,4.82-3.86,5.88L485.57,767.84z M487.97,769.69c0.92-0.35,2.24-0.81,1.76-2.06c-0.46-1.21-1.88-0.65-2.68-0.35    L487.97,769.69z"
   id="path1658" />
	</g><g
     id="g1664">
		<path
   class="st1"
   d="M493.44,775.25l0.02,0.04c0.53,0.07,0.95,0.26,1.26,0.54c0.34,0.28,0.6,0.67,0.81,1.15    c0.54,1.22,0.29,2.63-0.99,3.2l-7.41,3.28l-1.14-2.58l6.37-2.82c0.82-0.36,1.4-0.79,1.03-1.62c-0.36-0.82-1.07-0.69-1.89-0.32    l-6.37,2.82l-1.14-2.58l9.24-4.09l1.14,2.58L493.44,775.25z"
   id="path1662" />
	</g><g
     id="g1668">
		<path
   class="st1"
   d="M496.72,779.98l0.5,1.02l1.44-0.71l2.37,1.98l-2.57,1.26l0.64,1.31l-1.56,0.77l-0.64-1.31l-4.85,2.38    c-0.68,0.33-1.14,0.54-0.73,1.36c0.08,0.16,0.16,0.32,0.26,0.43l-1.56,0.77c-0.2-0.32-0.43-0.66-0.73-1.27    c-1.08-2.19,0.24-3.19,0.79-3.46l5.59-2.74l-0.5-1.02L496.72,779.98z"
   id="path1666" />
	</g><g
     id="g1672">
		<path
   class="st1"
   d="M498.17,800.05c-0.54,0.31-1.05,0.7-1.56,1.06l-1.3-2.27l1.1-0.77l-0.02-0.04c-1.2,0-2.04-0.46-2.65-1.52    c-0.98-1.7-0.07-3.05,1.46-3.93c2.9-1.66,4.3,0.5,5.57,2.8l0.68-0.39c0.75-0.43,1.22-0.84,0.72-1.73    c-0.49-0.85-1.17-0.55-1.86-0.15l-1.37-2.39c1.06-0.61,1.92-0.67,2.65-0.32c0.73,0.32,1.35,1.02,1.89,1.96    c1.78,3.11,0.68,4.27-0.92,5.19L498.17,800.05z M496.67,794.91c-0.62,0.36-1.33,0.9-0.87,1.7c0.83,1.44,2.64,0.1,3.59-0.45    C498.65,794.97,498.23,794.01,496.67,794.91z"
   id="path1670" />
	</g><g
     id="g1676">
		<path
   class="st1"
   d="M506.93,800.42l0.02,0.03c0.54-0.01,0.98,0.11,1.33,0.33c0.38,0.23,0.7,0.57,0.98,1.01    c0.73,1.13,0.69,2.55-0.48,3.31l-6.81,4.39l-1.53-2.37l5.85-3.77c0.76-0.49,1.26-1,0.77-1.76s-1.16-0.51-1.92-0.02l-5.85,3.77    l-1.53-2.37l8.49-5.48l1.53,2.37L506.93,800.42z"
   id="path1674" />
	</g><g
     id="g1680">
		<path
   class="st1"
   d="M506.22,815.43l0.91-0.66l-0.02-0.03c-1.1,0.15-1.83-0.28-2.46-1.16c-1.71-2.37,0.98-4.18,2.67-5.4    c1.66-1.19,4.16-3.09,5.82-0.79c0.6,0.83,0.76,1.57,0.4,2.54l0.02,0.03l4.3-3.1l1.65,2.29l-11.72,8.44L506.22,815.43z     M510.31,812.31c1.64-1.18,2.79-1.98,2.11-2.92c-0.71-0.99-1.84-0.16-3.48,1.03c-2.06,1.49-2.82,2.25-2.22,3.08    C507.28,814.27,508.25,813.8,510.31,812.31z"
   id="path1678" />
	</g><g
     id="g1684">
		<path
   class="st1"
   d="M523.08,813.71l3.51,4.16c1.78,2.11,1.19,4.02-0.83,5.72c-1.25,1.06-3.55,2.37-5.83-0.34l-1.44-1.71    l-4.5,3.79l-1.95-2.31L523.08,813.71z M520.18,820.1l1.08,1.29c0.58,0.69,1.73,0.53,2.46-0.09c0.9-0.76,1.46-1.65,0.58-2.69    l-0.98-1.16L520.18,820.1z"
   id="path1682" />
	</g><g
     id="g1688">
		<path
   class="st1"
   d="M528.41,826.37l-0.95,0.89l0.03,0.03c1.2-0.41,2.11,0.06,2.89,0.89l-1.84,1.72    c-1.58-1.92-2.66-0.97-3.39-0.29l-4.02,3.75l-1.92-2.06l7.38-6.89L528.41,826.37z"
   id="path1686" />
	</g><g
     id="g1692">
		<path
   class="st1"
   d="M527.24,832.31c1.95-1.96,3.89-3.35,6.53-0.73c2.64,2.62,1.26,4.58-0.69,6.54c-2.23,2.24-4.13,3.48-6.72,0.91    C523.78,836.47,525.01,834.55,527.24,832.31z M531.19,836.02c1.48-1.49,2.16-2.31,1.31-3.16c-0.85-0.85-1.67-0.16-3.15,1.33    c-2.17,2.18-2.45,2.84-1.71,3.57C528.37,838.49,529.02,838.21,531.19,836.02z"
   id="path1690" />
	</g><g
     id="g1696">
		<path
   class="st1"
   d="M536.94,834.92l0.84,0.77l1.08-1.18l2.93,0.99l-1.94,2.1l1.07,0.99l-1.18,1.28l-1.07-0.99l-3.66,3.97    c-0.52,0.56-0.87,0.91-0.19,1.54c0.13,0.12,0.26,0.24,0.4,0.31l-1.18,1.28c-0.31-0.23-0.64-0.46-1.14-0.92    c-1.79-1.65-0.93-3.06-0.51-3.52l4.22-4.57l-0.84-0.77L536.94,834.92z"
   id="path1694" />
	</g><g
     id="g1700">
		<path
   class="st1"
   d="M539.97,845.02c-0.77,0.92-1.89,2.33-0.94,3.12c0.77,0.64,1.54,0.03,2.07-0.61l2.2,1.83    c-0.73,0.82-1.59,1.28-2.51,1.32c-0.9,0.05-1.9-0.31-2.92-1.16c-2.79-2.33-1.74-4.34,0.28-6.77c1.77-2.12,3.59-3.67,6.45-1.29    c2.92,2.44,1.66,4.59-0.49,7.02L539.97,845.02z M542.97,845.46c0.63-0.75,1.56-1.8,0.53-2.66c-1-0.83-1.96,0.35-2.51,1.01    L542.97,845.46z"
   id="path1698" />
	</g><g
     id="g1704">
		<path
   class="st1"
   d="M550.74,851.18c0.9-1.2,0.9-1.83,0.2-2.36c-0.96-0.72-1.68,0.06-2.94,1.74c-1.86,2.46-2.05,3.14-1.22,3.77    c0.7,0.53,1.52,0.14,2.32-0.91l2.25,1.7c-1.65,2.19-3.54,2.24-5.65,0.65c-2.91-2.19-1.95-4.25-0.05-6.78    c1.66-2.2,3.4-3.85,6.38-1.61c2.08,1.57,2.56,3.38,0.97,5.49L550.74,851.18z"
   id="path1702" />
	</g><g
     id="g1708">
		<path
   class="st1"
   d="M555.59,850.31l0.93,0.65l0.92-1.31l3.03,0.58l-1.64,2.35l1.2,0.84l-1,1.43l-1.2-0.84l-3.09,4.43    c-0.44,0.62-0.74,1.02,0.02,1.55c0.15,0.1,0.3,0.21,0.43,0.25l-1,1.43c-0.33-0.18-0.7-0.37-1.25-0.75c-2-1.4-1.33-2.91-0.98-3.42    l3.56-5.1l-0.93-0.65L555.59,850.31z"
   id="path1706" />
	</g><g
     id="g1712">
		<path
   class="st1"
   d="M557.87,864.09l-2.35-1.56l5.58-8.42l2.35,1.56L557.87,864.09z M565.85,852.05l-1.23,1.85l-2.35-1.56    l1.23-1.85L565.85,852.05z"
   id="path1710" />
	</g><g
     id="g1716">
		<path
   class="st1"
   d="M562.47,860.91c1.44-2.35,3.02-4.16,6.19-2.21s2.28,4.17,0.84,6.52c-1.65,2.7-3.22,4.34-6.33,2.44    C560.07,865.75,560.82,863.6,562.47,860.91z M567.18,863.6c1.1-1.79,1.56-2.75,0.54-3.38s-1.66,0.23-2.76,2.02    c-1.61,2.63-1.73,3.33-0.85,3.87S565.57,866.23,567.18,863.6z"
   id="path1714" />
	</g><g
     id="g1720">
		<path
   class="st1"
   d="M575.29,863.93l0.04,0.02c0.46-0.27,0.9-0.38,1.33-0.36c0.45,0.01,0.89,0.16,1.35,0.4    c1.18,0.63,1.85,1.89,1.19,3.13l-3.81,7.15l-2.49-1.33l3.27-6.14c0.42-0.79,0.61-1.49-0.18-1.91c-0.79-0.42-1.27,0.12-1.69,0.91    l-3.27,6.14l-2.49-1.33l4.75-8.92l2.49,1.33L575.29,863.93z"
   id="path1718" />
	</g></a>
	
	
	
	
	
	
	
	
	<a
   id="a31728"
   xlink:href="/child-education"
   target="blank"
   xlink:title="Education, Leisure, and Culture"
   xlink:show="Education, Leisure, and Culture"><g
     id="g1724">
		<path
   class="st4"
   d="M636.4,894.52l2.09-14.29l7.8,1.14l-0.32,2.2l-4.81-0.7l-0.52,3.52l4.43,0.65l-0.32,2.2l-4.43-0.65    l-0.61,4.18l4.97,0.73l-0.32,2.2L636.4,894.52z"
   id="path1722" />
	</g><g
     id="g1728">
		<path
   class="st4"
   d="M651.17,896.41l0.11-1.12l-0.04,0c-0.61,0.92-1.42,1.19-2.5,1.08c-2.91-0.28-2.49-3.5-2.29-5.57    c0.2-2.03,0.42-5.16,3.25-4.89c1.02,0.1,1.68,0.47,2.18,1.38l0.04,0l0.52-5.28l2.81,0.28l-1.41,14.37L651.17,896.41z     M651.53,891.28c0.2-2.01,0.35-3.4-0.8-3.52c-1.21-0.12-1.33,1.28-1.53,3.29c-0.25,2.53-0.17,3.6,0.84,3.7    C651,894.85,651.28,893.81,651.53,891.28z"
   id="path1726" />
	</g><g
     id="g1732">
		<path
   class="st4"
   d="M661.09,896.07l-0.04,0c-0.3,0.43-0.64,0.73-1.04,0.89c-0.41,0.18-0.85,0.24-1.39,0.21    c-1.34-0.07-2.48-0.92-2.41-2.32l0.4-8.09l2.82,0.14l-0.35,6.99c-0.04,0.9,0.08,1.57,0.98,1.61c0.9,0.04,1.09-0.61,1.14-1.51    l0.35-6.99l2.82,0.14l-0.4,8.09c-0.03,0.66-0.03,1.34,0,2l-2.92-0.15L661.09,896.07z"
   id="path1730" />
	</g><g
     id="g1736">
		<path
   class="st4"
   d="M671.39,891.03c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.31,3.16c-0.01,3.08,0.25,3.74,1.29,3.74    c0.88,0,1.3-0.8,1.3-2.12l2.82,0.01c0,2.74-1.49,3.92-4.13,3.91c-3.64-0.01-4.12-2.23-4.11-5.39c0.01-2.76,0.41-5.12,4.13-5.11    c2.6,0,4.08,1.17,4.07,3.81L671.39,891.03z"
   id="path1734" />
	</g><g
     id="g1740">
		<path
   class="st4"
   d="M683.67,895.09c0.03,0.62,0.14,1.25,0.23,1.87l-2.62,0.12l-0.18-1.33l-0.04,0c-0.55,1.07-1.35,1.6-2.57,1.66    c-1.96,0.09-2.75-1.34-2.83-3.09c-0.15-3.34,2.42-3.6,5.04-3.68l-0.04-0.78c-0.04-0.86-0.19-1.47-1.21-1.43    c-0.98,0.05-1.02,0.79-0.99,1.59l-2.76,0.13c-0.06-1.22,0.29-2.02,0.93-2.51c0.62-0.51,1.53-0.73,2.61-0.78    c3.58-0.17,4.11,1.35,4.19,3.19L683.67,895.09z M678.42,894.07c0.03,0.72,0.19,1.59,1.11,1.55c1.66-0.08,1.3-2.3,1.25-3.4    C679.38,892.34,678.34,892.27,678.42,894.07z"
   id="path1738" />
	</g><g
     id="g1744">
		<path
   class="st4"
   d="M684.12,886.82l1.14-0.09l-0.13-1.59l2.71-1.49l0.23,2.85l1.46-0.12l0.14,1.74l-1.46,0.12l0.44,5.38    c0.06,0.76,0.08,1.26,1,1.18c0.18-0.01,0.36-0.03,0.5-0.08l0.14,1.73c-0.38,0.07-0.77,0.16-1.45,0.22c-2.43,0.2-2.88-1.39-2.94-2    l-0.51-6.2l-1.14,0.09L684.12,886.82z"
   id="path1742" />
	</g><g
     id="g1748">
		<path
   class="st4"
   d="M693.14,881.65l0.24,2.21l-2.8,0.3l-0.24-2.21L693.14,881.65z M694.67,896.01l-2.8,0.3l-1.07-10.05l2.8-0.3    L694.67,896.01z"
   id="path1746" />
	</g><g
     id="g1752">
		<path
   class="st4"
   d="M696.19,890.66c-0.39-2.73-0.33-5.13,3.35-5.66c3.68-0.53,4.42,1.75,4.81,4.48c0.45,3.13,0.29,5.39-3.31,5.91    C697.43,895.92,696.64,893.79,696.19,890.66z M701.53,889.73c-0.3-2.08-0.55-3.12-1.74-2.94c-1.19,0.17-1.14,1.23-0.84,3.31    c0.44,3.05,0.79,3.67,1.82,3.52C701.81,893.47,701.97,892.78,701.53,889.73z"
   id="path1750" />
	</g><g
     id="g1756">
		<path
   class="st4"
   d="M708.1,884.84l0.04-0.01c0.19-0.5,0.46-0.86,0.8-1.11c0.35-0.27,0.79-0.44,1.3-0.54    c1.32-0.25,2.63,0.31,2.89,1.68l1.54,7.95l-2.77,0.54l-1.32-6.83c-0.17-0.88-0.46-1.54-1.34-1.37c-0.88,0.17-0.91,0.89-0.74,1.77    l1.32,6.83l-2.77,0.54l-1.92-9.92l2.77-0.54L708.1,884.84z"
   id="path1754" />
	</g></a>
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a63680"
   xlink:title="Participation and Civil Rights"
   xlink:show="Participation and Civil Rights"
   target="blank"
   xlink:href="/child-participation"><g
     id="g1760">
		<path
   class="st2"
   d="M774.9,853.85l4.58-2.93c2.33-1.49,4.14-0.65,5.56,1.57c0.88,1.38,1.88,3.83-1.1,5.74l-1.89,1.21l3.17,4.96    l-2.54,1.63L774.9,853.85z M780.86,857.56l1.42-0.91c0.76-0.48,0.75-1.65,0.24-2.45c-0.64-0.99-1.44-1.66-2.59-0.93l-1.28,0.82    L780.86,857.56z"
   id="path1758" />
	</g><g
     id="g1764">
		<path
   class="st2"
   d="M797.05,854.09c0.36,0.51,0.79,0.98,1.2,1.45l-2.14,1.52l-0.87-1.02l-0.03,0.02c0.11,1.2-0.27,2.08-1.26,2.78    c-1.6,1.13-3.03,0.36-4.05-1.08c-1.93-2.72,0.09-4.33,2.25-5.82l-0.45-0.64c-0.5-0.7-0.95-1.14-1.79-0.55    c-0.8,0.57-0.44,1.22,0.03,1.87l-2.25,1.6c-0.71-1-0.85-1.85-0.58-2.61c0.24-0.76,0.89-1.44,1.77-2.07    c2.92-2.07,4.19-1.08,5.25,0.42L797.05,854.09z M792.08,856.08c0.42,0.59,1.02,1.24,1.77,0.7c1.35-0.96-0.16-2.64-0.79-3.54    C791.95,854.1,791.04,854.61,792.08,856.08z"
   id="path1762" />
	</g><g
     id="g1768">
		<path
   class="st2"
   d="M795.98,844.56l0.79,1.03l0.03-0.02c-0.29-1.24,0.26-2.09,1.17-2.78l1.53,2c-2.07,1.38-1.22,2.55-0.62,3.34    l3.34,4.37l-2.24,1.71l-6.14-8.02L795.98,844.56z"
   id="path1766" />
	</g><g
     id="g1772">
		<path
   class="st2"
   d="M797.96,843.07l0.88-0.73l-1.02-1.24l1.38-2.77l1.82,2.21l1.13-0.93l1.11,1.34l-1.13,0.93l3.43,4.17    c0.48,0.59,0.79,0.99,1.5,0.4c0.14-0.12,0.28-0.23,0.36-0.35l1.11,1.34c-0.27,0.27-0.54,0.57-1.06,1.01    c-1.88,1.55-3.16,0.5-3.55,0.03l-3.96-4.8l-0.88,0.73L797.96,843.07z"
   id="path1770" />
	</g><g
     id="g1776">
		<path
   class="st2"
   d="M802.41,833.67l1.45,1.68l-2.13,1.84l-1.45-1.68L802.41,833.67z M811.86,844.59l-2.13,1.84l-6.61-7.64    l2.13-1.84L811.86,844.59z"
   id="path1774" />
	</g><g
     id="g1780">
		<path
   class="st2"
   d="M813.1,834.71c-1.02-1.1-1.64-1.21-2.29-0.61c-0.88,0.82-0.23,1.66,1.2,3.2c2.1,2.26,2.74,2.56,3.5,1.85    c0.65-0.6,0.41-1.47-0.49-2.44l2.07-1.92c1.87,2.01,1.58,3.88-0.35,5.68c-2.67,2.48-4.53,1.18-6.68-1.14    c-1.88-2.02-3.19-4.02-0.47-6.56c1.91-1.77,3.78-1.93,5.58,0.01L813.1,834.71z"
   id="path1778" />
	</g><g
     id="g1784">
		<path
   class="st2"
   d="M813.01,823.72l1.57,1.57l-2,1.99l-1.57-1.57L813.01,823.72z M823.21,833.94l-2,1.99l-7.14-7.15l2-1.99    L823.21,833.94z"
   id="path1782" />
	</g><g
     id="g1788">
		<path
   class="st2"
   d="M819.4,823.31l0.82,0.76l0.03-0.03c-0.36-1.05-0.08-1.85,0.66-2.64c1.99-2.14,4.29,0.15,5.81,1.57    c1.49,1.39,3.84,3.48,1.91,5.55c-0.7,0.75-1.39,1.05-2.42,0.89l-0.03,0.03l3.88,3.62l-1.92,2.06l-10.56-9.85L819.4,823.31z     M824.72,824.88c-1.48-1.38-2.49-2.35-3.32-1.46c-0.79,0.85,0.25,1.79,1.72,3.17c1.86,1.73,2.76,2.32,3.41,1.62    C827.23,827.47,826.57,826.62,824.72,824.88z"
   id="path1786" />
	</g><g
     id="g1792">
		<path
   class="st2"
   d="M835.26,817.75c0.47,0.4,1.01,0.75,1.53,1.11l-1.69,2l-1.1-0.77l-0.03,0.03c0.4,1.13,0.26,2.08-0.53,3.01    c-1.27,1.5-2.85,1.1-4.19-0.04c-2.55-2.16-0.99-4.22,0.74-6.19l-0.59-0.5c-0.66-0.56-1.21-0.87-1.87-0.09    c-0.63,0.75-0.12,1.29,0.49,1.8l-1.79,2.11c-0.93-0.79-1.28-1.58-1.2-2.38c0.05-0.8,0.5-1.62,1.2-2.44    c2.31-2.73,3.79-2.09,5.19-0.9L835.26,817.75z M830.93,820.9c0.55,0.47,1.3,0.94,1.89,0.24c1.07-1.27-0.8-2.52-1.64-3.23    C830.32,819.02,829.56,819.74,830.93,820.9z"
   id="path1790" />
	</g><g
     id="g1796">
		<path
   class="st2"
   d="M829.48,811.75l0.71-0.9l-1.26-0.99l0.76-3l2.25,1.77l0.9-1.15l1.37,1.08l-0.9,1.15l4.24,3.34    c0.6,0.47,0.98,0.8,1.55,0.07c0.11-0.14,0.22-0.28,0.28-0.42l1.37,1.08c-0.2,0.32-0.41,0.67-0.83,1.21    c-1.51,1.92-2.98,1.17-3.47,0.78l-4.89-3.85l-0.71,0.9L829.48,811.75z"
   id="path1794" />
	</g><g
     id="g1800">
		<path
   class="st2"
   d="M831.69,801.72l1.79,1.31l-1.67,2.28l-1.79-1.31L831.69,801.72z M843.35,810.26l-1.67,2.28l-8.15-5.97    l1.67-2.28L843.35,810.26z"
   id="path1798" />
	</g><g
     id="g1804">
		<path
   class="st2"
   d="M840.43,805.55c-2.28-1.55-4.01-3.21-1.92-6.29c2.09-3.08,4.27-2.08,6.55-0.53c2.61,1.78,4.18,3.42,2.14,6.43    S843.05,807.32,840.43,805.55z M843.35,800.97c-1.74-1.18-2.67-1.69-3.35-0.7c-0.67,0.99,0.15,1.67,1.88,2.85    c2.55,1.73,3.24,1.88,3.83,1.02C846.29,803.29,845.89,802.7,843.35,800.97z"
   id="path1802" />
	</g><g
     id="g1808">
		<path
   class="st2"
   d="M844.16,792.82l0.02-0.03c-0.25-0.48-0.32-0.93-0.28-1.34c0.04-0.45,0.21-0.88,0.48-1.32    c0.7-1.14,2-1.73,3.19-1l6.91,4.23l-1.47,2.41l-5.94-3.63c-0.77-0.47-1.45-0.7-1.92,0.07s0.04,1.27,0.81,1.74l5.94,3.63    l-1.47,2.41l-8.62-5.27l1.47-2.41L844.16,792.82z"
   id="path1806" />
	</g><g
     id="g1812">
		<path
   class="st2"
   d="M859.67,779.89c0.55,0.29,1.16,0.51,1.73,0.74l-1.21,2.33l-1.24-0.51l-0.02,0.04    c0.65,1.01,0.71,1.97,0.15,3.05c-0.9,1.74-2.53,1.71-4.09,0.9c-2.97-1.54-1.9-3.89-0.66-6.2l-0.69-0.36    c-0.76-0.4-1.37-0.57-1.84,0.33c-0.45,0.87,0.17,1.28,0.88,1.65l-1.27,2.45c-1.08-0.56-1.6-1.26-1.71-2.05    c-0.13-0.79,0.13-1.69,0.63-2.65c1.65-3.18,3.23-2.88,4.86-2.04L859.67,779.89z M856.16,783.93c0.64,0.33,1.48,0.63,1.9-0.19    c0.76-1.47-1.35-2.27-2.32-2.78C855.15,782.23,854.56,783.1,856.16,783.93z"
   id="path1810" />
	</g><g
     id="g1816">
		<path
   class="st2"
   d="M855.33,772.32l0.02-0.04c-0.3-0.45-0.43-0.88-0.44-1.3c-0.02-0.45,0.1-0.9,0.32-1.37    c0.56-1.22,1.78-1.96,3.05-1.37l7.36,3.38l-1.18,2.56l-6.33-2.9c-0.82-0.38-1.52-0.52-1.9,0.3c-0.38,0.82,0.19,1.25,1.01,1.63    l6.33,2.9l-1.18,2.56l-9.18-4.21l1.18-2.56L855.33,772.32z"
   id="path1814" />
	</g><g
     id="g1820">
		<path
   class="st2"
   d="M868.43,764.89l-1.04-0.42l-0.02,0.04c0.72,0.85,0.74,1.7,0.34,2.7c-1.09,2.71-4.06,1.41-5.99,0.63    c-1.89-0.76-4.84-1.86-3.78-4.49c0.38-0.95,0.92-1.48,1.93-1.7l0.01-0.04l-4.92-1.98l1.05-2.62l13.4,5.39L868.43,764.89z     M863.61,763.11c-1.88-0.75-3.17-1.29-3.6-0.22c-0.46,1.13,0.85,1.64,2.73,2.39c2.36,0.95,3.41,1.18,3.79,0.23    C866.88,764.62,865.96,764.05,863.61,763.11z"
   id="path1818" />
	</g><g
     id="g1824">
		<path
   class="st2"
   d="M864.87,753.9c-3.64-1.17-7.11-2.27-5.59-7.02c0.94-2.93,2.94-3.6,5.85-2.54l-0.9,2.82    c-1.83-0.59-2.62-0.48-2.89,0.38c-0.52,1.62,0.94,2.32,4.46,3.44c3.53,1.13,5.12,1.41,5.64-0.21c0.43-1.33-1.31-1.83-2.38-2.21    l0.91-2.84c3.68,1.18,4.39,3.02,3.53,5.71C871.98,756.18,868.47,755.05,864.87,753.9z"
   id="path1822" />
	</g><g
     id="g1828">
		<path
   class="st2"
   d="M861.94,738.63l2.14,0.6l-0.76,2.72l-2.14-0.6L861.94,738.63z M875.85,742.52l-0.76,2.72l-9.73-2.73    l0.76-2.72L875.85,742.52z"
   id="path1826" />
	</g><g
     id="g1832">
		<path
   class="st2"
   d="M866.44,738.67l0.67-2.78l7.7,0.4l0.01-0.04l-7.02-3.22l0.65-2.68l9.17,5.07l-0.73,3.01L866.44,738.67z"
   id="path1830" />
	</g><g
     id="g1836">
		<path
   class="st2"
   d="M864.92,725.58l2.18,0.44l-0.56,2.76l-2.18-0.44L864.92,725.58z M879.07,728.44l-0.56,2.76l-9.9-2l0.56-2.76    L879.07,728.44z"
   id="path1834" />
	</g><g
     id="g1840">
		<path
   class="st2"
   d="M865.77,720.64l14.25,2.34l-0.46,2.78l-14.25-2.34L865.77,720.64z"
   id="path1838" />
	</g><g
     id="g1844">
		<path
   class="st2"
   d="M881.37,713.03l-0.3,3.01l-14.37-1.45l0.56-5.55c0.21-2.05,1.65-3.23,4.1-2.98c1.83,0.18,3.13,1.04,3.25,3.02    l0.04,0c0.15-0.65,0.5-2.58,3.09-2.32c0.92,0.09,3.63,0.3,4.25,0.09l-0.3,2.95c-0.92,0.31-1.88,0.13-2.82,0.04    c-1.71-0.17-3.15-0.48-3.38,1.83l-0.08,0.78L881.37,713.03z M873.21,712.21l0.13-1.33c0.12-1.19-1.04-1.65-1.96-1.75    c-1.37-0.14-1.95,0.39-2.04,1.34l-0.13,1.33L873.21,712.21z"
   id="path1842" />
	</g><g
     id="g1848">
		<path
   class="st2"
   d="M867.87,701.07l2.22,0.14l-0.18,2.81l-2.22-0.14L867.87,701.07z M882.29,701.97l-0.18,2.81l-10.08-0.63    l0.18-2.81L882.29,701.97z"
   id="path1846" />
	</g><g
     id="g1852">
		<path
   class="st2"
   d="M872.52,691.52l10.52,0.26c0.7,0.02,3.46,0.05,3.37,3.93c-0.05,2.1-0.64,3.89-3.1,3.88l0.07-2.76    c0.42,0.01,0.78-0.04,1.03-0.21c0.26-0.17,0.41-0.49,0.42-0.93c0.02-0.7-0.63-1.06-1.65-1.08l-1.94-0.05l0,0.04    c0.77,0.44,1.15,1.25,1.13,2.17c-0.08,3.1-2.91,2.89-5.19,2.83c-2.22-0.05-5.04-0.17-4.97-3.1c0.02-1,0.49-1.85,1.44-2.22l0-0.04    l-1.18-0.03L872.52,691.52z M880.64,695.71c0.03-1.02-1.03-1.19-3.17-1.24c-2.22-0.05-3.48,0.01-3.51,1.05    c-0.03,1.06,0.71,1.26,3.79,1.33C878.69,696.88,880.6,697.06,880.64,695.71z"
   id="path1850" />
	</g><g
     id="g1856">
		<path
   class="st2"
   d="M882.43,684.54l-6.96,0.18c-0.9,0.02-1.6,0.2-1.57,1.1s0.73,1.04,1.63,1.02l6.96-0.18l0.07,2.82l-14.44,0.38    l-0.07-2.82l5.36-0.14l0-0.04c-0.47-0.27-0.78-0.6-0.96-0.98c-0.21-0.39-0.3-0.85-0.32-1.37c-0.04-1.34,0.73-2.54,2.13-2.58    l8.1-0.21L882.43,684.54z"
   id="path1854" />
	</g><g
     id="g1860">
		<path
   class="st2"
   d="M872.2,681.41l-0.09-1.14l-1.6,0.12l-1.47-2.71l2.85-0.22l-0.11-1.46l1.74-0.13l0.11,1.46l5.39-0.42    c0.76-0.06,1.26-0.08,1.19-1c-0.01-0.18-0.03-0.36-0.08-0.5l1.74-0.13c0.07,0.38,0.16,0.77,0.21,1.45    c0.19,2.43-1.4,2.88-2.02,2.93l-6.2,0.48l0.09,1.14L872.2,681.41z"
   id="path1858" />
	</g><g
     id="g1864">
		<path
   class="st2"
   d="M878.29,672.08c0.46-0.03,0.9-0.09,1.2-0.26c0.3-0.19,0.43-0.51,0.37-1.07s-0.47-1-1.14-0.93    c-2.13,0.22-1.14,5.11-4.34,5.44c-2.17,0.22-3.05-1.86-3.24-3.67c-0.2-1.91,0.54-3.74,2.72-3.8l0.28,2.75    c-0.7,0.07-1.11,0.19-1.26,0.41c-0.16,0.2-0.17,0.44-0.14,0.74c0.06,0.62,0.5,0.91,1.17,0.84c1.59-0.17,1-5.09,4.22-5.42    c1.75-0.18,3.21,1.12,3.45,3.44c0.25,2.45-0.19,4.14-3.02,4.27L878.29,672.08z"
   id="path1862" />
	</g></a>
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a63610"><path
     class="st2"
     d="M896.09,752.56c-1.83,7.72-4.05,15.29-6.66,22.68c-2.29,6.52,0.74,13.71,7.02,16.58l45.22,20.65   c7.03,3.21,15.35-0.18,18.03-7.43c4.72-12.77,8.6-25.96,11.57-39.48c1.66-7.54-3.51-14.9-11.15-16l-49.12-7.06   C904.19,741.52,897.67,745.85,896.09,752.56L896.09,752.56z"
     id="path30" /><path
     class="st55"
     d="M917.92,782.65c-0.64-1.22-1.1-2.53-1.39-3.93c-0.16-0.79-0.93-1.3-1.72-1.14c-0.79,0.16-1.3,0.93-1.14,1.72   c0.4,1.93,1.08,3.73,2.03,5.36C916.21,783.77,916.99,783.06,917.92,782.65L917.92,782.65z"
     id="path1866" /><path
     class="st55"
     d="M928.16,790.34c-1.4-0.29-2.72-0.76-3.94-1.4c-0.42,0.94-1.13,1.72-2.02,2.23c1.64,0.95,3.45,1.64,5.38,2.04   c0.1,0.02,0.2,0.03,0.29,0.03c0.68,0,1.29-0.48,1.43-1.17C929.46,791.28,928.95,790.5,928.16,790.34L928.16,790.34z"
     id="path1868" /><path
     class="st55"
     d="M934.13,761.12c1.39,0.28,2.71,0.75,3.92,1.39c0.42-0.94,1.14-1.71,2.03-2.22c-1.64-0.94-3.45-1.63-5.37-2.03   c-0.79-0.16-1.56,0.35-1.72,1.14C932.83,760.19,933.33,760.96,934.13,761.12L934.13,761.12z"
     id="path1870" /><path
     class="st55"
     d="M944.35,768.82c0.64,1.22,1.12,2.54,1.4,3.93c0.14,0.69,0.75,1.17,1.43,1.17c0.09,0,0.19-0.01,0.29-0.03   c0.79-0.16,1.3-0.93,1.14-1.71c-0.39-1.93-1.09-3.74-2.04-5.39C946.07,767.68,945.29,768.39,944.35,768.82L944.35,768.82z"
     id="path1872" /><path
     class="st55"
     d="M914.81,773.89c0.1,0.02,0.2,0.03,0.29,0.03c0.68,0,1.28-0.47,1.43-1.17c0.28-1.39,0.75-2.69,1.37-3.9   c-0.94-0.41-1.73-1.11-2.24-1.98c-0.93,1.62-1.61,3.41-1.99,5.31C913.51,772.96,914.02,773.73,914.81,773.89L914.81,773.89z"
     id="path1874" /><path
     class="st55"
     d="M924.16,762.55c1.23-0.66,2.58-1.14,4-1.43c0.79-0.16,1.3-0.93,1.14-1.72c-0.16-0.79-0.93-1.3-1.72-1.14   c-1.94,0.39-3.77,1.1-5.42,2.05C923.04,760.82,923.75,761.61,924.16,762.55L924.16,762.55z"
     id="path1876" /><path
     class="st55"
     d="M938.05,788.96c-1.21,0.63-2.53,1.1-3.92,1.39c-0.8,0.16-1.3,0.93-1.15,1.72c0.15,0.69,0.75,1.17,1.43,1.17   c0.09,0,0.2-0.01,0.29-0.03c1.93-0.39,3.74-1.09,5.37-2.03C939.19,790.67,938.46,789.9,938.05,788.96L938.05,788.96z"
     id="path1878" /><path
     class="st55"
     d="M947.47,777.58c-0.79-0.16-1.56,0.35-1.72,1.14c-0.28,1.39-0.76,2.71-1.4,3.93c0.94,0.42,1.72,1.13,2.23,2.03   c0.95-1.64,1.64-3.45,2.04-5.39C948.77,778.51,948.26,777.74,947.47,777.58L947.47,777.58z"
     id="path1880" /><path
     class="st55"
     d="M918.66,767.57c0.35,0.13,0.73,0.2,1.13,0.2c1.83,0,3.31-1.49,3.31-3.32c0-0.41-0.07-0.79-0.2-1.15   c-0.36-0.99-1.17-1.75-2.2-2.04c-0.28-0.08-0.59-0.12-0.91-0.12c-1.83,0-3.32,1.48-3.32,3.31c0,0.33,0.05,0.64,0.14,0.94   C916.91,766.41,917.67,767.22,918.66,767.57L918.66,767.57z"
     id="path1882" /><path
     class="st55"
     d="M939.09,764.45c0,1.83,1.49,3.32,3.32,3.32c0.42,0,0.83-0.08,1.2-0.23c0.99-0.38,1.74-1.21,2.01-2.25   c0.07-0.27,0.11-0.55,0.11-0.85c0-1.83-1.48-3.31-3.31-3.31c-0.3,0-0.58,0.04-0.85,0.11c-1.03,0.28-1.86,1.03-2.24,2.01   C939.17,763.63,939.09,764.03,939.09,764.45L939.09,764.45z"
     id="path1884" /><path
     class="st55"
     d="M923.17,787.02c0-1.83-1.49-3.32-3.32-3.32c-0.42,0-0.81,0.07-1.17,0.22c-0.99,0.37-1.74,1.2-2.02,2.23   c-0.07,0.28-0.12,0.57-0.12,0.88c0,1.83,1.48,3.31,3.31,3.31c0.3,0,0.59-0.04,0.87-0.12c1.03-0.28,1.86-1.03,2.23-2.01   C923.09,787.83,923.17,787.43,923.17,787.02L923.17,787.02z"
     id="path1886" /><path
     class="st55"
     d="M943.61,783.92c-0.37-0.15-0.77-0.23-1.2-0.23c-1.83,0-3.32,1.49-3.32,3.32c0,0.42,0.08,0.82,0.23,1.2   c0.38,0.98,1.21,1.73,2.24,2.01c0.27,0.07,0.55,0.11,0.85,0.11c1.83,0,3.31-1.48,3.31-3.31c0-0.29-0.04-0.58-0.11-0.85   C945.34,785.13,944.59,784.3,943.61,783.92L943.61,783.92z"
     id="path1888" /><path
     class="st55"
     d="M931.13,781.57c-3.09,0-5.62-2.42-5.82-5.46l0.62,0.71c0.22,0.25,0.52,0.37,0.82,0.37   c0.26,0,0.51-0.09,0.72-0.27c0.46-0.4,0.5-1.09,0.1-1.55l-2.56-2.92c-0.21-0.24-0.51-0.37-0.82-0.37s-0.62,0.14-0.82,0.37   l-2.56,2.92c-0.4,0.46-0.35,1.15,0.1,1.55c0.46,0.4,1.15,0.35,1.54-0.1l0.66-0.75c0.18,4.27,3.7,7.69,8.01,7.69   c0.6,0,1.09-0.49,1.09-1.09C932.22,782.06,931.73,781.57,931.13,781.57L931.13,781.57z"
     id="path1890" /><path
     class="st55"
     d="M931.13,769.9c3.09,0,5.62,2.42,5.82,5.46l-0.62-0.71c-0.4-0.46-1.09-0.5-1.55-0.1   c-0.45,0.4-0.5,1.09-0.1,1.55l2.56,2.92c0.21,0.24,0.51,0.37,0.82,0.37c0.32,0,0.62-0.14,0.82-0.37l2.56-2.92   c0.4-0.46,0.35-1.15-0.1-1.54c-0.45-0.4-1.15-0.35-1.55,0.1l-0.66,0.75c-0.18-4.27-3.7-7.69-8.01-7.69c-0.61,0-1.1,0.49-1.1,1.1   C930.03,769.4,930.52,769.9,931.13,769.9L931.13,769.9z"
     id="path1892" /></a>
	<g
   id="g1960">
		<path
   class="st56"
   d="M515.3,116.5c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64    c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1    C515.3,123.97,515.3,120.29,515.3,116.5z"
   id="path1894" />
		<path
   class="st56"
   d="M531.36,123.73v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-14.44h2.82v5.36h0.04    c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1H531.36z"
   id="path1896" />
		<path
   class="st56"
   d="M539.48,109.28v2.22h-2.82v-2.22H539.48z M539.48,123.73h-2.82v-10.1h2.82V123.73z"
   id="path1898" />
		<path
   class="st56"
   d="M545.04,109.28v14.44h-2.82v-14.44H545.04z"
   id="path1900" />
		<path
   class="st56"
   d="M552.58,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32    c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H552.58z M552.44,118.59c0-2.02,0.02-3.42-1.14-3.42    c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C552.26,122.19,552.44,121.13,552.44,118.59z"
   id="path1902" />
		<path
   class="st56"
   d="M565.08,123.73h-3.02v-14.44h5.58c2.06,0,3.38,1.32,3.38,3.78c0,1.84-0.72,3.22-2.68,3.54v0.04    c0.66,0.08,2.62,0.24,2.62,2.84c0,0.92,0.06,3.64,0.34,4.24h-2.96c-0.4-0.88-0.32-1.86-0.32-2.8c0-1.72,0.16-3.18-2.16-3.18h-0.78    V123.73z M565.08,115.52h1.34c1.2,0,1.54-1.2,1.54-2.12c0-1.38-0.58-1.9-1.54-1.9h-1.34V115.52z"
   id="path1904" />
		<path
   class="st56"
   d="M576.16,109.28v2.22h-2.82v-2.22H576.16z M576.16,123.73h-2.82v-10.1h2.82V123.73z"
   id="path1906" />
		<path
   class="st56"
   d="M586.38,113.62v10.52c0,0.7,0.04,3.46-3.84,3.46c-2.1,0-3.9-0.54-3.96-3h2.76c0,0.42,0.06,0.78,0.24,1.02    c0.18,0.26,0.5,0.4,0.94,0.4c0.7,0,1.04-0.66,1.04-1.68v-1.94h-0.04c-0.42,0.78-1.22,1.18-2.14,1.18c-3.1,0-2.96-2.84-2.96-5.12    c0-2.22,0.04-5.04,2.98-5.04c1,0,1.86,0.44,2.26,1.38h0.04v-1.18H586.38z M582.4,121.85c1.02,0,1.16-1.06,1.16-3.2    c0-2.22-0.1-3.48-1.14-3.48c-1.06,0-1.24,0.74-1.24,3.82C581.18,119.93,581.04,121.85,582.4,121.85z"
   id="path1908" />
		<path
   class="st56"
   d="M593.6,123.73v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-14.44h2.82v5.36h0.04    c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1H593.6z"
   id="path1910" />
		<path
   class="st56"
   d="M597.52,113.62h1.14v-1.6l2.82-1.26v2.86h1.46v1.74h-1.46v5.4c0,0.76-0.02,1.26,0.9,1.26    c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V113.62z"
   id="path1912" />
		<path
   class="st56"
   d="M606.44,120.49c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04    c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3    c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08    c-2.46,0-4.1-0.62-3.94-3.44H606.44z"
   id="path1914" />
		<path
   class="st56"
   d="M617.7,123.73v-14.44h3.02v12.04h4.52v2.4H617.7z"
   id="path1916" />
		<path
   class="st56"
   d="M634.08,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54    c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76    c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M628.88,120.59    c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C629.92,118.91,628.88,118.79,628.88,120.59z"
   id="path1918" />
		<path
   class="st56"
   d="M639.24,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1    h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6c-0.9,0-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z"
   id="path1920" />
		<path
   class="st56"
   d="M651.46,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32    c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H651.46z M651.32,118.59c0-2.02,0.02-3.42-1.14-3.42    c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C651.14,122.19,651.32,121.13,651.32,118.59z"
   id="path1922" />
		<path
   class="st56"
   d="M658.64,120.49c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04    c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3    c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08    c-2.46,0-4.1-0.62-3.94-3.44H658.64z"
   id="path1924" />
		<path
   class="st56"
   d="M670.44,117.23c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.3,3.16c0,3.08,0.26,3.74,1.3,3.74    c0.88,0,1.3-0.8,1.3-2.12h2.82c0,2.74-1.48,3.92-4.12,3.92c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12    c2.6,0,4.08,1.16,4.08,3.8H670.44z"
   id="path1926" />
		<path
   class="st56"
   d="M682.96,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54    c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76    c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M677.76,120.59    c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C678.8,118.91,677.76,118.79,677.76,120.59z"
   id="path1928" />
		<path
   class="st56"
   d="M687.98,113.62v1.12h0.04c0.52-0.98,1.3-1.32,2.38-1.32c2.92,0,2.82,3.24,2.82,5.32    c0,2.04,0.08,5.18-2.76,5.18c-1.02,0-1.72-0.3-2.3-1.16h-0.04v5.3h-2.82v-14.44H687.98z M690.46,118.59c0-2.02,0.02-3.42-1.2-3.42    c-1.16,0-1.14,1.4-1.14,3.42c0,2.54,0.18,3.6,1.14,3.6C690.28,122.19,690.46,121.13,690.46,118.59z"
   id="path1930" />
		<path
   class="st56"
   d="M697.9,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62    c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H697.9z     M700.48,117.55c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H700.48z"
   id="path1932" />
		<path
   class="st56"
   d="M717.4,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54    c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76    c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M712.2,120.59    c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C713.24,118.91,712.2,118.79,712.2,120.59z"
   id="path1934" />
		<path
   class="st56"
   d="M722.56,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1    h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z"
   id="path1936" />
		<path
   class="st56"
   d="M734.78,123.73v-1.12h-0.04c-0.52,0.98-1.3,1.32-2.38,1.32c-2.92,0-2.82-3.24-2.82-5.32    c0-2.04-0.08-5.18,2.76-5.18c1.02,0,1.72,0.3,2.3,1.16h0.04v-5.3h2.82v14.44H734.78z M734.64,118.59c0-2.02,0.02-3.42-1.14-3.42    c-1.22,0-1.2,1.4-1.2,3.42c0,2.54,0.18,3.6,1.2,3.6C734.46,122.19,734.64,121.13,734.64,118.59z"
   id="path1938" />
		<path
   class="st56"
   d="M750.92,113.72c0.02-1.34-0.2-2.52-1.8-2.52c-1.88,0-1.88,2.54-1.88,5.34c0,4.52,0.44,5.32,2.16,5.32    c0.5,0,1.04-0.12,1.5-0.28v-3.2h-1.64v-2.22h4.66v7.32c-0.82,0.16-2.88,0.48-4.08,0.48c-5.08,0-5.66-2.1-5.66-7.58    c0-3.64,0.18-7.34,5.12-7.34c2.96,0,4.8,1.66,4.62,4.68H750.92z"
   id="path1940" />
		<path
   class="st56"
   d="M756.16,118.55c0-2.76,0.4-5.12,4.12-5.12s4.12,2.36,4.12,5.12c0,3.16-0.48,5.38-4.12,5.38    S756.16,121.71,756.16,118.55z M761.58,118.39c0-2.1-0.1-3.16-1.3-3.16s-1.3,1.06-1.3,3.16c0,3.08,0.26,3.74,1.3,3.74    S761.58,121.47,761.58,118.39z"
   id="path1942" />
		<path
   class="st56"
   d="M765.44,113.62h2.86l1.42,7.58h0.04l1.48-7.58H774l-2.78,10.1h-3.1L765.44,113.62z"
   id="path1944" />
		<path
   class="st56"
   d="M777.88,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62    c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H777.88z     M780.46,117.55c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H780.46z"
   id="path1946" />
		<path
   class="st56"
   d="M787.96,113.62v1.3H788c0.52-1.16,1.48-1.5,2.62-1.5v2.52c-2.48-0.16-2.52,1.28-2.52,2.28v5.5h-2.82v-10.1    H787.96z"
   id="path1948" />
		<path
   class="st56"
   d="M794.76,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1    h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z"
   id="path1950" />
		<path
   class="st56"
   d="M809.6,121.85c0,0.62,0.08,1.26,0.14,1.88h-2.62l-0.12-1.34h-0.04c-0.6,1.04-1.42,1.54-2.64,1.54    c-1.96,0-2.68-1.46-2.68-3.22c0-3.34,2.58-3.48,5.2-3.44v-0.78c0-0.86-0.12-1.48-1.14-1.48c-0.98,0-1.06,0.74-1.06,1.54h-2.76    c0-1.22,0.38-2,1.04-2.46c0.64-0.48,1.56-0.66,2.64-0.66c3.58,0,4.04,1.54,4.04,3.38V121.85z M804.4,120.59    c0,0.72,0.12,1.6,1.04,1.6c1.66,0,1.4-2.24,1.4-3.34C805.44,118.91,804.4,118.79,804.4,120.59z"
   id="path1952" />
		<path
   class="st56"
   d="M814.76,114.64h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1    h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V114.64z"
   id="path1954" />
		<path
   class="st56"
   d="M827.08,117.23c0-1.5-0.38-2-1.26-2c-1.2,0-1.3,1.06-1.3,3.16c0,3.08,0.26,3.74,1.3,3.74    c0.88,0,1.3-0.8,1.3-2.12h2.82c0,2.74-1.48,3.92-4.12,3.92c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12    c2.6,0,4.08,1.16,4.08,3.8H827.08z"
   id="path1956" />
		<path
   class="st56"
   d="M834.54,119.13c0,1.2,0.04,3,1.28,3c1,0,1.2-0.96,1.2-1.8h2.86c-0.04,1.1-0.4,2-1.08,2.62    c-0.66,0.62-1.66,0.98-2.98,0.98c-3.64,0-4.12-2.22-4.12-5.38c0-2.76,0.4-5.12,4.12-5.12c3.8,0,4.22,2.46,4.12,5.7H834.54z     M837.12,117.55c0-0.98,0.04-2.38-1.3-2.38c-1.3,0-1.28,1.52-1.28,2.38H837.12z"
   id="path1958" />
	</g>
	<a
   id="a3378"
   xlink:href="/child-rights#demography"
   target="blank"
   xlink:title="Demographics"
   xlink:show="Demographics"><g
     id="g1986">
		<path
   class="st56"
   d="M30.99,276.62h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24    c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V276.62z M32.65,288.18h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6    h-2.18V288.18z"
   id="path1962" />
		<path
   class="st56"
   d="M43.23,285.56c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H43.23z M46.78,284.44    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H46.78z"
   id="path1964" />
		<path
   class="st56"
   d="M55.26,289.62v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61c-0.27,0.45-0.34,0.99-0.34,1.33    v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31c0.83,0,1.78,0.34,2.12,1.17    c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3c0-0.92-0.25-1.76-1.44-1.76    c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H55.26z"
   id="path1966" />
		<path
   class="st56"
   d="M63.54,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C65.07,289.81,63.54,289.23,63.54,285.21z M68.9,284.58c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C68.52,288.6,68.9,287.54,68.9,284.58z"
   id="path1968" />
		<path
   class="st56"
   d="M77.6,280.53h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M75.87,281.58c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C77.63,283.68,77.72,281.58,75.87,281.58z"
   id="path1970" />
		<path
   class="st56"
   d="M83.32,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z"
   id="path1972" />
		<path
   class="st56"
   d="M92.46,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99c0-2.75,2.7-2.88,4.77-2.83    c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74c2.34,0,2.95,1.21,2.95,2.74v4.38    c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M89.13,286.92c0,0.88,0.43,1.67,1.42,1.67c0.9,0,2.02-0.56,1.87-3.49    C91.02,285.12,89.13,285,89.13,286.92z"
   id="path1974" />
		<path
   class="st56"
   d="M98.38,281.61h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V281.61z M101.9,284.93c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C101.68,288.6,101.9,287.36,101.9,284.93z"
   id="path1976" />
		<path
   class="st56"
   d="M110.72,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H110.72z"
   id="path1978" />
		<path
   class="st56"
   d="M114.66,276.62h1.66v1.58h-1.66V276.62z M116.22,289.62h-1.48v-9.09h1.48V289.62z"
   id="path1980" />
		<path
   class="st56"
   d="M123.53,283.45c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H123.53z"
   id="path1982" />
		<path
   class="st56"
   d="M130.46,289.81c-1.96,0-3.19-0.86-3.13-2.95H129c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C133.63,289.03,132.26,289.81,130.46,289.81z"
   id="path1984" />
	</g></a>
	<path
   class="st57"
   d="M25.02,276.3c-4.35,0.61-7.75,2.51-8.74,4.92"
   id="path1988" />
	<line
   class="st58"
   x1="16"
   y1="285.48"
   x2="16"
   y2="303.74"
   id="line1990" />
	<path
   class="st57"
   d="M17.07,307.86c1.69,2.04,5.23,3.52,9.44,3.81"
   id="path1992" />
	<line
   class="st59"
   x1="30.94"
   y1="311.72"
   x2="135.63"
   y2="311.72"
   id="line1994" />
	<path
   class="st57"
   d="M140.08,311.52c4.35-0.61,7.74-2.51,8.73-4.92"
   id="path1996" />
	<line
   class="st58"
   x1="149.11"
   y1="302.34"
   x2="149.11"
   y2="284.08"
   id="line1998" />
	<path
   class="st57"
   d="M148.04,279.96c-1.69-2.04-5.23-3.52-9.44-3.81"
   id="path2000" />
	<line
   class="st59"
   x1="134.16"
   y1="276.1"
   x2="29.47"
   y2="276.1"
   id="line2002" />
	<path
   class="st60"
   d="M16,282.67L16,282.67 M16,305.15L16,305.15 M28,311.72L28,311.72 M137.11,311.72L137.11,311.72    M149.11,305.15L149.11,305.15 M149.11,282.67L149.11,282.67 M137.11,276.1L137.11,276.1 M28,276.1L28,276.1"
   id="path2004" />
	<a
   id="a3381"
   xlink:href="/child-rights#demography"
   target="blank"
   xlink:title="Demographics" />
	<a
   id="a4916"
   xlink:href="child-rights#demography"
   target="blank"
   xlink:title="Demographics"
   xlink:show="Demographics"><path
     class="st56"
     d="M71.65,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.89-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87   C59.63,230.08,65.33,234.81,71.65,234.48L71.65,234.48z"
     id="path2006"
     style="enable-background:new 0 0 1355 1310.5" /><path
     class="st55"
     d="M98.41,205.04l-3.28-2.31l-7.82,11.12l-6.18-4.66l-5.36,7.27c-0.26,0.35-0.66,0.54-1.07,0.54   c-0.28,0-0.55-0.08-0.79-0.26c-0.59-0.44-0.72-1.27-0.28-1.86l6.95-9.43l6.13,4.62l6.23-8.87l-3.23-2.27l9.63-4.47L98.41,205.04   L98.41,205.04z M70.42,182.02c-0.93,0-1.68,0.75-1.68,1.68c0,0.93,0.75,1.68,1.68,1.68c0.93,0,1.68-0.75,1.68-1.68   C72.1,182.77,71.35,182.02,70.42,182.02L70.42,182.02z M70.22,195.21l-0.34,6.2c0,0.22-0.18,0.4-0.4,0.4   c-0.22,0-0.39-0.18-0.39-0.4l-0.34-6.2h-1.1l1.14-6.96l-2.29,4.55c-0.08,0.2-0.32,0.3-0.52,0.21c-0.2-0.09-0.29-0.32-0.21-0.52   c0,0,1.68-4.53,2.09-5.37c0.41-0.84,0.82-1.35,2.39-1.35h0.32c1.57,0,1.98,0.51,2.39,1.35c0.42,0.84,2.09,5.37,2.09,5.37   c0.09,0.2-0.01,0.43-0.21,0.52c-0.2,0.09-0.43-0.01-0.52-0.21l-2.28-4.55l1.13,6.96h-1.1l-0.34,6.2c0,0.22-0.18,0.4-0.39,0.4   c-0.22,0-0.39-0.18-0.39-0.4l-0.36-6.2H70.22L70.22,195.21z M85.69,183.69c0,0.93-0.75,1.68-1.68,1.68c-0.93,0-1.69-0.75-1.69-1.68   c0-0.93,0.75-1.68,1.69-1.68C84.94,182.01,85.69,182.76,85.69,183.69L85.69,183.69z M85.75,191.91l0.33,9.2   c0.02,0.36-0.25,0.68-0.61,0.7c-0.02,0-0.03,0-0.05,0c-0.34,0-0.64-0.26-0.66-0.61l-0.75-7.11l-0.75,7.11   c-0.03,0.35-0.32,0.61-0.66,0.61c-0.01,0-0.03,0-0.05,0c-0.36-0.03-0.64-0.34-0.61-0.7l0.32-9.2l-0.11-3.66l-2.05,4.55   c-0.08,0.2-0.32,0.3-0.52,0.21c-0.2-0.09-0.29-0.32-0.21-0.52c0,0,1.45-4.52,1.86-5.37c0.41-0.84,1.05-1.35,2.62-1.35h0.32   c1.57,0,2.21,0.51,2.62,1.35c0.41,0.84,1.86,5.37,1.86,5.37c0.09,0.2-0.01,0.43-0.21,0.52c-0.2,0.08-0.43-0.01-0.52-0.21   l-2.05-4.55L85.75,191.91L85.75,191.91L85.75,191.91z M78.25,193.27c0,0.57-0.46,1.03-1.03,1.03c-0.57,0-1.03-0.46-1.03-1.03   c0-0.57,0.46-1.03,1.03-1.03C77.78,192.23,78.25,192.69,78.25,193.27L78.25,193.27z M77.21,198.31c0,0-0.46,3.23-0.46,3.23   c-0.06,0.16-0.21,0.27-0.39,0.27c-0.19,0-0.34-0.12-0.4-0.29c0-0.01-0.02-0.2,0-0.23l0.19-3.97l-0.06-1.36   c-0.05-0.46-0.06-0.33-0.59-0.64c-0.54-0.32-1.45-1.74-1.5-1.81c-0.04-0.07-0.13-0.2-0.14-0.28c-0.03-0.14,0.07-0.28,0.21-0.31   c0.11-0.02,0.2,0.04,0.26,0.11c0.07,0.08,1.13,1.48,1.91,1.61c0.18-0.03,0.37-0.12,0.87-0.12h0.2c0.5,0,0.69,0.09,0.87,0.12   c0.79-0.13,1.84-1.54,1.91-1.61c0.07-0.07,0.16-0.13,0.26-0.11c0.14,0.03,0.24,0.16,0.21,0.31c-0.02,0.08-0.1,0.2-0.14,0.28   c-0.04,0.07-0.96,1.48-1.5,1.81c-0.53,0.31-0.53,0.18-0.59,0.64l-0.06,1.36l0.19,3.97c0.01,0.03,0,0.22,0,0.23   c-0.06,0.17-0.21,0.29-0.4,0.29c-0.18,0-0.33-0.11-0.39-0.27C77.68,201.54,77.21,198.31,77.21,198.31"
     id="path2008" /></a>
	<line
   class="st61"
   x1="82.55"
   y1="244.49"
   x2="82.55"
   y2="260.77"
   id="line2010" />
	<path
   class="st62"
   d="M82.55,241.53L82.55,241.53 M82.55,262.25L82.55,262.25"
   id="path2012" />
	<path
   d="M82.55,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C79.77,243.06,81.02,244.31,82.55,244.31L82.55,244.31z"
   id="path2014" />
	
	
	
	
	
	
	<path
   class="st63"
   d="M478.61,311.32c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2076" />
	<line
   class="st64"
   x1="487.5"
   y1="296.82"
   x2="487.5"
   y2="289.55"
   id="line2078" />
	<path
   class="st63"
   d="M487.09,284.99c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2080" />
	<a
   id="a9589"
   xlink:href="/child-rights#migration"
   target="blank"
   xlink:title="Migration and displacement"
   xlink:show="Migration and displacement"><g
     id="g2040">
		<path
   class="st56"
   d="M372.91,289.62h-1.55v-13h2.68l3.28,10.91h0.04l3.31-10.91h2.74v13h-1.66v-11.56h-0.04l-3.64,11.56h-1.57    l-3.56-11.56h-0.04V289.62z"
   id="path2016" />
		<path
   class="st56"
   d="M386.05,276.62h1.66v1.58h-1.66V276.62z M387.62,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2018" />
		<path
   class="st56"
   d="M394.98,280.53h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M393.25,281.58c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C395.02,283.68,395.11,281.58,393.25,281.58z"
   id="path2020" />
		<path
   class="st56"
   d="M400.71,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z"
   id="path2022" />
		<path
   class="st56"
   d="M409.85,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M406.52,286.92c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C408.41,285.12,406.52,285,406.52,286.92z"
   id="path2024" />
		<path
   class="st56"
   d="M414.33,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H414.33z"
   id="path2026" />
		<path
   class="st56"
   d="M419.05,276.62h1.66v1.58h-1.66V276.62z M420.61,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2028" />
		<path
   class="st56"
   d="M422.92,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C424.45,289.81,422.92,289.23,422.92,285.21z M428.28,284.58c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C427.9,288.6,428.28,287.54,428.28,284.58z"
   id="path2030" />
		<path
   class="st56"
   d="M437.1,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H437.1z"
   id="path2032" />
		<path
   class="st56"
   d="M449.85,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M446.51,286.92c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C448.41,285.12,446.51,285,446.51,286.92z"
   id="path2034" />
		<path
   class="st56"
   d="M459.1,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H459.1z"
   id="path2036" />
		<path
   class="st56"
   d="M467.97,276.62h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V276.62z M466.26,281.56c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C467.97,283.5,467.9,281.56,466.26,281.56z"
   id="path2038" />
	</g><g
     id="g2066">
		<path
   class="st56"
   d="M377.99,298.23h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V298.23z M376.28,303.16c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C377.99,305.1,377.92,303.16,376.28,303.16z"
   id="path2042" />
		<path
   class="st56"
   d="M382.06,298.23h1.66v1.58h-1.66V298.23z M383.63,311.23h-1.48v-9.09h1.48V311.23z"
   id="path2044" />
		<path
   class="st56"
   d="M388.86,311.41c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C392.03,310.63,390.66,311.41,388.86,311.41z"
   id="path2046" />
		<path
   class="st56"
   d="M395.77,303.21h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V303.21z M399.29,306.53c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C399.07,310.2,399.29,308.96,399.29,306.53z"
   id="path2048" />
		<path
   class="st56"
   d="M404.61,311.23h-1.48v-13h1.48V311.23z"
   id="path2050" />
		<path
   class="st56"
   d="M411.85,309.91h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V309.91z M408.52,308.53c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C410.41,306.73,408.52,306.6,408.52,308.53z"
   id="path2052" />
		<path
   class="st56"
   d="M420.92,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H420.92z"
   id="path2054" />
		<path
   class="st56"
   d="M426.61,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H426.61z M430.16,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H430.16z"
   id="path2056" />
		<path
   class="st56"
   d="M438.63,311.23v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H438.63z"
   id="path2058" />
		<path
   class="st56"
   d="M448.6,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H448.6z M452.15,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H452.15z"
   id="path2060" />
		<path
   class="st56"
   d="M461.1,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H461.1z"
   id="path2062" />
		<path
   class="st56"
   d="M465.33,302.13v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H465.33z"
   id="path2064" />
	</g><path
     class="st63"
     d="M363.28,276.5c-4.63,1.24-8.16,5.18-8.79,10.03"
     id="path2068" /><line
     class="st64"
     x1="354.39"
     y1="291"
     x2="354.39"
     y2="298.27"
     id="line2070" /><path
     class="st63"
     d="M354.8,302.83c1.24,4.63,5.18,8.16,10.03,8.79"
     id="path2072" /><line
     class="st59"
     x1="369.34"
     y1="311.72"
     x2="474.02"
     y2="311.72"
     id="line2074" /><line
     class="st59"
     x1="472.55"
     y1="276.1"
     x2="367.86"
     y2="276.1"
     id="line2082" /></a>
	<path
   class="st60"
   d="M354.39,288.1L354.39,288.1 M354.39,299.72L354.39,299.72 M366.39,311.72L366.39,311.72 M475.5,311.72   L475.5,311.72 M487.5,299.72L487.5,299.72 M487.5,288.1L487.5,288.1 M475.5,276.1L475.5,276.1 M366.39,276.1L366.39,276.1"
   id="path2084" />
	
	
	
	
	
	
	
	<a
   id="a11335"
   target="blank"
   xlink:title="Migration and displacement"
   xlink:show="Migration and displacement"
   xlink:href="/child-rights#migration"><path
     class="st56"
     d="m 410.04,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.2,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.39,10.9 12.71,10.57 z"
     id="path2086" /><path
     class="st55"
     d="m 425.26,187.08 c -0.51,-1.56 -2.19,-2.41 -3.76,-1.9 -1.56,0.51 -2.41,2.2 -1.9,3.76 0.51,1.56 2.2,2.41 3.76,1.9 1.56,-0.52 2.41,-2.2 1.9,-3.76 z"
     id="path2088" /><path
     class="st55"
     d="m 418.52,202.52 2.92,-5.79 c 0.9,-1.78 0.18,-3.95 -1.6,-4.85 l -1.9,-0.96 c -0.1,-0.05 -0.21,-0.09 -0.32,-0.11 -5.06,-2.22 -11.06,-0.15 -13.61,4.84 -0.39,0.76 -0.09,1.68 0.67,2.07 0.76,0.39 1.68,0.09 2.07,-0.67 1.47,-2.87 4.55,-4.38 7.59,-4 l -11.07,21.71 c -0.39,0.76 -0.09,1.7 0.68,2.09 0.22,0.11 0.47,0.17 0.7,0.17 0.57,0 1.11,-0.31 1.39,-0.85 l 6.73,-13.19 3.33,1.68 c 3.59,1.95 4.98,6.44 3.09,10.09 -0.39,0.76 -0.1,1.7 0.66,2.09 0.38,0.2 0.8,0.22 1.18,0.1 0.38,-0.12 0.71,-0.38 0.91,-0.77 2.48,-4.81 0.93,-10.66 -3.42,-13.65 z"
     id="path2090" /><path
     class="st55"
     d="m 438.46,198.67 -5.17,-5.17 c -0.45,-0.45 -1.18,-0.45 -1.63,0 -0.45,0.45 -0.45,1.18 0,1.63 l 3.24,3.23 h -9.86 c -0.62,0 -1.11,0.5 -1.11,1.12 0,0.62 0.5,1.12 1.11,1.12 h 9.86 l -3.24,3.24 c -0.45,0.45 -0.45,1.18 0,1.63 0.23,0.23 0.52,0.34 0.82,0.34 0.29,0 0.59,-0.11 0.82,-0.34 l 5.17,-5.17 c 0.22,-0.22 0.34,-0.51 0.34,-0.82 0,-0.31 -0.14,-0.59 -0.35,-0.81 z"
     id="path2092" /><path
     class="st55"
     d="m 428.01,202.84 c -0.62,0 -1.12,0.5 -1.12,1.12 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0.01,-0.62 -0.49,-1.12 -1.11,-1.12 z"
     id="path2094" /><path
     class="st55"
     d="m 428.01,196.14 c 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0,-0.62 -0.5,-1.12 -1.11,-1.12 -0.62,0 -1.12,0.5 -1.12,1.12 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 z"
     id="path2096" /><path
     class="st55"
     d="m 428.01,187.96 c 0.62,0 1.11,-0.5 1.11,-1.11 v -3.72 c 0,-0.62 -0.5,-1.11 -1.11,-1.11 -0.62,0 -1.12,0.5 -1.12,1.11 v 3.72 c 0,0.61 0.5,1.11 1.12,1.11 z"
     id="path2098" /><path
     class="st55"
     d="m 428.01,211.02 c -0.62,0 -1.12,0.5 -1.12,1.11 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0.01,-0.61 -0.49,-1.11 -1.11,-1.11 z"
     id="path2100" /></a>
	<line
   class="st61"
   x1="420.94"
   y1="244.49"
   x2="420.94"
   y2="260.77"
   id="line2102" />
	<path
   class="st62"
   d="M420.94,241.53L420.94,241.53 M420.94,262.25L420.94,262.25"
   id="path2104" />
	<path
   d="M420.94,244.31c1.54,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C418.17,243.06,419.41,244.31,420.94,244.31L420.94,244.31z"
   id="path2106" />
	
	
	<path
   class="st63"
   d="M194.09,276.5c-4.63,1.24-8.16,5.18-8.79,10.03"
   id="path2144" />
	<line
   class="st64"
   x1="185.19"
   y1="291"
   x2="185.19"
   y2="298.27"
   id="line2146" />
	<path
   class="st63"
   d="M185.6,302.83c1.24,4.63,5.18,8.16,10.03,8.79"
   id="path2148" />
	
	<path
   class="st63"
   d="M309.41,311.32c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2152" />
	<line
   class="st64"
   x1="318.3"
   y1="296.82"
   x2="318.3"
   y2="289.55"
   id="line2154" />
	<path
   class="st63"
   d="M317.9,284.99c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2156" />
	<a
   id="a6479"
   xlink:href="child-rights#economy"
   target="blank"
   xlink:title="Political economy"
   xlink:show="Political economy"><g
     id="g2126">
		<path
   class="st56"
   d="M223.87,289.62v-13h3.85c1.75,0,3.62,0.65,3.62,3.71c0,2.95-2.3,3.57-3.64,3.57h-2.18v5.73H223.87z     M225.52,282.46h1.82c0.68,0,2.3-0.18,2.3-2.21c0-1.98-1.48-2.18-1.84-2.18h-2.29V282.46z"
   id="path2108" />
		<path
   class="st56"
   d="M233.25,285.21c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C234.78,289.81,233.25,289.23,233.25,285.21z M238.61,284.58c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C238.23,288.6,238.61,287.54,238.61,284.58z"
   id="path2110" />
		<path
   class="st56"
   d="M243.94,289.62h-1.48v-13h1.48V289.62z"
   id="path2112" />
		<path
   class="st56"
   d="M246.37,276.62h1.66v1.58h-1.66V276.62z M247.93,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2114" />
		<path
   class="st56"
   d="M250.65,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H250.65z"
   id="path2116" />
		<path
   class="st56"
   d="M255.37,276.62h1.66v1.58h-1.66V276.62z M256.93,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2118" />
		<path
   class="st56"
   d="M264.24,283.45c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H264.24z"
   id="path2120" />
		<path
   class="st56"
   d="M273.17,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M269.84,286.92c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C271.73,285.12,269.84,285,269.84,286.92z"
   id="path2122" />
		<path
   class="st56"
   d="M278.93,289.62h-1.48v-13h1.48V289.62z"
   id="path2124" />
	</g><g
     id="g2142">
		<path
   class="st56"
   d="M220.93,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H220.93z M224.48,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H224.48z"
   id="path2128" />
		<path
   class="st56"
   d="M233.24,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H233.24z"
   id="path2130" />
		<path
   class="st56"
   d="M237.24,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C238.77,311.41,237.24,310.83,237.24,306.82z M242.6,306.19c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C242.23,310.2,242.6,309.14,242.6,306.19z"
   id="path2132" />
		<path
   class="st56"
   d="M251.42,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H251.42z"
   id="path2134" />
		<path
   class="st56"
   d="M255.24,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C256.77,311.41,255.24,310.83,255.24,306.82z M260.6,306.19c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C260.23,310.2,260.6,309.14,260.6,306.19z"
   id="path2136" />
		<path
   class="st56"
   d="M268.96,311.23v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H268.96z"
   id="path2138" />
		<path
   class="st56"
   d="M280.22,309.53h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L280.22,309.53z"
   id="path2140" />
	</g><line
     class="st59"
     x1="200.14"
     y1="311.72"
     x2="304.83"
     y2="311.72"
     id="line2150" /><line
     class="st59"
     x1="303.36"
     y1="276.1"
     x2="198.67"
     y2="276.1"
     id="line2158" /></a>
	<path
   class="st60"
   d="M185.19,288.1L185.19,288.1 M185.19,299.72L185.19,299.72 M197.19,311.72L197.19,311.72 M306.3,311.72   L306.3,311.72 M318.3,299.72L318.3,299.72 M318.3,288.1L318.3,288.1 M306.3,276.1L306.3,276.1 M197.19,276.1L197.19,276.1"
   id="path2160" />
	
	<line
   class="st61"
   x1="251.75"
   y1="244.49"
   x2="251.75"
   y2="260.77"
   id="line2164" />
	<path
   class="st62"
   d="M251.75,241.53L251.75,241.53 M251.75,262.25L251.75,262.25"
   id="path2166" />
	<path
   d="M251.75,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C248.97,243.06,250.21,244.31,251.75,244.31L251.75,244.31z"
   id="path2168" />
	
	
	
	
	
	
	<a
   id="a6457"
   target="blank"
   xlink:title="Political economy"
   xlink:show="Political economy"
   xlink:href="child-rights#economy"><path
     class="st56"
     d="M240.85,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.96-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87   C228.83,230.08,234.52,234.81,240.85,234.48L240.85,234.48z"
     id="path2162" /><path
     class="st55"
     d="M268.15,214.82h-32.81c-0.6,0-1.09,0.49-1.09,1.09s0.49,1.09,1.09,1.09h32.81c0.6,0,1.09-0.49,1.09-1.09   S268.76,214.82,268.15,214.82L268.15,214.82z"
     id="path2170" /><path
     class="st55"
     d="M238.26,213.36h26.98c0.61,0,1.09-0.49,1.09-1.09s-0.49-1.09-1.09-1.09h-26.98c-0.6,0-1.09,0.49-1.09,1.09   S237.65,213.36,238.26,213.36L238.26,213.36z"
     id="path2172" /><polygon
     class="st55"
     points="244.46,209.72 244.46,194.41 241.54,194.41 241.54,209.72 244.46,209.72  "
     id="polygon2174" /><polygon
     class="st55"
     points="250.29,209.72 250.29,194.41 247.37,194.41 247.37,209.72 250.29,209.72  "
     id="polygon2176" /><polygon
     class="st55"
     points="256.12,209.72 256.12,194.41 253.21,194.41 253.21,209.72 256.12,209.72  "
     id="polygon2178" /><polygon
     class="st55"
     points="261.96,209.72 261.96,194.41 259.04,194.41 259.04,209.72 261.96,209.72  "
     id="polygon2180" /><path
     class="st55"
     d="M240.08,192.95h23.33c0.8,0,1.46-0.65,1.46-1.46c0-0.81-0.65-1.46-1.46-1.46h-10.94v-2.19h6.56v-4.38h-6.56   v-0.36c0-0.6-0.49-1.09-1.09-1.09s-1.09,0.49-1.09,1.09v6.93h-10.21c-0.8,0-1.46,0.65-1.46,1.46   C238.62,192.29,239.28,192.95,240.08,192.95L240.08,192.95z"
     id="path2182" /></a>
	
	
	<path
   class="st63"
   d="M701.67,279.54c-4.63,1.24-8.16,5.18-8.79,10.03"
   id="path2236" />
	<line
   class="st64"
   x1="692.78"
   y1="294.04"
   x2="692.78"
   y2="301.31"
   id="line2238" />
	<path
   class="st63"
   d="M693.19,305.87c1.24,4.63,5.18,8.16,10.03,8.79"
   id="path2240" />
	
	<path
   class="st63"
   d="M827.52,314.36c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2244" />
	<line
   class="st64"
   x1="836.41"
   y1="299.86"
   x2="836.41"
   y2="292.59"
   id="line2246" />
	<path
   class="st63"
   d="M836.01,288.03c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2248" />
	<a
   id="a14275"
   xlink:href="/child-rights#spending"
   target="blank"
   xlink:title="Public spending on children"
   xlink:show="Public spending on children"><g
     id="g2212">
		<path
   class="st56"
   d="M708.46,292.67v-13h3.85c1.75,0,3.62,0.65,3.62,3.71c0,2.95-2.3,3.57-3.64,3.57h-2.18v5.73H708.46z     M710.12,285.51h1.82c0.68,0,2.3-0.18,2.3-2.21c0-1.98-1.48-2.18-1.84-2.18h-2.29V285.51z"
   id="path2184" />
		<path
   class="st56"
   d="M722.95,283.58h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V283.58z"
   id="path2186" />
		<path
   class="st56"
   d="M728.69,292.67h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.94,0,3.01,2.61,3.01,4.88    c0,4-1.48,4.57-2.93,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V292.67z M730.35,291.65c1.85,0,1.85-1.98,1.85-3.35    c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C728.69,289.14,728.53,291.65,730.35,291.65z"
   id="path2188" />
		<path
   class="st56"
   d="M737.53,292.67h-1.48v-13h1.48V292.67z"
   id="path2190" />
		<path
   class="st56"
   d="M739.96,279.67h1.66v1.58h-1.66V279.67z M741.53,292.67h-1.48v-9.09h1.48V292.67z"
   id="path2192" />
		<path
   class="st56"
   d="M748.84,286.5c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H748.84z"
   id="path2194" />
		<path
   class="st56"
   d="M759.76,292.85c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C762.93,292.08,761.56,292.85,759.76,292.85z"
   id="path2196" />
		<path
   class="st56"
   d="M766.67,284.66h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.93,0.58,2.93,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V284.66z M770.18,287.97c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C769.97,291.65,770.18,290.4,770.18,287.97z"
   id="path2198" />
		<path
   class="st56"
   d="M775.51,288.6c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H775.51z M779.06,287.49    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H779.06z"
   id="path2200" />
		<path
   class="st56"
   d="M788,292.67v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H788z"
   id="path2202" />
		<path
   class="st56"
   d="M796.88,279.67h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V279.67z M795.17,284.61c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C796.88,286.55,796.81,284.61,795.17,284.61z"
   id="path2204" />
		<path
   class="st56"
   d="M800.94,279.67h1.66v1.58h-1.66V279.67z M802.51,292.67h-1.48v-9.09h1.48V292.67z"
   id="path2206" />
		<path
   class="st56"
   d="M810,292.67v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H810z"
   id="path2208" />
		<path
   class="st56"
   d="M818.87,283.58h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V283.58z M817.14,284.62c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C818.91,286.73,819,284.62,817.14,284.62z"
   id="path2210" />
	</g><g
     id="g2234">
		<path
   class="st56"
   d="M724.33,309.86c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C725.86,314.45,724.33,313.88,724.33,309.86z M729.7,309.23c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C729.32,313.25,729.7,312.18,729.7,309.23z"
   id="path2214" />
		<path
   class="st56"
   d="M738.52,314.27v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H738.52z"
   id="path2216" />
		<path
   class="st56"
   d="M751.33,308.1c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H751.33z"
   id="path2218" />
		<path
   class="st56"
   d="M760.51,314.27v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H760.51z"
   id="path2220" />
		<path
   class="st56"
   d="M764.45,301.27h1.66v1.58h-1.66V301.27z M766.02,314.27h-1.48v-9.09h1.48V314.27z"
   id="path2222" />
		<path
   class="st56"
   d="M770.02,314.27h-1.48v-13h1.48V314.27z"
   id="path2224" />
		<path
   class="st56"
   d="M777.38,301.27h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V301.27z M775.67,306.21c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C777.38,308.15,777.31,306.21,775.67,306.21z"
   id="path2226" />
		<path
   class="st56"
   d="M783.1,306.55h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V306.55z"
   id="path2228" />
		<path
   class="st56"
   d="M789.01,310.2c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H789.01z M792.55,309.09    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H792.55z"
   id="path2230" />
		<path
   class="st56"
   d="M801.5,314.27v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H801.5z"
   id="path2232" />
	</g><line
     class="st65"
     x1="707.77"
     y1="314.76"
     x2="822.92"
     y2="314.76"
     id="line2242" /><line
     class="st65"
     x1="821.42"
     y1="279.14"
     x2="706.28"
     y2="279.14"
     id="line2250" /></a>
	<path
   class="st60"
   d="M692.78,291.14L692.78,291.14 M692.78,302.76L692.78,302.76 M704.78,314.76L704.78,314.76 M824.41,314.76   L824.41,314.76 M836.41,302.76L836.41,302.76 M836.41,291.14L836.41,291.14 M824.41,279.14L824.41,279.14 M704.78,279.14   L704.78,279.14"
   id="path2252" />
	
	<line
   class="st61"
   x1="764.6"
   y1="247.53"
   x2="764.6"
   y2="263.81"
   id="line2256" />
	<path
   class="st62"
   d="M764.6,244.57L764.6,244.57 M764.6,265.29L764.6,265.29"
   id="path2258" />
	<path
   d="M764.6,247.35c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78s-2.78,1.24-2.78,2.78   C761.82,246.1,763.06,247.35,764.6,247.35L764.6,247.35z"
   id="path2260" />
	<g
   id="g2284">
		<path
   class="st56"
   d="M556.28,280.21c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.1-2.83,4.1-3.67,4.1    c-1.62,0-4.1-0.11-4.1-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.57,0,3.56,1.33,3.4,3.85H556.28z"
   id="path2262" />
		<path
   class="st56"
   d="M565.33,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H565.33z"
   id="path2264" />
		<path
   class="st56"
   d="M569.27,276.62h1.66v1.58h-1.66V276.62z M570.84,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2266" />
		<path
   class="st56"
   d="M574.83,289.62h-1.48v-13h1.48V289.62z"
   id="path2268" />
		<path
   class="st56"
   d="M582.2,276.62h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V276.62z M580.48,281.56c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C582.2,283.5,582.12,281.56,580.48,281.56z"
   id="path2270" />
		<path
   class="st56"
   d="M591.91,281.9h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V281.9z"
   id="path2272" />
		<path
   class="st56"
   d="M596.25,276.62h1.66v1.58h-1.66V276.62z M597.82,289.62h-1.48v-9.09h1.48V289.62z"
   id="path2274" />
		<path
   class="st56"
   d="M605.18,280.53h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V280.53z M603.45,281.58c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C605.22,283.68,605.31,281.58,603.45,281.58z"
   id="path2276" />
		<path
   class="st56"
   d="M614.31,289.62v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H614.31z"
   id="path2278" />
		<path
   class="st56"
   d="M618.54,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H618.54z"
   id="path2280" />
		<path
   class="st56"
   d="M626.06,289.81c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C629.23,289.03,627.86,289.81,626.06,289.81z"
   id="path2282" />
	</g>
	<g
   id="g2306">
		<path
   class="st56"
   d="M552.69,302.13h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.85-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V302.13z M550.96,303.18c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C552.72,305.28,552.81,303.18,550.96,303.18z"
   id="path2286" />
		<path
   class="st56"
   d="M556.63,306.82c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C558.16,311.41,556.63,310.83,556.63,306.82z M561.99,306.19c0-2.48-0.77-3.02-1.91-3.02s-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C561.62,310.2,561.99,309.14,561.99,306.19z"
   id="path2288" />
		<path
   class="st56"
   d="M564.84,302.13h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L564.84,302.13z"
   id="path2290" />
		<path
   class="st56"
   d="M575.31,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H575.31z M578.86,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H578.86z"
   id="path2292" />
		<path
   class="st56"
   d="M584.4,303.5h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V303.5z"
   id="path2294" />
		<path
   class="st56"
   d="M593.8,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H593.8z"
   id="path2296" />
		<path
   class="st56"
   d="M602.55,309.91h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V309.91z M599.22,308.53c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C601.11,306.73,599.22,306.6,599.22,308.53z"
   id="path2298" />
		<path
   class="st56"
   d="M611.8,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H611.8z"
   id="path2300" />
		<path
   class="st56"
   d="M620.62,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H620.62z"
   id="path2302" />
		<path
   class="st56"
   d="M626.31,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H626.31z M629.85,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H629.85z"
   id="path2304" />
	</g>
	<path
   class="st63"
   d="M532.48,276.5c-4.63,1.24-8.16,5.18-8.79,10.03"
   id="path2308" />
	<line
   class="st64"
   x1="523.59"
   y1="291"
   x2="523.59"
   y2="298.27"
   id="line2310" />
	<path
   class="st63"
   d="M523.99,302.83c1.24,4.63,5.18,8.16,10.03,8.79"
   id="path2312" />
	<line
   class="st59"
   x1="538.53"
   y1="311.72"
   x2="643.22"
   y2="311.72"
   id="line2314" />
	<path
   class="st63"
   d="M647.8,311.32c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2316" />
	<line
   class="st64"
   x1="656.7"
   y1="296.82"
   x2="656.7"
   y2="289.55"
   id="line2318" />
	<path
   class="st63"
   d="M656.29,284.99c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2320" />
	<line
   class="st59"
   x1="641.75"
   y1="276.1"
   x2="537.06"
   y2="276.1"
   id="line2322" />
	<path
   class="st60"
   d="M523.59,288.1L523.59,288.1 M523.59,299.72L523.59,299.72 M535.59,311.72L535.59,311.72 M644.7,311.72   L644.7,311.72 M656.7,299.72L656.7,299.72 M656.7,288.1L656.7,288.1 M644.7,276.1L644.7,276.1 M535.59,276.1L535.59,276.1"
   id="path2324" />
	
	<line
   class="st61"
   x1="590.14"
   y1="244.49"
   x2="590.14"
   y2="260.77"
   id="line2328" />
	<path
   class="st62"
   d="M590.14,241.53L590.14,241.53 M590.14,262.25L590.14,262.25"
   id="path2330" />
	<path
   d="M590.14,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C587.36,243.06,588.61,244.31,590.14,244.31L590.14,244.31z"
   id="path2332" />
	
	
	
	<a
   id="a11131"
   xlink:href="/child-rights#access"
   target="blank"
   xlink:title="Child rights governance"
   xlink:show="Child rights governance"><path
     class="st56"
     d="M579.24,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.06,0.48-12.2,6.9-11.2,13.9l6.37,44.87   C567.22,230.08,572.91,234.81,579.24,234.48L579.24,234.48z"
     id="path2326" /><path
     class="st55"
     d="M593.06,203.52v-5.47v-1.46v-4.15c0.79,0.61,1.33,1.47,1.47,2.48c0.08,0.55,0.55,0.94,1.08,0.94   c0.05,0,0.1,0,0.15-0.01c0.6-0.08,1.01-0.64,0.93-1.24c-0.43-3.08-3.19-5.32-6.55-5.32c-3.36,0-6.12,2.24-6.55,5.32   c-0.08,0.6,0.33,1.15,0.93,1.24s1.15-0.33,1.24-0.93c0.14-1,0.68-1.86,1.47-2.48v4.15v1.46v5.47c0,0.6,0.49,1.09,1.09,1.09   s1.09-0.49,1.09-1.09v-5.47h1.46v5.47c0,0.6,0.49,1.09,1.09,1.09C592.57,204.61,593.06,204.12,593.06,203.52L593.06,203.52z"
     id="path2334" /><path
     class="st55"
     d="M590.14,187.84c1.61,0,2.92-1.31,2.92-2.92c0-1.61-1.3-2.92-2.92-2.92c-1.61,0-2.92,1.31-2.92,2.92   C587.22,186.54,588.53,187.84,590.14,187.84L590.14,187.84z"
     id="path2336" /><path
     class="st55"
     d="M581.07,200.69c-0.59-0.6-1.56-0.6-2.15,0c-0.59,0.6-0.59,1.58,0,2.19l2.77,2.66c0.35,0.35,0.35,0.92,0,1.27   c-0.35,0.35-0.91,0.35-1.25,0l-3.42-3.66v-11.67c0-1.21-1-2.19-2.19-2.19c-1.19,0-2.19,0.98-2.19,2.19v12.69   c0,0.58,0.23,1.14,0.63,1.55l8.12,8.37v2.92h6.56v-7.29c0-1.46-0.38-2.57-1.33-3.54L581.07,200.69L581.07,200.69z"
     id="path2338" /><path
     class="st55"
     d="M605.45,189.3c-1.19,0-2.19,0.98-2.19,2.19v11.67l-3.42,3.66c-0.35,0.35-0.91,0.35-1.25,0   c-0.35-0.35-0.35-0.92,0-1.27l2.77-2.66c0.59-0.6,0.59-1.58,0-2.19c-0.59-0.6-1.56-0.6-2.15,0l-5.55,5.49   c-0.95,0.97-1.33,2.08-1.33,3.54v7.29h6.56v-2.92l8.12-8.37c0.41-0.41,0.63-0.97,0.63-1.55v-12.69   C607.64,190.28,606.64,189.3,605.45,189.3L605.45,189.3z"
     id="path2340" /></a>
	<g
   id="g2364">
		<path
   class="st56"
   d="M1230.02,288.11v-13h4.23c1.8,0,2.41,0.61,2.9,1.33c0.45,0.7,0.52,1.48,0.52,1.73c0,1.62-0.56,2.7-2.23,3.08    v0.09c1.85,0.22,2.67,1.33,2.67,3.11c0,3.33-2.43,3.66-3.91,3.66H1230.02z M1231.68,280.58h2.41c1.3-0.02,1.93-0.81,1.93-2.07    c0-1.08-0.61-1.96-2-1.96h-2.34V280.58z M1231.68,286.67h2.34c1.76,0,2.4-1.26,2.4-2.21c0-2.07-1.28-2.43-2.97-2.43h-1.76V286.67z    "
   id="path2342" />
		<path
   class="st56"
   d="M1245.56,279.02h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V279.02z"
   id="path2344" />
		<path
   class="st56"
   d="M1252.38,288.29c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1255.55,287.52,1254.18,288.29,1252.38,288.29z"
   id="path2346" />
		<path
   class="st56"
   d="M1257.56,275.11h1.66v1.58h-1.66V275.11z M1259.13,288.11h-1.48v-9.09h1.48V288.11z"
   id="path2348" />
		<path
   class="st56"
   d="M1266.62,288.11v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1266.62z"
   id="path2350" />
		<path
   class="st56"
   d="M1272.13,284.04c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.94-3.17,2.94c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77    H1272.13z M1275.67,282.92c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1275.67z"
   id="path2352" />
		<path
   class="st56"
   d="M1282.37,288.29c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1285.54,287.52,1284.17,288.29,1282.37,288.29z"
   id="path2354" />
		<path
   class="st56"
   d="M1290.36,288.29c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1293.53,287.52,1292.16,288.29,1290.36,288.29z"
   id="path2356" />
		<path
   class="st56"
   d="M1304.35,286.79h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V286.79z M1301.02,285.41c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1302.91,283.61,1301.02,283.48,1301.02,285.41z"
   id="path2358" />
		<path
   class="st56"
   d="M1313.6,288.11v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1313.6z"
   id="path2360" />
		<path
   class="st56"
   d="M1322.47,275.11h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V275.11z M1320.76,280.04c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1322.47,281.99,1322.4,280.04,1320.76,280.04z"
   id="path2362" />
	</g>
	<g
   id="g2388">
		<path
   class="st56"
   d="M1241.57,300.29c0.02-0.74-0.04-1.48-0.38-1.89c-0.34-0.41-1.12-0.56-1.46-0.56c-1.37,0-1.91,0.83-1.96,1.01    c-0.05,0.14-0.38,0.47-0.38,2.7v3.47c0,3.19,1.04,3.57,2.32,3.57c0.5,0,2.03-0.18,2.05-2.72h1.71c0.07,4.1-2.83,4.1-3.67,4.1    c-1.62,0-4.11-0.11-4.11-5.15v-3.67c0-3.67,1.62-4.72,4.18-4.72c2.58,0,3.57,1.33,3.4,3.85H1241.57z"
   id="path2366" />
		<path
   class="st56"
   d="M1250.63,309.71v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1250.63z"
   id="path2368" />
		<path
   class="st56"
   d="M1254.57,296.71h1.66v1.58h-1.66V296.71z M1256.13,309.71h-1.48v-9.09h1.48V309.71z"
   id="path2370" />
		<path
   class="st56"
   d="M1260.13,309.71h-1.48v-13h1.48V309.71z"
   id="path2372" />
		<path
   class="st56"
   d="M1267.49,296.71h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V296.71z M1265.78,301.64c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1267.49,303.59,1267.42,301.64,1265.78,301.64z"
   id="path2374" />
		<path
   class="st56"
   d="M1277.46,303.73v5.98h-1.66v-13h4.48c2.3,0,3.12,1.62,3.12,3.24c0,1.53-0.85,2.7-2.38,2.97v0.04    c1.5,0.23,2.04,0.74,2.12,3.35c0.02,0.56,0.2,2.59,0.45,3.4h-1.73c-0.47-0.9-0.36-2.59-0.5-4.32c-0.13-1.58-1.4-1.66-1.96-1.66    H1277.46z M1277.46,302.29h2.48c1.19,0,1.76-1.03,1.76-2.16c0-0.94-0.47-1.98-1.75-1.98h-2.5V302.29z"
   id="path2376" />
		<path
   class="st56"
   d="M1285.56,296.71h1.66v1.58h-1.66V296.71z M1287.13,309.71h-1.48v-9.09h1.48V309.71z"
   id="path2378" />
		<path
   class="st56"
   d="M1294.49,300.62h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V300.62z M1292.76,301.66c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1294.53,303.77,1294.62,301.66,1292.76,301.66z"
   id="path2380" />
		<path
   class="st56"
   d="M1303.62,309.71v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1303.62z"
   id="path2382" />
		<path
   class="st56"
   d="M1307.85,300.62v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1307.85z"
   id="path2384" />
		<path
   class="st56"
   d="M1315.37,309.89c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1318.54,309.12,1317.17,309.89,1315.37,309.89z"
   id="path2386" />
	</g>
	<path
   class="st63"
   d="M1219.79,274.98c-4.64,1.24-8.16,5.18-8.8,10.03"
   id="path2390" />
	<line
   class="st64"
   x1="1210.89"
   y1="289.48"
   x2="1210.89"
   y2="296.75"
   id="line2392" />
	<path
   class="st63"
   d="M1211.3,301.31c1.24,4.63,5.18,8.16,10.03,8.79"
   id="path2394" />
	<line
   class="st59"
   x1="1225.84"
   y1="310.2"
   x2="1330.53"
   y2="310.2"
   id="line2396" />
	<path
   class="st63"
   d="M1335.11,309.8c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2398" />
	<line
   class="st64"
   x1="1344"
   y1="295.3"
   x2="1344"
   y2="288.03"
   id="line2400" />
	<path
   class="st63"
   d="M1343.6,283.47c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2402" />
	<line
   class="st59"
   x1="1329.06"
   y1="274.58"
   x2="1224.37"
   y2="274.58"
   id="line2404" />
	<path
   class="st60"
   d="M1210.89,286.58L1210.89,286.58 M1210.89,298.2L1210.89,298.2 M1222.89,310.2L1222.89,310.2 M1332,310.2   L1332,310.2 M1344,298.2L1344,298.2 M1344,286.58L1344,286.58 M1332,274.58L1332,274.58 M1222.89,274.58L1222.89,274.58"
   id="path2406" />
	<path
   class="st56"
   d="M1266.55,234.48c4.8-0.38,14.47-0.37,21.61,0.01c6.31,0.34,11.83-4.17,12.74-10.42l6.55-44.96   c0.9-7.21-4.09-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87   C1254.53,230.08,1260.22,234.81,1266.55,234.48L1266.55,234.48z"
   id="path2408" />
	<line
   class="st61"
   x1="1277.45"
   y1="242.97"
   x2="1277.45"
   y2="259.25"
   id="line2410" />
	<path
   class="st62"
   d="M1277.45,240.01L1277.45,240.01 M1277.45,260.73L1277.45,260.73"
   id="path2412" />
	<path
   d="M1277.45,242.79c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.25-2.78-2.78-2.78c-1.54,0-2.78,1.24-2.78,2.78   C1274.67,241.54,1275.91,242.79,1277.45,242.79L1277.45,242.79z"
   id="path2414" />
	<path
   class="st55"
   d="M1294.95,197.01h-1.04c-0.42-2.73-1.49-5.24-3.06-7.37l0.74-0.74c0.98-0.97,0.98-2.56,0-3.53   c-0.98-0.98-2.56-0.98-3.53,0l-0.75,0.74c-2.12-1.57-4.63-2.64-7.36-3.06v-1.04c0-1.38-1.12-2.5-2.5-2.5s-2.5,1.12-2.5,2.5v1.04   c-2.73,0.41-5.24,1.49-7.37,3.06l-0.74-0.74c-0.98-0.98-2.56-0.98-3.53,0c-0.98,0.98-0.98,2.56,0,3.53l0.74,0.74   c-1.57,2.13-2.65,4.64-3.06,7.37h-1.04c-1.38,0-2.5,1.12-2.5,2.5c0,1.38,1.12,2.5,2.5,2.5h1.04c0.41,2.73,1.49,5.24,3.06,7.37   l-0.74,0.74c-0.98,0.98-0.98,2.56,0,3.54c0.48,0.49,1.12,0.73,1.76,0.73c0.64,0,1.28-0.24,1.77-0.73l0.74-0.74   c2.13,1.57,4.64,2.64,7.37,3.06v1.04c0,1.38,1.12,2.5,2.5,2.5s2.5-1.12,2.5-2.5v-1.04c2.73-0.41,5.24-1.49,7.36-3.06l0.75,0.74   c0.48,0.49,1.12,0.73,1.76,0.73c0.64,0,1.28-0.24,1.77-0.73c0.98-0.98,0.98-2.56,0-3.54l-0.74-0.74c1.57-2.13,2.64-4.64,3.06-7.37   h1.04c1.38,0,2.5-1.12,2.5-2.5C1297.45,198.13,1296.33,197.01,1294.95,197.01L1294.95,197.01z M1277.45,211.18   c-6.43,0-11.67-5.23-11.67-11.67s5.24-11.67,11.67-11.67c6.43,0,11.67,5.23,11.67,11.67S1283.88,211.18,1277.45,211.18   L1277.45,211.18z"
   id="path2416" />
	<path
   class="st55"
   d="M1279.92,208.17v-4.64v-1.24v-3.52c0.67,0.52,1.13,1.25,1.25,2.1c0.06,0.46,0.46,0.8,0.91,0.8   c0.05,0,0.09,0,0.13-0.01c0.51-0.07,0.87-0.54,0.79-1.05c-0.36-2.61-2.7-4.51-5.55-4.51c-2.85,0-5.19,1.9-5.56,4.51   c-0.07,0.51,0.29,0.98,0.79,1.05c0.51,0.07,0.98-0.28,1.05-0.79c0.12-0.85,0.58-1.58,1.25-2.1v3.52v1.24v4.64   c0,0.51,0.41,0.93,0.92,0.93c0.52,0,0.93-0.42,0.93-0.93v-4.64h1.24v4.64c0,0.51,0.41,0.93,0.92,0.93   C1279.51,209.09,1279.92,208.68,1279.92,208.17L1279.92,208.17z"
   id="path2418" />
	<path
   class="st55"
   d="M1277.45,194.87c1.36,0,2.47-1.11,2.47-2.47c0-1.36-1.11-2.47-2.47-2.47c-1.37,0-2.47,1.11-2.47,2.47   C1274.98,193.77,1276.08,194.87,1277.45,194.87L1277.45,194.87z"
   id="path2420" />
	
	
	
	
	
	
	<path
   class="st63"
   d="M996.72,311.32c4.63-1.24,8.16-5.18,8.79-10.03"
   id="path2462" />
	<line
   class="st64"
   x1="1005.61"
   y1="296.82"
   x2="1005.61"
   y2="289.55"
   id="line2464" />
	<path
   class="st63"
   d="M1005.21,284.99c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2466" />
	<a
   id="a12706"
   xlink:href="/child-rights#data"
   target="blank"
   xlink:title="Data on children"
   xlink:show="Data on children"><g
     id="g2434">
		<path
   class="st56"
   d="M911.99,276.62h4c1.66,0,2.85,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24    c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V276.62z M913.65,288.18h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6    h-2.18V288.18z"
   id="path2422" />
		<path
   class="st56"
   d="M927.47,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M924.14,286.92c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C926.03,285.12,924.14,285,924.14,286.92z"
   id="path2424" />
		<path
   class="st56"
   d="M931.95,280.53v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H931.95z"
   id="path2426" />
		<path
   class="st56"
   d="M941.48,288.31h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V288.31z M938.15,286.92c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C940.04,285.12,938.15,285,938.15,286.92z"
   id="path2428" />
		<path
   class="st56"
   d="M949.54,285.21c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C951.07,289.81,949.54,289.23,949.54,285.21z M954.91,284.58c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C954.53,288.6,954.91,287.54,954.91,284.58z"
   id="path2430" />
		<path
   class="st56"
   d="M963.73,289.62v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H963.73z"
   id="path2432" />
	</g><g
     id="g2452">
		<path
   class="st56"
   d="M915.06,305.05c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.02c0,2.95,0.38,4.02,1.91,4.02    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H915.06z"
   id="path2436" />
		<path
   class="st56"
   d="M924.24,311.23v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H924.24z"
   id="path2438" />
		<path
   class="st56"
   d="M928.18,298.23h1.66v1.58h-1.66V298.23z M929.74,311.23h-1.48v-9.09h1.48V311.23z"
   id="path2440" />
		<path
   class="st56"
   d="M933.74,311.23h-1.48v-13h1.48V311.23z"
   id="path2442" />
		<path
   class="st56"
   d="M941.1,298.23h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V298.23z M939.39,303.16c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C941.1,305.1,941.03,303.16,939.39,303.16z"
   id="path2444" />
		<path
   class="st56"
   d="M946.82,303.5h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05s-0.25-0.04-0.4-0.04    c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V303.5z"
   id="path2446" />
		<path
   class="st56"
   d="M952.73,307.16c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62c-0.02,2.02-1.26,2.94-3.17,2.94    c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H952.73z M956.28,306.04    c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H956.28z"
   id="path2448" />
		<path
   class="st56"
   d="M965.22,311.23v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H965.22z"
   id="path2450" />
	</g><path
     class="st63"
     d="M881.39,276.5c-4.63,1.24-8.16,5.18-8.79,10.03"
     id="path2454" /><line
     class="st64"
     x1="872.5"
     y1="291"
     x2="872.5"
     y2="298.27"
     id="line2456" /><path
     class="st63"
     d="M872.91,302.83c1.24,4.63,5.18,8.16,10.03,8.79"
     id="path2458" /><line
     class="st59"
     x1="887.45"
     y1="311.72"
     x2="992.14"
     y2="311.72"
     id="line2460" /><line
     class="st59"
     x1="990.66"
     y1="276.1"
     x2="885.97"
     y2="276.1"
     id="line2468" /></a>
	<path
   class="st60"
   d="M872.5,288.1L872.5,288.1 M872.5,299.72L872.5,299.72 M884.5,311.72L884.5,311.72 M993.61,311.72   L993.61,311.72 M1005.61,299.72L1005.61,299.72 M1005.61,288.1L1005.61,288.1 M993.61,276.1L993.61,276.1 M884.5,276.1L884.5,276.1   "
   id="path2470" />
	
	<line
   class="st61"
   x1="939.06"
   y1="244.49"
   x2="939.06"
   y2="260.77"
   id="line2474" />
	<path
   class="st62"
   d="M939.06,241.53L939.06,241.53 M939.06,262.25L939.06,262.25"
   id="path2476" />
	<path
   d="M939.06,244.31c1.53,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.54,0-2.78,1.24-2.78,2.78   C936.28,243.06,937.52,244.31,939.06,244.31L939.06,244.31z"
   id="path2478" />
	
	
	
	
	<a
   id="a12683"
   xlink:actuate=""
   xlink:href="/child-rights#data"
   xlink:title="Data on children"
   target="blank"
   xlink:show="Data on children"><path
     class="st56"
     d="M928.15,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87   C916.14,230.08,921.83,234.81,928.15,234.48L928.15,234.48z"
     id="path2472" /><path
     class="st55"
     d="M927.67,206.66l-5.23,5.23c-1.17,1.17-1.17,3.08,0,4.24c1.17,1.17,3.08,1.17,4.24,0l5.24-5.24   C930.26,209.74,928.83,208.3,927.67,206.66L927.67,206.66z"
     id="path2480" /><path
     class="st55"
     d="M937.6,196.59h-2.92c-0.4,0-0.73,0.33-0.73,0.73v3.6c0.96,1.78,2.51,3.21,4.38,4.03v-7.63   C938.33,196.92,938,196.59,937.6,196.59L937.6,196.59z"
     id="path2482" /><path
     class="st55"
     d="M949.26,192.22h-2.92c-0.4,0-0.73,0.33-0.73,0.73v12c1.87-0.82,3.41-2.25,4.38-4.03v-7.98   C949.99,192.55,949.66,192.22,949.26,192.22L949.26,192.22z"
     id="path2484" /><path
     class="st55"
     d="M943.43,194.41h-2.92c-0.4,0-0.73,0.33-0.73,0.73v10.31c0.7,0.17,1.43,0.26,2.19,0.26   c0.76,0,1.49-0.09,2.19-0.26v-10.31C944.16,194.73,943.83,194.41,943.43,194.41L943.43,194.41z"
     id="path2486" /><path
     class="st55"
     d="M941.97,182.01c-8.06,0-14.58,6.53-14.58,14.58s6.53,14.58,14.58,14.58c8.06,0,14.58-6.53,14.58-14.58   S950.03,182.01,941.97,182.01L941.97,182.01z M949.99,204.02c-1.19,1.29-2.68,2.3-4.38,2.89c-0.47,0.17-0.95,0.31-1.46,0.41   c-0.71,0.15-1.44,0.22-2.19,0.22c-0.75,0-1.48-0.07-2.19-0.22c-0.5-0.1-0.98-0.24-1.46-0.41c-1.69-0.59-3.19-1.6-4.38-2.89   c-1.82-1.95-2.92-4.56-2.92-7.42c0-6.04,4.9-10.94,10.94-10.94c6.04,0,10.94,4.9,10.94,10.94   C952.91,199.46,951.81,202.07,949.99,204.02L949.99,204.02z"
     id="path2488" /></a>
	<g
   id="g2504">
		<path
   class="st56"
   d="M1083.27,285.17v5.98h-1.66v-13h4.48c2.3,0,3.11,1.62,3.11,3.24c0,1.53-0.85,2.7-2.38,2.97v0.04    c1.5,0.23,2.04,0.74,2.12,3.35c0.02,0.56,0.2,2.59,0.45,3.4h-1.73c-0.47-0.9-0.36-2.59-0.5-4.32c-0.13-1.58-1.4-1.66-1.96-1.66    H1083.27z M1083.27,283.73h2.48c1.19,0,1.76-1.03,1.76-2.16c0-0.94-0.47-1.98-1.75-1.98h-2.5V283.73z"
   id="path2490" />
		<path
   class="st56"
   d="M1091.37,278.15h1.66v1.58h-1.66V278.15z M1092.94,291.15h-1.48v-9.09h1.48V291.15z"
   id="path2492" />
		<path
   class="st56"
   d="M1100.3,282.06h1.48v10.01c0,2.03-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V282.06z M1098.57,283.1c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1100.34,285.21,1100.43,283.1,1098.57,283.1z"
   id="path2494" />
		<path
   class="st56"
   d="M1109.43,291.15v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1109.43z"
   id="path2496" />
		<path
   class="st56"
   d="M1113.66,282.06v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1113.66z"
   id="path2498" />
		<path
   class="st56"
   d="M1122.66,282.06v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1122.66z"
   id="path2500" />
		<path
   class="st56"
   d="M1127.25,286.74c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.02-1.53,4.59-3.46,4.59    C1128.78,291.33,1127.25,290.75,1127.25,286.74z M1132.61,286.11c0-2.48-0.77-3.02-1.91-3.02c-1.13,0-1.91,0.54-1.91,3.02    c0,2.95,0.38,4.02,1.91,4.02C1132.23,290.12,1132.61,289.06,1132.61,286.11z"
   id="path2502" />
	</g>
	<g
   id="g2518">
		<path
   class="st56"
   d="M1083.52,305.03h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    s-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V305.03z"
   id="path2506" />
		<path
   class="st56"
   d="M1089.42,308.68c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.94-3.17,2.94c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77    H1089.42z M1092.97,307.56c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1092.97z"
   id="path2508" />
		<path
   class="st56"
   d="M1101.45,312.75v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1101.45z"
   id="path2510" />
		<path
   class="st56"
   d="M1111.42,308.68c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.94-3.17,2.94c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77    H1111.42z M1114.97,307.56c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1114.97z"
   id="path2512" />
		<path
   class="st56"
   d="M1123.79,299.75h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V299.75z M1122.08,304.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1123.79,306.63,1123.71,304.68,1122.08,304.68z"
   id="path2514" />
		<path
   class="st56"
   d="M1130.72,311.06h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L1130.72,311.06z"
   id="path2516" />
	</g>
	<path
   class="st63"
   d="M1050.59,278.02c-4.63,1.24-8.16,5.18-8.79,10.03"
   id="path2520" />
	<line
   class="st64"
   x1="1041.7"
   y1="292.52"
   x2="1041.7"
   y2="299.79"
   id="line2522" />
	<path
   class="st63"
   d="M1042.1,304.35c1.24,4.63,5.18,8.16,10.03,8.79"
   id="path2524" />
	<line
   class="st59"
   x1="1056.65"
   y1="313.24"
   x2="1161.33"
   y2="313.24"
   id="line2526" />
	<path
   class="st63"
   d="M1165.91,312.84c4.64-1.24,8.16-5.18,8.8-10.03"
   id="path2528" />
	<line
   class="st64"
   x1="1174.81"
   y1="298.34"
   x2="1174.81"
   y2="291.07"
   id="line2530" />
	<path
   class="st63"
   d="M1174.4,286.51c-1.24-4.63-5.18-8.16-10.03-8.79"
   id="path2532" />
	<line
   class="st59"
   x1="1159.86"
   y1="277.62"
   x2="1055.17"
   y2="277.62"
   id="line2534" />
	<path
   class="st60"
   d="M1041.7,289.62L1041.7,289.62 M1041.7,301.24L1041.7,301.24 M1053.7,313.24L1053.7,313.24 M1162.81,313.24   L1162.81,313.24 M1174.81,301.24L1174.81,301.24 M1174.81,289.62L1174.81,289.62 M1162.81,277.62L1162.81,277.62 M1053.7,277.62   L1053.7,277.62"
   id="path2536" />
	<path
   class="st56"
   d="M1097.35,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.89-7.21-4.1-13.45-11.16-13.94c-8.1-0.87-24.95-0.89-37.63-0.03c-7.06,0.48-12.2,6.9-11.2,13.9l6.36,44.87   C1085.33,230.08,1091.03,234.81,1097.35,234.48L1097.35,234.48z"
   id="path2538" />
	<line
   class="st66"
   x1="1108.25"
   y1="246.01"
   x2="1108.25"
   y2="262.29"
   id="line2540" />
	<path
   class="st67"
   d="M1108.25,243.05L1108.25,243.05 M1108.25,263.77L1108.25,263.77"
   id="path2542" />
	<path
   class="st56"
   d="M1108.25,245.83c1.54,0,2.78-1.24,2.78-2.78c0-1.53-1.24-2.78-2.78-2.78c-1.53,0-2.78,1.24-2.78,2.78   C1105.47,244.58,1106.72,245.83,1108.25,245.83L1108.25,245.83z"
   id="path2544" />
	<path
   class="st55"
   d="M1109.84,191.45c0.31,0.31,0.31,0.81,0,1.12l-4.89,4.89c-0.31,0.31-0.81,0.31-1.12,0.01   c-0.31-0.32-0.3-0.82,0-1.13l4.89-4.89C1109.03,191.14,1109.53,191.14,1109.84,191.45L1109.84,191.45z M1112.16,205.79   c0.31,0.31,0.81,0.31,1.12,0l4.89-4.89c0.31-0.31,0.31-0.81,0-1.12c-0.3-0.31-0.81-0.31-1.12,0l-4.89,4.89   C1111.85,204.98,1111.85,205.48,1112.16,205.79L1112.16,205.79z M1123.89,191.62v23.36h-25.4v-0.38l-2.25,2.41l-3.63-3.64l5.88-5.5   v-25.86h16.15L1123.89,191.62L1123.89,191.62z M1115.07,190.84h4.36l-4.36-4.53V190.84L1115.07,190.84z M1121.22,192.84h-8.16   v-8.16h-11.89v20.69l5.97-5.59l-1.79-1.79l5.02-5.03l6.29,6.29l-5.02,5.03l-1.8-1.8l-8.67,9.27v0.56h20.05V192.84L1121.22,192.84z"
   id="path2546" />
	<path
   class="st68"
   d="M50.5,1086.52c-11.05,0-20,8.96-20,20v159.23c0,11.05,8.95,20,20,20h1254c11.05,0,20-8.95,20-20v-159.23   c0-11.04-8.95-20-20-20H50.5L50.5,1086.52z"
   id="path2548" />
	<a
   id="a65343"
   xlink:href="/gender"
   target="blank"
   xlink:title="Gender"
   xlink:show="Gender"><g
     id="g2562">
		<path
   class="st69"
   d="M551.42,1237.87c0-1.53-0.63-2.36-2.3-2.36c-0.52,0-2.4,0.09-2.4,2.81v4.39c0,2.84,0.83,3.57,2.4,3.57    c1.19,0,1.98-0.32,2.32-0.58v-3.89h-2.39v-1.44h4.05v6.32c-1.06,0.58-2.3,0.97-3.98,0.97c-2.75,0-4.09-1.42-4.09-5.02v-4.27    c0-2.59,1.33-4.25,4.09-4.25c2.81,0,4.14,1.03,4.03,3.75H551.42z"
   id="path2550" />
		<path
   class="st69"
   d="M557.47,1243.33c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H557.47    z M561.01,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H561.01z"
   id="path2552" />
		<path
   class="st69"
   d="M569.96,1247.4v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H569.96z"
   id="path2554" />
		<path
   class="st69"
   d="M578.83,1234.4h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1234.4z M577.12,1239.33c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C578.83,1241.28,578.76,1239.33,577.12,1239.33z"
   id="path2556" />
		<path
   class="st69"
   d="M584.47,1243.33c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H584.47    z M588.01,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H588.01z"
   id="path2558" />
		<path
   class="st69"
   d="M593.56,1239.67h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1239.67z"
   id="path2560" />
	</g></a>
	
	
	
	<a
   id="a65334"
   xlink:href="/gender"
   target="blank"
   xlink:title="Gender"
   xlink:show="Gender"><path
     class="st70"
     d="M538.06,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C552.46,1150.96,538.06,1165.36,538.06,1183.12L538.06,1183.12z"
     id="path2564" /><path
     class="st71"
     d="M538.06,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C552.46,1150.96,538.06,1165.36,538.06,1183.12L538.06,1183.12z"
     id="path2566" /><path
     class="st69"
     d="M583.23,1164.08c0-0.51-0.41-0.92-0.92-0.92h-7.79c-0.51,0-0.92,0.41-0.92,0.92v0.75   c0,0.51,0.41,0.92,0.93,0.92l4.31-0.01l-5.98,5.98c-1.63-1.22-3.65-1.95-5.84-1.95c-5.41,0-9.81,4.39-9.81,9.8s4.4,9.81,9.81,9.81   c5.41,0,9.81-4.4,9.81-9.81c0-2.29-0.79-4.39-2.12-6.06l5.95-5.95v4.18c0,0.59,0.48,1.07,1.08,1.07h0.59   c0.51,0,0.93-0.41,0.92-0.92L583.23,1164.08L583.23,1164.08z M567.01,1187.38c-4.31,0-7.81-3.5-7.81-7.81   c0-4.31,3.51-7.81,7.81-7.81c4.31,0,7.81,3.5,7.81,7.81C574.83,1183.88,571.32,1187.38,567.01,1187.38L567.01,1187.38z"
     id="path2568" /><path
     class="st69"
     d="M573.95,1186.53c3.82-3.83,3.82-10.05,0-13.87c-3.82-3.83-10.04-3.83-13.87,0c-3.82,3.82-3.82,10.04,0,13.87   c1.58,1.58,3.57,2.49,5.63,2.77v6.62h-2.67c-0.52,0-0.95,0.43-0.95,0.95v0.72c0,0.53,0.42,0.95,0.95,0.95h2.67v2.68   c0,0.52,0.42,0.94,0.94,0.94h0.74c0.52,0,0.94-0.42,0.94-0.94v-2.68h2.67c0.52,0,0.95-0.42,0.95-0.95v-0.72   c0-0.52-0.42-0.95-0.95-0.95h-2.67v-6.62C570.38,1189.02,572.37,1188.11,573.95,1186.53L573.95,1186.53z M561.49,1185.12   c-3.05-3.05-3.05-8.01,0-11.05c3.05-3.05,8-3.05,11.05,0c3.05,3.04,3.05,8,0,11.05C569.49,1188.16,564.54,1188.16,561.49,1185.12   L561.49,1185.12z"
     id="path2570" /></a>
	<a
   id="a65328"
   xlink:title="Disability"
   xlink:show="Disability"
   target="blank"
   xlink:href="/disability"><g
     id="g2592">
		<path
   class="st69"
   d="M322.55,1234.81h4c1.66,0,2.84,0.59,3.49,1.98c0.52,1.1,0.58,3.69,0.58,4.11c0,2.77-0.25,4.38-0.79,5.24    c-0.7,1.12-2.02,1.67-4.29,1.67h-2.99V1234.81z M324.2,1246.37h1.57c2.3,0,3.15-0.86,3.15-3.89v-2.63c0-2.63-0.81-3.6-2.54-3.6    h-2.18V1246.37z"
   id="path2572" />
		<path
   class="st69"
   d="M333.22,1234.81h1.66v1.58h-1.66V1234.81z M334.79,1247.81h-1.48v-9.09h1.48V1247.81z"
   id="path2574" />
		<path
   class="st69"
   d="M340.03,1247.99c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.4,0.43-1.4,1.22c0,1.6,4.54,1.57,4.54,4.34C343.19,1247.22,341.83,1247.99,340.03,1247.99z"
   id="path2576" />
		<path
   class="st69"
   d="M350.02,1246.5h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1246.5z M346.69,1245.11c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C348.58,1243.31,346.69,1243.19,346.69,1245.11z"
   id="path2578" />
		<path
   class="st69"
   d="M355.94,1247.81h-1.48v-13h1.48v4.83h0.05c0.5-0.72,1.13-1.1,2-1.1c2.93,0,3.01,2.61,3.01,4.88    c0,4-1.48,4.57-2.94,4.57c-0.95,0-1.58-0.41-2.09-1.26h-0.04V1247.81z M357.59,1246.79c1.85,0,1.85-1.98,1.85-3.35    c0-2.43-0.22-3.69-1.8-3.69c-1.64,0-1.71,1.94-1.71,3.15C355.94,1244.28,355.77,1246.79,357.59,1246.79z"
   id="path2580" />
		<path
   class="st69"
   d="M363.21,1234.81h1.66v1.58h-1.66V1234.81z M364.77,1247.81h-1.48v-9.09h1.48V1247.81z"
   id="path2582" />
		<path
   class="st69"
   d="M368.77,1247.81h-1.48v-13h1.48V1247.81z"
   id="path2584" />
		<path
   class="st69"
   d="M371.2,1234.81h1.66v1.58h-1.66V1234.81z M372.77,1247.81h-1.48v-9.09h1.48V1247.81z"
   id="path2586" />
		<path
   class="st69"
   d="M375.48,1238.72v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H375.48z"
   id="path2588" />
		<path
   class="st69"
   d="M383.06,1246.12h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L383.06,1246.12z"
   id="path2590" />
	</g></a>
	
	
	
	
	<a
   id="a65286"
   xlink:href="/disability"
   target="blank"
   xlink:title="Disability"
   xlink:show="Disability"><path
     class="st70"
     d="M321.88,1183.12c0,17.77,14.4,32.17,32.17,32.17c17.76,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C336.28,1150.96,321.88,1165.36,321.88,1183.12L321.88,1183.12z"
     id="path2594" /><path
     class="st71"
     d="M321.88,1183.12c0,17.77,14.4,32.17,32.17,32.17c17.76,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C336.28,1150.96,321.88,1165.36,321.88,1183.12L321.88,1183.12z"
     id="path2596" /><path
     class="st69"
     d="M355.04,1170.29c0,2.33-1.88,4.21-4.21,4.21c-2.32,0-4.21-1.88-4.21-4.21c0-2.32,1.88-4.21,4.21-4.21   C353.15,1166.08,355.04,1167.97,355.04,1170.29L355.04,1170.29z"
     id="path2598" /><path
     class="st69"
     d="M365.33,1193.25h-2.29c0,0-1.39-3.97-1.78-5.02c-0.25-0.7-0.9-1.21-1.68-1.21h-5.56v-3.9h5.28   c0.7,0,1.27-0.57,1.27-1.27c0-0.71-0.57-1.28-1.27-1.28h-5.28c0,0-0.3-4.64-2.92-4.64c-1.79,0-2.41,1.47-2.41,3.27v8.18   c0,1.8,1.46,3.26,3.25,3.26c0.05,0,0.1-0.02,0.15-0.02c0.05,0,0.1,0.02,0.15,0.02h6.78l2.26,5.67h4.05c0.84,0,1.52-0.69,1.52-1.53   C366.85,1193.94,366.17,1193.25,365.33,1193.25L365.33,1193.25z"
     id="path2600" /><path
     class="st69"
     d="M358.07,1192.62c-0.97,3.12-3.82,5.41-7.22,5.41c-4.19,0-7.6-3.45-7.6-7.7c0-2.86,1.57-5.34,3.86-6.66l0,0h0   v-8.43h-0.71h-0.71h-3.53c-0.39,0-0.7,0.32-0.7,0.72c0,0.39,0.32,0.71,0.7,0.71h3.53v5.44c-2.68,1.73-4.47,4.76-4.47,8.22   c0,5.38,4.32,9.75,9.63,9.75c3.52,0,6.58-1.95,8.26-4.82L358.07,1192.62L358.07,1192.62z"
     id="path2602" /></a>
	
	<a
   id="a65315"
   xlink:title="Early Childhood Development"
   xlink:show="Early Childhood Development"
   target="blank"
   xlink:href="/ecd"><g
     id="g2632">
		<path
   class="st69"
   d="M83.82,1240.61v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H83.82z"
   id="path2604" />
		<path
   class="st69"
   d="M97.34,1239.29h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.48-1.24-2.48-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1239.29z M94.01,1237.91c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C95.9,1236.11,94.01,1235.98,94.01,1237.91z"
   id="path2606" />
		<path
   class="st69"
   d="M103.19,1232.88h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1232.88z"
   id="path2608" />
		<path
   class="st69"
   d="M109.1,1240.61h-1.48v-13h1.48V1240.61z"
   id="path2610" />
		<path
   class="st69"
   d="M114.39,1238.92h0.04l2.18-7.4h1.6l-4.12,12.53h-1.53l1.03-3.44l-3.08-9.09h1.71L114.39,1238.92z"
   id="path2612" />
		<path
   class="st69"
   d="M128.39,1234.43c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H128.39z"
   id="path2614" />
		<path
   class="st69"
   d="M137.57,1240.61v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H137.57z"
   id="path2616" />
		<path
   class="st69"
   d="M141.51,1227.61h1.66v1.58h-1.66V1227.61z M143.08,1240.61h-1.48v-9.09h1.48V1240.61z"
   id="path2618" />
		<path
   class="st69"
   d="M147.07,1240.61h-1.48v-13h1.48V1240.61z"
   id="path2620" />
		<path
   class="st69"
   d="M154.44,1227.61h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1227.61z M152.73,1232.54c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C154.44,1234.49,154.37,1232.54,152.73,1232.54z"
   id="path2622" />
		<path
   class="st69"
   d="M163.56,1240.61v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H163.56z"
   id="path2624" />
		<path
   class="st69"
   d="M167.38,1236.2c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C168.91,1240.79,167.38,1240.21,167.38,1236.2z M172.74,1235.57c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C172.37,1239.58,172.74,1238.52,172.74,1235.57z"
   id="path2626" />
		<path
   class="st69"
   d="M176.38,1236.2c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C177.91,1240.79,176.38,1240.21,176.38,1236.2z M181.74,1235.57c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C181.37,1239.58,181.74,1238.52,181.74,1235.57z"
   id="path2628" />
		<path
   class="st69"
   d="M190.44,1227.61h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1227.61z M188.73,1232.54c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C190.44,1234.49,190.37,1232.54,188.73,1232.54z"
   id="path2630" />
	</g><g
     id="g2656">
		<path
   class="st69"
   d="M97.46,1249.21h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.93-0.58-2.93-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.49,0.38,2,1.1h0.05V1249.21z M95.75,1254.14c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C97.46,1256.09,97.39,1254.14,95.75,1254.14z"
   id="path2634" />
		<path
   class="st69"
   d="M103.09,1258.14c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H103.09    z M106.64,1257.03c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H106.64z"
   id="path2636" />
		<path
   class="st69"
   d="M109.61,1253.12h1.66l2.03,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L109.61,1253.12z"
   id="path2638" />
		<path
   class="st69"
   d="M120.09,1258.14c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H120.09    z M123.63,1257.03c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H123.63z"
   id="path2640" />
		<path
   class="st69"
   d="M129.09,1262.21h-1.48v-13h1.48V1262.21z"
   id="path2642" />
		<path
   class="st69"
   d="M131.39,1257.8c0-2.67,0.31-4.86,3.46-4.86s3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C132.92,1262.39,131.39,1261.81,131.39,1257.8z M136.75,1257.17c0-2.49-0.77-3.03-1.91-3.03s-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C136.38,1261.18,136.75,1260.12,136.75,1257.17z"
   id="path2644" />
		<path
   class="st69"
   d="M142.24,1254.2h0.04c0.5-0.85,1.13-1.26,2.09-1.26c1.46,0,2.94,0.58,2.94,4.57c0,2.27-0.07,4.88-3.01,4.88    c-0.86,0-1.49-0.38-2-1.1h-0.05v4.36h-1.48v-12.53h1.48V1254.2z M145.75,1257.51c0-1.37,0-3.37-1.85-3.37    c-1.82,0-1.66,2.52-1.66,3.91c0,1.21,0.07,3.13,1.71,3.13C145.54,1261.18,145.75,1259.94,145.75,1257.51z"
   id="path2646" />
		<path
   class="st69"
   d="M154.11,1262.21v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H154.11z"
   id="path2648" />
		<path
   class="st69"
   d="M164.08,1258.14c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H164.08    z M167.62,1257.03c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H167.62z"
   id="path2650" />
		<path
   class="st69"
   d="M176.57,1262.21v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H176.57z"
   id="path2652" />
		<path
   class="st69"
   d="M180.8,1253.12v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.03-0.58-2.03-1.62v-6.46h-1.49v-1.12H180.8z"
   id="path2654" />
	</g></a>
	
	
	
	
	
	
	
	<a
   id="a65279"
   xlink:href="/ecd"
   target="blank"
   xlink:title="Early Childhood Development"
   xlink:show="Early Childhood Development"><path
     class="st70"
     d="M105.69,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.17-14.4,32.17-32.17c0-17.76-14.4-32.16-32.17-32.16   S105.69,1165.36,105.69,1183.12L105.69,1183.12z"
     id="path2658" /><path
     class="st71"
     d="M105.69,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.17-14.4,32.17-32.17c0-17.76-14.4-32.16-32.17-32.16   S105.69,1165.36,105.69,1183.12L105.69,1183.12z"
     id="path2660" /><path
     class="st69"
     d="M137.19,1190.06c0,0,3.34,3.35,3.36,3.35c1.07,1.08,0.79,2.96-0.22,3.99l-4.67,4.87   c-1.8,1.79-4.21-0.7-2.46-2.44l2.96-2.96l-2.9-2.88L137.19,1190.06L137.19,1190.06L137.19,1190.06z M126.79,1190.06L126.79,1190.06   l-3.34,3.35c-1.08,1.08-0.8,2.96,0.2,3.99l4.68,4.87c1.8,1.79,4.2-0.7,2.46-2.44l-2.96-2.96l2.88-2.88L126.79,1190.06   L126.79,1190.06z M132.11,1177.6c2.68,0,4.85-2.17,4.85-4.86c0-2.68-2.17-4.85-4.85-4.85c-2.68,0-4.86,2.17-4.86,4.85   C127.25,1175.43,129.42,1177.6,132.11,1177.6L132.11,1177.6z M137.37,1188.11l0.07-3.31l4.03,3.77c0.33,0.31,0.75,0.46,1.17,0.46   c0.46,0,0.92-0.18,1.26-0.55c0.65-0.69,0.61-1.78-0.08-2.43c0,0-4.63-5.02-5.29-5.61c-1.23-1.09-3.04-1.71-5.97-1.71h-0.92   c-2.93,0-4.73,0.62-5.97,1.71c-0.66,0.59-5.29,5.61-5.29,5.61c-0.69,0.65-0.73,1.74-0.08,2.43c0.34,0.37,0.8,0.55,1.26,0.55   c0.42,0,0.84-0.15,1.17-0.46l4.03-3.77l0.07,3.31H137.37L137.37,1188.11z"
     id="path2662" /><path
     class="st69"
     d="M146.25,1176.03v5.36c0,0.66,0.54,1.2,1.2,1.2h5.36c0.66,0,1.2-0.54,1.2-1.2v-5.36c0-0.66-0.54-1.2-1.2-1.2   h-5.36C146.79,1174.83,146.25,1175.37,146.25,1176.03L146.25,1176.03z M150.63,1180.63l-0.07-0.39h-0.02   c-0.25,0.31-0.65,0.48-1.11,0.48c-0.78,0-1.25-0.57-1.25-1.19c0-1,0.9-1.48,2.26-1.47V1178c0-0.2-0.11-0.49-0.7-0.49   c-0.4,0-0.81,0.13-1.07,0.29l-0.22-0.78c0.27-0.14,0.8-0.33,1.5-0.33c1.28,0,1.7,0.75,1.7,1.66v1.34c0,0.37,0.02,0.73,0.05,0.94   H150.63L150.63,1180.63z"
     id="path2664" /><path
     class="st69"
     d="M148.1,1184.94v5.3c0,0.68,0.55,1.23,1.23,1.23h5.3c0.68,0,1.23-0.55,1.23-1.23v-5.3   c0-0.68-0.55-1.23-1.23-1.23h-5.3C148.65,1183.71,148.1,1184.26,148.1,1184.94L148.1,1184.94z M152.38,1190.14   c-0.45,0-0.88-0.16-1.16-0.62h-0.02l-0.05,0.54h-1.02c0.02-0.26,0.03-0.72,0.03-1.15v-4.45h1.2v2.2h0.02   c0.23-0.33,0.63-0.55,1.17-0.55c0.92,0,1.6,0.77,1.59,1.95C154.14,1189.45,153.26,1190.14,152.38,1190.14L152.38,1190.14z"
     id="path2666" /><path
     class="st69"
     d="M145.8,1193.83v5.28c0,0.69,0.55,1.24,1.24,1.24h5.28c0.68,0,1.24-0.55,1.24-1.24v-5.28   c0-0.68-0.56-1.24-1.24-1.24h-5.28C146.36,1192.59,145.8,1193.15,145.8,1193.83L145.8,1193.83z M149.9,1197.47   c0.28,0,0.51-0.04,0.69-0.12l0.14,0.89c-0.21,0.09-0.62,0.18-1.07,0.18c-1.25,0-2.04-0.77-2.04-1.98c0-1.13,0.77-2.05,2.21-2.05   c0.32,0,0.66,0.05,0.92,0.15l-0.19,0.89c-0.14-0.06-0.36-0.12-0.67-0.12c-0.63,0-1.04,0.45-1.03,1.08   C148.84,1197.1,149.32,1197.47,149.9,1197.47L149.9,1197.47z"
     id="path2668" /><path
     class="st69"
     d="M152.48,1186.94c-0.32,0-0.62,0.25-0.7,0.59c-0.02,0.07-0.02,0.14-0.02,0.22v0.57c0,0.08,0.01,0.15,0.02,0.21   c0.08,0.33,0.36,0.57,0.7,0.57c0.51,0,0.83-0.39,0.83-1.09C153.31,1187.41,153.04,1186.94,152.48,1186.94L152.48,1186.94z"
     id="path2670" /><path
     class="st69"
     d="M149.31,1179.48c0,0.31,0.2,0.46,0.47,0.46c0.3,0,0.54-0.2,0.62-0.44c0.02-0.06,0.02-0.14,0.02-0.21v-0.41   C149.8,1178.87,149.31,1179.02,149.31,1179.48L149.31,1179.48z"
     id="path2672" /></a>
	<a
   id="a65365"
   xlink:show="Adolescents"
   xlink:title="Adolescents"
   target="blank"
   xlink:href="/adolescent"><g
     id="g2696">
		<path
   class="st69"
   d="M745.81,1234.4h2.11l4.23,13h-1.85l-0.94-3.1h-5.02l-0.97,3.1h-1.67L745.81,1234.4z M746.82,1235.93h-0.04    l-2.03,6.93h4.16L746.82,1235.93z"
   id="path2674" />
		<path
   class="st69"
   d="M758.52,1234.4H760v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V1234.4z M756.81,1239.33c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C758.52,1241.28,758.45,1239.33,756.81,1239.33z"
   id="path2676" />
		<path
   class="st69"
   d="M762.46,1242.99c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C763.99,1247.58,762.46,1247,762.46,1242.99z M767.83,1242.36c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C767.45,1246.37,767.83,1245.31,767.83,1242.36z"
   id="path2678" />
		<path
   class="st69"
   d="M773.15,1247.4h-1.48v-13h1.48V1247.4z"
   id="path2680" />
		<path
   class="st69"
   d="M777.15,1243.33c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H777.15    z M780.7,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H780.7z"
   id="path2682" />
		<path
   class="st69"
   d="M787.39,1247.58c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C790.56,1246.8,789.19,1247.58,787.39,1247.58z"
   id="path2684" />
		<path
   class="st69"
   d="M797.46,1241.22c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H797.46z"
   id="path2686" />
		<path
   class="st69"
   d="M803.14,1243.33c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H803.14    z M806.69,1242.21c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H806.69z"
   id="path2688" />
		<path
   class="st69"
   d="M815.63,1247.4v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H815.63z"
   id="path2690" />
		<path
   class="st69"
   d="M819.86,1238.31v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H819.86z"
   id="path2692" />
		<path
   class="st69"
   d="M827.39,1247.58c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C830.56,1246.8,829.19,1247.58,827.39,1247.58z"
   id="path2694" />
	</g></a>
	
	
	
	
	
	<a
   id="a65351"
   xlink:href="/adolescent"
   target="blank"
   xlink:title="Adolescents"
   xlink:show="Adolescents"><path
     class="st70"
     d="M754.25,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.16-14.4,32.16-32.17c0-17.76-14.4-32.16-32.16-32.16   S754.25,1165.36,754.25,1183.12L754.25,1183.12z"
     id="path2698" /><path
     class="st71"
     d="M754.25,1183.12c0,17.77,14.4,32.17,32.16,32.17s32.16-14.4,32.16-32.17c0-17.76-14.4-32.16-32.16-32.16   S754.25,1165.36,754.25,1183.12L754.25,1183.12z"
     id="path2700" /><path
     class="st69"
     d="M792.09,1195.83v-7.1v-1.89v-5.38c-1.02,0.79-1.72,1.91-1.91,3.21c-0.1,0.71-0.71,1.22-1.4,1.22   c-0.07,0-0.13,0-0.2-0.01c-0.78-0.11-1.32-0.83-1.21-1.6c0.56-4,4.14-6.9,8.5-6.9c4.36,0,7.94,2.9,8.5,6.9   c0.11,0.77-0.43,1.49-1.21,1.6c-0.78,0.11-1.49-0.43-1.6-1.21c-0.18-1.3-0.88-2.42-1.91-3.21v5.38v1.89v7.1   c0,0.78-0.63,1.42-1.42,1.42c-0.78,0-1.42-0.64-1.42-1.42v-7.1h-1.89v7.1c0,0.78-0.64,1.42-1.42,1.42   C792.72,1197.25,792.09,1196.61,792.09,1195.83L792.09,1195.83z"
     id="path2702" /><path
     class="st69"
     d="M795.87,1175.49c-2.09,0-3.78-1.69-3.78-3.78s1.69-3.79,3.78-3.79c2.09,0,3.78,1.7,3.78,3.79   S797.96,1175.49,795.87,1175.49L795.87,1175.49z"
     id="path2704" /><path
     class="st69"
     d="M777.9,1171.72c5.39,0,9.46,3.84,9.46,8.97c0,0.79-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.63-1.42-1.42   c0-2.35-1.28-4.28-3.25-5.32l2.18,11.35c0.07,0.57-0.37,1.07-0.94,1.07h-0.82v8.04c0,0.78-0.64,1.42-1.42,1.42   c-0.78,0-1.42-0.64-1.42-1.42v-8.04h-1.89v8.04c0,0.78-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.64-1.42-1.42v-8.04h-0.82   c-0.57,0-1.01-0.5-0.94-1.07l2.18-11.36c-1.98,1.05-3.26,2.97-3.26,5.33c0,0.79-0.64,1.42-1.42,1.42c-0.78,0-1.42-0.63-1.42-1.42   C768.45,1175.56,772.51,1171.72,777.9,1171.72L777.9,1171.72z"
     id="path2706" /><path
     class="st69"
     d="M777.91,1169.81c-2.09,0-3.78-1.69-3.78-3.78c0-2.09,1.69-3.78,3.78-3.78c2.09,0,3.78,1.69,3.78,3.78   C781.69,1168.12,779.99,1169.81,777.91,1169.81L777.91,1169.81z"
     id="path2708" /></a>
	
	<a
   id="a65415"
   xlink:show="Environment and Climate Change"
   xlink:title="Environment and Climate Change"
   target="blank"
   xlink:href="/climate"><g
     id="g2738">
		<path
   class="st69"
   d="M943.57,1239.74v-13h6.7v1.44h-5.04v4.18h4.68v1.44h-4.68v4.5h5.15v1.44H943.57z"
   id="path2710" />
		<path
   class="st69"
   d="M957.34,1239.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H957.34z"
   id="path2712" />
		<path
   class="st69"
   d="M960.36,1230.65h1.66l2.04,7.71h0.04l2.2-7.71h1.55l-2.84,9.09h-1.93L960.36,1230.65z"
   id="path2714" />
		<path
   class="st69"
   d="M969.27,1226.74h1.66v1.58h-1.66V1226.74z M970.84,1239.74h-1.48v-9.09h1.48V1239.74z"
   id="path2716" />
		<path
   class="st69"
   d="M974.92,1232.02h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1232.02z"
   id="path2718" />
		<path
   class="st69"
   d="M979.13,1235.33c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C980.66,1239.92,979.13,1239.35,979.13,1235.33z M984.5,1234.7c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C984.12,1238.72,984.5,1237.65,984.5,1234.7z"
   id="path2720" />
		<path
   class="st69"
   d="M993.32,1239.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H993.32z"
   id="path2722" />
		<path
   class="st69"
   d="M1001.85,1239.74v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1001.85z"
   id="path2724" />
		<path
   class="st69"
   d="M1011.82,1235.67c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77    H1011.82z M1015.37,1234.56c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1015.37z"
   id="path2726" />
		<path
   class="st69"
   d="M1024.31,1239.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1024.31z"
   id="path2728" />
		<path
   class="st69"
   d="M1028.54,1230.65v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1028.54z"
   id="path2730" />
		<path
   class="st69"
   d="M1042.06,1238.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1238.43z M1038.73,1237.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1040.62,1235.24,1038.73,1235.12,1038.73,1237.04z"
   id="path2732" />
		<path
   class="st69"
   d="M1051.31,1239.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1051.31z"
   id="path2734" />
		<path
   class="st69"
   d="M1060.19,1226.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V1226.74z M1058.48,1231.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1060.19,1233.62,1060.12,1231.68,1058.48,1231.68z"
   id="path2736" />
	</g><g
     id="g2766">
		<path
   class="st69"
   d="M953.15,1255.17c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H953.15z"
   id="path2740" />
		<path
   class="st69"
   d="M958.84,1261.34h-1.48v-13h1.48V1261.34z"
   id="path2742" />
		<path
   class="st69"
   d="M961.27,1248.34h1.66v1.58h-1.66V1248.34z M962.83,1261.34h-1.48v-9.09h1.48V1261.34z"
   id="path2744" />
		<path
   class="st69"
   d="M969.85,1261.34v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H969.85z"
   id="path2746" />
		<path
   class="st69"
   d="M983.06,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M979.73,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C981.62,1256.84,979.73,1256.72,979.73,1258.64z"
   id="path2748" />
		<path
   class="st69"
   d="M987.54,1252.25v-1.75l1.48-0.67v2.41H991v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H987.54z"
   id="path2750" />
		<path
   class="st69"
   d="M993.83,1257.27c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77H993.83    z M997.38,1256.16c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H997.38z"
   id="path2752" />
		<path
   class="st69"
   d="M1010.14,1255.17c0.04-1.49-0.7-1.89-1.26-1.89c-1.13,0-1.91,0.54-1.91,3.03c0,2.95,0.38,4.01,1.91,4.01    c0.34,0,1.37-0.36,1.31-2h1.55c0.05,2.56-1.85,3.21-2.86,3.21c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86    c1.82,0,2.88,1.06,2.79,3.1H1010.14z"
   id="path2754" />
		<path
   class="st69"
   d="M1019.32,1261.34v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1019.32z"
   id="path2756" />
		<path
   class="st69"
   d="M1028.06,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M1024.73,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1026.62,1256.84,1024.73,1256.72,1024.73,1258.64z"
   id="path2758" />
		<path
   class="st69"
   d="M1037.32,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1037.32z"
   id="path2760" />
		<path
   class="st69"
   d="M1046.19,1252.25h1.48v10.01c0,2.04-1.35,2.52-3.35,2.52c-1.51,0-2.88-0.76-2.75-2.43h1.66    c0.02,0.85,0.58,1.31,1.39,1.31c1.03,0,1.58-0.63,1.58-1.57v-1.89h-0.05c-0.38,0.72-1.21,1.13-2,1.13c-2.47,0-2.95-2.12-2.95-4.83    c0-4.18,2.11-4.45,2.84-4.45c0.95,0,1.71,0.41,2.12,1.3h0.04V1252.25z M1044.46,1253.29c-1.67,0-1.73,2.02-1.73,3.22    c0,2.92,0.67,3.6,1.76,3.6c1.78,0,1.73-2.11,1.73-3.37C1046.23,1255.4,1046.32,1253.29,1044.46,1253.29z"
   id="path2762" />
		<path
   class="st69"
   d="M1051.82,1257.27c0,2.54,0.68,3.04,1.84,3.04c1.01,0,1.53-0.81,1.58-1.73h1.62    c-0.02,2.02-1.26,2.93-3.17,2.93c-1.93,0-3.46-0.58-3.46-4.59c0-2.67,0.31-4.86,3.46-4.86c2.59,0,3.24,1.42,3.24,4.43v0.77    H1051.82z M1055.37,1256.16c0-2.65-0.74-2.97-1.82-2.97c-0.94,0-1.71,0.45-1.73,2.97H1055.37z"
   id="path2764" />
	</g></a>
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	<a
   id="a65384"
   xlink:href="/climate"
   target="blank"
   xlink:title="Environment and Climate Change"
   xlink:show="Environment and Climate Change"><path
     class="st70"
     d="M968.61,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C983.01,1150.96,968.61,1165.36,968.61,1183.12L968.61,1183.12z"
     id="path2768" /><path
     class="st71"
     d="M968.61,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C983.01,1150.96,968.61,1165.36,968.61,1183.12L968.61,1183.12z"
     id="path2770" /><path
     class="st69"
     d="M989.67,1186.47l3.58-0.89l1.78-4.47l2.68-2.69l2.69,0.9l1.78-1.79l1.79,1.79l1.79,4.47l3.58,1.79l2.96,8.15   c-0.09,0.01-0.18,0.02-0.29,0.02c-0.83,0-1.15-0.31-1.86-1c-0.84-0.8-2.1-2.01-4.39-2.01c-2.3,0-3.56,1.21-4.39,2.01   c-0.71,0.69-1.04,1-1.87,1s-1.16-0.31-1.87-1c-0.81-0.77-2.03-1.94-4.21-2l-0.17-0.7l0.89-2.69l-3.58,0.9l-1.4,4.2   c-0.11,0.1-0.21,0.2-0.31,0.29c-0.71,0.69-1.03,1-1.86,1c-0.08,0-0.16,0.01-0.24,0.02L989.67,1186.47L989.67,1186.47z    M997.71,1185.58l3.58,3.57v-2.68l-2.68-3.58v-2.68l-1.79,1.79l-1.79,3.58H997.71L997.71,1185.58z"
     id="path2772" /><path
     class="st69"
     d="M986.99,1197.39c1.94,0,2.95-0.97,3.77-1.76c0.75-0.72,1.29-1.24,2.48-1.24c1.19,0,1.74,0.52,2.49,1.24   c0.82,0.79,1.83,1.76,3.77,1.76c1.94,0,2.95-0.97,3.77-1.76c0.75-0.72,1.3-1.24,2.49-1.24c1.19,0,1.73,0.52,2.48,1.24   c0.82,0.79,1.84,1.76,3.77,1.76c1.94,0,2.96-0.97,3.78-1.76c0.75-0.72,1.29-1.24,2.48-1.24c1.19,0,1.74,0.52,2.49,1.24   c0.82,0.79,1.83,1.76,3.77,1.76c0.51,0,0.93-0.41,0.93-0.93c0-0.51-0.42-0.92-0.93-0.92c-1.19,0-1.73-0.53-2.49-1.25   c-0.81-0.78-1.83-1.76-3.77-1.76c-1.94,0-2.95,0.98-3.77,1.76c-0.75,0.72-1.3,1.25-2.49,1.25c-1.19,0-1.73-0.53-2.48-1.25   c-0.82-0.78-1.84-1.76-3.77-1.76c-1.94,0-2.96,0.98-3.77,1.76c-0.76,0.72-1.3,1.25-2.49,1.25c-1.19,0-1.73-0.53-2.49-1.25   c-0.81-0.78-1.83-1.76-3.77-1.76c-1.93,0-2.95,0.98-3.77,1.76c-0.75,0.72-1.29,1.25-2.48,1.25c-0.51,0-0.93,0.41-0.93,0.92   C986.06,1196.98,986.48,1197.39,986.99,1197.39L986.99,1197.39z"
     id="path2774" /><path
     class="st69"
     d="M986.99,1200.97c1.94,0,2.95-0.98,3.77-1.76c0.75-0.72,1.29-1.25,2.48-1.25c1.19,0,1.74,0.53,2.49,1.25   c0.82,0.78,1.83,1.76,3.77,1.76c1.94,0,2.95-0.98,3.77-1.76c0.75-0.72,1.3-1.25,2.49-1.25c1.19,0,1.73,0.53,2.48,1.25   c0.82,0.78,1.84,1.76,3.77,1.76c1.94,0,2.96-0.98,3.78-1.76c0.75-0.72,1.29-1.25,2.48-1.25c1.19,0,1.74,0.53,2.49,1.25   c0.82,0.78,1.83,1.76,3.77,1.76c0.51,0,0.93-0.42,0.93-0.93s-0.42-0.93-0.93-0.93c-1.19,0-1.73-0.52-2.49-1.24   c-0.81-0.79-1.83-1.76-3.77-1.76c-1.94,0-2.95,0.97-3.77,1.76c-0.75,0.72-1.3,1.24-2.49,1.24c-1.19,0-1.73-0.52-2.48-1.24   c-0.82-0.79-1.84-1.76-3.77-1.76c-1.94,0-2.96,0.97-3.77,1.76c-0.76,0.72-1.3,1.24-2.49,1.24c-1.19,0-1.73-0.52-2.49-1.24   c-0.81-0.79-1.83-1.76-3.77-1.76c-1.93,0-2.95,0.97-3.77,1.76c-0.75,0.72-1.29,1.24-2.48,1.24c-0.51,0-0.93,0.42-0.93,0.93   S986.48,1200.97,986.99,1200.97L986.99,1200.97z"
     id="path2776" /><path
     class="st69"
     d="M991.41,1169.21c0.44,0,0.81-0.37,0.81-0.81v-1.62c0-0.45-0.37-0.81-0.81-0.81c-0.45,0-0.81,0.36-0.81,0.81   v1.62C990.6,1168.84,990.96,1169.21,991.41,1169.21L991.41,1169.21z"
     id="path2778" /><path
     class="st69"
     d="M990.6,1177.03v1.62c0,0.45,0.36,0.81,0.81,0.81c0.44,0,0.81-0.36,0.81-0.81v-1.62   c0-0.45-0.37-0.81-0.81-0.81C990.96,1176.22,990.6,1176.58,990.6,1177.03L990.6,1177.03z"
     id="path2780" /><path
     class="st69"
     d="M995.03,1170.23l1.15-1.14c0.31-0.32,0.31-0.83,0-1.15c-0.32-0.31-0.83-0.31-1.15,0l-1.14,1.15   c-0.32,0.31-0.32,0.83,0,1.14C994.2,1170.55,994.72,1170.55,995.03,1170.23L995.03,1170.23z"
     id="path2782" /><path
     class="st69"
     d="M987.78,1175.19l-1.14,1.15c-0.32,0.31-0.32,0.83,0,1.14c0.31,0.32,0.83,0.32,1.14,0l1.15-1.14   c0.31-0.32,0.31-0.83,0-1.15C988.61,1174.88,988.1,1174.88,987.78,1175.19L987.78,1175.19z"
     id="path2784" /><path
     class="st69"
     d="M994.92,1172.71c0,0.45,0.36,0.81,0.81,0.81h1.61c0.45,0,0.81-0.36,0.81-0.81c0-0.44-0.36-0.81-0.81-0.81   h-1.61C995.28,1171.9,994.92,1172.27,994.92,1172.71L994.92,1172.71z"
     id="path2786" /><path
     class="st69"
     d="M985.47,1173.52h1.62c0.45,0,0.81-0.36,0.81-0.81c0-0.44-0.36-0.81-0.81-0.81h-1.62   c-0.45,0-0.81,0.37-0.81,0.81C984.66,1173.16,985.02,1173.52,985.47,1173.52L985.47,1173.52z"
     id="path2788" /><path
     class="st69"
     d="M993.89,1175.19c-0.32,0.32-0.32,0.83,0,1.15l1.14,1.14c0.32,0.32,0.83,0.32,1.15,0   c0.31-0.31,0.31-0.83,0-1.14l-1.15-1.15C994.72,1174.88,994.2,1174.88,993.89,1175.19L993.89,1175.19z"
     id="path2790" /><path
     class="st69"
     d="M987.78,1170.23c0.32,0.32,0.83,0.32,1.15,0c0.31-0.31,0.31-0.83,0-1.14l-1.15-1.15   c-0.31-0.31-0.83-0.31-1.14,0c-0.32,0.32-0.32,0.83,0,1.15L987.78,1170.23L987.78,1170.23z"
     id="path2792" /><path
     class="st69"
     d="M991.41,1175.14c1.34,0,2.43-1.09,2.43-2.43c0-1.34-1.09-2.43-2.43-2.43c-1.34,0-2.43,1.09-2.43,2.43   C988.98,1174.05,990.07,1175.14,991.41,1175.14L991.41,1175.14z"
     id="path2794" /><path
     class="st69"
     d="M1018.65,1176.03c0-1.36-1.11-2.46-2.46-2.46c-1.36,0-2.46,1.1-2.46,2.46v9.49   c-0.73,0.68-1.14,1.62-1.14,2.62c0,1.98,1.62,3.59,3.6,3.59c1.98,0,3.59-1.61,3.59-3.59c0-1-0.41-1.94-1.13-2.62V1176.03   L1018.65,1176.03z M1016.19,1190.6c-1.36,0-2.46-1.11-2.46-2.46c0-0.75,0.34-1.45,0.92-1.92l0.21-0.17v-10.02   c0-0.73,0.6-1.33,1.33-1.33s1.32,0.6,1.32,1.33v10.02l0.22,0.17c0.58,0.47,0.92,1.17,0.92,1.92   C1018.65,1189.49,1017.54,1190.6,1016.19,1190.6L1016.19,1190.6z"
     id="path2796" /><path
     class="st69"
     d="M1016.76,1186.74v-9.96c0-0.31-0.26-0.56-0.57-0.56s-0.57,0.25-0.57,0.56v9.96c-0.55,0.22-0.95,0.76-0.95,1.4   c0,0.83,0.68,1.51,1.52,1.51c0.83,0,1.51-0.68,1.51-1.51C1017.7,1187.5,1017.31,1186.96,1016.76,1186.74L1016.76,1186.74z"
     id="path2798" /><path
     class="st69"
     d="M1024.89,1177.35h-1.7v-1.7c0-0.31-0.25-0.57-0.57-0.57c-0.31,0-0.57,0.26-0.57,0.57v1.7h-1.7   c-0.31,0-0.57,0.26-0.57,0.57c0,0.31,0.26,0.57,0.57,0.57h1.7v1.7c0,0.31,0.26,0.57,0.57,0.57c0.32,0,0.57-0.26,0.57-0.57v-1.7h1.7   c0.32,0,0.57-0.26,0.57-0.57C1025.46,1177.61,1025.21,1177.35,1024.89,1177.35L1024.89,1177.35z"
     id="path2800" /></a>
	
	<a
   id="a65455"
   xlink:href="/risks"
   target="blank"
   xlink:title="Risks and Humanitarian Situation"
   xlink:show="Risks and Humanitarian Situation"><g
     id="g2818">
		<path
   class="st69"
   d="M1187.37,1233.76v5.98h-1.66v-13h4.48c2.3,0,3.11,1.62,3.11,3.24c0,1.53-0.85,2.7-2.38,2.97v0.04    c1.5,0.23,2.04,0.74,2.12,3.35c0.02,0.56,0.2,2.59,0.45,3.4h-1.73c-0.47-0.9-0.36-2.59-0.5-4.32c-0.13-1.58-1.4-1.66-1.96-1.66    H1187.37z M1187.37,1232.32h2.48c1.19,0,1.76-1.03,1.76-2.16c0-0.94-0.47-1.98-1.75-1.98h-2.5V1232.32z"
   id="path2802" />
		<path
   class="st69"
   d="M1195.47,1226.74h1.66v1.58h-1.66V1226.74z M1197.04,1239.74h-1.48v-9.09h1.48V1239.74z"
   id="path2804" />
		<path
   class="st69"
   d="M1202.28,1239.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1205.45,1239.15,1204.08,1239.92,1202.28,1239.92z"
   id="path2806" />
		<path
   class="st69"
   d="M1209.06,1239.74h-1.48v-13h1.48v7.83h0.04l2.77-3.92h1.8l-3.02,3.91l3.57,5.19h-1.87l-3.24-5.1h-0.04    V1239.74z"
   id="path2808" />
		<path
   class="st69"
   d="M1218.26,1239.92c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1221.43,1239.15,1220.06,1239.92,1218.26,1239.92z"
   id="path2810" />
		<path
   class="st69"
   d="M1232.25,1238.43h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1238.43z M1228.92,1237.04c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1230.81,1235.24,1228.92,1235.12,1228.92,1237.04z"
   id="path2812" />
		<path
   class="st69"
   d="M1241.5,1239.74v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1241.5z"
   id="path2814" />
		<path
   class="st69"
   d="M1250.37,1226.74h1.48v13h-1.48v-1.08h-0.04c-0.5,0.85-1.13,1.26-2.09,1.26c-1.46,0-2.94-0.58-2.94-4.57    c0-2.27,0.07-4.88,3.01-4.88c0.86,0,1.5,0.38,2,1.1h0.05V1226.74z M1248.66,1231.68c-1.58,0-1.8,1.26-1.8,3.69    c0,1.37,0,3.35,1.85,3.35c1.66,0,1.66-2.05,1.66-3.89C1250.37,1233.62,1250.3,1231.68,1248.66,1231.68z"
   id="path2816" />
	</g><g
     id="g2862">
		<path
   class="st69"
   d="M1144.53,1261.34v-6.16c0-1.12-0.36-1.91-1.62-1.91c-1.48,0-1.85,1.19-1.85,2.72v5.35h-1.48v-13h1.48v5.08    h0.07c0.59-1.06,1.28-1.35,2.47-1.35c1.55,0,2.41,0.77,2.41,2.83v6.45H1144.53z"
   id="path2820" />
		<path
   class="st69"
   d="M1153.46,1252.25h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1252.25z"
   id="path2822" />
		<path
   class="st69"
   d="M1162.06,1261.34v-6.3c0-0.92-0.25-1.76-1.44-1.76c-0.45,0-1.06,0.27-1.28,0.61    c-0.27,0.45-0.34,0.99-0.34,1.33v6.12h-1.48v-7.2c0-0.63-0.04-1.26-0.09-1.89h1.57v1.13h0.04c0.43-0.97,1.21-1.31,2.27-1.31    c0.83,0,1.78,0.34,2.12,1.17c0.5-0.97,1.33-1.17,2.16-1.17c0.95,0,2.48,0.22,2.48,2.36v6.91h-1.48v-6.3    c0-0.92-0.25-1.76-1.44-1.76c-0.56,0-0.72,0.02-1.12,0.34c-0.43,0.36-0.5,1.26-0.5,1.6v6.12H1162.06z"
   id="path2824" />
		<path
   class="st69"
   d="M1175.28,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M1171.95,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1173.84,1256.84,1171.95,1256.72,1171.95,1258.64z"
   id="path2826" />
		<path
   class="st69"
   d="M1184.53,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1184.53z"
   id="path2828" />
		<path
   class="st69"
   d="M1188.47,1248.34h1.66v1.58h-1.66V1248.34z M1190.04,1261.34h-1.48v-9.09h1.48V1261.34z"
   id="path2830" />
		<path
   class="st69"
   d="M1192.75,1252.25v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1192.75z"
   id="path2832" />
		<path
   class="st69"
   d="M1202.28,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M1198.94,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1200.83,1256.84,1198.94,1256.72,1198.94,1258.64z"
   id="path2834" />
		<path
   class="st69"
   d="M1208.12,1253.62h0.04c0.61-1.39,1.37-1.55,2.81-1.55v1.53c-0.13-0.02-0.27-0.04-0.4-0.05    c-0.13-0.02-0.25-0.04-0.4-0.04c-1.64,0-2.05,1.24-2.05,2.47v5.37h-1.48v-9.09h1.48V1253.62z"
   id="path2836" />
		<path
   class="st69"
   d="M1212.46,1248.34h1.66v1.58h-1.66V1248.34z M1214.03,1261.34h-1.48v-9.09h1.48V1261.34z"
   id="path2838" />
		<path
   class="st69"
   d="M1221.27,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M1217.93,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1219.83,1256.84,1217.93,1256.72,1217.93,1258.64z"
   id="path2840" />
		<path
   class="st69"
   d="M1230.52,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1230.52z"
   id="path2842" />
		<path
   class="st69"
   d="M1241.26,1261.52c-1.96,0-3.19-0.86-3.13-2.95h1.67c0,0.52,0.02,1.75,1.51,1.75c0.88,0,1.57-0.45,1.57-1.39    c0-1.62-4.54-1.66-4.54-4.38c0-0.95,0.58-2.48,3.13-2.48c1.62,0,3.01,0.77,2.88,2.57h-1.64c0.02-0.95-0.49-1.46-1.42-1.46    c-0.79,0-1.41,0.43-1.41,1.22c0,1.6,4.54,1.57,4.54,4.34C1244.43,1260.75,1243.06,1261.52,1241.26,1261.52z"
   id="path2844" />
		<path
   class="st69"
   d="M1246.45,1248.34h1.66v1.58h-1.66V1248.34z M1248.01,1261.34h-1.48v-9.09h1.48V1261.34z"
   id="path2846" />
		<path
   class="st69"
   d="M1250.73,1252.25v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1250.73z"
   id="path2848" />
		<path
   class="st69"
   d="M1260.43,1252.25h1.48v7.2c0,0.63,0.04,1.26,0.09,1.89h-1.57v-1.1h-0.05c-0.49,0.83-1.35,1.28-2.3,1.28    c-1.58,0-2.45-0.79-2.45-2.34v-6.93h1.48v6.3c0,1.1,0.5,1.84,1.55,1.84c0.79,0,1.78-0.59,1.78-2.11V1252.25z"
   id="path2850" />
		<path
   class="st69"
   d="M1269.25,1260.03h-0.04c-0.45,1.04-1.15,1.49-2.29,1.49c-1.93,0-2.49-1.24-2.49-2.99    c0-2.75,2.7-2.88,4.77-2.83c0.04-1.21,0.05-2.52-1.53-2.52c-0.99,0-1.51,0.67-1.42,1.62h-1.6c0.07-2.03,1.15-2.74,3.08-2.74    c2.34,0,2.95,1.21,2.95,2.74v4.38c0,0.72,0.07,1.46,0.18,2.16h-1.62V1260.03z M1265.92,1258.64c0,0.88,0.43,1.67,1.42,1.67    c0.9,0,2.02-0.56,1.87-3.49C1267.81,1256.84,1265.92,1256.72,1265.92,1258.64z"
   id="path2852" />
		<path
   class="st69"
   d="M1273.73,1252.25v-1.75l1.48-0.67v2.41h1.98v1.12h-1.98v5.56c0,0.58,0,1.31,1.35,1.31    c0.11,0,0.34-0.04,0.67-0.07v1.13c-0.49,0.04-0.97,0.14-1.46,0.14c-1.4,0-2.04-0.58-2.04-1.62v-6.46h-1.49v-1.12H1273.73z"
   id="path2854" />
		<path
   class="st69"
   d="M1278.45,1248.34h1.66v1.58h-1.66V1248.34z M1280.02,1261.34h-1.48v-9.09h1.48V1261.34z"
   id="path2856" />
		<path
   class="st69"
   d="M1282.32,1256.93c0-2.67,0.31-4.86,3.46-4.86c3.15,0,3.46,2.2,3.46,4.86c0,4.01-1.53,4.59-3.46,4.59    C1283.85,1261.52,1282.32,1260.95,1282.32,1256.93z M1287.68,1256.3c0-2.49-0.77-3.03-1.91-3.03c-1.13,0-1.91,0.54-1.91,3.03    c0,2.95,0.38,4.01,1.91,4.01C1287.31,1260.32,1287.68,1259.25,1287.68,1256.3z"
   id="path2858" />
		<path
   class="st69"
   d="M1296.5,1261.34v-6.3c0-0.97-0.34-1.76-1.6-1.76c-1.62,0-1.85,1.44-1.85,2.68v5.38h-1.48v-7.2    c0-0.63-0.04-1.26-0.09-1.89h1.57v1.17h0.07c0.58-1.03,1.26-1.35,2.43-1.35c1.94,0,2.43,1.17,2.43,2.97v6.3H1296.5z"
   id="path2860" />
	</g></a>
	
	
	
	
	<a
   id="a65422"
   xlink:href="/risks"
   target="blank"
   xlink:title="Risks and Humanitarian Situation"
   xlink:show="Risks and Humanitarian Situation"><path
     class="st70"
     d="M1184.8,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C1199.2,1150.96,1184.8,1165.36,1184.8,1183.12L1184.8,1183.12z"
     id="path2864" /><path
     class="st71"
     d="M1184.8,1183.12c0,17.77,14.4,32.17,32.16,32.17c17.77,0,32.17-14.4,32.17-32.17   c0-17.76-14.4-32.16-32.17-32.16C1199.2,1150.96,1184.8,1165.36,1184.8,1183.12L1184.8,1183.12z"
     id="path2866" /><path
     class="st69"
     d="M1222.43,1199.85L1222.43,1199.85v-0.03v-0.3v-7.79c0-0.17,0.07-0.34,0.2-0.46l5.99-5.96   c0.19-0.2,0.44-0.34,0.71-0.4c0.25-0.05,0.5-0.05,0.75,0.02c0.23,0.06,0.44,0.18,0.62,0.34c0.58,0.56,0.59,1.46,0.03,2.03   l-2.64,2.62c-0.1,0.1-0.1,0.27,0.01,0.38c0.1,0.09,0.26,0.09,0.36-0.01l2.65-2.63c0.77-0.77,0.75-2-0.04-2.75   c-0.16-0.16-0.35-0.28-0.56-0.36c-0.24-0.1-0.42-0.33-0.42-0.6v-5.41c0-0.8,0.67-1.45,1.49-1.45c0.83,0,1.49,0.65,1.49,1.45v10.19   c0,0.33-0.13,0.63-0.34,0.88l-5.03,6.46c-0.09,0.11-0.14,0.25-0.14,0.4v3.12l0,0v0.26c0,0.43-0.35,0.77-0.78,0.77h-3.57   C1222.78,1200.62,1222.43,1200.28,1222.43,1199.85L1222.43,1199.85z"
     id="path2868" /><path
     class="st69"
     d="M1211.49,1199.85L1211.49,1199.85v-0.03v-0.3v-7.79c0-0.17-0.07-0.34-0.19-0.46l-6-5.96   c-0.19-0.2-0.44-0.34-0.71-0.4c-0.25-0.05-0.5-0.05-0.75,0.02c-0.23,0.06-0.44,0.18-0.62,0.34c-0.58,0.56-0.59,1.46-0.03,2.03   l2.64,2.62c0.1,0.1,0.1,0.27-0.01,0.38c-0.1,0.09-0.26,0.09-0.36-0.01l-2.65-2.63c-0.77-0.77-0.75-2,0.04-2.75   c0.17-0.16,0.36-0.28,0.56-0.36c0.25-0.1,0.42-0.33,0.42-0.6v-5.41c0-0.8-0.67-1.45-1.49-1.45c-0.82,0-1.49,0.65-1.49,1.45v10.19   c0,0.33,0.13,0.63,0.34,0.88l5.04,6.46c0.09,0.11,0.14,0.25,0.14,0.4v3.12l0,0v0.26c0,0.43,0.34,0.77,0.77,0.77h3.57   C1211.14,1200.62,1211.49,1200.28,1211.49,1199.85L1211.49,1199.85z"
     id="path2870" /><path
     class="st69"
     d="M1226.98,1174.54l0.04-0.03c0.01,0.05,0.02,0.11,0.04,0.17L1226.98,1174.54L1226.98,1174.54z    M1213.76,1171.87l0.1-0.09l0.15,0.09l-0.12,0.11L1213.76,1171.87L1213.76,1171.87z M1214.06,1172.15v0.2h-0.32l-0.09-0.13v-0.19   h0.02L1214.06,1172.15L1214.06,1172.15z M1212.67,1171.81h0.34l-0.44,0.61l-0.18-0.1l0.04-0.25L1212.67,1171.81L1212.67,1171.81z    M1213.48,1172.22v0.2l-0.14,0.15h-0.33l0.05-0.23l0.16-0.01l0.03-0.08L1213.48,1172.22L1213.48,1172.22z M1213.39,1171.73v-0.25   l0.21,0.19L1213.39,1171.73L1213.39,1171.73z M1213.56,1171.81v0.2l-0.15,0.1l-0.2,0.04v-0.34H1213.56L1213.56,1171.81z    M1213.28,1171.51v0.22h-0.62l-0.23-0.07l0.06-0.15l0.29-0.12h0.41v0.12H1213.28L1213.28,1171.51z M1211.84,1170.74l0.27-0.13   l0.25,0.06l-0.09,0.33l-0.26,0.08L1211.84,1170.74L1211.84,1170.74z M1226.82,1174.02h-0.83l-0.5-0.37l-0.53,0.05v0.32h-0.17   l-0.18-0.12l-0.91-0.24v-0.59l-1.16,0.09l-0.36,0.2h-0.46l-0.23-0.03l-0.56,0.31v0.59l-1.14,0.82l0.1,0.35h0.23l-0.06,0.34   l-0.16,0.06l-0.01,0.87l0.98,1.13h0.43l0.03-0.07h0.77l0.22-0.21h0.44l0.24,0.24l0.66,0.07l-0.09,0.87l0.73,1.28l-0.39,0.73   l0.03,0.34l0.3,0.3v0.83l0.39,0.53v0.69h0.35c-1.9,2.32-4.79,3.82-8.02,3.82c-5.7,0-10.33-4.64-10.33-10.34   c0-1.43,0.29-2.8,0.82-4.04v-0.32l0.37-0.45c0.13-0.24,0.27-0.48,0.41-0.71l0.02,0.19l-0.43,0.52c-0.13,0.25-0.26,0.51-0.37,0.77   v0.59l0.43,0.2v0.82l0.41,0.7l0.34,0.06l0.04-0.24l-0.39-0.61l-0.08-0.6h0.23l0.1,0.61l0.57,0.84l-0.15,0.26l0.36,0.56l0.91,0.22   v-0.14l0.36,0.05l-0.04,0.26l0.29,0.05l0.43,0.12l0.62,0.7l0.79,0.06l0.08,0.65l-0.54,0.37l-0.02,0.58l-0.08,0.35l0.78,0.98   l0.06,0.33c0,0,0.28,0.08,0.32,0.08c0.03,0,0.63,0.46,0.63,0.46v1.77l0.22,0.06l-0.15,0.81l0.36,0.48l-0.07,0.81l0.48,0.84   l0.61,0.53l0.62,0.01l0.06-0.19l-0.45-0.38l0.02-0.19l0.08-0.24l0.02-0.23l-0.31-0.01l-0.15-0.19l0.25-0.25l0.04-0.18l-0.29-0.08   l0.02-0.17l0.4-0.07l0.62-0.29l0.21-0.38l0.64-0.82l-0.15-0.65l0.2-0.34l0.59,0.02l0.4-0.32l0.13-1.24l0.44-0.56l0.08-0.36   l-0.4-0.14l-0.27-0.43l-0.91-0.01l-0.72-0.27l-0.03-0.52l-0.25-0.42l-0.65-0.01l-0.38-0.59l-0.33-0.17l-0.02,0.18l-0.61,0.04   l-0.22-0.31l-0.64-0.13l-0.52,0.61l-0.82-0.14l-0.06-0.93l-0.61-0.11l0.25-0.45l-0.07-0.26l-0.79,0.53l-0.5-0.06l-0.18-0.39   l0.11-0.4l0.28-0.51l0.63-0.32h1.22l-0.01,0.37l0.44,0.21l-0.04-0.64l0.32-0.32l0.64-0.42l0.04-0.29l0.64-0.66l0.67-0.37   l-0.06-0.05l0.46-0.43l0.17,0.04l0.07,0.1l0.18-0.2l0.04-0.02l-0.19-0.02l-0.19-0.07v-0.18l0.1-0.09h0.22l0.11,0.05l0.09,0.18   l0.11-0.02v-0.01l0.03,0.01l0.32-0.05l0.04-0.16l0.18,0.05v0.17l-0.16,0.11l0.02,0.19l0.57,0.17v0.01l0.14-0.01v-0.25l-0.45-0.2   l-0.03-0.13l0.38-0.12l0.02-0.37l-0.4-0.24l-0.02-0.6l-0.54,0.26h-0.2l0.05-0.46l-0.74-0.18l-0.3,0.23v0.71l-0.55,0.17l-0.22,0.46   l-0.24,0.04v-0.59l-0.51-0.07l-0.26-0.17l-0.1-0.38l0.92-0.54l0.45-0.14l0.05,0.31l0.25-0.01l0.02-0.16l0.26-0.03v-0.06l-0.11-0.05   l-0.03-0.16l0.33-0.02l0.19-0.21l0.01-0.01h0.01l0.05-0.06l0.68-0.09l0.3,0.26l-0.78,0.42l1,0.23l0.13-0.33h0.43l0.16-0.29   l-0.31-0.08v-0.37l-0.97-0.43l-0.67,0.08l-0.38,0.2l0.03,0.48l-0.4-0.06l-0.06-0.27l0.38-0.34l-0.69-0.04l-0.19,0.06l-0.09,0.23   l0.26,0.05l-0.05,0.25l-0.44,0.03l-0.07,0.17l-0.64,0.02c0,0-0.01-0.36-0.04-0.36c-0.02,0,0.5-0.01,0.5-0.01l0.38-0.37l-0.21-0.1   l-0.27,0.27l-0.46-0.03l-0.27-0.38h-0.59l-0.61,0.46h0.56l0.05,0.16l-0.14,0.13l0.62,0.02l0.09,0.23l-0.7-0.03l-0.03-0.17   l-0.44-0.1l-0.23-0.13l-0.52,0.01c1.71-1.24,3.8-1.98,6.07-1.98c2.61,0,5,0.98,6.82,2.58l-0.12,0.22l-0.48,0.19l-0.2,0.22   l0.05,0.25l0.24,0.04l0.15,0.37l0.43-0.18l0.07,0.5h-0.13l-0.35-0.05l-0.38,0.06l-0.38,0.53l-0.53,0.09l-0.08,0.45l0.23,0.06   l-0.07,0.29l-0.53-0.11l-0.49,0.11l-0.1,0.27l0.08,0.57l0.29,0.13h0.48l0.32-0.03l0.1-0.26l0.51-0.65l0.33,0.07l0.33-0.3l0.06,0.23   l0.81,0.54l-0.1,0.14l-0.37-0.02l0.14,0.19l0.23,0.05l0.26-0.1v-0.32l0.11-0.06l-0.09-0.1l-0.54-0.3l-0.14-0.4h0.44l0.15,0.14   l0.38,0.34l0.02,0.4l0.4,0.42l0.15-0.58l0.27-0.15l0.05,0.48l0.28,0.29l0.53-0.01c0.11,0.27,0.2,0.54,0.28,0.82L1226.82,1174.02   L1226.82,1174.02z M1211.25,1169.55c0,0,0.22-0.03,0.24-0.03s0,0.22,0,0.22l-0.5,0.03l-0.1-0.11L1211.25,1169.55L1211.25,1169.55z    M1210.89,1169.05v-0.02h0.23l0.01-0.07h0.37v0.16l-0.1,0.14h-0.51V1169.05L1210.89,1169.05z M1224.47,1170.3v-0.5   c0.18,0.19,0.35,0.38,0.51,0.58l-0.2,0.3h-0.71l-0.04-0.15L1224.47,1170.3L1224.47,1170.3z M1226.1,1172.27l0.07-0.08   c0.08,0.17,0.16,0.34,0.24,0.51h-0.11l-0.2,0.02V1172.27L1226.1,1172.27z M1228.22,1176.77c0-0.33-0.02-0.66-0.05-0.98   c-0.11-1.07-0.36-2.1-0.75-3.07c-0.03-0.07-0.05-0.14-0.08-0.21c-0.51-1.21-1.24-2.31-2.12-3.27c-0.05-0.06-0.11-0.12-0.17-0.18   c-0.17-0.17-0.34-0.34-0.52-0.5c-2-1.82-4.66-2.94-7.57-2.94c-2.94,0-5.62,1.14-7.62,2.99c-0.47,0.43-0.9,0.9-1.29,1.4   c-1.47,1.9-2.35,4.29-2.35,6.87c0,6.21,5.05,11.26,11.26,11.26c4.37,0,8.16-2.5,10.03-6.14c0.4-0.78,0.71-1.61,0.92-2.48   c0.05-0.22,0.1-0.44,0.14-0.67c0.11-0.64,0.17-1.3,0.17-1.97C1228.22,1176.84,1228.22,1176.81,1228.22,1176.77"
     id="path2872" /></a>
	<g
   id="g2900">
		<path
   class="st69"
   d="M623.62,1112.32c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64    c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1    C623.62,1119.78,623.62,1116.1,623.62,1112.32z"
   id="path2874" />
		<path
   class="st69"
   d="M637.42,1109.44v1.3h0.04c0.52-1.16,1.48-1.5,2.62-1.5v2.52c-2.48-0.16-2.52,1.28-2.52,2.28v5.5h-2.82v-10.1    H637.42z"
   id="path2876" />
		<path
   class="st69"
   d="M641.16,1114.36c0-2.76,0.4-5.12,4.12-5.12s4.12,2.36,4.12,5.12c0,3.16-0.48,5.38-4.12,5.38    C641.64,1119.74,641.16,1117.52,641.16,1114.36z M646.58,1114.2c0-2.1-0.1-3.16-1.3-3.16s-1.3,1.06-1.3,3.16    c0,3.08,0.26,3.74,1.3,3.74C646.32,1117.94,646.58,1117.28,646.58,1114.2z"
   id="path2878" />
		<path
   class="st69"
   d="M653.62,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04    c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3    c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08    c-2.46,0-4.1-0.62-3.94-3.44H653.62z"
   id="path2880" />
		<path
   class="st69"
   d="M662.5,1116.3c-0.02,0.46,0,0.9,0.14,1.22c0.16,0.32,0.46,0.48,1.02,0.48s1.04-0.36,1.04-1.04    c0-2.14-4.96-1.66-4.96-4.88c0-2.18,2.16-2.84,3.98-2.84c1.92,0,3.66,0.92,3.5,3.1h-2.76c0-0.7-0.08-1.12-0.28-1.3    c-0.18-0.18-0.42-0.22-0.72-0.22c-0.62,0-0.96,0.4-0.96,1.08c0,1.6,4.96,1.52,4.96,4.76c0,1.76-1.44,3.08-3.78,3.08    c-2.46,0-4.1-0.62-3.94-3.44H662.5z"
   id="path2882" />
		<path
   class="st69"
   d="M673.82,1113.12v2.04h-4.9v-2.04H673.82z"
   id="path2884" />
		<path
   class="st69"
   d="M675.82,1112.32c0-3.82,0-7.46,4.98-7.46c3.08,0,4.32,1.7,4.2,4.8h-2.96c0-1.92-0.34-2.64-1.24-2.64    c-1.7,0-1.92,1.6-1.92,5.3c0,3.7,0.22,5.3,1.92,5.3c1.4,0,1.34-1.8,1.38-2.94h2.98c0,3.86-1.54,5.1-4.36,5.1    C675.82,1119.78,675.82,1116.1,675.82,1112.32z"
   id="path2886" />
		<path
   class="st69"
   d="M691.88,1118.52h-0.04c-0.28,0.44-0.6,0.76-1,0.94c-0.4,0.2-0.84,0.28-1.38,0.28c-1.34,0-2.52-0.8-2.52-2.2    v-8.1h2.82v7c0,0.9,0.16,1.56,1.06,1.56s1.06-0.66,1.06-1.56v-7h2.82v8.1c0,0.66,0.04,1.34,0.1,2h-2.92V1118.52z"
   id="path2888" />
		<path
   class="st69"
   d="M695.8,1109.44h1.14v-1.6l2.82-1.26v2.86h1.46v1.74h-1.46v5.4c0,0.76-0.02,1.26,0.9,1.26    c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V1109.44z"
   id="path2890" />
		<path
   class="st69"
   d="M701.36,1109.44h1.14v-1.6l2.82-1.26v2.86h1.46v1.74h-1.46v5.4c0,0.76-0.02,1.26,0.9,1.26    c0.18,0,0.36,0,0.5-0.04v1.74c-0.38,0.04-0.78,0.1-1.46,0.1c-2.44,0-2.76-1.62-2.76-2.24v-6.22h-1.14V1109.44z"
   id="path2892" />
		<path
   class="st69"
   d="M711.12,1105.1v2.22h-2.82v-2.22H711.12z M711.12,1119.54h-2.82v-10.1h2.82V1119.54z"
   id="path2894" />
		<path
   class="st69"
   d="M716.44,1110.46h0.04c0.28-0.46,0.62-0.76,1-0.94c0.4-0.2,0.86-0.28,1.38-0.28c1.34,0,2.52,0.8,2.52,2.2v8.1    h-2.82v-6.96c0-0.9-0.16-1.6-1.06-1.6s-1.06,0.7-1.06,1.6v6.96h-2.82v-10.1h2.82V1110.46z"
   id="path2896" />
		<path
   class="st69"
   d="M731.34,1109.44v10.52c0,0.7,0.04,3.46-3.84,3.46c-2.1,0-3.9-0.54-3.96-3h2.76c0,0.42,0.06,0.78,0.24,1.02    c0.18,0.26,0.5,0.4,0.94,0.4c0.7,0,1.04-0.66,1.04-1.68v-1.94h-0.04c-0.42,0.78-1.22,1.18-2.14,1.18c-3.1,0-2.96-2.84-2.96-5.12    c0-2.22,0.04-5.04,2.98-5.04c1,0,1.86,0.44,2.26,1.38h0.04v-1.18H731.34z M727.36,1117.66c1.02,0,1.16-1.06,1.16-3.2    c0-2.22-0.1-3.48-1.14-3.48c-1.06,0-1.24,0.74-1.24,3.82C726.14,1115.74,726,1117.66,727.36,1117.66z"
   id="path2898" />
	</g>
	<path
   class="st72"
   d="M20,0C8.95,0,0,8.95,0,20v1270.5c0,11.05,8.95,20,20,20h1315c11.05,0,20-8.95,20-20V20c0-11.05-8.95-20-20-20   H20L20,0z"
   id="path2902" />
	<g
   id="g2974">
		<path
   class="st3"
   d="M140.59,58.84V33.57h13.79v3.89h-8.51v6.23h7.84v3.89h-7.84v7.39h8.79v3.89H140.59z"
   id="path2904" />
		<path
   class="st3"
   d="M166.49,57.06h-0.07c-0.49,0.77-1.05,1.33-1.75,1.65c-0.7,0.35-1.47,0.49-2.42,0.49    c-2.35,0-4.41-1.4-4.41-3.85V41.17h4.94v12.25c0,1.58,0.28,2.73,1.86,2.73s1.85-1.16,1.85-2.73V41.17h4.94v14.18    c0,1.16,0.07,2.35,0.18,3.5h-5.11V57.06z"
   id="path2906" />
		<path
   class="st3"
   d="M180.03,41.17v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94    V41.17H180.03z"
   id="path2908" />
		<path
   class="st3"
   d="M186.58,49.78c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42    S186.58,55.31,186.58,49.78z M196.06,49.5c0-3.68-0.18-5.53-2.28-5.53s-2.28,1.85-2.28,5.53c0,5.39,0.46,6.55,2.28,6.55    S196.06,54.89,196.06,49.5z"
   id="path2910" />
		<path
   class="st3"
   d="M209.19,41.17v1.96h0.07c0.91-1.71,2.28-2.31,4.17-2.31c5.11,0,4.94,5.67,4.94,9.31    c0,3.57,0.14,9.07-4.83,9.07c-1.79,0-3.01-0.52-4.03-2.03h-0.07v9.28h-4.94V41.17H209.19z M213.53,49.85    c0-3.54,0.04-5.99-2.1-5.99c-2.03,0-2,2.45-2,5.99c0,4.45,0.32,6.3,2,6.3C213.21,56.15,213.53,54.29,213.53,49.85z"
   id="path2912" />
		<path
   class="st3"
   d="M226.55,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5.01c-0.07,1.93-0.7,3.5-1.89,4.59    c-1.15,1.08-2.91,1.72-5.22,1.72c-6.37,0-7.21-3.89-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H226.55z     M231.06,48.03c0-1.72,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H231.06z"
   id="path2914" />
		<path
   class="st3"
   d="M260.67,55.55c0,1.09,0.14,2.21,0.25,3.29h-4.59l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7    c-3.43,0-4.69-2.56-4.69-5.64c0-5.85,4.52-6.09,9.1-6.02v-1.37c0-1.5-0.21-2.59-2-2.59c-1.72,0-1.86,1.3-1.86,2.7h-4.83    c0-2.14,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M251.57,53.35    c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C253.39,50.41,251.57,50.2,251.57,53.35z"
   id="path2916" />
		<path
   class="st3"
   d="M269.7,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path2918" />
		<path
   class="st3"
   d="M291.09,58.84v-1.96h-0.07c-0.91,1.71-2.27,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31    c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.52,4.03,2.03h0.07v-9.28h4.94v25.27H291.09z M290.84,49.85c0-3.54,0.04-5.99-2-5.99    c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.31,6.3,2.1,6.3C290.53,56.15,290.84,54.29,290.84,49.85z"
   id="path2920" />
		<path
   class="st3"
   d="M307.54,46.21c0-6.69,0-13.06,8.72-13.06c5.39,0,7.56,2.98,7.35,8.4h-5.18c0-3.36-0.59-4.62-2.17-4.62    c-2.98,0-3.36,2.8-3.36,9.28s0.38,9.28,3.36,9.28c2.45,0,2.35-3.15,2.42-5.15h5.22c0,6.76-2.7,8.93-7.63,8.93    C307.54,59.26,307.54,52.82,307.54,46.21z"
   id="path2922" />
		<path
   class="st3"
   d="M331.55,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5.01c-0.07,1.93-0.7,3.5-1.89,4.59    c-1.15,1.08-2.91,1.72-5.22,1.72c-6.37,0-7.21-3.89-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H331.55z     M336.06,48.03c0-1.72,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H336.06z"
   id="path2924" />
		<path
   class="st3"
   d="M349.43,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path2926" />
		<path
   class="st3"
   d="M360,41.17h2v-2.8l4.94-2.21v5.01h2.56v3.05h-2.56v9.45c0,1.33-0.03,2.21,1.58,2.21c0.32,0,0.63,0,0.88-0.07    v3.05c-0.67,0.07-1.37,0.17-2.56,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.21h-2V41.17z"
   id="path2928" />
		<path
   class="st3"
   d="M376.42,41.17v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94    V41.17H376.42z"
   id="path2930" />
		<path
   class="st3"
   d="M396.79,55.55c0,1.09,0.14,2.21,0.25,3.29h-4.59l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7    c-3.43,0-4.69-2.56-4.69-5.64c0-5.85,4.52-6.09,9.1-6.02v-1.37c0-1.5-0.21-2.59-2-2.59c-1.72,0-1.86,1.3-1.86,2.7h-4.83    c0-2.14,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M387.69,53.35    c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C389.51,50.41,387.69,50.2,387.69,53.35z"
   id="path2932" />
		<path
   class="st3"
   d="M406.24,33.57v25.27h-4.94V33.57H406.24z"
   id="path2934" />
		<path
   class="st3"
   d="M416.7,58.84l7-25.27h6.97l6.86,25.27h-5.57l-1.4-5.6h-7.21l-1.44,5.6H416.7z M426.89,38.44h-0.07    l-2.42,10.92h5.04L426.89,38.44z"
   id="path2936" />
		<path
   class="st3"
   d="M443.65,53.17c-0.04,0.8,0,1.58,0.25,2.14c0.28,0.56,0.8,0.84,1.79,0.84c0.98,0,1.82-0.63,1.82-1.82    c0-3.75-8.68-2.91-8.68-8.54c0-3.82,3.78-4.97,6.97-4.97c3.36,0,6.41,1.61,6.13,5.43h-4.83c0-1.23-0.14-1.96-0.49-2.27    c-0.32-0.31-0.74-0.39-1.26-0.39c-1.08,0-1.68,0.7-1.68,1.89c0,2.8,8.68,2.66,8.68,8.33c0,3.08-2.52,5.39-6.62,5.39    c-4.31,0-7.18-1.08-6.9-6.02H443.65z"
   id="path2938" />
		<path
   class="st3"
   d="M460.66,33.57v3.89h-4.94v-3.89H460.66z M460.66,58.84h-4.94V41.17h4.94V58.84z"
   id="path2940" />
		<path
   class="st3"
   d="M478.44,55.55c0,1.09,0.14,2.21,0.25,3.29h-4.59l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7    c-3.43,0-4.69-2.56-4.69-5.64c0-5.85,4.52-6.09,9.1-6.02v-1.37c0-1.5-0.21-2.59-2-2.59c-1.72,0-1.86,1.3-1.86,2.7h-4.83    c0-2.14,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M469.34,53.35    c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C471.16,50.41,469.34,50.2,469.34,53.35z"
   id="path2942" />
		<path
   class="st3"
   d="M490.3,46.21c0-6.69,0-13.06,8.72-13.06c5.39,0,7.56,2.98,7.35,8.4h-5.18c0-3.36-0.59-4.62-2.17-4.62    c-2.98,0-3.36,2.8-3.36,9.28s0.38,9.28,3.36,9.28c2.45,0,2.35-3.15,2.42-5.15h5.22c0,6.76-2.7,8.93-7.63,8.93    C490.3,59.26,490.3,52.82,490.3,46.21z"
   id="path2944" />
		<path
   class="st3"
   d="M518.41,58.84V46.66c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V33.57h4.94v9.38h0.07    c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85v14.18H518.41z"
   id="path2946" />
		<path
   class="st3"
   d="M532.62,33.57v3.89h-4.94v-3.89H532.62z M532.62,58.84h-4.94V41.17h4.94V58.84z"
   id="path2948" />
		<path
   class="st3"
   d="M542.35,33.57v25.27h-4.94V33.57H542.35z"
   id="path2950" />
		<path
   class="st3"
   d="M555.54,58.84v-1.96h-0.07c-0.91,1.71-2.27,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31    c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.52,4.03,2.03h0.07v-9.28h4.94v25.27H555.54z M555.3,49.85c0-3.54,0.04-5.99-2-5.99    c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.31,6.3,2.1,6.3C554.98,56.15,555.3,54.29,555.3,49.85z"
   id="path2952" />
		<path
   class="st3"
   d="M577.42,58.84h-5.29V33.57h9.77c3.61,0,5.92,2.31,5.92,6.62c0,3.22-1.26,5.64-4.69,6.2v0.07    c1.16,0.14,4.59,0.42,4.59,4.97c0,1.61,0.1,6.37,0.6,7.42h-5.18c-0.7-1.54-0.56-3.26-0.56-4.9c0-3.01,0.28-5.57-3.78-5.57h-1.37    V58.84z M577.42,44.49h2.35c2.1,0,2.7-2.1,2.7-3.71c0-2.42-1.02-3.33-2.7-3.33h-2.35V44.49z"
   id="path2954" />
		<path
   class="st3"
   d="M596.81,33.57v3.89h-4.94v-3.89H596.81z M596.81,58.84h-4.94V41.17h4.94V58.84z"
   id="path2956" />
		<path
   class="st3"
   d="M614.69,41.17v18.41c0,1.23,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.94-6.93-5.25h4.83c0,0.74,0.1,1.37,0.42,1.79    c0.31,0.46,0.88,0.7,1.65,0.7c1.23,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.74,1.36-2.14,2.06-3.75,2.06c-5.43,0-5.18-4.97-5.18-8.96    c0-3.89,0.07-8.82,5.22-8.82c1.75,0,3.26,0.77,3.96,2.42H610v-2.06H614.69z M607.73,55.55c1.79,0,2.03-1.85,2.03-5.6    c0-3.89-0.17-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C605.59,52.19,605.35,55.55,607.73,55.55z"
   id="path2958" />
		<path
   class="st3"
   d="M627.33,58.84V46.66c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V33.57h4.94v9.38h0.07    c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.51-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85v14.18H627.33z"
   id="path2960" />
		<path
   class="st3"
   d="M634.19,41.17h2v-2.8l4.94-2.21v5.01h2.56v3.05h-2.56v9.45c0,1.33-0.03,2.21,1.58,2.21    c0.32,0,0.63,0,0.88-0.07v3.05c-0.67,0.07-1.37,0.17-2.56,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.21h-2V41.17z"
   id="path2962" />
		<path
   class="st3"
   d="M649.8,53.17c-0.04,0.8,0,1.58,0.25,2.14c0.28,0.56,0.8,0.84,1.79,0.84c0.98,0,1.82-0.63,1.82-1.82    c0-3.75-8.68-2.91-8.68-8.54c0-3.82,3.78-4.97,6.97-4.97c3.36,0,6.41,1.61,6.13,5.43h-4.83c0-1.23-0.14-1.96-0.49-2.27    c-0.32-0.31-0.74-0.39-1.26-0.39c-1.08,0-1.68,0.7-1.68,1.89c0,2.8,8.68,2.66,8.68,8.33c0,3.08-2.52,5.39-6.62,5.39    c-4.31,0-7.18-1.08-6.9-6.02H649.8z"
   id="path2964" />
		<path
   class="st3"
   d="M682.63,55.55c0,1.09,0.14,2.21,0.25,3.29h-4.58l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7    c-3.43,0-4.69-2.56-4.69-5.64c0-5.85,4.52-6.09,9.1-6.02v-1.37c0-1.5-0.21-2.59-2-2.59c-1.72,0-1.86,1.3-1.86,2.7h-4.83    c0-2.14,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M673.53,53.35    c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C675.35,50.41,673.53,50.2,673.53,53.35z"
   id="path2966" />
		<path
   class="st3"
   d="M691.66,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path2968" />
		<path
   class="st3"
   d="M713.04,58.84v-1.96h-0.07c-0.91,1.71-2.28,2.31-4.17,2.31c-5.11,0-4.94-5.67-4.94-9.31    c0-3.57-0.14-9.07,4.83-9.07c1.79,0,3.01,0.52,4.03,2.03h0.07v-9.28h4.94v25.27H713.04z M712.8,49.85c0-3.54,0.04-5.99-2-5.99    c-2.14,0-2.1,2.45-2.1,5.99c0,4.45,0.32,6.3,2.1,6.3C712.48,56.15,712.8,54.29,712.8,49.85z"
   id="path2970" />
		<path
   class="st3"
   d="M727.5,33.57h5.43l3.29,17.75h0.07l3.99-17.75h6.23l3.78,17.75h0.07l3.15-17.75h5.18l-5.6,25.27h-5.85    l-3.96-18.48h-0.07l-4.38,18.48h-5.74L727.5,33.57z"
   id="path2972" />
	</g>
	<g
   id="g3030">
		<path
   class="st3"
   d="M764.28,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5c-0.07,1.93-0.7,3.5-1.89,4.59    c-1.16,1.08-2.91,1.72-5.22,1.72c-6.37,0-7.21-3.89-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H764.28z     M768.8,48.03c0-1.72,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H768.8z"
   id="path2976" />
		<path
   class="st3"
   d="M782.59,33.57v25.27h-4.94V33.57H782.59z"
   id="path2978" />
		<path
   class="st3"
   d="M792.32,33.57v25.27h-4.94V33.57H792.32z"
   id="path2980" />
		<path
   class="st3"
   d="M796.69,33.57h4.94v9.28h0.07c1.01-1.51,2.24-2.03,4.03-2.03c4.97,0,4.83,5.5,4.83,9.07    c0,3.64,0.18,9.31-4.94,9.31c-1.89,0-3.25-0.6-4.17-2.31h-0.07v1.96h-4.69V33.57z M805.72,49.85c0-3.54,0.04-5.99-2.1-5.99    c-2.03,0-2,2.45-2,5.99c0,4.45,0.32,6.3,2,6.3C805.41,56.15,805.72,54.29,805.72,49.85z"
   id="path2982" />
		<path
   class="st3"
   d="M818.74,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5c-0.07,1.93-0.7,3.5-1.89,4.59    c-1.16,1.08-2.91,1.72-5.22,1.72c-6.37,0-7.21-3.89-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H818.74z     M823.26,48.03c0-1.72,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H823.26z"
   id="path2984" />
		<path
   class="st3"
   d="M837.05,33.57v3.89h-4.94v-3.89H837.05z M837.05,58.84h-4.94V41.17h4.94V58.84z"
   id="path2986" />
		<path
   class="st3"
   d="M846.36,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path2988" />
		<path
   class="st3"
   d="M872.43,41.17v18.41c0,1.23,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.94-6.93-5.25h4.83    c0,0.74,0.11,1.37,0.42,1.79c0.32,0.46,0.88,0.7,1.65,0.7c1.23,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.73,1.36-2.13,2.06-3.75,2.06    c-5.43,0-5.18-4.97-5.18-8.96c0-3.89,0.07-8.82,5.22-8.82c1.75,0,3.25,0.77,3.96,2.42h0.07v-2.06H872.43z M865.47,55.55    c1.79,0,2.03-1.85,2.03-5.6c0-3.89-0.17-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C863.33,52.19,863.09,55.55,865.47,55.55z"
   id="path2990" />
		<path
   class="st3"
   d="M884.33,58.84V33.57h8.51l3.96,17.19h0.07l4.2-17.19h8.23v25.27h-5.15v-19.5h-0.07l-4.87,19.5h-5.04    l-4.62-19.5h-0.07v19.5H884.33z"
   id="path2992" />
		<path
   class="st3"
   d="M912.93,49.78c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42    S912.93,55.31,912.93,49.78z M922.41,49.5c0-3.68-0.17-5.53-2.28-5.53s-2.28,1.85-2.28,5.53c0,5.39,0.46,6.55,2.28,6.55    S922.41,54.89,922.41,49.5z"
   id="path2994" />
		<path
   class="st3"
   d="M935.78,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path2996" />
		<path
   class="st3"
   d="M953.7,33.57v3.89h-4.94v-3.89H953.7z M953.7,58.84h-4.94V41.17h4.94V58.84z"
   id="path2998" />
		<path
   class="st3"
   d="M956.08,41.17h2v-2.8l4.94-2.21v5.01h2.56v3.05h-2.56v9.45c0,1.33-0.04,2.21,1.58,2.21    c0.32,0,0.63,0,0.88-0.07v3.05c-0.67,0.07-1.37,0.17-2.55,0.17c-4.27,0-4.83-2.83-4.83-3.92V44.21h-2V41.17z"
   id="path3000" />
		<path
   class="st3"
   d="M967.39,49.78c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42    C968.23,59.19,967.39,55.31,967.39,49.78z M976.87,49.5c0-3.68-0.17-5.53-2.28-5.53s-2.28,1.85-2.28,5.53    c0,5.39,0.46,6.55,2.28,6.55S976.87,54.89,976.87,49.5z"
   id="path3002" />
		<path
   class="st3"
   d="M990,41.17v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94V41.17    H990z"
   id="path3004" />
		<path
   class="st3"
   d="M1002.32,33.57v3.89h-4.94v-3.89H1002.32z M1002.32,58.84h-4.94V41.17h4.94V58.84z"
   id="path3006" />
		<path
   class="st3"
   d="M1011.63,42.95h0.07c0.49-0.81,1.08-1.33,1.75-1.65c0.7-0.35,1.5-0.49,2.42-0.49c2.35,0,4.41,1.4,4.41,3.85    v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.86-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path3008" />
		<path
   class="st3"
   d="M1037.7,41.17v18.41c0,1.23,0.07,6.06-6.72,6.06c-3.68,0-6.83-0.94-6.93-5.25h4.83    c0,0.74,0.11,1.37,0.42,1.79c0.32,0.46,0.88,0.7,1.65,0.7c1.23,0,1.82-1.16,1.82-2.94v-3.4h-0.07c-0.73,1.36-2.13,2.06-3.75,2.06    c-5.43,0-5.18-4.97-5.18-8.96c0-3.89,0.07-8.82,5.22-8.82c1.75,0,3.25,0.77,3.96,2.42h0.07v-2.06H1037.7z M1030.74,55.55    c1.79,0,2.03-1.85,2.03-5.6c0-3.89-0.17-6.09-2-6.09c-1.86,0-2.17,1.29-2.17,6.69C1028.6,52.19,1028.36,55.55,1030.74,55.55z"
   id="path3010" />
		<path
   class="st3"
   d="M1057.37,58.84V33.57h13.13v3.89h-7.84v6.48h7.49v3.89h-7.49v11.03H1057.37z"
   id="path3012" />
		<path
   class="st3"
   d="M1077.46,41.17v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94    V41.17H1077.46z"
   id="path3014" />
		<path
   class="st3"
   d="M1097.83,55.55c0,1.09,0.14,2.21,0.25,3.29h-4.58l-0.21-2.35h-0.07c-1.05,1.82-2.49,2.7-4.62,2.7    c-3.43,0-4.69-2.56-4.69-5.64c0-5.85,4.51-6.09,9.1-6.02v-1.37c0-1.5-0.21-2.59-2-2.59c-1.71,0-1.86,1.3-1.86,2.7h-4.83    c0-2.14,0.67-3.5,1.82-4.31c1.12-0.84,2.73-1.16,4.62-1.16c6.27,0,7.07,2.7,7.07,5.92V55.55z M1088.73,53.35    c0,1.26,0.21,2.8,1.82,2.8c2.91,0,2.45-3.92,2.45-5.85C1090.55,50.41,1088.73,50.2,1088.73,53.35z"
   id="path3016" />
		<path
   class="st3"
   d="M1106.47,42.95h0.07c0.98-1.58,2.31-2.14,4.17-2.14c1.75,0,3.15,0.84,3.96,2.24    c1.16-1.54,2.56-2.24,4.59-2.24c2.34,0,4.41,1.4,4.41,3.85v14.18h-4.94V46.66c0-1.58-0.28-2.8-1.85-2.8    c-1.58,0-1.86,1.23-1.86,2.8v12.18h-4.83V46.66c0-1.58-0.28-2.8-1.85-2.8s-1.86,1.23-1.86,2.8v12.18h-4.94V41.17h4.94V42.95z"
   id="path3018" />
		<path
   class="st3"
   d="M1131.74,50.79c0,2.1,0.07,5.25,2.24,5.25c1.75,0,2.1-1.68,2.1-3.15h5c-0.07,1.93-0.7,3.5-1.89,4.59    c-1.16,1.08-2.91,1.72-5.22,1.72c-6.37,0-7.21-3.89-7.21-9.42c0-4.83,0.7-8.96,7.21-8.96c6.65,0,7.39,4.31,7.21,9.98H1131.74z     M1136.26,48.03c0-1.72,0.07-4.17-2.28-4.17c-2.28,0-2.24,2.66-2.24,4.17H1136.26z"
   id="path3020" />
		<path
   class="st3"
   d="M1143.12,41.17h4.9l2.42,13.3h0.07l3.4-13.3h5.11l3.12,13.3h0.07l2.66-13.3h4.73l-4.79,17.68h-5.18    l-3.19-12.08h-0.07l-3.57,12.08h-5.25L1143.12,41.17z"
   id="path3022" />
		<path
   class="st3"
   d="M1171.5,49.78c0-4.83,0.7-8.96,7.21-8.96s7.21,4.13,7.21,8.96c0,5.53-0.84,9.42-7.21,9.42    C1172.34,59.19,1171.5,55.31,1171.5,49.78z M1180.99,49.5c0-3.68-0.17-5.53-2.28-5.53s-2.28,1.85-2.28,5.53    c0,5.39,0.46,6.55,2.28,6.55S1180.99,54.89,1180.99,49.5z"
   id="path3024" />
		<path
   class="st3"
   d="M1194.11,41.17v2.28h0.07c0.91-2.03,2.59-2.63,4.59-2.63v4.41c-4.34-0.28-4.41,2.24-4.41,3.99v9.63h-4.94    V41.17H1194.11z"
   id="path3026" />
		<path
   class="st3"
   d="M1200.97,58.84V33.57h4.94v15.05h0.07l4.45-7.46h5.15l-5.01,7.88l5.57,9.8h-5.57l-4.59-9.63h-0.07v9.63    H1200.97z"
   id="path3028" />
	</g>
	
	
	
	<a
   id="a11138"
   xlink:href="/child-rights#spending"
   target="blank"
   xlink:title="Public spending on children"
   xlink:show="Public spending on children"><path
     class="st56"
     d="M753.7,234.48c4.8-0.38,14.48-0.37,21.61,0.01c6.31,0.34,11.84-4.17,12.75-10.42l6.55-44.96   c0.9-7.21-4.1-13.45-11.15-13.94c-8.1-0.87-24.95-0.89-37.64-0.03c-7.05,0.48-12.19,6.9-11.2,13.9l6.37,44.87   C741.68,230.08,747.37,234.81,753.7,234.48L753.7,234.48z"
     id="path2254" /><path
     class="st55"
     d="M766.05,209.34c0.06-0.06,0.19-0.03,0.3-0.05c0.77-0.11,1.53-0.06,2.3-0.01c1.6,0.12,3.22,0.1,4.82,0.29   c0.39,0.05,0.79,0.13,1.18,0.04c0.96-0.23,1.38-0.96,1.68-1.8c0.13-0.35,0.07-0.68-0.11-1.01c-0.35-0.62-0.91-0.95-1.56-1.16   c-1.65-0.52-3.35-0.8-5.08-0.9c-1.4-0.08-2.73-0.3-3.98-1.02c-1.13-0.65-2.37-1.08-3.67-1.3c-3.04-0.52-5.98,0.05-8.89,0.88   c-0.36,0.1-0.53,0.36-0.53,0.73c0,0.44,0,0.89,0,1.33c0,1.84,0,3.68,0,5.53c0,0.53,0.26,0.88,0.72,0.91   c1.14,0.06,2.17,0.45,3.19,0.93c2.51,1.17,4.97,2.43,7.51,3.53c1,0.43,2,0.85,3.12,0.71c0.67-0.08,1.34-0.14,2.01-0.24   c1.75-0.26,3.49-0.56,5.25-0.8c1.05-0.14,2.07-0.29,2.97-0.91c1.06-0.74,2.14-1.44,3.21-2.17c0.48-0.33,0.93-0.7,1.35-1.1   c0.33-0.31,0.55-0.69,0.61-1.15c0.03-0.25-0.01-0.5-0.27-0.58c-0.37-0.11-0.29-0.23-0.08-0.45c0.58-0.63,0.45-1.34-0.31-1.74   c-0.39-0.21-0.81-0.29-1.25-0.25c-1.17,0.09-2.13,0.64-2.96,1.42c-0.75,0.7-1.61,1.13-2.6,1.35c-0.78,0.17-1.57,0.22-2.35,0.32   C770.28,210.98,768.08,210.52,766.05,209.34"
     id="path3032" /><path
     class="st55"
     d="M751.5,207.54L751.5,207.54c0-1.69,0-3.38,0-5.07c0-0.61-0.26-0.86-0.87-0.86c-0.77,0-1.54,0-2.31,0   c-0.55,0-0.83,0.27-0.83,0.81c0,3.4,0,6.81,0,10.21c0,0.56,0.25,0.82,0.8,0.82c0.78,0.01,1.56,0,2.34,0c0.63,0,0.86-0.24,0.86-0.87   C751.5,210.9,751.5,209.22,751.5,207.54"
     id="path3034" /><path
     class="st55"
     d="M781.89,189.96c-1.94-5.59-7.37-8.79-13.19-7.76c-5.55,0.98-9.69,6.1-9.49,11.74   c0.1,2.77,1.04,5.21,2.83,7.32c0.14,0.17,0.3,0.27,0.52,0.31c1.17,0.23,2.29,0.62,3.33,1.21c1.18,0.67,2.45,0.92,3.78,1   c1.65,0.09,3.27,0.35,4.85,0.79c0.15,0.04,0.27,0.02,0.4-0.03C780.73,202.45,783.91,195.79,781.89,189.96L781.89,189.96z    M770.85,202.84c-5.26,0-9.54-4.28-9.54-9.54s4.28-9.54,9.54-9.54s9.54,4.28,9.54,9.54S776.11,202.84,770.85,202.84L770.85,202.84z   "
     id="path3036" /><path
     class="st55"
     d="M770.85,184.51c-4.85,0-8.79,3.94-8.79,8.79c0,4.85,3.94,8.79,8.79,8.79c4.84,0,8.79-3.94,8.79-8.79   C779.64,188.46,775.69,184.51,770.85,184.51L770.85,184.51z M775.62,195.32h-9.54c-0.38,0-0.69-0.31-0.69-0.69   c0-0.38,0.31-0.69,0.69-0.69h9.54c0.38,0,0.69,0.31,0.69,0.69C776.31,195.02,776,195.32,775.62,195.32L775.62,195.32z    M775.62,192.65h-9.54c-0.38,0-0.69-0.31-0.69-0.69c0-0.38,0.31-0.69,0.69-0.69h9.54c0.38,0,0.69,0.31,0.69,0.69   C776.31,192.34,776,192.65,775.62,192.65L775.62,192.65z"
     id="path3038" /></a>
	<line
   class="st73"
   x1="977.95"
   y1="616.5"
   x2="1013.09"
   y2="616.5"
   id="line3040" />
	<line
   class="st74"
   x1="1014.62"
   y1="619.47"
   x2="1014.62"
   y2="644.75"
   id="line3042" />
	<line
   class="st75"
   x1="1017.6"
   y1="646.24"
   x2="1322.52"
   y2="646.24"
   id="line3044" />
	<path
   class="st29"
   d="M974.9,616.5L974.9,616.5 M1014.62,616.5L1014.62,616.5 M1014.62,646.24L1014.62,646.24 M1324,646.24   L1324,646.24"
   id="path3046" />
	<path
   class="st3"
   d="M974.9,619.28c1.53,0,2.77-1.24,2.77-2.78s-1.24-2.78-2.77-2.78c-1.53,0-2.78,1.24-2.78,2.78   S973.36,619.28,974.9,619.28L974.9,619.28z"
   id="path3048" />
</g>
</svg>


                    """,
                style={"height": "80rem", "display": "flex"},
            )
        ]
    )

    # return html.Div([
    # html.Iframe(srcDoc=f"""{encoded_image}""", style={"height": "80rem", "display": "flex"},)])
    # return html.Img(src="data:image/svg+xml;base64,{}".format(encoded_image))
    # return html.Img(src="assets/socr_diagram.svg")
