import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "REGISTRATION": {
        "NAME": "Birth registration and documentation",
        "CARDS": [
            {
                "name": "whose births have been registered with a civil authority (%, by sex, age groups, residence and wealth quintile)",
                "indicator": "PT_CHLD_Y0T4_REG",
                "suffix": "Proportion of Children",
                "absolute": True,
            },
            {
                "name": "with birth registration data that are at least 90 percent complete",
                "indicator": "PP_SG_REG_BRTH90N",
                "suffix": "Countries",
            },
        ],
        "MAIN": {
            "name": "Poverty and Deprivation",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PT_CHLD_Y0T4_REG",
                "PP_SG_REG_BRTH90N",
                "PP_SG_REG_DETH75N",
            ],
            "default": "PT_CHLD_Y0T4_REG",
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
                "PT_CHLD_Y0T4_REG",
                "PP_SG_REG_BRTH90N",
                "PP_SG_REG_DETH75N",
            ],
            "default": "PT_CHLD_Y0T4_REG",
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
            "indicators": [
                "PT_CHLD_Y0T4_REG",
                "PP_SG_REG_BRTH90N",
                "PP_SG_REG_DETH75N",
            ],
            "default": "PT_CHLD_Y0T4_REG",
            "default_graph": "line",
        },
    },
    "ACCESS": {
        "NAME": "Access to Justice",
        "CARDS": [
            {
                "name": "with National Human Rights Institutions in compliance with the Paris Principles (A status)",
                "indicator": "PP_SG_NHR_IMPLN",
                "suffix": "Countries",
            },
            {
                "name": "of registered crimes committed against children (during the year, by sex and age groups)",
                "indicator": "JJ_CHLD_CRIME",
                "suffix": "Total Number",
            },
            {
                "name": "of crimes committed against children (per 100,000 average population aged 0-17)",
                "indicator": "JJ_CHLD_CRIMERT",
                "suffix": "Registered Rate",
            },
        ],
        "MAIN": {
            "name": "Children without parental care",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PP_SG_NHR_IMPLN",
                "PP_SG_NHR_INTEXSTN",
                "PP_SG_NHR_NOSTUSN",
                "PP_SG_NHR_NOAPPLN",
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
            ],
            "default": "PP_SG_NHR_IMPLN",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "PV_SI_COV_BENFTS",
            "indicators": [
                "PP_SG_NHR_IMPLN",
                "PP_SG_NHR_INTEXSTN",
                "PP_SG_NHR_NOSTUSN",
                "PP_SG_NHR_NOAPPLN",
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
            ],
            "default": "PP_SG_NHR_IMPLN",
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
            "indicators": [
                "PP_SG_NHR_IMPLN",
                "PP_SG_NHR_INTEXSTN",
                "PP_SG_NHR_NOSTUSN",
                "PP_SG_NHR_NOAPPLN",
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
            ],
            "default": "PP_SG_NHR_IMPLN",
            "default_graph": "line",
        },
    },
    # "ENGAGEMENT": {
    #     "NAME": "Child and adolescent engagement and freedom of expression",
    #     "CARDS": [
    #         {
    #             "name": "covered by at least one social protection benefit (%)",
    #             "indicator": "PV_SI_COV_BENFTS",
    #             "suffix": "Proportion of Population",
    #             "abosolute": True,
    #         },
    #     ],
    #     "MAIN": {
    #         "name": "Children without parental care",
    #         "geo": "Geographic area",
    #         "options": dict(
    #             lat="latitude",
    #             lon="longitude",
    #             size="OBS_VALUE",
    #             text="Geographic area",
    #             color="OBS_VALUE",
    #             color_continuous_scale=px.colors.sequential.GnBu,
    #             size_max=40,
    #             zoom=2.5,
    #             animation_frame="TIME_PERIOD",
    #             height=750,
    #         ),
    #         "indicators": [
    #             "PV_SI_COV_BENFTS",
    #             "PV_SI_COV_LMKT",
    #             "PV_SI_COV_SOCAST",
    #             "PV_SI_COV_SOCINS",
    #             "PV_SI_COV_WKINJRY",
    #             "PV_SI_COV_CHLD",
    #             "PV_SI_COV_DISAB",
    #             "PV_SI_COV_MATNL",
    #             "PV_SI_COV_POOR",
    #             "PV_SI_COV_UEMP",
    #             "PV_SI_COV_VULN",
    #             "PV_SI_COV_PENSN",
    #         ],
    #         "default": "PV_SI_COV_BENFTS",
    #     },
    #     "AREA_1": {
    #         "type": "bar",
    #         "options": dict(
    #             x="Geographic area",
    #             y="OBS_VALUE",
    #             barmode="group",
    #             text="TIME_PERIOD",
    #         ),
    #         # compare is the default selection
    #         "compare": "Sex",
    #         "default": "PV_SI_COV_BENFTS",
    #         "indicators": [
    #             "PV_SI_COV_BENFTS",
    #             "PV_SI_COV_LMKT",
    #             "PV_SI_COV_SOCAST",
    #             "PV_SI_COV_SOCINS",
    #             "PV_SI_COV_WKINJRY",
    #             "PV_SI_COV_CHLD",
    #             "PV_SI_COV_DISAB",
    #             "PV_SI_COV_MATNL",
    #             "PV_SI_COV_POOR",
    #             "PV_SI_COV_UEMP",
    #             "PV_SI_COV_VULN",
    #             "PV_SI_COV_PENSN",
    #         ],
    #     },
    #     "AREA_2": {
    #         "graphs": {
    #             "bar": {
    #                 "options": dict(
    #                     x="Geographic area",
    #                     y="OBS_VALUE",
    #                     barmode="group",
    #                     text="TIME_PERIOD",
    #                 ),
    #                 "compare": "Sex",
    #             },
    #             "line": {
    #                 "options": dict(
    #                     x="TIME_PERIOD",
    #                     y="OBS_VALUE",
    #                     color="Geographic area",
    #                     hover_name="Geographic area",
    #                     line_shape="spline",
    #                     render_mode="svg",
    #                 ),
    #                 "trace_options": dict(mode="lines+markers"),
    #             },
    #         },
    #         "indicators": [
    #             "PV_SI_COV_BENFTS",
    #             "PV_SI_COV_LMKT",
    #             "PV_SI_COV_SOCAST",
    #             "PV_SI_COV_SOCINS",
    #             "PV_SI_COV_WKINJRY",
    #             "PV_SI_COV_CHLD",
    #             "PV_SI_COV_DISAB",
    #             "PV_SI_COV_MATNL",
    #             "PV_SI_COV_POOR",
    #             "PV_SI_COV_UEMP",
    #             "PV_SI_COV_VULN",
    #             "PV_SI_COV_PENSN",
    #         ],
    #         "default_graph": "line",
    #         "default": "PV_SI_COV_BENFTS",
    #     },
    # },
    "INFORMATION": {
        "NAME": "Information, internet and right to privacy",
        "CARDS": [
            {
                "name": "with ICT skill: sending e-mails with attached files (%, by sex)",
                "indicator": "PP_SE_ADT_ACTS_ATCH",
                "suffix": "Proportion of youth and adults",
            },
            {
                "name": "with ICT skill: copying or moving a file or folder (%, by sex)",
                "indicator": "PP_SE_ADT_ACTS_CMFL",
                "suffix": "Proportion of youth and adults",
            },
        ],
        "MAIN": {
            "name": "Children without parental care",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PP_IT_USE_ii99",
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
                "PP_IT_MOB_OWN",
            ],
            "default": "PP_SE_ADT_ACTS_ATCH",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "PV_SI_COV_BENFTS",
            "indicators": [
                "PP_IT_USE_ii99",
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
                "PP_IT_MOB_OWN",
            ],
            "default": "PP_SE_ADT_ACTS_ATCH",
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
            "indicators": [
                "PP_IT_USE_ii99",
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
                "PP_IT_MOB_OWN",
            ],
            "default": "PP_SE_ADT_ACTS_ATCH",
            "default_graph": "line",
        },
    },
    "LEISURE": {
        "NAME": "Leisure and culture",
        "CARDS": [
            {
                "name": "(15-year-olds) who watch TV or play video games, before or after school",
                "indicator": "PP_ADOL_TVGM",
                "suffix": "Percentage of Adolescents",
            },
            {
                "name": "(15-year-olds) who use the internet and social networks, before or after school",
                "indicator": "PP_ADOL_INET",
                "suffix": "Percentage of Adolescents",
            },
        ],
        "MAIN": {
            "name": "Children without parental care",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
            ],
            "default": "PP_ADOL_TVGM",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "PV_SI_COV_BENFTS",
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
            ],
            "default": "PP_ADOL_TVGM",
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
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
            ],
            "default": "PP_ADOL_TVGM",
            "default_graph": "line",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
