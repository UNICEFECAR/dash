import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "VIOLENCE": {
        "NAME": "Violence against Children and Women",
        "CARDS": [
            # revise denominator population: children 1-14?
            {
                "name": "Who experienced physical punishment or psychological aggression by caregivers",
                "indicator": "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
        ],
        "MAIN": {
            "name": "Violence and Harmful Practices",
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
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
            ],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
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
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
            ],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
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
                # "line": {
                #     "options": dict(
                #         x="TIME_PERIOD",
                #         y="OBS_VALUE",
                #         color="Geographic area",
                #         hover_name="Geographic area",
                #         line_shape="spline",
                #         render_mode="svg",
                #     ),
                #     "trace_options": dict(mode="lines+markers"),
                # },
            },
            "indicators": [
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_ADLT_PS_NEC",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_ST_13-15_BUL_30-DYS",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
    },
    "CARE": {
        "NAME": "Children without parental care",
        "CARDS": [
            {
                "name": "In Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            {
                "name": "In Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL_RATE_B",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
            {
                "name": "In care of foster parents or guardians",
                "indicator": "PT_CHLD_INCARE_FOSTER",
                "suffix": "Children",
            },
            {
                "name": "Available for adoption",
                "indicator": "PT_CHLD_ADOPTION_AVAILABLE",
                "suffix": "Children",
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
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
            "default": "PT_CHLD_INRESIDENTIAL",
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
            "default": "PT_CHLD_INRESIDENTIAL",
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
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
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_LEFTRESCARE",
                "PT_CHLD_LEFTRESCARE_RETURNED",
                "PT_CHLD_LEFTRESCARE_INFAMILY",
                "PT_CHLD_LEFTRESCARE_ADOPTED",
                "PT_CHLD_LEFTRESCARE_INDEPENDENT",
                "PT_CHLD_LEFTRESCARE_TRANSFERED",
                "PT_CHLD_LEFTRESCARE_DIED",
                "PT_CHLD_LEFTRESCARE_OTHER",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_GUARDIAN",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_INRESIDENTIAL",
        },
    },
    "JUSTICE": {
        "NAME": "Juvenile Justice",
        "CARDS": [
            {
                "name": "Committed against children during the year",
                "indicator": "JJ_CHLD_CRIME",
                "suffix": "Registered crimes",
            },
            {
                "name": "Who are reported as being in contact with the police because of their own behaviour during the year",
                "indicator": "JJ_CHLD_POLICE",
                "suffix": "Children",
            },
            {
                "name": "Who are charged with an offence or crime during the year",
                "indicator": "JJ_CHLD_OFFENCE",
                "suffix": "Children",
            },
        ],
        "MAIN": {
            "name": "Child Victims of Crime",
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
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
                "JJ_PRISIONERS",
                "JJ_PRISIONERS_RT",
            ],
            "default": "JJ_CHLD_CONVICTED",
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
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
                "JJ_PRISIONERS",
                "JJ_PRISIONERS_RT",
            ],
            "default": "JJ_CHLD_CONVICTED",
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
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_VC_PRS_UNSNT",
                "JJ_PRISIONERS",
                "JJ_PRISIONERS_RT",
            ],
            "default_graph": "line",
            "default": "JJ_CHLD_CONVICTED",
        },
    },
    "MARRIAGE": {
        "NAME": "Child marriage and other harmful practices",
        "CARDS": [
            {
                "name": "aged 15-19 years (by residence and wealth quintile) who are currently married or in union",
                "indicator": "PT_F_15-19_MRD",
                "suffix": "Percentage of girls",
            },
            {
                "name": "aged 15-19 years (by residence and wealth quintile) who are currently married or in union",
                "indicator": "PT_M_15-19_MRD",
                "suffix": "Percentage of boys",
            },
        ],
        "MAIN": {
            "name": "Child Victims of Crime",
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
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
            ],
            "default": "PT_F_15-19_MRD",
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
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
            ],
            "default": "PT_F_15-19_MRD",
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
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
            ],
            "default_graph": "line",
            "default": "PT_F_15-19_MRD",
        },
    },
    "LABOUR": {
        "NAME": "Child Labour",
        "CARDS": [
            {
                "name": "(aged 5-17 years, by sex and age groups) engaged in child labour (economic activities)",
                "indicator": "PT_CHLD_5-17_LBR_ECON",
                "suffix": "Percentage of Children",
            },
        ],
        "MAIN": {
            "name": "Child Victims of Crime",
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
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default": "PT_CHLD_5-17_LBR_ECON",
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
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default": "PT_CHLD_5-17_LBR_ECON",
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
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_5-17_LBR_ECON",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
