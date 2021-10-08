import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, State, Output
from .base_page import get_base_layout, geo_json_countries
import plotly.express as px

indicators_dict = {
    "ADOLESCENT": {
        "NAME": "Adolescent",
        "CARDS": [
            {
                "name": "Card Unit",
                "indicator": "",
                "suffix": "Card Name",
                # "absolute": True,
                "min_max": True,
            },
            {
                "name": "Card Unit",
                "indicator": "",
                "suffix": "Card Name",
                # "absolute": True,
                "min_max": True,
            },
            {
                "name": "Card Unit",
                "indicator": "",
                "suffix": "Card Name",
                # "absolute": True,
                "min_max": True,
            },
            {
                "name": "Card Unit",
                "indicator": "",
                "suffix": "Card Name",
                # "absolute": True,
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Adolescent",
            "geo": "Geographic area",
            "options": dict(
                geojson=geo_json_countries,
                locations="REF_AREA",
                featureidkey="id",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                mapbox_style="carto-positron",
                zoom=2,
                center={"lat": 48.3794, "lon": 31.1656},
                opacity=0.5,
                labels={
                    "OBS_VALUE": "Value",
                    "Geographic area": "Country",
                    "TIME_PERIOD": "Year",
                    "REF_AREA": "ISO3 Code",
                },
                hover_data={
                    "OBS_VALUE": True,
                    "REF_AREA": False,
                    "Geographic area": True,
                    "TIME_PERIOD": True,
                },
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PV_SI_POV_EMP1",
                "PV_SI_POV_DAY1",
                "PV_SI_POV_UMIC",
                "PV_SDG_SI_POV_NAHC",
                "PV_WB_SI_POV_NAHC",
                "PV_AROPE",
                "PV_AROPRT",
                "PV_SD_MDP_CSMP",
                "PV_SD_MDP_MUHHC",
                "PV_SD_MDP_MUHC",
                "PV_SI_POV_MDIM",
                "PV_SI_POV_MDIM_17",
                "WS_PPL_W-B",
                "WS_PPL_S-B",
                "PV_SEV_MAT_DPRT",
            ],
            "default": "PV_SEV_MAT_DPRT",
        },
        "AREA_1": {
            "name": "Education",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "indicators": [
                "EDU_PISA_MAT",
                "EDU_PISA_REA",
                "EDU_PISA_SCI",
                "ED_ANAR_L2",
                "ED_ANAR_L3",
                "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
                "EDUNF_ROFST_L2",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "ICT_SKILL_COPY",
                "ICT_SKILL_CONNECT",
                "ICT_SKILL_CREATE",
                "ICT_SKILL_DUP",
                "ICT_SKILL_AT",
                "ICT_SKILL_FORM",
                "ICT_SKILL_SOFT",
                "ICT_SKILL_TRAN",
                "ICT_SKILL_PROG",
                "EDUNF_OFST_L2",
                "EDUNF_OFST_L3",
                "EDU_SDG_YOUTH_NEET",
                "EDUNF_GER_L2_VOC",
                "EDUNF_GER_L3_VOC",
                "EDUNF_GER_L2_GEN",
                "EDUNF_GER_L3_GEN",
            ],
            "default": "EDU_PISA_MAT",
        },
        "AREA_2": {
            "name": "Family Environment and Protection",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
            ],
            "default_graph": "line",
            "default": "PT_ST_13-15_BUL_30-DYS",
        },
        "AREA_3": {
            "name": "Health and Nutrition",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "HT_ADOL_MT",
                "SP_DYN_ADKL",
                "HT_ADOL_UNMETMED_NOUNMET",
                "HT_ADOL_UNMETMED_TOOEXP",
                "HT_ADOL_UNMETMED_TOOFAR",
                "HT_ADOL_UNMETMED_WAITING",
                "HT_ADOL_UNMETMED_TOOEFW",
                "HT_ADOL_UNMETMED_NOTIME",
                "HT_ADOL_UNMETMED_NOKNOW",
                "HT_ADOL_UNMETMED_FEAR",
                "HT_ADOL_UNMETMED_HOPING",
                "HT_ADOL_UNMETMED_OTH",
                "HT_ADOL_MEAL",
                "HT_ADOL_NO_EXCS",
                "HT_ADOL_VGRS_EXCS",
                "HT_ADOL_HIGH_SATS",
                "HT_ADOL_LOW_SATS",
            ],
            "default_graph": "bar",
            "default": "HT_ADOL_MT",
        },
        "AREA_4": {
            "name": "Poverty",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [],
            "default_graph": "bar",
            "default": "",
        },
        "AREA_5": {
            "name": "Child Rights Landscape",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "DM_ADOL_POP",
            ],
            "default_graph": "bar",
            "default": "DM_ADOL_POP",
        },
        "AREA_6": {
            "name": "Participation",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Geographic area",
                        hover_name="Geographic area",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
            ],
            "default_graph": "bar",
            "default": "PP_ADOL_TVGM",
        },
    },
}

main_title = "Adolescent"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    kwargs["only_gender"] = True
    return get_base_layout(**kwargs)


def get_layout2(**kwargs):
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
