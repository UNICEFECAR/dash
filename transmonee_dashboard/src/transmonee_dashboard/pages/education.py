import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "PARTICIPATION": {
        "NAME": "Participation",
        "CARDS": [
            {
                "name": "Total Number OOS (P+LS+US)",
                "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Children, Adolescents and Youth",
            },
            {
                "name": "Number of Girls OOS (P+LS+US)",
                "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Female Children, Adolescents and Youth",
                "sex": "F",
            },
            {
                "name": "Total Number OOS Under-1 Year (P)",
                "indicator": "EDUNF_OFST_L1_UNDER1",
                "suffix": "Children under-1 year of the primary official entry age",
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
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT",
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NERA_L1",
                "EDUNF_NERA_L2",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3",
                "EDUNF_NIR_L1_ENTRYAGE",
            ],
            "default": "EDUNF_ROFST_L3",
        },
        "RIGHT": {
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
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_STU_L1_TOT",
                "EDUNF_STU_L2_TOT",
                "EDUNF_STU_L3_TOT",
                "EDUNF_NER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NERA_L1",
                "EDUNF_NERA_L2",
                "EDUNF_GER_L1",
                "EDUNF_GER_L2",
                "EDUNF_GER_L3",
                "EDUNF_NIR_L1_ENTRYAGE",
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
                "EDU_CHLD_DISAB_L02",
                "EDU_CHLD_DISAB_L1",
                "EDU_CHLD_DISAB_L2",
                "EDU_CHLD_DISAB_L3",
            ],
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
                "name": "Total Number of Repeaters (P+LS)",
                "indicator": "EDUNF_RPTR_L1,EDUNF_RPTR_L2",
                "suffix": "Children and Adolescents",
            },
            {
                "name": "Total Number of Early School Leavers (P)",
                "indicator": "EDUNF_ESL_L1",
                "suffix": "Children",
            },
            {
                "name": "Number of Countries assessing both Math and Reading learning (End Primary)",
                "indicator": "EDUNF_ADMIN_L1_GLAST_REA,EDUNF_ADMIN_L1_GLAST_MAT",
                "suffix": "Countries",
            },
            {
                "name": "Number of Countries participating in PISA",
                "indicator": "EDU_PISA_MAT,EDU_PISA_REA,EDU_PISA_SCI",
                "suffix": "Countries",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "PISA: 15-year-olds achieving proficiency Level 2 (%)",
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
            "indicators": ["EDU_PISA_MAT2", "EDU_PISA_REA2", "EDU_PISA_SCI2",],
        },
        "LEFT": {
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
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
        "RIGHT": {
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
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
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
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
    },
    "GOVERNANCE": {
        "NAME": "Governance",
        "CARDS": [
            {
                "name": "Number of Countries guaranteeing free education (Pre-Primary 1+ years)",
                "indicator": "EDU_SDG_FREE_EDU_L02",
                "suffix": "Countries",
            },
            {
                "name": "Enrolments in Private Institutions (P+LS+US)",
                "indicator": "EDUNF_STU_L1_PRV,EDUNF_STU_L2_PRV,EDUNF_STU_L3_PRV",
                "suffix": "Children, Adolescents and Youth",
            },
            {
                "name": "Total Number of classroom teachers (P+LS+US)",
                "indicator": "EDUNF_TEACH_L1,EDUNF_TEACH_L2,EDUNF_TEACH_L3",
                "suffix": "Persons",
            },
        ],
        "MAIN": {
            "name": "PISA: 15-year-olds achieving proficiency Level 2 (%)",
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
            "indicators": ["EDU_PISA_MAT2", "EDU_PISA_REA2", "EDU_PISA_SCI2",],
        },
        "LEFT": {
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
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
        "RIGHT": {
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
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_G2OR3_REA",
            ],
            "default": "EDU_SDG_STU_L2_GLAST_MAT",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
