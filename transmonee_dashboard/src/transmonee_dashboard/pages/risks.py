import plotly.express as px
from .base_page import get_base_layout, geo_json_countries

indicators_dict = {
    "RISKS": {
        "NAME": "Cross-Cutting Issues",
        "CARDS": [
            {
                "name": "Deaths and missing persons attributed to disasters (per 100,000 population)",
                "indicator": "CR_VC_DSR_MTMP",
                "suffix": "Rate range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Risks and humanitarian situation",
            "geo": "REF_AREA",
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
                    "REF_AREA": "Country",
                    "TIME_PERIOD": "Year",
                    "REF_AREA": "ISO3 Code",
                },
                hover_data={
                    "OBS_VALUE": True,
                    "REF_AREA": False,
                    "REF_AREA": True,
                    "TIME_PERIOD": True,
                },
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "CR_VC_DSR_MTMP",
                "CR_VC_DSR_DAFF",
                "CR_SG_DSR_LGRGSR",
                "CR_SH_AAP_MORT",
                "CR_SH_HAP_MORT",
                "CR_SH_STA_AIRP",
                "CR_SH_AAP_ASMORT",
                "CR_SH_HAP_ASMORT",
                "CR_SH_STA_ASAIRP",
                "CR_AAP_DEATH",
                "CR_HAP_DEATH",
            ],
            "default": "CR_VC_DSR_MTMP",
        },
        "AREA_1": {
            "name": "Humanitarian Situation",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="REF_AREA",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "default_graph": "bar",
            "indicators": [
                "CR_VC_DSR_MTMP",
                "CR_VC_DSR_DAFF",
                "CR_SH_AAP_MORT",
                "CR_SH_HAP_MORT",
                "CR_SH_STA_AIRP",
                "CR_SH_AAP_ASMORT",
                "CR_SH_HAP_ASMORT",
                "CR_SH_STA_ASAIRP",
                "CR_AAP_DEATH",
                "CR_HAP_DEATH",
            ],
            "default": "CR_VC_DSR_MTMP",
        },
        "AREA_2": {
            "name": "Disaster Risk Reduction",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="REF_AREA",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "CR_SG_DSR_LGRGSR",
            ],
            "default": "CR_SG_DSR_LGRGSR",
            "default_graph": "line",
        },
    },
}

main_title = "Risks and Humanitarian Situation"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
