from collections import defaultdict
import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "PARTICIPATION": {
        "NAME": "Education access and participation",
        "CARDS": [
            {
                "name": "Who are Out-of-School",
                "indicator": "REPROV_EFFINAL_ESTADUAL",
                "suffix": "Failure rate: final years of Elementary School - State network",
                # "age": "SCHOOL_AGE",
            },
            # {
            #     "name": "Who are Out-of-School",
            #     "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
            #     "suffix": "Primary to upper secondary aged Girls",
            #     "sex": "F",
            #     "age": "SCHOOL_AGE",
            # },
            # {
            #     "name": "Who are Out-of-School",
            #     "indicator": "EDUNF_OFST_L1_UNDER1",
            #     "suffix": "Children one year younger than the official primary entry age",
            #     "age": "UNDER1_SCHOOL_ENTRY",
            # },
        ],
        "MAIN": {
            "name": "Out-of-School Children",
            "geo": "Country_name",  # REF_AREA
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
                    "REF_AREA": "ISO3 Code",
                    "TIME_PERIOD": "Year",
                    "Country_name": "Country",
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
                "TDI_EFFINAL_ESTADUAL",
                "TDI_EFFINAL_MUNICIPAL",
                "ABANDONOEFFINAISABSOLUTO",
            ],
            "default": "TDI_EFFINAL_ESTADUAL",
        },

    },
}


main_title = "Education"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
