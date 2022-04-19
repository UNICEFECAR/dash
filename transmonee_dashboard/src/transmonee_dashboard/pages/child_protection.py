import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "VIOLENCE": {
        "NAME": "Violence against Children and Women",
        "CARDS": [
            {
                "name": "Population subjected to physical violence in the previous 12 months",
                "indicator": "PT_VC_VOV_PHYL",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Adults who think that physical punishment is necessary to raise/educate children",
                "indicator": "PT_ADLT_PS_NEC",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Violence and Assault",
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
            "default": "PT_ADLT_PS_NEC",
        },
        "AREA_1": {
            "name": "Violent Discipline",
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
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_ADLT_PS_NEC",
                "PT_ST_13-15_BUL_30-DYS",
            ],
            "default": "PT_ADLT_PS_NEC",
        },
        "AREA_2": {
            "name": "Crime, Assault, and Safety",
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
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_M_18-29_SX-V_AGE-18",
                "PT_VC_PRR_PHYV",
                "PT_VC_PRR_SEXV",
                "PT_VC_PRR_ROBB",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
            ],
            "default_graph": "bar",
            "default": "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
        },
    },
    "CARE": {
        "NAME": "Children without parental care",
        "CARDS": [
            {
                "name": "aged 0-17 in formal residential care (at the end of the year)",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "Total number of children",
                "sex": "_T",
                "age": "_T",
                "absolute": True,
            },
            {
                "name": "aged 0-17 in formal foster care (at the end of the year)",
                "indicator": "PT_CHLD_CARED_BY_FOSTER",
                "suffix": "Total number of children",
                "sex": "_T",
                "age": "_T",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "Family Environment",
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
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
            ],
            "default": "PT_CHLD_INRESIDENTIAL",
        },
        "AREA_1": {
            "name": "Residencial Care",
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
            "default": "PT_CHLD_INRESIDENTIAL",
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
            ],
        },
        "AREA_2": {
            "name": "Foster Care and Adoption",
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
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_DISAB_FOSTER",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_ADOPTION_RATE",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_CARED_BY_FOSTER",
        },
    },
    "JUSTICE": {
        "NAME": "Justice for Children",
        "CARDS": [
            {
                "name": "detained in pre-sentence detention (during the year)",
                "indicator": "JJ_CHLD_DETENTION",
                "suffix": "Total number of children",
                "sex": "_T",
                "age": "_T",
                "absolute": True,
            },
            {
                "name": "in detention at the end of the year (per 100,000)",
                "indicator": "JJ_CHLD_DETENTION_RATE",
                "suffix": "Rate of children",
                "sex": "_T",
                "age": "_T",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Access to Justice for Children",
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
                "JJ_CHLD_DETENTION",
                "JJ_VC_PRS_UNSNT",
                "JJ_PRISIONERS",
                "JJ_PRISIONERS_RT",
            ],
            "default": "JJ_CHLD_DETENTION",
        },
        "AREA_1": {
            "name": "Children Victims and Prisoners",
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
                "JJ_PRISIONERS",
                "JJ_PRISIONERS_RT",
            ],
            "default": "JJ_PRISIONERS",
        },
        "AREA_2": {
            "name": "Diversion, Sentencing, and Detention of Children",
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
                "JJ_CHLD_DETENTION",
                "JJ_VC_PRS_UNSNT",
            ],
            "default_graph": "line",
            "default": "JJ_CHLD_DETENTION",
        },
    },
    "MARRIAGE": {
        "NAME": "Child marriage and other harmful practices",
        "CARDS": [
            {
                "name": "Women age 20-24 years married or in union before age 18",
                "indicator": "PT_F_20-24_MRD_U18",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Men age 20-24 years married or in union before age 18",
                "indicator": "PT_M_20-24_MRD_U18",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Child Marriage",
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
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
            ],
            "default": "PT_F_15-19_MRD",
        },
        "AREA_1": {
            "name": "Currently married or in union children age 15-19 years",
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
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
            ],
            "default": "PT_F_15-19_MRD",
        },
        "AREA_2": {
            "name": "Currently married or in union adults before age 18 or 15 years",
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
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
            ],
            "default_graph": "bar",
            "default": "PT_F_20-24_MRD_U15",
        },
    },
    "LABOUR": {
        "NAME": "Child labour and other forms of exploitation",
        "CARDS": [
            {
                "name": "Children age 5-17 years who are involved in child labour",
                "indicator": "PT_CHLD_5-17_LBR_ECON-HC",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Child labour and other forms of exploitation",
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
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default": "PT_CHLD_5-17_LBR_ECON",
        },
        "AREA_1": {
            "name": "Child labour - only economic activities",
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
                "PT_CHLD_5-17_LBR_ECON",
            ],
            "default": "PT_CHLD_5-17_LBR_ECON",
        },
        "AREA_2": {
            "name": "Child labour - economic activities and household chores",
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
                "PT_CHLD_5-17_LBR_ECON-HC",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_5-17_LBR_ECON-HC",
        },
    },
}


main_title = "Family environment and protection from violence and harmful practices"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
