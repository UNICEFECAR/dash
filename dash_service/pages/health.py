from collections import defaultdict
import plotly.express as px

# from . import data, years
from .base_page import get_base_layout

cfg = {
    "ddl_ref_areas_cl": {
        "agency": "BRAZIL_CO",
        "id": "CL_BRAZIL_REF_AREAS",
    },
    "main_title": "Health",
    "THEMES": {
        "IMMUNIZATION": {
            "NAME": "Immunization",
            "CARDS": [
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "IMUNOPOLIO",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "% of Polio immunization coverage",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "IMUNOTRIPLICED1",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "% of Triple Viral D1 immunization coverage (Measles, mumps, and rubella)",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "IMUNOTRIPLICEDTP",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "% of Triple bacterial DTP immunization coverage (Diphtheria, tetanus, and whooping cough)",
                },
            ],
            "MAIN": {
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
                        "name": "Country",
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750,
                },
                "name": "Immunization",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOPOLIO",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOTRIPLICED1",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of Elementary School"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOTRIPLICEDTP",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - High School"
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOPOLIO",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of elementary school 1"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOTRIPLICED1",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school 2"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOTRIPLICEDTP",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "IMUNOTRIPLICED1",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    }
                ],
                "default": "EDUNF_ROFST_L1",
            },
        },
        "MNCH": {
            "NAME": "Maternal, Newborn and Child Health",
            "CARDS": [
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "PREMATUROPORCENTAGEM",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "TDIANOSFINAISPUB",
                    "suffix": "% of premature births - less than 37 weeks",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "MORTALIDADEINFANTIL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Infant mortality rate",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "RAZAOMORTALIDADEMAT",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Maternal mortality ratio",
                },
            ],
            "MAIN": {
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
                        "name": "Country",
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750,
                },
                "name": "Maternal, Newborn and Child Health",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Children born alive to mothers 10 to 14 years of age",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 10 to 14 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y15T19",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 15 to 19 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PREMATUROPORCENTAGEM",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of premature births - less than 37 weeks",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANTIL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Infant mortality rate",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANCIAMENOR5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Childhood mortality rate - under 5 years old",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADENEONATAL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Neonatal mortality rate - 0 to 27 days",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "RAZAOMORTALIDADEMAT",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Maternal mortality ratio",
                    },
                ],
            },
            "AREA_1": {
                "name": "Mortality",
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANTIL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANCIAMENOR5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADENEONATAL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "RAZAOMORTALIDADEMAT",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    },
                ],
            },
            "AREA_2": {
                "name": "Births",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="name",
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Children born alive to mothers 10 to 14 years of age",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 10 to 14 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14",
                            "AGE": "Y15T19",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Children born alive to mothers 15 to 19 years of age",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y15T19",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 15 to 19 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PREMATUROPORCENTAGEM",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                    },
                ],
            },
            "AREA_3": {
                "name": "Maternal, Newborn and Child Health",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="name",
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Children born alive to mothers 10 to 14 years of age",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y10T14",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 10 to 14 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "NASCIMENTOS10A14PERCENTAGEM",
                            "AGE": "Y15T19",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of live births to mothers aged 15 to 19 years",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PREMATUROPORCENTAGEM",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "% of premature births - less than 37 weeks",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANTIL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Infant mortality rate",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADEINFANCIAMENOR5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Childhood mortality rate - under 5 years old",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "MORTALIDADENEONATAL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Neonatal mortality rate - 0 to 27 days",
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "RAZAOMORTALIDADEMAT",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "label": "Maternal mortality ratio",
                    },
                ],
            },
        },
        "VECTOR_DISEASE": {
            "NAME": "Vector-borne diseases",
            "CARDS": [
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "DENGUEINCIDENCIA",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Dengue incidence rate",
                },
            ],
            "MAIN": {
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
                        "name": "Country",
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750,
                },
                "name": "Vector-borne diseases",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "DENGUEINCIDENCIA",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "DENGUETOTAL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of Elementary School"
                    },
                ],
            },
            "AREA_1": {
                "name": "Vector-borne diseases",
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "DENGUEINCIDENCIA",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of elementary school 1"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "DENGUETOTAL",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school 2"
                    },
                ],
            },
        },
        "NUTRITION": {
            "NAME": "Nutrition",
            "CARDS": [
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "PESO0A5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Overweight: % of children aged 0 to 5 years with high weight for their age",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "PESO5A9",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Overweight: % of children aged 5 to 9 years who are overweight for their age",
                },
                {
                    "data": {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "BR",
                            "INDICATOR": "PESOADOLESCENTES",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        "lastnobservations": 1,
                    },
                    "name": "",
                    "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                    "suffix": "Overweight: overweight adolescents aged 10 to 19",
                },
            ],
            "MAIN": {
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
                        "name": "Country",
                    },
                    "hover_data": {
                        "OBS_VALUE": True,
                        "REF_AREA": False,
                        "name": True,
                        "TIME_PERIOD": True,
                    },
                    "animation_frame": "TIME_PERIOD",
                    "height": 750,
                },
                "name": "Nutrition",
                # "indicator": "EDUNF_OFST_L1,EDUNF_OFST_L2,EDUNF_OFST_L3",
                "suffix": "Primary to upper secondary aged Children and Adolescents",
                "data": [
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESO0A5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESO5A9",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of Elementary School"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESOADOLESCENTES",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of Elementary School"
                    },
                ],
            },
            "AREA_1": {
                "name": "Nutrition",
                "graphs": {
                    "bar": {
                        "options": dict(
                            x="name",
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
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESO0A5",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - final years of elementary school 1"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESO5A9",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school 2"
                    },
                    {
                        "agency": "BRAZIL_CO",
                        "id": "BRAZIL_CO",
                        "version": "1.0",
                        "dq": {
                            "REF_AREA": "",
                            "INDICATOR": "PESOADOLESCENTES",
                            "AGE": "_T",
                            "EDUCATION_LEVEL": "_T",
                        },
                        # "label": "% of school dropout - early years of elementary school 2"
                    },
                ],
            },
        },
    },
}


def get_layout(**kwargs):
    # kwargs["indicators"] = indicators_dict
    # kwargs["main_title"] = main_title
    # kwargs["main_title"] = cfg["main_title"]
    kwargs["cfg"] = cfg
    return get_base_layout(**kwargs)
