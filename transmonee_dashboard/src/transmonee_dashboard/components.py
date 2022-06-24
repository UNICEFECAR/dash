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
    <!-- Generator: Adobe Illustrator 26.0.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->

    <svg
       version="1.1"
       id="Layer_1"
       x="0px"
       y="0px"
       viewBox="0 0 1353.81 1308.66"
       style="enable-background:new 0 0 1353.81 1308.66;"
       xml:space="preserve"
       sodipodi:docname="SOCR_Diagram_[UPDATED v2].svg"
       inkscape:version="1.2 (dc2aedaf03, 2022-05-15)"
       xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
       xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
       xmlns:xlink="http://www.w3.org/1999/xlink"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:svg="http://www.w3.org/2000/svg"><defs
       id="defs6226" /><sodipodi:namedview
       id="namedview6224"
       pagecolor="#ffffff"
       bordercolor="#000000"
       borderopacity="0.25"
       inkscape:showpageshadow="2"
       inkscape:pageopacity="0.0"
       inkscape:pagecheckerboard="0"
       inkscape:deskcolor="#d1d1d1"
       showgrid="false"
       inkscape:zoom="4.9760823"
       inkscape:cx="501.80039"
       inkscape:cy="807.36205"
       inkscape:window-width="1920"
       inkscape:window-height="1001"
       inkscape:window-x="-9"
       inkscape:window-y="-9"
       inkscape:window-maximized="1"
       inkscape:current-layer="g6221" />
    <style
       type="text/css"
       id="style3115">
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
    <g
       id="g6221"
       inkscape:transform-center-x="14.469214"
       inkscape:transform-center-y="-16.076904">
    	<a
       id="a12727"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#nutrition"
       xlink:title="Nutrition"
       target="blank"><path
         class="st0"
         d="m 633.88,480.31 c 7.66,-1.51 15.46,-2.62 23.38,-3.33 6.89,-0.61 12.13,-6.46 12.13,-13.38 v -49.51 c 0,-7.72 -6.54,-13.88 -14.25,-13.32 -13.85,1.02 -27.44,2.98 -40.71,5.81 -7.56,1.61 -12.1,9.37 -9.93,16.79 L 618.48,471 c 1.96,6.61 8.63,10.64 15.4,9.31 z"
         id="path3117" /></a>
    	<path
       class="st0"
       d="m 573.57,501.52 c 6.97,-3.65 14.16,-6.94 21.54,-9.85 6.39,-2.52 9.74,-9.56 7.81,-16.15 l -13.98,-47.6 c -2.18,-7.42 -10.2,-11.48 -17.43,-8.76 -12.92,4.86 -25.41,10.59 -37.41,17.11 -6.78,3.68 -8.95,12.4 -4.78,18.9 l 26.84,41.76 c 3.74,5.81 11.29,7.79 17.41,4.59 z"
       id="path3119" />
    	<a
       id="a17457"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:show=""
       xlink:title="Violence"><path
         class="st1"
         d="m 458.88,648.9 c 1.83,-7.73 4.05,-15.3 6.65,-22.69 2.29,-6.52 -0.74,-13.7 -7.02,-16.57 L 413.32,589 c -7.02,-3.21 -15.35,0.18 -18.03,7.43 -4.72,12.78 -8.6,25.96 -11.57,39.48 -1.66,7.54 3.51,14.9 11.15,16 l 49.09,7.06 c 6.82,0.98 13.34,-3.36 14.92,-10.07 z"
         id="path3121" /></a>
    	<a
       id="a15876"
       xlink:actuate="https://tm-dash.azurewebsites.net/child-health#hs"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#hs"
       target="blank"
       xlink:title="Health System"><path
         class="st0"
         d="m 420.09,574.26 45.16,20.63 c 6.24,2.85 13.67,0.54 17.07,-5.42 3.93,-6.88 8.21,-13.53 12.82,-19.93 4.04,-5.61 3.15,-13.36 -2.07,-17.88 l -37.52,-32.51 c -5.83,-5.06 -14.77,-4.15 -19.39,2.04 -8.17,10.97 -15.62,22.52 -22.26,34.57 -3.73,6.77 -0.85,15.29 6.19,18.5 z"
         id="path3123" /></a>
    	<path
       class="st0"
       d="m 697.74,476.98 c 7.92,0.71 15.72,1.82 23.38,3.33 6.77,1.33 13.44,-2.69 15.39,-9.32 l 13.98,-47.63 c 2.18,-7.41 -2.37,-15.18 -9.93,-16.79 -13.27,-2.83 -26.86,-4.79 -40.71,-5.81 -7.7,-0.57 -14.25,5.59 -14.25,13.32 v 49.51 c 0.01,6.93 5.25,12.78 12.14,13.39 z"
       id="path3125" />
    	<a
       id="a35285"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#hivaids"
       target="blank"
       xlink:title="HIV/AIDS"><path
         class="st0"
         d="m 766.06,427.91 -13.98,47.6 c -1.93,6.59 1.42,13.63 7.81,16.15 7.38,2.91 14.57,6.2 21.54,9.85 6.12,3.2 13.67,1.23 17.41,-4.59 l 26.84,-41.76 c 4.17,-6.49 2.01,-15.21 -4.78,-18.9 -12,-6.52 -24.49,-12.25 -37.41,-17.11 -7.23,-2.72 -15.26,1.35 -17.43,8.76 z"
         id="path3127" /></a>
    	<path
       class="st1"
       d="m 452.88,700.68 c 0,-3.98 0.1,-7.93 0.31,-11.85 0.36,-6.85 -4.64,-12.82 -11.43,-13.8 l -49.15,-7.07 c -7.65,-1.1 -14.68,4.51 -15.21,12.22 -0.46,6.79 -0.69,13.64 -0.69,20.55 0,6.91 0.23,13.76 0.69,20.55 0.52,7.71 7.55,13.32 15.21,12.22 l 49.16,-7.07 c 6.79,-0.98 11.79,-6.95 11.43,-13.8 -0.21,-3.95 -0.32,-7.94 -0.32,-11.95 z"
       id="path3129" />
    	<a
       id="a38497"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#justice"
       target="blank"
       xlink:title="Justice for Children"><path
         class="st1"
         d="m 465.56,775.24 c -2.6,-7.39 -4.83,-14.96 -6.66,-22.68 -1.59,-6.7 -8.1,-11.04 -14.92,-10.06 l -49.11,7.06 c -7.65,1.1 -12.81,8.45 -11.15,16 2.97,13.52 6.85,26.71 11.57,39.48 2.68,7.24 11,10.63 18.03,7.43 l 45.22,-20.65 c 6.29,-2.87 9.32,-10.06 7.02,-16.58 z"
         id="path3131" /></a>
    	<a
       id="a23929"
       xlink:href="https://tm-dash.azurewebsites.net/child-participation#registration"
       target="blank"
       xlink:title="Birth Registration"><path
         class="st2"
         d="m 902.11,700.68 c 0,4.01 -0.11,7.99 -0.32,11.95 -0.36,6.85 4.64,12.82 11.43,13.8 l 49.16,7.07 c 7.65,1.1 14.68,-4.51 15.2,-12.22 0.46,-6.79 0.69,-13.64 0.69,-20.55 0,-6.91 -0.23,-13.76 -0.69,-20.55 -0.52,-7.71 -7.55,-13.32 -15.2,-12.22 l -49.16,7.07 c -6.79,0.98 -11.79,6.95 -11.43,13.8 0.22,3.93 0.32,7.88 0.32,11.85 z"
         id="path3133" /></a>
    	<a
       id="a32057"
       xlink:href="https://tm-dash.azurewebsites.net/child-poverty#povertydeprivation"
       target="blank"
       xlink:title="Child Poverty"><path
         class="st3"
         d="m 941.68,589 -45.19,20.64 c -6.28,2.87 -9.32,10.05 -7.03,16.57 2.6,7.39 4.83,14.96 6.65,22.69 1.58,6.71 8.1,11.04 14.92,10.06 l 49.1,-7.06 c 7.64,-1.1 12.81,-8.45 11.15,-16 -2.97,-13.53 -6.85,-26.71 -11.57,-39.48 -2.68,-7.24 -11.01,-10.63 -18.03,-7.42 z"
         id="path3135" /></a>
    	<path
       class="st3"
       d="m 859.86,569.54 c 4.61,6.4 8.89,13.05 12.82,19.93 3.4,5.95 10.83,8.26 17.07,5.42 l 45.17,-20.63 c 7.03,-3.21 9.92,-11.74 6.18,-18.51 -6.64,-12.05 -14.09,-23.6 -22.26,-34.57 -4.61,-6.19 -13.55,-7.1 -19.39,-2.04 l -37.52,32.51 c -5.23,4.53 -6.11,12.28 -2.07,17.89 z"
       id="path3137" />
    	<path
       class="st4"
       d="m 657.26,924.38 c -7.91,-0.7 -15.7,-1.82 -23.36,-3.32 -6.77,-1.33 -13.44,2.69 -15.39,9.32 L 604.5,978.1 c -2.18,7.42 2.37,15.18 9.93,16.79 13.27,2.83 26.86,4.79 40.71,5.81 7.7,0.56 14.25,-5.59 14.25,-13.32 v -49.62 c 0,-6.92 -5.24,-12.76 -12.13,-13.38 z"
       id="path3139" />
    	<path
       class="st0"
       d="m 521.69,538.91 c 5.66,-5.45 11.61,-10.61 17.82,-15.45 5.44,-4.24 6.77,-11.92 3.03,-17.73 L 515.7,463.97 c -4.18,-6.5 -13.02,-8.15 -19.2,-3.49 -10.96,8.27 -21.33,17.27 -31.05,26.93 -5.48,5.45 -5.11,14.43 0.73,19.49 l 37.51,32.5 c 5.23,4.53 13.03,4.3 18,-0.49 z"
       id="path3141" />
    	<path
       class="st2"
       d="m 896.09,752.56 c -1.83,7.72 -4.05,15.29 -6.66,22.68 -2.29,6.52 0.74,13.71 7.02,16.58 l 45.22,20.65 c 7.03,3.21 15.35,-0.18 18.03,-7.43 4.72,-12.77 8.6,-25.96 11.57,-39.48 1.66,-7.54 -3.51,-14.9 -11.15,-16 L 911,742.5 c -6.81,-0.98 -13.33,3.35 -14.91,10.06 z"
       id="path3143" />
    	<path
       class="st0"
       d="m 815.49,523.46 c 6.21,4.84 12.15,10 17.81,15.45 4.97,4.79 12.77,5.01 17.99,0.49 l 37.52,-32.51 c 5.84,-5.06 6.21,-14.04 0.73,-19.49 -9.72,-9.66 -20.09,-18.66 -31.05,-26.93 -6.17,-4.66 -15.02,-3.02 -19.2,3.49 l -26.84,41.76 c -3.72,5.82 -2.4,13.5 3.04,17.74 z"
       id="path3145" />
    	<path
       class="st1"
       d="m 539.55,877.94 c -6.2,-4.84 -12.15,-9.99 -17.8,-15.43 -4.98,-4.79 -12.77,-5.01 -17.99,-0.49 l -37.57,32.55 c -5.84,5.06 -6.21,14.04 -0.73,19.49 9.72,9.66 20.09,18.66 31.05,26.93 6.17,4.66 15.02,3.02 19.2,-3.49 l 26.88,-41.83 c 3.73,-5.81 2.4,-13.49 -3.04,-17.73 z"
       id="path3147" />
    	<path
       class="st1"
       d="m 495.18,831.89 c -4.61,-6.4 -8.89,-13.04 -12.82,-19.92 -3.4,-5.95 -10.83,-8.26 -17.06,-5.41 l -45.21,20.65 c -7.03,3.21 -9.92,11.73 -6.18,18.51 6.64,12.05 14.09,23.6 22.26,34.57 4.61,6.19 13.55,7.1 19.39,2.04 l 37.57,-32.55 c 5.21,-4.53 6.09,-12.29 2.05,-17.89 z"
       id="path3149" />
    	<path
       class="st2"
       d="m 833.26,862.5 c -5.66,5.45 -11.6,10.6 -17.8,15.43 -5.44,4.24 -6.77,11.92 -3.04,17.73 l 26.88,41.83 c 4.18,6.5 13.02,8.14 19.2,3.49 10.96,-8.27 21.33,-17.27 31.05,-26.93 5.48,-5.45 5.11,-14.43 -0.73,-19.49 L 851.25,862 c -5.23,-4.51 -13.02,-4.29 -17.99,0.5 z"
       id="path3151" />
    	<a
       id="a22266"
       xlink:href="https://tm-dash.azurewebsites.net/child-education#system"
       target="blank"
       xlink:title="Education System"><path
         class="st4"
         d="m 588.94,973.55 14.01,-47.7 c 1.93,-6.59 -1.42,-13.63 -7.8,-16.14 -7.37,-2.91 -14.56,-6.2 -21.52,-9.84 -6.12,-3.2 -13.67,-1.22 -17.41,4.59 l -26.89,41.84 c -4.17,6.49 -2.01,15.21 4.78,18.9 12,6.52 24.49,12.25 37.41,17.11 7.22,2.72 15.25,-1.34 17.42,-8.76 z"
         id="path3153" /></a>
    	<path
       class="st4"
       d="m 721.09,921.06 c -7.65,1.5 -15.45,2.62 -23.35,3.32 -6.89,0.61 -12.13,6.46 -12.13,13.38 v 49.62 c 0,7.73 6.54,13.88 14.25,13.32 13.85,-1.02 27.44,-2.98 40.71,-5.81 7.56,-1.61 12.1,-9.37 9.93,-16.79 l -14.01,-47.72 c -1.96,-6.62 -8.63,-10.65 -15.4,-9.32 z"
       id="path3155" />
    	<path
       class="st2"
       d="M 934.91,827.2 889.7,806.55 c -6.23,-2.85 -13.66,-0.54 -17.06,5.41 -3.93,6.88 -8.21,13.52 -12.82,19.92 -4.04,5.61 -3.16,13.36 2.07,17.89 l 37.57,32.55 c 5.84,5.06 14.77,4.15 19.39,-2.04 8.17,-10.97 15.62,-22.52 22.26,-34.57 3.72,-6.77 0.84,-15.29 -6.2,-18.51 z"
       id="path3157" />
    	<path
       class="st4"
       d="m 781.38,899.87 c -6.97,3.64 -14.15,6.93 -21.52,9.84 -6.39,2.52 -9.74,9.56 -7.8,16.14 l 14.01,47.7 c 2.18,7.42 10.2,11.48 17.43,8.76 12.92,-4.86 25.41,-10.59 37.41,-17.11 6.78,-3.69 8.95,-12.4 4.78,-18.9 L 798.8,904.46 c -3.75,-5.81 -11.3,-7.79 -17.42,-4.59 z"
       id="path3159" />
    	<g
       class="st5"
       id="g3253">
    		<path
       class="st0"
       d="m 949.98,360.73 h 2.11 l 4.23,13 h -1.86 l -0.94,-3.1 h -5.02 l -0.97,3.1 h -1.67 z m 1.01,1.53 h -0.04 l -2.03,6.93 h 4.16 z"
       id="path3161" />
    		<path
       class="st0"
       d="m 962.69,360.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3163" />
    		<path
       class="st0"
       d="m 966.63,369.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path3165" />
    		<path
       class="st0"
       d="m 977.32,373.73 h -1.48 v -13 h 1.48 z"
       id="path3167" />
    		<path
       class="st0"
       d="m 981.32,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3169" />
    		<path
       class="st0"
       d="m 991.56,373.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path3171" />
    		<path
       class="st0"
       d="m 1001.62,367.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3173" />
    		<path
       class="st0"
       d="m 1007.31,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3175" />
    		<path
       class="st0"
       d="m 1019.8,373.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3177" />
    		<path
       class="st0"
       d="m 1024.03,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3179" />
    		<path
       class="st0"
       d="m 1034.47,365.71 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.5,-0.38 -2,-1.1 h -0.05 v 4.36 H 1033 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path3181" />
    		<path
       class="st0"
       d="m 1046.8,373.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3183" />
    		<path
       class="st0"
       d="m 1053.6,372.03 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3185" />
    		<path
       class="st0"
       d="m 1061.54,373.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 H 1063 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 -0.01,2 -1.38,2.78 -3.18,2.78 z"
       id="path3187" />
    		<path
       class="st0"
       d="m 1066.72,360.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3189" />
    		<path
       class="st0"
       d="m 1075.6,367.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3191" />
    		<path
       class="st0"
       d="m 1084.53,372.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3193" />
    		<path
       class="st0"
       d="m 1090.29,373.73 h -1.48 v -13 h 1.48 z"
       id="path3195" />
    		<path
       class="st0"
       d="m 1093.09,371.85 h 1.85 l -1.64,4.16 h -1.15 z"
       id="path3197" />
    		<path
       class="st0"
       d="m 1105.3,373.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3199" />
    		<path
       class="st0"
       d="m 1115.27,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3201" />
    		<path
       class="st0"
       d="m 1127.76,373.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3203" />
    		<path
       class="st0"
       d="m 1131.99,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3205" />
    		<path
       class="st0"
       d="m 1141.51,372.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3207" />
    		<path
       class="st0"
       d="m 1147.27,373.73 h -1.48 v -13 h 1.48 z"
       id="path3209" />
    		<path
       class="st0"
       d="m 1158.51,372.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.39,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3211" />
    		<path
       class="st0"
       d="m 1167.76,373.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3213" />
    		<path
       class="st0"
       d="m 1176.63,360.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3215" />
    		<path
       class="st0"
       d="m 1186.35,366 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 366 Z"
       id="path3217" />
    		<path
       class="st0"
       d="m 1192.25,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3219" />
    		<path
       class="st0"
       d="m 1201.42,365.71 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path3221" />
    		<path
       class="st0"
       d="m 1210.35,366 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 366 Z"
       id="path3223" />
    		<path
       class="st0"
       d="m 1214.56,369.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path3225" />
    		<path
       class="st0"
       d="m 1228.62,360.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.94,-0.58 -2.94,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.5,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.08,-3.15 -1.71,-3.15 z"
       id="path3227" />
    		<path
       class="st0"
       d="m 1237.67,364.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path3229" />
    		<path
       class="st0"
       d="m 1246.56,367.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3231" />
    		<path
       class="st0"
       d="m 1250.97,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3233" />
    		<path
       class="st0"
       d="m 1255.69,360.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3235" />
    		<path
       class="st0"
       d="m 1258.76,364.63 h 1.66 l 2.04,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path3237" />
    		<path
       class="st0"
       d="m 1269.24,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3239" />
    		<path
       class="st0"
       d="m 1285.73,373.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3241" />
    		<path
       class="st0"
       d="m 1291.24,369.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3243" />
    		<path
       class="st0"
       d="m 1303.48,372.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3245" />
    		<path
       class="st0"
       d="m 1309.24,373.73 h -1.48 v -13 h 1.48 z"
       id="path3247" />
    		<path
       class="st0"
       d="m 1311.95,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3249" />
    		<path
       class="st0"
       d="m 1321.73,373.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3251" />
    	</g>
    	<a
       id="a12721"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#nutrition"
       target="blank"
       xlink:title="Nutrition"><g
         class="st5"
         id="g3273">
    		<path
       class="st0"
       d="m 40.96,360.73 v 13 h -2.27 l -5.13,-11.27 h -0.04 v 11.27 h -1.48 v -13 h 2.34 l 5.06,11.13 h 0.04 v -11.13 z"
       id="path3255" />
    		<path
       class="st0"
       d="m 48.66,364.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path3257" />
    		<path
       class="st0"
       d="m 52.96,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3259" />
    		<path
       class="st0"
       d="m 59.34,366 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 366 Z"
       id="path3261" />
    		<path
       class="st0"
       d="m 63.67,360.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3263" />
    		<path
       class="st0"
       d="m 67.96,364.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3265" />
    		<path
       class="st0"
       d="m 72.67,360.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3267" />
    		<path
       class="st0"
       d="m 76.54,369.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path3269" />
    		<path
       class="st0"
       d="m 90.73,373.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 H 85.8 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3271" />
    	</g></a>
    	<a
       id="a35299"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#hivaids"
       target="blank"
       xlink:title="HIV/AIDS"><g
         class="st5"
         id="g3291">
    		<path
       class="st0"
       d="m 1258.04,440.73 v -13 h 1.66 v 5.62 h 4.56 v -5.62 h 1.66 v 13 h -1.66 v -5.94 h -4.56 v 5.94 z"
       id="path3275" />
    		<path
       class="st0"
       d="m 1270.81,440.73 h -1.66 v -13 h 1.66 z"
       id="path3277" />
    		<path
       class="st0"
       d="m 1278.46,440.73 h -1.98 l -3.76,-13 h 1.8 l 2.97,11.43 h 0.04 l 3.04,-11.43 h 1.69 z"
       id="path3279" />
    		<path
       class="st0"
       d="m 1283.26,442.46 h -1.21 l 4.23,-14.73 h 1.21 z"
       id="path3281" />
    		<path
       class="st0"
       d="m 1291.88,427.73 h 2.11 l 4.23,13 h -1.85 l -0.94,-3.1 h -5.02 l -0.97,3.1 h -1.67 z m 1.01,1.53 h -0.04 l -2.03,6.93 h 4.16 z"
       id="path3283" />
    		<path
       class="st0"
       d="m 1301.82,440.73 h -1.66 v -13 h 1.66 z"
       id="path3285" />
    		<path
       class="st0"
       d="m 1304.99,427.73 h 4 c 1.66,0 2.84,0.59 3.49,1.98 0.52,1.1 0.58,3.69 0.58,4.11 0,2.77 -0.25,4.38 -0.79,5.24 -0.7,1.12 -2.02,1.67 -4.29,1.67 h -2.99 z m 1.65,11.56 h 1.57 c 2.3,0 3.15,-0.86 3.15,-3.89 v -2.63 c 0,-2.63 -0.81,-3.6 -2.54,-3.6 h -2.18 z"
       id="path3287" />
    		<path
       class="st0"
       d="m 1317.23,436.86 v 0.38 c 0,1.76 1.12,2.32 2.18,2.32 1.31,0 2.32,-0.56 2.32,-2.11 0,-2.88 -5.83,-2.56 -5.83,-6.46 0,-2.3 1.64,-3.53 3.82,-3.53 2.38,0 3.71,1.15 3.6,3.8 h -1.73 c 0.02,-1.42 -0.43,-2.36 -2,-2.36 -0.99,0 -2,0.5 -2,1.91 0,2.86 5.83,2.45 5.83,6.57 0,2.74 -1.89,3.62 -4.03,3.62 -3.83,0.04 -3.83,-2.9 -3.8,-4.14 h 1.64 z"
       id="path3289" />
    	</g></a>
    	<g
       class="st5"
       id="g3317">
    		<path
       class="st0"
       d="m 33.83,440.73 h -1.66 v -13 h 1.66 z"
       id="path3293" />
    		<path
       class="st0"
       d="m 41.27,440.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 H 45.8 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3295" />
    		<path
       class="st0"
       d="m 54.26,440.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 H 58.8 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.48 z"
       id="path3297" />
    		<path
       class="st0"
       d="m 67.65,431.64 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 H 67.6 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path3299" />
    		<path
       class="st0"
       d="m 76.73,440.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 H 71.8 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3301" />
    		<path
       class="st0"
       d="m 80.67,427.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3303" />
    		<path
       class="st0"
       d="m 89.74,432.99 -4.02,6.54 h 4.14 v 1.21 h -5.74 v -1.39 l 3.96,-6.46 v -0.04 h -3.76 v -1.21 h 5.42 z"
       id="path3305" />
    		<path
       class="st0"
       d="m 96.47,439.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3307" />
    		<path
       class="st0"
       d="m 100.95,431.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3309" />
    		<path
       class="st0"
       d="m 105.67,427.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3311" />
    		<path
       class="st0"
       d="m 109.54,436.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3313" />
    		<path
       class="st0"
       d="m 123.72,440.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3315" />
    	</g>
    	<g
       class="st5"
       id="g3321">
    		<path
       class="st0"
       d="m 1110.44,494.73 h 1.77 l 2.45,11.27 h 0.04 l 2.61,-11.27 h 2.14 l 2.36,11.27 h 0.04 l 2.65,-11.27 h 1.73 l -3.44,13 h -2.02 l -2.47,-11.27 h -0.04 l -2.63,11.27 h -2.02 z"
       id="path3319" />
    	</g>
    	<g
       class="st5"
       id="g3331">
    		<path
       class="st0"
       d="m 1131.77,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3323" />
    		<path
       class="st0"
       d="m 1136.26,498.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3325" />
    		<path
       class="st0"
       d="m 1142.54,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3327" />
    		<path
       class="st0"
       d="m 1151.63,500.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3329" />
    	</g>
    	<g
       class="st5"
       id="g3375">
    		<path
       class="st0"
       d="m 1155.09,505.86 h 1.85 l -1.64,4.16 h -1.15 z"
       id="path3333" />
    		<path
       class="st0"
       d="m 1165.51,507.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3335" />
    		<path
       class="st0"
       d="m 1175.5,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3337" />
    		<path
       class="st0"
       d="m 1184.75,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path3339" />
    		<path
       class="st0"
       d="m 1188.69,494.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3341" />
    		<path
       class="st0"
       d="m 1192.98,498.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3343" />
    		<path
       class="st0"
       d="m 1202.5,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3345" />
    		<path
       class="st0"
       d="m 1206.98,498.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3347" />
    		<path
       class="st0"
       d="m 1211.7,494.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3349" />
    		<path
       class="st0"
       d="m 1215.57,503.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3351" />
    		<path
       class="st0"
       d="m 1229.75,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3353" />
    		<path
       class="st0"
       d="m 1242.5,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3355" />
    		<path
       class="st0"
       d="m 1251.75,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3357" />
    		<path
       class="st0"
       d="m 1260.62,494.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3359" />
    		<path
       class="st0"
       d="m 1273.74,507.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.86,1.19 -1.86,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.47 z"
       id="path3361" />
    		<path
       class="st0"
       d="m 1280.55,506.04 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3363" />
    		<path
       class="st0"
       d="m 1290.61,498.64 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.84,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.68,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.09,-3.45 -1.76,-3.45 z"
       id="path3365" />
    		<path
       class="st0"
       d="m 1294.68,494.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3367" />
    		<path
       class="st0"
       d="m 1300.24,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3369" />
    		<path
       class="st0"
       d="m 1312.73,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3371" />
    		<path
       class="st0"
       d="m 1318.24,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3373" />
    	</g>
    	<g
       class="st5"
       id="g3437">
    		<path
       class="st0"
       d="m 33.52,507.73 h -1.55 v -13 h 2.68 l 3.28,10.91 h 0.04 l 3.31,-10.91 h 2.74 v 13 h -1.66 v -11.56 h -0.04 l -3.64,11.56 h -1.57 l -3.56,-11.56 h -0.04 v 11.56 z"
       id="path3377" />
    		<path
       class="st0"
       d="m 51.47,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3379" />
    		<path
       class="st0"
       d="m 55.95,498.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3381" />
    		<path
       class="st0"
       d="m 62.23,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3383" />
    		<path
       class="st0"
       d="m 71.32,500.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path3385" />
    		<path
       class="st0"
       d="m 80.72,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3387" />
    		<path
       class="st0"
       d="m 89.47,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3389" />
    		<path
       class="st0"
       d="m 95.23,507.73 h -1.48 v -13 h 1.48 z"
       id="path3391" />
    		<path
       class="st0"
       d="m 98.04,505.86 h 1.85 l -1.64,4.16 H 97.1 Z"
       id="path3393" />
    		<path
       class="st0"
       d="m 110.71,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3395" />
    		<path
       class="st0"
       d="m 116.22,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3397" />
    		<path
       class="st0"
       d="m 122.64,498.64 h 1.64 l 1.64,7.83 h 0.04 l 2.02,-7.83 h 2.09 l 1.85,7.83 h 0.04 l 1.8,-7.83 h 1.57 l -2.43,9.09 h -1.98 l -1.94,-7.74 h -0.04 l -2.03,7.74 h -1.98 z"
       id="path3399" />
    		<path
       class="st0"
       d="m 138.37,507.73 h -1.48 v -13 h 1.48 v 4.83 h 0.05 c 0.5,-0.72 1.13,-1.1 2,-1.1 2.93,0 3.01,2.61 3.01,4.88 0,4 -1.48,4.57 -2.94,4.57 -0.95,0 -1.58,-0.41 -2.09,-1.26 h -0.04 v 1.08 z m 1.66,-1.02 c 1.85,0 1.85,-1.98 1.85,-3.35 0,-2.43 -0.22,-3.69 -1.8,-3.69 -1.64,0 -1.71,1.94 -1.71,3.15 0,1.39 -0.16,3.89 1.66,3.89 z"
       id="path3401" />
    		<path
       class="st0"
       d="m 145.52,503.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3403" />
    		<path
       class="st0"
       d="m 156.3,500.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3405" />
    		<path
       class="st0"
       d="m 165.7,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3407" />
    		<path
       class="st0"
       d="m 178.44,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3409" />
    		<path
       class="st0"
       d="m 187.69,507.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3411" />
    		<path
       class="st0"
       d="m 196.57,494.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3413" />
    		<path
       class="st0"
       d="m 209.51,501.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3415" />
    		<path
       class="st0"
       d="m 218.69,507.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3417" />
    		<path
       class="st0"
       d="m 222.63,494.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3419" />
    		<path
       class="st0"
       d="m 228.19,507.73 h -1.48 v -13 h 1.48 z"
       id="path3421" />
    		<path
       class="st0"
       d="m 235.56,494.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.72,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0.01,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3423" />
    		<path
       class="st0"
       d="m 248.68,507.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3425" />
    		<path
       class="st0"
       d="m 254.18,503.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3427" />
    		<path
       class="st0"
       d="m 266.42,506.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3429" />
    		<path
       class="st0"
       d="m 272.18,507.73 h -1.48 v -13 h 1.48 z"
       id="path3431" />
    		<path
       class="st0"
       d="m 274.9,498.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3433" />
    		<path
       class="st0"
       d="m 284.68,507.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.86,1.19 -1.86,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.47 z"
       id="path3435" />
    	</g>
    	<g
       class="st5"
       id="g3483">
    		<path
       class="st3"
       d="m 1149.28,570.86 v 0.38 c 0,1.76 1.12,2.32 2.18,2.32 1.31,0 2.32,-0.56 2.32,-2.11 0,-2.88 -5.83,-2.56 -5.83,-6.46 0,-2.3 1.64,-3.53 3.82,-3.53 2.38,0 3.71,1.15 3.6,3.8 h -1.73 c 0.02,-1.42 -0.43,-2.36 -2,-2.36 -0.99,0 -2,0.5 -2,1.91 0,2.86 5.83,2.45 5.83,6.57 0,2.74 -1.89,3.62 -4.03,3.62 -3.83,0.04 -3.83,-2.9 -3.8,-4.14 z"
       id="path3439" />
    		<path
       class="st3"
       d="m 1157.59,570.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3441" />
    		<path
       class="st3"
       d="m 1171.6,568.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3443" />
    		<path
       class="st3"
       d="m 1175.72,561.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3445" />
    		<path
       class="st3"
       d="m 1184.52,573.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3447" />
    		<path
       class="st3"
       d="m 1190.28,574.73 h -1.48 v -13 h 1.48 z"
       id="path3449" />
    		<path
       class="st3"
       d="m 1198.43,566.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.87,0 -1.5,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.8,-1.24 1.8,-3.67 z"
       id="path3451" />
    		<path
       class="st3"
       d="m 1207.36,567.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3453" />
    		<path
       class="st3"
       d="m 1211.57,570.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3455" />
    		<path
       class="st3"
       d="m 1220.99,565.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3457" />
    		<path
       class="st3"
       d="m 1227.27,570.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3459" />
    		<path
       class="st3"
       d="m 1239.58,568.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3461" />
    		<path
       class="st3"
       d="m 1243.99,565.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3463" />
    		<path
       class="st3"
       d="m 1248.71,561.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3465" />
    		<path
       class="st3"
       d="m 1252.58,570.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3467" />
    		<path
       class="st3"
       d="m 1266.76,574.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3469" />
    		<path
       class="st3"
       d="m 1277.51,574.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3471" />
    		<path
       class="st3"
       d="m 1285.55,573.04 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3473" />
    		<path
       class="st3"
       d="m 1293.49,574.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3475" />
    		<path
       class="st3"
       d="m 1298.96,565.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3477" />
    		<path
       class="st3"
       d="m 1305.24,570.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3479" />
    		<path
       class="st3"
       d="m 1317.27,574.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3481" />
    	</g>
    	<g
       class="st5"
       id="g3509">
    		<path
       class="st0"
       d="m 32.07,574.73 v -13 h 1.66 v 5.62 h 4.56 v -5.62 h 1.66 v 13 h -1.66 v -5.94 h -4.56 v 5.94 z"
       id="path3485" />
    		<path
       class="st0"
       d="m 44.23,570.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3487" />
    		<path
       class="st0"
       d="m 56.48,573.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3489" />
    		<path
       class="st0"
       d="m 62.23,574.73 h -1.48 v -13 h 1.48 z"
       id="path3491" />
    		<path
       class="st0"
       d="m 64.95,565.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3493" />
    		<path
       class="st0"
       d="m 74.73,574.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3495" />
    		<path
       class="st0"
       d="m 85.47,574.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3497" />
    		<path
       class="st0"
       d="m 93.52,573.04 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3499" />
    		<path
       class="st0"
       d="m 101.46,574.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 H 100 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 -0.01,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3501" />
    		<path
       class="st0"
       d="m 106.93,565.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3503" />
    		<path
       class="st0"
       d="m 113.21,570.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3505" />
    		<path
       class="st0"
       d="m 125.23,574.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3507" />
    	</g>
    	<a
       id="a32054"
       xlink:href="https://tm-dash.azurewebsites.net/child-poverty#povertydeprivation"
       target="blank"
       xlink:title="Child Poverty"><g
         class="st5"
         id="g3579">
    		<path
       class="st3"
       d="m 1058.75,632.32 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.11,-0.11 -4.11,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.7 z"
       id="path3511" />
    		<path
       class="st3"
       d="m 1067.81,641.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3513" />
    		<path
       class="st3"
       d="m 1071.75,628.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3515" />
    		<path
       class="st3"
       d="m 1077.31,641.73 h -1.48 v -13 h 1.48 z"
       id="path3517" />
    		<path
       class="st3"
       d="m 1084.67,628.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.08,-3.15 -1.72,-3.15 z"
       id="path3519" />
    		<path
       class="st3"
       d="m 1094.46,633.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.87,0 -1.5,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.52,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path3521" />
    		<path
       class="st3"
       d="m 1101.61,637.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3523" />
    		<path
       class="st3"
       d="m 1109.82,632.64 h 1.66 l 2.03,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path3525" />
    		<path
       class="st3"
       d="m 1120.29,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3527" />
    		<path
       class="st3"
       d="m 1129.38,634.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.12,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3529" />
    		<path
       class="st3"
       d="m 1134.01,632.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3531" />
    		<path
       class="st3"
       d="m 1141.59,640.04 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3533" />
    		<path
       class="st3"
       d="m 1155.52,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3535" />
    		<path
       class="st3"
       d="m 1164.77,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3537" />
    		<path
       class="st3"
       d="m 1173.65,628.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.09,-3.15 -1.72,-3.15 z"
       id="path3539" />
    		<path
       class="st3"
       d="m 1186.3,641.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3541" />
    		<path
       class="st3"
       d="m 1199.51,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3543" />
    		<path
       class="st3"
       d="m 1203.99,632.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3545" />
    		<path
       class="st3"
       d="m 1210.28,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3547" />
    		<path
       class="st3"
       d="m 1219.37,634.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3549" />
    		<path
       class="st3"
       d="m 1223.7,628.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3551" />
    		<path
       class="st3"
       d="m 1232.5,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3553" />
    		<path
       class="st3"
       d="m 1238.26,641.73 h -1.48 v -13 h 1.48 z"
       id="path3555" />
    		<path
       class="st3"
       d="m 1249.62,628.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.08,-3.15 -1.72,-3.15 z"
       id="path3557" />
    		<path
       class="st3"
       d="m 1255.26,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3559" />
    		<path
       class="st3"
       d="m 1264.42,633.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path3561" />
    		<path
       class="st3"
       d="m 1273.35,634.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3563" />
    		<path
       class="st3"
       d="m 1277.68,628.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3565" />
    		<path
       class="st3"
       d="m 1280.76,632.64 h 1.66 l 2.03,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path3567" />
    		<path
       class="st3"
       d="m 1294.48,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3569" />
    		<path
       class="st3"
       d="m 1298.96,632.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3571" />
    		<path
       class="st3"
       d="m 1303.67,628.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3573" />
    		<path
       class="st3"
       d="m 1307.54,637.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.92,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3575" />
    		<path
       class="st3"
       d="m 1321.73,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3577" />
    	</g></a>
    	<a
       id="a19095"
       xlink:title="Violence"
       target="blank"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"><g
         class="st5"
         id="g3643">
    		<path
       class="st1"
       d="M 36.48,641.73 H 34.5 l -3.76,-13 h 1.8 l 2.97,11.43 h 0.04 l 3.04,-11.43 h 1.69 z"
       id="path3581" />
    		<path
       class="st1"
       d="m 41.68,628.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3583" />
    		<path
       class="st1"
       d="m 45.55,637.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3585" />
    		<path
       class="st1"
       d="m 56.24,641.73 h -1.48 v -13 h 1.48 z"
       id="path3587" />
    		<path
       class="st1"
       d="m 60.24,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3589" />
    		<path
       class="st1"
       d="m 72.73,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 H 67.8 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3591" />
    		<path
       class="st1"
       d="m 81.55,635.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3593" />
    		<path
       class="st1"
       d="m 87.24,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3595" />
    		<path
       class="st1"
       d="m 103.47,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3597" />
    		<path
       class="st1"
       d="m 112.6,632.64 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.1,-3.45 -1.76,-3.45 z"
       id="path3599" />
    		<path
       class="st1"
       d="m 121.47,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3601" />
    		<path
       class="st1"
       d="m 125.67,628.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3603" />
    		<path
       class="st1"
       d="m 134.72,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3605" />
    		<path
       class="st1"
       d="m 141.47,641.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3607" />
    		<path
       class="st1"
       d="m 146.94,632.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3609" />
    		<path
       class="st1"
       d="m 160.53,635.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3611" />
    		<path
       class="st1"
       d="m 169.71,641.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3613" />
    		<path
       class="st1"
       d="m 173.65,628.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3615" />
    		<path
       class="st1"
       d="m 179.21,641.73 h -1.48 v -13 h 1.48 z"
       id="path3617" />
    		<path
       class="st1"
       d="m 186.58,628.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3619" />
    		<path
       class="st1"
       d="m 192.3,634.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3621" />
    		<path
       class="st1"
       d="m 198.2,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3623" />
    		<path
       class="st1"
       d="m 210.7,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3625" />
    		<path
       class="st1"
       d="m 223.44,640.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3627" />
    		<path
       class="st1"
       d="m 232.69,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3629" />
    		<path
       class="st1"
       d="m 241.57,628.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3631" />
    		<path
       class="st1"
       d="m 248.62,632.64 h 1.64 l 1.64,7.83 h 0.04 l 2.02,-7.83 h 2.09 l 1.85,7.83 h 0.04 l 1.8,-7.83 h 1.57 l -2.43,9.09 h -1.98 l -1.94,-7.74 h -0.04 l -2.03,7.74 h -1.98 z"
       id="path3633" />
    		<path
       class="st1"
       d="m 262.5,637.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3635" />
    		<path
       class="st1"
       d="m 276.22,641.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3637" />
    		<path
       class="st1"
       d="m 286.19,637.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3639" />
    		<path
       class="st1"
       d="m 298.68,641.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3641" />
    	</g></a>
    	<a
       id="a23926"
       xlink:href="https://tm-dash.azurewebsites.net/child-participation#registration"
       target="blank"
       xlink:title="Birth Registration"><g
         class="st5"
         id="g3701">
    		<path
       class="st2"
       d="m 1116.17,708.73 v -13 h 4.23 c 1.8,0 2.41,0.61 2.9,1.33 0.45,0.7 0.52,1.48 0.52,1.73 0,1.62 -0.56,2.7 -2.23,3.08 v 0.09 c 1.85,0.22 2.67,1.33 2.67,3.11 0,3.33 -2.43,3.66 -3.91,3.66 h -4.18 z m 1.65,-7.53 h 2.41 c 1.3,-0.02 1.93,-0.81 1.93,-2.07 0,-1.08 -0.61,-1.96 -2,-1.96 h -2.34 v 4.03 z m 0,6.09 h 2.34 c 1.77,0 2.39,-1.26 2.39,-2.21 0,-2.07 -1.28,-2.43 -2.97,-2.43 h -1.76 z"
       id="path3645" />
    		<path
       class="st2"
       d="m 1126.71,695.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3647" />
    		<path
       class="st2"
       d="m 1132.37,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 701 Z"
       id="path3649" />
    		<path
       class="st2"
       d="m 1136.99,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3651" />
    		<path
       class="st2"
       d="m 1146.77,708.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3653" />
    		<path
       class="st2"
       d="m 1156.36,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 701 Z"
       id="path3655" />
    		<path
       class="st2"
       d="m 1162.26,704.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3657" />
    		<path
       class="st2"
       d="m 1174.63,699.63 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.76,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.84,-4.45 0.96,0 1.71,0.41 2.12,1.3 h 0.04 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0.01,-1.34 0.1,-3.45 -1.76,-3.45 z"
       id="path3659" />
    		<path
       class="st2"
       d="m 1178.7,695.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3661" />
    		<path
       class="st2"
       d="m 1185.5,708.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path3663" />
    		<path
       class="st2"
       d="m 1190.97,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3665" />
    		<path
       class="st2"
       d="m 1197.35,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 701 Z"
       id="path3667" />
    		<path
       class="st2"
       d="m 1206.49,707.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3669" />
    		<path
       class="st2"
       d="m 1210.97,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3671" />
    		<path
       class="st2"
       d="m 1215.69,695.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3673" />
    		<path
       class="st2"
       d="m 1219.56,704.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path3675" />
    		<path
       class="st2"
       d="m 1233.74,708.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3677" />
    		<path
       class="st2"
       d="m 1246.49,707.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3679" />
    		<path
       class="st2"
       d="m 1255.74,708.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path3681" />
    		<path
       class="st2"
       d="m 1264.61,695.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.94,-0.58 -2.94,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3683" />
    		<path
       class="st2"
       d="m 1272.67,695.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3685" />
    		<path
       class="st2"
       d="m 1281.6,695.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3687" />
    		<path
       class="st2"
       d="m 1287.24,704.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3689" />
    		<path
       class="st2"
       d="m 1299.73,708.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3691" />
    		<path
       class="st2"
       d="m 1303.96,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3693" />
    		<path
       class="st2"
       d="m 1308.67,695.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3695" />
    		<path
       class="st2"
       d="m 1312.96,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3697" />
    		<path
       class="st2"
       d="m 1320.54,707.03 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path3699" />
    	</g></a>
    	<g
       class="st5"
       id="g3757">
    		<path
       class="st1"
       d="m 37.68,699.31 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.1,-0.11 -4.1,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.71 z"
       id="path3703" />
    		<path
       class="st1"
       d="m 46.74,708.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3705" />
    		<path
       class="st1"
       d="m 50.68,695.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3707" />
    		<path
       class="st1"
       d="m 56.24,708.73 h -1.48 v -13 h 1.48 z"
       id="path3709" />
    		<path
       class="st1"
       d="m 63.6,695.73 h 1.48 v 13 H 63.6 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3711" />
    		<path
       class="st1"
       d="m 69.33,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path3713" />
    		<path
       class="st1"
       d="m 75.23,704.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3715" />
    		<path
       class="st1"
       d="m 87.72,708.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3717" />
    		<path
       class="st1"
       d="m 94.65,699.63 h 1.64 l 1.64,7.83 h 0.04 l 2.02,-7.83 h 2.09 l 1.85,7.83 h 0.04 l 1.8,-7.83 h 1.57 l -2.43,9.09 h -1.98 l -1.94,-7.74 h -0.04 l -2.03,7.74 h -1.98 z"
       id="path3719" />
    		<path
       class="st1"
       d="m 108.66,695.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3721" />
    		<path
       class="st1"
       d="m 112.94,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3723" />
    		<path
       class="st1"
       d="m 122.71,708.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3725" />
    		<path
       class="st1"
       d="m 126.53,704.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0 1.91,-1.06 1.91,-4.01 z"
       id="path3727" />
    		<path
       class="st1"
       d="m 140.64,699.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path3729" />
    		<path
       class="st1"
       d="m 144.94,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3731" />
    		<path
       class="st1"
       d="m 155.38,700.71 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.8,-1.24 1.8,-3.67 z"
       id="path3733" />
    		<path
       class="st1"
       d="m 167.46,707.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3735" />
    		<path
       class="st1"
       d="m 173.31,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 701 Z"
       id="path3737" />
    		<path
       class="st1"
       d="m 179.21,704.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3739" />
    		<path
       class="st1"
       d="m 191.71,708.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3741" />
    		<path
       class="st1"
       d="m 195.94,699.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3743" />
    		<path
       class="st1"
       d="m 205.46,707.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3745" />
    		<path
       class="st1"
       d="m 211.22,708.73 h -1.48 v -13 h 1.48 z"
       id="path3747" />
    		<path
       class="st1"
       d="m 222.52,702.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3749" />
    		<path
       class="st1"
       d="m 231.45,707.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path3751" />
    		<path
       class="st1"
       d="m 237.3,701 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 701 Z"
       id="path3753" />
    		<path
       class="st1"
       d="m 243.2,704.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3755" />
    	</g>
    	<a
       id="a23895"><g
         class="st5"
         id="g3795">
    		<path
       class="st2"
       d="m 1200.71,766.32 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.11,-0.11 -4.11,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.7 z"
       id="path3759" />
    		<path
       class="st2"
       d="m 1209.76,775.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3761" />
    		<path
       class="st2"
       d="m 1213.7,762.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3763" />
    		<path
       class="st2"
       d="m 1219.26,775.73 h -1.48 v -13 h 1.48 z"
       id="path3765" />
    		<path
       class="st2"
       d="m 1226.63,762.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.09,-3.15 -1.72,-3.15 z"
       id="path3767" />
    		<path
       class="st2"
       d="m 1236.42,767.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.87,0 -1.5,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path3769" />
    		<path
       class="st2"
       d="m 1248.5,774.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3771" />
    		<path
       class="st2"
       d="m 1254.35,768.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3773" />
    		<path
       class="st2"
       d="m 1258.97,766.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3775" />
    		<path
       class="st2"
       d="m 1263.69,762.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3777" />
    		<path
       class="st2"
       d="m 1272.56,769.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3779" />
    		<path
       class="st2"
       d="m 1276.68,762.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3781" />
    		<path
       class="st2"
       d="m 1282.41,767.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.86,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.81,-1.24 1.81,-3.67 z"
       id="path3783" />
    		<path
       class="st2"
       d="m 1294.49,774.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3785" />
    		<path
       class="st2"
       d="m 1298.97,766.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3787" />
    		<path
       class="st2"
       d="m 1303.68,762.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3789" />
    		<path
       class="st2"
       d="m 1307.55,771.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3791" />
    		<path
       class="st2"
       d="m 1321.74,775.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3793" />
    	</g></a>
    	<a
       id="a38521"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#justice"
       target="blank"
       xlink:title="Justice for Children"><g
         class="st5"
         id="g3833">
    		<path
       class="st1"
       d="m 32.77,771.7 c 0.04,1.17 -0.11,2.92 1.58,2.92 1.76,0 1.87,-1.51 1.87,-3.1 v -8.79 h 1.66 v 9.78 c 0,0.7 -0.02,3.49 -3.58,3.49 -0.72,0 -2.11,-0.25 -2.74,-1.28 -0.52,-0.87 -0.52,-1.98 -0.52,-3.03 h 1.73 z"
       id="path3797" />
    		<path
       class="st1"
       d="m 45.66,766.64 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 H 45.6 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 z"
       id="path3799" />
    		<path
       class="st1"
       d="m 52.48,775.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3801" />
    		<path
       class="st1"
       d="m 57.95,766.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3803" />
    		<path
       class="st1"
       d="m 62.67,762.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3805" />
    		<path
       class="st1"
       d="m 71.54,769.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3807" />
    		<path
       class="st1"
       d="m 77.23,771.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3809" />
    		<path
       class="st1"
       d="m 89.05,766.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path3811" />
    		<path
       class="st1"
       d="m 93.54,771.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3813" />
    		<path
       class="st1"
       d="m 104.32,768.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path3815" />
    		<path
       class="st1"
       d="m 117.53,769.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3817" />
    		<path
       class="st1"
       d="m 126.71,775.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3819" />
    		<path
       class="st1"
       d="m 130.65,762.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3821" />
    		<path
       class="st1"
       d="m 136.21,775.73 h -1.48 v -13 h 1.48 z"
       id="path3823" />
    		<path
       class="st1"
       d="m 143.58,762.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.08,-3.15 -1.71,-3.15 z"
       id="path3825" />
    		<path
       class="st1"
       d="m 149.3,768.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3827" />
    		<path
       class="st1"
       d="m 155.2,771.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3829" />
    		<path
       class="st1"
       d="m 167.7,775.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3831" />
    	</g></a>
    	<g
       class="st5"
       id="g3885">
    		<path
       class="st2"
       d="m 1137.73,833.32 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.11,-0.11 -4.11,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.7 z"
       id="path3835" />
    		<path
       class="st2"
       d="m 1141.72,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3837" />
    		<path
       class="st2"
       d="m 1144.8,833.64 h 1.66 l 2.04,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.85,9.09 h -1.93 z"
       id="path3839" />
    		<path
       class="st2"
       d="m 1153.71,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3841" />
    		<path
       class="st2"
       d="m 1159.28,842.73 h -1.48 v -13 h 1.48 z"
       id="path3843" />
    		<path
       class="st2"
       d="m 1170.51,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3845" />
    		<path
       class="st2"
       d="m 1179.76,842.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3847" />
    		<path
       class="st2"
       d="m 1188.63,829.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3849" />
    		<path
       class="st2"
       d="m 1198.42,834.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.52,3.32 c 0,-1.37 0,-3.37 -1.86,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.81,-1.24 1.81,-3.67 z"
       id="path3851" />
    		<path
       class="st2"
       d="m 1205.57,838.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3853" />
    		<path
       class="st2"
       d="m 1216.26,842.73 h -1.48 v -13 h 1.48 z"
       id="path3855" />
    		<path
       class="st2"
       d="m 1218.69,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3857" />
    		<path
       class="st2"
       d="m 1222.97,833.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3859" />
    		<path
       class="st2"
       d="m 1227.69,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3861" />
    		<path
       class="st2"
       d="m 1236.57,836.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3863" />
    		<path
       class="st2"
       d="m 1245.49,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3865" />
    		<path
       class="st2"
       d="m 1251.25,842.73 h -1.48 v -13 h 1.48 z"
       id="path3867" />
    		<path
       class="st2"
       d="m 1258.07,833.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path3869" />
    		<path
       class="st2"
       d="m 1264.34,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3871" />
    		<path
       class="st2"
       d="m 1270.24,838.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3873" />
    		<path
       class="st2"
       d="m 1279.24,838.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3875" />
    		<path
       class="st2"
       d="m 1291.61,829.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3877" />
    		<path
       class="st2"
       d="m 1295.55,838.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3879" />
    		<path
       class="st2"
       d="m 1309.27,842.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3881" />
    		<path
       class="st2"
       d="m 1320.48,842.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path3883" />
    	</g>
    	<g
       class="st5"
       id="g3961">
    		<path
       class="st1"
       d="m 37.68,833.32 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.1,-0.11 -4.1,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.71 z"
       id="path3887" />
    		<path
       class="st1"
       d="m 46.74,842.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3889" />
    		<path
       class="st1"
       d="m 50.68,829.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path3891" />
    		<path
       class="st1"
       d="m 56.24,842.73 h -1.48 v -13 h 1.48 z"
       id="path3893" />
    		<path
       class="st1"
       d="m 63.6,829.73 h 1.48 v 13 H 63.6 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3895" />
    		<path
       class="st1"
       d="m 76.26,842.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3897" />
    		<path
       class="st1"
       d="m 89.47,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3899" />
    		<path
       class="st1"
       d="m 95.32,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path3901" />
    		<path
       class="st1"
       d="m 101.31,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path3903" />
    		<path
       class="st1"
       d="m 105.65,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3905" />
    		<path
       class="st1"
       d="m 114.45,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3907" />
    		<path
       class="st1"
       d="m 123.58,833.64 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.09,-3.45 -1.76,-3.45 z"
       id="path3909" />
    		<path
       class="st1"
       d="m 129.21,838.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3911" />
    		<path
       class="st1"
       d="m 145.45,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3913" />
    		<path
       class="st1"
       d="m 154.7,842.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3915" />
    		<path
       class="st1"
       d="m 163.57,829.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path3917" />
    		<path
       class="st1"
       d="m 171.51,838.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3919" />
    		<path
       class="st1"
       d="m 180.92,833.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path3921" />
    		<path
       class="st1"
       d="m 190.7,842.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3923" />
    		<path
       class="st1"
       d="m 196.21,838.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3925" />
    		<path
       class="st1"
       d="m 205.3,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3927" />
    		<path
       class="st1"
       d="m 218.69,842.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path3929" />
    		<path
       class="st1"
       d="m 227.44,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3931" />
    		<path
       class="st1"
       d="m 233.29,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3933" />
    		<path
       class="st1"
       d="m 242.21,842.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3935" />
    		<path
       class="st1"
       d="m 251.02,833.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path3937" />
    		<path
       class="st1"
       d="m 260.61,833.64 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path3939" />
    		<path
       class="st1"
       d="m 266.19,842.73 h -1.48 v -13 h 1.48 z"
       id="path3941" />
    		<path
       class="st1"
       d="m 274.34,834.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.8,-1.24 1.8,-3.67 z"
       id="path3943" />
    		<path
       class="st1"
       d="m 283.27,835.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3945" />
    		<path
       class="st1"
       d="m 292.42,841.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.39,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3947" />
    		<path
       class="st1"
       d="m 301.49,836.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3949" />
    		<path
       class="st1"
       d="m 305.9,833.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path3951" />
    		<path
       class="st1"
       d="m 310.61,829.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3953" />
    		<path
       class="st1"
       d="m 319.49,836.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path3955" />
    		<path
       class="st1"
       d="m 325.18,838.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3957" />
    		<path
       class="st1"
       d="m 335.42,842.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.41,0.43 -1.41,1.22 0,1.6 4.54,1.57 4.54,4.34 0.01,2.01 -1.36,2.78 -3.16,2.78 z"
       id="path3959" />
    	</g>
    	<g
       class="st5"
       id="g4047">
    		<path
       class="st2"
       d="m 996.89,909.73 h -1.66 v -13 h 1.66 z"
       id="path3963" />
    		<path
       class="st2"
       d="m 1004.8,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3965" />
    		<path
       class="st2"
       d="m 1009.13,900.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path3967" />
    		<path
       class="st2"
       d="m 1013.62,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.94,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3969" />
    		<path
       class="st2"
       d="m 1024.4,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3971" />
    		<path
       class="st2"
       d="m 1033.33,909.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path3973" />
    		<path
       class="st2"
       d="m 1046.54,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path3975" />
    		<path
       class="st2"
       d="m 1051.02,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3977" />
    		<path
       class="st2"
       d="m 1055.73,896.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3979" />
    		<path
       class="st2"
       d="m 1059.6,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path3981" />
    		<path
       class="st2"
       d="m 1073.79,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path3983" />
    		<path
       class="st2"
       d="m 1078.11,907.86 h 1.86 l -1.64,4.16 h -1.15 z"
       id="path3985" />
    		<path
       class="st2"
       d="m 1085.72,896.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path3987" />
    		<path
       class="st2"
       d="m 1094.78,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3989" />
    		<path
       class="st2"
       d="m 1099.01,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path3991" />
    		<path
       class="st2"
       d="m 1105.29,905.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3993" />
    		<path
       class="st2"
       d="m 1114.38,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path3995" />
    		<path
       class="st2"
       d="m 1123.78,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path3997" />
    		<path
       class="st2"
       d="m 1129.28,905.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path3999" />
    		<path
       class="st2"
       d="m 1137,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path4001" />
    		<path
       class="st2"
       d="m 1150.52,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path4003" />
    		<path
       class="st2"
       d="m 1159.77,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4005" />
    		<path
       class="st2"
       d="m 1168.65,896.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.08,-3.15 -1.72,-3.15 z"
       id="path4007" />
    		<path
       class="st2"
       d="m 1178.44,901.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path4009" />
    		<path
       class="st2"
       d="m 1187.37,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4011" />
    		<path
       class="st2"
       d="m 1191.58,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4013" />
    		<path
       class="st2"
       d="m 1200.99,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path4015" />
    		<path
       class="st2"
       d="m 1207.28,905.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4017" />
    		<path
       class="st2"
       d="m 1219.59,903.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4019" />
    		<path
       class="st2"
       d="m 1224,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path4021" />
    		<path
       class="st2"
       d="m 1228.71,896.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4023" />
    		<path
       class="st2"
       d="m 1232.58,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4025" />
    		<path
       class="st2"
       d="m 1246.77,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4027" />
    		<path
       class="st2"
       d="m 1254.58,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4029" />
    		<path
       class="st2"
       d="m 1264.1,900.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path4031" />
    		<path
       class="st2"
       d="m 1274.43,901.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.8,-1.24 1.8,-3.67 z"
       id="path4033" />
    		<path
       class="st2"
       d="m 1283.36,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4035" />
    		<path
       class="st2"
       d="m 1287.7,896.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path4037" />
    		<path
       class="st2"
       d="m 1290.78,900.64 h 1.66 l 2.04,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path4039" />
    		<path
       class="st2"
       d="m 1304.49,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path4041" />
    		<path
       class="st2"
       d="m 1313.56,903.56 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4043" />
    		<path
       class="st2"
       d="m 1320.55,908.04 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path4045" />
    	</g>
    	<g
       class="st5"
       id="g4125">
    		<path
       class="st1"
       d="m 37.68,900.32 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.1,-0.11 -4.1,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 h -1.71 z"
       id="path4049" />
    		<path
       class="st1"
       d="m 46.74,909.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path4051" />
    		<path
       class="st1"
       d="m 50.68,896.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path4053" />
    		<path
       class="st1"
       d="m 56.24,909.73 h -1.48 v -13 h 1.48 z"
       id="path4055" />
    		<path
       class="st1"
       d="m 63.6,896.73 h 1.48 v 13 H 63.6 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4057" />
    		<path
       class="st1"
       d="m 73.23,909.73 h -1.48 v -13 h 1.48 z"
       id="path4059" />
    		<path
       class="st1"
       d="m 80.47,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path4061" />
    		<path
       class="st1"
       d="m 86.39,909.73 h -1.48 v -13 h 1.48 v 4.83 h 0.05 c 0.5,-0.72 1.13,-1.1 2,-1.1 2.93,0 3.01,2.61 3.01,4.88 0,4 -1.48,4.57 -2.94,4.57 -0.95,0 -1.58,-0.41 -2.09,-1.26 h -0.04 v 1.08 z m 1.66,-1.02 c 1.85,0 1.85,-1.98 1.85,-3.35 0,-2.43 -0.22,-3.69 -1.8,-3.69 -1.64,0 -1.71,1.94 -1.71,3.15 0,1.39 -0.16,3.89 1.66,3.89 z"
       id="path4063" />
    		<path
       class="st1"
       d="m 93.54,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4065" />
    		<path
       class="st1"
       d="m 107.65,900.64 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path4067" />
    		<path
       class="st1"
       d="m 113.32,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path4069" />
    		<path
       class="st1"
       d="m 126.46,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path4071" />
    		<path
       class="st1"
       d="m 135.71,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4073" />
    		<path
       class="st1"
       d="m 144.58,896.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4075" />
    		<path
       class="st1"
       d="m 152.52,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4077" />
    		<path
       class="st1"
       d="m 161.93,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4079" />
    		<path
       class="st1"
       d="m 171.71,909.73 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path4081" />
    		<path
       class="st1"
       d="m 177.22,905.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4083" />
    		<path
       class="st1"
       d="m 186.31,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4085" />
    		<path
       class="st1"
       d="m 195.04,900.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path4087" />
    		<path
       class="st1"
       d="m 199.52,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4089" />
    		<path
       class="st1"
       d="m 210.3,902.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4091" />
    		<path
       class="st1"
       d="m 219.23,909.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path4093" />
    		<path
       class="st1"
       d="m 230.44,909.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path4095" />
    		<path
       class="st1"
       d="m 239.5,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4097" />
    		<path
       class="st1"
       d="m 249.02,900.64 v -1.76 c 0,-1.84 1.3,-2.2 2.61,-2.2 0.31,0 0.49,0.02 0.7,0.05 v 1.06 c -1.57,-0.11 -1.84,0.56 -1.84,1.3 v 1.55 h 1.84 v 1.12 h -1.84 v 7.98 h -1.48 v -7.98 h -1.4 v -1.12 h 1.41 z"
       id="path4099" />
    		<path
       class="st1"
       d="m 259.19,905.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4101" />
    		<path
       class="st1"
       d="m 273.32,909.73 h -1.94 l -2.11,-3.73 -1.96,3.73 h -1.75 l 2.83,-4.75 -2.59,-4.34 h 1.89 l 1.73,3.26 1.84,-3.26 h 1.78 l -2.72,4.34 z"
       id="path4103" />
    		<path
       class="st1"
       d="m 276.34,901.72 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.59,0 1.8,-1.24 1.8,-3.67 z"
       id="path4105" />
    		<path
       class="st1"
       d="m 285.18,909.73 h -1.48 v -13 h 1.48 z"
       id="path4107" />
    		<path
       class="st1"
       d="m 287.48,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4109" />
    		<path
       class="st1"
       d="m 296.61,896.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4111" />
    		<path
       class="st1"
       d="m 300.89,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path4113" />
    		<path
       class="st1"
       d="m 310.42,908.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path4115" />
    		<path
       class="st1"
       d="m 314.9,900.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path4117" />
    		<path
       class="st1"
       d="m 319.61,896.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4119" />
    		<path
       class="st1"
       d="m 323.48,905.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path4121" />
    		<path
       class="st1"
       d="m 337.67,909.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4123" />
    	</g>
    	<g
       class="st5"
       id="g4161">
    		<path
       class="st4"
       d="m 1187,976.73 v -13 h 1.66 v 11.56 h 4.77 v 1.44 z"
       id="path4127" />
    		<path
       class="st4"
       d="m 1196.27,972.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4129" />
    		<path
       class="st4"
       d="m 1203.7,963.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4131" />
    		<path
       class="st4"
       d="m 1210.51,976.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 -0.01,2 -1.37,2.78 -3.17,2.78 z"
       id="path4133" />
    		<path
       class="st4"
       d="m 1220.68,967.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path4135" />
    		<path
       class="st4"
       d="m 1226.34,969 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.12,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 969 Z"
       id="path4137" />
    		<path
       class="st4"
       d="m 1232.25,972.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4139" />
    		<path
       class="st4"
       d="m 1248.49,975.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4141" />
    		<path
       class="st4"
       d="m 1257.74,976.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4143" />
    		<path
       class="st4"
       d="m 1266.61,963.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4145" />
    		<path
       class="st4"
       d="m 1279.55,970.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.86,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4147" />
    		<path
       class="st4"
       d="m 1288.66,967.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path4149" />
    		<path
       class="st4"
       d="m 1294.24,976.73 h -1.48 v -13 h 1.48 z"
       id="path4151" />
    		<path
       class="st4"
       d="m 1296.96,967.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path4153" />
    		<path
       class="st4"
       d="m 1306.66,967.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path4155" />
    		<path
       class="st4"
       d="m 1312.33,969 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 V 969 Z"
       id="path4157" />
    		<path
       class="st4"
       d="m 1318.23,972.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4159" />
    	</g>
    	<a
       id="a22287"
       xlink:href="https://tm-dash.azurewebsites.net/child-education#system"
       target="blank"
       xlink:title="Education System"><g
         class="st5"
         id="g4193">
    		<path
       class="st4"
       d="m 31.96,976.73 v -13 h 6.7 v 1.44 h -5.04 v 4.18 h 4.68 v 1.44 h -4.68 v 4.5 h 5.15 v 1.44 h -6.81 z"
       id="path4163" />
    		<path
       class="st4"
       d="m 45.6,963.73 h 1.48 v 13 H 45.6 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4165" />
    		<path
       class="st4"
       d="m 54.66,967.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 H 54.6 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 z"
       id="path4167" />
    		<path
       class="st4"
       d="m 63.55,970.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4169" />
    		<path
       class="st4"
       d="m 72.48,975.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4171" />
    		<path
       class="st4"
       d="m 76.96,967.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4173" />
    		<path
       class="st4"
       d="m 81.67,963.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4175" />
    		<path
       class="st4"
       d="m 85.54,972.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path4177" />
    		<path
       class="st4"
       d="m 99.73,976.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 H 94.8 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4179" />
    		<path
       class="st4"
       d="m 110.47,976.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.36,2.78 -3.17,2.78 z"
       id="path4181" />
    		<path
       class="st4"
       d="m 118.52,975.03 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path4183" />
    		<path
       class="st4"
       d="m 126.46,976.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 H 125 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path4185" />
    		<path
       class="st4"
       d="m 131.93,967.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4187" />
    		<path
       class="st4"
       d="m 138.21,972.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4189" />
    		<path
       class="st4"
       d="m 150.24,976.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path4191" />
    	</g></a>
    	<g
       class="st5"
       id="g4243">
    		<path
       class="st4"
       d="m 1140.04,1043.73 v -13 h 1.66 v 11.56 h 4.77 v 1.44 z"
       id="path4195" />
    		<path
       class="st4"
       d="m 1149.31,1039.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4197" />
    		<path
       class="st4"
       d="m 1161.55,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4199" />
    		<path
       class="st4"
       d="m 1167.4,1036 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4201" />
    		<path
       class="st4"
       d="m 1176.79,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path4203" />
    		<path
       class="st4"
       d="m 1180.73,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4205" />
    		<path
       class="st4"
       d="m 1189.79,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path4207" />
    		<path
       class="st4"
       d="m 1198.66,1034.63 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.84,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.72,1.05 c -1.68,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.34 0.09,-3.45 -1.76,-3.45 z"
       id="path4209" />
    		<path
       class="st4"
       d="m 1211.66,1034.63 h 1.48 v 12.53 h -1.48 v -4.36 h -0.05 c -0.5,0.72 -1.13,1.1 -2,1.1 -2.93,0 -3.01,-2.61 -3.01,-4.88 0,-4 1.48,-4.57 2.93,-4.57 0.95,0 1.58,0.41 2.09,1.26 h 0.04 z m 0,4.94 c 0,-1.39 0.16,-3.87 -1.66,-3.87 -1.85,0 -1.85,1.96 -1.85,3.33 0,2.43 0.22,3.67 1.8,3.67 1.64,0 1.71,-1.93 1.71,-3.13 z"
       id="path4211" />
    		<path
       class="st4"
       d="m 1220.71,1034.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path4213" />
    		<path
       class="st4"
       d="m 1229.53,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4215" />
    		<path
       class="st4"
       d="m 1235.29,1043.73 h -1.48 v -13 h 1.48 z"
       id="path4217" />
    		<path
       class="st4"
       d="m 1237.72,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4219" />
    		<path
       class="st4"
       d="m 1242.01,1034.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path4221" />
    		<path
       class="st4"
       d="m 1249.58,1042.03 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path4223" />
    		<path
       class="st4"
       d="m 1263.52,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4225" />
    		<path
       class="st4"
       d="m 1272.77,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path4227" />
    		<path
       class="st4"
       d="m 1281.64,1030.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.94,-0.58 -2.94,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4229" />
    		<path
       class="st4"
       d="m 1292.51,1043.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path4231" />
    		<path
       class="st4"
       d="m 1299.3,1043.73 h -1.48 v -13 h 1.48 v 7.83 h 0.04 l 2.77,-3.92 h 1.8 l -3.03,3.91 3.56,5.19 h -1.87 l -3.24,-5.1 h -0.04 v 5.09 z"
       id="path4233" />
    		<path
       class="st4"
       d="m 1305.69,1030.73 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path4235" />
    		<path
       class="st4"
       d="m 1311.25,1043.73 h -1.48 v -13 h 1.48 z"
       id="path4237" />
    		<path
       class="st4"
       d="m 1315.25,1043.73 h -1.48 v -13 h 1.48 z"
       id="path4239" />
    		<path
       class="st4"
       d="m 1320.48,1043.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path4241" />
    	</g>
    	<g
       class="st5"
       id="g4307">
    		<path
       class="st4"
       d="m 31.96,1043.73 v -13 h 6.7 v 1.44 h -5.04 v 4.18 h 4.68 v 1.44 h -4.68 v 4.5 h 5.15 v 1.44 h -6.81 z"
       id="path4245" />
    		<path
       class="st4"
       d="m 45.6,1030.73 h 1.48 v 13 H 45.6 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4247" />
    		<path
       class="st4"
       d="m 54.66,1034.63 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 H 54.6 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 z"
       id="path4249" />
    		<path
       class="st4"
       d="m 63.55,1037.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4251" />
    		<path
       class="st4"
       d="m 72.48,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4253" />
    		<path
       class="st4"
       d="m 76.96,1034.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4255" />
    		<path
       class="st4"
       d="m 81.67,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4257" />
    		<path
       class="st4"
       d="m 85.54,1039.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path4259" />
    		<path
       class="st4"
       d="m 99.73,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 H 94.8 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4261" />
    		<path
       class="st4"
       d="m 112.47,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4263" />
    		<path
       class="st4"
       d="m 121.55,1037.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4265" />
    		<path
       class="st4"
       d="m 130.55,1037.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4267" />
    		<path
       class="st4"
       d="m 136.23,1039.66 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path4269" />
    		<path
       class="st4"
       d="m 146.47,1043.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.36,2.78 -3.17,2.78 z"
       id="path4271" />
    		<path
       class="st4"
       d="m 154.47,1043.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path4273" />
    		<path
       class="st4"
       d="m 168.45,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4275" />
    		<path
       class="st4"
       d="m 177.7,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4277" />
    		<path
       class="st4"
       d="m 186.58,1030.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path4279" />
    		<path
       class="st4"
       d="m 196.37,1035.71 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path4281" />
    		<path
       class="st4"
       d="m 208.45,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4283" />
    		<path
       class="st4"
       d="m 214.3,1036 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path4285" />
    		<path
       class="st4"
       d="m 218.92,1034.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4287" />
    		<path
       class="st4"
       d="m 223.64,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4289" />
    		<path
       class="st4"
       d="m 232.51,1037.55 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path4291" />
    		<path
       class="st4"
       d="m 236.63,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4293" />
    		<path
       class="st4"
       d="m 242.36,1035.71 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path4295" />
    		<path
       class="st4"
       d="m 254.44,1042.41 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path4297" />
    		<path
       class="st4"
       d="m 258.92,1034.63 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path4299" />
    		<path
       class="st4"
       d="m 263.63,1030.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path4301" />
    		<path
       class="st4"
       d="m 267.5,1039.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path4303" />
    		<path
       class="st4"
       d="m 281.69,1043.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path4305" />
    	</g>
    	<line
       class="st6"
       x1="724.09003"
       y1="393.17001"
       x2="724.09003"
       y2="380.62"
       id="line4309" />
    	<line
       class="st7"
       x1="727.07001"
       y1="379.23001"
       x2="1322.02"
       y2="379.23001"
       id="line4311" />
    	<path
       class="st8"
       d="m 724.09,395.96 v 0 m 0,-16.73 v 0 m 599.42,0 v 0"
       id="path4313" />
    	<path
       class="st0"
       d="m 724.09,398.73 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.54,0 -2.78,1.24 -2.78,2.78 0,1.54 1.24,2.78 2.78,2.78 z"
       id="path4315" />
    	<line
       class="st9"
       x1="721.32001"
       y1="1008.47"
       x2="721.32001"
       y2="1046.71"
       id="line4317" />
    	<line
       class="st10"
       x1="724.29999"
       y1="1048.24"
       x2="1322.02"
       y2="1048.24"
       id="line4319" />
    	<path
       class="st11"
       d="m 721.32,1005.41 v 0 m 0,42.83 v 0 m 602.19,0 v 0"
       id="path4321" />
    	<path
       class="st4"
       d="m 721.32,1002.63 c 1.53,0 2.78,1.24 2.78,2.78 0,1.53 -1.24,2.78 -2.78,2.78 -1.53,0 -2.78,-1.25 -2.78,-2.78 0,-1.54 1.25,-2.78 2.78,-2.78 z"
       id="path4323" />
    	<path
       class="st12"
       d="m 884.35,934.73 c 9.93,0 42.27,0 61.35,0"
       id="path4325" />
    	<line
       class="st13"
       x1="947.20001"
       y1="931.95001"
       x2="947.20001"
       y2="916.62"
       id="line4327" />
    	<line
       class="st14"
       x1="950.17999"
       y1="915.22998"
       x2="1322.02"
       y2="915.22998"
       id="line4329" />
    	<path
       class="st15"
       d="m 881.35,934.73 v 0 m 65.85,0 v 0 m 0,-19.5 v 0 m 376.31,0 v 0"
       id="path4331" />
    	<path
       class="st2"
       d="m 881.35,937.51 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.54 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0.01,1.54 1.25,2.78 2.78,2.78 z"
       id="path4333" />
    	<line
       class="st16"
       x1="940.02002"
       y1="867.72998"
       x2="1007.11"
       y2="867.72998"
       id="line4335" />
    	<line
       class="st13"
       x1="1008.6"
       y1="864.95001"
       x2="1008.6"
       y2="849.62"
       id="line4337" />
    	<line
       class="st17"
       x1="1011.57"
       y1="848.22998"
       x2="1322.03"
       y2="848.22998"
       id="line4339" />
    	<path
       class="st15"
       d="m 937.03,867.73 v 0 m 71.57,0 v 0 m 0,-19.5 v 0 m 314.91,0 v 0"
       id="path4341" />
    	<path
       class="st2"
       d="m 937.03,870.51 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0.01,1.54 1.25,2.78 2.78,2.78 z"
       id="path4343" />
    	<line
       class="st18"
       x1="971.90002"
       y1="798.72998"
       x2="1019.23"
       y2="798.72998"
       id="line4345" />
    	<path
       class="st19"
       d="m 1020.76,795.73 c 0,-2.3 0,-6.35 0,-13.5"
       id="path4347" />
    	<line
       class="st20"
       x1="1023.72"
       y1="780.72998"
       x2="1322.03"
       y2="780.72998"
       id="line4349" />
    	<path
       class="st15"
       d="m 968.85,798.73 v 0 m 51.91,0 v 0 m 0,-18 v 0 m 302.75,0 v 0"
       id="path4351" />
    	<path
       class="st2"
       d="m 968.85,801.51 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.54 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.54 1.25,2.78 2.78,2.78 z"
       id="path4353" />
    	<line
       class="st21"
       x1="990.64001"
       y1="693.72998"
       x2="1026.8101"
       y2="693.72998"
       id="line4355" />
    	<line
       class="st22"
       x1="1028.26"
       y1="696.59003"
       x2="1028.26"
       y2="712.29999"
       id="line4357" />
    	<line
       class="st23"
       x1="1031.25"
       y1="713.72998"
       x2="1322.51"
       y2="713.72998"
       id="line4359" />
    	<path
       class="st15"
       d="m 987.74,693.73 v 0 m 40.52,0 v 0 m 0,20 v 0 m 295.74,0 v 0"
       id="path4361" />
    	<path
       class="st2"
       d="m 987.74,696.51 c 1.54,0 2.78,-1.24 2.78,-2.78 0,-1.54 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.54 1.25,2.78 2.78,2.78 z"
       id="path4363" />
    	<line
       class="st24"
       x1="815.76001"
       y1="423.32001"
       x2="883.71997"
       y2="423.32001"
       id="line4365" />
    	<line
       class="st25"
       x1="885.22998"
       y1="426.12"
       x2="885.22998"
       y2="444.32999"
       id="line4367" />
    	<line
       class="st26"
       x1="888.21002"
       y1="445.73001"
       x2="1322.02"
       y2="445.73001"
       id="line4369" />
    	<path
       class="st8"
       d="m 812.73,423.32 v 0 m 72.5,0 v 0 m 0,22.41 v 0 m 438.28,0 v 0"
       id="path4371" />
    	<path
       class="st0"
       d="m 812.73,426.1 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.54 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.54 1.25,2.78 2.78,2.78 z"
       id="path4373" />
    	<line
       class="st27"
       x1="888.35999"
       y1="471.73001"
       x2="965.59003"
       y2="471.73001"
       id="line4375" />
    	<line
       class="st28"
       x1="967.10999"
       y1="474.66"
       x2="967.10999"
       y2="511.26999"
       id="line4377" />
    	<line
       class="st29"
       x1="970.08002"
       y1="512.72998"
       x2="1322.52"
       y2="512.72998"
       id="line4379" />
    	<path
       class="st8"
       d="m 885.33,471.73 v 0 m 81.78,0 v 0 m 0,41 v 0 m 356.89,0 v 0"
       id="path4381" />
    	<path
       class="st0"
       d="m 885.33,474.51 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.54 1.25,2.78 2.78,2.78 z"
       id="path4383" />
    	<line
       class="st30"
       x1="942.83002"
       y1="538.79999"
       x2="997.03998"
       y2="538.79999"
       id="line4385" />
    	<line
       class="st31"
       x1="998.51001"
       y1="541.72998"
       x2="998.51001"
       y2="578.34003"
       id="line4387" />
    	<line
       class="st32"
       x1="1001.47"
       y1="579.79999"
       x2="1323.02"
       y2="579.79999"
       id="line4389" />
    	<path
       class="st33"
       d="m 939.9,538.8 v 0 m 58.61,0 v 0 m 0,41 v 0 m 325.99,0 v 0"
       id="path4391" />
    	<path
       class="st3"
       d="m 939.9,541.58 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 z"
       id="path4393" />
    	<line
       class="st34"
       x1="812.77002"
       y1="982.53003"
       x2="812.77002"
       y2="1014.22"
       id="line4395" />
    	<line
       class="st35"
       x1="815.71997"
       y1="1015.73"
       x2="893.95001"
       y2="1015.73"
       id="line4397" />
    	<line
       class="st36"
       x1="895.41998"
       y1="1012.86"
       x2="895.41998"
       y2="982.66998"
       id="line4399" />
    	<line
       class="st37"
       x1="898.40002"
       y1="981.23999"
       x2="1322.02"
       y2="981.23999"
       id="line4401" />
    	<path
       class="st11"
       d="m 812.77,979.51 v 0 m 0,36.22 v 0 m 82.65,0 v 0 m 0,-34.49 v 0 m 428.09,0 v 0"
       id="path4403" />
    	<path
       class="st4"
       d="m 812.77,976.73 c 1.53,0 2.78,1.25 2.78,2.78 0,1.54 -1.24,2.78 -2.78,2.78 -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.25,-2.78 2.78,-2.78 z"
       id="path4405" />
    	<line
       class="st6"
       x1="631.14001"
       y1="393.17001"
       x2="631.14001"
       y2="380.62"
       id="line4407" />
    	<line
       class="st7"
       x1="628.15997"
       y1="379.23001"
       x2="33.200001"
       y2="379.23001"
       id="line4409" />
    	<path
       class="st8"
       d="m 631.14,395.96 v 0 m 0,-16.73 v 0 m -599.43,0 v 0"
       id="path4411" />
    	<path
       class="st0"
       d="m 631.14,398.73 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.24,-2.78 2.78,-2.78 1.54,0 2.78,1.24 2.78,2.78 -0.01,1.54 -1.25,2.78 -2.78,2.78 z"
       id="path4413" />
    	<line
       class="st9"
       x1="633.90002"
       y1="1008.47"
       x2="633.90002"
       y2="1046.71"
       id="line4415" />
    	<line
       class="st10"
       x1="630.91998"
       y1="1048.24"
       x2="33.200001"
       y2="1048.24"
       id="line4417" />
    	<path
       class="st11"
       d="m 633.9,1005.41 v 0 m 0,42.83 v 0 m -602.19,0 v 0"
       id="path4419" />
    	<path
       class="st4"
       d="m 633.9,1002.63 c -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 1.53,0 2.78,-1.25 2.78,-2.78 0,-1.54 -1.25,-2.78 -2.78,-2.78 z"
       id="path4421" />
    	<path
       class="st38"
       d="m 470.87,934.73 c -9.93,0 -42.26,0 -61.35,0"
       id="path4423" />
    	<line
       class="st39"
       x1="408.03"
       y1="931.95001"
       x2="408.03"
       y2="916.62"
       id="line4425" />
    	<line
       class="st40"
       x1="405.04001"
       y1="915.22998"
       x2="33.200001"
       y2="915.22998"
       id="line4427" />
    	<path
       class="st41"
       d="m 473.87,934.73 v 0 m -65.84,0 v 0 m 0,-19.5 v 0 m -376.32,0 v 0"
       id="path4429" />
    	<path
       class="st1"
       d="m 473.87,937.51 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.54 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 -0.01,1.54 -1.25,2.78 -2.78,2.78 z"
       id="path4431" />
    	<line
       class="st42"
       x1="415.20999"
       y1="867.72998"
       x2="348.10999"
       y2="867.72998"
       id="line4433" />
    	<line
       class="st39"
       x1="346.62"
       y1="864.95001"
       x2="346.62"
       y2="849.62"
       id="line4435" />
    	<line
       class="st43"
       x1="343.64999"
       y1="848.22998"
       x2="33.200001"
       y2="848.22998"
       id="line4437" />
    	<path
       class="st41"
       d="m 418.19,867.73 v 0 m -71.57,0 v 0 m 0,-19.5 v 0 m -314.91,0 v 0"
       id="path4439" />
    	<path
       class="st1"
       d="m 418.19,870.51 c -1.54,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.54 -1.25,2.78 -2.78,2.78 z"
       id="path4441" />
    	<line
       class="st44"
       x1="383.32001"
       y1="798.72998"
       x2="335.98999"
       y2="798.72998"
       id="line4443" />
    	<path
       class="st45"
       d="m 334.47,795.73 c 0,-2.3 0,-6.35 0,-13.5"
       id="path4445" />
    	<line
       class="st46"
       x1="331.5"
       y1="780.72998"
       x2="33.200001"
       y2="780.72998"
       id="line4447" />
    	<path
       class="st41"
       d="m 386.37,798.73 v 0 m -51.9,0 v 0 m 0,-18 v 0 m -302.76,0 v 0"
       id="path4449" />
    	<path
       class="st1"
       d="m 386.37,801.51 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.54 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.54 -1.24,2.78 -2.78,2.78 z"
       id="path4451" />
    	<line
       class="st47"
       x1="364.59"
       y1="693.72998"
       x2="328.41"
       y2="693.72998"
       id="line4453" />
    	<line
       class="st48"
       x1="326.95999"
       y1="696.59003"
       x2="326.95999"
       y2="712.29999"
       id="line4455" />
    	<line
       class="st49"
       x1="323.97"
       y1="713.72998"
       x2="32.709999"
       y2="713.72998"
       id="line4457" />
    	<path
       class="st41"
       d="m 367.48,693.73 v 0 m -40.52,0 v 0 m 0,20 v 0 m -295.74,0 v 0"
       id="path4459" />
    	<path
       class="st1"
       d="m 367.48,696.51 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.54 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.54 -1.24,2.78 -2.78,2.78 z"
       id="path4461" />
    	<line
       class="st24"
       x1="539.46997"
       y1="423.32001"
       x2="471.5"
       y2="423.32001"
       id="line4463" />
    	<line
       class="st25"
       x1="469.98999"
       y1="426.12"
       x2="469.98999"
       y2="444.32999"
       id="line4465" />
    	<line
       class="st26"
       x1="467.01001"
       y1="445.73001"
       x2="33.200001"
       y2="445.73001"
       id="line4467" />
    	<path
       class="st8"
       d="m 542.49,423.32 v 0 m -72.5,0 v 0 m 0,22.41 v 0 m -438.28,0 v 0"
       id="path4469" />
    	<path
       class="st0"
       d="m 542.49,426.1 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.54 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.54 -1.25,2.78 -2.78,2.78 z"
       id="path4471" />
    	<line
       class="st27"
       x1="466.85999"
       y1="471.73001"
       x2="389.63"
       y2="471.73001"
       id="line4473" />
    	<line
       class="st28"
       x1="388.10999"
       y1="474.66"
       x2="388.10999"
       y2="511.26999"
       id="line4475" />
    	<line
       class="st29"
       x1="385.14001"
       y1="512.72998"
       x2="32.709999"
       y2="512.72998"
       id="line4477" />
    	<path
       class="st8"
       d="m 469.89,471.73 v 0 m -81.78,0 v 0 m 0,41 v 0 m -356.89,0 v 0"
       id="path4479" />
    	<path
       class="st0"
       d="m 469.89,474.51 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.54 -1.25,2.78 -2.78,2.78 z"
       id="path4481" />
    	<line
       class="st50"
       x1="409.57001"
       y1="538.23999"
       x2="343.20999"
       y2="538.23999"
       id="line4483" />
    	<line
       class="st28"
       x1="341.73001"
       y1="541.16998"
       x2="341.73001"
       y2="577.77002"
       id="line4485" />
    	<line
       class="st51"
       x1="338.75"
       y1="579.23999"
       x2="32.709999"
       y2="579.23999"
       id="line4487" />
    	<path
       class="st8"
       d="m 412.52,538.24 v 0 m -70.79,0 v 0 m 0,41 v 0 m -310.51,0 v 0"
       id="path4489" />
    	<path
       class="st0"
       d="m 412.52,541.02 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 0,1.53 -1.25,2.78 -2.78,2.78 z"
       id="path4491" />
    	<line
       class="st52"
       x1="376.39999"
       y1="605.23999"
       x2="316.35999"
       y2="605.23999"
       id="line4493" />
    	<line
       class="st52"
       x1="314.89999"
       y1="608.16998"
       x2="314.89999"
       y2="644.77002"
       id="line4495" />
    	<line
       class="st53"
       x1="311.91"
       y1="646.23999"
       x2="32.709999"
       y2="646.23999"
       id="line4497" />
    	<path
       class="st41"
       d="m 379.33,605.24 v 0 m -64.43,0 v 0 m 0,41 v 0 m -283.68,0 v 0"
       id="path4499" />
    	<path
       class="st1"
       d="m 379.33,608.02 c -1.53,0 -2.78,-1.24 -2.78,-2.78 0,-1.53 1.24,-2.78 2.78,-2.78 1.53,0 2.78,1.24 2.78,2.78 -0.01,1.53 -1.25,2.78 -2.78,2.78 z"
       id="path4501" />
    	<line
       class="st34"
       x1="542.45001"
       y1="982.53003"
       x2="542.45001"
       y2="1014.22"
       id="line4503" />
    	<line
       class="st35"
       x1="539.5"
       y1="1015.73"
       x2="461.26999"
       y2="1015.73"
       id="line4505" />
    	<line
       class="st36"
       x1="459.79999"
       y1="1012.86"
       x2="459.79999"
       y2="982.66998"
       id="line4507" />
    	<line
       class="st37"
       x1="456.82001"
       y1="981.23999"
       x2="33.200001"
       y2="981.23999"
       id="line4509" />
    	<path
       class="st11"
       d="m 542.45,979.51 v 0 m 0,36.22 v 0 m -82.65,0 v 0 m 0,-34.49 v 0 m -428.09,0 v 0"
       id="path4511" />
    	<path
       class="st4"
       d="m 542.45,976.73 c -1.53,0 -2.78,1.25 -2.78,2.78 0,1.54 1.24,2.78 2.78,2.78 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.25,-2.78 -2.78,-2.78 z"
       id="path4513" />
    	<a
       id="a17463"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:title="Violence"><path
         class="st54"
         d="m 437.9,627.88 h -0.65 c -0.8,0 -1.46,0.65 -1.46,1.46 v 7.1 l -3.29,-3.7 c -0.31,-0.35 -0.77,-0.53 -1.25,-0.48 -0.47,0.05 -0.89,0.33 -1.12,0.74 l -3.64,6.56 c -0.39,0.7 -0.14,1.59 0.57,1.98 0.22,0.12 0.47,0.18 0.71,0.18 0.51,0 1.01,-0.27 1.28,-0.75 l 2.65,-4.77 4.47,5.02 c 0.01,0.01 0.02,0.02 0.03,0.03 0.03,0.04 0.07,0.07 0.11,0.1 0.04,0.03 0.07,0.06 0.11,0.09 0.04,0.03 0.08,0.05 0.12,0.07 0.04,0.02 0.08,0.05 0.12,0.07 0.04,0.02 0.09,0.03 0.13,0.05 0.05,0.01 0.09,0.03 0.14,0.04 0.04,0.01 0.09,0.02 0.13,0.02 0.05,0.01 0.1,0.01 0.15,0.01 0.01,0 0.03,0.01 0.04,0.01 h 3.65 c 0.81,0 1.46,-0.65 1.46,-1.46 v -7.95 c -0.01,-2.43 -2,-4.42 -4.46,-4.42 z"
         id="path4515" /></a>
    	<a
       id="a17469"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:title="Violence"><path
         class="st54"
         d="m 433.24,622.78 c -1.41,0 -2.55,1.14 -2.55,2.55 0,1.41 1.14,2.55 2.55,2.55 1.41,0 2.55,-1.14 2.55,-2.55 0,-1.41 -1.14,-2.55 -2.55,-2.55 z"
         id="path4517" /></a>
    	<a
       id="a17460"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:title="Violence"><path
         class="st54"
         d="m 416.83,614.03 c -5.49,0 -9.48,3.68 -9.48,8.75 0,0.8 0.65,1.46 1.46,1.46 0.81,0 1.46,-0.65 1.46,-1.46 0,-2.2 1.11,-3.97 2.92,-4.96 v 10.14 c 0,0.02 0.01,0.04 0.01,0.06 0,0.02 -0.01,0.04 -0.01,0.06 v 12.2 c 0,0.81 0.65,1.46 1.46,1.46 0.81,0 1.46,-0.65 1.46,-1.46 v -10.94 h 1.46 v 10.94 c 0,0.81 0.65,1.46 1.46,1.46 0.81,0 1.46,-0.65 1.46,-1.46 v -12.2 c 0,-0.02 0,-0.04 -0.01,-0.06 0,-0.02 0.01,-0.04 0.01,-0.06 v -10.14 c 1.81,0.99 2.92,2.76 2.92,4.96 0,0.8 0.65,1.46 1.46,1.46 0.81,0 1.46,-0.65 1.46,-1.46 -0.02,-5.07 -4,-8.75 -9.5,-8.75 z"
         id="path4519" /></a>
    	<a
       id="a17466"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:title="Violence"><path
         class="st54"
         d="m 421.21,613.3 c 1.61,0 2.92,-1.31 2.92,-2.92 0,-1.61 -1.31,-2.92 -2.92,-2.92 -1.61,0 -2.92,1.31 -2.92,2.92 0,1.61 1.31,2.92 2.92,2.92 z"
         id="path4521" /></a>
    	<a
       id="a17475"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       xlink:title="Violence"
       target="blank"><path
         class="st54"
         d="m 431.42,612.93 c 0,0.6 0.49,1.09 1.09,1.09 h 2.92 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.49,-1.09 -1.09,-1.09 h -2.92 c -0.6,0 -1.09,0.49 -1.09,1.09 z"
         id="path4523" /></a>
    	<a
       id="a17472"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       xlink:title="Violence"
       target="blank"><path
         class="st54"
         d="m 429.11,611.72 c 0.16,0.08 0.32,0.12 0.49,0.12 0.4,0 0.79,-0.22 0.98,-0.6 l 1.46,-2.92 c 0.27,-0.54 0.05,-1.2 -0.49,-1.47 -0.54,-0.27 -1.2,-0.05 -1.47,0.49 l -1.46,2.92 c -0.27,0.53 -0.06,1.19 0.49,1.46 z"
         id="path4525" /></a>
    	<a
       id="a17478"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#violence"
       target="blank"
       xlink:title="Violence"><path
         class="st54"
         d="m 430.07,618.53 c 0.19,0.38 0.58,0.6 0.98,0.6 0.17,0 0.33,-0.04 0.49,-0.12 0.54,-0.27 0.76,-0.93 0.49,-1.47 l -1.46,-2.92 c -0.27,-0.54 -0.93,-0.76 -1.47,-0.49 -0.54,0.27 -0.76,0.93 -0.49,1.47 l 1.46,2.93 z"
         id="path4527" /></a>
    	<a
       id="a32060"
       xlink:href="https://tm-dash.azurewebsites.net/child-poverty#povertydeprivation"
       target="blank"
       xlink:title="Child Poverty"><path
         class="st54"
         d="m 938.33,626.21 c 2.03,1.03 2.09,-4.37 2.09,-4.37 -0.47,0.28 -4.12,3.34 -2.09,4.37 m -0.2,2.59 c 1.91,0.97 4.45,-2.79 4.45,-3.36 0,0 -0.52,1.38 -2.77,1.27 -2.53,-0.13 -2.53,1.65 -1.68,2.09 m -1.4,2.74 c 1.91,0.98 4.45,-2.78 4.45,-3.36 0,0 -0.52,1.38 -2.77,1.27 -2.53,-0.12 -2.53,1.66 -1.68,2.09 m -1.45,2.84 c 1.91,0.97 4.45,-2.79 4.45,-3.36 0,0 -0.52,1.37 -2.77,1.27 -2.53,-0.13 -2.53,1.65 -1.68,2.09 m 1.51,-9.22 c -1.41,-1.76 -0.6,-2.98 -0.6,-2.98 -0.46,0.34 -2.02,4.6 -0.11,5.58 0.85,0.42 2.29,-0.62 0.71,-2.6 m -1.4,2.75 c -1.41,-1.76 -0.59,-2.99 -0.59,-2.99 -0.47,0.34 -2.02,4.6 -0.11,5.58 0.84,0.44 2.28,-0.61 0.7,-2.59 m -1.45,2.83 c -1.41,-1.76 -0.6,-2.98 -0.6,-2.98 -0.47,0.34 -2.02,4.6 -0.11,5.57 0.86,0.44 2.3,-0.61 0.71,-2.59 m -0.77,6.31 1.46,-2.35 c 0.12,-0.23 -0.29,-0.18 -0.66,-0.37 -0.37,-0.19 -0.56,-0.55 -0.68,-0.32 l -1.03,2.64 c -0.12,0.26 0.64,0.94 0.91,0.4 m 8.24,-5.4 c -0.23,0.36 -0.47,0.69 -0.71,1.02 1.28,0.54 2.08,1.22 2.08,1.97 0,1.73 -4.11,3.14 -9.17,3.14 -5.06,0 -9.17,-1.41 -9.17,-3.14 0,-1.49 3.02,-2.72 7.07,-3.05 0,-0.35 0.01,-0.7 0.04,-1.07 -5.16,0.24 -9.09,1.56 -9.09,5.63 0,4.57 4.95,9.57 11.04,9.57 6.1,0 11.04,-5 11.04,-9.57 0.01,-2.24 -1.2,-3.64 -3.13,-4.5 m -16.11,-6.14 v 2.15 c -0.22,-0.09 -0.42,-0.23 -0.6,-0.43 -0.18,-0.2 -0.3,-0.44 -0.36,-0.71 l -1.59,0.14 c 0.12,0.67 0.4,1.19 0.84,1.56 0.43,0.37 1,0.59 1.71,0.66 v 0.93 h 0.88 v -0.96 c 0.79,-0.1 1.41,-0.36 1.85,-0.78 0.45,-0.42 0.67,-0.95 0.67,-1.56 0,-0.55 -0.18,-1.01 -0.53,-1.36 -0.35,-0.36 -1.01,-0.64 -1.98,-0.87 v -2 c 0.39,0.14 0.63,0.42 0.73,0.82 l 1.54,-0.17 c -0.1,-0.51 -0.35,-0.92 -0.73,-1.23 -0.38,-0.31 -0.9,-0.49 -1.54,-0.55 v -0.51 h -0.88 v 0.51 c -0.7,0.06 -1.26,0.28 -1.67,0.66 -0.42,0.38 -0.63,0.85 -0.63,1.41 0,0.56 0.18,1.02 0.56,1.42 0.35,0.39 0.93,0.68 1.73,0.87 m -2.97,6.91 h -2.78 c -2.84,0 -3.46,-2.37 -3.46,-2.37 -1.87,-8.22 3.8,-12.68 3.8,-12.68 h 11.8 c 0,0 2.24,1.76 3.43,5.11 -0.79,0.91 -1.51,1.99 -2.12,3.22 -0.57,1.16 -0.97,2.33 -1.22,3.44 -2.87,0.1 -7.31,0.61 -9.45,3.28 m 7.68,-21.66 c -2.28,-0.25 -3.08,1.15 -4.22,1.21 -1.15,-0.06 -1.94,-1.46 -4.23,-1.21 -2.33,0.26 -3.75,2.25 -3.75,2.25 l 2.85,2.65 h 10.26 l 2.85,-2.65 c -0.01,0 -1.42,-1.99 -3.76,-2.25 m -5.5,12.64 c 0,0.18 0.07,0.35 0.19,0.5 0.13,0.16 0.33,0.28 0.59,0.38 v -1.77 c -0.24,0.07 -0.43,0.18 -0.57,0.35 -0.14,0.17 -0.21,0.34 -0.21,0.54 m 2.46,2.95 c 0.16,0.17 0.24,0.36 0.24,0.59 0,0.25 -0.09,0.48 -0.28,0.67 -0.19,0.19 -0.43,0.31 -0.74,0.35 v -2 c 0.35,0.09 0.62,0.22 0.78,0.39"
         id="path4529" /></a>
    	<a
       id="a15879"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#hs"
       target="blank"
       xlink:title="Health System"><path
         class="st54"
         d="m 459.13,544.52 c -0.98,-0.8 -1.66,-0.61 -2.64,1.14 -0.65,1.16 -1.68,1.3 -2.31,1.26 v -0.23 c 0.73,-0.36 1.25,-1.1 1.25,-1.97 0,-1.23 -0.99,-2.22 -2.22,-2.22 -1.23,0 -2.22,0.99 -2.22,2.22 0,0.87 0.52,1.61 1.25,1.97 v 0.23 c -0.63,0.04 -1.66,-0.1 -2.31,-1.26 -0.98,-1.75 -1.66,-1.94 -2.63,-1.14 -0.98,0.8 -4.86,5.43 -9.58,5.01 0,0 0.94,2.13 3.49,1.65 0,0 1.37,1.42 3.58,0.42 0,0 1.15,1.04 2.98,0.09 0,0 1.36,1.04 2.81,0.14 0,0 0.82,0.59 1.73,0.44 l 0.06,5.35 c -0.1,-0.02 -0.19,-0.04 -0.29,-0.06 0,0 -1.59,-0.34 -3.26,-0.81 -1.61,-0.42 -3.38,-1.11 -3.64,-1.46 0.02,-0.02 0.06,-0.04 0.11,-0.06 0.14,-0.07 0.39,-0.15 0.68,-0.21 0.59,-0.12 1.39,-0.18 2.2,-0.21 1.6,-0.06 1.89,0.01 1.92,0.02 0,-0.05 0.93,0.11 1.18,-0.83 -0.01,-0.01 0.02,-0.05 0,-0.07 -0.05,-0.65 -0.55,-0.68 -0.96,-0.76 -0.66,-0.09 -0.32,-0.05 -1.21,-0.04 -1.47,0.11 -5.98,-0.26 -6.55,2.12 0,0.07 -0.01,0.11 -0.01,0.17 0.19,2.07 4.47,2.97 7.58,3.59 -1.05,0.72 -1.62,1.66 -1.84,2.87 -0.11,1.29 0.92,2.53 3.31,3.9 -1.81,1.28 -3,2.49 -2.91,3.94 0.17,1.19 1.22,2.77 3.27,3.77 0.01,0 0.01,0 0.01,0 v 0 c 0,0 0,0 0.01,0 0,0 -1.44,-2.2 -1.54,-3.4 -0.1,-0.7 0.3,-1.74 2.06,-2.99 l 0.05,4.39 h 0.01 c 0.01,0.37 0.3,0.67 0.66,0.67 0.36,0 0.65,-0.3 0.66,-0.67 h 0.01 l 0.06,-4.28 c 1.61,1.2 1.98,2.19 1.89,2.87 -0.1,1.2 -1.53,3.4 -1.53,3.4 v 0 c 0,0 0.01,0 0.02,0 2.06,-1 3.11,-2.59 3.27,-3.77 0.1,-1.46 -1.09,-2.66 -2.9,-3.94 2.38,-1.38 3.41,-2.61 3.31,-3.9 -0.22,-1.21 -0.79,-2.15 -1.84,-2.87 3.11,-0.62 7.39,-1.52 7.58,-3.59 -0.01,-0.06 -0.01,-0.1 -0.01,-0.17 -0.57,-2.38 -5.08,-2.01 -6.55,-2.12 -0.89,-0.01 -0.55,-0.05 -1.21,0.04 -0.41,0.08 -0.91,0.11 -0.96,0.76 -0.02,0.02 0.01,0.06 0,0.07 0.25,0.94 1.18,0.78 1.18,0.83 0.03,-0.01 0.31,-0.08 1.92,-0.02 0.8,0.03 1.6,0.09 2.2,0.21 0.29,0.06 0.53,0.14 0.68,0.21 0.05,0.02 0.08,0.04 0.11,0.06 -0.26,0.36 -2.03,1.04 -3.64,1.46 -1.67,0.47 -3.26,0.81 -3.26,0.81 -0.04,0.01 -0.07,0.02 -0.11,0.02 l 0.07,-5.31 c 0.92,0.16 1.74,-0.44 1.74,-0.44 1.45,0.9 2.81,-0.14 2.81,-0.14 1.83,0.94 2.98,-0.09 2.98,-0.09 2.21,0.99 3.58,-0.42 3.58,-0.42 2.55,0.47 3.49,-1.65 3.49,-1.65 -4.77,0.43 -8.65,-4.2 -9.63,-5 z m -8.81,17.76 c 0.03,-0.47 -0.13,-1.58 2.08,-2.39 l 0.05,4.41 c -0.43,-0.27 -0.87,-0.55 -1.31,-0.83 -0.6,-0.36 -0.88,-0.85 -0.82,-1.19 z m 4.78,1.2 c -0.39,0.25 -0.77,0.48 -1.14,0.72 l 0.06,-4.24 c 2.01,0.8 1.86,1.87 1.89,2.32 0.06,0.34 -0.22,0.83 -0.81,1.2 z"
         id="path4531" /></a>
    	<path
       class="st54"
       d="m 510.37,488.07 c 0,2.94 -2.39,5.33 -5.33,5.33 -2.94,0 -5.33,-2.39 -5.33,-5.33 0,-2.94 2.39,-5.33 5.33,-5.33 2.95,0 5.33,2.38 5.33,5.33 z"
       id="path4533" />
    	<path
       class="st54"
       d="m 517.17,503.44 c 0,0 -2.03,-4.06 -3.35,-6.19 -1.32,-2.13 -3.15,-2.23 -3.15,-2.23 h -10.15 c -2.94,0.51 -4.87,3.65 -7.51,10.76 -2.64,7.1 5.48,9.74 9.23,9.95 3.75,0.2 5.08,-1.52 4.87,-3.25 -0.2,-1.73 -2.34,-1.73 -3.15,-1.62 -0.81,0.1 -4.36,-0.41 -5.68,-1.12 -1.32,-0.71 -0.91,-1.02 0.61,-1.02 1.52,0 2.44,-0.81 2.44,-0.81 0.81,-0.2 -0.51,-1.62 -0.71,-2.64 -0.2,-1.02 -0.41,-2.03 0.91,-2.33 1.32,-0.3 1.12,0.41 3.35,3.25 2.23,2.84 4.97,2.23 4.97,2.23 0,0 -2.84,1.62 -1.32,3.76 1.52,2.13 6.29,0 8.22,-3.45 1.94,-3.46 0.42,-5.29 0.42,-5.29 z m -7.96,4.16 c -1.99,0 -3.6,-1.61 -3.6,-3.6 0,-1.99 1.61,-3.6 3.6,-3.6 1.99,0 3.6,1.61 3.6,3.6 0,1.99 -1.62,3.6 -3.6,3.6 z"
       id="path4535" />
    	<path
       class="st54"
       d="m 584.81,449.61 h -13.75 c -0.38,0 -0.69,0.31 -0.69,0.69 v 3.44 c 0,0.38 0.31,0.69 0.69,0.69 h 13.75 c 0.38,0 0.69,-0.31 0.69,-0.69 v -3.44 c 0,-0.38 -0.31,-0.69 -0.69,-0.69 z"
       id="path4537" />
    	<path
       class="st54"
       d="m 571.75,475.05 c 0,0.38 0.31,0.69 0.69,0.69 h 11 c 0.38,0 0.69,-0.31 0.69,-0.69 V 455.8 h -12.38 v 19.25 z m 2.06,-15.13 c 0,-0.38 0.31,-0.69 0.69,-0.69 h 6.88 c 0.38,0 0.69,0.31 0.69,0.69 v 4.81 c 0,0.38 -0.31,0.69 -0.69,0.69 h -6.88 c -0.38,0 -0.69,-0.31 -0.69,-0.69 v -4.81 z m 0.69,7.56 h 6.88 c 0.38,0 0.69,0.31 0.69,0.69 0,0.38 -0.31,0.69 -0.69,0.69 h -6.88 c -0.38,0 -0.69,-0.31 -0.69,-0.69 0,-0.38 0.31,-0.69 0.69,-0.69 z"
       id="path4539" />
    	<path
       class="st54"
       d="m 565.91,448.23 h -3.78 v -3.44 h 1.72 c 0.57,0 1.03,-0.46 1.03,-1.03 0,-0.57 -0.46,-1.03 -1.03,-1.03 h -8.25 c -0.57,0 -1.03,0.46 -1.03,1.03 0,0.57 0.46,1.03 1.03,1.03 h 1.72 v 3.44 h -3.78 c -0.57,0 -1.03,0.46 -1.03,1.03 0,0.57 0.46,1.03 1.03,1.03 h 2.41 v 15.81 c 0,0.76 0.62,1.38 1.38,1.38 v 1.38 c 0,0.38 0.31,0.69 0.69,0.69 h 0.69 v 5.16 c 0,0.57 0.46,1.03 1.03,1.03 0.57,0 1.03,-0.46 1.03,-1.03 v -5.16 h 0.69 c 0.38,0 0.69,-0.31 0.69,-0.69 v -1.38 c 0.76,0 1.38,-0.62 1.38,-1.38 v -15.8 h 2.41 c 0.57,0 1.03,-0.46 1.03,-1.03 -0.03,-0.58 -0.49,-1.04 -1.06,-1.04 z m -4.47,12.38 H 558 v -8.94 h 3.44 v 8.94 z"
       id="path4541" />
    	<path
       class="st54"
       d="m 642.1,451.27 c 2.82,0 4.53,-1.85 4.65,-4.43 0.01,-0.12 -0.11,-0.22 -0.23,-0.22 h -15.56 -6.29 c -0.73,0 -1.16,0.49 -1.16,1.16 0,0.68 0.43,1.16 1.16,1.16 h 7.47 6.09 c 0.9,1.46 1.93,2.33 3.87,2.33"
       id="path4543" />
    	<a
       id="a12724"
       xlink:title="Nutrition"
       target="blank"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#nutrition"><path
         class="st54"
         d="m 650.85,439.27 c -0.76,0.74 -1.77,1.15 -2.84,1.15 -1.07,0 -2.08,-0.4 -2.84,-1.15 -0.35,-0.34 -0.35,-0.91 0,-1.25 0.36,-0.35 0.93,-0.35 1.29,0 0.83,0.81 2.27,0.81 3.1,0 0.36,-0.35 0.93,-0.35 1.29,0 0.35,0.35 0.35,0.91 0,1.25 m -10.85,0 c -0.76,0.74 -1.77,1.15 -2.84,1.15 -1.07,0 -2.08,-0.4 -2.84,-1.15 -0.35,-0.34 -0.35,-0.91 0,-1.25 0.36,-0.35 0.93,-0.35 1.29,0 0.83,0.81 2.27,0.81 3.1,0 0.36,-0.35 0.93,-0.35 1.29,0 0.34,0.35 0.34,0.91 0,1.25 m 15.63,-1.89 c -0.39,-0.39 -0.88,-0.69 -1.42,-0.83 V 435 c 0,-2.99 -1.3,-5.7 -3.41,-7.67 -2.08,-1.94 -4.94,-3.15 -8.11,-3.18 -0.54,0.39 -0.88,1.02 -0.88,1.73 0,1.15 1.09,2.15 2.33,2.15 0.43,0 0.77,0.35 0.77,0.78 0,0.43 -0.35,0.77 -0.77,0.77 -2.1,0 -3.88,-1.69 -3.88,-3.7 0,-0.56 0.12,-1.09 0.36,-1.57 -5.49,0.87 -9.66,5.33 -9.66,10.7 v 1.55 c -0.54,0.14 -1.03,0.44 -1.42,0.83 -0.56,0.58 -0.91,1.39 -0.91,2.27 0,0.88 0.35,1.68 0.91,2.27 0.39,0.39 0.88,0.69 1.42,0.83 v 1.55 c 0,0.25 0.02,0.5 0.06,0.77 H 647 c 0.49,0 0.96,0.2 1.3,0.56 0.33,0.34 0.5,0.81 0.48,1.28 -0.17,3.53 -2.66,5.91 -6.2,5.91 -2.42,0 -3.79,-1.13 -4.69,-2.33 h -4.13 c 2.12,2.54 5.29,4.65 8.82,4.65 6.42,0 11.62,-6.92 11.62,-10.85 v -1.55 c 0.54,-0.14 1.03,-0.44 1.42,-0.83 0.56,-0.59 0.91,-1.39 0.91,-2.27 0,-0.88 -0.34,-1.69 -0.9,-2.27"
         id="path4545" /></a>
    	<path
       class="st54"
       d="m 731.44,425.6 v -0.04 c -3.74,-3.76 -9.83,-3.78 -13.59,-0.03 -0.01,0.01 -0.02,0.02 -0.03,0.03 l -1.43,1.42 -1.42,-1.42 c -3.77,-3.77 -9.88,-3.76 -13.65,0.02 -3.76,3.77 -3.76,9.88 0.02,13.65 l 14.19,14.14 c 0.46,0.48 1.22,0.49 1.7,0.03 0.01,-0.01 0.02,-0.02 0.03,-0.03 l 14.19,-14.14 c 3.75,-3.77 3.75,-9.86 -0.01,-13.63 z m -11.38,13.86 h -2.45 v 2.45 c 0,0.67 -0.55,1.22 -1.22,1.22 -0.67,0 -1.22,-0.55 -1.22,-1.22 v -2.45 h -2.45 c -0.67,0 -1.22,-0.55 -1.22,-1.22 0,-0.67 0.55,-1.22 1.22,-1.22 h 2.45 v -2.45 c 0,-0.67 0.55,-1.22 1.22,-1.22 0.67,0 1.22,0.55 1.22,1.22 v 2.45 h 2.45 c 0.67,0 1.22,0.55 1.22,1.22 0,0.67 -0.54,1.21 -1.22,1.22 z"
       id="path4547" />
    	<path
       class="st54"
       d="m 732.04,955.28 -16.04,-7.97 -16.04,7.97 -1.46,-2.93 17.48,-8.69 0.01,-0.02 0.02,0.01 0.02,-0.01 0.01,0.02 17.48,8.69 -1.48,2.93 z m -0.87,3.25 c 0,0.06 0,1.04 0,2.54 v 16.94 H 718.6 c -0.43,0.36 -1.45,0.62 -2.64,0.62 -1.19,0 -2.21,-0.26 -2.64,-0.62 h -12.49 v -16.94 c 0,-1.5 0,-2.49 0,-2.54 8.24,-3.55 14.27,-0.06 15.32,0.94 0.8,-0.73 7.11,-4.42 15.02,-0.94 z m -16.14,4.09 c 0,-2.52 -3.35,-3.88 -7.5,-3.88 -1.99,0 -3.8,0.47 -5.14,1.24 v 16.52 c 6.77,-4.26 12.63,-0.36 12.63,0.31 v -14.19 h 0.01 z m 14.67,-2.65 c -1.34,-0.77 -3.14,-1.24 -5.13,-1.24 -4.14,0 -7.49,1.36 -7.49,3.88 v 14.18 c 0,-0.67 5.86,-4.57 12.63,-0.31 v -16.51 z"
       id="path4549" />
    	<path
       class="st54"
       d="m 424.77,700.99 v 0.02 c -0.12,-0.01 -0.24,-0.02 -0.37,-0.02 -0.08,0 -0.16,0.01 -0.24,0.01 -0.04,0 -0.08,-0.01 -0.12,-0.01 h -9.15 c -1.42,0 -2.56,1.15 -2.56,2.56 0,1.41 1.15,2.56 2.56,2.56 h 2.81 1.21 c 0.81,0 1.46,0.65 1.46,1.46 0,0.81 -0.65,1.46 -1.46,1.46 h -1.37 -3.75 -1.46 c -0.39,0 -0.9,-0.17 -1.17,-0.44 l -9.94,-9.68 c -1.21,-1.21 -3.22,-1.14 -4.34,0.21 -0.97,1.18 -0.8,2.94 0.28,4.02 l 11.14,10.88 c 0.55,0.55 1.3,0.86 2.07,0.86 h 13.66 c 0.06,0 0.11,-0.01 0.17,-0.02 0.07,0 0.13,0.01 0.2,0.01 0.12,0 0.25,-0.01 0.37,-0.02 v 0.03 c 3.64,0 6.58,-2.95 6.58,-6.59 v -0.73 c 0.01,-3.62 -2.94,-6.57 -6.58,-6.57 z"
       id="path4551" />
    	<path
       class="st54"
       d="m 400.99,694.4 c 0.02,0 0.03,0 0.05,0 0.01,0 0.02,0 0.02,0 h 6.52 c 1.01,0 1.83,-0.82 1.83,-1.83 0,-1.01 -0.82,-1.83 -1.83,-1.83 h -1.97 v -0.01 h -0.96 c -0.61,0 -1.1,-0.49 -1.1,-1.1 0,-0.61 0.49,-1.1 1.1,-1.1 h 0.96 1.78 1.93 c 0.27,0 0.63,0.12 0.82,0.31 l 6.78,7.15 c 0.84,0.84 2.24,0.79 3.02,-0.15 0.68,-0.82 0.55,-2.04 -0.2,-2.8 l -7.75,-7.56 c -0.38,-0.38 -0.9,-0.6 -1.44,-0.6 h -9.5 c -0.02,0 -0.03,0.01 -0.05,0.01 v 0 c -2.63,0 -4.75,2.13 -4.75,4.75 -0.02,2.63 2.11,4.76 4.74,4.76 z"
       id="path4553" />
    	<path
       class="st54"
       d="m 890.05,844.29 c 0.2,-1.16 0.62,-2.26 1.19,-3.25 0.3,-0.54 0.68,-1.06 1.08,-1.53 0.14,-0.17 0.29,-0.34 0.45,-0.49 -1.32,-0.86 -2.89,-1.35 -4.57,-1.35 -4.65,0 -8.43,3.78 -8.43,8.44 0,3.11 1.7,5.84 4.21,7.29 v 1.15 c 0,0.93 0.76,1.69 1.69,1.69 h 5.06 c 0.94,0 1.69,-0.76 1.69,-1.69 v -1.14 -0.62 c -0.46,-0.51 -0.84,-1.05 -1.17,-1.62 -1.19,-2.02 -1.64,-4.44 -1.2,-6.88 z m -7.77,1.82 c 0,-1.62 0.65,-3.08 1.7,-4.15 v 8.3 c -1.05,-1.07 -1.7,-2.53 -1.7,-4.15 z"
       id="path4555" />
    	<path
       class="st54"
       d="m 888.2,835.98 c 1.86,0 3.38,-1.51 3.38,-3.38 0,-1.87 -1.51,-3.38 -3.38,-3.38 -1.86,0 -3.38,1.51 -3.38,3.38 0,1.87 1.52,3.38 3.38,3.38 z"
       id="path4557" />
    	<path
       class="st54"
       d="m 911.82,835.98 c 1.86,0 3.38,-1.51 3.38,-3.38 0,-1.87 -1.51,-3.38 -3.38,-3.38 -1.87,0 -3.38,1.51 -3.38,3.38 0,1.87 1.52,3.38 3.38,3.38 z"
       id="path4559" />
    	<path
       class="st54"
       d="m 911.82,837.67 c -1.7,0 -3.27,0.5 -4.59,1.36 0.16,0.16 0.32,0.34 0.46,0.51 0.4,0.46 0.76,0.97 1.07,1.5 0.86,1.49 1.36,3.22 1.36,5.06 0,1.8 -0.49,3.53 -1.36,5.05 -0.34,0.57 -0.73,1.11 -1.16,1.61 v 0.63 1.14 c 0,0.93 0.76,1.69 1.69,1.69 h 5.06 c 0.93,0 1.69,-0.76 1.69,-1.69 v -1.15 c 2.51,-1.45 4.21,-4.18 4.21,-7.29 0,-4.64 -3.78,-8.42 -8.43,-8.42 z m 4.22,12.59 v -8.3 c 1.05,1.07 1.7,2.53 1.7,4.15 0,1.62 -0.65,3.08 -1.7,4.15 z"
       id="path4561" />
    	<path
       class="st54"
       d="m 900.01,835.98 c 1.86,0 3.38,-1.51 3.38,-3.38 0,-1.87 -1.51,-3.38 -3.38,-3.38 -1.86,0 -3.38,1.51 -3.38,3.38 0.01,1.87 1.52,3.38 3.38,3.38 z"
       id="path4563" />
    	<path
       class="st54"
       d="m 908.44,846.11 c 0,-1.31 -0.3,-2.55 -0.84,-3.65 -0.05,-0.11 -0.1,-0.21 -0.16,-0.32 -0.4,-0.75 -0.92,-1.44 -1.53,-2.04 -1.52,-1.49 -3.6,-2.42 -5.91,-2.42 -0.52,0 -1.05,0.05 -1.59,0.14 -1.65,0.3 -3.16,1.11 -4.32,2.27 -0.61,0.59 -1.13,1.28 -1.53,2.04 -0.06,0.1 -0.11,0.2 -0.15,0.3 -0.34,0.68 -0.57,1.4 -0.71,2.15 -0.33,1.87 -0.03,3.66 0.71,5.19 0.05,0.1 0.1,0.21 0.16,0.31 0.4,0.75 0.92,1.43 1.53,2.03 0.51,0.49 1.07,0.93 1.69,1.28 v 0.39 c 0,0.03 0.01,0.05 0.01,0.08 0,0.02 -0.01,0.04 -0.01,0.07 v 0.62 c 0,0.93 0.76,1.69 1.69,1.69 h 5.06 c 0.93,0 1.69,-0.76 1.69,-1.69 v -0.62 c 0,-0.02 -0.01,-0.04 -0.01,-0.07 0,-0.03 0.01,-0.05 0.01,-0.08 v -0.39 c 0.62,-0.35 1.18,-0.78 1.69,-1.28 0.61,-0.6 1.12,-1.28 1.53,-2.04 0.06,-0.1 0.11,-0.21 0.16,-0.32 0.53,-1.1 0.83,-2.34 0.83,-3.64 z m -12.65,4.14 c -0.05,-0.05 -0.11,-0.11 -0.15,-0.17 -0.9,-0.98 -1.48,-2.26 -1.54,-3.67 0.02,-0.1 0.02,-0.2 0.02,-0.3 0,-0.1 0,-0.2 -0.02,-0.3 0.06,-1.42 0.63,-2.69 1.54,-3.68 0.04,-0.06 0.1,-0.11 0.15,-0.17 v 0.48 7.34 0.47 z m 8.59,-0.18 c -0.04,0.06 -0.09,0.12 -0.15,0.18 v -0.47 -7.34 -0.47 c 0.05,0.05 0.11,0.11 0.15,0.17 0.91,0.99 1.49,2.3 1.53,3.75 -0.01,0.08 -0.01,0.15 -0.01,0.23 0,0.08 0,0.15 0.01,0.23 -0.04,1.42 -0.62,2.73 -1.53,3.72 z"
       id="path4565" />
    	<path
       class="st54"
       d="m 870.71,909.79 h -1.86 -2.83 -8.4 c 0,0.45 -0.18,0.86 -0.48,1.15 -0.29,0.3 -0.7,0.48 -1.15,0.48 h -8.18 c -0.9,0 -1.64,-0.74 -1.64,-1.64 h -8.18 -3.27 -1.64 c -0.45,0 -0.82,0.37 -0.82,0.82 v 3.27 c 0,0.45 0.37,0.82 0.82,0.82 h 37.64 c 0.45,0 0.82,-0.37 0.82,-0.82 v -3.27 c -0.02,-0.44 -0.38,-0.81 -0.83,-0.81 z"
       id="path4567" />
    	<path
       class="st54"
       d="m 837.98,907.34 h 0.82 v -15.55 h 26.18 v 15.55 h 0.82 3.27 v -18 c 0,-0.22 -0.05,-0.44 -0.13,-0.64 -0.16,-0.39 -0.48,-0.71 -0.87,-0.87 -0.19,-0.08 -0.41,-0.13 -0.64,-0.13 h -31.09 c -0.9,0 -1.64,0.73 -1.64,1.64 v 0.82 17.18 h 2.45 0.83 z"
       id="path4569" />
    	<a
       id="a38500"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection#justice"
       target="blank"
       xlink:title="Justics for Children"><path
         class="st54"
         d="m 434.35,790.32 h -8.02 v -26.98 h 7.53 l -3.81,8.71 c -0.28,0.72 0.25,1.49 1.02,1.49 0.45,0 0.85,-0.27 1.01,-0.69 l 3.36,-8.06 3.36,8.06 c 0.16,0.42 0.57,0.69 1.02,0.69 0.77,0 1.3,-0.78 1.02,-1.49 l -4.36,-10.21 c -0.16,-0.42 -0.56,-0.69 -1.01,-0.69 h -9.14 v -1.46 c 0,-0.81 -0.63,-1.46 -1.44,-1.46 -0.81,0 -1.48,0.65 -1.48,1.46 v 1.46 h -9.09 c -0.45,0 -0.85,0.28 -1.01,0.69 l -4.4,10.21 c -0.28,0.72 0.24,1.49 1.02,1.49 0.45,0 0.85,-0.27 1.02,-0.69 l 3.36,-8.06 3.36,8.06 c 0.17,0.42 0.57,0.69 1.02,0.69 0.77,0 1.3,-0.78 1.01,-1.49 l -3.77,-8.71 h 7.49 v 26.98 h -8.02 c -0.81,0 -1.46,0.65 -1.46,1.46 0,0.81 0.65,1.46 1.46,1.46 h 18.96 c 0.8,0 1.46,-0.65 1.46,-1.46 -0.01,-0.81 -0.67,-1.46 -1.47,-1.46 z"
         id="path4571" /></a>
    	<path
       class="st54"
       d="m 421.22,775.96 c 0.03,-0.12 -0.06,-0.23 -0.18,-0.23 h -13.48 c -0.12,0 -0.21,0.11 -0.18,0.23 0.74,3.11 3.54,5.61 6.88,5.61 3.32,0 6.22,-2.5 6.96,-5.61 z"
       id="path4573" />
    	<path
       class="st54"
       d="m 442.36,775.96 c 0.03,-0.12 -0.06,-0.23 -0.18,-0.23 H 428.7 c -0.12,0 -0.21,0.11 -0.18,0.23 0.74,3.11 3.54,5.61 6.88,5.61 3.33,0 6.22,-2.5 6.96,-5.61 z"
       id="path4575" />
    	<path
       class="st54"
       d="m 463.01,831.53 c -5.4,0 -9.48,3.76 -9.48,8.75 0,0.8 0.65,1.46 1.46,1.46 0.8,0 1.46,-0.65 1.46,-1.46 0,-2.2 1.23,-4.03 3.15,-5.03 l -2.41,13.66 c -0.07,0.44 0.27,0.85 0.72,0.85 h 1.46 v 8.02 c 0,0.81 0.65,1.46 1.46,1.46 0.8,0 1.46,-0.65 1.46,-1.46 v -8.02 h 1.46 v 8.02 c 0,0.81 0.65,1.46 1.46,1.46 0.8,0 1.46,-0.65 1.46,-1.46 v -8.02 h 1.46 c 0.45,0 0.79,-0.41 0.72,-0.85 l -2.34,-13.62 c 1.87,1 3.08,2.82 3.08,4.99 0,0.8 0.65,1.46 1.46,1.46 0.81,0 1.46,-0.65 1.46,-1.46 -0.02,-4.99 -4.1,-8.75 -9.5,-8.75 z"
       id="path4577" />
    	<path
       class="st54"
       d="m 463.01,830.07 c 1.61,0 2.92,-1.31 2.92,-2.92 0,-1.61 -1.31,-2.92 -2.92,-2.92 -1.61,0 -2.92,1.31 -2.92,2.92 0,1.61 1.31,2.92 2.92,2.92 z"
       id="path4579" />
    	<path
       class="st54"
       d="m 446.6,854.13 c -0.6,0 -1.09,0.49 -1.09,1.09 v 2.92 c 0,0.6 0.49,1.09 1.09,1.09 0.6,0 1.09,-0.49 1.09,-1.09 v -2.92 c 0,-0.6 -0.49,-1.09 -1.09,-1.09 z"
       id="path4581" />
    	<path
       class="st54"
       d="m 454.62,849.03 h -2.92 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 2.92 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.49,-1.09 -1.09,-1.09 z"
       id="path4583" />
    	<path
       class="st54"
       d="m 446.6,841 c -0.6,0 -1.09,0.49 -1.09,1.09 V 845 c 0,0.6 0.49,1.09 1.09,1.09 0.6,0 1.09,-0.49 1.09,-1.09 v -2.91 c 0.01,-0.6 -0.48,-1.09 -1.09,-1.09 z"
       id="path4585" />
    	<path
       class="st54"
       d="m 442.59,850.12 c 0,-0.6 -0.49,-1.09 -1.09,-1.09 h -2.92 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 2.92 c 0.6,0 1.09,-0.49 1.09,-1.09 z"
       id="path4587" />
    	<path
       class="st54"
       d="m 451.02,852.99 c -0.43,-0.43 -1.12,-0.43 -1.55,0 -0.43,0.43 -0.43,1.12 0,1.55 l 2.19,2.19 c 0.43,0.43 1.12,0.43 1.55,0 0.43,-0.43 0.43,-1.12 0,-1.55 l -2.19,-2.19 z"
       id="path4589" />
    	<path
       class="st54"
       d="m 451.02,847.25 2.19,-2.19 c 0.43,-0.43 0.43,-1.12 0,-1.55 -0.43,-0.43 -1.12,-0.43 -1.55,0 l -2.19,2.19 c -0.43,0.43 -0.43,1.12 0,1.55 0.43,0.42 1.12,0.42 1.55,0 z"
       id="path4591" />
    	<path
       class="st54"
       d="m 442.18,847.25 c 0.43,0.43 1.12,0.43 1.55,0 0.43,-0.43 0.43,-1.12 0,-1.55 l -2.19,-2.19 c -0.43,-0.43 -1.12,-0.43 -1.55,0 -0.43,0.43 -0.43,1.12 0,1.55 l 2.19,2.19 z"
       id="path4593" />
    	<path
       class="st54"
       d="m 442.18,852.99 -2.19,2.19 c -0.43,0.43 -0.43,1.12 0,1.55 0.43,0.43 1.12,0.43 1.55,0 l 2.19,-2.19 c 0.43,-0.43 0.43,-1.12 0,-1.55 -0.43,-0.43 -1.12,-0.43 -1.55,0 z"
       id="path4595" />
    	<path
       class="st54"
       d="m 491.54,889.22 c 1.61,0 2.92,-1.31 2.92,-2.92 0,-1.61 -1.31,-2.92 -2.92,-2.92 -1.61,0 -2.92,1.31 -2.92,2.92 0,1.62 1.31,2.92 2.92,2.92 z"
       id="path4597" />
    	<path
       class="st54"
       d="m 516.88,904.14 2.86,-5.65 c 0.88,-1.74 0.17,-3.87 -1.57,-4.75 l -0.92,-0.46 -0.95,-0.48 c -0.09,-0.04 -0.18,-0.08 -0.28,-0.1 -0.85,-0.39 -1.74,-0.65 -2.63,-0.79 -3.62,-0.59 -7.33,0.74 -9.64,3.62 l -1.55,-1.79 c -2.19,-2.4 -5.32,-3.78 -8.57,-3.78 -1.55,0 -3.05,0.74 -3.98,1.99 -1,1.33 -1.27,3.07 -0.71,4.65 0.01,0.04 0.03,0.07 0.04,0.1 l 2.1,4.81 c 0.15,0.56 0.53,1.76 1.11,3.58 1.04,3.28 1.75,6.67 2.09,10.08 l 0.19,1.92 c 0.07,0.75 0.71,1.31 1.45,1.31 0.04,0 0.09,0 0.15,-0.01 0.8,-0.08 1.38,-0.79 1.3,-1.6 l -0.19,-1.91 c -0.33,-3.24 -0.96,-6.47 -1.89,-9.61 h 2.9 c 0.83,2.22 1.37,4.6 1.37,8.75 0,0.68 0.47,1.25 1.09,1.41 l 1.77,-3.47 c -0.24,-4.94 -1.36,-7.52 -2.64,-10.44 -0.29,-0.67 -0.6,-1.36 -0.9,-2.12 l -2.46,-6.06 c 1.37,0.47 2.62,1.26 3.6,2.33 l 2.81,3.27 c 0.26,0.3 0.61,0.47 0.98,0.5 0.07,0 0.12,0.01 0.17,0.01 0.55,0 1.08,-0.3 1.35,-0.82 1.18,-2.3 3.43,-3.64 5.84,-3.81 0.28,-0.02 0.55,-0.03 0.82,-0.01 0.26,0.01 0.52,0.04 0.78,0.07 l -10.86,21.31 c -0.39,0.75 -0.09,1.67 0.66,2.05 0.22,0.12 0.46,0.17 0.69,0.17 0.55,0 1.09,-0.31 1.36,-0.83 l 6.59,-12.93 0.65,0.33 0.66,0.33 2.38,1.21 c 0.01,0.01 0.02,0.01 0.03,0.02 0.02,0.01 0.03,0.02 0.05,0.03 l 0.04,0.02 c 3.15,2.04 4.3,6.2 2.53,9.6 -0.39,0.75 -0.1,1.66 0.65,2.05 0.37,0.19 0.79,0.22 1.16,0.1 0.37,-0.12 0.7,-0.38 0.89,-0.75 2.47,-4.76 0.93,-10.52 -3.37,-13.45 z"
       id="path4599" />
    	<path
       class="st54"
       d="m 523.47,889.04 c -0.5,-1.53 -2.15,-2.36 -3.68,-1.86 -1.53,0.5 -2.36,2.15 -1.86,3.68 0.5,1.53 2.15,2.36 3.68,1.86 1.54,-0.5 2.37,-2.15 1.86,-3.68 z"
       id="path4601" />
    	<path
       class="st54"
       d="m 583.63,954.06 h -32.81 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 32.81 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.48,-1.09 -1.09,-1.09 z"
       id="path4603" />
    	<a
       id="a22269"
       xlink:href="https://tm-dash.azurewebsites.net/child-education#system"
       target="blank"
       xlink:title="Education System"><path
         class="st54"
         d="m 564.31,945.31 c 0,-0.8 0.66,-1.46 1.46,-1.46 h 2.92 c 0.8,0 1.46,0.66 1.46,1.46 v 7.29 h 11.67 v -18.23 c 0,-0.4 -0.33,-0.73 -0.73,-0.73 h -7.29 l -5.1,-3.83 v -2.73 h 6.56 v -4.38 h -6.56 c 0,-0.81 -0.65,-1.46 -1.46,-1.46 -0.8,0 -1.46,0.65 -1.46,1.46 v 7.11 l -5.1,3.83 h -7.29 c -0.4,0 -0.73,0.33 -0.73,0.73 v 18.23 h 11.67 v -7.29 z m 10.94,-8.02 c 0,-0.4 0.33,-0.73 0.73,-0.73 h 1.46 c 0.4,0 0.73,0.33 0.73,0.73 v 3.65 c 0,0.4 -0.33,0.73 -0.73,0.73 h -1.46 c -0.4,0 -0.73,-0.33 -0.73,-0.73 v -3.65 z m 0,8.02 c 0,-0.4 0.33,-0.73 0.73,-0.73 h 1.46 c 0.4,0 0.73,0.33 0.73,0.73 v 3.65 c 0,0.4 -0.33,0.73 -0.73,0.73 h -1.46 c -0.4,0 -0.73,-0.33 -0.73,-0.73 v -3.65 z m -16.04,3.65 c 0,0.4 -0.33,0.73 -0.73,0.73 h -1.46 c -0.4,0 -0.73,-0.33 -0.73,-0.73 v -3.65 c 0,-0.4 0.33,-0.73 0.73,-0.73 h 1.46 c 0.4,0 0.73,0.33 0.73,0.73 v 3.65 z m 0,-8.02 c 0,0.4 -0.33,0.73 -0.73,0.73 h -1.46 c -0.4,0 -0.73,-0.33 -0.73,-0.73 v -3.65 c 0,-0.4 0.33,-0.73 0.73,-0.73 h 1.46 c 0.4,0 0.73,0.33 0.73,0.73 v 3.65 z m 10.93,-4.37 c 0,1.61 -1.3,2.92 -2.92,2.92 -1.61,0 -2.92,-1.31 -2.92,-2.92 0,-1.61 1.31,-2.92 2.92,-2.92 1.62,0 2.92,1.3 2.92,2.92 z"
         id="path4605" /></a>
    	<path
       class="st54"
       d="m 902.46,562.01 5.23,-5.18 c 0.56,-0.57 1.47,-0.57 2.03,0 0.56,0.57 0.56,1.49 0,2.06 l -2.61,2.51 c -0.33,0.33 -0.33,0.87 0,1.2 0.33,0.33 0.86,0.33 1.18,0 l 3.23,-3.45 v -11 c 0,-1.14 0.94,-2.06 2.06,-2.06 1.12,0 2.06,0.92 2.06,2.06 v 11.96 c 0,0.55 -0.21,1.07 -0.59,1.46 l -7.66,7.89 v 6.19 h -6.19 v -10.31 c 0.01,-1.37 0.36,-2.41 1.26,-3.33 z"
       id="path4607" />
    	<path
       class="st54"
       d="m 895.82,562.01 -5.23,-5.18 c -0.56,-0.57 -1.47,-0.57 -2.03,0 -0.56,0.57 -0.56,1.49 0,2.06 l 2.61,2.51 c 0.33,0.33 0.33,0.87 0,1.2 -0.33,0.33 -0.85,0.33 -1.18,0 l -3.23,-3.45 v -11 c 0,-1.14 -0.94,-2.06 -2.06,-2.06 -1.12,0 -2.06,0.92 -2.06,2.06 v 11.96 c 0,0.55 0.21,1.07 0.6,1.46 l 7.65,7.89 v 6.19 h 6.19 v -10.31 c 0,-1.37 -0.36,-2.41 -1.26,-3.33 z"
       id="path4609" />
    	<path
       class="st54"
       d="m 905.33,548.85 c 0,-3.42 -2.77,-6.19 -6.19,-6.19 -3.42,0 -6.19,2.77 -6.19,6.19 0,3.42 2.77,6.19 6.19,6.19 3.42,-0.01 6.19,-2.78 6.19,-6.19 z"
       id="path4611" />
    	<path
       class="st54"
       d="m 939.72,707.87 h -1.46 c -0.4,0 -0.73,0.33 -0.73,0.73 v 0.73 c 0,0.4 0.33,0.73 0.73,0.73 h 1.46 c 0.4,0 0.73,-0.33 0.73,-0.73 v -0.73 c 0,-0.4 -0.33,-0.73 -0.73,-0.73 z"
       id="path4613" />
    	<path
       class="st54"
       d="m 939.72,702.04 h -1.46 c -0.4,0 -0.73,0.33 -0.73,0.73 v 0.73 c 0,0.4 0.33,0.73 0.73,0.73 h 1.46 c 0.4,0 0.73,-0.33 0.73,-0.73 v -0.73 c 0,-0.41 -0.33,-0.73 -0.73,-0.73 z"
       id="path4615" />
    	<path
       class="st54"
       d="m 944.1,694.02 c 0.81,0 1.46,-0.65 1.46,-1.46 0,-0.81 -0.65,-1.46 -1.46,-1.46 -0.8,0 -1.46,0.65 -1.46,1.46 0,0.8 0.65,1.46 1.46,1.46 z"
       id="path4617" />
    	<path
       class="st54"
       d="m 949.57,707.87 h -5.83 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 5.83 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.49,-1.09 -1.09,-1.09 z"
       id="path4619" />
    	<path
       class="st54"
       d="m 947.01,697.96 c 0,-1.37 -1.11,-2.49 -2.49,-2.49 h -0.86 c -1.37,0 -2.49,1.11 -2.49,2.49 v 1.16 H 947 l 0.01,-1.16 z"
       id="path4621" />
    	<a
       id="a23932"
       xlink:href="https://tm-dash.azurewebsites.net/child-participation#registration"
       target="blank"
       xlink:title="Birth Registration"><path
         class="st54"
         d="m 954.3,685.27 h -3.65 c 0,-0.8 -0.66,-1.46 -1.46,-1.46 H 947 c 0,-0.8 -0.33,-1.53 -0.85,-2.06 -0.53,-0.52 -1.26,-0.85 -2.06,-0.85 -1.61,0 -2.92,1.3 -2.92,2.92 h -2.19 c -0.8,0 -1.46,0.66 -1.46,1.46 h -3.64 c -0.8,0 -1.46,0.71 -1.46,1.57 v 27.49 c 0,0.86 0.66,1.57 1.46,1.57 h 20.42 c 0.8,0 1.46,-0.71 1.46,-1.57 v -27.49 c 0,-0.88 -0.65,-1.58 -1.46,-1.58 z m -10.2,-1.46 c 0.4,0 0.73,0.33 0.73,0.73 0,0.4 -0.33,0.73 -0.73,0.73 -0.4,0 -0.73,-0.33 -0.73,-0.73 0,-0.41 0.32,-0.73 0.73,-0.73 z m 8.75,29.16 h -17.5 v -24.79 h 2.19 c 0,0.8 0.66,1.46 1.46,1.46 h 10.21 c 0.8,0 1.46,-0.66 1.46,-1.46 h 2.19 v 24.79 z"
         id="path4623" /></a>
    	<path
       class="st54"
       d="m 949.57,702.04 h -5.83 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 5.83 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.49,-1.09 -1.09,-1.09 z"
       id="path4625" />
    	<path
       class="st54"
       d="m 852.2,482.89 c -0.16,-0.2 -0.47,-0.2 -0.63,0 -1.93,2.48 -12.08,15.83 -12.08,22.17 0,7 5.55,12.68 12.4,12.68 6.85,0 12.4,-5.68 12.4,-12.68 -0.01,-6.34 -10.16,-19.69 -12.09,-22.17 z m 2.97,29.75 c -0.6,0 -1.09,-0.49 -1.09,-1.09 0,-0.6 0.49,-1.09 1.09,-1.09 1.81,0 3.28,-1.8 3.28,-4.01 0,-0.6 0.49,-1.09 1.09,-1.09 0.6,0 1.09,0.49 1.09,1.09 0.01,3.41 -2.44,6.19 -5.46,6.19 z"
       id="path4627" />
    	<a
       id="a35288"
       xlink:href="https://tm-dash.azurewebsites.net/child-health#hivaids"
       target="blank"
       xlink:title="HIV/AIDS"><path
         class="st54"
         d="m 806.47,467.85 -18.89,-9.48 c 0,0 0,-0.04 0.01,-0.1 0.02,-0.11 0.02,-0.21 0.02,-0.26 L 787.6,458 c 0.04,-1.42 -0.03,-6.67 -2.92,-9.86 0.12,0.13 0.25,0.25 0.36,0.4 0,0 -3.53,-5.18 -6.95,-5.36 -1.66,-0.09 -2.89,1.19 -3.28,1.69 -0.39,0.5 -2.07,3.32 -1.96,7.4 0,0 -0.02,-1.57 0.84,-3.22 -1.49,3.12 -0.65,5.49 0.23,7.02 0.19,1.6 1.07,2.74 1.48,3.35 0.78,1.18 2.85,2.87 3.56,3.33 -0.36,1.48 -1,4.18 -1.26,5.95 -0.29,2.04 -0.51,7.79 -0.51,7.79 l 6.66,1.69 c 0,0 0.22,-0.28 0.25,-0.67 0.02,-0.21 0.8,-7.98 1.38,-11.01 3.43,1.77 11.9,6.14 11.9,6.14 l 0.56,-0.91 c 2.64,1.36 4.67,2.41 4.67,2.41 l 3.86,-6.29 z m -21.9,-19.83 c -0.06,-0.06 -0.12,-0.12 -0.18,-0.18 0.06,0.06 0.12,0.12 0.18,0.18 z m -8.67,-1.43 c 1.66,-1.09 4.58,-0.67 5.06,-0.59 0.2,0.04 0.71,0.18 1.33,0.46 0.83,1.7 0.77,5.88 -0.85,8.9 0,0 -6.78,-3.11 -7.68,-6.43 0.44,-0.83 1.12,-1.68 2.14,-2.34 z"
         id="path4629" /></a>
    	<path
       class="st54"
       d="m 636.54,965.41 -1.5,2.76 c -0.07,0.16 -0.28,0.43 -0.79,0.43 -0.62,0 -1.67,-0.39 -2.35,-0.68 l -0.13,0.29 -1.02,-0.47 0.13,-0.28 c -0.9,-0.45 -2.01,-1.1 -2.22,-1.66 l -0.08,-0.31 0.08,-0.22 1.15,-2.96 c -1.18,0.75 -2.2,2.38 -3.49,4.99 l -1.46,3.07 c -0.12,0.27 -0.25,0.54 -0.38,0.83 l 8.72,4.03 c 0.13,-0.28 0.26,-0.56 0.38,-0.83 l 1.4,-3.09 c 1.18,-2.69 1.76,-4.52 1.56,-5.9 z m -2.8,6.73 -1.08,2.35 -7.26,-3.36 1.09,-2.35 c 0.31,-0.66 1.11,-1 2.12,-1 0.75,0 1.62,0.19 2.48,0.59 2,0.93 3.2,2.61 2.65,3.77 z m -0.57,-1.05 c 0.11,0.31 0.11,0.57 0.01,0.79 l -0.83,1.79 -6.14,-2.84 0.83,-1.79 c 0.19,-0.4 0.77,-0.65 1.55,-0.65 0.69,0 1.48,0.19 2.22,0.54 1.17,0.54 2.07,1.36 2.36,2.16 z m 1.65,-8.58 c 0.21,0.09 0.44,0.15 0.67,0.17 0.04,0.22 0.05,0.45 0.03,0.68 0.64,0.4 1.03,0.73 0.96,0.87 l -2,3.69 c -0.11,0.24 -1.37,-0.1 -2.82,-0.77 -1.44,-0.67 -2.52,-1.41 -2.41,-1.66 l 1.51,-3.91 c 0.07,-0.14 0.57,-0.06 1.28,0.17 0.44,-0.45 1.03,-0.7 1.6,-0.7 0.04,0.2 0.1,0.41 0.23,0.63 -0.39,-0.07 -0.8,0.05 -1.15,0.31 0.35,0.14 0.72,0.29 1.11,0.47 0.39,0.18 0.75,0.36 1.07,0.54 -0.01,-0.17 -0.02,-0.33 -0.08,-0.49 0.01,0 0.01,0 0,0 z m 14.91,0.63 c -0.09,0.47 0.02,1.36 0.22,1.8 l 5.13,11.13 c 0.26,0.56 0.56,1.21 0.11,1.91 -0.26,0.41 -0.72,0.66 -1.21,0.66 v 0 c -0.86,0 -1.25,-0.65 -1.56,-1.17 l -6.33,-10.65 -1.72,3.49 c -0.4,0.82 -1.2,1.97 -1.81,2.63 l -3.46,3.73 c -0.45,0.48 -0.8,0.86 -1.46,0.86 -0.55,0 -1.05,-0.32 -1.29,-0.82 -0.4,-0.84 0.09,-1.45 0.52,-1.98 l 3.41,-4.22 c 0.36,-0.45 0.85,-1.38 1.01,-1.94 l 1.27,-4.42 c 0.18,-0.65 0.4,-1.8 0.45,-2.47 l 0.56,-6.8 c -2.76,0.91 -5.46,4.52 -6.38,6.03 -0.39,0.63 -0.72,1.18 -1.54,1.18 h -0.01 c -0.5,0 -0.98,-0.27 -1.23,-0.71 -0.42,-0.72 -0.11,-1.28 0.25,-1.93 0.21,-0.38 5.31,-9.37 12.19,-8.83 2.97,0.26 3.92,2.49 4.55,3.97 0.15,0.34 0.29,0.68 0.45,0.98 l 3.92,7.09 c 0.37,0.68 0.15,1.56 -0.52,1.95 -0.67,0.39 -1.51,0.21 -1.92,-0.45 l -2.92,-4.66 -0.68,3.64 z m 1.7,-16.73 c 0.3,1.8 -0.93,3.49 -2.72,3.79 -1.8,0.3 -3.49,-0.92 -3.79,-2.72 -0.3,-1.8 0.92,-3.49 2.72,-3.79 1.8,-0.3 3.49,0.92 3.79,2.72 z"
       id="path4631" />
    	<path
       class="st54"
       d="m 799.94,923.23 c -0.55,-1.67 -2.35,-2.57 -4.01,-2.02 -1.67,0.55 -2.57,2.34 -2.03,4.01 0.55,1.67 2.35,2.57 4.01,2.02 1.67,-0.54 2.58,-2.34 2.03,-4.01 z"
       id="path4633" />
    	<path
       class="st54"
       d="m 792.74,939.72 3.12,-6.19 c 0.96,-1.9 0.2,-4.22 -1.71,-5.18 l -2.03,-1.02 c -0.11,-0.06 -0.22,-0.09 -0.34,-0.12 -5.41,-2.37 -11.82,-0.16 -14.54,5.17 -0.41,0.81 -0.09,1.8 0.72,2.21 0.81,0.41 1.8,0.09 2.21,-0.71 1.57,-3.07 4.86,-4.68 8.1,-4.27 l -11.83,23.19 c -0.42,0.82 -0.09,1.81 0.72,2.23 0.24,0.12 0.5,0.18 0.75,0.18 0.6,0 1.19,-0.33 1.48,-0.91 l 7.18,-14.09 3.56,1.79 c 3.84,2.09 5.32,6.88 3.3,10.77 -0.42,0.81 -0.11,1.81 0.71,2.23 0.41,0.21 0.86,0.24 1.26,0.11 0.4,-0.13 0.76,-0.41 0.97,-0.82 2.68,-5.12 1.02,-11.37 -3.63,-14.57 z"
       id="path4635" />
    	<path
       class="st54"
       d="m 774.21,935.49 h -9.14 c -0.39,0 -0.72,-0.32 -0.72,-0.72 v 0 c 0,-0.39 0.32,-0.72 0.72,-0.72 h 9.14 c 0.39,0 0.72,0.32 0.72,0.72 v 0 c 0,0.4 -0.32,0.72 -0.72,0.72 z"
       id="path4637" />
    	<path
       class="st54"
       d="m 778.91,938.82 h -9.14 c -0.39,0 -0.72,-0.32 -0.72,-0.72 v 0 c 0,-0.4 0.32,-0.72 0.72,-0.72 h 9.14 c 0.39,0 0.72,0.32 0.72,0.72 v 0 c -0.01,0.39 -0.33,0.72 -0.72,0.72 z"
       id="path4639" />
    	<path
       class="st54"
       d="m 774.21,942.13 h -9.14 c -0.39,0 -0.72,-0.32 -0.72,-0.72 v 0 c 0,-0.4 0.32,-0.72 0.72,-0.72 h 9.14 c 0.39,0 0.72,0.32 0.72,0.72 v 0 c 0,0.4 -0.32,0.72 -0.72,0.72 z"
       id="path4641" />
    	<path
       class="st54"
       d="m 803.03,949.16 c 0.94,0 1.79,0.38 2.41,0.99 -0.84,1.05 -1.85,2.02 -3.05,2.9 -0.11,-0.09 -0.25,-0.14 -0.41,-0.15 -0.44,-1.21 -0.52,-2.37 -0.25,-3.48 0.4,-0.16 0.84,-0.26 1.3,-0.26 v 0 z"
       id="path4643" />
    	<path
       class="st54"
       d="m 801.41,949.57 c -0.22,1.09 -0.13,2.21 0.29,3.38 -0.15,0.06 -0.28,0.17 -0.36,0.32 l -1.74,-0.75 c 0.03,-1.28 0.75,-2.39 1.81,-2.95 v 0 z"
       id="path4645" />
    	<path
       class="st54"
       d="m 805.64,950.36 c 0.52,0.6 0.83,1.39 0.83,2.24 0,0.46 -0.09,0.9 -0.25,1.3 -1.18,0.08 -2.36,-0.01 -3.55,-0.28 v -0.01 c 0,-0.13 -0.04,-0.24 -0.09,-0.35 1.19,-0.87 2.21,-1.84 3.06,-2.9 v 0 z"
       id="path4647" />
    	<path
       class="st54"
       d="m 799.6,952.83 1.65,0.7 c 0,0.03 -0.01,0.05 -0.01,0.08 0,0.17 0.07,0.33 0.17,0.45 l -0.71,1.06 c -0.63,-0.57 -1.04,-1.38 -1.1,-2.29 v 0 z"
       id="path4649" />
    	<path
       class="st54"
       d="m 801.95,953.18 c 0.24,0 0.43,0.19 0.43,0.43 0,0.24 -0.19,0.43 -0.43,0.43 -0.24,0 -0.43,-0.19 -0.43,-0.43 0.01,-0.24 0.2,-0.43 0.43,-0.43 z"
       id="path4651" />
    	<path
       class="st54"
       d="m 802.61,953.9 c 1.16,0.26 2.32,0.36 3.47,0.3 -0.51,0.97 -1.46,1.66 -2.59,1.82 -0.5,-0.56 -0.83,-1.2 -1.02,-1.91 0.06,-0.07 0.11,-0.14 0.14,-0.21 z"
       id="path4653" />
    	<path
       class="st54"
       d="m 801.63,954.25 c 0.1,0.05 0.21,0.08 0.32,0.08 0.1,0 0.19,-0.02 0.27,-0.05 0.18,0.65 0.48,1.24 0.91,1.77 -0.04,0 -0.07,0.01 -0.11,0.01 -0.8,0 -1.53,-0.27 -2.12,-0.73 l 0.73,-1.08 z"
       id="path4655" />
    	<g
       class="st5"
       id="g4659">

    	</g>
    	<g
       class="st5"
       id="g4663">

    	</g>
    	<g
       class="st5"
       id="g4667">

    	</g>
    	<g
       class="st5"
       id="g4671">

    	</g>
    	<g
       class="st5"
       id="g4675">

    	</g>
    	<g
       class="st5"
       id="g4679">

    	</g>
    	<g
       class="st5"
       id="g4683">

    	</g>
    	<g
       class="st5"
       id="g4687">

    	</g>
    	<g
       class="st5"
       id="g4691">

    	</g>
    	<g
       class="st5"
       id="g4695">

    	</g>
    	<g
       class="st5"
       id="g4699">

    	</g>
    	<g
       class="st5"
       id="g4703">

    	</g>
    	<g
       class="st5"
       id="g4707">

    	</g>
    	<g
       class="st5"
       id="g4711">

    	</g>
    	<g
       class="st5"
       id="g4715">

    	</g>
    	<g
       class="st5"
       id="g4719">

    	</g>
    	<g
       class="st5"
       id="g4723">

    	</g>
    	<a
       id="a36907"
       xlink:href="https://tm-dash.azurewebsites.net/child-health"
       target="blank"
       xlink:title="Health and Nutrition"><g
         class="st5"
         id="g4727">
    		<path
       id="path4725"
       class="st0"
       d="m 714.51,503.95 0.04,0.01 c 0.36,-0.4 0.75,-0.63 1.16,-0.74 0.43,-0.12 0.9,-0.12 1.41,-0.02 1.32,0.25 2.33,1.25 2.07,2.63 l -1.49,7.96 -2.77,-0.52 1.28,-6.84 c 0.17,-0.88 0.14,-1.6 -0.75,-1.77 -0.89,-0.17 -1.17,0.49 -1.34,1.38 l -1.28,6.84 -2.77,-0.52 1.86,-9.93 2.77,0.52 z m -13.88,1.85 c 0.37,-2.74 1.08,-5.02 4.77,-4.52 3.69,0.5 3.77,2.89 3.4,5.63 -0.42,3.13 -1.2,5.27 -4.8,4.78 -3.62,-0.5 -3.8,-2.76 -3.37,-5.89 z m 5.39,0.56 c 0.28,-2.08 0.32,-3.15 -0.87,-3.31 -1.19,-0.16 -1.43,0.88 -1.71,2.96 -0.41,3.05 -0.24,3.74 0.79,3.88 1.03,0.15 1.38,-0.47 1.79,-3.53 z m -8.35,4.38 -2.81,-0.27 0.97,-10.06 2.81,0.27 z m 1.39,-14.37 -0.21,2.21 -2.81,-0.27 0.21,-2.21 z m -10.53,3.57 1.14,0.07 0.09,-1.6 2.89,-1.09 -0.17,2.86 1.46,0.09 -0.1,1.74 -1.46,-0.09 -0.32,5.39 c -0.04,0.76 -0.09,1.26 0.82,1.31 0.18,0.01 0.36,0.02 0.5,-0.01 l -0.1,1.74 c -0.38,0.02 -0.79,0.05 -1.46,0.01 -2.44,-0.14 -2.66,-1.78 -2.62,-2.4 l 0.36,-6.21 -1.14,-0.07 z m -1.96,10.04 -2.82,-0.09 0.34,-10.1 2.82,0.09 z m 0.49,-14.43 -0.07,2.22 -2.82,-0.09 0.07,-2.22 z m -7.56,4.18 v 1.3 h 0.04 c 0.52,-1.16 1.47,-1.51 2.62,-1.51 l 0.01,2.52 c -2.48,-0.15 -2.52,1.29 -2.51,2.29 l 0.02,5.5 -2.82,0.01 -0.04,-10.1 z m -9.62,0.19 1.14,-0.03 -0.05,-1.6 2.78,-1.34 0.08,2.86 1.46,-0.04 0.05,1.74 -1.46,0.04 0.15,5.4 c 0.02,0.76 0.02,1.26 0.94,1.24 0.18,0 0.36,-0.01 0.5,-0.05 l 0.05,1.74 c -0.38,0.05 -0.78,0.12 -1.46,0.14 -2.44,0.07 -2.81,-1.54 -2.82,-2.16 l -0.18,-6.22 -1.14,0.03 z m -3.7,9.34 h -0.04 c -0.25,0.46 -0.54,0.81 -0.92,1.02 -0.38,0.23 -0.82,0.34 -1.35,0.39 -1.34,0.1 -2.58,-0.6 -2.68,-2 l -0.63,-8.08 2.81,-0.22 0.54,6.98 c 0.07,0.9 0.28,1.54 1.18,1.47 0.9,-0.07 1.01,-0.74 0.94,-1.64 l -0.54,-6.98 2.81,-0.22 0.63,8.08 c 0.05,0.66 0.14,1.33 0.26,1.99 l -2.91,0.23 z m -17.93,3.08 -2,-14.3 4.04,-0.56 5.19,9.38 0.04,-0.01 -1.38,-9.91 2.79,-0.39 2,14.3 -3.94,0.55 -5.36,-9.92 -0.04,0.01 1.46,10.46 z m -9.38,1.84 -0.25,-1.09 -0.04,0.01 c -0.29,1.07 -0.98,1.58 -2.03,1.82 -2.85,0.65 -3.47,-2.54 -3.93,-4.56 -0.45,-1.99 -1.23,-5.03 1.54,-5.66 1,-0.23 1.75,-0.09 2.5,0.62 l 0.04,-0.01 -1.18,-5.17 2.75,-0.62 3.2,14.08 z m -1.28,-4.98 c -0.45,-1.97 -0.74,-3.34 -1.87,-3.08 -1.19,0.27 -0.86,1.63 -0.41,3.6 0.56,2.48 0.97,3.47 1.97,3.25 0.94,-0.22 0.88,-1.29 0.31,-3.77 z m -13.01,-0.78 0.04,-0.01 c 0.15,-0.52 0.39,-0.9 0.71,-1.17 0.33,-0.3 0.75,-0.5 1.25,-0.64 1.29,-0.36 2.64,0.09 3.02,1.44 l 2.17,7.8 -2.72,0.76 -1.87,-6.71 c -0.24,-0.87 -0.58,-1.5 -1.45,-1.26 -0.87,0.24 -0.83,0.96 -0.59,1.83 l 1.87,6.71 -2.72,0.76 -2.71,-9.73 2.72,-0.76 z m -3.1,8.43 c 0.19,0.59 0.47,1.17 0.72,1.74 l -2.49,0.82 -0.53,-1.23 -0.04,0.01 c -0.24,1.18 -0.87,1.91 -2.02,2.29 -1.86,0.62 -3,-0.55 -3.56,-2.22 -1.05,-3.17 1.36,-4.12 3.86,-4.9 l -0.25,-0.74 c -0.27,-0.82 -0.58,-1.37 -1.55,-1.05 -0.93,0.31 -0.77,1.04 -0.52,1.79 l -2.62,0.87 c -0.38,-1.16 -0.27,-2.02 0.22,-2.66 0.46,-0.66 1.27,-1.12 2.3,-1.46 3.4,-1.12 4.32,0.19 4.9,1.94 z m -5.33,0.44 c 0.23,0.68 0.62,1.48 1.49,1.19 1.58,-0.52 0.63,-2.57 0.28,-3.61 -1.31,0.49 -2.34,0.71 -1.77,2.42 z m -10.19,7.22 -2.73,-6.41 c -0.35,-0.83 -0.77,-1.41 -1.6,-1.06 -0.83,0.35 -0.7,1.06 -0.35,1.89 l 2.73,6.41 -2.6,1.11 -5.66,-13.29 2.6,-1.11 2.1,4.93 0.04,-0.02 c 0.08,-0.53 0.27,-0.94 0.55,-1.26 0.29,-0.34 0.68,-0.59 1.16,-0.8 1.23,-0.53 2.63,-0.25 3.18,1.04 l 3.18,7.45 z m -14.92,-4.39 1.03,-0.48 -0.68,-1.45 2.02,-2.34 1.21,2.59 1.32,-0.62 0.74,1.58 -1.32,0.62 2.29,4.89 c 0.32,0.69 0.52,1.15 1.35,0.76 0.16,-0.08 0.33,-0.15 0.44,-0.25 l 0.74,1.58 c -0.33,0.2 -0.66,0.42 -1.28,0.71 -2.21,1.04 -3.19,-0.29 -3.45,-0.86 l -2.64,-5.63 -1.03,0.48 z m -3.36,-3.16 6.44,12.93 -2.52,1.26 -6.44,-12.93 z m 0.7,13.7 c 0.3,0.54 0.68,1.06 1.04,1.57 l -2.29,1.28 -0.76,-1.11 -0.04,0.02 c -0.02,1.2 -0.49,2.04 -1.55,2.63 -1.71,0.96 -3.05,0.03 -3.91,-1.5 -1.63,-2.92 0.55,-4.3 2.86,-5.54 l -0.38,-0.68 c -0.42,-0.75 -0.83,-1.23 -1.72,-0.74 -0.86,0.48 -0.56,1.16 -0.17,1.86 l -2.41,1.35 c -0.59,-1.06 -0.64,-1.93 -0.29,-2.65 0.32,-0.73 1.04,-1.34 1.98,-1.87 3.12,-1.75 4.28,-0.63 5.18,0.98 z m -5.16,1.44 c 0.35,0.63 0.89,1.34 1.69,0.89 1.45,-0.81 0.13,-2.64 -0.41,-3.6 -1.19,0.73 -2.15,1.14 -1.28,2.71 z m -9.35,3.9 c 0.63,1.02 1.62,2.52 2.67,1.87 0.85,-0.53 0.51,-1.45 0.07,-2.16 l 2.43,-1.51 c 0.55,0.95 0.72,1.91 0.47,2.79 -0.23,0.88 -0.89,1.71 -2.01,2.41 -3.09,1.93 -4.67,0.3 -6.34,-2.39 -1.46,-2.34 -2.37,-4.56 0.79,-6.53 3.22,-2.01 4.88,-0.15 6.51,2.66 z m 1.35,-2.71 c -0.52,-0.83 -1.22,-2.04 -2.36,-1.33 -1.1,0.69 -0.28,1.97 0.17,2.7 z m -10.71,4 -3.35,-4.71 2.46,-1.75 8.36,11.78 -2.46,1.75 -3.73,-5.25 -2.82,2 3.73,5.25 -2.46,1.75 -8.36,-11.78 2.46,-1.75 3.35,4.71 z" />
    	</g></a>
    	<g
       class="st5"
       id="g4731">

    	</g>
    	<g
       class="st5"
       id="g4735">

    	</g>
    	<g
       class="st5"
       id="g4739">

    	</g>
    	<g
       class="st5"
       id="g4743">

    	</g>
    	<g
       class="st5"
       id="g4747">

    	</g>
    	<g
       class="st5"
       id="g4751">

    	</g>
    	<a
       id="a33682"
       xlink:href="https://tm-dash.azurewebsites.net/child-poverty"
       target="blank"
       xlink:title="Poverty"><g
         class="st5"
         id="g4755">
    		<path
       id="path4753"
       class="st3"
       d="m 856.42,636.77 8.74,-5.9 0.91,2.65 -6.25,3.67 0.01,0.04 7.21,-0.87 0.88,2.57 -14.44,0.84 -0.96,-2.8 z m 6.54,-11.62 0.41,1.06 1.49,-0.57 2.19,2.18 -2.67,1.03 0.52,1.36 -1.63,0.62 -0.52,-1.36 -5.04,1.94 c -0.71,0.27 -1.18,0.43 -0.85,1.29 0.07,0.17 0.13,0.34 0.22,0.45 l -1.62,0.62 c -0.17,-0.34 -0.37,-0.69 -0.62,-1.33 -0.88,-2.28 0.52,-3.16 1.1,-3.38 l 5.81,-2.23 -0.41,-1.06 z m -1.16,-2.86 -1.2,0.49 0.02,0.04 c 1.27,0.04 1.95,0.8 2.38,1.85 l -2.33,0.96 c -0.8,-2.35 -2.14,-1.84 -3.07,-1.46 l -5.09,2.1 -1.07,-2.61 9.34,-3.85 z m -9.28,-7.31 c -1.09,0.51 -2.7,1.31 -2.17,2.43 0.43,0.91 1.38,0.68 2.14,0.32 l 1.21,2.59 c -1.01,0.43 -1.98,0.49 -2.83,0.14 -0.84,-0.33 -1.59,-1.09 -2.15,-2.28 -1.55,-3.3 0.26,-4.67 3.12,-6.02 2.5,-1.17 4.81,-1.81 6.39,1.56 1.61,3.44 -0.44,4.87 -3.41,6.15 z m 2.53,1.67 c 0.89,-0.42 2.17,-0.97 1.6,-2.19 -0.55,-1.18 -1.92,-0.51 -2.7,-0.15 z m -3.44,-15.5 1.34,2.53 -6.04,4.8 0.02,0.04 7.39,-2.24 1.29,2.44 -10.23,2.27 -1.45,-2.74 z m -9.21,-5.92 c 2.38,-1.41 4.61,-2.27 6.51,0.93 1.9,3.2 0.07,4.75 -2.3,6.16 -2.72,1.61 -4.87,2.33 -6.73,-0.8 -1.86,-3.13 -0.2,-4.67 2.52,-6.29 z m 2.9,4.58 c 1.81,-1.07 2.67,-1.7 2.06,-2.73 -0.61,-1.03 -1.58,-0.58 -3.38,0.49 -2.65,1.57 -3.08,2.13 -2.55,3.03 0.53,0.9 1.22,0.78 3.87,-0.79 z m -1.35,-18.95 3.05,4.5 c 1.55,2.28 0.76,4.12 -1.42,5.6 -1.36,0.92 -3.78,1.98 -5.77,-0.95 l -1.26,-1.85 -4.87,3.3 -1.7,-2.5 z m -3.56,6.06 0.94,1.39 c 0.5,0.74 1.66,0.71 2.46,0.17 0.98,-0.66 1.62,-1.49 0.86,-2.62 l -0.85,-1.26 z" />
    	</g></a>
    	<g
       class="st5"
       id="g4759">

    	</g>
    	<g
       class="st5"
       id="g4763">

    	</g>
    	<g
       class="st5"
       id="g4767">

    	</g>
    	<g
       class="st5"
       id="g4771">

    	</g>
    	<g
       class="st5"
       id="g4775">

    	</g>
    	<g
       class="st5"
       id="g4779">

    	</g>
    	<g
       class="st5"
       id="g4783">

    	</g>
    	<g
       class="st5"
       id="g4787">

    	</g>
    	<g
       class="st5"
       id="g4791">

    	</g>
    	<g
       class="st5"
       id="g4795">

    	</g>
    	<g
       class="st5"
       id="g4799">

    	</g>
    	<g
       class="st5"
       id="g4803">

    	</g>
    	<g
       class="st5"
       id="g4807">

    	</g>
    	<g
       class="st5"
       id="g4811">

    	</g>
    	<g
       class="st5"
       id="g4815">

    	</g>
    	<g
       class="st5"
       id="g4819">

    	</g>
    	<g
       class="st5"
       id="g4823">

    	</g>
    	<g
       class="st5"
       id="g4827">

    	</g>
    	<g
       class="st5"
       id="g4831">

    	</g>
    	<g
       class="st5"
       id="g4835">

    	</g>
    	<g
       class="st5"
       id="g4839">

    	</g>
    	<g
       class="st5"
       id="g4843">

    	</g>
    	<g
       class="st5"
       id="g4847">

    	</g>
    	<g
       class="st5"
       id="g4851">

    	</g>
    	<g
       class="st5"
       id="g4855">

    	</g>
    	<g
       class="st5"
       id="g4859">

    	</g>
    	<g
       class="st5"
       id="g4863">

    	</g>
    	<g
       class="st5"
       id="g4867">

    	</g>
    	<g
       class="st5"
       id="g4871">

    	</g>
    	<a
       id="a40116"
       xlink:href="https://tm-dash.azurewebsites.net/child-protection"
       target="blank"
       xlink:title="Child Protection"><g
         class="st5"
         id="g4875">
    		<path
       id="path4873"
       class="st1"
       d="m 575.29,863.92 0.04,0.02 c 0.46,-0.27 0.9,-0.38 1.33,-0.36 0.45,0.01 0.89,0.16 1.35,0.4 1.18,0.63 1.85,1.89 1.19,3.13 l -3.81,7.15 -2.49,-1.33 3.27,-6.14 c 0.42,-0.79 0.61,-1.49 -0.18,-1.91 -0.79,-0.42 -1.26,0.12 -1.69,0.91 l -3.27,6.14 -2.49,-1.33 4.75,-8.92 2.49,1.33 z m -12.82,-3.01 c 1.44,-2.35 3.02,-4.16 6.19,-2.21 3.17,1.94 2.28,4.17 0.84,6.52 -1.65,2.7 -3.22,4.34 -6.33,2.44 -3.1,-1.91 -2.35,-4.06 -0.7,-6.75 z m 4.71,2.69 c 1.1,-1.79 1.57,-2.75 0.54,-3.38 -1.03,-0.63 -1.66,0.23 -2.76,2.02 -1.61,2.63 -1.73,3.33 -0.84,3.87 0.88,0.55 1.45,0.12 3.06,-2.51 z m -9.31,0.49 -2.35,-1.56 5.58,-8.42 2.35,1.56 z m 7.99,-12.04 -1.23,1.85 -2.35,-1.56 1.23,-1.85 z m -10.27,-1.75 0.93,0.65 0.92,-1.31 3.03,0.58 -1.64,2.34 1.2,0.84 -1,1.43 -1.2,-0.84 -3.09,4.43 c -0.44,0.62 -0.74,1.02 0.02,1.55 0.15,0.1 0.3,0.21 0.43,0.25 l -1,1.43 c -0.33,-0.19 -0.7,-0.37 -1.25,-0.75 -2,-1.4 -1.33,-2.91 -0.98,-3.42 l 3.56,-5.1 -0.93,-0.65 z m -4.84,0.88 c 0.9,-1.2 0.9,-1.83 0.2,-2.36 -0.96,-0.72 -1.68,0.06 -2.94,1.74 -1.86,2.46 -2.04,3.14 -1.21,3.77 0.7,0.53 1.52,0.14 2.31,-0.91 l 2.25,1.7 c -1.65,2.19 -3.54,2.24 -5.65,0.65 -2.91,-2.19 -1.95,-4.26 -0.05,-6.78 1.66,-2.2 3.4,-3.85 6.37,-1.61 2.08,1.57 2.56,3.38 0.97,5.49 z m -10.78,-6.17 c -0.77,0.92 -1.89,2.33 -0.94,3.12 0.77,0.64 1.54,0.03 2.07,-0.61 l 2.2,1.83 c -0.74,0.82 -1.59,1.28 -2.51,1.32 -0.9,0.05 -1.9,-0.31 -2.92,-1.16 -2.79,-2.33 -1.74,-4.35 0.28,-6.77 1.77,-2.12 3.59,-3.68 6.44,-1.29 2.92,2.44 1.66,4.59 -0.49,7.02 z m 3,0.44 c 0.63,-0.75 1.56,-1.8 0.53,-2.66 -1,-0.83 -1.96,0.35 -2.51,1.01 z m -6.03,-10.53 0.84,0.77 1.08,-1.18 2.93,0.98 -1.94,2.1 1.07,0.99 -1.18,1.28 -1.07,-0.99 -3.66,3.97 c -0.52,0.56 -0.87,0.91 -0.19,1.54 0.13,0.12 0.26,0.25 0.39,0.31 l -1.18,1.28 c -0.31,-0.23 -0.64,-0.46 -1.14,-0.92 -1.79,-1.65 -0.93,-3.06 -0.51,-3.52 l 4.22,-4.57 -0.84,-0.77 z m -9.71,-2.61 c 1.95,-1.96 3.89,-3.35 6.53,-0.73 2.64,2.62 1.26,4.58 -0.69,6.54 -2.23,2.24 -4.13,3.48 -6.72,0.91 -2.59,-2.57 -1.34,-4.48 0.88,-6.72 z m 3.96,3.7 c 1.48,-1.49 2.16,-2.31 1.31,-3.16 -0.85,-0.85 -1.67,-0.16 -3.15,1.33 -2.17,2.19 -2.45,2.84 -1.71,3.57 0.73,0.73 1.38,0.45 3.55,-1.74 z m -2.79,-9.65 -0.95,0.89 0.03,0.03 c 1.2,-0.41 2.11,0.06 2.89,0.89 l -1.84,1.72 c -1.58,-1.92 -2.66,-0.97 -3.39,-0.29 l -4.02,3.75 -1.92,-2.06 7.38,-6.89 z m -5.33,-12.67 3.51,4.16 c 1.78,2.11 1.19,4.02 -0.83,5.72 -1.25,1.06 -3.55,2.37 -5.83,-0.34 l -1.44,-1.71 -4.5,3.79 -1.95,-2.31 z m -2.9,6.39 1.08,1.29 c 0.58,0.69 1.73,0.53 2.46,-0.09 0.9,-0.76 1.46,-1.65 0.58,-2.69 l -0.98,-1.16 z m -13.96,-4.66 0.91,-0.65 -0.02,-0.03 c -1.1,0.15 -1.83,-0.28 -2.46,-1.16 -1.71,-2.37 0.98,-4.18 2.67,-5.4 1.66,-1.19 4.16,-3.09 5.82,-0.79 0.6,0.83 0.76,1.57 0.4,2.54 l 0.02,0.03 4.3,-3.1 1.65,2.29 -11.72,8.44 z m 4.09,-3.11 c 1.64,-1.18 2.79,-1.98 2.11,-2.93 -0.71,-0.99 -1.84,-0.16 -3.48,1.03 -2.06,1.49 -2.82,2.25 -2.22,3.08 0.57,0.78 1.53,0.3 3.59,-1.18 z m -3.36,-11.89 0.02,0.03 c 0.54,-0.01 0.97,0.11 1.33,0.33 0.39,0.23 0.7,0.57 0.98,1.01 0.73,1.13 0.69,2.55 -0.48,3.31 l -6.81,4.39 -1.53,-2.37 5.85,-3.77 c 0.76,-0.49 1.26,-1 0.77,-1.76 -0.49,-0.76 -1.16,-0.51 -1.92,-0.02 l -5.85,3.77 -1.53,-2.37 8.49,-5.48 1.53,2.37 z m -8.77,-0.38 c -0.54,0.31 -1.05,0.7 -1.56,1.06 l -1.31,-2.27 1.1,-0.77 -0.02,-0.04 c -1.2,0 -2.04,-0.46 -2.65,-1.52 -0.98,-1.7 -0.07,-3.05 1.46,-3.93 2.9,-1.66 4.3,0.51 5.57,2.8 l 0.68,-0.39 c 0.75,-0.43 1.22,-0.84 0.72,-1.73 -0.49,-0.85 -1.17,-0.55 -1.86,-0.15 l -1.38,-2.39 c 1.06,-0.61 1.92,-0.67 2.65,-0.32 0.74,0.31 1.35,1.02 1.89,1.96 1.78,3.11 0.68,4.27 -0.92,5.19 z m -1.5,-5.13 c -0.62,0.36 -1.33,0.9 -0.87,1.7 0.83,1.44 2.64,0.1 3.59,-0.45 -0.74,-1.19 -1.16,-2.15 -2.72,-1.25 z m 0.06,-14.93 0.5,1.02 1.44,-0.71 2.37,1.98 -2.57,1.26 0.64,1.31 -1.56,0.77 -0.64,-1.31 -4.85,2.38 c -0.68,0.33 -1.14,0.54 -0.74,1.36 0.08,0.16 0.16,0.32 0.26,0.43 l -1.56,0.77 c -0.2,-0.32 -0.43,-0.66 -0.73,-1.27 -1.07,-2.19 0.24,-3.19 0.8,-3.47 l 5.58,-2.74 -0.5,-1.02 z m -3.28,-4.72 0.02,0.04 c 0.53,0.07 0.95,0.26 1.26,0.53 0.34,0.28 0.6,0.67 0.81,1.15 0.54,1.23 0.29,2.63 -0.99,3.2 l -7.41,3.28 -1.14,-2.58 6.37,-2.82 c 0.82,-0.36 1.4,-0.79 1.03,-1.62 -0.37,-0.83 -1.07,-0.69 -1.89,-0.32 l -6.37,2.82 -1.14,-2.58 9.24,-4.09 1.14,2.58 z m -7.87,-7.43 c -1.12,0.43 -2.79,1.11 -2.35,2.27 0.36,0.93 1.32,0.78 2.11,0.48 l 1.02,2.67 c -1.04,0.36 -2.01,0.34 -2.83,-0.07 -0.82,-0.4 -1.51,-1.2 -1.98,-2.44 -1.3,-3.4 0.61,-4.64 3.56,-5.77 2.58,-0.98 4.93,-1.45 6.25,2.03 1.35,3.55 -0.79,4.82 -3.86,5.88 z m 2.4,1.85 c 0.92,-0.35 2.24,-0.81 1.76,-2.06 -0.46,-1.21 -1.88,-0.66 -2.68,-0.35 z m -2.73,-16.65 0.01,0.04 c 1.03,0.26 1.57,0.88 1.89,1.89 0.31,0.95 0.1,1.86 -0.53,2.54 1.04,0.36 1.67,1 2.02,2.1 0.41,1.28 0.01,2.65 -1.32,3.08 l -7.71,2.49 -0.87,-2.68 6.63,-2.14 c 0.86,-0.28 1.47,-0.64 1.2,-1.5 -0.28,-0.86 -0.99,-0.79 -1.85,-0.52 l -6.62,2.14 -0.85,-2.63 6.62,-2.14 c 0.86,-0.28 1.47,-0.64 1.2,-1.5 -0.28,-0.86 -0.99,-0.79 -1.85,-0.52 l -6.62,2.14 -0.87,-2.68 9.61,-3.1 0.87,2.69 z m -2.34,-8.89 0.01,0.04 c 0.51,0.16 0.89,0.42 1.16,0.74 0.29,0.34 0.48,0.77 0.61,1.27 0.33,1.3 -0.16,2.64 -1.52,2.98 l -7.86,1.98 -0.69,-2.74 6.75,-1.7 c 0.87,-0.22 1.51,-0.55 1.29,-1.42 -0.22,-0.87 -0.94,-0.86 -1.81,-0.64 l -6.75,1.7 -0.69,-2.74 9.8,-2.46 0.69,2.74 z m -6.45,-11.56 c 2.71,-0.53 5.1,-0.6 5.82,3.06 0.72,3.65 -1.52,4.5 -4.23,5.03 -3.1,0.61 -5.37,0.57 -6.07,-3.01 -0.7,-3.58 1.38,-4.47 4.48,-5.08 z m 1.21,5.28 c 2.06,-0.41 3.08,-0.71 2.85,-1.89 -0.23,-1.18 -1.29,-1.07 -3.35,-0.67 -3.02,0.59 -3.62,0.98 -3.42,2 0.2,1.03 0.9,1.16 3.92,0.56 z m 3.15,-9.52 -1.29,0.2 0.01,0.04 c 1.23,0.33 1.71,1.23 1.89,2.36 l -2.49,0.39 c -0.22,-2.48 -1.65,-2.29 -2.64,-2.14 l -5.43,0.85 -0.44,-2.79 9.98,-1.56 z m -10.71,-3.58 -0.33,-2.8 10.03,-1.17 0.33,2.8 z m 14.35,-1.67 -2.21,0.26 -0.33,-2.8 2.21,-0.26 z m -5.49,-11.96 0.22,2.85 -7.45,2 v 0.04 l 7.67,0.89 0.21,2.75 -10.29,-1.99 -0.24,-3.09 z m -1.21,-5.67 v 0.04 c 0.47,0.27 0.78,0.6 0.97,0.98 0.21,0.39 0.3,0.85 0.32,1.37 0.04,1.34 -0.73,2.54 -2.13,2.58 l -8.1,0.21 -0.07,-2.82 6.96,-0.18 c 0.9,-0.02 1.6,-0.2 1.57,-1.1 -0.02,-0.9 -0.73,-1.04 -1.63,-1.02 l -6.96,0.18 -0.07,-2.82 10.1,-0.26 0.07,2.82 z m -9.02,-12.44 14.44,0.36 -0.2,7.88 -2.22,-0.06 0.12,-4.86 -3.56,-0.09 -0.11,4.48 -2.22,-0.05 0.11,-4.48 -4.22,-0.11 -0.12,5.02 -2.22,-0.05 z m 0.72,-11.64 10.38,-1.84 -0.25,2.79 -7.2,0.81 v 0.04 l 6.94,2.14 -0.24,2.71 -13.53,-5.11 0.26,-2.95 z m 14.89,-2.46 -14.33,-1.81 0.35,-2.8 14.33,1.81 z m -13.58,-7.32 0.42,-2.79 9.99,1.51 -0.42,2.79 z m 14.28,2.17 -2.2,-0.33 0.42,-2.79 2.2,0.33 z m -2.65,-14.89 -0.01,0.04 c 0.76,0.74 0.92,1.55 0.69,2.58 -0.21,0.98 -0.85,1.66 -1.73,1.94 0.72,0.83 0.94,1.7 0.7,2.83 -0.28,1.31 -1.31,2.3 -2.68,2 l -7.92,-1.71 0.59,-2.76 6.81,1.46 c 0.88,0.19 1.6,0.18 1.79,-0.7 0.19,-0.88 -0.46,-1.18 -1.34,-1.37 l -6.81,-1.47 0.58,-2.7 6.81,1.46 c 0.88,0.19 1.6,0.18 1.79,-0.7 0.19,-0.88 -0.46,-1.18 -1.34,-1.37 l -6.81,-1.46 0.59,-2.76 9.88,2.13 -0.59,2.76 z m -5.95,-6.22 c -0.6,-0.17 -1.24,-0.26 -1.85,-0.37 l 0.71,-2.52 1.32,0.25 0.01,-0.04 c -0.84,-0.86 -1.1,-1.78 -0.77,-2.96 0.53,-1.89 2.13,-2.19 3.83,-1.71 3.22,0.9 2.65,3.42 1.91,5.94 l 0.75,0.21 c 0.83,0.23 1.46,0.28 1.73,-0.7 0.26,-0.94 -0.43,-1.22 -1.2,-1.44 l 0.75,-2.66 c 1.17,0.33 1.82,0.91 2.09,1.67 0.29,0.75 0.21,1.68 -0.08,2.72 -0.97,3.45 -2.57,3.48 -4.34,2.98 z m 2.62,-4.67 c -0.69,-0.19 -1.57,-0.32 -1.82,0.57 -0.45,1.6 1.78,1.95 2.84,2.25 0.32,-1.36 0.71,-2.33 -1.02,-2.82 z m 0.31,-11.6 13.76,4.4 -2.29,7.14 -2.11,-0.68 1.37,-4.27 -3.53,-1.13 -1.3,4.08 -2.11,-0.68 1.31,-4.08 -6,-1.92 z" />
    	</g></a>
    	<g
       class="st5"
       id="g4879">
    		<path
       class="st4"
       d="m 636.39,894.51 2.09,-14.29 7.8,1.14 -0.32,2.2 -4.81,-0.7 -0.52,3.52 4.43,0.65 -0.32,2.2 -4.43,-0.65 -0.61,4.18 4.97,0.73 -0.32,2.2 z"
       id="path4877" />
    	</g>
    	<g
       class="st5"
       id="g4883">
    		<path
       class="st4"
       d="m 651.18,896.41 0.11,-1.11 h -0.04 c -0.61,0.92 -1.42,1.19 -2.5,1.08 -2.91,-0.29 -2.49,-3.5 -2.29,-5.57 0.2,-2.03 0.42,-5.16 3.25,-4.89 1.02,0.1 1.68,0.47 2.18,1.38 h 0.04 l 0.52,-5.28 2.81,0.27 -1.41,14.37 z m 0.36,-5.13 c 0.2,-2.01 0.35,-3.4 -0.8,-3.52 -1.21,-0.12 -1.33,1.28 -1.53,3.29 -0.25,2.53 -0.17,3.6 0.84,3.7 0.96,0.09 1.25,-0.94 1.49,-3.47 z"
       id="path4881" />
    	</g>
    	<g
       class="st5"
       id="g4887">
    		<path
       class="st4"
       d="m 661.09,896.07 h -0.04 c -0.3,0.43 -0.64,0.73 -1.05,0.89 -0.41,0.18 -0.85,0.24 -1.39,0.21 -1.34,-0.07 -2.48,-0.92 -2.41,-2.32 l 0.4,-8.09 2.82,0.14 -0.35,6.99 c -0.04,0.9 0.08,1.57 0.98,1.61 0.9,0.04 1.09,-0.61 1.14,-1.51 l 0.35,-6.99 2.82,0.14 -0.4,8.09 c -0.03,0.66 -0.03,1.34 0,2 l -2.92,-0.15 z"
       id="path4885" />
    	</g>
    	<g
       class="st5"
       id="g4891">
    		<path
       class="st4"
       d="m 671.41,891 c 0,-1.5 -0.38,-2 -1.26,-2 -1.2,0 -1.3,1.06 -1.31,3.16 -0.01,3.08 0.25,3.74 1.29,3.74 0.88,0 1.3,-0.8 1.3,-2.12 h 2.82 c -0.01,2.74 -1.49,3.92 -4.13,3.91 -3.64,-0.01 -4.12,-2.23 -4.11,-5.39 0.01,-2.76 0.41,-5.12 4.13,-5.11 2.6,0 4.08,1.17 4.07,3.81 z"
       id="path4889" />
    	</g>
    	<g
       class="st5"
       id="g4895">
    		<path
       class="st4"
       d="m 683.67,895.09 c 0.03,0.62 0.14,1.26 0.23,1.87 l -2.62,0.12 -0.18,-1.33 h -0.04 c -0.55,1.07 -1.35,1.6 -2.57,1.66 -1.96,0.09 -2.75,-1.34 -2.83,-3.09 -0.15,-3.34 2.42,-3.6 5.04,-3.68 l -0.04,-0.78 c -0.04,-0.86 -0.19,-1.47 -1.21,-1.43 -0.98,0.04 -1.02,0.79 -0.99,1.59 l -2.76,0.13 c -0.06,-1.22 0.29,-2.02 0.92,-2.51 0.62,-0.51 1.53,-0.73 2.61,-0.78 3.58,-0.17 4.11,1.35 4.19,3.19 z m -5.25,-1.02 c 0.03,0.72 0.19,1.59 1.11,1.55 1.66,-0.08 1.29,-2.3 1.24,-3.4 -1.39,0.13 -2.44,0.05 -2.35,1.85 z"
       id="path4893" />
    	</g>
    	<g
       class="st5"
       id="g4899">
    		<path
       class="st4"
       d="m 684.13,886.83 1.14,-0.09 -0.13,-1.59 2.71,-1.49 0.24,2.85 1.46,-0.12 0.14,1.74 -1.46,0.12 0.44,5.38 c 0.06,0.76 0.08,1.26 1,1.18 0.18,-0.01 0.36,-0.03 0.5,-0.08 l 0.14,1.73 c -0.38,0.07 -0.77,0.16 -1.45,0.22 -2.43,0.2 -2.88,-1.39 -2.94,-2 l -0.51,-6.2 -1.14,0.09 z"
       id="path4897" />
    	</g>
    	<g
       class="st5"
       id="g4903">
    		<path
       class="st4"
       d="m 693.14,881.65 0.24,2.21 -2.8,0.3 -0.24,-2.21 z m 1.54,14.36 -2.8,0.3 -1.07,-10.04 2.8,-0.3 z"
       id="path4901" />
    	</g>
    	<g
       class="st5"
       id="g4907">
    		<path
       class="st4"
       d="m 696.18,890.66 c -0.39,-2.73 -0.33,-5.13 3.35,-5.66 3.68,-0.53 4.42,1.75 4.81,4.48 0.45,3.13 0.29,5.39 -3.31,5.91 -3.61,0.52 -4.4,-1.61 -4.85,-4.73 z m 5.34,-0.93 c -0.3,-2.08 -0.55,-3.11 -1.74,-2.94 -1.19,0.17 -1.14,1.24 -0.84,3.31 0.44,3.05 0.79,3.67 1.82,3.52 1.04,-0.16 1.2,-0.85 0.76,-3.89 z"
       id="path4905" />
    	</g>
    	<g
       class="st5"
       id="g4911">
    		<path
       class="st4"
       d="m 708.1,884.84 0.04,-0.01 c 0.19,-0.5 0.46,-0.86 0.8,-1.11 0.36,-0.27 0.79,-0.44 1.3,-0.54 1.32,-0.25 2.63,0.31 2.89,1.68 l 1.54,7.95 -2.77,0.54 -1.32,-6.83 c -0.17,-0.88 -0.46,-1.54 -1.35,-1.37 -0.88,0.17 -0.91,0.89 -0.74,1.77 l 1.32,6.83 -2.77,0.54 -1.92,-9.92 2.77,-0.54 z"
       id="path4909" />
    	</g>
    	<g
       class="st5"
       id="g4915">
    		<path
       class="st2"
       d="m 774.91,853.85 4.58,-2.93 c 2.33,-1.49 4.14,-0.65 5.56,1.57 0.88,1.38 1.88,3.83 -1.1,5.74 l -1.89,1.21 3.17,4.95 -2.54,1.63 z m 5.96,3.72 1.42,-0.91 c 0.76,-0.49 0.75,-1.65 0.23,-2.45 -0.64,-1 -1.44,-1.67 -2.59,-0.93 l -1.28,0.82 z"
       id="path4913" />
    	</g>
    	<g
       class="st5"
       id="g4919">
    		<path
       class="st2"
       d="m 797.04,854.09 c 0.36,0.51 0.79,0.98 1.2,1.45 l -2.14,1.52 -0.87,-1.02 -0.03,0.02 c 0.11,1.2 -0.27,2.08 -1.26,2.78 -1.6,1.13 -3.03,0.36 -4.05,-1.08 -1.93,-2.72 0.09,-4.33 2.25,-5.82 l -0.45,-0.64 c -0.5,-0.7 -0.95,-1.14 -1.79,-0.55 -0.8,0.57 -0.44,1.22 0.03,1.87 l -2.25,1.6 c -0.71,-1 -0.85,-1.85 -0.58,-2.61 0.24,-0.76 0.89,-1.44 1.77,-2.07 2.92,-2.07 4.19,-1.08 5.25,0.42 z m -4.97,1.98 c 0.42,0.59 1.02,1.24 1.77,0.7 1.35,-0.96 -0.15,-2.64 -0.79,-3.54 -1.1,0.87 -2.02,1.37 -0.98,2.84 z"
       id="path4917" />
    	</g>
    	<g
       class="st5"
       id="g4923">
    		<path
       class="st2"
       d="m 795.98,844.56 0.79,1.03 0.03,-0.02 c -0.29,-1.24 0.26,-2.09 1.17,-2.78 l 1.53,2 c -2.07,1.38 -1.22,2.55 -0.62,3.34 l 3.34,4.37 -2.24,1.71 -6.14,-8.02 z"
       id="path4921" />
    	</g>
    	<g
       class="st5"
       id="g4927">
    		<path
       class="st2"
       d="m 797.96,843.06 0.88,-0.72 -1.02,-1.23 1.38,-2.77 1.82,2.21 1.13,-0.93 1.11,1.34 -1.13,0.93 3.43,4.17 c 0.48,0.59 0.79,0.99 1.5,0.4 0.14,-0.11 0.28,-0.23 0.36,-0.35 l 1.11,1.34 c -0.27,0.27 -0.54,0.57 -1.06,1 -1.88,1.55 -3.16,0.5 -3.55,0.03 l -3.96,-4.8 -0.88,0.72 z"
       id="path4925" />
    	</g>
    	<g
       class="st5"
       id="g4931">
    		<path
       class="st2"
       d="m 802.42,833.67 1.45,1.68 -2.13,1.85 -1.45,-1.68 z m 9.45,10.93 -2.13,1.84 -6.61,-7.64 2.13,-1.85 z"
       id="path4929" />
    	</g>
    	<g
       class="st5"
       id="g4935">
    		<path
       class="st2"
       d="m 813.1,834.7 c -1.02,-1.1 -1.64,-1.21 -2.29,-0.61 -0.88,0.82 -0.23,1.66 1.2,3.2 2.1,2.26 2.74,2.56 3.5,1.85 0.64,-0.6 0.41,-1.47 -0.49,-2.44 l 2.07,-1.92 c 1.87,2.01 1.58,3.88 -0.35,5.68 -2.67,2.48 -4.53,1.18 -6.68,-1.14 -1.88,-2.02 -3.19,-4.02 -0.47,-6.56 1.91,-1.77 3.78,-1.93 5.58,0.01 z"
       id="path4933" />
    	</g>
    	<g
       class="st5"
       id="g4939">
    		<path
       class="st2"
       d="m 812.99,823.71 1.57,1.57 -2,1.99 -1.57,-1.57 z m 10.21,10.22 -2,1.99 -7.14,-7.15 2,-1.99 z"
       id="path4937" />
    	</g>
    	<g
       class="st5"
       id="g4943">
    		<path
       class="st2"
       d="m 819.4,823.32 0.82,0.76 0.03,-0.03 c -0.36,-1.05 -0.08,-1.85 0.66,-2.64 1.99,-2.14 4.29,0.15 5.82,1.57 1.49,1.39 3.84,3.48 1.91,5.55 -0.7,0.75 -1.39,1.05 -2.42,0.89 l -0.03,0.03 3.88,3.62 -1.92,2.06 -10.56,-9.85 z m 5.32,1.57 c -1.48,-1.38 -2.49,-2.35 -3.32,-1.46 -0.79,0.85 0.25,1.79 1.72,3.17 1.86,1.73 2.76,2.32 3.41,1.62 0.7,-0.74 0.05,-1.6 -1.81,-3.33 z"
       id="path4941" />
    	</g>
    	<g
       class="st5"
       id="g4947">
    		<path
       class="st2"
       d="m 835.25,817.74 c 0.47,0.4 1.01,0.75 1.53,1.11 l -1.69,2 -1.1,-0.78 -0.03,0.03 c 0.41,1.13 0.26,2.08 -0.53,3.01 -1.27,1.5 -2.85,1.1 -4.19,-0.04 -2.55,-2.16 -0.99,-4.22 0.74,-6.19 l -0.6,-0.5 c -0.66,-0.56 -1.21,-0.87 -1.87,-0.09 -0.63,0.75 -0.12,1.29 0.49,1.8 l -1.78,2.11 c -0.93,-0.79 -1.28,-1.58 -1.21,-2.38 0.05,-0.8 0.51,-1.62 1.21,-2.44 2.31,-2.73 3.79,-2.09 5.19,-0.9 z m -4.32,3.16 c 0.55,0.47 1.3,0.94 1.89,0.24 1.07,-1.27 -0.8,-2.52 -1.64,-3.23 -0.86,1.11 -1.62,1.82 -0.25,2.99 z"
       id="path4945" />
    	</g>
    	<g
       class="st5"
       id="g4951">
    		<path
       class="st2"
       d="m 829.48,811.75 0.71,-0.9 -1.26,-0.99 0.76,-3 2.25,1.77 0.9,-1.15 1.37,1.08 -0.9,1.15 4.24,3.34 c 0.6,0.47 0.98,0.8 1.55,0.07 0.11,-0.14 0.22,-0.28 0.28,-0.42 l 1.37,1.08 c -0.2,0.32 -0.4,0.67 -0.83,1.21 -1.51,1.92 -2.98,1.16 -3.47,0.78 l -4.89,-3.85 -0.71,0.9 z"
       id="path4949" />
    	</g>
    	<g
       class="st5"
       id="g4955">
    		<path
       class="st2"
       d="m 831.69,801.71 1.79,1.31 -1.67,2.28 -1.79,-1.31 z m 11.65,8.54 -1.67,2.28 -8.15,-5.97 1.67,-2.28 z"
       id="path4953" />
    	</g>
    	<g
       class="st5"
       id="g4959">
    		<path
       class="st2"
       d="m 840.44,805.55 c -2.28,-1.55 -4.01,-3.21 -1.92,-6.29 2.09,-3.08 4.27,-2.08 6.55,-0.53 2.61,1.78 4.18,3.42 2.14,6.43 -2.05,3.02 -4.16,2.17 -6.77,0.39 z m 2.91,-4.57 c -1.74,-1.18 -2.67,-1.69 -3.35,-0.7 -0.67,0.99 0.15,1.67 1.88,2.85 2.55,1.73 3.24,1.88 3.83,1.02 0.59,-0.86 0.19,-1.44 -2.36,-3.17 z"
       id="path4957" />
    	</g>
    	<g
       class="st5"
       id="g4963">
    		<path
       class="st2"
       d="m 844.17,792.82 0.02,-0.03 c -0.25,-0.48 -0.32,-0.92 -0.28,-1.34 0.04,-0.45 0.21,-0.88 0.48,-1.32 0.7,-1.14 2,-1.73 3.19,-1 l 6.91,4.23 -1.47,2.41 -5.94,-3.63 c -0.77,-0.47 -1.45,-0.7 -1.92,0.07 -0.47,0.77 0.04,1.27 0.81,1.74 l 5.94,3.63 -1.47,2.41 -8.62,-5.27 1.47,-2.41 z"
       id="path4961" />
    	</g>
    	<g
       class="st5"
       id="g4967">
    		<path
       class="st2"
       d="m 859.68,779.89 c 0.55,0.29 1.16,0.51 1.73,0.74 l -1.21,2.33 -1.25,-0.51 -0.02,0.04 c 0.65,1.01 0.71,1.97 0.15,3.05 -0.9,1.74 -2.53,1.71 -4.09,0.9 -2.97,-1.54 -1.9,-3.89 -0.66,-6.2 l -0.69,-0.36 c -0.76,-0.4 -1.37,-0.57 -1.84,0.33 -0.45,0.87 0.17,1.28 0.88,1.65 l -1.27,2.45 c -1.08,-0.56 -1.6,-1.26 -1.71,-2.05 -0.13,-0.79 0.13,-1.69 0.63,-2.65 1.65,-3.18 3.23,-2.88 4.86,-2.03 z m -3.51,4.04 c 0.64,0.33 1.48,0.63 1.9,-0.19 0.76,-1.47 -1.35,-2.27 -2.32,-2.78 -0.6,1.27 -1.18,2.14 0.42,2.97 z"
       id="path4965" />
    	</g>
    	<g
       class="st5"
       id="g4971">
    		<path
       class="st2"
       d="m 855.33,772.31 0.02,-0.04 c -0.3,-0.45 -0.43,-0.88 -0.44,-1.3 -0.01,-0.45 0.11,-0.9 0.32,-1.37 0.56,-1.22 1.78,-1.96 3.05,-1.37 l 7.36,3.38 -1.18,2.56 -6.33,-2.9 c -0.82,-0.38 -1.52,-0.52 -1.9,0.3 -0.38,0.82 0.19,1.26 1.01,1.63 l 6.33,2.9 -1.18,2.56 -9.18,-4.21 1.18,-2.56 z"
       id="path4969" />
    	</g>
    	<g
       class="st5"
       id="g4975">
    		<path
       class="st2"
       d="m 868.44,764.88 -1.04,-0.42 -0.02,0.04 c 0.72,0.85 0.74,1.7 0.34,2.7 -1.09,2.71 -4.06,1.41 -5.99,0.63 -1.89,-0.76 -4.84,-1.86 -3.78,-4.49 0.38,-0.95 0.92,-1.48 1.94,-1.7 l 0.01,-0.04 -4.92,-1.98 1.05,-2.62 13.4,5.39 z m -4.83,-1.78 c -1.88,-0.75 -3.17,-1.29 -3.6,-0.22 -0.46,1.13 0.85,1.63 2.73,2.39 2.36,0.95 3.41,1.18 3.79,0.23 0.36,-0.89 -0.56,-1.46 -2.92,-2.4 z"
       id="path4973" />
    	</g>
    	<g
       class="st5"
       id="g4979">
    		<path
       class="st2"
       d="m 864.87,753.89 c -3.64,-1.16 -7.11,-2.27 -5.59,-7.02 0.94,-2.94 2.94,-3.6 5.85,-2.54 l -0.9,2.82 c -1.83,-0.58 -2.62,-0.48 -2.89,0.38 -0.52,1.62 0.94,2.32 4.46,3.44 3.52,1.12 5.12,1.41 5.63,-0.21 0.43,-1.33 -1.31,-1.83 -2.38,-2.21 l 0.91,-2.84 c 3.68,1.18 4.39,3.02 3.53,5.71 -1.51,4.75 -5.02,3.62 -8.62,2.47 z"
       id="path4977" />
    	</g>
    	<g
       class="st5"
       id="g4983">
    		<path
       class="st2"
       d="m 861.95,738.62 2.14,0.6 -0.76,2.72 -2.14,-0.6 z m 13.91,3.9 -0.76,2.72 -9.73,-2.73 0.76,-2.72 z"
       id="path4981" />
    	</g>
    	<g
       class="st5"
       id="g4987">
    		<path
       class="st2"
       d="m 866.44,738.67 0.67,-2.78 7.7,0.4 0.01,-0.04 -7.02,-3.22 0.65,-2.68 9.17,5.07 -0.73,3.01 z"
       id="path4985" />
    	</g>
    	<g
       class="st5"
       id="g4991">
    		<path
       class="st2"
       d="m 864.91,725.58 2.18,0.44 -0.56,2.76 -2.18,-0.44 z m 14.16,2.87 -0.56,2.76 -9.9,-2.01 0.56,-2.76 z"
       id="path4989" />
    	</g>
    	<g
       class="st5"
       id="g4995">
    		<path
       class="st2"
       d="m 865.78,720.63 14.25,2.34 -0.46,2.78 -14.25,-2.34 z"
       id="path4993" />
    	</g>
    	<g
       class="st5"
       id="g4999">
    		<path
       class="st2"
       d="m 881.38,713.03 -0.3,3 -14.37,-1.45 0.56,-5.55 c 0.21,-2.05 1.65,-3.23 4.1,-2.98 1.83,0.18 3.13,1.04 3.25,3.02 h 0.04 c 0.14,-0.65 0.5,-2.58 3.09,-2.32 0.92,0.09 3.63,0.31 4.25,0.09 l -0.3,2.95 c -0.92,0.31 -1.88,0.13 -2.82,0.04 -1.71,-0.17 -3.15,-0.48 -3.38,1.83 l -0.08,0.78 z m -8.16,-0.82 0.13,-1.33 c 0.12,-1.19 -1.04,-1.65 -1.96,-1.75 -1.37,-0.14 -1.95,0.39 -2.04,1.34 l -0.13,1.33 z"
       id="path4997" />
    	</g>
    	<g
       class="st5"
       id="g5003">
    		<path
       class="st2"
       d="m 867.87,701.08 2.22,0.14 -0.18,2.81 -2.22,-0.14 z m 14.42,0.9 -0.18,2.81 -10.08,-0.63 0.18,-2.81 z"
       id="path5001" />
    	</g>
    	<g
       class="st5"
       id="g5007">
    		<path
       class="st2"
       d="m 872.52,691.53 10.52,0.26 c 0.7,0.02 3.46,0.05 3.37,3.93 -0.05,2.1 -0.64,3.89 -3.1,3.88 l 0.07,-2.76 c 0.42,0.01 0.78,-0.04 1.03,-0.21 0.26,-0.17 0.41,-0.49 0.42,-0.93 0.02,-0.7 -0.63,-1.06 -1.65,-1.08 l -1.94,-0.05 v 0.04 c 0.77,0.44 1.15,1.25 1.13,2.17 -0.08,3.1 -2.91,2.89 -5.19,2.83 -2.22,-0.05 -5.04,-0.17 -4.96,-3.1 0.02,-1 0.49,-1.85 1.43,-2.23 v -0.04 l -1.18,-0.03 z m 8.12,4.19 c 0.03,-1.02 -1.03,-1.19 -3.17,-1.24 -2.22,-0.05 -3.48,0.01 -3.51,1.05 -0.03,1.06 0.71,1.26 3.79,1.33 0.94,0.03 2.85,0.22 2.89,-1.14 z"
       id="path5005" />
    	</g>
    	<g
       class="st5"
       id="g5011">
    		<path
       class="st2"
       d="m 882.43,684.54 -6.96,0.18 c -0.9,0.02 -1.6,0.2 -1.57,1.1 0.02,0.9 0.73,1.04 1.63,1.02 l 6.96,-0.18 0.07,2.82 -14.44,0.38 -0.07,-2.82 5.36,-0.14 v -0.04 c -0.47,-0.27 -0.78,-0.6 -0.97,-0.98 -0.21,-0.39 -0.3,-0.85 -0.31,-1.37 -0.04,-1.34 0.73,-2.54 2.13,-2.58 l 8.1,-0.21 z"
       id="path5009" />
    	</g>
    	<g
       class="st5"
       id="g5015">
    		<path
       class="st2"
       d="m 872.2,681.42 -0.09,-1.14 -1.59,0.12 -1.47,-2.72 2.85,-0.22 -0.11,-1.46 1.74,-0.13 0.11,1.46 5.38,-0.42 c 0.76,-0.06 1.26,-0.08 1.19,-1 -0.01,-0.18 -0.03,-0.36 -0.08,-0.5 l 1.74,-0.13 c 0.07,0.38 0.16,0.77 0.21,1.45 0.19,2.43 -1.4,2.88 -2.02,2.93 l -6.2,0.48 0.09,1.14 z"
       id="path5013" />
    	</g>
    	<g
       class="st5"
       id="g5019">
    		<path
       class="st2"
       d="m 878.29,672.07 c 0.46,-0.03 0.89,-0.09 1.2,-0.26 0.3,-0.19 0.43,-0.51 0.37,-1.06 -0.06,-0.56 -0.46,-1 -1.14,-0.93 -2.13,0.22 -1.14,5.11 -4.35,5.44 -2.17,0.22 -3.05,-1.86 -3.23,-3.67 -0.2,-1.91 0.54,-3.74 2.72,-3.8 l 0.29,2.75 c -0.7,0.07 -1.11,0.2 -1.27,0.41 -0.16,0.2 -0.18,0.44 -0.14,0.74 0.06,0.62 0.5,0.91 1.17,0.84 1.59,-0.16 1,-5.09 4.22,-5.42 1.75,-0.18 3.21,1.12 3.45,3.44 0.25,2.45 -0.19,4.14 -3.02,4.27 z"
       id="path5017" />
    	</g>
    	<path
       class="st54"
       d="m 917.92,782.65 c -0.64,-1.22 -1.1,-2.53 -1.39,-3.93 -0.16,-0.79 -0.93,-1.3 -1.72,-1.14 -0.79,0.16 -1.3,0.93 -1.14,1.72 0.4,1.93 1.08,3.73 2.03,5.36 0.51,-0.89 1.29,-1.6 2.22,-2.01 z"
       id="path5021" />
    	<path
       class="st54"
       d="m 928.16,790.34 c -1.4,-0.29 -2.72,-0.76 -3.94,-1.4 -0.42,0.94 -1.13,1.72 -2.02,2.23 1.64,0.95 3.45,1.64 5.38,2.04 0.1,0.02 0.2,0.03 0.29,0.03 0.68,0 1.29,-0.48 1.43,-1.17 0.16,-0.79 -0.35,-1.57 -1.14,-1.73 z"
       id="path5023" />
    	<path
       class="st54"
       d="m 934.13,761.12 c 1.39,0.28 2.71,0.75 3.92,1.39 0.42,-0.94 1.14,-1.71 2.03,-2.22 -1.64,-0.94 -3.45,-1.63 -5.37,-2.03 -0.79,-0.16 -1.56,0.35 -1.72,1.14 -0.16,0.79 0.34,1.56 1.14,1.72 z"
       id="path5025" />
    	<path
       class="st54"
       d="m 944.35,768.82 c 0.64,1.22 1.12,2.54 1.4,3.93 0.14,0.69 0.75,1.17 1.43,1.17 0.09,0 0.19,-0.01 0.29,-0.03 0.79,-0.16 1.3,-0.93 1.14,-1.71 -0.39,-1.93 -1.09,-3.74 -2.04,-5.39 -0.5,0.89 -1.28,1.6 -2.22,2.03 z"
       id="path5027" />
    	<path
       class="st54"
       d="m 914.81,773.89 c 0.1,0.02 0.2,0.03 0.29,0.03 0.68,0 1.28,-0.47 1.43,-1.17 0.28,-1.39 0.75,-2.69 1.37,-3.9 -0.94,-0.41 -1.73,-1.11 -2.24,-1.98 -0.93,1.62 -1.61,3.41 -1.99,5.31 -0.16,0.78 0.35,1.55 1.14,1.71 z"
       id="path5029" />
    	<path
       class="st54"
       d="m 924.16,762.55 c 1.23,-0.66 2.58,-1.14 4,-1.43 0.79,-0.16 1.3,-0.93 1.14,-1.72 -0.16,-0.79 -0.93,-1.3 -1.72,-1.14 -1.94,0.39 -3.77,1.1 -5.42,2.05 0.88,0.51 1.59,1.3 2,2.24 z"
       id="path5031" />
    	<path
       class="st54"
       d="m 938.05,788.96 c -1.21,0.63 -2.53,1.1 -3.92,1.39 -0.8,0.16 -1.3,0.93 -1.15,1.72 0.15,0.69 0.75,1.17 1.43,1.17 0.09,0 0.2,-0.01 0.29,-0.03 1.93,-0.39 3.74,-1.09 5.37,-2.03 -0.88,-0.51 -1.61,-1.28 -2.02,-2.22 z"
       id="path5033" />
    	<path
       class="st54"
       d="m 947.47,777.58 c -0.79,-0.16 -1.56,0.35 -1.72,1.14 -0.28,1.39 -0.76,2.71 -1.4,3.93 0.94,0.42 1.72,1.13 2.23,2.03 0.95,-1.64 1.64,-3.45 2.04,-5.39 0.15,-0.78 -0.36,-1.55 -1.15,-1.71 z"
       id="path5035" />
    	<path
       class="st54"
       d="m 918.66,767.57 c 0.35,0.13 0.73,0.2 1.13,0.2 1.83,0 3.31,-1.49 3.31,-3.32 0,-0.41 -0.07,-0.79 -0.2,-1.15 -0.36,-0.99 -1.17,-1.75 -2.2,-2.04 -0.28,-0.08 -0.59,-0.12 -0.91,-0.12 -1.83,0 -3.32,1.48 -3.32,3.31 0,0.33 0.05,0.64 0.14,0.94 0.3,1.02 1.06,1.83 2.05,2.18 z"
       id="path5037" />
    	<path
       class="st54"
       d="m 939.09,764.45 c 0,1.83 1.49,3.32 3.32,3.32 0.42,0 0.83,-0.08 1.2,-0.23 0.99,-0.38 1.74,-1.21 2.01,-2.25 0.07,-0.27 0.11,-0.55 0.11,-0.85 0,-1.83 -1.48,-3.31 -3.31,-3.31 -0.3,0 -0.58,0.04 -0.85,0.11 -1.03,0.28 -1.86,1.03 -2.24,2.01 -0.16,0.38 -0.24,0.78 -0.24,1.2 z"
       id="path5039" />
    	<path
       class="st54"
       d="m 923.17,787.02 c 0,-1.83 -1.49,-3.32 -3.32,-3.32 -0.42,0 -0.81,0.07 -1.17,0.22 -0.99,0.37 -1.74,1.2 -2.02,2.23 -0.07,0.28 -0.12,0.57 -0.12,0.88 0,1.83 1.48,3.31 3.31,3.31 0.3,0 0.59,-0.04 0.87,-0.12 1.03,-0.28 1.86,-1.03 2.23,-2.01 0.14,-0.38 0.22,-0.78 0.22,-1.19 z"
       id="path5041" />
    	<path
       class="st54"
       d="m 943.61,783.92 c -0.37,-0.15 -0.77,-0.23 -1.2,-0.23 -1.83,0 -3.32,1.49 -3.32,3.32 0,0.42 0.08,0.82 0.23,1.2 0.38,0.98 1.21,1.73 2.24,2.01 0.27,0.07 0.55,0.11 0.85,0.11 1.83,0 3.31,-1.48 3.31,-3.31 0,-0.29 -0.04,-0.58 -0.11,-0.85 -0.27,-1.04 -1.02,-1.87 -2,-2.25 z"
       id="path5043" />
    	<path
       class="st54"
       d="m 931.13,781.57 c -3.09,0 -5.62,-2.42 -5.82,-5.46 l 0.62,0.71 c 0.22,0.25 0.52,0.37 0.82,0.37 0.26,0 0.51,-0.09 0.72,-0.27 0.46,-0.4 0.5,-1.09 0.1,-1.55 l -2.56,-2.92 c -0.21,-0.24 -0.51,-0.37 -0.82,-0.37 -0.31,0 -0.62,0.14 -0.82,0.37 l -2.56,2.92 c -0.4,0.46 -0.35,1.15 0.1,1.55 0.46,0.4 1.15,0.35 1.54,-0.1 l 0.66,-0.75 c 0.18,4.27 3.7,7.69 8.01,7.69 0.6,0 1.09,-0.49 1.09,-1.09 0.01,-0.61 -0.48,-1.1 -1.08,-1.1 z"
       id="path5045" />
    	<path
       class="st54"
       d="m 931.13,769.9 c 3.09,0 5.62,2.42 5.82,5.46 l -0.62,-0.71 c -0.4,-0.46 -1.09,-0.5 -1.55,-0.1 -0.45,0.4 -0.5,1.09 -0.1,1.55 l 2.56,2.92 c 0.21,0.24 0.51,0.37 0.82,0.37 0.32,0 0.62,-0.14 0.82,-0.37 l 2.56,-2.92 c 0.4,-0.46 0.35,-1.15 -0.1,-1.54 -0.45,-0.4 -1.15,-0.35 -1.55,0.1 l -0.66,0.75 c -0.18,-4.27 -3.7,-7.69 -8.01,-7.69 -0.61,0 -1.1,0.49 -1.1,1.1 0.01,0.58 0.5,1.08 1.11,1.08 z"
       id="path5047" />
    	<g
       class="st5"
       id="g5115">
    		<path
       class="st55"
       d="m 517.52,116.5 c 0,-3.82 0,-7.46 4.98,-7.46 3.08,0 4.32,1.7 4.2,4.8 h -2.96 c 0,-1.92 -0.34,-2.64 -1.24,-2.64 -1.7,0 -1.92,1.6 -1.92,5.3 0,3.7 0.22,5.3 1.92,5.3 1.4,0 1.34,-1.8 1.38,-2.94 h 2.98 c 0,3.86 -1.54,5.1 -4.36,5.1 -4.98,0.01 -4.98,-3.67 -4.98,-7.46 z"
       id="path5049" />
    		<path
       class="st55"
       d="m 533.58,123.73 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -14.44 h 2.82 v 5.36 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 z"
       id="path5051" />
    		<path
       class="st55"
       d="m 541.7,109.28 v 2.22 h -2.82 v -2.22 z m 0,14.45 h -2.82 v -10.1 h 2.82 z"
       id="path5053" />
    		<path
       class="st55"
       d="m 547.26,109.28 v 14.44 h -2.82 v -14.44 z"
       id="path5055" />
    		<path
       class="st55"
       d="m 554.8,123.73 v -1.12 h -0.04 c -0.52,0.98 -1.3,1.32 -2.38,1.32 -2.92,0 -2.82,-3.24 -2.82,-5.32 0,-2.04 -0.08,-5.18 2.76,-5.18 1.02,0 1.72,0.3 2.3,1.16 h 0.04 v -5.3 h 2.82 v 14.44 h -2.68 z m -0.14,-5.14 c 0,-2.02 0.02,-3.42 -1.14,-3.42 -1.22,0 -1.2,1.4 -1.2,3.42 0,2.54 0.18,3.6 1.2,3.6 0.96,0 1.14,-1.06 1.14,-3.6 z"
       id="path5057" />
    		<path
       class="st55"
       d="m 567.3,123.73 h -3.02 v -14.44 h 5.58 c 2.06,0 3.38,1.32 3.38,3.78 0,1.84 -0.72,3.22 -2.68,3.54 v 0.04 c 0.66,0.08 2.62,0.24 2.62,2.84 0,0.92 0.06,3.64 0.34,4.24 h -2.96 c -0.4,-0.88 -0.32,-1.86 -0.32,-2.8 0,-1.72 0.16,-3.18 -2.16,-3.18 h -0.78 v 5.98 z m 0,-8.21 h 1.34 c 1.2,0 1.54,-1.2 1.54,-2.12 0,-1.38 -0.58,-1.9 -1.54,-1.9 h -1.34 z"
       id="path5059" />
    		<path
       class="st55"
       d="m 578.38,109.28 v 2.22 h -2.82 v -2.22 z m 0,14.45 h -2.82 v -10.1 h 2.82 z"
       id="path5061" />
    		<path
       class="st55"
       d="m 588.6,113.62 v 10.52 c 0,0.7 0.04,3.46 -3.84,3.46 -2.1,0 -3.9,-0.54 -3.96,-3 h 2.76 c 0,0.42 0.06,0.78 0.24,1.02 0.18,0.26 0.5,0.4 0.94,0.4 0.7,0 1.04,-0.66 1.04,-1.68 v -1.94 h -0.04 c -0.42,0.78 -1.22,1.18 -2.14,1.18 -3.1,0 -2.96,-2.84 -2.96,-5.12 0,-2.22 0.04,-5.04 2.98,-5.04 1,0 1.86,0.44 2.26,1.38 h 0.04 v -1.18 h 2.68 z m -3.98,8.23 c 1.02,0 1.16,-1.06 1.16,-3.2 0,-2.22 -0.1,-3.48 -1.14,-3.48 -1.06,0 -1.24,0.74 -1.24,3.82 0,0.94 -0.14,2.86 1.22,2.86 z"
       id="path5063" />
    		<path
       class="st55"
       d="m 595.82,123.73 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -14.44 h 2.82 v 5.36 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 z"
       id="path5065" />
    		<path
       class="st55"
       d="m 599.74,113.62 h 1.14 v -1.6 l 2.82,-1.26 v 2.86 h 1.46 v 1.74 h -1.46 v 5.4 c 0,0.76 -0.02,1.26 0.9,1.26 0.18,0 0.36,0 0.5,-0.04 v 1.74 c -0.38,0.04 -0.78,0.1 -1.46,0.1 -2.44,0 -2.76,-1.62 -2.76,-2.24 v -6.22 h -1.14 z"
       id="path5067" />
    		<path
       class="st55"
       d="m 608.66,120.49 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path5069" />
    		<path
       class="st55"
       d="m 619.92,123.73 v -14.44 h 3.02 v 12.04 h 4.52 v 2.4 h -7.54 z"
       id="path5071" />
    		<path
       class="st55"
       d="m 636.3,121.85 c 0,0.62 0.08,1.26 0.14,1.88 h -2.62 l -0.12,-1.34 h -0.04 c -0.6,1.04 -1.42,1.54 -2.64,1.54 -1.96,0 -2.68,-1.46 -2.68,-3.22 0,-3.34 2.58,-3.48 5.2,-3.44 v -0.78 c 0,-0.86 -0.12,-1.48 -1.14,-1.48 -0.98,0 -1.06,0.74 -1.06,1.54 h -2.76 c 0,-1.22 0.38,-2 1.04,-2.46 0.64,-0.48 1.56,-0.66 2.64,-0.66 3.58,0 4.04,1.54 4.04,3.38 v 5.04 z m -5.2,-1.26 c 0,0.72 0.12,1.6 1.04,1.6 1.66,0 1.4,-2.24 1.4,-3.34 -1.4,0.06 -2.44,-0.06 -2.44,1.74 z"
       id="path5073" />
    		<path
       class="st55"
       d="m 641.46,114.64 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 h -2.82 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -10.1 h 2.82 z"
       id="path5075" />
    		<path
       class="st55"
       d="m 653.68,123.73 v -1.12 h -0.04 c -0.52,0.98 -1.3,1.32 -2.38,1.32 -2.92,0 -2.82,-3.24 -2.82,-5.32 0,-2.04 -0.08,-5.18 2.76,-5.18 1.02,0 1.72,0.3 2.3,1.16 h 0.04 v -5.3 h 2.82 v 14.44 h -2.68 z m -0.14,-5.14 c 0,-2.02 0.02,-3.42 -1.14,-3.42 -1.22,0 -1.2,1.4 -1.2,3.42 0,2.54 0.18,3.6 1.2,3.6 0.96,0 1.14,-1.06 1.14,-3.6 z"
       id="path5077" />
    		<path
       class="st55"
       d="m 660.86,120.49 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path5079" />
    		<path
       class="st55"
       d="m 672.66,117.23 c 0,-1.5 -0.38,-2 -1.26,-2 -1.2,0 -1.3,1.06 -1.3,3.16 0,3.08 0.26,3.74 1.3,3.74 0.88,0 1.3,-0.8 1.3,-2.12 h 2.82 c 0,2.74 -1.48,3.92 -4.12,3.92 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 2.6,0 4.08,1.16 4.08,3.8 h -2.82 z"
       id="path5081" />
    		<path
       class="st55"
       d="m 685.18,121.85 c 0,0.62 0.08,1.26 0.14,1.88 h -2.62 l -0.12,-1.34 h -0.04 c -0.6,1.04 -1.42,1.54 -2.64,1.54 -1.96,0 -2.68,-1.46 -2.68,-3.22 0,-3.34 2.58,-3.48 5.2,-3.44 v -0.78 c 0,-0.86 -0.12,-1.48 -1.14,-1.48 -0.98,0 -1.06,0.74 -1.06,1.54 h -2.76 c 0,-1.22 0.38,-2 1.04,-2.46 0.64,-0.48 1.56,-0.66 2.64,-0.66 3.58,0 4.04,1.54 4.04,3.38 v 5.04 z m -5.2,-1.26 c 0,0.72 0.12,1.6 1.04,1.6 1.66,0 1.4,-2.24 1.4,-3.34 -1.4,0.06 -2.44,-0.06 -2.44,1.74 z"
       id="path5083" />
    		<path
       class="st55"
       d="m 690.2,113.62 v 1.12 h 0.04 c 0.52,-0.98 1.3,-1.32 2.38,-1.32 2.92,0 2.82,3.24 2.82,5.32 0,2.04 0.08,5.18 -2.76,5.18 -1.02,0 -1.72,-0.3 -2.3,-1.16 h -0.04 v 5.3 h -2.82 v -14.44 h 2.68 z m 2.48,4.97 c 0,-2.02 0.02,-3.42 -1.2,-3.42 -1.16,0 -1.14,1.4 -1.14,3.42 0,2.54 0.18,3.6 1.14,3.6 1.02,0 1.2,-1.06 1.2,-3.6 z"
       id="path5085" />
    		<path
       class="st55"
       d="m 700.12,119.13 c 0,1.2 0.04,3 1.28,3 1,0 1.2,-0.96 1.2,-1.8 h 2.86 c -0.04,1.1 -0.4,2 -1.08,2.62 -0.66,0.62 -1.66,0.98 -2.98,0.98 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 3.8,0 4.22,2.46 4.12,5.7 h -5.4 z m 2.58,-1.59 c 0,-0.98 0.04,-2.38 -1.3,-2.38 -1.3,0 -1.28,1.52 -1.28,2.38 z"
       id="path5087" />
    		<path
       class="st55"
       d="m 719.62,121.85 c 0,0.62 0.08,1.26 0.14,1.88 h -2.62 l -0.12,-1.34 h -0.04 c -0.6,1.04 -1.42,1.54 -2.64,1.54 -1.96,0 -2.68,-1.46 -2.68,-3.22 0,-3.34 2.58,-3.48 5.2,-3.44 v -0.78 c 0,-0.86 -0.12,-1.48 -1.14,-1.48 -0.98,0 -1.06,0.74 -1.06,1.54 h -2.76 c 0,-1.22 0.38,-2 1.04,-2.46 0.64,-0.48 1.56,-0.66 2.64,-0.66 3.58,0 4.04,1.54 4.04,3.38 v 5.04 z m -5.2,-1.26 c 0,0.72 0.12,1.6 1.04,1.6 1.66,0 1.4,-2.24 1.4,-3.34 -1.4,0.06 -2.44,-0.06 -2.44,1.74 z"
       id="path5089" />
    		<path
       class="st55"
       d="m 724.78,114.64 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 h -2.82 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -10.1 h 2.82 z"
       id="path5091" />
    		<path
       class="st55"
       d="m 737,123.73 v -1.12 h -0.04 c -0.52,0.98 -1.3,1.32 -2.38,1.32 -2.92,0 -2.82,-3.24 -2.82,-5.32 0,-2.04 -0.08,-5.18 2.76,-5.18 1.02,0 1.72,0.3 2.3,1.16 h 0.04 v -5.3 h 2.82 v 14.44 H 737 Z m -0.14,-5.14 c 0,-2.02 0.02,-3.42 -1.14,-3.42 -1.22,0 -1.2,1.4 -1.2,3.42 0,2.54 0.18,3.6 1.2,3.6 0.96,0 1.14,-1.06 1.14,-3.6 z"
       id="path5093" />
    		<path
       class="st55"
       d="m 753.14,113.72 c 0.02,-1.34 -0.2,-2.52 -1.8,-2.52 -1.88,0 -1.88,2.54 -1.88,5.34 0,4.52 0.44,5.32 2.16,5.32 0.5,0 1.04,-0.12 1.5,-0.28 v -3.2 h -1.64 v -2.22 h 4.66 v 7.32 c -0.82,0.16 -2.88,0.48 -4.08,0.48 -5.08,0 -5.66,-2.1 -5.66,-7.58 0,-3.64 0.18,-7.34 5.12,-7.34 2.96,0 4.8,1.66 4.62,4.68 h -3 z"
       id="path5095" />
    		<path
       class="st55"
       d="m 758.38,118.55 c 0,-2.76 0.4,-5.12 4.12,-5.12 3.72,0 4.12,2.36 4.12,5.12 0,3.16 -0.48,5.38 -4.12,5.38 -3.64,0 -4.12,-2.22 -4.12,-5.38 z m 5.42,-0.16 c 0,-2.1 -0.1,-3.16 -1.3,-3.16 -1.2,0 -1.3,1.06 -1.3,3.16 0,3.08 0.26,3.74 1.3,3.74 1.04,0 1.3,-0.66 1.3,-3.74 z"
       id="path5097" />
    		<path
       class="st55"
       d="m 767.66,113.62 h 2.86 l 1.42,7.58 h 0.04 l 1.48,-7.58 h 2.76 l -2.78,10.1 h -3.1 z"
       id="path5099" />
    		<path
       class="st55"
       d="m 780.1,119.13 c 0,1.2 0.04,3 1.28,3 1,0 1.2,-0.96 1.2,-1.8 h 2.86 c -0.04,1.1 -0.4,2 -1.08,2.62 -0.66,0.62 -1.66,0.98 -2.98,0.98 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 3.8,0 4.22,2.46 4.12,5.7 h -5.4 z m 2.58,-1.59 c 0,-0.98 0.04,-2.38 -1.3,-2.38 -1.3,0 -1.28,1.52 -1.28,2.38 z"
       id="path5101" />
    		<path
       class="st55"
       d="m 790.18,113.62 v 1.3 h 0.04 c 0.52,-1.16 1.48,-1.5 2.62,-1.5 v 2.52 c -2.48,-0.16 -2.52,1.28 -2.52,2.28 v 5.5 h -2.82 v -10.1 z"
       id="path5103" />
    		<path
       class="st55"
       d="m 796.98,114.64 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 h -2.82 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -10.1 h 2.82 z"
       id="path5105" />
    		<path
       class="st55"
       d="m 811.82,121.85 c 0,0.62 0.08,1.26 0.14,1.88 h -2.62 l -0.12,-1.34 h -0.04 c -0.6,1.04 -1.42,1.54 -2.64,1.54 -1.96,0 -2.68,-1.46 -2.68,-3.22 0,-3.34 2.58,-3.48 5.2,-3.44 v -0.78 c 0,-0.86 -0.12,-1.48 -1.14,-1.48 -0.98,0 -1.06,0.74 -1.06,1.54 h -2.76 c 0,-1.22 0.38,-2 1.04,-2.46 0.64,-0.48 1.56,-0.66 2.64,-0.66 3.58,0 4.04,1.54 4.04,3.38 v 5.04 z m -5.2,-1.26 c 0,0.72 0.12,1.6 1.04,1.6 1.66,0 1.4,-2.24 1.4,-3.34 -1.4,0.06 -2.44,-0.06 -2.44,1.74 z"
       id="path5107" />
    		<path
       class="st55"
       d="m 816.98,114.64 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 h -2.82 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -10.1 h 2.82 z"
       id="path5109" />
    		<path
       class="st55"
       d="m 829.3,117.23 c 0,-1.5 -0.38,-2 -1.26,-2 -1.2,0 -1.3,1.06 -1.3,3.16 0,3.08 0.26,3.74 1.3,3.74 0.88,0 1.3,-0.8 1.3,-2.12 h 2.82 c 0,2.74 -1.48,3.92 -4.12,3.92 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 2.6,0 4.08,1.16 4.08,3.8 h -2.82 z"
       id="path5111" />
    		<path
       class="st55"
       d="m 836.76,119.13 c 0,1.2 0.04,3 1.28,3 1,0 1.2,-0.96 1.2,-1.8 h 2.86 c -0.04,1.1 -0.4,2 -1.08,2.62 -0.66,0.62 -1.66,0.98 -2.98,0.98 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 3.8,0 4.22,2.46 4.12,5.7 h -5.4 z m 2.58,-1.59 c 0,-0.98 0.04,-2.38 -1.3,-2.38 -1.3,0 -1.28,1.52 -1.28,2.38 z"
       id="path5113" />
    	</g>
    	<a
       id="a6399"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#demography"
       target="blank"
       xlink:title="Demographics"><g
         class="st5"
         id="g5141">
    		<path
       class="st55"
       d="m 30.99,276.62 h 4 c 1.66,0 2.84,0.59 3.49,1.98 0.52,1.1 0.58,3.69 0.58,4.11 0,2.77 -0.25,4.38 -0.79,5.24 -0.7,1.12 -2.02,1.67 -4.29,1.67 h -2.99 v -13 z m 1.66,11.56 h 1.57 c 2.3,0 3.15,-0.86 3.15,-3.89 v -2.63 c 0,-2.63 -0.81,-3.6 -2.54,-3.6 h -2.18 z"
       id="path5117" />
    		<path
       class="st55"
       d="m 43.23,285.56 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5119" />
    		<path
       class="st55"
       d="m 55.26,289.62 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 H 59.8 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.48 z"
       id="path5121" />
    		<path
       class="st55"
       d="m 63.54,285.21 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path5123" />
    		<path
       class="st55"
       d="m 77.6,280.53 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.09,-3.45 -1.76,-3.45 z"
       id="path5125" />
    		<path
       class="st55"
       d="m 83.32,281.9 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5127" />
    		<path
       class="st55"
       d="m 92.46,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5129" />
    		<path
       class="st55"
       d="m 98.39,281.61 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 H 98.4 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path5131" />
    		<path
       class="st55"
       d="m 110.72,289.62 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5133" />
    		<path
       class="st55"
       d="m 114.66,276.62 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5135" />
    		<path
       class="st55"
       d="m 123.53,283.45 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5137" />
    		<path
       class="st55"
       d="m 130.46,289.8 c -1.96,0 -3.19,-0.86 -3.13,-2.95 H 129 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5139" />
    	</g></a>
    	<path
       class="st56"
       d="m 25.02,276.3 c -4.35,0.61 -7.75,2.51 -8.74,4.92"
       id="path5143" />
    	<line
       class="st57"
       x1="16"
       y1="285.48001"
       x2="16"
       y2="303.73999"
       id="line5145" />
    	<path
       class="st56"
       d="m 17.07,307.86 c 1.69,2.04 5.23,3.52 9.44,3.81"
       id="path5147" />
    	<line
       class="st58"
       x1="30.940001"
       y1="311.72"
       x2="135.63"
       y2="311.72"
       id="line5149" />
    	<path
       class="st56"
       d="m 140.08,311.52 c 4.35,-0.61 7.74,-2.51 8.73,-4.92"
       id="path5151" />
    	<line
       class="st57"
       x1="149.11"
       y1="302.34"
       x2="149.11"
       y2="284.07999"
       id="line5153" />
    	<path
       class="st56"
       d="m 148.04,279.96 c -1.69,-2.04 -5.23,-3.52 -9.44,-3.81"
       id="path5155" />
    	<line
       class="st58"
       x1="134.16"
       y1="276.10001"
       x2="29.469999"
       y2="276.10001"
       id="line5157" />
    	<path
       class="st59"
       d="m 16,282.67 v 0 m 0,22.48 v 0 m 12,6.57 v 0 m 109.11,0 v 0 m 12,-6.57 v 0 m 0,-22.48 v 0 m -12,-6.57 v 0 M 28,276.1 v 0"
       id="path5159" />
    	<a
       id="a7960"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#demography"
       target="blank"
       xlink:title="Demographics"><path
         class="st55"
         d="m 71.65,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.89,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.19,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.39,10.9 12.71,10.57 z"
         id="path5161" /></a>
    	<a
       id="a7963"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#demography"
       target="blank"
       xlink:title="Demographics"><path
         class="st54"
         d="m 98.41,205.04 -3.28,-2.31 -7.82,11.12 -6.18,-4.66 -5.36,7.27 c -0.26,0.35 -0.66,0.54 -1.07,0.54 -0.28,0 -0.55,-0.08 -0.79,-0.26 -0.59,-0.44 -0.72,-1.27 -0.28,-1.86 l 6.95,-9.43 6.13,4.62 6.23,-8.87 -3.23,-2.27 9.63,-4.47 -0.93,10.58 z M 70.42,182.02 c -0.93,0 -1.68,0.75 -1.68,1.68 0,0.93 0.75,1.68 1.68,1.68 0.93,0 1.68,-0.75 1.68,-1.68 0,-0.93 -0.75,-1.68 -1.68,-1.68 z m -0.2,13.19 -0.34,6.2 c 0,0.22 -0.18,0.4 -0.4,0.4 -0.22,0 -0.39,-0.18 -0.39,-0.4 l -0.34,-6.2 h -1.1 l 1.14,-6.96 -2.29,4.55 c -0.08,0.2 -0.32,0.3 -0.52,0.21 -0.2,-0.09 -0.29,-0.32 -0.21,-0.52 0,0 1.68,-4.53 2.09,-5.37 0.41,-0.84 0.82,-1.35 2.39,-1.35 h 0.32 c 1.57,0 1.98,0.51 2.39,1.35 0.42,0.84 2.09,5.37 2.09,5.37 0.09,0.2 -0.01,0.43 -0.21,0.52 -0.2,0.09 -0.43,-0.01 -0.52,-0.21 l -2.28,-4.55 1.13,6.96 h -1.1 l -0.34,6.2 c 0,0.22 -0.18,0.4 -0.39,0.4 -0.22,0 -0.39,-0.18 -0.39,-0.4 l -0.36,-6.2 h -0.37 z m 15.47,-11.52 c 0,0.93 -0.75,1.68 -1.68,1.68 -0.93,0 -1.69,-0.75 -1.69,-1.68 0,-0.93 0.75,-1.68 1.69,-1.68 0.93,0 1.68,0.75 1.68,1.68 z m 0.06,8.22 0.33,9.2 c 0.02,0.36 -0.25,0.68 -0.61,0.7 -0.02,0 -0.03,0 -0.05,0 -0.34,0 -0.64,-0.26 -0.66,-0.61 l -0.75,-7.11 -0.75,7.11 c -0.03,0.35 -0.32,0.61 -0.66,0.61 -0.01,0 -0.03,0 -0.05,0 -0.36,-0.03 -0.64,-0.34 -0.61,-0.7 l 0.32,-9.2 -0.11,-3.66 -2.05,4.55 c -0.08,0.2 -0.32,0.3 -0.52,0.21 -0.2,-0.09 -0.29,-0.32 -0.21,-0.52 0,0 1.45,-4.52 1.86,-5.37 0.41,-0.84 1.05,-1.35 2.62,-1.35 h 0.32 c 1.57,0 2.21,0.51 2.62,1.35 0.41,0.84 1.86,5.37 1.86,5.37 0.09,0.2 -0.01,0.43 -0.21,0.52 -0.2,0.08 -0.43,-0.01 -0.52,-0.21 l -2.05,-4.55 -0.12,3.66 v 0 z m -7.5,1.36 c 0,0.57 -0.46,1.03 -1.03,1.03 -0.57,0 -1.03,-0.46 -1.03,-1.03 0,-0.57 0.46,-1.03 1.03,-1.03 0.56,-0.01 1.03,0.45 1.03,1.03 z m -1.04,5.04 -0.46,3.23 c -0.06,0.16 -0.21,0.27 -0.39,0.27 -0.19,0 -0.34,-0.12 -0.4,-0.29 0,-0.01 -0.02,-0.2 0,-0.23 l 0.19,-3.97 -0.06,-1.36 c -0.05,-0.46 -0.06,-0.33 -0.59,-0.64 -0.54,-0.32 -1.45,-1.74 -1.5,-1.81 -0.04,-0.07 -0.13,-0.2 -0.14,-0.28 -0.03,-0.14 0.07,-0.28 0.21,-0.31 0.11,-0.02 0.2,0.04 0.26,0.11 0.07,0.08 1.13,1.48 1.91,1.61 0.18,-0.03 0.37,-0.12 0.87,-0.12 h 0.2 c 0.5,0 0.69,0.09 0.87,0.12 0.79,-0.13 1.84,-1.54 1.91,-1.61 0.07,-0.07 0.16,-0.13 0.26,-0.11 0.14,0.03 0.24,0.16 0.21,0.31 -0.02,0.08 -0.1,0.2 -0.14,0.28 -0.04,0.07 -0.96,1.48 -1.5,1.81 -0.53,0.31 -0.53,0.18 -0.59,0.64 l -0.06,1.36 0.19,3.97 c 0.01,0.03 0,0.22 0,0.23 -0.06,0.17 -0.21,0.29 -0.4,0.29 -0.18,0 -0.33,-0.11 -0.39,-0.27 0.01,0 -0.46,-3.23 -0.46,-3.23"
         id="path5163" /></a>
    	<line
       class="st60"
       x1="82.550003"
       y1="244.49001"
       x2="82.550003"
       y2="260.76999"
       id="line5165" />
    	<path
       class="st61"
       d="m 82.55,241.53 v 0 m 0,20.72 v 0"
       id="path5167" />
    	<path
       d="m 82.55,244.31 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.25,2.78 2.78,2.78 z"
       id="path5169" />
    	<g
       class="st5"
       id="g5195">
    		<path
       class="st55"
       d="m 372.92,289.62 h -1.55 v -13 h 2.68 l 3.28,10.91 h 0.04 l 3.31,-10.91 h 2.74 v 13 h -1.66 v -11.56 h -0.04 l -3.64,11.56 h -1.57 l -3.56,-11.56 h -0.04 v 11.56 z"
       id="path5171" />
    		<path
       class="st55"
       d="m 386.05,276.62 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5173" />
    		<path
       class="st55"
       d="m 394.98,280.53 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 H 395 v -1.1 z m -1.72,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.09,-3.45 -1.76,-3.45 z"
       id="path5175" />
    		<path
       class="st55"
       d="m 400.71,281.9 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path5177" />
    		<path
       class="st55"
       d="m 409.85,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5179" />
    		<path
       class="st55"
       d="m 414.33,280.53 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5181" />
    		<path
       class="st55"
       d="m 419.05,276.62 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5183" />
    		<path
       class="st55"
       d="m 422.92,285.21 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path5185" />
    		<path
       class="st55"
       d="m 437.1,289.62 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5187" />
    		<path
       class="st55"
       d="m 449.85,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5189" />
    		<path
       class="st55"
       d="m 459.1,289.62 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5191" />
    		<path
       class="st55"
       d="m 467.97,276.62 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5193" />
    	</g>
    	<g
       class="st5"
       id="g5221">
    		<path
       class="st55"
       d="m 377.99,298.23 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5197" />
    		<path
       class="st55"
       d="m 382.06,298.23 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5199" />
    		<path
       class="st55"
       d="m 388.87,311.41 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 -0.01,2 -1.37,2.78 -3.17,2.78 z"
       id="path5201" />
    		<path
       class="st55"
       d="m 395.78,303.21 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.32 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0 1.8,-1.24 1.8,-3.67 z"
       id="path5203" />
    		<path
       class="st55"
       d="m 404.61,311.23 h -1.48 v -13 h 1.48 z"
       id="path5205" />
    		<path
       class="st55"
       d="m 411.85,309.91 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path5207" />
    		<path
       class="st55"
       d="m 420.92,305.05 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5209" />
    		<path
       class="st55"
       d="m 426.61,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5211" />
    		<path
       class="st55"
       d="m 438.64,311.23 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5213" />
    		<path
       class="st55"
       d="m 448.61,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5215" />
    		<path
       class="st55"
       d="m 461.1,311.23 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5217" />
    		<path
       class="st55"
       d="m 465.33,302.13 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5219" />
    	</g>
    	<path
       class="st62"
       d="m 363.28,276.5 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5223" />
    	<line
       class="st63"
       x1="354.39001"
       y1="291"
       x2="354.39001"
       y2="298.26999"
       id="line5225" />
    	<path
       class="st62"
       d="m 354.8,302.83 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5227" />
    	<line
       class="st58"
       x1="369.34"
       y1="311.72"
       x2="474.01999"
       y2="311.72"
       id="line5229" />
    	<path
       class="st62"
       d="m 478.61,311.32 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5231" />
    	<line
       class="st63"
       x1="487.5"
       y1="296.82001"
       x2="487.5"
       y2="289.54999"
       id="line5233" />
    	<path
       class="st62"
       d="m 487.09,284.99 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5235" />
    	<line
       class="st58"
       x1="472.54999"
       y1="276.10001"
       x2="367.85999"
       y2="276.10001"
       id="line5237" />
    	<path
       class="st59"
       d="m 354.39,288.1 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5239" />
    	<path
       class="st55"
       d="m 410.04,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.2,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.39,10.9 12.71,10.57 z"
       id="path5241" />
    	<path
       class="st54"
       d="m 425.26,187.08 c -0.51,-1.56 -2.19,-2.41 -3.76,-1.9 -1.56,0.51 -2.41,2.2 -1.9,3.76 0.51,1.56 2.2,2.41 3.76,1.9 1.56,-0.52 2.41,-2.2 1.9,-3.76 z"
       id="path5243" />
    	<path
       class="st54"
       d="m 418.52,202.52 2.92,-5.79 c 0.9,-1.78 0.18,-3.95 -1.6,-4.85 l -1.9,-0.96 c -0.1,-0.05 -0.21,-0.09 -0.32,-0.11 -5.06,-2.22 -11.06,-0.15 -13.61,4.84 -0.39,0.76 -0.09,1.68 0.67,2.07 0.76,0.39 1.68,0.09 2.07,-0.67 1.47,-2.87 4.55,-4.38 7.59,-4 l -11.07,21.71 c -0.39,0.76 -0.09,1.7 0.68,2.09 0.22,0.11 0.47,0.17 0.7,0.17 0.57,0 1.11,-0.31 1.39,-0.85 l 6.73,-13.19 3.33,1.68 c 3.59,1.95 4.98,6.44 3.09,10.09 -0.39,0.76 -0.1,1.7 0.66,2.09 0.38,0.2 0.8,0.22 1.18,0.1 0.38,-0.12 0.71,-0.38 0.91,-0.77 2.48,-4.81 0.93,-10.66 -3.42,-13.65 z"
       id="path5245" />
    	<path
       class="st54"
       d="m 438.46,198.67 -5.17,-5.17 c -0.45,-0.45 -1.18,-0.45 -1.63,0 -0.45,0.45 -0.45,1.18 0,1.63 l 3.24,3.23 h -9.86 c -0.62,0 -1.11,0.5 -1.11,1.12 0,0.62 0.5,1.12 1.11,1.12 h 9.86 l -3.24,3.24 c -0.45,0.45 -0.45,1.18 0,1.63 0.23,0.23 0.52,0.34 0.82,0.34 0.29,0 0.59,-0.11 0.82,-0.34 l 5.17,-5.17 c 0.22,-0.22 0.34,-0.51 0.34,-0.82 0,-0.31 -0.14,-0.59 -0.35,-0.81 z"
       id="path5247" />
    	<path
       class="st54"
       d="m 428.01,202.84 c -0.62,0 -1.12,0.5 -1.12,1.12 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0.01,-0.62 -0.49,-1.12 -1.11,-1.12 z"
       id="path5249" />
    	<path
       class="st54"
       d="m 428.01,196.14 c 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0,-0.62 -0.5,-1.12 -1.11,-1.12 -0.62,0 -1.12,0.5 -1.12,1.12 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 z"
       id="path5251" />
    	<path
       class="st54"
       d="m 428.01,187.96 c 0.62,0 1.11,-0.5 1.11,-1.11 v -3.72 c 0,-0.62 -0.5,-1.11 -1.11,-1.11 -0.62,0 -1.12,0.5 -1.12,1.11 v 3.72 c 0,0.61 0.5,1.11 1.12,1.11 z"
       id="path5253" />
    	<path
       class="st54"
       d="m 428.01,211.02 c -0.62,0 -1.12,0.5 -1.12,1.11 v 3.72 c 0,0.62 0.5,1.12 1.12,1.12 0.62,0 1.11,-0.5 1.11,-1.12 v -3.72 c 0.01,-0.61 -0.49,-1.11 -1.11,-1.11 z"
       id="path5255" />
    	<line
       class="st60"
       x1="420.94"
       y1="244.49001"
       x2="420.94"
       y2="260.76999"
       id="line5257" />
    	<path
       class="st61"
       d="m 420.94,241.53 v 0 m 0,20.72 v 0"
       id="path5259" />
    	<path
       d="m 420.94,244.31 c 1.54,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0.01,1.53 1.25,2.78 2.78,2.78 z"
       id="path5261" />
    	<a
       id="a9538"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><g
         class="st5"
         id="g5281">
    		<path
       class="st55"
       d="m 223.86,289.62 v -13 h 3.85 c 1.75,0 3.62,0.65 3.62,3.71 0,2.95 -2.3,3.57 -3.64,3.57 h -2.18 v 5.73 h -1.65 z m 1.66,-7.16 h 1.82 c 0.68,0 2.3,-0.18 2.3,-2.21 0,-1.98 -1.48,-2.18 -1.84,-2.18 h -2.29 v 4.39 z"
       id="path5263" />
    		<path
       class="st55"
       d="m 233.24,285.21 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path5265" />
    		<path
       class="st55"
       d="m 243.93,289.62 h -1.48 v -13 h 1.48 z"
       id="path5267" />
    		<path
       class="st55"
       d="m 246.36,276.62 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5269" />
    		<path
       class="st55"
       d="m 250.65,280.53 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5271" />
    		<path
       class="st55"
       d="m 255.36,276.62 h 1.66 v 1.58 h -1.66 v -1.58 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5273" />
    		<path
       class="st55"
       d="m 264.24,283.45 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5275" />
    		<path
       class="st55"
       d="m 273.16,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5277" />
    		<path
       class="st55"
       d="m 278.92,289.62 h -1.48 v -13 h 1.48 z"
       id="path5279" />
    	</g></a>
    	<a
       id="a9548"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><g
         class="st5"
         id="g5297">
    		<path
       class="st55"
       d="m 220.93,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5283" />
    		<path
       class="st55"
       d="m 233.25,305.05 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5285" />
    		<path
       class="st55"
       d="m 237.24,306.82 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5287" />
    		<path
       class="st55"
       d="m 251.43,311.23 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5289" />
    		<path
       class="st55"
       d="m 255.24,306.82 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5291" />
    		<path
       class="st55"
       d="m 268.96,311.23 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5293" />
    		<path
       class="st55"
       d="m 280.22,309.53 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path5295" />
    	</g></a>
    	<path
       class="st62"
       d="m 194.09,276.5 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5299" />
    	<line
       class="st63"
       x1="185.19"
       y1="291"
       x2="185.19"
       y2="298.26999"
       id="line5301" />
    	<path
       class="st62"
       d="m 185.6,302.83 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5303" />
    	<line
       class="st58"
       x1="200.14"
       y1="311.72"
       x2="304.82999"
       y2="311.72"
       id="line5305" />
    	<path
       class="st62"
       d="m 309.41,311.32 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5307" />
    	<line
       class="st63"
       x1="318.29999"
       y1="296.82001"
       x2="318.29999"
       y2="289.54999"
       id="line5309" />
    	<path
       class="st62"
       d="m 317.9,284.99 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5311" />
    	<line
       class="st58"
       x1="303.35999"
       y1="276.10001"
       x2="198.67"
       y2="276.10001"
       id="line5313" />
    	<path
       class="st59"
       d="m 185.19,288.1 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5315" />
    	<a
       id="a9526"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><path
         class="st55"
         d="m 240.85,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.96,-0.89 -37.64,-0.03 -7.05,0.48 -12.19,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.38,10.9 12.71,10.57 z"
         id="path5317" /></a>
    	<line
       class="st60"
       x1="251.75"
       y1="244.49001"
       x2="251.75"
       y2="260.76999"
       id="line5319" />
    	<path
       class="st61"
       d="m 251.75,241.53 v 0 m 0,20.72 v 0"
       id="path5321" />
    	<path
       d="m 251.75,244.31 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 z"
       id="path5323" />
    	<a
       id="a9569"
       target="blank"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       xlink:title="Political Economy"><path
         class="st54"
         d="m 268.15,214.82 h -32.81 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.49,1.09 1.09,1.09 h 32.81 c 0.6,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.48,-1.09 -1.09,-1.09 z"
         id="path5325" /></a>
    	<a
       id="a9554"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><path
         class="st54"
         d="m 238.26,213.36 h 26.98 c 0.61,0 1.09,-0.49 1.09,-1.09 0,-0.6 -0.49,-1.09 -1.09,-1.09 h -26.98 c -0.6,0 -1.09,0.49 -1.09,1.09 0,0.6 0.48,1.09 1.09,1.09 z"
         id="path5327" /></a>
    	<a
       id="a9557"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><polygon
         class="st54"
         points="244.46,194.41 241.54,194.41 241.54,209.72 244.46,209.72 "
         id="polygon5329" /></a>
    	<a
       id="a9560"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><polygon
         class="st54"
         points="250.29,194.41 247.37,194.41 247.37,209.72 250.29,209.72 "
         id="polygon5331" /></a>
    	<a
       id="a9563"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><polygon
         class="st54"
         points="256.12,194.41 253.21,194.41 253.21,209.72 256.12,209.72 "
         id="polygon5333" /></a>
    	<a
       id="a9566"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><polygon
         class="st54"
         points="261.96,194.41 259.04,194.41 259.04,209.72 261.96,209.72 "
         id="polygon5335" /></a>
    	<a
       id="a9551"
       xlink:href="https://tm-dash.azurewebsites.net/child-rights#economy"
       target="blank"
       xlink:title="Political Economy"><path
         class="st54"
         d="m 240.08,192.95 h 23.33 c 0.8,0 1.46,-0.65 1.46,-1.46 0,-0.81 -0.65,-1.46 -1.46,-1.46 h -10.94 v -2.19 h 6.56 v -4.38 h -6.56 v -0.36 c 0,-0.6 -0.49,-1.09 -1.09,-1.09 -0.6,0 -1.09,0.49 -1.09,1.09 v 6.93 h -10.21 c -0.8,0 -1.46,0.65 -1.46,1.46 0,0.8 0.66,1.46 1.46,1.46 z"
         id="path5337" /></a>
    	<g
       class="st5"
       id="g5367">
    		<path
       class="st55"
       d="m 708.46,292.66 v -13 h 3.85 c 1.75,0 3.62,0.65 3.62,3.71 0,2.95 -2.3,3.57 -3.64,3.57 h -2.18 v 5.73 h -1.65 z m 1.66,-7.16 h 1.82 c 0.68,0 2.3,-0.18 2.3,-2.21 0,-1.98 -1.48,-2.18 -1.84,-2.18 h -2.29 v 4.39 z"
       id="path5339" />
    		<path
       class="st55"
       d="m 722.96,283.57 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path5341" />
    		<path
       class="st55"
       d="m 728.7,292.66 h -1.48 v -13 h 1.48 v 4.83 h 0.05 c 0.5,-0.72 1.13,-1.1 2,-1.1 2.93,0 3.01,2.61 3.01,4.88 0,4 -1.48,4.57 -2.94,4.57 -0.95,0 -1.58,-0.41 -2.09,-1.26 h -0.04 v 1.08 z m 1.65,-1.02 c 1.85,0 1.85,-1.98 1.85,-3.35 0,-2.43 -0.22,-3.69 -1.8,-3.69 -1.64,0 -1.71,1.94 -1.71,3.15 0.01,1.38 -0.16,3.89 1.66,3.89 z"
       id="path5343" />
    		<path
       class="st55"
       d="m 737.53,292.66 h -1.48 v -13 h 1.48 z"
       id="path5345" />
    		<path
       class="st55"
       d="m 739.96,279.66 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5347" />
    		<path
       class="st55"
       d="m 748.84,286.49 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5349" />
    		<path
       class="st55"
       d="m 759.76,292.84 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5351" />
    		<path
       class="st55"
       d="m 766.67,284.65 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.93,0.58 2.93,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 z m 3.52,3.31 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0.01 1.8,-1.23 1.8,-3.67 z"
       id="path5353" />
    		<path
       class="st55"
       d="m 775.51,288.59 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5355" />
    		<path
       class="st55"
       d="m 788.01,292.66 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5357" />
    		<path
       class="st55"
       d="m 796.88,279.66 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5359" />
    		<path
       class="st55"
       d="m 800.95,279.66 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5361" />
    		<path
       class="st55"
       d="m 810,292.66 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 H 810 Z"
       id="path5363" />
    		<path
       class="st55"
       d="m 818.88,283.57 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.84,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.35 0.09,-3.45 -1.76,-3.45 z"
       id="path5365" />
    	</g>
    	<g
       class="st5"
       id="g5389">
    		<path
       class="st55"
       d="m 724.33,309.85 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0.01 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path5369" />
    		<path
       class="st55"
       d="m 738.52,314.27 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5371" />
    		<path
       class="st55"
       d="m 751.33,308.09 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5373" />
    		<path
       class="st55"
       d="m 760.51,314.27 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5375" />
    		<path
       class="st55"
       d="m 764.46,301.27 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5377" />
    		<path
       class="st55"
       d="m 770.02,314.27 h -1.48 v -13 h 1.48 z"
       id="path5379" />
    		<path
       class="st55"
       d="m 777.38,301.27 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5381" />
    		<path
       class="st55"
       d="m 783.1,306.54 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5383" />
    		<path
       class="st55"
       d="m 789.01,310.2 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5385" />
    		<path
       class="st55"
       d="m 801.5,314.27 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5387" />
    	</g>
    	<path
       class="st62"
       d="m 701.67,279.54 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5391" />
    	<line
       class="st63"
       x1="692.78003"
       y1="294.04001"
       x2="692.78003"
       y2="301.31"
       id="line5393" />
    	<path
       class="st62"
       d="m 693.19,305.87 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5395" />
    	<line
       class="st64"
       x1="707.77002"
       y1="314.76001"
       x2="822.91998"
       y2="314.76001"
       id="line5397" />
    	<path
       class="st62"
       d="m 827.52,314.36 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5399" />
    	<line
       class="st63"
       x1="836.40997"
       y1="299.85999"
       x2="836.40997"
       y2="292.59"
       id="line5401" />
    	<path
       class="st62"
       d="m 836.01,288.03 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5403" />
    	<line
       class="st64"
       x1="821.41998"
       y1="279.14001"
       x2="706.28003"
       y2="279.14001"
       id="line5405" />
    	<path
       class="st59"
       d="m 692.78,291.14 v 0 m 0,11.62 v 0 m 12,12 v 0 m 119.63,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -119.63,0 v 0"
       id="path5407" />
    	<path
       class="st55"
       d="m 753.7,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.19,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.38,10.9 12.71,10.57 z"
       id="path5409" />
    	<line
       class="st60"
       x1="764.59998"
       y1="247.53"
       x2="764.59998"
       y2="263.81"
       id="line5411" />
    	<path
       class="st61"
       d="m 764.6,244.57 v 0 m 0,20.72 v 0"
       id="path5413" />
    	<path
       d="m 764.6,247.35 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.54,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 z"
       id="path5415" />
    	<g
       class="st5"
       id="g5439">
    		<path
       class="st55"
       d="m 556.28,280.21 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.1,-0.11 -4.1,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 z"
       id="path5417" />
    		<path
       class="st55"
       d="m 565.33,289.62 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5419" />
    		<path
       class="st55"
       d="m 569.27,276.62 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5421" />
    		<path
       class="st55"
       d="m 574.83,289.62 h -1.48 v -13 h 1.48 z"
       id="path5423" />
    		<path
       class="st55"
       d="m 582.2,276.62 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.08,-3.15 -1.71,-3.15 z"
       id="path5425" />
    		<path
       class="st55"
       d="m 591.92,281.9 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5427" />
    		<path
       class="st55"
       d="m 596.25,276.62 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5429" />
    		<path
       class="st55"
       d="m 605.18,280.53 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0.01,-1.35 0.1,-3.45 -1.76,-3.45 z"
       id="path5431" />
    		<path
       class="st55"
       d="m 614.31,289.62 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5433" />
    		<path
       class="st55"
       d="m 618.54,280.53 v -1.75 l 1.48,-0.67 v 2.41 H 622 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5435" />
    		<path
       class="st55"
       d="m 626.06,289.8 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5437" />
    	</g>
    	<g
       class="st5"
       id="g5461">
    		<path
       class="st55"
       d="m 552.69,302.13 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0.01,-1.34 0.1,-3.45 -1.76,-3.45 z"
       id="path5441" />
    		<path
       class="st55"
       d="m 556.63,306.82 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5443" />
    		<path
       class="st55"
       d="m 564.84,302.13 h 1.66 l 2.03,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path5445" />
    		<path
       class="st55"
       d="m 575.31,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5447" />
    		<path
       class="st55"
       d="m 584.4,303.5 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5449" />
    		<path
       class="st55"
       d="m 593.8,311.23 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5451" />
    		<path
       class="st55"
       d="m 602.55,309.91 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path5453" />
    		<path
       class="st55"
       d="m 611.8,311.23 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5455" />
    		<path
       class="st55"
       d="m 620.62,305.05 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5457" />
    		<path
       class="st55"
       d="m 626.31,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5459" />
    	</g>
    	<path
       class="st62"
       d="m 532.48,276.5 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5463" />
    	<line
       class="st63"
       x1="523.59003"
       y1="291"
       x2="523.59003"
       y2="298.26999"
       id="line5465" />
    	<path
       class="st62"
       d="m 523.99,302.83 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5467" />
    	<line
       class="st58"
       x1="538.53003"
       y1="311.72"
       x2="643.21997"
       y2="311.72"
       id="line5469" />
    	<path
       class="st62"
       d="m 647.8,311.32 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5471" />
    	<line
       class="st63"
       x1="656.70001"
       y1="296.82001"
       x2="656.70001"
       y2="289.54999"
       id="line5473" />
    	<path
       class="st62"
       d="m 656.29,284.99 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5475" />
    	<line
       class="st58"
       x1="641.75"
       y1="276.10001"
       x2="537.06"
       y2="276.10001"
       id="line5477" />
    	<path
       class="st59"
       d="m 523.59,288.1 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5479" />
    	<path
       class="st55"
       d="m 579.24,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.06,0.48 -12.2,6.9 -11.2,13.9 l 6.37,44.87 c 0.69,6.17 6.38,10.9 12.71,10.57 z"
       id="path5481" />
    	<line
       class="st60"
       x1="590.14001"
       y1="244.49001"
       x2="590.14001"
       y2="260.76999"
       id="line5483" />
    	<path
       class="st61"
       d="m 590.14,241.53 v 0 m 0,20.72 v 0"
       id="path5485" />
    	<path
       d="m 590.14,244.31 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.25,2.78 2.78,2.78 z"
       id="path5487" />
    	<path
       class="st54"
       d="m 593.06,203.52 v -5.47 -1.46 -4.15 c 0.79,0.61 1.33,1.47 1.47,2.48 0.08,0.55 0.55,0.94 1.08,0.94 0.05,0 0.1,0 0.15,-0.01 0.6,-0.08 1.01,-0.64 0.93,-1.24 -0.43,-3.08 -3.19,-5.32 -6.55,-5.32 -3.36,0 -6.12,2.24 -6.55,5.32 -0.08,0.6 0.33,1.15 0.93,1.24 0.6,0.09 1.15,-0.33 1.24,-0.93 0.14,-1 0.68,-1.86 1.47,-2.48 v 4.15 1.46 5.47 c 0,0.6 0.49,1.09 1.09,1.09 0.6,0 1.09,-0.49 1.09,-1.09 v -5.47 h 1.46 v 5.47 c 0,0.6 0.49,1.09 1.09,1.09 0.61,0 1.1,-0.49 1.1,-1.09 z"
       id="path5489" />
    	<path
       class="st54"
       d="m 590.14,187.84 c 1.61,0 2.92,-1.31 2.92,-2.92 0,-1.61 -1.3,-2.92 -2.92,-2.92 -1.61,0 -2.92,1.31 -2.92,2.92 0,1.62 1.31,2.92 2.92,2.92 z"
       id="path5491" />
    	<path
       class="st54"
       d="m 581.07,200.69 c -0.59,-0.6 -1.56,-0.6 -2.15,0 -0.59,0.6 -0.59,1.58 0,2.19 l 2.77,2.66 c 0.35,0.35 0.35,0.92 0,1.27 -0.35,0.35 -0.91,0.35 -1.25,0 l -3.42,-3.66 v -11.67 c 0,-1.21 -1,-2.19 -2.19,-2.19 -1.19,0 -2.19,0.98 -2.19,2.19 v 12.69 c 0,0.58 0.23,1.14 0.63,1.55 l 8.12,8.37 v 2.92 h 6.56 v -7.29 c 0,-1.46 -0.38,-2.57 -1.33,-3.54 l -5.55,-5.49 z"
       id="path5493" />
    	<path
       class="st54"
       d="m 605.45,189.3 c -1.19,0 -2.19,0.98 -2.19,2.19 v 11.67 l -3.42,3.66 c -0.35,0.35 -0.91,0.35 -1.25,0 -0.35,-0.35 -0.35,-0.92 0,-1.27 l 2.77,-2.66 c 0.59,-0.6 0.59,-1.58 0,-2.19 -0.59,-0.6 -1.56,-0.6 -2.15,0 l -5.55,5.49 c -0.95,0.97 -1.33,2.08 -1.33,3.54 v 7.29 h 6.56 v -2.92 l 8.12,-8.37 c 0.41,-0.41 0.63,-0.97 0.63,-1.55 v -12.69 c 0,-1.21 -1,-2.19 -2.19,-2.19 z"
       id="path5495" />
    	<g
       class="st5"
       id="g5519">
    		<path
       class="st55"
       d="m 1230.03,288.1 v -13 h 4.23 c 1.8,0 2.41,0.61 2.9,1.33 0.45,0.7 0.52,1.48 0.52,1.73 0,1.62 -0.56,2.7 -2.23,3.08 v 0.09 c 1.85,0.22 2.67,1.33 2.67,3.11 0,3.33 -2.43,3.66 -3.91,3.66 z m 1.65,-7.52 h 2.41 c 1.3,-0.02 1.93,-0.81 1.93,-2.07 0,-1.08 -0.61,-1.96 -2,-1.96 h -2.34 v 4.03 z m 0,6.08 h 2.34 c 1.77,0 2.39,-1.26 2.39,-2.21 0,-2.07 -1.28,-2.43 -2.97,-2.43 h -1.76 z"
       id="path5497" />
    		<path
       class="st55"
       d="m 1245.56,279.01 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 V 287 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path5499" />
    		<path
       class="st55"
       d="m 1252.38,288.28 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5501" />
    		<path
       class="st55"
       d="m 1257.57,275.1 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5503" />
    		<path
       class="st55"
       d="m 1266.62,288.1 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path5505" />
    		<path
       class="st55"
       d="m 1272.13,284.03 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5507" />
    		<path
       class="st55"
       d="m 1282.37,288.28 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5509" />
    		<path
       class="st55"
       d="m 1290.36,288.28 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5511" />
    		<path
       class="st55"
       d="m 1304.35,286.79 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path5513" />
    		<path
       class="st55"
       d="m 1313.6,288.1 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5515" />
    		<path
       class="st55"
       d="m 1322.47,275.1 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.08,-3.15 -1.72,-3.15 z"
       id="path5517" />
    	</g>
    	<g
       class="st5"
       id="g5543">
    		<path
       class="st55"
       d="m 1241.57,300.29 c 0.02,-0.74 -0.04,-1.48 -0.38,-1.89 -0.34,-0.41 -1.12,-0.56 -1.46,-0.56 -1.37,0 -1.91,0.83 -1.96,1.01 -0.05,0.14 -0.38,0.47 -0.38,2.7 v 3.47 c 0,3.19 1.04,3.57 2.32,3.57 0.5,0 2.03,-0.18 2.05,-2.72 h 1.71 c 0.07,4.11 -2.83,4.11 -3.67,4.11 -1.62,0 -4.11,-0.11 -4.11,-5.15 v -3.67 c 0,-3.67 1.62,-4.72 4.18,-4.72 2.57,0 3.56,1.33 3.4,3.85 z"
       id="path5521" />
    		<path
       class="st55"
       d="m 1250.63,309.7 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5523" />
    		<path
       class="st55"
       d="m 1254.57,296.7 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5525" />
    		<path
       class="st55"
       d="m 1260.13,309.7 h -1.48 v -13 h 1.48 z"
       id="path5527" />
    		<path
       class="st55"
       d="m 1267.49,296.7 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.86,3.35 1.66,0 1.66,-2.05 1.66,-3.89 -0.01,-1.21 -0.08,-3.15 -1.72,-3.15 z"
       id="path5529" />
    		<path
       class="st55"
       d="m 1277.46,303.73 v 5.98 h -1.66 v -13 h 4.48 c 2.3,0 3.12,1.62 3.12,3.24 0,1.53 -0.85,2.7 -2.38,2.97 v 0.04 c 1.5,0.23 2.04,0.74 2.12,3.35 0.02,0.56 0.2,2.59 0.45,3.4 h -1.73 c -0.47,-0.9 -0.36,-2.59 -0.5,-4.32 -0.13,-1.58 -1.41,-1.66 -1.96,-1.66 h -1.94 z m 0,-1.44 h 2.48 c 1.19,0 1.76,-1.03 1.76,-2.16 0,-0.94 -0.47,-1.98 -1.75,-1.98 h -2.5 v 4.14 z"
       id="path5531" />
    		<path
       class="st55"
       d="m 1285.56,296.7 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5533" />
    		<path
       class="st55"
       d="m 1294.49,300.61 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.84,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.72,1.04 c -1.68,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0,-1.34 0.09,-3.45 -1.76,-3.45 z"
       id="path5535" />
    		<path
       class="st55"
       d="m 1303.62,309.7 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5537" />
    		<path
       class="st55"
       d="m 1307.85,300.61 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5539" />
    		<path
       class="st55"
       d="m 1315.37,309.88 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5541" />
    	</g>
    	<path
       class="st62"
       d="m 1219.79,274.98 c -4.64,1.24 -8.16,5.18 -8.8,10.03"
       id="path5545" />
    	<line
       class="st63"
       x1="1210.89"
       y1="289.48001"
       x2="1210.89"
       y2="296.75"
       id="line5547" />
    	<path
       class="st62"
       d="m 1211.3,301.31 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5549" />
    	<line
       class="st58"
       x1="1225.84"
       y1="310.20001"
       x2="1330.53"
       y2="310.20001"
       id="line5551" />
    	<path
       class="st62"
       d="m 1335.11,309.8 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5553" />
    	<line
       class="st63"
       x1="1344"
       y1="295.29999"
       x2="1344"
       y2="288.03"
       id="line5555" />
    	<path
       class="st62"
       d="m 1343.6,283.47 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5557" />
    	<line
       class="st58"
       x1="1329.0601"
       y1="274.57999"
       x2="1224.37"
       y2="274.57999"
       id="line5559" />
    	<path
       class="st59"
       d="m 1210.89,286.58 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5561" />
    	<path
       class="st55"
       d="m 1266.55,234.48 c 4.8,-0.38 14.47,-0.37 21.61,0.01 6.31,0.34 11.83,-4.17 12.74,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.09,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.19,6.9 -11.2,13.9 l 6.37,44.87 c 0.7,6.17 6.39,10.9 12.72,10.57 z"
       id="path5563" />
    	<line
       class="st60"
       x1="1277.45"
       y1="242.97"
       x2="1277.45"
       y2="259.25"
       id="line5565" />
    	<path
       class="st61"
       d="m 1277.45,240.01 v 0 m 0,20.72 v 0"
       id="path5567" />
    	<path
       d="m 1277.45,242.79 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.25,-2.78 -2.78,-2.78 -1.54,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 z"
       id="path5569" />
    	<path
       class="st54"
       d="m 1294.95,197.01 h -1.04 c -0.42,-2.73 -1.49,-5.24 -3.06,-7.37 l 0.74,-0.74 c 0.98,-0.97 0.98,-2.56 0,-3.53 -0.98,-0.98 -2.56,-0.98 -3.53,0 l -0.75,0.74 c -2.12,-1.57 -4.63,-2.64 -7.36,-3.06 v -1.04 c 0,-1.38 -1.12,-2.5 -2.5,-2.5 -1.38,0 -2.5,1.12 -2.5,2.5 v 1.04 c -2.73,0.41 -5.24,1.49 -7.37,3.06 l -0.74,-0.74 c -0.98,-0.98 -2.56,-0.98 -3.53,0 -0.98,0.98 -0.98,2.56 0,3.53 l 0.74,0.74 c -1.57,2.13 -2.65,4.64 -3.06,7.37 h -1.04 c -1.38,0 -2.5,1.12 -2.5,2.5 0,1.38 1.12,2.5 2.5,2.5 h 1.04 c 0.41,2.73 1.49,5.24 3.06,7.37 l -0.74,0.74 c -0.98,0.98 -0.98,2.56 0,3.54 0.48,0.49 1.12,0.73 1.76,0.73 0.64,0 1.28,-0.24 1.77,-0.73 l 0.74,-0.74 c 2.13,1.57 4.64,2.64 7.37,3.06 v 1.04 c 0,1.38 1.12,2.5 2.5,2.5 1.38,0 2.5,-1.12 2.5,-2.5 v -1.04 c 2.73,-0.41 5.24,-1.49 7.36,-3.06 l 0.75,0.74 c 0.48,0.49 1.12,0.73 1.76,0.73 0.64,0 1.28,-0.24 1.77,-0.73 0.98,-0.98 0.98,-2.56 0,-3.54 l -0.74,-0.74 c 1.57,-2.13 2.64,-4.64 3.06,-7.37 h 1.04 c 1.38,0 2.5,-1.12 2.5,-2.5 0,-1.38 -1.12,-2.5 -2.5,-2.5 z m -17.5,14.17 c -6.43,0 -11.67,-5.23 -11.67,-11.67 0,-6.44 5.24,-11.67 11.67,-11.67 6.43,0 11.67,5.23 11.67,11.67 0,6.44 -5.24,11.67 -11.67,11.67 z"
       id="path5571" />
    	<path
       class="st54"
       d="m 1279.92,208.17 v -4.64 -1.24 -3.52 c 0.67,0.52 1.13,1.25 1.25,2.1 0.06,0.46 0.46,0.8 0.91,0.8 0.05,0 0.09,0 0.13,-0.01 0.51,-0.07 0.87,-0.54 0.79,-1.05 -0.36,-2.61 -2.7,-4.51 -5.55,-4.51 -2.85,0 -5.19,1.9 -5.56,4.51 -0.07,0.51 0.29,0.98 0.79,1.05 0.51,0.07 0.98,-0.28 1.05,-0.79 0.12,-0.85 0.58,-1.58 1.25,-2.1 v 3.52 1.24 4.64 c 0,0.51 0.41,0.93 0.92,0.93 0.52,0 0.93,-0.42 0.93,-0.93 v -4.64 h 1.24 v 4.64 c 0,0.51 0.41,0.93 0.92,0.93 0.52,-0.01 0.93,-0.42 0.93,-0.93 z"
       id="path5573" />
    	<path
       class="st54"
       d="m 1277.45,194.87 c 1.36,0 2.47,-1.11 2.47,-2.47 0,-1.36 -1.11,-2.47 -2.47,-2.47 -1.37,0 -2.47,1.11 -2.47,2.47 0,1.37 1.1,2.47 2.47,2.47 z"
       id="path5575" />
    	<g
       class="st5"
       id="g5589">
    		<path
       class="st55"
       d="m 911.99,276.62 h 4 c 1.66,0 2.84,0.59 3.49,1.98 0.52,1.1 0.58,3.69 0.58,4.11 0,2.77 -0.25,4.38 -0.79,5.24 -0.7,1.12 -2.02,1.67 -4.29,1.67 h -2.99 v -13 z m 1.66,11.56 h 1.57 c 2.3,0 3.15,-0.86 3.15,-3.89 v -2.63 c 0,-2.63 -0.81,-3.6 -2.54,-3.6 h -2.18 v 10.12 z"
       id="path5577" />
    		<path
       class="st55"
       d="m 927.48,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.34,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.39,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5579" />
    		<path
       class="st55"
       d="m 931.96,280.53 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path5581" />
    		<path
       class="st55"
       d="m 941.48,288.31 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5583" />
    		<path
       class="st55"
       d="m 949.54,285.21 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.05 1.91,-4.01 z"
       id="path5585" />
    		<path
       class="st55"
       d="m 963.73,289.62 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5587" />
    	</g>
    	<g
       class="st5"
       id="g5607">
    		<path
       class="st55"
       d="m 915.05,305.05 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5591" />
    		<path
       class="st55"
       d="m 924.23,311.23 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5593" />
    		<path
       class="st55"
       d="m 928.17,298.23 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5595" />
    		<path
       class="st55"
       d="m 933.73,311.23 h -1.48 v -13 h 1.48 z"
       id="path5597" />
    		<path
       class="st55"
       d="m 941.1,298.23 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.94,-0.58 -2.94,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.72,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0.01,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5599" />
    		<path
       class="st55"
       d="m 946.82,303.5 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5601" />
    		<path
       class="st55"
       d="m 952.72,307.16 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5603" />
    		<path
       class="st55"
       d="m 965.21,311.23 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path5605" />
    	</g>
    	<path
       class="st62"
       d="m 881.39,276.5 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5609" />
    	<line
       class="st63"
       x1="872.5"
       y1="291"
       x2="872.5"
       y2="298.26999"
       id="line5611" />
    	<path
       class="st62"
       d="m 872.91,302.83 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5613" />
    	<line
       class="st58"
       x1="887.45001"
       y1="311.72"
       x2="992.14001"
       y2="311.72"
       id="line5615" />
    	<path
       class="st62"
       d="m 996.72,311.32 c 4.63,-1.24 8.16,-5.18 8.79,-10.03"
       id="path5617" />
    	<line
       class="st63"
       x1="1005.61"
       y1="296.82001"
       x2="1005.61"
       y2="289.54999"
       id="line5619" />
    	<path
       class="st62"
       d="m 1005.21,284.99 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5621" />
    	<line
       class="st58"
       x1="990.65997"
       y1="276.10001"
       x2="885.96997"
       y2="276.10001"
       id="line5623" />
    	<path
       class="st59"
       d="m 872.5,288.1 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5625" />
    	<path
       class="st55"
       d="m 928.15,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.9,-7.21 -4.1,-13.45 -11.15,-13.94 -8.1,-0.87 -24.95,-0.89 -37.64,-0.03 -7.05,0.48 -12.19,6.9 -11.2,13.9 l 6.37,44.87 c 0.7,6.17 6.39,10.9 12.71,10.57 z"
       id="path5627" />
    	<line
       class="st60"
       x1="939.06"
       y1="244.49001"
       x2="939.06"
       y2="260.76999"
       id="line5629" />
    	<path
       class="st61"
       d="m 939.06,241.53 v 0 m 0,20.72 v 0"
       id="path5631" />
    	<path
       d="m 939.06,244.31 c 1.53,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.54,0 -2.78,1.24 -2.78,2.78 0,1.53 1.24,2.78 2.78,2.78 z"
       id="path5633" />
    	<path
       class="st54"
       d="m 927.67,206.66 -5.23,5.23 c -1.17,1.17 -1.17,3.08 0,4.24 1.17,1.17 3.08,1.17 4.24,0 l 5.24,-5.24 c -1.66,-1.15 -3.09,-2.59 -4.25,-4.23 z"
       id="path5635" />
    	<path
       class="st54"
       d="m 937.6,196.59 h -2.92 c -0.4,0 -0.73,0.33 -0.73,0.73 v 3.6 c 0.96,1.78 2.51,3.21 4.38,4.03 v -7.63 c 0,-0.4 -0.33,-0.73 -0.73,-0.73 z"
       id="path5637" />
    	<path
       class="st54"
       d="m 949.26,192.22 h -2.92 c -0.4,0 -0.73,0.33 -0.73,0.73 v 12 c 1.87,-0.82 3.41,-2.25 4.38,-4.03 v -7.98 c 0,-0.39 -0.33,-0.72 -0.73,-0.72 z"
       id="path5639" />
    	<path
       class="st54"
       d="m 943.43,194.41 h -2.92 c -0.4,0 -0.73,0.33 -0.73,0.73 v 10.31 c 0.7,0.17 1.43,0.26 2.19,0.26 0.76,0 1.49,-0.09 2.19,-0.26 v -10.31 c 0,-0.41 -0.33,-0.73 -0.73,-0.73 z"
       id="path5641" />
    	<path
       class="st54"
       d="m 941.97,182.01 c -8.06,0 -14.58,6.53 -14.58,14.58 0,8.05 6.53,14.58 14.58,14.58 8.06,0 14.58,-6.53 14.58,-14.58 0,-8.05 -6.52,-14.58 -14.58,-14.58 z m 8.02,22.01 c -1.19,1.29 -2.68,2.3 -4.38,2.89 -0.47,0.17 -0.95,0.31 -1.46,0.41 -0.71,0.15 -1.44,0.22 -2.19,0.22 -0.75,0 -1.48,-0.07 -2.19,-0.22 -0.5,-0.1 -0.98,-0.24 -1.46,-0.41 -1.69,-0.59 -3.19,-1.6 -4.38,-2.89 -1.82,-1.95 -2.92,-4.56 -2.92,-7.42 0,-6.04 4.9,-10.94 10.94,-10.94 6.04,0 10.94,4.9 10.94,10.94 0.02,2.86 -1.08,5.47 -2.9,7.42 z"
       id="path5643" />
    	<g
       class="st5"
       id="g5661">
    		<path
       class="st55"
       d="m 1076.1,278.15 h 2.11 l 4.23,13 h -1.85 l -0.94,-3.1 h -5.02 l -0.97,3.1 h -1.67 z m 1,1.53 h -0.04 l -2.03,6.93 h 4.16 z"
       id="path5645" />
    		<path
       class="st55"
       d="m 1088.75,284.97 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5647" />
    		<path
       class="st55"
       d="m 1097.75,284.97 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5649" />
    		<path
       class="st55"
       d="m 1103.44,287.08 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5651" />
    		<path
       class="st55"
       d="m 1113.68,291.33 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path5653" />
    		<path
       class="st55"
       d="m 1121.67,291.33 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path5655" />
    		<path
       class="st55"
       d="m 1131.14,282.06 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5657" />
    		<path
       class="st55"
       d="m 1135.73,286.74 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.36,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.54,0 1.91,-1.06 1.91,-4.01 z"
       id="path5659" />
    	</g>
    	<g
       class="st5"
       id="g5677">
    		<path
       class="st55"
       d="m 1084.96,303.65 h 1.48 V 314 c 0,1.44 -0.41,2.18 -2.57,2.18 v -1.26 c 0.63,0 1.1,-0.09 1.1,-0.85 v -10.42 z m -0.09,-3.91 h 1.66 v 1.58 h -1.66 z"
       id="path5663" />
    		<path
       class="st55"
       d="m 1093.86,303.65 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path5665" />
    		<path
       class="st55"
       d="m 1100.68,312.92 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5667" />
    		<path
       class="st55"
       d="m 1106.15,303.65 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5669" />
    		<path
       class="st55"
       d="m 1110.87,299.74 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5671" />
    		<path
       class="st55"
       d="m 1119.74,306.57 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5673" />
    		<path
       class="st55"
       d="m 1125.43,308.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5675" />
    	</g>
    	<path
       class="st62"
       d="m 1050.59,278.02 c -4.63,1.24 -8.16,5.18 -8.79,10.03"
       id="path5679" />
    	<line
       class="st63"
       x1="1041.7"
       y1="292.51999"
       x2="1041.7"
       y2="299.79001"
       id="line5681" />
    	<path
       class="st62"
       d="m 1042.1,304.35 c 1.24,4.63 5.18,8.16 10.03,8.79"
       id="path5683" />
    	<line
       class="st58"
       x1="1056.65"
       y1="313.23999"
       x2="1161.33"
       y2="313.23999"
       id="line5685" />
    	<path
       class="st62"
       d="m 1165.91,312.84 c 4.64,-1.24 8.16,-5.18 8.8,-10.03"
       id="path5687" />
    	<line
       class="st63"
       x1="1174.8101"
       y1="298.34"
       x2="1174.8101"
       y2="291.07001"
       id="line5689" />
    	<path
       class="st62"
       d="m 1174.4,286.51 c -1.24,-4.63 -5.18,-8.16 -10.03,-8.79"
       id="path5691" />
    	<line
       class="st58"
       x1="1159.86"
       y1="277.62"
       x2="1055.17"
       y2="277.62"
       id="line5693" />
    	<path
       class="st59"
       d="m 1041.7,289.62 v 0 m 0,11.62 v 0 m 12,12 v 0 m 109.11,0 v 0 m 12,-12 v 0 m 0,-11.62 v 0 m -12,-12 v 0 m -109.11,0 v 0"
       id="path5695" />
    	<path
       class="st55"
       d="m 1097.35,234.48 c 4.8,-0.38 14.48,-0.37 21.61,0.01 6.31,0.34 11.84,-4.17 12.75,-10.42 l 6.55,-44.96 c 0.89,-7.21 -4.1,-13.45 -11.16,-13.94 -8.1,-0.87 -24.95,-0.89 -37.63,-0.03 -7.06,0.48 -12.2,6.9 -11.2,13.9 l 6.36,44.87 c 0.7,6.17 6.4,10.9 12.72,10.57 z"
       id="path5697" />
    	<line
       class="st65"
       x1="1108.25"
       y1="246.00999"
       x2="1108.25"
       y2="262.29001"
       id="line5699" />
    	<path
       class="st66"
       d="m 1108.25,243.05 v 0 m 0,20.72 v 0"
       id="path5701" />
    	<path
       class="st55"
       d="m 1108.25,245.83 c 1.54,0 2.78,-1.24 2.78,-2.78 0,-1.53 -1.24,-2.78 -2.78,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.53 1.25,2.78 2.78,2.78 z"
       id="path5703" />
    	<path
       class="st54"
       d="m 1109.84,191.45 c 0.31,0.31 0.31,0.81 0,1.12 l -4.89,4.89 c -0.31,0.31 -0.81,0.31 -1.12,0.01 -0.31,-0.32 -0.3,-0.82 0,-1.13 l 4.89,-4.89 c 0.31,-0.31 0.81,-0.31 1.12,0 z m 2.32,14.34 c 0.31,0.31 0.81,0.31 1.12,0 l 4.89,-4.89 c 0.31,-0.31 0.31,-0.81 0,-1.12 -0.3,-0.31 -0.81,-0.31 -1.12,0 l -4.89,4.89 c -0.31,0.31 -0.31,0.81 0,1.12 z m 11.73,-14.17 v 23.36 h -25.4 v -0.38 l -2.25,2.41 -3.63,-3.64 5.88,-5.5 v -25.86 h 16.15 l 9.25,9.61 z m -8.82,-0.78 h 4.36 l -4.36,-4.53 v 4.53 z m 6.15,2 h -8.16 v -8.16 h -11.89 v 20.69 l 5.97,-5.59 -1.79,-1.79 5.02,-5.03 6.29,6.29 -5.02,5.03 -1.8,-1.8 -8.67,9.27 v 0.56 h 20.05 l 0,-19.47 z"
       id="path5705" />
    	<path
       class="st67"
       d="m 50.515889,1075.6799 c -11.05,0 -20,8.96 -20,20 v 159.23 c 0,11.05 8.95,20 20,20 H 1304.5159 c 11.05,0 20,-8.95 20,-20 v -159.23 c 0,-11.04 -8.95,-20 -20,-20 z"
       id="path5707" />
    	<g
       class="st5"
       id="g5721">
    		<path
       class="st68"
       d="m 551.42,1237.87 c 0,-1.53 -0.63,-2.36 -2.3,-2.36 -0.52,0 -2.4,0.09 -2.4,2.81 v 4.39 c 0,2.84 0.83,3.57 2.4,3.57 1.19,0 1.98,-0.32 2.32,-0.58 v -3.89 h -2.39 v -1.44 h 4.05 v 6.32 c -1.06,0.58 -2.3,0.97 -3.98,0.97 -2.75,0 -4.09,-1.42 -4.09,-5.02 v -4.27 c 0,-2.59 1.33,-4.25 4.09,-4.25 2.81,0 4.14,1.03 4.03,3.75 z"
       id="path5709" />
    		<path
       class="st68"
       d="m 557.47,1243.32 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5711" />
    		<path
       class="st68"
       d="m 569.96,1247.39 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5713" />
    		<path
       class="st68"
       d="m 578.84,1234.39 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.2 -0.08,-3.15 -1.71,-3.15 z"
       id="path5715" />
    		<path
       class="st68"
       d="m 584.47,1243.32 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5717" />
    		<path
       class="st68"
       d="m 593.56,1239.67 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5719" />
    	</g>
    	<path
       class="st69"
       d="m 538.06,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path5723" />
    	<path
       class="st70"
       d="m 538.06,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path5725" />
    	<path
       class="st68"
       d="m 583.23,1164.08 c 0,-0.51 -0.41,-0.92 -0.92,-0.92 h -7.79 c -0.51,0 -0.92,0.41 -0.92,0.92 v 0.75 c 0,0.51 0.41,0.92 0.93,0.92 l 4.31,-0.01 -5.98,5.98 c -1.63,-1.22 -3.65,-1.95 -5.84,-1.95 -5.41,0 -9.81,4.39 -9.81,9.8 0,5.41 4.4,9.81 9.81,9.81 5.41,0 9.81,-4.4 9.81,-9.81 0,-2.29 -0.79,-4.39 -2.12,-6.06 l 5.95,-5.95 v 4.18 c 0,0.59 0.48,1.07 1.08,1.07 h 0.59 c 0.51,0 0.93,-0.41 0.92,-0.92 l -0.02,-7.81 z m -16.22,23.3 c -4.31,0 -7.81,-3.5 -7.81,-7.81 0,-4.31 3.51,-7.81 7.81,-7.81 4.31,0 7.81,3.5 7.81,7.81 0.01,4.31 -3.5,7.81 -7.81,7.81 z"
       id="path5727" />
    	<path
       class="st68"
       d="m 573.95,1186.53 c 3.82,-3.83 3.82,-10.05 0,-13.87 -3.82,-3.83 -10.04,-3.83 -13.87,0 -3.82,3.82 -3.82,10.04 0,13.87 1.58,1.58 3.57,2.49 5.63,2.77 v 6.62 h -2.67 c -0.52,0 -0.95,0.43 -0.95,0.95 v 0.72 c 0,0.53 0.42,0.95 0.95,0.95 h 2.67 v 2.68 c 0,0.52 0.42,0.94 0.94,0.94 h 0.74 c 0.52,0 0.94,-0.42 0.94,-0.94 v -2.68 H 571 c 0.52,0 0.95,-0.42 0.95,-0.95 v -0.72 c 0,-0.52 -0.42,-0.95 -0.95,-0.95 h -2.67 v -6.62 c 2.05,-0.28 4.04,-1.19 5.62,-2.77 z m -12.46,-1.41 c -3.05,-3.05 -3.05,-8.01 0,-11.05 3.05,-3.05 8,-3.05 11.05,0 3.05,3.04 3.05,8 0,11.05 -3.05,3.04 -8,3.04 -11.05,0 z"
       id="path5729" />
    	<a
       id="a25595"
       xlink:href="https://tm-dash.azurewebsites.net/disability"
       target="blank"
       xlink:title="Disability"><g
         class="st5"
         id="g5751">
    		<path
       class="st68"
       d="m 322.55,1234.8 h 4 c 1.66,0 2.84,0.59 3.49,1.98 0.52,1.1 0.58,3.69 0.58,4.11 0,2.77 -0.25,4.38 -0.79,5.24 -0.7,1.12 -2.02,1.67 -4.29,1.67 h -2.99 v -13 z m 1.66,11.56 h 1.57 c 2.3,0 3.15,-0.86 3.15,-3.89 v -2.63 c 0,-2.63 -0.81,-3.6 -2.54,-3.6 h -2.18 v 10.12 z"
       id="path5731" />
    		<path
       class="st68"
       d="m 333.22,1234.8 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5733" />
    		<path
       class="st68"
       d="m 340.03,1247.98 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path5735" />
    		<path
       class="st68"
       d="m 350.02,1246.48 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path5737" />
    		<path
       class="st68"
       d="m 355.94,1247.8 h -1.48 v -13 h 1.48 v 4.83 h 0.05 c 0.5,-0.72 1.13,-1.1 2,-1.1 2.93,0 3.01,2.61 3.01,4.88 0,4 -1.48,4.57 -2.94,4.57 -0.95,0 -1.58,-0.41 -2.09,-1.26 h -0.04 v 1.08 z m 1.66,-1.03 c 1.85,0 1.85,-1.98 1.85,-3.35 0,-2.43 -0.22,-3.69 -1.8,-3.69 -1.64,0 -1.71,1.94 -1.71,3.15 0,1.39 -0.16,3.89 1.66,3.89 z"
       id="path5739" />
    		<path
       class="st68"
       d="m 363.21,1234.8 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5741" />
    		<path
       class="st68"
       d="m 368.77,1247.8 h -1.48 v -13 h 1.48 z"
       id="path5743" />
    		<path
       class="st68"
       d="m 371.2,1234.8 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5745" />
    		<path
       class="st68"
       d="m 375.49,1238.7 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5747" />
    		<path
       class="st68"
       d="m 383.06,1246.1 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path5749" />
    	</g></a>
    	<a
       id="a28807"
       xlink:href="https://tm-dash.azurewebsites.net/disability"
       target="blank"
       xlink:title="Disability"><path
         class="st69"
         d="m 321.88,1183.12 c 0,17.77 14.4,32.17 32.17,32.17 17.76,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.77,0 -32.17,14.4 -32.17,32.16 z"
         id="path5753" /></a>
    	<a
       id="a25598"><path
         class="st70"
         d="m 321.88,1183.12 c 0,17.77 14.4,32.17 32.17,32.17 17.76,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.77,0 -32.17,14.4 -32.17,32.16 z"
         id="path5755" /></a>
    	<a
       id="a28813"
       xlink:href="https://tm-dash.azurewebsites.net/disability"
       target="blank"
       xlink:title="Disability"><path
         class="st68"
         d="m 355.04,1170.29 c 0,2.33 -1.88,4.21 -4.21,4.21 -2.32,0 -4.21,-1.88 -4.21,-4.21 0,-2.32 1.88,-4.21 4.21,-4.21 2.32,0 4.21,1.89 4.21,4.21 z"
         id="path5757" /></a>
    	<a
       id="a28810"
       xlink:href="https://tm-dash.azurewebsites.net/disability"
       target="blank"
       xlink:title="Disability"><path
         class="st68"
         d="m 365.33,1193.25 h -2.29 c 0,0 -1.39,-3.97 -1.78,-5.02 -0.25,-0.7 -0.9,-1.21 -1.68,-1.21 h -5.56 v -3.9 h 5.28 c 0.7,0 1.27,-0.57 1.27,-1.27 0,-0.71 -0.57,-1.28 -1.27,-1.28 h -5.28 c 0,0 -0.3,-4.64 -2.92,-4.64 -1.79,0 -2.41,1.47 -2.41,3.27 v 8.18 c 0,1.8 1.46,3.26 3.25,3.26 0.05,0 0.1,-0.02 0.15,-0.02 0.05,0 0.1,0.02 0.15,0.02 h 6.78 l 2.26,5.67 h 4.05 c 0.84,0 1.52,-0.69 1.52,-1.53 0,-0.84 -0.68,-1.53 -1.52,-1.53 z"
         id="path5759" /></a>
    	<path
       class="st68"
       d="m 358.07,1192.62 c -0.97,3.12 -3.82,5.41 -7.22,5.41 -4.19,0 -7.6,-3.45 -7.6,-7.7 0,-2.86 1.57,-5.34 3.86,-6.66 v 0 0 -8.43 h -0.71 -0.71 -3.53 c -0.39,0 -0.7,0.32 -0.7,0.72 0,0.39 0.32,0.71 0.7,0.71 h 3.53 v 5.44 c -2.68,1.73 -4.47,4.76 -4.47,8.22 0,5.38 4.32,9.75 9.63,9.75 3.52,0 6.58,-1.95 8.26,-4.82 l -1.04,-2.64 z"
       id="path5761" />
    	<g
       class="st5"
       id="g5791">
    		<path
       class="st68"
       d="m 83.83,1240.61 v -13 h 6.7 v 1.44 h -5.04 v 4.18 h 4.68 v 1.44 h -4.68 v 4.5 h 5.15 v 1.44 h -6.81 z"
       id="path5763" />
    		<path
       class="st68"
       d="M 97.34,1239.29 H 97.3 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.38 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.11 -3.29,1.82 z"
       id="path5765" />
    		<path
       class="st68"
       d="m 103.19,1232.88 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5767" />
    		<path
       class="st68"
       d="m 109.1,1240.61 h -1.48 v -13 h 1.48 z"
       id="path5769" />
    		<path
       class="st68"
       d="m 114.39,1238.92 h 0.04 l 2.18,-7.4 h 1.6 l -4.12,12.53 h -1.53 l 1.03,-3.44 -3.08,-9.09 h 1.71 z"
       id="path5771" />
    		<path
       class="st68"
       d="m 128.39,1234.43 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 H 130 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.54 z"
       id="path5773" />
    		<path
       class="st68"
       d="m 137.57,1240.61 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5775" />
    		<path
       class="st68"
       d="m 141.51,1227.61 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5777" />
    		<path
       class="st68"
       d="m 147.08,1240.61 h -1.48 v -13 h 1.48 z"
       id="path5779" />
    		<path
       class="st68"
       d="m 154.44,1227.61 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.2 -0.07,-3.15 -1.71,-3.15 z"
       id="path5781" />
    		<path
       class="st68"
       d="m 163.57,1240.61 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5783" />
    		<path
       class="st68"
       d="m 167.38,1236.2 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5785" />
    		<path
       class="st68"
       d="m 176.38,1236.2 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5787" />
    		<path
       class="st68"
       d="m 190.44,1227.61 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.2 -0.07,-3.15 -1.71,-3.15 z"
       id="path5789" />
    	</g>
    	<g
       class="st5"
       id="g5815">
    		<path
       class="st68"
       d="m 97.46,1249.2 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.86,0 1.49,0.38 2,1.1 h 0.05 v -4.83 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5793" />
    		<path
       class="st68"
       d="m 103.1,1258.13 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5795" />
    		<path
       class="st68"
       d="m 109.61,1253.11 h 1.66 l 2.03,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.84,9.09 h -1.93 z"
       id="path5797" />
    		<path
       class="st68"
       d="m 120.09,1258.13 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5799" />
    		<path
       class="st68"
       d="m 129.09,1262.2 h -1.48 v -13 h 1.48 z"
       id="path5801" />
    		<path
       class="st68"
       d="m 131.39,1257.79 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.06 1.91,-4.01 z"
       id="path5803" />
    		<path
       class="st68"
       d="m 142.25,1254.19 h 0.04 c 0.5,-0.85 1.13,-1.26 2.09,-1.26 1.46,0 2.94,0.58 2.94,4.57 0,2.27 -0.07,4.88 -3.01,4.88 -0.86,0 -1.49,-0.38 -2,-1.1 h -0.05 v 4.36 h -1.48 v -12.53 h 1.48 v 1.08 z m 3.51,3.31 c 0,-1.37 0,-3.37 -1.85,-3.37 -1.82,0 -1.66,2.52 -1.66,3.91 0,1.21 0.07,3.13 1.71,3.13 1.58,0.01 1.8,-1.24 1.8,-3.67 z"
       id="path5805" />
    		<path
       class="st68"
       d="m 154.11,1262.2 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5807" />
    		<path
       class="st68"
       d="m 164.08,1258.13 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5809" />
    		<path
       class="st68"
       d="m 176.57,1262.2 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5811" />
    		<path
       class="st68"
       d="m 180.8,1253.11 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.49 v -1.12 h 1.48 z"
       id="path5813" />
    	</g>
    	<path
       class="st69"
       d="m 105.69,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.76,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.77,0 -32.16,14.4 -32.16,32.16 z"
       id="path5817" />
    	<path
       class="st70"
       d="m 105.69,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.76,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.77,0 -32.16,14.4 -32.16,32.16 z"
       id="path5819" />
    	<path
       class="st68"
       d="m 137.19,1190.06 c 0,0 3.34,3.35 3.36,3.35 1.07,1.08 0.79,2.96 -0.22,3.99 l -4.67,4.87 c -1.8,1.79 -4.21,-0.7 -2.46,-2.44 l 2.96,-2.96 -2.9,-2.88 3.93,-3.93 v 0 z m -10.4,0 v 0 l -3.34,3.35 c -1.08,1.08 -0.8,2.96 0.2,3.99 l 4.68,4.87 c 1.8,1.79 4.2,-0.7 2.46,-2.44 l -2.96,-2.96 2.88,-2.88 -3.92,-3.93 z m 5.32,-12.46 c 2.68,0 4.85,-2.17 4.85,-4.86 0,-2.68 -2.17,-4.85 -4.85,-4.85 -2.68,0 -4.86,2.17 -4.86,4.85 0,2.69 2.17,4.86 4.86,4.86 z m 5.26,10.51 0.07,-3.31 4.03,3.77 c 0.33,0.31 0.75,0.46 1.17,0.46 0.46,0 0.92,-0.18 1.26,-0.55 0.65,-0.69 0.61,-1.78 -0.08,-2.43 0,0 -4.63,-5.02 -5.29,-5.61 -1.23,-1.09 -3.04,-1.71 -5.97,-1.71 h -0.92 c -2.93,0 -4.73,0.62 -5.97,1.71 -0.66,0.59 -5.29,5.61 -5.29,5.61 -0.69,0.65 -0.73,1.74 -0.08,2.43 0.34,0.37 0.8,0.55 1.26,0.55 0.42,0 0.84,-0.15 1.17,-0.46 l 4.03,-3.77 0.07,3.31 h 10.54 z"
       id="path5821" />
    	<path
       class="st68"
       d="m 146.25,1176.03 v 5.36 c 0,0.66 0.54,1.2 1.2,1.2 h 5.36 c 0.66,0 1.2,-0.54 1.2,-1.2 v -5.36 c 0,-0.66 -0.54,-1.2 -1.2,-1.2 h -5.36 c -0.66,0 -1.2,0.54 -1.2,1.2 z m 4.38,4.6 -0.07,-0.39 h -0.02 c -0.25,0.31 -0.65,0.48 -1.11,0.48 -0.78,0 -1.25,-0.57 -1.25,-1.19 0,-1 0.9,-1.48 2.26,-1.47 V 1178 c 0,-0.2 -0.11,-0.49 -0.7,-0.49 -0.4,0 -0.81,0.13 -1.07,0.29 l -0.22,-0.78 c 0.27,-0.14 0.8,-0.33 1.5,-0.33 1.28,0 1.7,0.75 1.7,1.66 v 1.34 c 0,0.37 0.02,0.73 0.05,0.94 h -1.07 z"
       id="path5823" />
    	<path
       class="st68"
       d="m 148.1,1184.94 v 5.3 c 0,0.68 0.55,1.23 1.23,1.23 h 5.3 c 0.68,0 1.23,-0.55 1.23,-1.23 v -5.3 c 0,-0.68 -0.55,-1.23 -1.23,-1.23 h -5.3 c -0.68,0 -1.23,0.55 -1.23,1.23 z m 4.28,5.2 c -0.45,0 -0.88,-0.16 -1.16,-0.62 h -0.02 l -0.05,0.54 h -1.02 c 0.02,-0.26 0.03,-0.72 0.03,-1.15 v -4.45 h 1.2 v 2.2 h 0.02 c 0.23,-0.33 0.63,-0.55 1.17,-0.55 0.92,0 1.6,0.77 1.59,1.95 0,1.39 -0.88,2.08 -1.76,2.08 z"
       id="path5825" />
    	<path
       class="st68"
       d="m 145.8,1193.83 v 5.28 c 0,0.69 0.55,1.24 1.24,1.24 h 5.28 c 0.68,0 1.24,-0.55 1.24,-1.24 v -5.28 c 0,-0.68 -0.56,-1.24 -1.24,-1.24 h -5.28 c -0.68,0 -1.24,0.56 -1.24,1.24 z m 4.1,3.64 c 0.28,0 0.51,-0.04 0.69,-0.12 l 0.14,0.89 c -0.21,0.09 -0.62,0.18 -1.07,0.18 -1.25,0 -2.04,-0.77 -2.04,-1.98 0,-1.13 0.77,-2.05 2.21,-2.05 0.32,0 0.66,0.05 0.92,0.15 l -0.19,0.89 c -0.14,-0.06 -0.36,-0.12 -0.67,-0.12 -0.63,0 -1.04,0.45 -1.03,1.08 -0.02,0.71 0.46,1.08 1.04,1.08 z"
       id="path5827" />
    	<path
       class="st68"
       d="m 152.48,1186.94 c -0.32,0 -0.62,0.25 -0.7,0.59 -0.02,0.07 -0.02,0.14 -0.02,0.22 v 0.57 c 0,0.08 0.01,0.15 0.02,0.21 0.08,0.33 0.36,0.57 0.7,0.57 0.51,0 0.83,-0.39 0.83,-1.09 0,-0.6 -0.27,-1.07 -0.83,-1.07 z"
       id="path5829" />
    	<path
       class="st68"
       d="m 149.31,1179.48 c 0,0.31 0.2,0.46 0.47,0.46 0.3,0 0.54,-0.2 0.62,-0.44 0.02,-0.06 0.02,-0.14 0.02,-0.21 v -0.41 c -0.62,-0.01 -1.11,0.14 -1.11,0.6 z"
       id="path5831" />
    	<a
       id="a25582"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       target="blank"
       xlink:title="Adolescents"><g
         class="st5"
         id="g5855">
    		<path
       class="st68"
       d="m 745.82,1234.39 h 2.11 l 4.23,13 h -1.85 l -0.94,-3.1 h -5.02 l -0.97,3.1 h -1.67 z m 1,1.53 h -0.04 l -2.03,6.93 h 4.16 z"
       id="path5833" />
    		<path
       class="st68"
       d="M 758.52,1234.39 H 760 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.93 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.2 -0.07,-3.15 -1.71,-3.15 z"
       id="path5835" />
    		<path
       class="st68"
       d="m 762.46,1242.98 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.58 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.06 1.91,-4.01 z"
       id="path5837" />
    		<path
       class="st68"
       d="m 773.16,1247.39 h -1.48 v -13 h 1.48 z"
       id="path5839" />
    		<path
       class="st68"
       d="m 777.15,1243.32 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5841" />
    		<path
       class="st68"
       d="m 787.39,1247.57 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.36,2.78 -3.17,2.78 z"
       id="path5843" />
    		<path
       class="st68"
       d="m 797.46,1241.21 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5845" />
    		<path
       class="st68"
       d="m 803.14,1243.32 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.11 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5847" />
    		<path
       class="st68"
       d="m 815.64,1247.39 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path5849" />
    		<path
       class="st68"
       d="m 819.87,1238.3 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5851" />
    		<path
       class="st68"
       d="m 827.39,1247.57 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5853" />
    	</g></a>
    	<a
       id="a25568"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       target="blank"
       xlink:title="Adolescents"><path
         class="st69"
         d="m 754.25,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.76,0 32.16,-14.4 32.16,-32.17 0,-17.76 -14.4,-32.16 -32.16,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
         id="path5857" /></a>
    	<path
       class="st70"
       d="m 754.25,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.76,0 32.16,-14.4 32.16,-32.17 0,-17.76 -14.4,-32.16 -32.16,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path5859" />
    	<a
       id="a27202"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       target="blank"
       xlink:title="Adolescents"><path
         class="st68"
         d="m 792.09,1195.83 v -7.1 -1.89 -5.38 c -1.02,0.79 -1.72,1.91 -1.91,3.21 -0.1,0.71 -0.71,1.22 -1.4,1.22 -0.07,0 -0.13,0 -0.2,-0.01 -0.78,-0.11 -1.32,-0.83 -1.21,-1.6 0.56,-4 4.14,-6.9 8.5,-6.9 4.36,0 7.94,2.9 8.5,6.9 0.11,0.77 -0.43,1.49 -1.21,1.6 -0.78,0.11 -1.49,-0.43 -1.6,-1.21 -0.18,-1.3 -0.88,-2.42 -1.91,-3.21 v 5.38 1.89 7.1 c 0,0.78 -0.63,1.42 -1.42,1.42 -0.78,0 -1.42,-0.64 -1.42,-1.42 v -7.1 h -1.89 v 7.1 c 0,0.78 -0.64,1.42 -1.42,1.42 -0.78,0 -1.41,-0.64 -1.41,-1.42 z"
         id="path5861" /></a>
    	<a
       id="a27205"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       target="blank"
       xlink:title="Adolescents"><path
         class="st68"
         d="m 795.87,1175.49 c -2.09,0 -3.78,-1.69 -3.78,-3.78 0,-2.09 1.69,-3.79 3.78,-3.79 2.09,0 3.78,1.7 3.78,3.79 0,2.09 -1.69,3.78 -3.78,3.78 z"
         id="path5863" /></a>
    	<a
       id="a27196"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       target="blank"
       xlink:title="Adolescents"><path
         class="st68"
         d="m 777.9,1171.72 c 5.39,0 9.46,3.84 9.46,8.97 0,0.79 -0.64,1.42 -1.42,1.42 -0.78,0 -1.42,-0.63 -1.42,-1.42 0,-2.35 -1.28,-4.28 -3.25,-5.32 l 2.18,11.35 c 0.07,0.57 -0.37,1.07 -0.94,1.07 h -0.82 v 8.04 c 0,0.78 -0.64,1.42 -1.42,1.42 -0.78,0 -1.42,-0.64 -1.42,-1.42 v -8.04 h -1.89 v 8.04 c 0,0.78 -0.64,1.42 -1.42,1.42 -0.78,0 -1.42,-0.64 -1.42,-1.42 v -8.04 h -0.82 c -0.57,0 -1.01,-0.5 -0.94,-1.07 l 2.18,-11.36 c -1.98,1.05 -3.26,2.97 -3.26,5.33 0,0.79 -0.64,1.42 -1.42,1.42 -0.78,0 -1.42,-0.63 -1.42,-1.42 0.01,-5.13 4.07,-8.97 9.46,-8.97 z"
         id="path5865" /></a>
    	<a
       id="a27199"
       xlink:href="https://tm-dash.azurewebsites.net/adolescent"
       xlink:title="Adolescents"
       target="blank"><path
         class="st68"
         d="m 777.91,1169.81 c -2.09,0 -3.78,-1.69 -3.78,-3.78 0,-2.09 1.69,-3.78 3.78,-3.78 2.09,0 3.78,1.69 3.78,3.78 0,2.09 -1.7,3.78 -3.78,3.78 z"
         id="path5867" /></a>
    	<g
       class="st5"
       id="g5897">
    		<path
       class="st68"
       d="m 943.57,1239.73 v -13 h 6.7 v 1.44 h -5.04 v 4.18 h 4.68 v 1.44 h -4.68 v 4.5 h 5.15 v 1.44 h -6.81 z"
       id="path5869" />
    		<path
       class="st68"
       d="m 957.34,1239.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5871" />
    		<path
       class="st68"
       d="m 960.36,1230.64 h 1.66 l 2.04,7.71 h 0.04 l 2.2,-7.71 h 1.55 l -2.85,9.09 h -1.93 z"
       id="path5873" />
    		<path
       class="st68"
       d="m 969.27,1226.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5875" />
    		<path
       class="st68"
       d="m 974.92,1232.01 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 z"
       id="path5877" />
    		<path
       class="st68"
       d="m 979.13,1235.32 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.92,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0.01 1.91,-1.05 1.91,-4.01 z"
       id="path5879" />
    		<path
       class="st68"
       d="m 993.32,1239.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.86,1.44 -1.86,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.47 z"
       id="path5881" />
    		<path
       class="st68"
       d="m 1001.85,1239.73 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5883" />
    		<path
       class="st68"
       d="m 1011.82,1235.67 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5885" />
    		<path
       class="st68"
       d="m 1024.32,1239.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5887" />
    		<path
       class="st68"
       d="m 1028.54,1230.64 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.41,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5889" />
    		<path
       class="st68"
       d="m 1042.06,1238.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5891" />
    		<path
       class="st68"
       d="m 1051.32,1239.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5893" />
    		<path
       class="st68"
       d="m 1060.19,1226.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.07,-3.15 -1.71,-3.15 z"
       id="path5895" />
    	</g>
    	<g
       class="st5"
       id="g5925">
    		<path
       class="st68"
       d="m 953.15,1255.16 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5899" />
    		<path
       class="st68"
       d="m 958.84,1261.34 h -1.48 v -13 h 1.48 z"
       id="path5901" />
    		<path
       class="st68"
       d="m 961.27,1248.34 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5903" />
    		<path
       class="st68"
       d="m 969.85,1261.34 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5905" />
    		<path
       class="st68"
       d="m 983.07,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5907" />
    		<path
       class="st68"
       d="m 987.55,1252.24 v -1.75 l 1.48,-0.67 v 2.41 H 991 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.5 z"
       id="path5909" />
    		<path
       class="st68"
       d="m 993.83,1257.27 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.55,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5911" />
    		<path
       class="st68"
       d="m 1010.14,1255.16 c 0.04,-1.49 -0.7,-1.89 -1.26,-1.89 -1.13,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 0.34,0 1.37,-0.36 1.31,-2 h 1.55 c 0.05,2.56 -1.85,3.21 -2.86,3.21 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 1.82,0 2.88,1.06 2.79,3.1 h -1.53 z"
       id="path5913" />
    		<path
       class="st68"
       d="m 1019.32,1261.34 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5915" />
    		<path
       class="st68"
       d="m 1028.07,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5917" />
    		<path
       class="st68"
       d="m 1037.32,1261.34 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5919" />
    		<path
       class="st68"
       d="m 1046.19,1252.24 h 1.48 v 10.01 c 0,2.04 -1.35,2.52 -3.35,2.52 -1.51,0 -2.88,-0.76 -2.75,-2.43 h 1.66 c 0.02,0.85 0.58,1.31 1.39,1.31 1.03,0 1.58,-0.63 1.58,-1.57 v -1.89 h -0.05 c -0.38,0.72 -1.21,1.13 -2,1.13 -2.47,0 -2.95,-2.12 -2.95,-4.83 0,-4.18 2.11,-4.45 2.85,-4.45 0.95,0 1.71,0.41 2.12,1.3 h 0.04 v -1.1 z m -1.73,1.05 c -1.67,0 -1.73,2.02 -1.73,3.22 0,2.92 0.67,3.6 1.76,3.6 1.78,0 1.73,-2.11 1.73,-3.37 0.01,-1.35 0.1,-3.45 -1.76,-3.45 z"
       id="path5921" />
    		<path
       class="st68"
       d="m 1051.83,1257.27 c 0,2.54 0.68,3.04 1.84,3.04 1.01,0 1.53,-0.81 1.58,-1.73 h 1.62 c -0.02,2.02 -1.26,2.93 -3.17,2.93 -1.93,0 -3.46,-0.58 -3.46,-4.59 0,-2.67 0.31,-4.86 3.46,-4.86 2.59,0 3.24,1.42 3.24,4.43 v 0.77 h -5.11 z m 3.54,-1.12 c 0,-2.65 -0.74,-2.97 -1.82,-2.97 -0.94,0 -1.71,0.45 -1.73,2.97 z"
       id="path5923" />
    	</g>
    	<path
       class="st69"
       d="m 968.61,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path5927" />
    	<path
       class="st70"
       d="m 968.61,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path5929" />
    	<path
       class="st68"
       d="m 989.67,1186.47 3.58,-0.89 1.78,-4.47 2.68,-2.69 2.69,0.9 1.78,-1.79 1.79,1.79 1.79,4.47 3.58,1.79 2.96,8.15 c -0.09,0.01 -0.18,0.02 -0.29,0.02 -0.83,0 -1.15,-0.31 -1.86,-1 -0.84,-0.8 -2.1,-2.01 -4.39,-2.01 -2.3,0 -3.56,1.21 -4.39,2.01 -0.71,0.69 -1.04,1 -1.87,1 -0.83,0 -1.16,-0.31 -1.87,-1 -0.81,-0.77 -2.03,-1.94 -4.21,-2 l -0.17,-0.7 0.89,-2.69 -3.58,0.9 -1.4,4.2 c -0.11,0.1 -0.21,0.2 -0.31,0.29 -0.71,0.69 -1.03,1 -1.86,1 -0.08,0 -0.16,0.01 -0.24,0.02 l 2.92,-7.3 z m 8.04,-0.89 3.58,3.57 v -2.68 l -2.68,-3.58 v -2.68 l -1.79,1.79 -1.79,3.58 2.68,0 z"
       id="path5931" />
    	<path
       class="st68"
       d="m 986.99,1197.39 c 1.94,0 2.95,-0.97 3.77,-1.76 0.75,-0.72 1.29,-1.24 2.48,-1.24 1.19,0 1.74,0.52 2.49,1.24 0.82,0.79 1.83,1.76 3.77,1.76 1.94,0 2.95,-0.97 3.77,-1.76 0.75,-0.72 1.3,-1.24 2.49,-1.24 1.19,0 1.73,0.52 2.48,1.24 0.82,0.79 1.84,1.76 3.77,1.76 1.94,0 2.96,-0.97 3.78,-1.76 0.75,-0.72 1.29,-1.24 2.48,-1.24 1.19,0 1.74,0.52 2.49,1.24 0.82,0.79 1.83,1.76 3.77,1.76 0.51,0 0.93,-0.41 0.93,-0.93 0,-0.51 -0.42,-0.92 -0.93,-0.92 -1.19,0 -1.73,-0.53 -2.49,-1.25 -0.81,-0.78 -1.83,-1.76 -3.77,-1.76 -1.94,0 -2.95,0.98 -3.77,1.76 -0.75,0.72 -1.3,1.25 -2.49,1.25 -1.19,0 -1.73,-0.53 -2.48,-1.25 -0.82,-0.78 -1.84,-1.76 -3.77,-1.76 -1.94,0 -2.96,0.98 -3.77,1.76 -0.76,0.72 -1.3,1.25 -2.49,1.25 -1.19,0 -1.73,-0.53 -2.49,-1.25 -0.81,-0.78 -1.83,-1.76 -3.77,-1.76 -1.93,0 -2.95,0.98 -3.77,1.76 -0.75,0.72 -1.29,1.25 -2.48,1.25 -0.51,0 -0.93,0.41 -0.93,0.92 0,0.52 0.42,0.93 0.93,0.93 z"
       id="path5933" />
    	<path
       class="st68"
       d="m 986.99,1200.97 c 1.94,0 2.95,-0.98 3.77,-1.76 0.75,-0.72 1.29,-1.25 2.48,-1.25 1.19,0 1.74,0.53 2.49,1.25 0.82,0.78 1.83,1.76 3.77,1.76 1.94,0 2.95,-0.98 3.77,-1.76 0.75,-0.72 1.3,-1.25 2.49,-1.25 1.19,0 1.73,0.53 2.48,1.25 0.82,0.78 1.84,1.76 3.77,1.76 1.94,0 2.96,-0.98 3.78,-1.76 0.75,-0.72 1.29,-1.25 2.48,-1.25 1.19,0 1.74,0.53 2.49,1.25 0.82,0.78 1.83,1.76 3.77,1.76 0.51,0 0.93,-0.42 0.93,-0.93 0,-0.51 -0.42,-0.93 -0.93,-0.93 -1.19,0 -1.73,-0.52 -2.49,-1.24 -0.81,-0.79 -1.83,-1.76 -3.77,-1.76 -1.94,0 -2.95,0.97 -3.77,1.76 -0.75,0.72 -1.3,1.24 -2.49,1.24 -1.19,0 -1.73,-0.52 -2.48,-1.24 -0.82,-0.79 -1.84,-1.76 -3.77,-1.76 -1.94,0 -2.96,0.97 -3.77,1.76 -0.76,0.72 -1.3,1.24 -2.49,1.24 -1.19,0 -1.73,-0.52 -2.49,-1.24 -0.81,-0.79 -1.83,-1.76 -3.77,-1.76 -1.93,0 -2.95,0.97 -3.77,1.76 -0.75,0.72 -1.29,1.24 -2.48,1.24 -0.51,0 -0.93,0.42 -0.93,0.93 0,0.51 0.42,0.93 0.93,0.93 z"
       id="path5935" />
    	<path
       class="st68"
       d="m 991.41,1169.21 c 0.44,0 0.81,-0.37 0.81,-0.81 v -1.62 c 0,-0.45 -0.37,-0.81 -0.81,-0.81 -0.45,0 -0.81,0.36 -0.81,0.81 v 1.62 c 0,0.44 0.36,0.81 0.81,0.81 z"
       id="path5937" />
    	<path
       class="st68"
       d="m 990.6,1177.03 v 1.62 c 0,0.45 0.36,0.81 0.81,0.81 0.44,0 0.81,-0.36 0.81,-0.81 v -1.62 c 0,-0.45 -0.37,-0.81 -0.81,-0.81 -0.45,0 -0.81,0.36 -0.81,0.81 z"
       id="path5939" />
    	<path
       class="st68"
       d="m 995.03,1170.23 1.15,-1.14 c 0.31,-0.32 0.31,-0.83 0,-1.15 -0.32,-0.31 -0.83,-0.31 -1.15,0 l -1.14,1.15 c -0.32,0.31 -0.32,0.83 0,1.14 0.31,0.32 0.83,0.32 1.14,0 z"
       id="path5941" />
    	<path
       class="st68"
       d="m 987.78,1175.19 -1.14,1.15 c -0.32,0.31 -0.32,0.83 0,1.14 0.31,0.32 0.83,0.32 1.14,0 l 1.15,-1.14 c 0.31,-0.32 0.31,-0.83 0,-1.15 -0.32,-0.31 -0.83,-0.31 -1.15,0 z"
       id="path5943" />
    	<path
       class="st68"
       d="m 994.92,1172.71 c 0,0.45 0.36,0.81 0.81,0.81 h 1.61 c 0.45,0 0.81,-0.36 0.81,-0.81 0,-0.44 -0.36,-0.81 -0.81,-0.81 h -1.61 c -0.45,0 -0.81,0.37 -0.81,0.81 z"
       id="path5945" />
    	<path
       class="st68"
       d="m 985.47,1173.52 h 1.62 c 0.45,0 0.81,-0.36 0.81,-0.81 0,-0.44 -0.36,-0.81 -0.81,-0.81 h -1.62 c -0.45,0 -0.81,0.37 -0.81,0.81 0,0.45 0.36,0.81 0.81,0.81 z"
       id="path5947" />
    	<path
       class="st68"
       d="m 993.89,1175.19 c -0.32,0.32 -0.32,0.83 0,1.15 l 1.14,1.14 c 0.32,0.32 0.83,0.32 1.15,0 0.31,-0.31 0.31,-0.83 0,-1.14 l -1.15,-1.15 c -0.31,-0.31 -0.83,-0.31 -1.14,0 z"
       id="path5949" />
    	<path
       class="st68"
       d="m 987.78,1170.23 c 0.32,0.32 0.83,0.32 1.15,0 0.31,-0.31 0.31,-0.83 0,-1.14 l -1.15,-1.15 c -0.31,-0.31 -0.83,-0.31 -1.14,0 -0.32,0.32 -0.32,0.83 0,1.15 l 1.14,1.14 z"
       id="path5951" />
    	<path
       class="st68"
       d="m 991.41,1175.14 c 1.34,0 2.43,-1.09 2.43,-2.43 0,-1.34 -1.09,-2.43 -2.43,-2.43 -1.34,0 -2.43,1.09 -2.43,2.43 0,1.34 1.09,2.43 2.43,2.43 z"
       id="path5953" />
    	<path
       class="st68"
       d="m 1018.65,1176.03 c 0,-1.36 -1.11,-2.46 -2.46,-2.46 -1.36,0 -2.46,1.1 -2.46,2.46 v 9.49 c -0.73,0.68 -1.14,1.62 -1.14,2.62 0,1.98 1.62,3.59 3.6,3.59 1.98,0 3.59,-1.61 3.59,-3.59 0,-1 -0.41,-1.94 -1.13,-2.62 v -9.49 z m -2.46,14.57 c -1.36,0 -2.46,-1.11 -2.46,-2.46 0,-0.75 0.34,-1.45 0.92,-1.92 l 0.21,-0.17 v -10.02 c 0,-0.73 0.6,-1.33 1.33,-1.33 0.73,0 1.32,0.6 1.32,1.33 v 10.02 l 0.22,0.17 c 0.58,0.47 0.92,1.17 0.92,1.92 0,1.35 -1.11,2.46 -2.46,2.46 z"
       id="path5955" />
    	<path
       class="st68"
       d="m 1016.76,1186.74 v -9.96 c 0,-0.31 -0.26,-0.56 -0.57,-0.56 -0.31,0 -0.57,0.25 -0.57,0.56 v 9.96 c -0.55,0.22 -0.95,0.76 -0.95,1.4 0,0.83 0.68,1.51 1.52,1.51 0.83,0 1.51,-0.68 1.51,-1.51 0,-0.64 -0.39,-1.18 -0.94,-1.4 z"
       id="path5957" />
    	<path
       class="st68"
       d="m 1024.89,1177.35 h -1.7 v -1.7 c 0,-0.31 -0.25,-0.57 -0.57,-0.57 -0.31,0 -0.57,0.26 -0.57,0.57 v 1.7 h -1.7 c -0.31,0 -0.57,0.26 -0.57,0.57 0,0.31 0.26,0.57 0.57,0.57 h 1.7 v 1.7 c 0,0.31 0.26,0.57 0.57,0.57 0.32,0 0.57,-0.26 0.57,-0.57 v -1.7 h 1.7 c 0.32,0 0.57,-0.26 0.57,-0.57 0,-0.31 -0.25,-0.57 -0.57,-0.57 z"
       id="path5959" />
    	<g
       class="st5"
       id="g5977">
    		<path
       class="st68"
       d="m 1187.38,1233.76 v 5.98 h -1.66 v -13 h 4.48 c 2.3,0 3.11,1.62 3.11,3.24 0,1.53 -0.85,2.7 -2.38,2.97 v 0.04 c 1.49,0.23 2.03,0.74 2.12,3.35 0.02,0.56 0.2,2.59 0.45,3.4 h -1.73 c -0.47,-0.9 -0.36,-2.59 -0.5,-4.32 -0.13,-1.58 -1.4,-1.66 -1.96,-1.66 z m 0,-1.44 h 2.48 c 1.19,0 1.76,-1.03 1.76,-2.16 0,-0.94 -0.47,-1.98 -1.75,-1.98 h -2.5 v 4.14 z"
       id="path5961" />
    		<path
       class="st68"
       d="m 1195.47,1226.73 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5963" />
    		<path
       class="st68"
       d="m 1202.28,1239.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5965" />
    		<path
       class="st68"
       d="m 1209.07,1239.73 h -1.48 v -13 h 1.48 v 7.83 h 0.04 l 2.77,-3.92 h 1.8 l -3.02,3.91 3.56,5.19 h -1.87 l -3.24,-5.1 h -0.04 z"
       id="path5967" />
    		<path
       class="st68"
       d="m 1218.26,1239.91 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2.01 -1.37,2.78 -3.17,2.78 z"
       id="path5969" />
    		<path
       class="st68"
       d="m 1232.25,1238.42 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5971" />
    		<path
       class="st68"
       d="m 1241.5,1239.73 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5973" />
    		<path
       class="st68"
       d="m 1250.38,1226.73 h 1.48 v 13 h -1.48 v -1.08 h -0.04 c -0.5,0.85 -1.13,1.26 -2.09,1.26 -1.46,0 -2.93,-0.58 -2.93,-4.57 0,-2.27 0.07,-4.88 3.01,-4.88 0.87,0 1.5,0.38 2,1.1 h 0.05 z m -1.71,4.94 c -1.58,0 -1.8,1.26 -1.8,3.69 0,1.37 0,3.35 1.85,3.35 1.66,0 1.66,-2.05 1.66,-3.89 0,-1.21 -0.08,-3.15 -1.71,-3.15 z"
       id="path5975" />
    	</g>
    	<g
       class="st5"
       id="g6021">
    		<path
       class="st68"
       d="m 1144.53,1261.34 v -6.16 c 0,-1.12 -0.36,-1.91 -1.62,-1.91 -1.48,0 -1.85,1.19 -1.85,2.72 v 5.35 h -1.48 v -13 h 1.48 v 5.08 h 0.07 c 0.59,-1.06 1.28,-1.35 2.47,-1.35 1.55,0 2.41,0.77 2.41,2.83 v 6.45 h -1.48 z"
       id="path5979" />
    		<path
       class="st68"
       d="m 1153.46,1252.24 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path5981" />
    		<path
       class="st68"
       d="m 1162.06,1261.34 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.45,0 -1.06,0.27 -1.28,0.61 -0.27,0.45 -0.34,0.99 -0.34,1.33 v 6.12 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.13 h 0.04 c 0.43,-0.97 1.21,-1.31 2.27,-1.31 0.83,0 1.78,0.34 2.12,1.17 0.5,-0.97 1.33,-1.17 2.16,-1.17 0.95,0 2.48,0.22 2.48,2.36 v 6.91 h -1.48 v -6.3 c 0,-0.92 -0.25,-1.76 -1.44,-1.76 -0.56,0 -0.72,0.02 -1.12,0.34 -0.43,0.36 -0.5,1.26 -0.5,1.6 v 6.12 h -1.47 z"
       id="path5983" />
    		<path
       class="st68"
       d="m 1175.27,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5985" />
    		<path
       class="st68"
       d="m 1184.52,1261.34 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path5987" />
    		<path
       class="st68"
       d="m 1188.46,1248.34 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path5989" />
    		<path
       class="st68"
       d="m 1192.75,1252.24 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.04,-0.58 -2.04,-1.62 v -6.46 h -1.49 v -1.12 h 1.49 z"
       id="path5991" />
    		<path
       class="st68"
       d="m 1202.27,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5993" />
    		<path
       class="st68"
       d="m 1208.12,1253.61 h 0.04 c 0.61,-1.39 1.37,-1.55 2.81,-1.55 v 1.53 c -0.13,-0.02 -0.27,-0.04 -0.4,-0.05 -0.13,-0.02 -0.25,-0.04 -0.4,-0.04 -1.64,0 -2.05,1.24 -2.05,2.47 v 5.37 h -1.48 v -9.09 h 1.48 v 1.36 z"
       id="path5995" />
    		<path
       class="st68"
       d="m 1212.46,1248.34 h 1.66 v 1.58 h -1.66 z m 1.56,13 h -1.48 v -9.09 h 1.48 z"
       id="path5997" />
    		<path
       class="st68"
       d="m 1221.26,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.49,-1.24 -2.49,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path5999" />
    		<path
       class="st68"
       d="m 1230.51,1261.34 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.95,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path6001" />
    		<path
       class="st68"
       d="m 1241.26,1261.52 c -1.96,0 -3.19,-0.86 -3.13,-2.95 h 1.67 c 0,0.52 0.02,1.75 1.51,1.75 0.88,0 1.57,-0.45 1.57,-1.39 0,-1.62 -4.54,-1.66 -4.54,-4.38 0,-0.95 0.58,-2.48 3.13,-2.48 1.62,0 3.01,0.77 2.88,2.57 h -1.64 c 0.02,-0.95 -0.49,-1.46 -1.42,-1.46 -0.79,0 -1.4,0.43 -1.4,1.22 0,1.6 4.54,1.57 4.54,4.34 0,2 -1.37,2.78 -3.17,2.78 z"
       id="path6003" />
    		<path
       class="st68"
       d="m 1246.44,1248.34 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path6005" />
    		<path
       class="st68"
       d="m 1250.72,1252.24 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path6007" />
    		<path
       class="st68"
       d="m 1260.43,1252.24 h 1.48 v 7.2 c 0,0.63 0.04,1.26 0.09,1.89 h -1.57 v -1.1 h -0.05 c -0.49,0.83 -1.35,1.28 -2.3,1.28 -1.58,0 -2.45,-0.79 -2.45,-2.34 v -6.93 h 1.48 v 6.3 c 0,1.1 0.5,1.84 1.55,1.84 0.79,0 1.78,-0.59 1.78,-2.11 v -6.03 z"
       id="path6009" />
    		<path
       class="st68"
       d="m 1269.25,1260.02 h -0.04 c -0.45,1.04 -1.15,1.49 -2.29,1.49 -1.93,0 -2.48,-1.24 -2.48,-2.99 0,-2.75 2.7,-2.88 4.77,-2.83 0.04,-1.21 0.05,-2.52 -1.53,-2.52 -0.99,0 -1.51,0.67 -1.42,1.62 h -1.6 c 0.07,-2.03 1.15,-2.74 3.08,-2.74 2.34,0 2.95,1.21 2.95,2.74 v 4.38 c 0,0.72 0.07,1.46 0.18,2.16 h -1.62 v -1.31 z m -3.33,-1.39 c 0,0.88 0.43,1.67 1.42,1.67 0.9,0 2.02,-0.56 1.87,-3.49 -1.4,0.02 -3.29,-0.1 -3.29,1.82 z"
       id="path6011" />
    		<path
       class="st68"
       d="m 1273.73,1252.24 v -1.75 l 1.48,-0.67 v 2.41 h 1.98 v 1.12 h -1.98 v 5.56 c 0,0.58 0,1.31 1.35,1.31 0.11,0 0.34,-0.04 0.67,-0.07 v 1.13 c -0.49,0.04 -0.97,0.14 -1.46,0.14 -1.4,0 -2.03,-0.58 -2.03,-1.62 v -6.46 h -1.5 v -1.12 h 1.49 z"
       id="path6013" />
    		<path
       class="st68"
       d="m 1278.44,1248.34 h 1.66 v 1.58 h -1.66 z m 1.57,13 h -1.48 v -9.09 h 1.48 z"
       id="path6015" />
    		<path
       class="st68"
       d="m 1282.31,1256.92 c 0,-2.67 0.31,-4.86 3.46,-4.86 3.15,0 3.46,2.2 3.46,4.86 0,4.01 -1.53,4.59 -3.46,4.59 -1.93,0 -3.46,-0.57 -3.46,-4.59 z m 5.37,-0.63 c 0,-2.49 -0.77,-3.03 -1.91,-3.03 -1.14,0 -1.91,0.54 -1.91,3.03 0,2.95 0.38,4.01 1.91,4.01 1.53,0 1.91,-1.05 1.91,-4.01 z"
       id="path6017" />
    		<path
       class="st68"
       d="m 1296.5,1261.34 v -6.3 c 0,-0.97 -0.34,-1.76 -1.6,-1.76 -1.62,0 -1.85,1.44 -1.85,2.68 v 5.38 h -1.48 v -7.2 c 0,-0.63 -0.04,-1.26 -0.09,-1.89 h 1.57 v 1.17 h 0.07 c 0.58,-1.03 1.26,-1.35 2.43,-1.35 1.94,0 2.43,1.17 2.43,2.97 v 6.3 h -1.48 z"
       id="path6019" />
    	</g>
    	<path
       class="st69"
       d="m 1184.8,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path6023" />
    	<path
       class="st70"
       d="m 1184.8,1183.12 c 0,17.77 14.4,32.17 32.16,32.17 17.77,0 32.17,-14.4 32.17,-32.17 0,-17.76 -14.4,-32.16 -32.17,-32.16 -17.76,0 -32.16,14.4 -32.16,32.16 z"
       id="path6025" />
    	<path
       class="st68"
       d="m 1222.43,1199.85 v 0 -0.03 -0.3 -7.79 c 0,-0.17 0.07,-0.34 0.2,-0.46 l 5.99,-5.96 c 0.19,-0.2 0.44,-0.34 0.71,-0.4 0.25,-0.05 0.5,-0.05 0.75,0.02 0.23,0.06 0.44,0.18 0.62,0.34 0.58,0.56 0.59,1.46 0.03,2.03 l -2.64,2.62 c -0.1,0.1 -0.1,0.27 0.01,0.38 0.1,0.09 0.26,0.09 0.36,-0.01 l 2.65,-2.63 c 0.77,-0.77 0.75,-2 -0.04,-2.75 -0.16,-0.16 -0.35,-0.28 -0.56,-0.36 -0.24,-0.1 -0.42,-0.33 -0.42,-0.6 v -5.41 c 0,-0.8 0.67,-1.45 1.49,-1.45 0.83,0 1.49,0.65 1.49,1.45 v 10.19 c 0,0.33 -0.13,0.63 -0.34,0.88 l -5.03,6.46 c -0.09,0.11 -0.14,0.25 -0.14,0.4 v 3.12 0 0.26 c 0,0.43 -0.35,0.77 -0.78,0.77 h -3.57 c -0.43,0 -0.78,-0.34 -0.78,-0.77 z"
       id="path6027" />
    	<path
       class="st68"
       d="m 1211.49,1199.85 v 0 -0.03 -0.3 -7.79 c 0,-0.17 -0.07,-0.34 -0.19,-0.46 l -6,-5.96 c -0.19,-0.2 -0.44,-0.34 -0.71,-0.4 -0.25,-0.05 -0.5,-0.05 -0.75,0.02 -0.23,0.06 -0.44,0.18 -0.62,0.34 -0.58,0.56 -0.59,1.46 -0.03,2.03 l 2.64,2.62 c 0.1,0.1 0.1,0.27 -0.01,0.38 -0.1,0.09 -0.26,0.09 -0.36,-0.01 l -2.65,-2.63 c -0.77,-0.77 -0.75,-2 0.04,-2.75 0.17,-0.16 0.36,-0.28 0.56,-0.36 0.25,-0.1 0.42,-0.33 0.42,-0.6 v -5.41 c 0,-0.8 -0.67,-1.45 -1.49,-1.45 -0.82,0 -1.49,0.65 -1.49,1.45 v 10.19 c 0,0.33 0.13,0.63 0.34,0.88 l 5.04,6.46 c 0.09,0.11 0.14,0.25 0.14,0.4 v 3.12 0 0.26 c 0,0.43 0.34,0.77 0.77,0.77 h 3.57 c 0.43,0 0.78,-0.34 0.78,-0.77 z"
       id="path6029" />
    	<path
       class="st68"
       d="m 1226.98,1174.54 0.04,-0.03 c 0.01,0.05 0.02,0.11 0.04,0.17 l -0.08,-0.14 z m -13.22,-2.67 0.1,-0.09 0.15,0.09 -0.12,0.11 -0.13,-0.11 z m 0.3,0.28 v 0.2 h -0.32 l -0.09,-0.13 v -0.19 h 0.02 l 0.39,0.12 z m -1.39,-0.34 h 0.34 l -0.44,0.61 -0.18,-0.1 0.04,-0.25 0.24,-0.26 z m 0.81,0.41 v 0.2 l -0.14,0.15 h -0.33 l 0.05,-0.23 0.16,-0.01 0.03,-0.08 0.23,-0.03 z m -0.09,-0.49 v -0.25 l 0.21,0.19 -0.21,0.06 z m 0.17,0.08 v 0.2 l -0.15,0.1 -0.2,0.04 v -0.34 h 0.35 z m -0.28,-0.3 v 0.22 h -0.62 l -0.23,-0.07 0.06,-0.15 0.29,-0.12 h 0.41 v 0.12 h 0.09 z m -1.44,-0.77 0.27,-0.13 0.25,0.06 -0.09,0.33 -0.26,0.08 -0.17,-0.34 z m 14.98,3.28 h -0.83 l -0.5,-0.37 -0.53,0.05 v 0.32 h -0.17 l -0.18,-0.12 -0.91,-0.24 v -0.59 l -1.16,0.09 -0.36,0.2 h -0.46 l -0.23,-0.03 -0.56,0.31 v 0.59 l -1.14,0.82 0.1,0.35 h 0.23 l -0.06,0.34 -0.16,0.06 -0.01,0.87 0.98,1.13 h 0.43 l 0.03,-0.07 h 0.77 l 0.22,-0.21 h 0.44 l 0.24,0.24 0.66,0.07 -0.09,0.87 0.73,1.28 -0.39,0.73 0.03,0.34 0.3,0.3 v 0.83 l 0.39,0.53 v 0.69 h 0.35 c -1.9,2.32 -4.79,3.82 -8.02,3.82 -5.7,0 -10.33,-4.64 -10.33,-10.34 0,-1.43 0.29,-2.8 0.82,-4.04 v -0.32 l 0.37,-0.45 c 0.13,-0.24 0.27,-0.48 0.41,-0.71 l 0.02,0.19 -0.43,0.52 c -0.13,0.25 -0.26,0.51 -0.37,0.77 v 0.59 l 0.43,0.2 v 0.82 l 0.41,0.7 0.34,0.06 0.04,-0.24 -0.39,-0.61 -0.08,-0.6 h 0.23 l 0.1,0.61 0.57,0.84 -0.15,0.26 0.36,0.56 0.91,0.22 v -0.14 l 0.36,0.05 -0.04,0.26 0.29,0.05 0.43,0.12 0.62,0.7 0.79,0.06 0.08,0.65 -0.54,0.37 -0.02,0.58 -0.08,0.35 0.78,0.98 0.06,0.33 c 0,0 0.28,0.08 0.32,0.08 0.03,0 0.63,0.46 0.63,0.46 v 1.77 l 0.22,0.06 -0.15,0.81 0.36,0.48 -0.07,0.81 0.48,0.84 0.61,0.53 0.62,0.01 0.06,-0.19 -0.45,-0.38 0.02,-0.19 0.08,-0.24 0.02,-0.23 -0.31,-0.01 -0.15,-0.19 0.25,-0.25 0.04,-0.18 -0.29,-0.08 0.02,-0.17 0.4,-0.07 0.62,-0.29 0.21,-0.38 0.64,-0.82 -0.15,-0.65 0.2,-0.34 0.59,0.02 0.4,-0.32 0.13,-1.24 0.44,-0.56 0.08,-0.36 -0.4,-0.14 -0.27,-0.43 -0.91,-0.01 -0.72,-0.27 -0.03,-0.52 -0.25,-0.42 -0.65,-0.01 -0.38,-0.59 -0.33,-0.17 -0.02,0.18 -0.61,0.04 -0.22,-0.31 -0.64,-0.13 -0.52,0.61 -0.82,-0.14 -0.06,-0.93 -0.61,-0.11 0.25,-0.45 -0.07,-0.26 -0.79,0.53 -0.5,-0.06 -0.18,-0.39 0.11,-0.4 0.28,-0.51 0.63,-0.32 h 1.22 l -0.01,0.37 0.44,0.21 -0.04,-0.64 0.32,-0.32 0.64,-0.42 0.04,-0.29 0.64,-0.66 0.67,-0.37 -0.06,-0.05 0.46,-0.43 0.17,0.04 0.07,0.1 0.18,-0.2 0.04,-0.02 -0.19,-0.02 -0.19,-0.07 v -0.18 l 0.1,-0.09 h 0.22 l 0.11,0.05 0.09,0.18 0.11,-0.02 v -0.01 l 0.03,0.01 0.32,-0.05 0.04,-0.16 0.18,0.05 v 0.17 l -0.16,0.11 0.02,0.19 0.57,0.17 v 0.01 l 0.14,-0.01 v -0.25 l -0.45,-0.2 -0.03,-0.13 0.38,-0.12 0.02,-0.37 -0.4,-0.24 -0.02,-0.6 -0.54,0.26 h -0.2 l 0.05,-0.46 -0.74,-0.18 -0.3,0.23 v 0.71 l -0.55,0.17 -0.22,0.46 -0.24,0.04 v -0.59 l -0.51,-0.07 -0.26,-0.17 -0.1,-0.38 0.92,-0.54 0.45,-0.14 0.05,0.31 0.25,-0.01 0.02,-0.16 0.26,-0.03 v -0.06 l -0.11,-0.05 -0.03,-0.16 0.33,-0.02 0.19,-0.21 0.01,-0.01 h 0.01 l 0.05,-0.06 0.68,-0.09 0.3,0.26 -0.78,0.42 1,0.23 0.13,-0.33 h 0.43 l 0.16,-0.29 -0.31,-0.08 v -0.37 l -0.97,-0.43 -0.67,0.08 -0.38,0.2 0.03,0.48 -0.4,-0.06 -0.06,-0.27 0.38,-0.34 -0.69,-0.04 -0.19,0.06 -0.09,0.23 0.26,0.05 -0.05,0.25 -0.44,0.03 -0.07,0.17 -0.64,0.02 c 0,0 -0.01,-0.36 -0.04,-0.36 -0.02,0 0.5,-0.01 0.5,-0.01 l 0.38,-0.37 -0.21,-0.1 -0.27,0.27 -0.46,-0.03 -0.27,-0.38 h -0.59 l -0.61,0.46 h 0.56 l 0.05,0.16 -0.14,0.13 0.62,0.02 0.09,0.23 -0.7,-0.03 -0.03,-0.17 -0.44,-0.1 -0.23,-0.13 -0.52,0.01 c 1.71,-1.24 3.8,-1.98 6.07,-1.98 2.61,0 5,0.98 6.82,2.58 l -0.12,0.22 -0.48,0.19 -0.2,0.22 0.05,0.25 0.24,0.04 0.15,0.37 0.43,-0.18 0.07,0.5 h -0.13 l -0.35,-0.05 -0.38,0.06 -0.38,0.53 -0.53,0.09 -0.08,0.45 0.23,0.06 -0.07,0.29 -0.53,-0.11 -0.49,0.11 -0.1,0.27 0.08,0.57 0.29,0.13 h 0.48 l 0.32,-0.03 0.1,-0.26 0.51,-0.65 0.33,0.07 0.33,-0.3 0.06,0.23 0.81,0.54 -0.1,0.14 -0.37,-0.02 0.14,0.19 0.23,0.05 0.26,-0.1 v -0.32 l 0.11,-0.06 -0.09,-0.1 -0.54,-0.3 -0.14,-0.4 h 0.44 l 0.15,0.14 0.38,0.34 0.02,0.4 0.4,0.42 0.15,-0.58 0.27,-0.15 0.05,0.48 0.28,0.29 0.53,-0.01 c 0.11,0.27 0.2,0.54 0.28,0.82 l -0.05,0.05 z m -15.57,-4.47 c 0,0 0.22,-0.03 0.24,-0.03 0.02,0 0,0.22 0,0.22 l -0.5,0.03 -0.1,-0.11 0.36,-0.11 z m -0.36,-0.5 v -0.02 h 0.23 l 0.01,-0.07 h 0.37 v 0.16 l -0.1,0.14 h -0.51 v -0.21 z m 13.58,1.25 v -0.5 c 0.18,0.19 0.35,0.38 0.51,0.58 l -0.2,0.3 h -0.71 l -0.04,-0.15 0.44,-0.23 z m 1.63,1.97 0.07,-0.08 c 0.08,0.17 0.16,0.34 0.24,0.51 h -0.11 l -0.2,0.02 v -0.45 z m 2.12,4.5 c 0,-0.33 -0.02,-0.66 -0.05,-0.98 -0.11,-1.07 -0.36,-2.1 -0.75,-3.07 -0.03,-0.07 -0.05,-0.14 -0.08,-0.21 -0.51,-1.21 -1.24,-2.31 -2.12,-3.27 -0.05,-0.06 -0.11,-0.12 -0.17,-0.18 -0.17,-0.17 -0.34,-0.34 -0.52,-0.5 -2,-1.82 -4.66,-2.94 -7.57,-2.94 -2.94,0 -5.62,1.14 -7.62,2.99 -0.47,0.43 -0.9,0.9 -1.29,1.4 -1.47,1.9 -2.35,4.29 -2.35,6.87 0,6.21 5.05,11.26 11.26,11.26 4.37,0 8.16,-2.5 10.03,-6.14 0.4,-0.78 0.71,-1.61 0.92,-2.48 0.05,-0.22 0.1,-0.44 0.14,-0.67 0.11,-0.64 0.17,-1.3 0.17,-1.97 0,-0.04 0,-0.07 0,-0.11"
       id="path6031" />
    	<g
       class="st5"
       id="g6071">
    		<path
       class="st68"
       d="m 595.3,1112.32 c 0,-3.82 0,-7.46 4.98,-7.46 3.08,0 4.32,1.7 4.2,4.8 h -2.96 c 0,-1.92 -0.34,-2.64 -1.24,-2.64 -1.7,0 -1.92,1.6 -1.92,5.3 0,3.7 0.22,5.3 1.92,5.3 1.4,0 1.34,-1.8 1.38,-2.94 h 2.98 c 0,3.86 -1.54,5.1 -4.36,5.1 -4.98,0 -4.98,-3.68 -4.98,-7.46 z"
       id="path6033" />
    		<path
       class="st68"
       d="m 609.1,1109.44 v 1.3 h 0.04 c 0.52,-1.16 1.48,-1.5 2.62,-1.5 v 2.52 c -2.48,-0.16 -2.52,1.28 -2.52,2.28 v 5.5 h -2.82 v -10.1 z"
       id="path6035" />
    		<path
       class="st68"
       d="m 612.84,1114.36 c 0,-2.76 0.4,-5.12 4.12,-5.12 3.72,0 4.12,2.36 4.12,5.12 0,3.16 -0.48,5.38 -4.12,5.38 -3.64,0 -4.12,-2.22 -4.12,-5.38 z m 5.42,-0.16 c 0,-2.1 -0.1,-3.16 -1.3,-3.16 -1.2,0 -1.3,1.06 -1.3,3.16 0,3.08 0.26,3.74 1.3,3.74 1.04,0 1.3,-0.66 1.3,-3.74 z"
       id="path6037" />
    		<path
       class="st68"
       d="m 625.3,1116.3 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path6039" />
    		<path
       class="st68"
       d="m 634.18,1116.3 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path6041" />
    		<path
       class="st68"
       d="m 645.5,1113.12 v 2.04 h -4.9 v -2.04 z"
       id="path6043" />
    		<path
       class="st68"
       d="m 647.5,1112.32 c 0,-3.82 0,-7.46 4.98,-7.46 3.08,0 4.32,1.7 4.2,4.8 h -2.96 c 0,-1.92 -0.34,-2.64 -1.24,-2.64 -1.7,0 -1.92,1.6 -1.92,5.3 0,3.7 0.22,5.3 1.92,5.3 1.4,0 1.34,-1.8 1.38,-2.94 h 2.98 c 0,3.86 -1.54,5.1 -4.36,5.1 -4.98,0 -4.98,-3.68 -4.98,-7.46 z"
       id="path6045" />
    		<path
       class="st68"
       d="m 663.56,1118.52 h -0.04 c -0.28,0.44 -0.6,0.76 -1,0.94 -0.4,0.2 -0.84,0.28 -1.38,0.28 -1.34,0 -2.52,-0.8 -2.52,-2.2 v -8.1 h 2.82 v 7 c 0,0.9 0.16,1.56 1.06,1.56 0.9,0 1.06,-0.66 1.06,-1.56 v -7 h 2.82 v 8.1 c 0,0.66 0.04,1.34 0.1,2 h -2.92 z"
       id="path6047" />
    		<path
       class="st68"
       d="m 667.48,1109.44 h 1.14 v -1.6 l 2.82,-1.26 v 2.86 h 1.46 v 1.74 h -1.46 v 5.4 c 0,0.76 -0.02,1.26 0.9,1.26 0.18,0 0.36,0 0.5,-0.04 v 1.74 c -0.38,0.04 -0.78,0.1 -1.46,0.1 -2.44,0 -2.76,-1.62 -2.76,-2.24 v -6.22 h -1.14 z"
       id="path6049" />
    		<path
       class="st68"
       d="m 673.04,1109.44 h 1.14 v -1.6 l 2.82,-1.26 v 2.86 h 1.46 v 1.74 H 677 v 5.4 c 0,0.76 -0.02,1.26 0.9,1.26 0.18,0 0.36,0 0.5,-0.04 v 1.74 c -0.38,0.04 -0.78,0.1 -1.46,0.1 -2.44,0 -2.76,-1.62 -2.76,-2.24 v -6.22 h -1.14 z"
       id="path6051" />
    		<path
       class="st68"
       d="m 682.8,1105.1 v 2.22 h -2.82 v -2.22 z m 0,14.44 h -2.82 v -10.1 h 2.82 z"
       id="path6053" />
    		<path
       class="st68"
       d="m 688.12,1110.46 h 0.04 c 0.28,-0.46 0.62,-0.76 1,-0.94 0.4,-0.2 0.86,-0.28 1.38,-0.28 1.34,0 2.52,0.8 2.52,2.2 v 8.1 h -2.82 v -6.96 c 0,-0.9 -0.16,-1.6 -1.06,-1.6 -0.9,0 -1.06,0.7 -1.06,1.6 v 6.96 h -2.82 v -10.1 h 2.82 z"
       id="path6055" />
    		<path
       class="st68"
       d="m 703.02,1109.44 v 10.52 c 0,0.7 0.04,3.46 -3.84,3.46 -2.1,0 -3.9,-0.54 -3.96,-3 h 2.76 c 0,0.42 0.06,0.78 0.24,1.02 0.18,0.26 0.5,0.4 0.94,0.4 0.7,0 1.04,-0.66 1.04,-1.68 v -1.94 h -0.04 c -0.42,0.78 -1.22,1.18 -2.14,1.18 -3.1,0 -2.96,-2.84 -2.96,-5.12 0,-2.22 0.04,-5.04 2.98,-5.04 1,0 1.86,0.44 2.26,1.38 h 0.04 v -1.18 z m -3.98,8.22 c 1.02,0 1.16,-1.06 1.16,-3.2 0,-2.22 -0.1,-3.48 -1.14,-3.48 -1.06,0 -1.24,0.74 -1.24,3.82 0,0.94 -0.14,2.86 1.22,2.86 z"
       id="path6057" />
    		<path
       class="st68"
       d="m 709.88,1119.54 v -14.44 h 3.02 v 14.44 z"
       id="path6059" />
    		<path
       class="st68"
       d="m 717.52,1116.3 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path6061" />
    		<path
       class="st68"
       d="m 726.4,1116.3 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path6063" />
    		<path
       class="st68"
       d="m 738,1118.52 h -0.04 c -0.28,0.44 -0.6,0.76 -1,0.94 -0.4,0.2 -0.84,0.28 -1.38,0.28 -1.34,0 -2.52,-0.8 -2.52,-2.2 v -8.1 h 2.82 v 7 c 0,0.9 0.16,1.56 1.06,1.56 0.9,0 1.06,-0.66 1.06,-1.56 v -7 h 2.82 v 8.1 c 0,0.66 0.04,1.34 0.1,2 H 738 Z"
       id="path6065" />
    		<path
       class="st68"
       d="m 745.66,1114.94 c 0,1.2 0.04,3 1.28,3 1,0 1.2,-0.96 1.2,-1.8 H 751 c -0.04,1.1 -0.4,2 -1.08,2.62 -0.66,0.62 -1.66,0.98 -2.98,0.98 -3.64,0 -4.12,-2.22 -4.12,-5.38 0,-2.76 0.4,-5.12 4.12,-5.12 3.8,0 4.22,2.46 4.12,5.7 z m 2.58,-1.58 c 0,-0.98 0.04,-2.38 -1.3,-2.38 -1.3,0 -1.28,1.52 -1.28,2.38 z"
       id="path6067" />
    		<path
       class="st68"
       d="m 755.28,1116.3 c -0.02,0.46 0,0.9 0.14,1.22 0.16,0.32 0.46,0.48 1.02,0.48 0.56,0 1.04,-0.36 1.04,-1.04 0,-2.14 -4.96,-1.66 -4.96,-4.88 0,-2.18 2.16,-2.84 3.98,-2.84 1.92,0 3.66,0.92 3.5,3.1 h -2.76 c 0,-0.7 -0.08,-1.12 -0.28,-1.3 -0.18,-0.18 -0.42,-0.22 -0.72,-0.22 -0.62,0 -0.96,0.4 -0.96,1.08 0,1.6 4.96,1.52 4.96,4.76 0,1.76 -1.44,3.08 -3.78,3.08 -2.46,0 -4.1,-0.62 -3.94,-3.44 z"
       id="path6069" />
    	</g>
    	<path
       class="st71"
       d="M 20,0 C 8.95,0 0,8.95 0,20 v 1270.5 c 0,11.05 8.95,20 20,20 h 1315 c 11.05,0 20,-8.95 20,-20 V 20 C 1355,8.95 1346.05,0 1335,0 H 20 Z"
       id="path6073" />
    	<g
       class="st5"
       id="g6145">
    		<path
       class="st3"
       d="M 140.58,58.84 V 33.56 h 13.79 v 3.88 h -8.51 v 6.23 h 7.84 v 3.88 h -7.84 v 7.39 h 8.79 v 3.89 h -14.07 z"
       id="path6075" />
    		<path
       class="st3"
       d="m 166.48,57.05 h -0.07 c -0.49,0.77 -1.05,1.33 -1.75,1.65 -0.7,0.35 -1.47,0.49 -2.42,0.49 -2.35,0 -4.41,-1.4 -4.41,-3.85 V 41.16 h 4.94 v 12.25 c 0,1.58 0.28,2.73 1.86,2.73 1.58,0 1.85,-1.16 1.85,-2.73 V 41.16 h 4.94 v 14.18 c 0,1.15 0.07,2.34 0.18,3.5 h -5.11 v -1.79 z"
       id="path6077" />
    		<path
       class="st3"
       d="m 180.03,41.16 v 2.28 h 0.07 c 0.91,-2.03 2.59,-2.63 4.59,-2.63 v 4.41 c -4.34,-0.28 -4.41,2.24 -4.41,3.99 v 9.63 h -4.94 V 41.16 Z"
       id="path6079" />
    		<path
       class="st3"
       d="m 186.57,49.77 c 0,-4.83 0.7,-8.96 7.21,-8.96 6.51,0 7.21,4.13 7.21,8.96 0,5.53 -0.84,9.42 -7.21,9.42 -6.37,0 -7.21,-3.89 -7.21,-9.42 z m 9.49,-0.28 c 0,-3.68 -0.18,-5.53 -2.28,-5.53 -2.1,0 -2.28,1.86 -2.28,5.53 0,5.39 0.46,6.54 2.28,6.54 1.82,0 2.28,-1.15 2.28,-6.54 z"
       id="path6081" />
    		<path
       class="st3"
       d="m 209.18,41.16 v 1.96 h 0.07 c 0.91,-1.71 2.28,-2.31 4.17,-2.31 5.11,0 4.94,5.67 4.94,9.31 0,3.57 0.14,9.07 -4.83,9.07 -1.79,0 -3.01,-0.52 -4.03,-2.03 h -0.07 v 9.28 h -4.94 V 41.16 Z m 4.34,8.68 c 0,-3.54 0.04,-5.99 -2.1,-5.99 -2.03,0 -2,2.45 -2,5.99 0,4.45 0.32,6.3 2,6.3 1.79,0 2.1,-1.85 2.1,-6.3 z"
       id="path6083" />
    		<path
       class="st3"
       d="m 226.54,50.79 c 0,2.1 0.07,5.25 2.24,5.25 1.75,0 2.1,-1.68 2.1,-3.15 h 5.01 c -0.07,1.92 -0.7,3.5 -1.89,4.58 -1.15,1.08 -2.91,1.71 -5.22,1.71 -6.37,0 -7.21,-3.88 -7.21,-9.42 0,-4.83 0.7,-8.96 7.21,-8.96 6.65,0 7.39,4.31 7.21,9.98 h -9.45 z m 4.52,-2.77 c 0,-1.71 0.07,-4.17 -2.28,-4.17 -2.28,0 -2.24,2.66 -2.24,4.17 z"
       id="path6085" />
    		<path
       class="st3"
       d="m 260.67,55.55 c 0,1.08 0.14,2.21 0.25,3.29 h -4.59 l -0.21,-2.35 h -0.07 c -1.05,1.82 -2.49,2.7 -4.62,2.7 -3.43,0 -4.69,-2.55 -4.69,-5.63 0,-5.85 4.52,-6.09 9.1,-6.02 v -1.36 c 0,-1.51 -0.21,-2.59 -2,-2.59 -1.72,0 -1.86,1.29 -1.86,2.7 h -4.83 c 0,-2.13 0.67,-3.5 1.82,-4.31 1.12,-0.84 2.73,-1.16 4.62,-1.16 6.27,0 7.07,2.7 7.07,5.92 v 8.81 z m -9.11,-2.21 c 0,1.26 0.21,2.8 1.82,2.8 2.91,0 2.45,-3.92 2.45,-5.85 -2.44,0.11 -4.27,-0.1 -4.27,3.05 z"
       id="path6087" />
    		<path
       class="st3"
       d="m 269.69,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.51,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 V 58.83 H 273.4 V 46.65 c 0,-1.58 -0.28,-2.8 -1.85,-2.8 -1.57,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 z"
       id="path6089" />
    		<path
       class="st3"
       d="m 291.08,58.84 v -1.96 h -0.07 c -0.91,1.71 -2.27,2.31 -4.17,2.31 -5.11,0 -4.94,-5.67 -4.94,-9.31 0,-3.57 -0.14,-9.07 4.83,-9.07 1.79,0 3.01,0.53 4.03,2.03 h 0.07 v -9.28 h 4.94 v 25.27 h -4.69 z m -0.24,-9 c 0,-3.54 0.04,-5.99 -2,-5.99 -2.14,0 -2.1,2.45 -2.1,5.99 0,4.45 0.31,6.3 2.1,6.3 1.68,0 2,-1.85 2,-6.3 z"
       id="path6091" />
    		<path
       class="st3"
       d="m 307.53,46.2 c 0,-6.69 0,-13.06 8.72,-13.06 5.39,0 7.56,2.97 7.35,8.4 h -5.18 c 0,-3.36 -0.59,-4.62 -2.17,-4.62 -2.98,0 -3.36,2.8 -3.36,9.28 0,6.48 0.38,9.28 3.36,9.28 2.45,0 2.35,-3.15 2.42,-5.15 h 5.22 c 0,6.76 -2.7,8.93 -7.63,8.93 -8.73,0 -8.73,-6.44 -8.73,-13.06 z"
       id="path6093" />
    		<path
       class="st3"
       d="m 331.54,50.79 c 0,2.1 0.07,5.25 2.24,5.25 1.75,0 2.1,-1.68 2.1,-3.15 h 5.01 c -0.07,1.92 -0.7,3.5 -1.89,4.58 -1.15,1.08 -2.91,1.71 -5.22,1.71 -6.37,0 -7.21,-3.88 -7.21,-9.42 0,-4.83 0.7,-8.96 7.21,-8.96 6.65,0 7.39,4.31 7.21,9.98 h -9.45 z m 4.52,-2.77 c 0,-1.71 0.07,-4.17 -2.28,-4.17 -2.28,0 -2.24,2.66 -2.24,4.17 z"
       id="path6095" />
    		<path
       class="st3"
       d="m 349.42,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.51,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.85,-2.8 -1.57,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 z"
       id="path6097" />
    		<path
       class="st3"
       d="m 359.99,41.16 h 2 v -2.8 l 4.94,-2.21 v 5.01 h 2.56 v 3.04 h -2.56 v 9.45 c 0,1.33 -0.03,2.21 1.58,2.21 0.32,0 0.63,0 0.88,-0.07 v 3.04 C 368.72,58.9 368.02,59 366.83,59 362.56,59 362,56.17 362,55.08 V 44.2 h -2 v -3.04 z"
       id="path6099" />
    		<path
       class="st3"
       d="m 376.41,41.16 v 2.28 h 0.07 c 0.91,-2.03 2.59,-2.63 4.59,-2.63 v 4.41 c -4.34,-0.28 -4.41,2.24 -4.41,3.99 v 9.63 h -4.94 V 41.16 Z"
       id="path6101" />
    		<path
       class="st3"
       d="m 396.78,55.55 c 0,1.08 0.14,2.21 0.25,3.29 h -4.59 l -0.21,-2.35 h -0.07 c -1.05,1.82 -2.49,2.7 -4.62,2.7 -3.43,0 -4.69,-2.55 -4.69,-5.63 0,-5.85 4.52,-6.09 9.1,-6.02 v -1.36 c 0,-1.51 -0.21,-2.59 -2,-2.59 -1.71,0 -1.85,1.29 -1.85,2.7 h -4.83 c 0,-2.13 0.67,-3.5 1.82,-4.31 1.12,-0.84 2.73,-1.16 4.62,-1.16 6.27,0 7.07,2.7 7.07,5.92 v 8.81 z m -9.1,-2.21 c 0,1.26 0.21,2.8 1.82,2.8 2.91,0 2.45,-3.92 2.45,-5.85 -2.45,0.11 -4.27,-0.1 -4.27,3.05 z"
       id="path6103" />
    		<path
       class="st3"
       d="m 406.23,33.56 v 25.27 h -4.94 V 33.56 Z"
       id="path6105" />
    		<path
       class="st3"
       d="m 416.69,58.84 7,-25.27 h 6.97 l 6.86,25.27 h -5.57 l -1.4,-5.6 h -7.21 l -1.44,5.6 z m 10.19,-20.41 h -0.07 l -2.42,10.92 h 5.04 z"
       id="path6107" />
    		<path
       class="st3"
       d="m 443.64,53.17 c -0.04,0.81 0,1.58 0.25,2.14 0.28,0.56 0.8,0.84 1.79,0.84 0.98,0 1.82,-0.63 1.82,-1.82 0,-3.75 -8.68,-2.91 -8.68,-8.54 0,-3.82 3.78,-4.97 6.97,-4.97 3.36,0 6.41,1.61 6.13,5.43 h -4.83 c 0,-1.22 -0.14,-1.96 -0.49,-2.28 -0.32,-0.31 -0.74,-0.38 -1.26,-0.38 -1.08,0 -1.68,0.7 -1.68,1.89 0,2.8 8.68,2.66 8.68,8.33 0,3.08 -2.52,5.39 -6.62,5.39 -4.31,0 -7.18,-1.08 -6.9,-6.02 h 4.82 z"
       id="path6109" />
    		<path
       class="st3"
       d="m 460.65,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 h -4.94 V 41.16 h 4.94 z"
       id="path6111" />
    		<path
       class="st3"
       d="m 478.43,55.55 c 0,1.08 0.14,2.21 0.25,3.29 h -4.58 l -0.21,-2.35 h -0.07 c -1.05,1.82 -2.49,2.7 -4.62,2.7 -3.43,0 -4.69,-2.55 -4.69,-5.63 0,-5.85 4.51,-6.09 9.1,-6.02 v -1.36 c 0,-1.51 -0.21,-2.59 -2,-2.59 -1.71,0 -1.86,1.29 -1.86,2.7 h -4.83 c 0,-2.13 0.67,-3.5 1.82,-4.31 1.12,-0.84 2.73,-1.16 4.62,-1.16 6.27,0 7.07,2.7 7.07,5.92 v 8.81 z m -9.1,-2.21 c 0,1.26 0.21,2.8 1.82,2.8 2.91,0 2.45,-3.92 2.45,-5.85 -2.45,0.11 -4.27,-0.1 -4.27,3.05 z"
       id="path6113" />
    		<path
       class="st3"
       d="m 490.3,46.2 c 0,-6.69 0,-13.06 8.72,-13.06 5.39,0 7.56,2.97 7.35,8.4 h -5.18 c 0,-3.36 -0.6,-4.62 -2.17,-4.62 -2.97,0 -3.36,2.8 -3.36,9.28 0,6.48 0.39,9.28 3.36,9.28 2.45,0 2.35,-3.15 2.42,-5.15 h 5.21 c 0,6.76 -2.7,8.93 -7.63,8.93 -8.72,0 -8.72,-6.44 -8.72,-13.06 z"
       id="path6115" />
    		<path
       class="st3"
       d="M 518.4,58.84 V 46.65 c 0,-1.58 -0.28,-2.8 -1.86,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 33.56 h 4.94 v 9.38 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.5,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 v 14.18 h -4.93 z"
       id="path6117" />
    		<path
       class="st3"
       d="m 532.61,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 h -4.94 V 41.16 h 4.94 z"
       id="path6119" />
    		<path
       class="st3"
       d="M 542.34,33.56 V 58.83 H 537.4 V 33.56 Z"
       id="path6121" />
    		<path
       class="st3"
       d="m 555.54,58.84 v -1.96 h -0.07 c -0.91,1.71 -2.28,2.31 -4.17,2.31 -5.11,0 -4.94,-5.67 -4.94,-9.31 0,-3.57 -0.14,-9.07 4.83,-9.07 1.79,0 3.01,0.53 4.03,2.03 h 0.07 v -9.28 h 4.94 v 25.27 h -4.69 z m -0.25,-9 c 0,-3.54 0.04,-5.99 -2,-5.99 -2.14,0 -2.1,2.45 -2.1,5.99 0,4.45 0.32,6.3 2.1,6.3 1.69,0 2,-1.85 2,-6.3 z"
       id="path6123" />
    		<path
       class="st3"
       d="m 577.41,58.84 h -5.29 V 33.56 h 9.77 c 3.61,0 5.92,2.31 5.92,6.62 0,3.22 -1.26,5.64 -4.69,6.2 v 0.07 c 1.15,0.14 4.58,0.42 4.58,4.97 0,1.61 0.11,6.37 0.59,7.42 h -5.18 c -0.7,-1.54 -0.56,-3.25 -0.56,-4.9 0,-3.01 0.28,-5.57 -3.78,-5.57 h -1.37 v 10.47 z m 0,-14.36 h 2.35 c 2.1,0 2.7,-2.1 2.7,-3.71 0,-2.42 -1.02,-3.33 -2.7,-3.33 h -2.35 z"
       id="path6125" />
    		<path
       class="st3"
       d="m 596.8,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 h -4.94 V 41.16 h 4.94 z"
       id="path6127" />
    		<path
       class="st3"
       d="m 614.69,41.16 v 18.41 c 0,1.22 0.07,6.06 -6.72,6.06 -3.68,0 -6.83,-0.95 -6.93,-5.25 h 4.83 c 0,0.74 0.11,1.37 0.42,1.79 0.32,0.46 0.88,0.7 1.65,0.7 1.23,0 1.82,-1.16 1.82,-2.94 v -3.4 h -0.07 c -0.73,1.37 -2.13,2.07 -3.75,2.07 -5.43,0 -5.18,-4.97 -5.18,-8.96 0,-3.89 0.07,-8.82 5.22,-8.82 1.75,0 3.25,0.77 3.96,2.42 H 610 v -2.07 h 4.69 z m -6.97,14.39 c 1.79,0 2.03,-1.86 2.03,-5.6 0,-3.89 -0.17,-6.09 -2,-6.09 -1.86,0 -2.17,1.29 -2.17,6.69 0.01,1.64 -0.24,5 2.14,5 z"
       id="path6129" />
    		<path
       class="st3"
       d="M 627.32,58.84 V 46.65 c 0,-1.58 -0.28,-2.8 -1.86,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 33.56 h 4.94 v 9.38 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.5,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 v 14.18 h -4.93 z"
       id="path6131" />
    		<path
       class="st3"
       d="m 634.18,41.16 h 2 v -2.8 l 4.94,-2.21 v 5.01 h 2.56 v 3.04 h -2.56 v 9.45 c 0,1.33 -0.04,2.21 1.58,2.21 0.32,0 0.63,0 0.88,-0.07 v 3.04 c -0.67,0.07 -1.37,0.17 -2.55,0.17 -4.27,0 -4.83,-2.83 -4.83,-3.92 V 44.2 h -2 v -3.04 z"
       id="path6133" />
    		<path
       class="st3"
       d="m 649.79,53.17 c -0.04,0.81 0,1.58 0.25,2.14 0.28,0.56 0.8,0.84 1.79,0.84 0.98,0 1.82,-0.63 1.82,-1.82 0,-3.75 -8.68,-2.91 -8.68,-8.54 0,-3.82 3.78,-4.97 6.97,-4.97 3.36,0 6.41,1.61 6.13,5.43 h -4.83 c 0,-1.22 -0.14,-1.96 -0.49,-2.28 -0.32,-0.31 -0.74,-0.38 -1.26,-0.38 -1.08,0 -1.68,0.7 -1.68,1.89 0,2.8 8.68,2.66 8.68,8.33 0,3.08 -2.52,5.39 -6.62,5.39 -4.31,0 -7.18,-1.08 -6.9,-6.02 h 4.82 z"
       id="path6135" />
    		<path
       class="st3"
       d="m 682.62,55.55 c 0,1.08 0.14,2.21 0.25,3.29 h -4.58 l -0.21,-2.35 H 678 c -1.05,1.82 -2.49,2.7 -4.62,2.7 -3.43,0 -4.69,-2.55 -4.69,-5.63 0,-5.85 4.51,-6.09 9.1,-6.02 v -1.36 c 0,-1.51 -0.21,-2.59 -2,-2.59 -1.71,0 -1.86,1.29 -1.86,2.7 h -4.83 c 0,-2.13 0.67,-3.5 1.82,-4.31 1.12,-0.84 2.73,-1.16 4.62,-1.16 6.27,0 7.07,2.7 7.07,5.92 v 8.81 z m -9.1,-2.21 c 0,1.26 0.21,2.8 1.82,2.8 2.91,0 2.45,-3.92 2.45,-5.85 -2.45,0.11 -4.27,-0.1 -4.27,3.05 z"
       id="path6137" />
    		<path
       class="st3"
       d="m 691.65,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.5,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.86,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 V 58.83 H 686.7 V 41.16 h 4.94 v 1.78 z"
       id="path6139" />
    		<path
       class="st3"
       d="m 713.04,58.84 v -1.96 h -0.07 c -0.91,1.71 -2.28,2.31 -4.17,2.31 -5.11,0 -4.94,-5.67 -4.94,-9.31 0,-3.57 -0.14,-9.07 4.83,-9.07 1.79,0 3.01,0.53 4.03,2.03 h 0.07 v -9.28 h 4.94 v 25.27 h -4.69 z m -0.25,-9 c 0,-3.54 0.04,-5.99 -2,-5.99 -2.14,0 -2.1,2.45 -2.1,5.99 0,4.45 0.32,6.3 2.1,6.3 1.69,0 2,-1.85 2,-6.3 z"
       id="path6141" />
    		<path
       class="st3"
       d="m 727.49,33.56 h 5.43 l 3.29,17.75 h 0.07 l 3.99,-17.75 h 6.23 l 3.78,17.75 h 0.07 l 3.15,-17.75 h 5.18 l -5.6,25.27 h -5.85 l -3.96,-18.48 h -0.07 l -4.38,18.48 h -5.74 z"
       id="path6143" />
    	</g>
    	<g
       class="st5"
       id="g6201">
    		<path
       class="st3"
       d="m 764.28,50.79 c 0,2.1 0.07,5.25 2.24,5.25 1.75,0 2.1,-1.68 2.1,-3.15 h 5 c -0.07,1.92 -0.7,3.5 -1.89,4.58 -1.16,1.08 -2.91,1.71 -5.22,1.71 -6.37,0 -7.21,-3.88 -7.21,-9.42 0,-4.83 0.7,-8.96 7.21,-8.96 6.65,0 7.39,4.31 7.21,9.98 h -9.44 z m 4.51,-2.77 c 0,-1.71 0.07,-4.17 -2.28,-4.17 -2.28,0 -2.24,2.66 -2.24,4.17 z"
       id="path6147" />
    		<path
       class="st3"
       d="m 782.58,33.56 v 25.27 h -4.94 V 33.56 Z"
       id="path6149" />
    		<path
       class="st3"
       d="m 792.31,33.56 v 25.27 h -4.94 V 33.56 Z"
       id="path6151" />
    		<path
       class="st3"
       d="m 796.69,33.56 h 4.94 v 9.28 h 0.07 c 1.02,-1.5 2.24,-2.03 4.03,-2.03 4.97,0 4.83,5.5 4.83,9.07 0,3.64 0.18,9.31 -4.94,9.31 -1.89,0 -3.25,-0.59 -4.17,-2.31 h -0.07 v 1.96 h -4.69 z m 9.03,16.28 c 0,-3.54 0.04,-5.99 -2.1,-5.99 -2.03,0 -2,2.45 -2,5.99 0,4.45 0.32,6.3 2,6.3 1.78,0 2.1,-1.85 2.1,-6.3 z"
       id="path6153" />
    		<path
       class="st3"
       d="m 818.74,50.79 c 0,2.1 0.07,5.25 2.24,5.25 1.75,0 2.1,-1.68 2.1,-3.15 h 5.01 c -0.07,1.92 -0.7,3.5 -1.89,4.58 -1.15,1.08 -2.9,1.71 -5.21,1.71 -6.37,0 -7.21,-3.88 -7.21,-9.42 0,-4.83 0.7,-8.96 7.21,-8.96 6.65,0 7.39,4.31 7.21,9.98 h -9.46 z m 4.51,-2.77 c 0,-1.71 0.07,-4.17 -2.28,-4.17 -2.28,0 -2.24,2.66 -2.24,4.17 z"
       id="path6155" />
    		<path
       class="st3"
       d="m 837.04,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 H 832.1 V 41.16 h 4.94 z"
       id="path6157" />
    		<path
       class="st3"
       d="m 846.35,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.5,-0.49 2.42,-0.49 2.34,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.85,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 v 1.78 z"
       id="path6159" />
    		<path
       class="st3"
       d="m 872.43,41.16 v 18.41 c 0,1.22 0.07,6.06 -6.72,6.06 -3.68,0 -6.83,-0.95 -6.93,-5.25 h 4.83 c 0,0.74 0.1,1.37 0.42,1.79 0.32,0.46 0.88,0.7 1.65,0.7 1.22,0 1.82,-1.16 1.82,-2.94 v -3.4 h -0.07 c -0.74,1.37 -2.13,2.07 -3.75,2.07 -5.43,0 -5.18,-4.97 -5.18,-8.96 0,-3.89 0.07,-8.82 5.21,-8.82 1.75,0 3.26,0.77 3.96,2.42 h 0.07 v -2.07 h 4.69 z m -6.97,14.39 c 1.79,0 2.03,-1.86 2.03,-5.6 0,-3.89 -0.18,-6.09 -2,-6.09 -1.86,0 -2.17,1.29 -2.17,6.69 0.01,1.64 -0.24,5 2.14,5 z"
       id="path6161" />
    		<path
       class="st3"
       d="M 884.33,58.84 V 33.56 h 8.51 l 3.96,17.19 h 0.07 l 4.2,-17.19 h 8.23 v 25.27 h -5.15 v -19.5 h -0.07 l -4.87,19.5 h -5.04 l -4.62,-19.5 h -0.07 v 19.5 h -5.15 z"
       id="path6163" />
    		<path
       class="st3"
       d="m 912.92,49.77 c 0,-4.83 0.7,-8.96 7.21,-8.96 6.51,0 7.21,4.13 7.21,8.96 0,5.53 -0.84,9.42 -7.21,9.42 -6.37,0 -7.21,-3.89 -7.21,-9.42 z m 9.49,-0.28 c 0,-3.68 -0.18,-5.53 -2.28,-5.53 -2.1,0 -2.28,1.86 -2.28,5.53 0,5.39 0.46,6.54 2.28,6.54 1.82,0 2.28,-1.15 2.28,-6.54 z"
       id="path6165" />
    		<path
       class="st3"
       d="m 935.78,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.51,-0.49 2.42,-0.49 2.34,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.86,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 v 1.78 z"
       id="path6167" />
    		<path
       class="st3"
       d="m 953.7,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 h -4.94 V 41.16 h 4.94 z"
       id="path6169" />
    		<path
       class="st3"
       d="m 956.07,41.16 h 2 v -2.8 l 4.94,-2.21 v 5.01 h 2.55 v 3.04 h -2.55 v 9.45 c 0,1.33 -0.04,2.21 1.57,2.21 0.32,0 0.63,0 0.88,-0.07 v 3.04 c -0.67,0.07 -1.37,0.17 -2.56,0.17 -4.27,0 -4.83,-2.83 -4.83,-3.92 V 44.2 h -2 v -3.04 z"
       id="path6171" />
    		<path
       class="st3"
       d="m 967.38,49.77 c 0,-4.83 0.7,-8.96 7.21,-8.96 6.51,0 7.21,4.13 7.21,8.96 0,5.53 -0.84,9.42 -7.21,9.42 -6.37,0 -7.21,-3.89 -7.21,-9.42 z m 9.49,-0.28 c 0,-3.68 -0.17,-5.53 -2.28,-5.53 -2.11,0 -2.28,1.86 -2.28,5.53 0,5.39 0.46,6.54 2.28,6.54 1.82,0 2.28,-1.15 2.28,-6.54 z"
       id="path6173" />
    		<path
       class="st3"
       d="m 989.99,41.16 v 2.28 h 0.07 c 0.91,-2.03 2.59,-2.63 4.59,-2.63 v 4.41 c -4.34,-0.28 -4.41,2.24 -4.41,3.99 v 9.63 H 985.3 V 41.16 Z"
       id="path6175" />
    		<path
       class="st3"
       d="m 1002.31,33.56 v 3.88 h -4.94 v -3.88 z m 0,25.28 h -4.94 V 41.16 h 4.94 z"
       id="path6177" />
    		<path
       class="st3"
       d="m 1011.62,42.94 h 0.07 c 0.49,-0.8 1.08,-1.33 1.75,-1.65 0.7,-0.35 1.5,-0.49 2.42,-0.49 2.35,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.86,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 v 1.78 z"
       id="path6179" />
    		<path
       class="st3"
       d="m 1037.7,41.16 v 18.41 c 0,1.22 0.07,6.06 -6.72,6.06 -3.68,0 -6.83,-0.95 -6.93,-5.25 h 4.83 c 0,0.74 0.11,1.37 0.42,1.79 0.32,0.46 0.88,0.7 1.65,0.7 1.23,0 1.82,-1.16 1.82,-2.94 v -3.4 h -0.07 c -0.73,1.37 -2.13,2.07 -3.75,2.07 -5.43,0 -5.18,-4.97 -5.18,-8.96 0,-3.89 0.07,-8.82 5.22,-8.82 1.75,0 3.25,0.77 3.96,2.42 h 0.07 v -2.07 h 4.68 z m -6.97,14.39 c 1.79,0 2.03,-1.86 2.03,-5.6 0,-3.89 -0.17,-6.09 -2,-6.09 -1.86,0 -2.17,1.29 -2.17,6.69 0.01,1.64 -0.24,5 2.14,5 z"
       id="path6181" />
    		<path
       class="st3"
       d="M 1057.36,58.84 V 33.56 h 13.13 v 3.88 h -7.84 v 6.48 h 7.49 v 3.88 h -7.49 v 11.03 h -5.29 z"
       id="path6183" />
    		<path
       class="st3"
       d="m 1077.45,41.16 v 2.28 h 0.07 c 0.91,-2.03 2.59,-2.63 4.59,-2.63 v 4.41 c -4.34,-0.28 -4.41,2.24 -4.41,3.99 v 9.63 h -4.94 V 41.16 Z"
       id="path6185" />
    		<path
       class="st3"
       d="m 1097.82,55.55 c 0,1.08 0.14,2.21 0.25,3.29 h -4.58 l -0.21,-2.35 h -0.07 c -1.05,1.82 -2.49,2.7 -4.62,2.7 -3.43,0 -4.69,-2.55 -4.69,-5.63 0,-5.85 4.51,-6.09 9.1,-6.02 v -1.36 c 0,-1.51 -0.21,-2.59 -2,-2.59 -1.71,0 -1.86,1.29 -1.86,2.7 h -4.83 c 0,-2.13 0.67,-3.5 1.82,-4.31 1.12,-0.84 2.73,-1.16 4.62,-1.16 6.27,0 7.07,2.7 7.07,5.92 z m -9.1,-2.21 c 0,1.26 0.21,2.8 1.82,2.8 2.91,0 2.45,-3.92 2.45,-5.85 -2.45,0.11 -4.27,-0.1 -4.27,3.05 z"
       id="path6187" />
    		<path
       class="st3"
       d="m 1106.47,42.94 h 0.07 c 0.98,-1.58 2.31,-2.14 4.17,-2.14 1.75,0 3.15,0.84 3.96,2.24 1.16,-1.54 2.56,-2.24 4.59,-2.24 2.34,0 4.41,1.4 4.41,3.85 v 14.18 h -4.94 V 46.65 c 0,-1.58 -0.28,-2.8 -1.85,-2.8 -1.58,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.83 V 46.65 c 0,-1.58 -0.28,-2.8 -1.85,-2.8 -1.57,0 -1.86,1.22 -1.86,2.8 v 12.18 h -4.94 V 41.16 h 4.94 v 1.78 z"
       id="path6189" />
    		<path
       class="st3"
       d="m 1131.74,50.79 c 0,2.1 0.07,5.25 2.24,5.25 1.75,0 2.1,-1.68 2.1,-3.15 h 5 c -0.07,1.92 -0.7,3.5 -1.89,4.58 -1.16,1.08 -2.91,1.71 -5.22,1.71 -6.37,0 -7.21,-3.88 -7.21,-9.42 0,-4.83 0.7,-8.96 7.21,-8.96 6.65,0 7.39,4.31 7.21,9.98 h -9.44 z m 4.51,-2.77 c 0,-1.71 0.07,-4.17 -2.28,-4.17 -2.28,0 -2.24,2.66 -2.24,4.17 z"
       id="path6191" />
    		<path
       class="st3"
       d="m 1143.11,41.16 h 4.9 l 2.42,13.3 h 0.07 l 3.4,-13.3 h 5.11 l 3.12,13.3 h 0.07 l 2.66,-13.3 h 4.73 l -4.79,17.68 h -5.18 l -3.19,-12.08 h -0.07 l -3.57,12.08 h -5.25 z"
       id="path6193" />
    		<path
       class="st3"
       d="m 1171.5,49.77 c 0,-4.83 0.7,-8.96 7.21,-8.96 6.51,0 7.21,4.13 7.21,8.96 0,5.53 -0.84,9.42 -7.21,9.42 -6.37,0 -7.21,-3.89 -7.21,-9.42 z m 9.48,-0.28 c 0,-3.68 -0.17,-5.53 -2.28,-5.53 -2.11,0 -2.28,1.86 -2.28,5.53 0,5.39 0.46,6.54 2.28,6.54 1.82,0 2.28,-1.15 2.28,-6.54 z"
       id="path6195" />
    		<path
       class="st3"
       d="m 1194.11,41.16 v 2.28 h 0.07 c 0.91,-2.03 2.59,-2.63 4.59,-2.63 v 4.41 c -4.34,-0.28 -4.41,2.24 -4.41,3.99 v 9.63 h -4.94 V 41.16 Z"
       id="path6197" />
    		<path
       class="st3"
       d="M 1200.97,58.84 V 33.56 h 4.94 v 15.05 h 0.07 l 4.45,-7.46 h 5.15 l -5.01,7.88 5.57,9.8 h -5.57 l -4.59,-9.63 h -0.07 v 9.63 h -4.94 z"
       id="path6199" />
    	</g>
    	<path
       class="st54"
       d="m 766.05,209.34 c 0.06,-0.06 0.19,-0.03 0.3,-0.05 0.77,-0.11 1.53,-0.06 2.3,-0.01 1.6,0.12 3.22,0.1 4.82,0.29 0.39,0.05 0.79,0.13 1.18,0.04 0.96,-0.23 1.38,-0.96 1.68,-1.8 0.13,-0.35 0.07,-0.68 -0.11,-1.01 -0.35,-0.62 -0.91,-0.95 -1.56,-1.16 -1.65,-0.52 -3.35,-0.8 -5.08,-0.9 -1.4,-0.08 -2.73,-0.3 -3.98,-1.02 -1.13,-0.65 -2.37,-1.08 -3.67,-1.3 -3.04,-0.52 -5.98,0.05 -8.89,0.88 -0.36,0.1 -0.53,0.36 -0.53,0.73 0,0.44 0,0.89 0,1.33 0,1.84 0,3.68 0,5.53 0,0.53 0.26,0.88 0.72,0.91 1.14,0.06 2.17,0.45 3.19,0.93 2.51,1.17 4.97,2.43 7.51,3.53 1,0.43 2,0.85 3.12,0.71 0.67,-0.08 1.34,-0.14 2.01,-0.24 1.75,-0.26 3.49,-0.56 5.25,-0.8 1.05,-0.14 2.07,-0.29 2.97,-0.91 1.06,-0.74 2.14,-1.44 3.21,-2.17 0.48,-0.33 0.93,-0.7 1.35,-1.1 0.33,-0.31 0.55,-0.69 0.61,-1.15 0.03,-0.25 -0.01,-0.5 -0.27,-0.58 -0.37,-0.11 -0.29,-0.23 -0.08,-0.45 0.58,-0.63 0.45,-1.34 -0.31,-1.74 -0.39,-0.21 -0.81,-0.29 -1.25,-0.25 -1.17,0.09 -2.13,0.64 -2.96,1.42 -0.75,0.7 -1.61,1.13 -2.6,1.35 -0.78,0.17 -1.57,0.22 -2.35,0.32 -2.35,0.31 -4.55,-0.15 -6.58,-1.33"
       id="path6203" />
    	<path
       class="st54"
       d="m 751.5,207.54 v 0 c 0,-1.69 0,-3.38 0,-5.07 0,-0.61 -0.26,-0.86 -0.87,-0.86 -0.77,0 -1.54,0 -2.31,0 -0.55,0 -0.83,0.27 -0.83,0.81 0,3.4 0,6.81 0,10.21 0,0.56 0.25,0.82 0.8,0.82 0.78,0.01 1.56,0 2.34,0 0.63,0 0.86,-0.24 0.86,-0.87 0.01,-1.68 0.01,-3.36 0.01,-5.04"
       id="path6205" />
    	<path
       class="st54"
       d="m 781.89,189.96 c -1.94,-5.59 -7.37,-8.79 -13.19,-7.76 -5.55,0.98 -9.69,6.1 -9.49,11.74 0.1,2.77 1.04,5.21 2.83,7.32 0.14,0.17 0.3,0.27 0.52,0.31 1.17,0.23 2.29,0.62 3.33,1.21 1.18,0.67 2.45,0.92 3.78,1 1.65,0.09 3.27,0.35 4.85,0.79 0.15,0.04 0.27,0.02 0.4,-0.03 5.81,-2.09 8.99,-8.75 6.97,-14.58 z m -11.04,12.88 c -5.26,0 -9.54,-4.28 -9.54,-9.54 0,-5.26 4.28,-9.54 9.54,-9.54 5.26,0 9.54,4.28 9.54,9.54 0,5.26 -4.28,9.54 -9.54,9.54 z"
       id="path6207" />
    	<path
       class="st54"
       d="m 770.85,184.51 c -4.85,0 -8.79,3.94 -8.79,8.79 0,4.85 3.94,8.79 8.79,8.79 4.84,0 8.79,-3.94 8.79,-8.79 0,-4.84 -3.95,-8.79 -8.79,-8.79 z m 4.77,10.81 h -9.54 c -0.38,0 -0.69,-0.31 -0.69,-0.69 0,-0.38 0.31,-0.69 0.69,-0.69 h 9.54 c 0.38,0 0.69,0.31 0.69,0.69 0,0.39 -0.31,0.69 -0.69,0.69 z m 0,-2.67 h -9.54 c -0.38,0 -0.69,-0.31 -0.69,-0.69 0,-0.38 0.31,-0.69 0.69,-0.69 h 9.54 c 0.38,0 0.69,0.31 0.69,0.69 0,0.38 -0.31,0.69 -0.69,0.69 z"
       id="path6209" />
    	<line
       class="st72"
       x1="977.95001"
       y1="616.5"
       x2="1013.09"
       y2="616.5"
       id="line6211" />
    	<line
       class="st73"
       x1="1014.62"
       y1="619.46997"
       x2="1014.62"
       y2="644.75"
       id="line6213" />
    	<line
       class="st74"
       x1="1017.6"
       y1="646.23999"
       x2="1322.52"
       y2="646.23999"
       id="line6215" />
    	<path
       class="st33"
       d="m 974.9,616.5 v 0 m 39.72,0 v 0 m 0,29.74 v 0 m 309.38,0 v 0"
       id="path6217" />
    	<path
       class="st3"
       d="m 974.9,619.28 c 1.53,0 2.77,-1.24 2.77,-2.78 0,-1.54 -1.24,-2.78 -2.77,-2.78 -1.53,0 -2.78,1.24 -2.78,2.78 0,1.54 1.24,2.78 2.78,2.78 z"
       id="path6219" />
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
