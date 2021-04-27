import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "PARTICIPATION": {
        "NAME": "Participation",
        "CARDS": [
            {
                "name": "who are out-of-school",
                "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "primary-to-upper-secondary-aged children and adolescents",
            },
            {
                "name": "who are out-of-school",
                "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "primary-to-upper-secondary-aged girls",
                "sex": "F",
            },
            {
                "name": "who are out-of-school",
                "indicator": "EDUNF_OFST_L1_UNDER1",
                "suffix": "children one year younger than the official primary entry age",
            },
        ],
        "MAIN": {
            "name": "Out of School Children",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=3,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_OFST_L1",
                "EDUNF_OFST_L2",
                "EDUNF_OFST_L3",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
            "default_graph": "line",
            "indicators": [
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NERA_L1",
                "EDUNF_NERA_L2",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3",
                "EDUNF_NIR_L1_ENTRYAGE",
                "EDUNF_TRANRA_L2",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_SCH_L1",
                "EDU_SDG_SCH_L2",
                "EDU_SDG_SCH_L3",
                "WS_SCH_H-B",
                "WS_SCH_S-B",
                "WS_SCH_W-B",
                "EDU_CHLD_DISAB",
                "EDU_CHLD_DISAB_GENERAL",
                "EDU_CHLD_DISAB_SPECIAL",
            ],
            "default": "EDU_CHLD_DISAB",
        },
        "AREA_4": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
                "EDUNF_DR_L1",
                "EDUNF_DR_L2",
                "EDUNF_GER_L2",
                "EDUNF_GER_L2_GEN",
                "EDUNF_GER_L2_VOC",
                "EDUNF_GER_L3",
                "EDUNF_GER_L3_GEN",
                "EDUNF_GER_L3_VOC",
            ],
            "default": "EDUNF_CR_L1",
        },
    },
    "QUALITY": {
        "NAME": "Learning Quality",
        "CARDS": [
            {
                "name": "(enrolled in the same grade for a second or further year) in primary and lower secondary education",
                "indicator": "EDUNF_RPTR_L1,EDUNF_RPTR_L2",
                "suffix": "children and adolescent repeaters",
            },
            {
                "name": "from primary education",
                "indicator": "EDUNF_ESL_L1",
                "suffix": "early school leavers",
            },
            {
                "name": "administering nationally representative learning assessment in both reading and math at the end of primary education",
                "indicator": "EDUNF_ADMIN_L1_GLAST_REA,EDUNF_ADMIN_L1_GLAST_MAT",
                "suffix": "countries",
            },
            {
                "name": "participating in the latest round of PISA",
                "indicator": "EDU_PISA_MAT,EDU_PISA_REA,EDU_PISA_SCI",
                "suffix": "countries",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "PISA: Mean performance for 15-year-old students",
            "geo": "Country",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": ["EDU_PISA_MAT", "EDU_PISA_REA", "EDU_PISA_SCI"],
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "ECD_CHLD_36-59M_LMPSL",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDUNF_LR_YOUTH",
                "EDUNF_LR_ADULT",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
            "default_graph": "line",
            "indicators": [
                "ECD_CHLD_36-59M_LMPSL",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDUNF_LR_YOUTH",
                "EDUNF_LR_ADULT",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_REA",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_TRTP_L02",
                "EDU_SDG_TRTP_L1",
                "EDU_SDG_TRTP_L2",
                "EDU_SDG_TRTP_L3",
            ],
            "default": "EDU_SDG_TRTP_L2",
        },
        "AREA_4": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "EDU_SDG_QUTP_L02",
                "EDU_SDG_QUTP_L1",
                "EDU_SDG_QUTP_L2",
                "EDU_SDG_QUTP_L3",
            ],
            "default": "EDU_SDG_QUTP_L2",
        },
    },
    "GOVERNANCE": {
        "NAME": "Governance",
        "CARDS": [
            {
                "name": "guaranteeing at least one year of free pre-primary education in their legal frameworks",
                "indicator": "EDU_SDG_FREE_EDU_L02",
                "suffix": "countries",
            },
            {
                "name": "enrolled in private institutions (primary, lower secondary and upper secondary education)",
                "indicator": "EDUNF_STU_L1_PRV,EDUNF_STU_L2_PRV,EDUNF_STU_L3_PRV",
                "suffix": "children and adolescents",
            },
            {
                "name": "total in primary, lower secondary and upper secondary education",
                "indicator": "EDUNF_TEACH_L1,EDUNF_TEACH_L2,EDUNF_TEACH_L3",
                "suffix": "classroom teachers",
            },
        ],
        "MAIN": {
            "name": "Education Expenditures and Legal Frameworks",
            "geo": "Country",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "EDU_FIN_EXP_PT_GDP",
                "EDU_FIN_EXP_PT_TOT",
                "EDU_SDG_FREE_EDU_L02",
                "EDU_SDG_COMP_EDU_L02",
            ],
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                color="Sex",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_PRP_L02",
                "EDUNF_PRP_L1",
                "EDUNF_PRP_L2",
                "EDUNF_PRP_L3",
                "EDUNF_STU_L01_PUB",
                "EDUNF_STU_L02_PUB",
                "EDUNF_STU_L1_PUB",
                "EDUNF_STU_L2_PUB",
                "EDUNF_STU_L3_PUB",
                "EDUNF_STU_L01_PRV",
                "EDUNF_STU_L02_PRV",
                "EDUNF_STU_L1_PRV",
                "EDUNF_STU_L2_PRV",
                "EDUNF_STU_L3_PRV",
            ],
            "default": "EDUNF_PRP_L1",
        },
        "AREA_2": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
            "default_graph": "line",
            "indicators": [
                "EDUNF_PRP_L02",
                "EDUNF_PRP_L1",
                "EDUNF_PRP_L2",
                "EDUNF_PRP_L3",
                "EDUNF_STU_L01_PUB",
                "EDUNF_STU_L02_PUB",
                "EDUNF_STU_L1_PUB",
                "EDUNF_STU_L2_PUB",
                "EDUNF_STU_L3_PUB",
                "EDUNF_STU_L01_PRV",
                "EDUNF_STU_L02_PRV",
                "EDUNF_STU_L1_PRV",
                "EDUNF_STU_L2_PRV",
                "EDUNF_STU_L3_PRV",
            ],
            "default": "EDUNF_PRP_L2",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_FIN_EXP_L02",
                "EDU_FIN_EXP_L1",
                "EDU_FIN_EXP_L2",
                "EDU_FIN_EXP_L3",
                "EDU_FIN_EXP_L4",
                "EDU_FIN_EXP_L5T8",
            ],
            "default": "EDU_FIN_EXP_L2",
        },
        "AREA_4": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "EDUNF_ADMIN_L1_GLAST_REA",
                "EDUNF_ADMIN_L1_GLAST_MAT",
                "EDUNF_ADMIN_L2_REA",
                "EDUNF_ADMIN_L2_MAT",
                "EDUNF_ADMIN_L1_G2OR3_REA",
                "EDUNF_ADMIN_L1_G2OR3_MAT",
            ],
            "default": "EDUNF_ADMIN_L2_MAT",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
