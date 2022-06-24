from .base_page import get_base_layout, geo_json_countries
import plotly.express as px

indicators_dict = {
    "ADOLESCENT": {
        "NAME": "Cross-Cutting Issues",
        "CARDS": [
            {
                "name": "Children at the end of lower secondary education reaching minimum proficiency in reading",
                "indicator": "EDU_SDG_STU_L2_GLAST_REA",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Children at the end of lower secondary education reaching minimum proficiency in math",
                "indicator": "EDU_SDG_STU_L2_GLAST_MAT",
                "suffix": "Percentage range among countries",
                "min_max": True,
            },
            {
                "name": "Proportion of youth aged 15-24 years not in education, employment or training",
                "indicator": "EDU_SDG_YOUTH_NEET",
                "suffix": "Range among countries",
                "min_max": True,
            },
            {
                "name": "Adolescent birth rate (ages 15-19) per 1,000 women",
                "indicator": "FT_SP_DYN_ADKL",
                "suffix": "Range among countries",
                "sex": "Female",
                "min_max": True,
            },
        ],
        "MAIN": {
            "name": "Adolescent",
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
                    "REF_AREA": "Country",
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
                "EDU_PISA_MAT",
                "EDU_PISA_REA",
                "EDU_PISA_SCI",
                "EDU_PISA_MAT2",
                "EDU_PISA_MAT3",
                "EDU_PISA_MAT4",
                "EDU_PISA_MAT5",
                "EDU_PISA_MAT6",
                "EDU_PISA_REA2",
                "EDU_PISA_REA3",
                "EDU_PISA_REA4",
                "EDU_PISA_REA5",
                "EDU_PISA_REA6",
                "ED_ANAR_L2",
                "ED_ANAR_L3",
                # "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L2_GLAST_MAT",
                # "ICT_SKILL_COPY",
                # "ICT_SKILL_CONNECT",
                # "ICT_SKILL_CREATE",
                # "ICT_SKILL_DUP",
                # "ICT_SKILL_AT",
                # "ICT_SKILL_FORM",
                # "ICT_SKILL_SOFT",
                # "ICT_SKILL_TRAN",
                # "ICT_SKILL_PROG",
                "EDUNF_OFST_L2",
                "EDUNF_OFST_L3",
                "EDU_SDG_YOUTH_NEET",
                "EDUNF_GER_L2_VOC",
                "EDUNF_GER_L3_VOC",
                "EDUNF_GER_L2_GEN",
                "EDUNF_GER_L3_GEN",
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "HT_ADOL_MT",
                "FT_SP_DYN_ADKL",
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
                "HT_ADOL_MEAL",
                "HT_ADOL_NO_EXCS",
                "HT_ADOL_VGRS_EXCS",
                "HT_ADOL_HIGH_SATS",
                "HT_ADOL_LOW_SATS",
                "HT_CDRT_SELF_HARM",
                "HT_CHLD_BODY_RGHT",
                "HT_CHLD_BODY_NO_RGHT",
                "HT_CHLD_REG_SMOK",
                "HVA_EPI_LHIV_0-19",
                "HVA_EPI_LHIV_15-24",
                "HVA_EPI_INF_RT_10-19",
                "MNCH_CSEC",
                "MNCH_SAB",
                "MNCH_PNCMOM",
                # "MT_SDG_SUICIDE",
                "HT_CHLD_DRNK",
                "HT_SH_PRV_SMOK",
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
                "JJ_CHLD_CRIME",
                "PP_SG_REG_BRTH90N",
                "PP_SG_REG_DETH75N",
                "PP_IT_USE_ii99",
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
                "PP_IT_MOB_OWN",
                "DM_ADOL_POP",
                "EC_SL_UEM_TOTL_ZS",
                "EC_YOUTH_UNE_RT",
                "EC_YOUTH_INACT_RT",
                "DM_ASYL_FRST",
                "DM_ASYL_UASC",
                "EC_SL_UEM_TOTL_NE_ZS",
                "PT_CHLD_INRESIDENTIAL",
                "JJ_CHLD_POLICE",
                "JJ_PRISIONERS_RT",
            ],
            "default": "DM_ADOL_POP",
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
                "EDUNF_GER_L2_VOC",
                "EDUNF_GER_L3_VOC",
                "EDUNF_GER_L2_GEN",
                "EDUNF_GER_L3_GEN",
                "ED_ANAR_L2",
                "ED_ANAR_L3",
                "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
                "EDUNF_OFST_L2",
                "EDUNF_OFST_L3",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDU_SDG_YOUTH_NEET",
                "EDU_SDG_STU_L1_G2OR3_REA",
                "EDU_SDG_STU_L1_G2OR3_MAT",
                "EDU_SDG_STU_L1_GLAST_REA",
                "EDU_SDG_STU_L1_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_PISA_MAT",
                "EDU_PISA_REA",
                "EDU_PISA_SCI",
                "EDU_PISA_MAT2",
                "EDU_PISA_MAT3",
                "EDU_PISA_MAT4",
                "EDU_PISA_MAT5",
                "EDU_PISA_MAT6",
                "EDU_PISA_REA2",
                "EDU_PISA_REA3",
                "EDU_PISA_REA4",
                "EDU_PISA_REA5",
                "EDU_PISA_REA6",
                "EDU_PISA_SCI2",
                "EDU_PISA_SCI3",
                "EDU_PISA_SCI4",
                "EDU_PISA_SCI5",
                "EDU_PISA_SCI6",
            ],
            "default": "EDU_PISA_MAT",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
                "PT_F_20-24_MRD_U15",
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_ST_13-15_BUL_30-DYS",
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_GE15_SX_V_PTNR_12MNTH",
                "PT_ADLT_PS_NEC",
                "PT_CHLD_5-17_LBR_ECON",
                "PT_CHLD_5-17_LBR_ECON-HC",
                "PT_CHLD_ADOPTION",
                "PT_CHLD_ADOPTION_AVAILABLE",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_DISAB_PUBLIC",
                "PT_CHLD_ENTEREDFOSTER",
                "PT_CHLD_GUARDIAN",
                "PT_F_15-49_W-BTNG",
                "PT_M_15-49_W-BTNG",
                "JJ_CHLD_POLICE",
                "JJ_PRISIONERS_RT",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_ADOPTION_AVAILABLE",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "HT_ADOL_MT",
                "FT_SP_DYN_ADKL",
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
                "HT_ADOL_MEAL",
                "HT_ADOL_NO_EXCS",
                "HT_ADOL_VGRS_EXCS",
                "HT_ADOL_HIGH_SATS",
                "HT_ADOL_LOW_SATS",
                "HT_CDRT_SELF_HARM",
                "HT_SH_HIV_INCD",
                "HT_SH_PRV_SMOK",
                "HT_CHLD_BODY_RGHT",
                "HT_CHLD_BODY_NO_RGHT",
                "HT_CHLD_REG_SMOK",
                "HT_CHLD_DRNK",
                "HVA_EPI_LHIV_0-19",
                "HVA_EPI_LHIV_15-24",
                "HVA_EPI_INF_RT_10-19",
                "MNCH_CSEC",
                "MNCH_SAB",
                "MNCH_PNCMOM",
                # "MT_SDG_SUICIDE",
                "NT_BF_EIBF",
                "NT_BF_EXBF",
                "NT_CF_MAD",
                "NT_ANT_WHZ_PO2",
                "NT_ANT_HAZ_NE2",
            ],
            "default_graph": "bar",
            "default": "HT_ADOL_MT",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PV_AROPE",
                "PV_AROPRT",
                "PV_SD_MDP_MUHC",
                "PV_SEV_MAT_DPRT",
                "PV_SI_POV_EMP1",
            ],
            "default_graph": "bar",
            "default": "PV_AROPE",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "DM_ADOL_POP",
                "EC_SL_UEM_TOTL_ZS",
                "EC_YOUTH_UNE_RT",
                "EC_YOUTH_INACT_RT",
                "DM_ASYL_FRST",
                "DM_ASYL_UASC",
                "EC_SL_UEM_TOTL_NE_ZS",
            ],
            "default_graph": "bar",
            "default": "DM_ADOL_POP",
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
                        color="REF_AREA",
                        hover_name="REF_AREA",
                        line_shape="spline",
                        render_mode="svg",
                    ),
                    "trace_options": dict(mode="lines+markers"),
                },
            },
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
                "PP_ADOL_ITXT",
                "PP_ADOL_WORK_PAID",
                "PP_ADOL_WORK_HOME",
                "JJ_CHLD_CRIME",
                "PT_CHLD_Y0T4_REG",
                "PP_SG_REG_BRTH90N",
                "PP_SG_REG_DETH75N",
                "PP_IT_USE_ii99",
                "PP_SE_ADT_ACTS_ATCH",
                "PP_SE_ADT_ACTS_CPT",
                "PP_SE_ADT_ACTS_CDV",
                "PP_SE_ADT_ACTS_SSHT",
                "PP_SE_ADT_ACTS_PRGM",
                "PP_SE_ADT_ACTS_PST",
                "PP_SE_ADT_ACTS_SFWR",
                "PP_SE_ADT_ACTS_TRFF",
                "PP_SE_ADT_ACTS_CMFL",
                "PP_IT_MOB_OWN",
            ],
            "default_graph": "bar",
            "default": "PP_ADOL_TVGM",
        },
    },
}

main_title = "Adolescent"


def get_layout(**kwargs):
    kwargs["indicators"] = indicators_dict
    kwargs["main_title"] = main_title
    return get_base_layout(**kwargs)