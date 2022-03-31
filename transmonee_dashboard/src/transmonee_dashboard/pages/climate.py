import plotly.express as px
from .base_page import get_base_layout, geo_json_countries

indicators_dict = {
    "CLIMATE": {
        "NAME": "Cross-Cutting Issues",
        "CARDS": [
            {
                "name": "Population with primary reliance on clean fuels and technology",
                "indicator": "CR_EG_EGY_CLEAN",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "of Children's Climate and Environment Risk Index (CCRI)",
                "indicator": "CR_CCRI",
                "suffix": "Range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Environment and Climate Change",
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
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "CR_EG_EGY_CLEAN",
                "CR_EG_ACS_ELEC",
                "CR_CCRI_VUL_HT",
                "CR_CCRI_VUL_EDU",
                "CR_CCRI_VUL_WASH",
                "CR_CCRI_VUL_SP",
                "CR_CCRI_VUL_ES",
                "CR_CCRI",
                "CR_CCRI_EXP_WS",
                "CR_CCRI_EXP_RF",
                "CR_CCRI_EXP_CF",
                "CR_CCRI_EXP_TC",
                "CR_CCRI_EXP_VBD",
                "CR_CCRI_EXP_HEAT",
                "CR_CCRI_EXP_AP",
                "CR_CCRI_EXP_SWP",
                "CR_CCRI_EXP_CESS",
            ],
            "default": "CR_SH_STA_AIRP",
        },
        "AREA_1": {
            "name": "Vulnerability, Exposure, and Pollution",
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
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "CR_CCRI_VUL_HT",
                "CR_CCRI_VUL_EDU",
                "CR_CCRI_VUL_WASH",
                "CR_CCRI_VUL_SP",
                "CR_CCRI_VUL_ES",
                "CR_CCRI",
                "CR_CCRI_EXP_WS",
                "CR_CCRI_EXP_RF",
                "CR_CCRI_EXP_CF",
                "CR_CCRI_EXP_TC",
                "CR_CCRI_EXP_VBD",
                "CR_CCRI_EXP_HEAT",
                "CR_CCRI_EXP_AP",
                "CR_CCRI_EXP_SWP",
                "CR_CCRI_EXP_CESS",
            ],
            "default": "CR_SH_STA_AIRP",
        },
        "AREA_2": {
            "name": "Clean Fuels and Technology",
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
                "CR_EG_EGY_CLEAN",
                "CR_EG_ACS_ELEC",
            ],
            "default": "CR_EG_EGY_CLEAN",
            "default_graph": "line",
        },
    },
}

main_title = "Environment and Climate Change"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
