import pandas as pd

import plotly.express as px

from . import data, years
from .base_page import get_base_layout

indicators_dict = {
    "DEMOGRAPHY": {
        "NAME": "Demography about Children",
        "CARDS": [
            # {
            #     "name": "age 0-17 years",
            #     "indicator": "",
            #     "suffix": "Total child population",
            #     "absolute": True,
            # },
            {
                "name": "Children (0-17) living with two parents",
                "indicator": "DM_CHLD_TWO_PRNT",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Demography",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "DM_CHLD_TWO_PRNT",
                "DM_FRATE_TOT",
            ],
            "default": "DM_FRATE_TOT",
        },
        "AREA_1": {
            "name": " Child Population and Living Arrangements",
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "DM_CHLD_TWO_PRNT",
            ],
            "default": "DM_CHLD_TWO_PRNT",
        },
        "AREA_2": {
            "name": "Total Fertility Rate",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "DM_FRATE_TOT",
            ],
            "default_graph": "bar",
            "default": "DM_FRATE_TOT",
        },
    },
    "ECONOMY": {
        "NAME": "Political Economy",
        "CARDS": [
            {
                "name": "Human Development Index (HDI)",
                "indicator": "EC_HDI",
                "suffix": "Index value range among countries",
                "min_max": True,
            },
            {
                "name": "Unemployment estimate as % of Total Labor Force",
                "indicator": "EC_SL_UEM_TOTL_NE_ZS",
                "suffix": "Index value range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Political Economy",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "EC_HDI",
                "EC_NY_GDP_MKTP_KD_ZG",
                "EC_NY_GDP_PCAP_KD_ZG",
                "EC_NE_DAB_TOTL_ZS",
                "EC_TEC_GRL_GOV_EXP",
                "EC_TEC_CNT_GOV_EXP",
                "EC_TEC_STA_GOV_EXP",
                "EC_TEC_LOC_GOV_EXP",
                "EC_TEC_SSF_EXP",
                "EC_GR_G14_GDP",
                "EDU_FIN_EXP_PT_GDP",
                "HT_SH_XPD_GHED_GD_ZS",
                "EC_SP_GOV_EXP_GDP",
                "EC_SP_GOV_EXP_TOT",
                "EC_NY_GDP_PCAP_PP_CD",
                "EC_NY_GNP_ATLS_CD",
                "EC_NY_GNP_PCAP_CD",
                "EC_GC_DOD_TOTL_GD_ZS",
                "EC_SI_POV_GINI",
                "EC_SL_UEM_TOTL_NE_ZS",
            ],
            "default": "EC_HDI",
        },
        "AREA_1": {
            "name": "GDP and Public expenditure",
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            # compare is the default selection
            "compare": "Sex",
            "default": "EC_NY_GDP_MKTP_KD_ZG",
            "indicators": [
                "EC_NY_GDP_MKTP_KD_ZG",
                "EC_NY_GDP_PCAP_KD_ZG",
                "EC_NE_DAB_TOTL_ZS",
                "EC_TEC_GRL_GOV_EXP",
                "EC_TEC_CNT_GOV_EXP",
                "EC_TEC_STA_GOV_EXP",
                "EC_TEC_LOC_GOV_EXP",
                "EC_TEC_SSF_EXP",
                "EC_GR_G14_GDP",
                "EDU_FIN_EXP_PT_GDP",
                "HT_SH_XPD_GHED_GD_ZS",
                "EC_SP_GOV_EXP_GDP",
                "EC_SP_GOV_EXP_TOT",
                "EC_NY_GNP_ATLS_CD",
                "EC_NY_GNP_PCAP_CD",
                "EC_GC_DOD_TOTL_GD_ZS",
                "EC_SL_UEM_TOTL_ZS",
            ],
        },
        "AREA_2": {
            "name": "Human Development and GDP",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "EC_HDI",
                "EC_NY_GDP_PCAP_PP_CD",
                "EC_SI_POV_GINI",
                "EC_SL_UEM_TOTL_NE_ZS",
                "EC_SL_UEM_TOTL_ZS",
            ],
            "default_graph": "line",
            "default": "EC_HDI",
        },
    },
    "MIGRATION": {
        "NAME": "Migration and Displacement",
        "CARDS": [
            {
                "name": "Net Migration",
                "indicator": "EC_SL_UEM_TOTL_ZS",
                "suffix": "Thousands of persons",
                "absolute": True,
            },
            {
                "name": "Asylum applicants considered to be unaccompanied minors",
                "indicator": "DM_ASYL_FRST",
                "suffix": "Persons",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "Migration and Displacement",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "DM_POP_NETM",
                "DM_SM_POP_REFG",
                "DM_SM_POP_REFG_OR",
                "DM_ASYL_FRST",
                "DM_ASYL_UASC",
                "MG_INTNL_MG_CNTRY_DEST_PS",
            ],
            "default": "DM_POP_NETM",
        },
        "AREA_1": {
            "name": "Migration",
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "DM_SM_POP_REFG",
                "MG_INTNL_MG_CNTRY_DEST_PS",
            ],
            "default": "DM_SM_POP_REFG",
        },
        "AREA_2": {
            "name": "Refugee",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "DM_SM_POP_REFG",
                "DM_SM_POP_REFG_OR",
                "DM_ASYL_FRST",
                "DM_ASYL_UASC",
            ],
            "default_graph": "line",
            "default": "DM_SM_POP_REFG",
        },
    },
    "RISKS": {
        "NAME": "Risks, humanitarian situation and impact of climate change",
        "CARDS": [
            {
                "name": "Deaths and missing persons attributed to disasters (per 100,000 population)",
                "indicator": "CR_VC_DSR_MTMP",
                "suffix": "Rate range among countries",
                "min_max": True,
            },
            {
                "name": "Population with primary reliance on clean fuels and technology",
                "indicator": "CR_EG_EGY_CLEAN",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Risks, humanitarian situation and impact of climate change",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "CR_VC_DSR_MTMP",
                "CR_VC_DSR_DAFF",
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "CR_EG_EGY_CLEAN",
                "CR_EG_ACS_ELEC",
                "CR_SG_DSR_LGRGSR",
            ],
            "default": "CR_VC_DSR_MTMP",
        },
        "AREA_1": {
            "name": "Risks and Humanitarian Situation",
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "CR_VC_DSR_MTMP",
                "CR_VC_DSR_DAFF",
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "CR_SG_DSR_LGRGSR",
            ],
            "default": "CR_VC_DSR_MTMP",
        },
        "AREA_2": {
            "name": "Clean Environment",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "CR_EG_EGY_CLEAN",
                "CR_EG_ACS_ELEC",
            ],
            "default": "CR_EG_EGY_CLEAN",
            "default_graph": "line",
        },
    },
    "DATASPENDING": {
        "NAME": "Data and Public spending on Children",
        "CARDS": [
            {
                "name": "Government expenditure on education as a % of GDP",
                "indicator": "EDU_FIN_EXP_PT_GDP",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Total public social expenditure as of % of GDP",
                "indicator": "EC_TOT_PUB_EXP_GDP",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "with national statistical legislation exists that complies with the Fundamental Principles of Official Statistics",
                "indicator": "CR_SG_STT_FPOS",
                "suffix": "Countries",
                "absolute": True,
            },
            {
                "name": "that have conducted at least one population and housing census in the last 10 years",
                "indicator": "CR_SG_REG_CENSUSN",
                "suffix": "Countries",
                "absolute": True,
            },
        ],
        "MAIN": {
            "name": "Availability of data and Public Expendiure on Children",
            "geo": "Geographic area",
            "options": dict(
                lat="latitude",
                lon="longitude",
                size="OBS_VALUE",
                text="Geographic area",
                color="OBS_VALUE",
                color_continuous_scale=px.colors.sequential.GnBu,
                size_max=40,
                zoom=2.5,
                animation_frame="TIME_PERIOD",
                height=750,
            ),
            "indicators": [
                "EDU_FIN_EXP_PT_GDP",
                "HT_SH_XPD_GHED_GD_ZS",
                "EC_SP_GOV_EXP_GDP",
                "EC_TOT_PUB_EXP_GDP",
                "EC_TOT_PUB_EXP_TOT",
                "EC_FAM_PUB_EXP_GDP",
                "EC_FAM_PUB_EXP_TOT",
                "CR_IQ_SCI_OVRL",
                "CR_SG_STT_FPOS",
                "CR_SG_STT_NSDSFND",
                "CR_SG_STT_NSDSIMPL",
                "CR_SG_STT_NSDSFDGVT",
                "CR_SG_STT_NSDSFDDNR",
                "CR_SG_STT_NSDSFDOTHR",
                "CR_SG_STT_CAPTY",
                "CR_SG_REG_CENSUSN",
            ],
            "default": "EC_TOT_PUB_EXP_TOT",
        },
        "AREA_1": {
            "name": "Government Spending on Children",
            "type": "bar",
            "options": dict(
                x="Geographic area",
                y="OBS_VALUE",
                barmode="group",
                text="TIME_PERIOD",
            ),
            "compare": "Sex",
            "indicators": [
                "EDU_FIN_EXP_PT_GDP",
                "HT_SH_XPD_GHED_GD_ZS",
                "EC_SP_GOV_EXP_GDP",
                "EC_TOT_PUB_EXP_GDP",
                "EC_TOT_PUB_EXP_TOT",
                "EC_FAM_PUB_EXP_GDP",
                "EC_FAM_PUB_EXP_TOT",
            ],
            "default": "EC_TOT_PUB_EXP_TOT",
        },
        "AREA_2": {
            "name": "Availalbity of Data on Children",
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Geographic area",
                        y="OBS_VALUE",
                        barmode="group",
                        text="TIME_PERIOD",
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
                "CR_IQ_SCI_OVRL",
                "CR_SG_STT_FPOS",
                "CR_SG_STT_NSDSFND",
                "CR_SG_STT_NSDSIMPL",
                "CR_SG_STT_NSDSFDGVT",
                "CR_SG_STT_NSDSFDDNR",
                "CR_SG_STT_NSDSFDOTHR",
                "CR_SG_STT_CAPTY",
                "CR_SG_REG_CENSUSN",
            ],
            "default": "CR_IQ_SCI_OVRL",
            "default_graph": "line",
        },
    },
}


main_title = "Child Rights Landscape"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
