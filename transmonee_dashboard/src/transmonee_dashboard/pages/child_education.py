from collections import defaultdict
import plotly.express as px

# from . import data, years
from .base_page import get_base_layout

cfg = {
    "ddl_ref_areas_cl": {
        "agency": "BRAZIL_CO",
        "id": "CL_BRAZIL_REF_AREAS",
    },
    "main_title": "Education, Leisure, and Culture",
    "THEMES": {
        "PARTICIPATION": {
            "NAME": "Education access and participation",
            "CARDS": [
                {"data": {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                          "dq": {
                              "REF_AREA": "BR",
                              "INDICATOR": "ABANDONOEFINICIAIS",
                              "AGE": "_T",
                              "EDUCATION_LEVEL": "ISCED11_1"
                          },
                          "lastnobservations": 1},
                 "name": "",
                 "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                 "suffix": "% of school dropout - early years of elementary school",
                 },
                {"data": {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                          "dq": {
                              "REF_AREA": "BR",
                              "INDICATOR": "ABANDONOEFINICIAIS",
                              "AGE": "_T",
                              "EDUCATION_LEVEL": "ISCED11_2"
                          },
                          "lastnobservations": 1},
                 "name": "",
                 "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                 "suffix": "% of school dropout - late years of elementary school",
                 },
                {"data": {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                          "dq": {
                              "REF_AREA": "BR",
                              "INDICATOR": "ABANDONOEFINICIAIS",
                              "AGE": "_T",
                              "EDUCATION_LEVEL": "ISCED11_3"
                          },
                          "lastnobservations": 1},
                 "name": "",
                 "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                 "suffix": "% of school dropout - high school",
                 }
            ],
            "MAIN": {
                "name": "Out-of-School Children",
                "options": {
                    "locations": "REF_AREA",
                    "featureidkey": "id",
                    "color": "OBS_VALUE",
                    "color_continuous_scale": "gnbu",
                    "mapbox_style": "carto-positron",
                    "zoom": 3,
                    "center": {"lat": -11.7462, "lon": -53.222},
                    "opacity": 0.5,
                    "labels": {
                        "OBS_VALUE": "Value",
                        "REF_AREA": "ISO3 Code",
                        "TIME_PERIOD": "Year",
                        # "REF_AREA": "Country",
                        "name": "Country"
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750},
                "name": "Who are Out-of-School",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFINICIAIS", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "% of school dropout - early years of elementary school"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFINICIAIS", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "% of school dropout - final years of Elementary School"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFINICIAIS", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "% of school dropout - High School"
                     },

                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFFINAISABSOLUTO", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Total school dropout - early years of elementary school"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFFINAISABSOLUTO", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Total school dropout - final years of Elementary School"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFFINAISABSOLUTO", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Total school dropout - High School"
                     },

                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFFINAISABSOLUTO", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "% of BPC beneficiary children enrolled in school"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "FORADAESCOLA0A3", "AGE": "_T",
                            "EDUCATION_LEVEL": "_T"},
                     "label": "% of children aged 0 to 3 years old in daycare"
                     },

                ],

            },
            "AREA_1": {
                "name": "Education entry and transition",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="REF_AREA_l",
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
                            color="name",
                            hover_name="name",
                            line_shape="spline",
                            render_mode="svg",
                        ),
                        "trace_options": dict(mode="lines+markers"),
                    },
                },
                "default_graph": "bar",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "BPCNAESCOLA", "AGE": "_T",
                            "EDUCATION_LEVEL": "_T"},
                     # "label": "% of school dropout - final years of elementary school 1"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "FORADAESCOLA0A3", "AGE": "_T",
                            "EDUCATION_LEVEL": "_T"},
                     # "label": "% of school dropout - early years of elementary school 2"
                     },

                ],
                "default": "EDUNF_ROFST_L1",
            },
            "AREA_2": {
                "name": "Education entry and transition",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="REF_AREA_l",
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
                            color="name",
                            hover_name="name",
                            line_shape="spline",
                            render_mode="svg",
                        ),
                        "trace_options": dict(mode="lines+markers"),
                    },
                },
                "default_graph": "bar",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "FORADAESCOLA0A3", "AGE": "_T",
                            "EDUCATION_LEVEL": "_T"},
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "BPCNAESCOLA", "AGE": "_T",
                            "EDUCATION_LEVEL": "_T"},
                     }
                ],
                "default": "EDUNF_ROFST_L1",
            },

        },
        "QUALITY": {
            "NAME": "Learning quality",
            "CARDS": [
                {"data": {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                          "dq": {
                              "REF_AREA": "BR",
                              "INDICATOR": "TDIANOSFINAISPUB",
                              "AGE": "_T",
                              "EDUCATION_LEVEL": "ISCED11_1"
                          },
                          "lastnobservations": 1},
                 "name": "",
                 "indicator": "TDIANOSFINAISPUB",
                 "suffix": "Age-grade distortion rate: final years of Elementary School - Public Network",
                 },
                {"data": {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                          "dq": {
                              "REF_AREA": "BR",
                              "INDICATOR": "TDI_EFFINAL_ESTADUAL",
                              "AGE": "_T",
                              "EDUCATION_LEVEL": "ISCED11_2"
                          },
                          "lastnobservations": 1},
                 "name": "",
                 "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                 "suffix": "ge-grade distortion rate: final years of Elementary School - State Public Network",
                 },

            ],

            "MAIN": {
                "name": "Out-of-School Children",
                "options": {
                    "locations": "REF_AREA",
                    "featureidkey": "id",
                    "color": "OBS_VALUE",
                    "color_continuous_scale": "gnbu",
                    "mapbox_style": "carto-positron",
                    "zoom": 3,
                    "center": {"lat": -11.7462, "lon": -53.222},
                    "opacity": 0.5,
                    "labels": {
                        "OBS_VALUE": "Value",
                        "REF_AREA": "ISO3 Code",
                        "TIME_PERIOD": "Year",
                        # "REF_AREA": "Country",
                        "name": "Country"
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750},
                "name": "Who are Out-of-School",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "IDEBFINAIS", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "% of municipalities that reached the IDEB target - early years of Elementary School"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "ABANDONOEFINICIAIS", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "% of municipalities that reached the IDEB target - final years of Elementary School"
                     },

                ],

            },

            "AREA_1": {
                "name": "School Failure Rate",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="REF_AREA_l",
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
                            color="name",
                            hover_name="name",
                            line_shape="spline",
                            render_mode="svg",
                        ),
                        "trace_options": dict(mode="lines+markers"),
                    },
                },
                "default_graph": "bar",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Failure rate: early years of Elementary School - Municipal network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Failure rate: final years of Elementary School - Municipal network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Failure rate: High School - Municipal network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_PUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Failure rate: early years of Elementary School - Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_PUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Failure rate: final years of Elementary School - Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_PUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Failure rate: high School - Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Failure rate: early years of Elementary School - State network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Failure rate: final years of Elementary School - State networ"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "REPROV_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Failure rate: high years of Elementary School - State networ"
                     },
                ],
                "default": "EDUNF_ROFST_L1",
            },

            "AREA_2": {
                "name": "Education entry and transition",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="REF_AREA_l",
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
                            color="name",
                            hover_name="name",
                            line_shape="spline",
                            render_mode="svg",
                        ),
                        "trace_options": dict(mode="lines+markers"),
                    },
                },
                "default_graph": "bar",
                "data": [
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Age-grade distortion rate: early years of Elementary School - Municipal Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Age-grade distortion rate: final years of Elementary School - Municipal Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_MUNICIPAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Age-grade distortion rate: High School - Municipal public network"
                     },

                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Age-grade distortion rate: early years of Elementary School - State Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Age-grade distortion rate: final years of Elementary School - State Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDI_EFFINAL_ESTADUAL", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Age-grade distortion rate: High School - State public network"
                     },

                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDIANOSFINAISPUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_1"},
                     "label": "Age-grade distortion rate: early years of Elementary School - Total Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDIANOSFINAISPUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_2"},
                     "label": "Age-grade distortion rate: final years of Elementary School - Public Network"
                     },
                    {"agency": "BRAZIL_CO", "id": "BRAZIL_CO", "version": "1.0",
                     "dq": {"REF_AREA": "", "INDICATOR": "TDIANOSFINAISPUB", "AGE": "_T",
                            "EDUCATION_LEVEL": "ISCED11_3"},
                     "label": "Age-grade distortion rate: High School - Public Network"
                     },

                ],
                "default": "EDUNF_ROFST_L1",
            }

        }
    }
}


def get_layout(**kwargs):
    # kwargs["indicators"] = indicators_dict
    # kwargs["main_title"] = main_title
    # kwargs["main_title"] = cfg["main_title"]
    kwargs["cfg"] = cfg
    return get_base_layout(**kwargs)
