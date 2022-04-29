import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "POVERTYDEPRIVATION": {
        "NAME": "Child Poverty and Material Deprivation",
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
                # "PV_SD_MDP_ANDI",
                # "PV_SD_MDP_ANDIHH",
            ],
            "default": "PV_SDG_SI_POV_NAHC",
        },
        "AREA_1": {
            "name": "Absolute Poverty",
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
                "PV_AROPE",
                "PV_AROPRT",
                "PV_SD_MDP_CSMP",
                "PV_SD_MDP_MUHHC",
                "PV_SD_MDP_MUHC",
                # "PV_SD_MDP_ANDI",
                # "PV_SD_MDP_ANDIHH",
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
            "default": "PV_SI_COV_CHLD",
            "indicators": [
                "PV_SI_COV_CHLD",
                "PV_SI_COV_DISAB",
                "PV_SI_COV_MATNL",
                "PV_SI_COV_POOR",
                "PV_SI_COV_UEMP",
                "PV_SI_COV_VULN",
                "PV_SI_COV_PENSN",
                "SP_PS_DISAB_CASH",
                "SP_CHLD_DISAB_CASH",
                "SP_EXP_CHLD_DISAB_CASH",
            ],
        },
        "AREA_2": {
            "name": "Social Assistances other than Cash",
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
                "PV_SI_COV_BENFTS",
                "PV_SI_COV_LMKT",
                "PV_SI_COV_SOCAST",
                "PV_SI_COV_SOCINS",
                "PV_SI_COV_WKINJRY",
                "HT_REG_PS_DISAB",
                "HT_REG_CHLD_DISAB",
                "HT_NEW_REG_PS_DISAB",
                "HT_NEW_REG_CHLD_DISAB",
                "HT_REG_CHLD_DISAB_PROP",
                "HT_NEW_REG_CHLD_DISAB_PROP",
            ],
            "default_graph": "line",
            "default": "PV_SI_COV_BENFTS",
        },
    },
}


main_title = "Poverty and Social Protection"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
