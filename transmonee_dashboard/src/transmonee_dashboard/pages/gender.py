import plotly.express as px
from .base_page import get_base_layout, geo_json_countries

indicators_dict = {
    "GENDER": {
        "NAME": "Cross-Cutting Issues",
        "CARDS": [
            {
                "name": "Girls completion rate - Upper secondary education",
                "indicator": "EDUNF_CR_L3",
                "suffix": "Range among countries",
                "sex": "F",
                "min_max": True,
            },
            {
                "name": "Adolescent birth rate for age 15-19 years (per 1,000 women)",
                "indicator": "FT_SP_DYN_ADKL",
                "suffix": "Range among countries",
                "sex": "F",
                "min_max": True,
            },
            {
                "name": "Gender Development Index",
                "indicator": "EC_GDI",
                "suffix": "Range among countries",
                "min_max": True,
            },
            {
                "name": "Gender Inequality Index",
                "indicator": "EC_GII",
                "suffix": "Range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Gender Data",
            "geo": "Country_name",
            "options": dict(
                geojson=geo_json_countries,
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
                "EC_GII",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NARA_L1_UNDER1",
                "EDUNF_ROFST_L1_UNDER1",
                "EDUNF_EA_L2T8",
                "EDU_SE_GPI_PTNPRE",
                "EDU_SDG_YOUTH_NEET",
                "EDU_SE_AGP_CPRA_L1",
                "EDU_SE_AGP_CPRA_L2",
                "EDU_SE_AGP_CPRA_L3",
                "EDU_SE_ALP_CPLR_L1",
                "EDU_SE_ALP_CPLR_L2",
                "EDU_SE_ALP_CPLR_L3",
                "EDU_SE_AWP_CPRA_L1",
                "EDU_SE_AWP_CPRA_L2",
                "EDU_SE_AWP_CPRA_L3",
                "EDUNF_STEM_GRAD_RT",
                "FT_SP_DYN_ADKL",
                "HT_SH_FPL_MTMM",
                # "HT_SH_HIV_INCD ",
                "HT_DIST79DTP3_P",
                "HT_SH_ACS_DTP3",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
                "HT_SH_STA_ANEM",
                "HT_SH_STA_ANEM_NPRG",
                "HT_SH_STA_ANEM_PREG",
                "HT_ADOL_MT",
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "IM_DTP3",
                "IM_MCV1",
                "MNCH_MMR",
                "MNCH_CSEC",
                "MNCH_INSTDEL",
                "MNCH_BIRTH18",
                "CME_MRM0",
                "MNCH_SAB",
                "CME_MRY0T4",
                "WS_PPL_S-SM",
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PV_SI_POV_DAY1",
                "PV_SI_POV_EMP1",
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
                "PV_SDG_SI_POV_NAHC",
                "DM_CHLD_POP_PT",
                "DM_LIFE_EXP",
                "EC_GII",
                "EC_GDI",
                "EC_EAP_RT",
                "EC_IQ_CPA_GNDR_XQ",
                "EC_SIGI",
                "SG_GEN_PARL",
                "SL_DOM_TSPD",
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "DM_CHLD_TWO_PRNT",
                "DM_SP_POP_BRTH_MF",
                "DM_ADOL_YOUTH_POP",
                "EC_SL_UEM_TOTL_NE_ZS",
                "EC_SL_UEM_TOTL_ZS",
                "PP_SE_GPI_ICTS_ATCH",
                "PP_SE_GPI_ICTS_CPT",
                "PP_SE_GPI_ICTS_CDV",
                "PP_SE_GPI_ICTS_SSHT",
                "PP_SE_GPI_ICTS_PRGM",
                "PP_SE_GPI_ICTS_PST",
                "PP_SE_GPI_ICTS_SFWR",
                "PP_SE_GPI_ICTS_TRFF",
                "PP_SE_GPI_ICTS_CMFL",
                "GN_MTNTY_LV_BNFTS",
                "GN_PTNTY_LV_BNFTS",
                "PP_ADOL_INET",
                "PP_ADOL_WORK_HOME",
            ],
            "default": "EC_GII",
        },
        "AREA_1": {
            "name": "Education",
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
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NARA_L1_UNDER1",
                "EDU_SDG_YOUTH_NEET",
                "EDUNF_ROFST_L1_UNDER1",
                "EDUNF_EA_L2T8",
                "EDU_SE_GPI_PTNPRE",
                "EDU_SE_AGP_CPRA_L1",
                "EDU_SE_AGP_CPRA_L2",
                "EDU_SE_AGP_CPRA_L3",
                "EDU_SE_ALP_CPLR_L1",
                "EDU_SE_ALP_CPLR_L2",
                "EDU_SE_ALP_CPLR_L3",
                "EDU_SE_AWP_CPRA_L1",
                "EDU_SE_AWP_CPRA_L2",
                "EDU_SE_AWP_CPRA_L3",
                "EDUNF_STEM_GRAD_RT",
            ],
            "default": "EDU_SDG_STU_L1_G2OR3_REA",
        },
        "AREA_2": {
            "name": "Family Environment and Protection",
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
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
            ],
            "default_graph": "bar",
            "default": "PT_F_20-24_MRD_U15",
        },
        "AREA_3": {
            "name": "Health and Nutrition",
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
                "FT_SP_DYN_ADKL",
                "HT_SH_FPL_MTMM",
                # "HT_SH_HIV_INCD ",
                "HT_DIST79DTP3_P",
                "HT_SH_ACS_DTP3",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
                "HT_SH_STA_ANEM",
                "HT_SH_STA_ANEM_NPRG",
                "HT_SH_STA_ANEM_PREG",
                "HT_ADOL_MT",
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "IM_DTP3",
                "IM_MCV1",
                "MNCH_MMR",
                "MNCH_CSEC",
                "MNCH_INSTDEL",
                "MNCH_BIRTH18",
                "CME_MRM0",
                "MNCH_SAB",
                "CME_MRY0T4",
            ],
            "default_graph": "bar",
            "default": "FT_SP_DYN_ADKL",
        },
        "AREA_4": {
            "name": "Poverty and Social Protection",
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
                "PV_SI_POV_DAY1",
                "PV_SI_POV_EMP1",
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
                "PV_SDG_SI_POV_NAHC",
            ],
            "default_graph": "bar",
            "default": "PV_SI_POV_EMP1",
        },
        "AREA_5": {
            "name": "Child Rights Landscape and Governance",
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
                "DM_CHLD_POP_PT",
                "EC_GII",
                "EC_GDI",
                "EC_EAP_RT",
                "EC_IQ_CPA_GNDR_XQ",
                "EC_SIGI",
                "DM_CHLD_TWO_PRNT",
                "DM_SP_POP_BRTH_MF",
                "DM_ADOL_YOUTH_POP",
                "EC_SL_UEM_TOTL_NE_ZS",
                "EC_SL_UEM_TOTL_ZS",
                "SG_GEN_PARL",
                "SL_DOM_TSPD",
                "CR_SH_STA_AIRP",
                "CR_SH_STA_ASAIRP",
                "DM_LIFE_EXP",
                "GN_MTNTY_LV_BNFTS",
                "GN_PTNTY_LV_BNFTS",
                "CR_AAP_DEATH",
                "CR_HAP_DEATH",
            ],
            "default_graph": "bar",
            "default": "DM_CHLD_POP_PT",
        },
        "AREA_6": {
            "name": "Participation and Civil Rights",
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
                "PP_SE_GPI_ICTS_ATCH",
                "PP_SE_GPI_ICTS_CPT",
                "PP_SE_GPI_ICTS_CDV",
                "PP_SE_GPI_ICTS_SSHT",
                "PP_SE_GPI_ICTS_PRGM",
                "PP_SE_GPI_ICTS_PST",
                "PP_SE_GPI_ICTS_SFWR",
                "PP_SE_GPI_ICTS_TRFF",
                "PP_SE_GPI_ICTS_CMFL",
                "PP_ADOL_INET",
                "PP_ADOL_WORK_HOME",
            ],
            "default_graph": "bar",
            "default": "PP_SE_GPI_ICTS_ATCH",
        },
    },
}

main_title = "Gender"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)