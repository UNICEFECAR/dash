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
                "name": "Child physical punishment by caregivers",
                "indicator": "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "denominator": "EDUNF_SAP_L2",
                "suffix": "%",
            },
        ],
        "MAIN": {
            "name": "Child physical punishment by caregivers",
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
                height=750,
            ),
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
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
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
        "RIGHT": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        color="Sex",
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
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
            "default_graph": "line",
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
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
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
    },
    "CARE": {
        "NAME": "Children without parental care",
        "CARDS": [
            {
                "name": "TMEE Number: Children in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            {
                "name": "TMEE Rate: Children in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL_RATE_B",
                "denominator": "EDUNF_SAP_L2",
                "suffix": "%",
            },
            {
                "name": "TMEE Number: Children cared by Fosters or Guardians",
                "indicator": "PT_CHLD_INCARE_FOSTER",
                "suffix": "Children",
            },
            {
                "name": "TMEE Number: Children available for adoption",
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
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=3,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_NONPUBLIC",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_NO_PARENTAL_CARE_RATE",
                "PT_CHLD_INCARE_FOSTER",
                "PT_CHLD_INCARE_FOSTER_RATE",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_RATE",
            ],
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "PT_CHLD_INRESIDENTIAL",
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_NO_PARENTAL_CARE_RATE",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_INTERCOUNTRY",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION_INTERCOUNTRY_RATE",
            ],
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
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_NO_PARENTAL_CARE_RATE",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_CARED_BY_FOSTER_RATE",
                "PT_CHLD_CARED_GUARDIAN",
                "PT_CHLD_CARED_GUARDIAN_RATE",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_ADOPTION_INTERCOUNTRY",
                "PT_CHLD_ADOPTION_RATE",
                "PT_CHLD_ADOPTION_INTERCOUNTRY_RATE",
            ],
            "default": "PT_CHLD_INRESIDENTIAL",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_INTER_COUNTRY_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
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
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_DISAB_CARED_GUARDIAN",
                "PT_CHLD_ADOPTION_DISAB",
                "PT_CHLD_ADOPTION_INTER_COUNTRY_DISAB",
                "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
            ],
            "default": "PT_CHLD_DISAB_PUBLIC",
        },
    },
    "JUSTICE": {
        "NAME": "Access to Justice",
        "CARDS": [
            {
                "name": "TMEE Number: Child Victims of Crime",
                "indicator": "JJ_CHLD_CRIME",
                "suffix": "PER_100,000 Children",
            },
            # revise denominator: population children 0-17
            {
                "name": "TMEE Rate: Child Victims of Crime",
                "indicator": "JJ_CHLD_CRIMERT",
                "denominator": "EDUNF_SAP_L2",
                "suffix": "%",
            },
            # revise denominator: population children 0-17
            {
                "name": "TMEE Rate: Child Sentencing",
                "indicator": "JJ_CHLD_SENTENCERT",
                "denominator": "EDUNF_SAP_L2",
                "suffix": "%",
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
                color_continuous_scale=px.colors.sequential.Jet,
                size_max=40,
                zoom=3,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
            ],
        },
        "LEFT": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_CHLD_PRISION",
                "JJ_CHLD_PRETRIAL",
                "JJ_CHLD_PRISION_ADJUDICATION",
                "JJ_CHLD_CONVICTED_VIOLENT",
                "JJ_CHLD_CONVICTED_PROPERTY",
                "JJ_CHLD_CONVICTED_OTHER",
            ],
            "default": "JJ_CHLD_CRIME",
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
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_CHLD_PRISION",
                "JJ_CHLD_PRETRIAL",
                "JJ_CHLD_PRISION_ADJUDICATION",
                "JJ_CHLD_CONVICTED_VIOLENT",
                "JJ_CHLD_CONVICTED_PROPERTY",
                "JJ_CHLD_CONVICTED_OTHER",
            ],
            "default": "JJ_CHLD_CRIME",
        },
        "AREA_3": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD"
            ),
            "compare": "Sex",
            "indicators": [
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_CHLD_PRISION",
                "JJ_CHLD_PRETRIAL",
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
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
                "JJ_CHLD_PRISION",
                "JJ_CHLD_PRETRIAL",
            ],
            "default": "JJ_CHLD_CRIMERT",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
