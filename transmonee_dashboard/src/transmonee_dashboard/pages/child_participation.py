import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "REGISTRATION": {
        "NAME": "Birth registration and identity",
        "CARDS": [
            {
                "name": "Children whose births have been registered with a civil authority",
                "indicator": "PT_CHLD_Y0T4_REG",  # wealth quintile has no Total
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Birth and Death Registration",
            "geo": "Country_name",
            "options": dict(
                locations="REF_AREA",
                featureidkey="id",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                mapbox_style="carto-positron",
                zoom=2,
                center={"lat": 62.995158, "lon": 88.048713},
                opacity=0.5,
                labels={
                    "OBS_VALUE": "Value",
                    "Country_name": "Country",
                    "TIME_PERIOD": "Year",
                    "REF_AREA": "ISO3 Code",
                },
                hover_data={
                    "OBS_VALUE": True,
                    "REF_AREA": False,
                    "Country_name": True,
                    "TIME_PERIOD": True,
                },
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
            "name": "Birth Registration",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "indicators": [
                "PT_CHLD_Y0T4_REG",
                "PP_SG_REG_BRTH90N",
            ],
            "default": "PP_SG_REG_BRTH90N",
        },
        "AREA_2": {
            "name": "Death Registration",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PP_SG_REG_DETH75N",
            ],
            "default": "PP_SG_REG_DETH75N",
            "default_graph": "bar",
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
    #         "geo": "Country_name",
    #         "options": dict(
    #             lat="latitude",
    #             lon="longitude",
    #             size="OBS_VALUE",
    #             text="REF_AREA",
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
    #             x="Country_name",
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
    #                     x="Country_name",
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
    #                     color="Country_name",
    #                     hover_name="Country_name",
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
        "NAME": "Information, Internet and Protection of privacy",
        "CARDS": [
            {
                "name": "Internet users per 100 inhabitants",
                "indicator": "PP_IT_USE_ii99",
                "suffix": "Average among countries",
                "absolute": True,
                "average": True,
            },
            {
                "name": "Individuals who own a mobile telephone",
                "indicator": "PP_IT_MOB_OWN",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Information, Internet and Protection of privacy",
            "geo": "Country_name",
            "options": dict(
                locations="REF_AREA",
                featureidkey="id",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                mapbox_style="carto-positron",
                zoom=2,
                center={"lat": 62.995158, "lon": 88.048713},
                opacity=0.5,
                labels={
                    "OBS_VALUE": "Value",
                    "Country_name": "Country",
                    "TIME_PERIOD": "Year",
                    "REF_AREA": "ISO3 Code",
                },
                hover_data={
                    "OBS_VALUE": True,
                    "REF_AREA": False,
                    "Country_name": True,
                    "TIME_PERIOD": True,
                },
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
            "name": "Mobile phones and Internet",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "default": "PV_SI_COV_BENFTS",
            "indicators": [
                "PP_IT_USE_ii99",
                "PP_IT_MOB_OWN",
            ],
            "default": "PP_IT_USE_ii99",
        },
        "AREA_2": {
            "name": "Youth and Adults with ICT skills",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
            ],
            "default": "PP_SE_ADT_ACTS_ATCH",
            "default_graph": "line",
        },
    },
    "LEISURE": {
        "NAME": "Education, Leisure, and Culture",
        "CARDS": [
            {
                "name": "Adolescents (15-year-olds) who use the internet and social networks, before or after school",
                "indicator": "PP_ADOL_WORK_PAID",
                "suffix": "Percentage ranges among countries",
                "min_max": True,
            },
            {
                "name": "Adolescents (15-year-olds) who do paid work, before or after school",
                "indicator": "PP_ADOL_INET",
                "suffix": "Percentage ranges among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Education, Leisure, and Culture",
            "geo": "Country_name",
            "options": dict(
                locations="REF_AREA",
                featureidkey="id",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                mapbox_style="carto-positron",
                zoom=2,
                center={"lat": 62.995158, "lon": 88.048713},
                opacity=0.5,
                labels={
                    "OBS_VALUE": "Value",
                    "Country_name": "Country",
                    "TIME_PERIOD": "Year",
                    "REF_AREA": "ISO3 Code",
                },
                hover_data={
                    "OBS_VALUE": True,
                    "REF_AREA": False,
                    "Country_name": True,
                    "TIME_PERIOD": True,
                },
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
            "name": "TV or Play Video Games",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "default": "PV_SI_COV_BENFTS",
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
            ],
            "default": "PP_ADOL_TVGM",
        },
        "AREA_2": {
            "name": "Internet and Social Networks",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        # text="TIME_PERIOD",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                    ),
                    # "compare": "Sex",
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
            ],
            "default": "PP_ADOL_INET",
            "default_graph": "line",
        },
    },
}

main_title = "Participation and Civil Rights"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
