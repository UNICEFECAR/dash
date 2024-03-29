import plotly.express as px
from .base_page import get_base_layout, geo_json_countries

indicators_dict = {
    "ECD": {
        "NAME": "Cross-Cutting Issues",
        "CARDS": [
            {
                "name": "Children (aged 36-59 months) developmentally on track in at least 3 of the 4 following domains: literacy-numeracy, physical, social-emotional and learning",
                "indicator": "ECD_CHLD_36-59M_LMPSL",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Participation in organized learning - adjusted net enrolment rate, one year before official primary entry age",
                "indicator": "EDUNF_NERA_L1_UNDER1",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "of infants under 6 months of age who are exclusively breastfed",
                "indicator": "NT_BF_EXBF",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "of Neonatal mortality rate",
                "indicator": "CME_MRM0",
                "suffix": "Range among countries",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Nurturing care for early childhood development",
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
                "EDU_SDG_FREE_EDU_L02",
                "EDU_SDG_COMP_EDU_L02",
                "EDU_FIN_EXP_PT_GDP",
                "EDU_FIN_EXP_PT_TOT",
                "EDU_FIN_INIT_GOV_L02_GDP",
                "EDUNF_GER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NARA_L1_UNDER1",
                "EDUNF_GER_GPI_L01",
                "EDUNF_GECER_L01",
                "EDUNF_GECER_L02",
                "EDU_ECEC_PART",
                "EDU_SE_GPI_PTNPRE",
                "ECD_CHLD_36-59M_EDU-PGM",
                "ECD_CHLD_36-59M_ADLT_SRC",
                "ECD_CHLD_36-59M_LMPSL",
                "ECD_CHLD_U5_BKS-HM",
                "ECD_CHLD_U5_PLYTH-HM",
                "ECD_CHLD_36-59M_FHR-SPT-LNG",
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "HT_SDG_PM25",
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_CHEX_PC_CD",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_GHED_PC_CD",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_SH_XPD_OOPC_PP_CD",
                "IM_DTP3",
                "IM_MCV1",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
                "MNCH_MMR",
                "MNCH_PNCMOM",
                "MNCH_ANC4",
                "MNCH_PNEUCARE",
                "CME_PND",
                "CME_SBR",
                "CME_MRM0",
                # "CME_TRY0T4",
                "CME_MRY0T4",
                "CME_MRY0",
                "HT_SN_STA_OVWGTN",
                "NT_BF_EXBF",
                "NT_BF_EIBF",
                "NT_BW_LBW",
                "NT_BW_UNW",
                "NT_CF_MAD",
                "NT_ANT_WHZ_PO2",
                "NT_ANT_HAZ_NE2",
                "FT_SP_DYN_ADKL",
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "PV_SI_POV_DAY1",
                "PV_SI_POV_UMIC",
                "PV_WB_SI_POV_NAHC",
                "PV_SDG_SI_POV_NAHC",
                "PV_AROPE",
                "PV_SD_MDP_CSMP",
                "PV_SD_MDP_MUHHC",
                "PV_SI_POV_MDIM_17",
                "PV_SI_COV_CHLD",
                "PV_SI_COV_MATNL",
                "DM_BRTS",
                "DM_POP_URBN",
                "FT_WHS_PBR",
                "DM_FRATE_TOT",
                "DM_CHLD_POP",
                "DM_CHLD_POP_PT",
                "EC_HDI",
                "EC_GII",
                "EC_SP_GOV_EXP_GDP",
                "EC_SP_GOV_EXP_TOT",
                "EC_NY_GNP_ATLS_CD",
                "EC_NY_GNP_PCAP_CD",
                "EC_SI_POV_GINI",
                "EC_SL_UEM_TOTL_NE_ZS",
                "EC_SL_UEM_TOTL_ZS",
                "GN_MTNTY_LV_BNFTS",
                "GN_PTNTY_LV_BNFTS",
                "EC_EAP_RT",
                "EC_HCI_OVRL",
                "EC_MIN_WAGE",
                "DM_POP_NETM",
                "CR_UN_CHLD_RIGHTS",
                "CR_UN_CHLD_SALE",
                "CR_UN_RIGHTS_DISAB",
                "EC_TOT_PUB_EXP_GDP",
                "EC_TOT_PUB_EXP_TOT",
                "EC_FAM_PUB_EXP_GDP",
                "EC_FAM_PUB_EXP_TOT",
            ],
            "default": "CME_MRM0",
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
                    # "compare": "Age",
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
                "EDU_SDG_FREE_EDU_L02",
                "EDU_SDG_COMP_EDU_L02",
                "EDU_FIN_EXP_PT_GDP",
                "EDU_FIN_EXP_PT_TOT",
                "EDU_FIN_INIT_GOV_L02_GDP",
                "EDUNF_GER_L02",
                "EDUNF_NERA_L1_UNDER1",
                "EDUNF_NARA_L1_UNDER1",
                "EDUNF_GER_GPI_L01",
                "EDUNF_GECER_L01",
                "EDUNF_GECER_L02",
                "EDU_ECEC_PART",
                "EDU_SE_GPI_PTNPRE",
                "ECD_CHLD_36-59M_EDU-PGM",
                "ECD_CHLD_36-59M_ADLT_SRC",
                "ECD_CHLD_36-59M_LMPSL",
                "ECD_CHLD_U5_BKS-HM",
                "ECD_CHLD_U5_PLYTH-HM",
                "ECD_CHLD_36-59M_FHR-SPT-LNG",
            ],
            "default": "EDU_FIN_EXP_PT_GDP",
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
                    # "compare": "Age",
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
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_INRESIDENTIAL_RATE_B",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_VC_VOV_PHYL",
                "PT_VC_VOV_SEXL",
                "PT_VC_VOV_ROBB",
                "PT_VC_SNS_WALN",
            ],
            "default_graph": "line",
            "default": "PT_CHLD_INRESIDENTIAL_RATE_B",
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
                    # "compare": "Age",
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
                "HT_SDG_PM25",
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_CHEX_PC_CD",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_GHED_PC_CD",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_SH_XPD_OOPC_PP_CD",
                "IM_DTP3",
                "IM_MCV1",
                "HT_DIST80DTP3_P",
                "HT_COVERAGE_DTP3",
                "MNCH_MMR",
                "MNCH_PNCMOM",
                "MNCH_ANC4",
                "MNCH_PNEUCARE",
                "CME_PND",
                "CME_SBR",
                "CME_MRM0",
                # "CME_TRY0T4",
                "CME_MRY0T4",
                "CME_MRY0",
                "HT_SN_STA_OVWGTN",
                "NT_BF_EXBF",
                "NT_BF_EIBF",
                "NT_BW_LBW",
                "NT_BW_UNW",
                "NT_CF_MAD",
                "NT_ANT_WHZ_PO2",
                "NT_ANT_HAZ_NE2",
                "FT_SP_DYN_ADKL",
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
            ],
            "default_graph": "bar",
            "default": "HT_SH_XPD_CHEX_GD_ZS",
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
                    # "compare": "Age",
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
                "PV_SI_POV_UMIC",
                "PV_WB_SI_POV_NAHC",
                "PV_SDG_SI_POV_NAHC",
                "PV_AROPE",
                "PV_SD_MDP_CSMP",
                "PV_SD_MDP_MUHHC",
                "PV_SI_POV_MDIM_17",
                "PV_SI_COV_CHLD",
                "PV_SI_COV_MATNL",
            ],
            "default_graph": "bar",
            "default": "PV_SI_POV_UMIC",
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
                    # "compare": "Age",
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
                "DM_BRTS",
                "DM_POP_URBN",
                "FT_WHS_PBR",
                "DM_FRATE_TOT",
                "DM_CHLD_POP",
                "DM_CHLD_POP_PT",
                "EC_HDI",
                "EC_GII",
                "EC_SP_GOV_EXP_GDP",
                "EC_SP_GOV_EXP_TOT",
                "EC_NY_GNP_ATLS_CD",
                "EC_NY_GNP_PCAP_CD",
                "EC_SI_POV_GINI",
                "EC_SL_UEM_TOTL_NE_ZS",
                "EC_SL_UEM_TOTL_ZS",
                "GN_MTNTY_LV_BNFTS",
                "GN_PTNTY_LV_BNFTS",
                "EC_EAP_RT",
                "EC_HCI_OVRL",
                "EC_MIN_WAGE",
                "DM_POP_NETM",
                "CR_UN_CHLD_RIGHTS",
                "CR_UN_CHLD_SALE",
                "CR_UN_RIGHTS_DISAB",
                "EC_TOT_PUB_EXP_GDP",
                "EC_TOT_PUB_EXP_TOT",
                "EC_FAM_PUB_EXP_GDP",
                "EC_FAM_PUB_EXP_TOT",
            ],
            "default_graph": "bar",
            "default": "DM_CHLD_POP_PT",
        },
        # "AREA_6": {
        #     "name": "Participation",
        #     "graphs": {
        #         "bar": {
        #             "options": dict(
        #                 x="Country_name",
        #                 y="OBS_VALUE",
        #                 barmode="group",
        #                 # text="TIME_PERIOD",
        #                 text="OBS_VALUE",
        #                 hover_name="TIME_PERIOD",
        #             ),
        #             "compare": "Age",
        #         },
        #         "line": {
        #             "options": dict(
        #                 x="TIME_PERIOD",
        #                 y="OBS_VALUE",
        #                 color="Country_name",
        #                 hover_name="Country_name",
        #                 line_shape="spline",
        #                 render_mode="svg",
        #             ),
        #             "trace_options": dict(mode="lines+markers"),
        #         },
        #     },
        #     "indicators": [],
        #     "default_graph": "bar",
        #     "default": "",
        # },
    },
}

main_title = "Early Childhood Development (ECD)"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)
