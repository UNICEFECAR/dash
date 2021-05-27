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
                "name": "who experienced physical punishment or psychological aggression by caregivers",
                "indicator": "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
        ],
        "MAIN": {
            "name": "Children physical punishment or psychological aggression by caregivers",
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
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
        "AREA_1": {
            "type": "bar",
            "options": dict(
                x="Geographic area", y="OBS_VALUE", barmode="group", text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": ["PT_CHLD_1-14_PS-PSY-V_CGVR"],
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
    },
    "CARE": {
        "NAME": "Children without parental care",
        "CARDS": [
            {
                "name": "in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            {
                "name": "in Residential Care",
                "indicator": "PT_CHLD_INRESIDENTIAL_RATE_B",
                "denominator": "EDUNF_SAP_L1T3",
                "suffix": "Percent of Children",
            },
            {
                "name": "in care of foster parents or guardians",
                "indicator": "PT_CHLD_INCARE_FOSTER",
                "suffix": "Children",
            },
            {
                "name": "available for adoption",
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
        "AREA_1": {
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
            "default": "PT_CHLD_DISAB_PUBLIC",
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
            "default": "PT_CHLD_ADOPTION_DISAB",
        },
    },
    "JUSTICE": {
        "NAME": "Access to Justice",
        "CARDS": [
            {
                "name": "committed against children during the year",
                "indicator": "JJ_CHLD_CRIME",
                "suffix": "Registered crimes",
            },
            {
                "name": "who are reported as being in contact with the police because of their own behaviour during the year",
                "indicator": "JJ_CHLD_POLICE",
                "suffix": "Children",
            },
            {
                "name": "who are charged with an offence or crime during the year",
                "indicator": "JJ_CHLD_OFFENCE",
                "suffix": "Children",
            },
            # revise denominator: population children 0-17
            # we don't have the ability yet to deal with rates that are not percentage
            # {
            #     "name": "committed against children (per 100,000 population aged 0-17)",
            #     "indicator": "JJ_CHLD_CRIMERT",
            #     "denominator": "EDUNF_SAP_L1T3",
            #     "suffix": "Registered crimes",
            # },
            # revise denominator: population children 14-17
            # we don't have the ability yet to deal with rates that are not percentage
            # {
            #     "name": "who are sentenced (per 100,000 population aged 14-17)",
            #     "indicator": "JJ_CHLD_SENTENCERT",
            #     "denominator": "EDUNF_SAP_L3",
            #     "suffix": "Children",
            # },
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
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
            ],
            "default": "JJ_CHLD_CRIME",
        },
        "AREA_1": {
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
            ],
            "default": "JJ_CHLD_CRIME",
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
                "JJ_CHLD_CRIME",
                "JJ_CHLD_CRIMERT",
                "JJ_CHLD_DETENTION",
                "JJ_CHLD_CONVICTED",
                "JJ_CHLD_SENTENCERT",
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
                "JJ_CHLD_CRIME_PERPETRATOR",
                "JJ_CHLD_CRIME_PERSON",
                "JJ_CHLD_CRIME_PROPERTY",
                "JJ_CHLD_CRIME_OTHER",
                "JJ_CHLD_POLICE",
                "JJ_CHLD_ARRESTED",
                "JJ_CHLD_OFFENCE",
                "JJ_CHLD_VICTIM",
                "JJ_CHLD_OFFENDER",
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
                "JJ_CHLD_PRISION",
                "JJ_CHLD_PRETRIAL",
                "JJ_CHLD_PRISION_ADJUDICATION",
                "JJ_CHLD_CONVICTED_VIOLENT",
                "JJ_CHLD_CONVICTED_PROPERTY",
                "JJ_CHLD_CONVICTED_OTHER",
            ],
            "default": "JJ_CHLD_CRIMERT",
        },
    },
}


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    return get_base_layout(**kwargs)
