from dash_html_components.Title import Title
import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "HS": {
        "NAME": "Health System",
        "CARDS": [
            {
                "name": "Current health expenditure as % of GDP",
                "indicator": "HT_SH_XPD_CHEX_GD_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
            {
                "name": "Out-of-pocket expenditure (OOPS), as % of current health expenditure",
                "indicator": "HT_SH_XPD_OOPC_CH_ZS",
                "suffix": "Percent range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Health System - coverage, expenditure, and insurance",
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
                "HT_SH_ACS_UNHC",
                "HT_ADOL_UNMETMED_NOUNMET",
                "HT_ADOL_UNMETMED_TOOEXP",
                "HT_ADOL_UNMETMED_TOOFAR",
                "HT_ADOL_UNMETMED_WAITING",
                "HT_ADOL_UNMETMED_TOOEFW",
                "HT_ADOL_UNMETMED_NOTIME",
                "HT_ADOL_UNMETMED_NOKNOW",
                "HT_ADOL_UNMETMED_FEAR",
                "HT_ADOL_UNMETMED_HOPING",
                "HT_ADOL_UNMETMED_OTH",
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_CH_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_GHED_PC_CD",
                "HT_SH_XPD_PVTD_CH_ZS",
                "HT_SH_XPD_PVTD_PP_CD",
                "HT_SH_XPD_PVTD_PC_CD",
                "HT_SH_XPD_CHEX_PP_CD",
                "HT_SH_XPD_CHEX_PC_CD",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_SH_XPD_OOPC_PP_CD",
                "HT_SH_XPD_OOPC_PC_CD",
                "HT_INS_COV",
            ],
            "default": "HT_SH_ACS_UNHC",
        },
        "AREA_1": {
            "name": "Unmet needs for medical examination",
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
                "HT_SH_ACS_UNHC",
                "HT_ADOL_UNMETMED_NOUNMET",
                "HT_ADOL_UNMETMED_TOOEXP",
                "HT_ADOL_UNMETMED_TOOFAR",
                "HT_ADOL_UNMETMED_WAITING",
                "HT_ADOL_UNMETMED_TOOEFW",
                "HT_ADOL_UNMETMED_NOTIME",
                "HT_ADOL_UNMETMED_NOKNOW",
                "HT_ADOL_UNMETMED_FEAR",
                "HT_ADOL_UNMETMED_HOPING",
                "HT_ADOL_UNMETMED_OTH",
            ],
            "default": "HT_SH_ACS_UNHC",
        },
        "AREA_2": {
            "name": "Coverage index,  Expenditures, and Insurance",
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
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_CH_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_GHED_PC_CD",
                "HT_SH_XPD_PVTD_CH_ZS",
                "HT_SH_XPD_PVTD_PP_CD",
                "HT_SH_XPD_PVTD_PC_CD",
                "HT_SH_XPD_CHEX_PP_CD",
                "HT_SH_XPD_CHEX_PC_CD",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_SH_XPD_OOPC_PP_CD",
                "HT_SH_XPD_OOPC_PC_CD",
                "HT_INS_COV",
            ],
            "default_graph": "line",
            "default": "HT_SH_XPD_CHEX_GD_ZS",
        },
    },
    "MNCH": {
        "NAME": "Maternal, newborn and child health",
        "CARDS": [
            {
                "name": "Neonatal mortality rate (per 1,000 live births)",
                "indicator": "CME_MRM0",
                "suffix": "Range among countries",
                "min_max": True,
            },
            {
                "name": "Under-5 mortality rate  (per 1,000 live births)",
                "indicator": "CME_MRY0T4",
                "suffix": "Range among countries",
                "min_max": True,
            },
            {
                "name": "of under-five deaths",
                "indicator": "CME_TMY0T4",
                "suffix": "Number",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "Status of Maternal, Newborn, and Child Health",
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
                "CME_MRY0T4",
                "CME_MRY0",
                "CME_MRM0",
                "MNCH_MMR",
                "MNCH_SAB",
                "MNCH_PNCMOM",
                "CME_TMY0T4",
                "CME_SBR",
                "CME_PND",
                "HT_U5DEATH_AIDS",
                "HT_U5DEATH_DIAR",
                "HT_U5DEATH_PERT",
                "HT_U5DEATH_TETA",
                "HT_U5DEATH_MEAS",
                "HT_U5DEATH_MENI",
                "HT_U5DEATH_MALA",
                "HT_U5DEATH_PNEU",
                "HT_U5DEATH_PRET",
                "HT_U5DEATH_INTR",
                "HT_U5DEATH_SEPS",
                "HT_U5DEATH_OTHE",
                "HT_U5DEATH_CONG",
                "HT_U5DEATH_NCDS",
                "HT_U5DEATH_INJU",
                "MNCH_CSEC",
                "MNCH_PNCMOM",
                "MNCH_ANC4",
                "MNCH_PNEUCARE",
                # "MT_SDG_SUICIDE",
            ],
            "default": "CME_MRY0T4",
        },
        "AREA_1": {
            "name": "Mortality rates - NMR, IMR, U5M, MMR",
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
            "default": "CME_MRY0T4",
            "indicators": [
                "CME_MRY0T4",
                "CME_MRY0",
                "CME_MRM0",
                "MNCH_MMR",
                "CME_TMY0T4",
                "CME_SBR",
            ],
        },
        "AREA_2": {
            "name": "Health Services and Mortality by Causes",
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
                "MNCH_SAB",
                "MNCH_PNCMOM",
                "CME_PND",
                "HT_U5DEATH_AIDS",
                "HT_U5DEATH_DIAR",
                "HT_U5DEATH_PERT",
                "HT_U5DEATH_TETA",
                "HT_U5DEATH_MEAS",
                "HT_U5DEATH_MENI",
                "HT_U5DEATH_MALA",
                "HT_U5DEATH_PNEU",
                "HT_U5DEATH_PRET",
                "HT_U5DEATH_INTR",
                "HT_U5DEATH_SEPS",
                "HT_U5DEATH_OTHE",
                "HT_U5DEATH_CONG",
                "HT_U5DEATH_NCDS",
                "HT_U5DEATH_INJU",
                "MNCH_CSEC",
                "MNCH_PNCMOM",
                "MNCH_ANC4",
                "MNCH_PNEUCARE",
                # "MT_SDG_SUICIDE",
            ],
            "default_graph": "line",
            "default": "MNCH_SAB",
        },
    },
    "IMMUNIZATION": {
        "NAME": "Immunization",
        "CARDS": [
            {
                "name": "Surviving infants who received the third dose of DPT-containing vaccine",
                "indicator": "IM_DTP3",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "districts with at least 80 percent of DTP3 coverage",
                "indicator": "HT_DIST80DTP3_P",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Immunization - access and coverage",
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
                "IM_DTP3",
                "HT_SH_ACS_DTP3",
                "HT_SH_ACS_HPV",
                "HT_SH_ACS_MCV2",
                "HT_SH_ACS_PCV3",
                "IM_MCV1",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
            ],
            "default": "IM_DTP3",
        },
        "AREA_1": {
            "name": "DPT, PCV3 and Measles vaccine",
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
                "IM_DTP3",
                "HT_SH_ACS_HPV",
                "HT_SH_ACS_MCV2",
                "HT_SH_ACS_PCV3",
                "IM_MCV1",
            ],
            "default": "IM_DTP3",
        },
        "AREA_2": {
            "name": "DTP3 Coverage",
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
                "HT_SH_ACS_DTP3",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
            ],
            "default_graph": "line",
            "default": "HT_SH_ACS_DTP3",
        },
    },
    "NUTRITION": {
        "NAME": "Nutrition",
        "CARDS": [
            {
                "name": "Prevalence of overweight among children under 5 years of age",
                "indicator": "NT_ANT_WHZ_PO2",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Prevalence of stunting among children under 5 years of age",
                "indicator": "NT_ANT_HAZ_NE2",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Infants 0-5 months of age who are fed exclusively with breast milk",
                "indicator": "NT_BF_EXBF",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Nutrition status",
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
                "NT_BW_LBW",
                "NT_BF_EIBF",
                "NT_BF_EXBF",
                "NT_CF_MAD",
                "NT_ANT_WHZ_PO2",
                "NT_ANT_HAZ_NE2",
                "HT_SN_STA_OVWGTN",
                "HT_SH_STA_ANEM",
                "HT_SH_STA_ANEM_NPRG",
                "HT_SH_STA_ANEM_PREG",
                "NT_BW_UNW",
            ],
            "default": "NT_BW_LBW",
        },
        "AREA_1": {
            "name": "Nutrition and IYFC",
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
                "NT_BW_LBW",
                "NT_BF_EIBF",
                "NT_BF_EXBF",
                "NT_CF_MAD",
                "NT_ANT_WHZ_PO2",
                "NT_ANT_HAZ_NE2",
                "HT_SN_STA_OVWGTN",
                "NT_BW_UNW",
            ],
            "default": "NT_BW_LBW",
        },
        "AREA_2": {
            "name": "Prevalence of Anaemia",
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
                "NT_ANT_WHZ_PO2",
                "HT_SH_STA_ANEM",
                "HT_SH_STA_ANEM_NPRG",
                "HT_SH_STA_ANEM_PREG",
            ],
            "default_graph": "line",
            "default": "NT_ANT_WHZ_PO2",
        },
    },
    "ADOLESCENTS": {
        "NAME": "Adolescent physical, mental, and reproductive health",
        "CARDS": [
            {
                "name": "Adolescent birth rate for age 15-19 years (per 1,000 women)",
                "indicator": "FT_SP_DYN_ADKL",
                "suffix": "Range among countries",
                "sex": "Female",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Adolescent Health Status",
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
                "FT_SP_DYN_ADKL",
                "HT_SH_FPL_MTMM",
                "HT_ADOL_MT",
                "HT_SH_PRV_SMOK",
                "HT_CDRT_SELF_HARM",
                "HT_ADOL_MEAL",
                "HT_ADOL_NO_EXCS",
                "HT_ADOL_VGRS_EXCS",
                "HT_CHLD_BODY_RGHT",
                "HT_CHLD_BODY_NO_RGHT",
                "HT_CHLD_REG_SMOK",
                "HT_CHLD_DRNK",
                "HT_ADOL_HIGH_SATS",
                "HT_ADOL_LOW_SATS",
            ],
            "default": "FT_SP_DYN_ADKL",
        },
        "AREA_1": {
            "name": "Birth, Mortality, and Suicide Rates including Life Satisfaction",
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
                "FT_SP_DYN_ADKL",
                "HT_ADOL_MT",
                "HT_ADOL_HIGH_SATS",
                "HT_ADOL_LOW_SATS",
            ],
            "default": "FT_SP_DYN_ADKL",
        },
        "AREA_2": {
            "name": "Lifestyle and Family Planning",
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
                "HT_SH_FPL_MTMM",
                "HT_ADOL_MT",
                "HT_SH_PRV_SMOK",
                "HT_ADOL_MEAL",
                "HT_ADOL_NO_EXCS",
                "HT_ADOL_VGRS_EXCS",
                "HT_CHLD_BODY_RGHT",
                "HT_CHLD_BODY_NO_RGHT",
                "HT_CHLD_REG_SMOK",
                "HT_CHLD_DRNK",
            ],
            "default_graph": "line",
            "default": "HT_SH_FPL_MTMM",
        },
    },
    "HIVAIDS": {
        "NAME": "HIV/AIDS",
        "CARDS": [
            {
                "name": "per 1,000 uninfected population",
                "indicator": "HT_SH_HIV_INCD",
                "suffix": "Number of new HIV infections",
                "absolute": True,
                "average": True,
            },
            {
                "name": "(aged 0-14 years) living with HIV",
                "indicator": "HT_SH_HIV_0014",
                "suffix": "Children",
                "absolute": True,
            },
            {
                "name": "Children (aged 0-14 years) living with HIV and receiving antiretroviral therapy (ART)",
                "indicator": "HVA_PED_ART_CVG",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "HIV/AIDS",
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
                "HT_SH_HIV_INCD",
                "HVA_PMTCT_ARV_CVG",
                "HT_SH_HIV_0014",
                "HVA_EPI_LHIV_0-19",
                "HVA_EPI_LHIV_15-24",
                "HVA_EPI_INF_RT_0-14",
                "HVA_EPI_INF_RT_10-19",
                "HVA_PED_ART_NUM",
                "HVA_PED_ART_CVG",
            ],
            "default": "HT_SH_HIV_INCD",
        },
        "AREA_1": {
            "name": "Living with HIV and/or receiving antiretroviral therapy (ART)",
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
                "HVA_PMTCT_ARV_CVG",
                "HT_SH_HIV_0014",
                "HVA_EPI_LHIV_0-19",
                "HVA_EPI_LHIV_15-24",
                "HVA_PED_ART_NUM",
                "HVA_PED_ART_CVG",
            ],
            "default": "HVA_PMTCT_ARV_CVG",
        },
        "AREA_2": {
            "name": "Estimated Incidence Rate",
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
                "HT_SH_HIV_INCD",
                "HVA_EPI_INF_RT_0-14",
                "HVA_EPI_INF_RT_10-19",
            ],
            "default_graph": "line",
            "default": "HT_SH_HIV_INCD",
        },
    },
    "WASH": {
        "NAME": "Water, sanitation and hygiene",
        "CARDS": [
            {
                "name": "Population using safely managed drinking water service",
                "indicator": "WS_PPL_W-SM",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Population using safely managed sanitation services",
                "indicator": "WS_PPL_S-SM",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Drinking Water and Sanitation Services",
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
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "WS_PPL_H-B",
                "WS_PPS_S-OD",
                "HT_NO_BTH_SHW_FLSH",
            ],
            "default": "WS_PPL_W-SM",
        },
        "AREA_1": {
            "name": "Safely Managed Drinking Water Services",
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
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "WS_PPL_H-B",
                "WS_PPS_S-OD",
                "HT_NO_BTH_SHW_FLSH",
            ],
            "default": "WS_PPL_W-SM",
        },
        "AREA_2": {
            "name": "Sanitation services",
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
                "WS_PPL_S-SM",
                "WS_PPL_H-B",
                "WS_PPS_S-OD",
                "HT_NO_BTH_SHW_FLSH",
            ],
            "default_graph": "line",
            "default": "WS_PPL_S-SM",
        },
    },
}

main_title = "Child Health"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
