import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout, geo_json_countries

indicators_dict = {
    "POVERTYDEPRIVATION": {
        "NAME": "Poverty and multi-dimensional deprivation",
        "CARDS": [
            {
                "name": "Population living below the national poverty line",
                "indicator": "PV_SDG_SI_POV_NAHC",
                "suffix": "Percentage range among countries",
                # "absolute": True,
                "min_max": True,
            },
            {
                "name": "People at risk of poverty or social exclusion",
                "indicator": "PV_AROPE",
                "suffix": "Percentage range among countries",
                # "absolute": True,
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Poverty and Deprivation",
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
            "default": "PV_SDG_SI_POV_NAHC",
        },
        "AREA_1": {
            "name": "Absolute Poverty",
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
                "PV_SI_POV_EMP1",
                "PV_SI_POV_DAY1",
                "PV_SI_POV_UMIC",
                "PV_SDG_SI_POV_NAHC",
                "PV_WB_SI_POV_NAHC",
                "WS_PPL_W-B",
                "WS_PPL_S-B",
                "PV_SEV_MAT_DPRT",
            ],
            "default": "PV_SI_POV_EMP1",
        },
        "AREA_2": {
            "name": "Relative Poverty and Deprivation",
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
                "PV_AROPE",
                "PV_AROPRT",
                "PV_SD_MDP_CSMP",
                "PV_SD_MDP_MUHHC",
                "PV_SD_MDP_MUHC",
                "PV_SI_POV_MDIM",
                "PV_SI_POV_MDIM_17",
            ],
            "default_graph": "line",
            "default": "PV_AROPE",
        },
    },
    "SOCIALPROTECTION": {
        "NAME": "Social protection system",
        "CARDS": [
            {
                "name": "Population covered by at least one social protection benefit",
                "indicator": "PV_SI_COV_BENFTS",
                "suffix": "Percentage range among countries",
                "abosolute": True,
                "min_max": True,
            },
            {
                "name": "Children/households receiving child/family cash benefits",
                "indicator": "PV_SI_COV_CHLD",
                "suffix": "Percentage range among countries",
                "abosolute": True,
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Social Protection Transfers",
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
                "PV_SI_COV_BENFTS",
                "PV_SI_COV_LMKT",
                "PV_SI_COV_SOCAST",
                "PV_SI_COV_SOCINS",
                "PV_SI_COV_WKINJRY",
                "PV_SI_COV_CHLD",
                "PV_SI_COV_DISAB",
                "PV_SI_COV_MATNL",
                "PV_SI_COV_POOR",
                "PV_SI_COV_UEMP",
                "PV_SI_COV_VULN",
                "PV_SI_COV_PENSN",
            ],
            "default": "PV_SI_COV_BENFTS",
        },
        "AREA_1": {
            "name": "Cash Benefits",
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
            "default": "PV_SI_COV_CHLD",
            "indicators": [
                "PV_SI_COV_CHLD",
                "PV_SI_COV_DISAB",
                "PV_SI_COV_MATNL",
                "PV_SI_COV_POOR",
                "PV_SI_COV_UEMP",
                "PV_SI_COV_VULN",
                "PV_SI_COV_PENSN",
            ],
        },
        "AREA_2": {
            "name": "Social Assistances other than Cash",
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
                "PV_SI_COV_BENFTS",
                "PV_SI_COV_LMKT",
                "PV_SI_COV_SOCAST",
                "PV_SI_COV_SOCINS",
                "PV_SI_COV_WKINJRY",
            ],
            "default_graph": "line",
            "default": "PV_SI_COV_BENFTS",
        },
    },
}


main_title = "Poverty and adequate standards of living"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
