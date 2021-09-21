import collections
import urllib

import dash_html_components as html
import pandas as pd
from mapbox import Geocoder
import requests
from io import BytesIO

mapbox_access_token = "pk.eyJ1IjoiamNyYW53ZWxsd2FyZCIsImEiOiJja2NkMW02aXcwYTl5MnFwbjdtdDB0M3oyIn0.zkIzPc4NSjLZvrY-DWrlZg"

sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv&startPeriod={}&endPeriod={}"

geocoder = Geocoder(access_token=mapbox_access_token)


def geocode_address(address):
    """Geocode iso3 country code into lat/long."""
    # Set the type of address to country in order to return the lat/long of the country Georgia and not the US State!
    # Had to change the ISO3 of Kosovo ==> need to check Kosovo ISO3 code returned by SDMX
    response = geocoder.forward(
        "KOS" if address == "XKX" else address, types=["country"]
    )
    coords = response.json()["features"][0]["center"]
    return dict(longitude=coords[0], latitude=coords[1])


codes = [
    "EDUNF_OFST_L1_UNDER1",
    "EDUNF_OFST_L1",
    "EDUNF_OFST_L2",
    "EDUNF_OFST_L3",
    "EDUNF_ROFST_L1",
    "EDUNF_ROFST_L2",
    "EDUNF_ROFST_L3",
    "EDUNF_STU_L1_TOT",
    "EDUNF_STU_L2_TOT",
    "EDUNF_STU_L3_TOT",
    "EDUNF_NER_L02",
    "EDUNF_NERA_L1_UNDER1",
    "EDUNF_NERA_L1",
    "EDUNF_NERA_L2",
    "EDUNF_NIR_L1_ENTRYAGE",
    "EDUNF_TRANRA_L2",
    "EDUNF_GER_L1",
    "EDUNF_GER_L2",
    "EDUNF_GER_L2_GEN",
    "EDUNF_GER_L2_VOC",
    "EDUNF_GER_L3",
    "EDUNF_GER_L3_GEN",
    "EDUNF_GER_L3_VOC",
    "EDU_SDG_SCH_L1",
    "EDU_SDG_SCH_L2",
    "EDU_SDG_SCH_L3",
    "EDU_CHLD_DISAB",
    "EDU_CHLD_DISAB_GENERAL",
    "EDU_CHLD_DISAB_SPECIAL",
    "WS_SCH_H-B",
    "WS_SCH_S-B",
    "WS_SCH_W-B",
    "EDUNF_CR_L1",
    "EDUNF_CR_L2",
    "EDUNF_CR_L3",
    "EDUNF_DR_L1",
    "EDUNF_DR_L2",
    "EDUNF_RPTR_L1",
    "EDUNF_RPTR_L2",
    "EDUNF_ESL_L1",
    "EDUNF_ADMIN_L1_GLAST_REA",
    "EDUNF_ADMIN_L1_GLAST_MAT",
    "EDUNF_ADMIN_L2_REA",
    "EDUNF_ADMIN_L2_MAT",
    "EDUNF_ADMIN_L1_G2OR3_REA",
    "EDUNF_ADMIN_L1_G2OR3_MAT",
    "EDU_PISA_MAT",
    "EDU_PISA_REA",
    "EDU_PISA_SCI",
    "ECD_CHLD_36-59M_LMPSL",
    "EDU_SDG_STU_L2_GLAST_MAT",
    "EDU_SDG_STU_L2_GLAST_REA",
    "EDU_SDG_STU_L1_GLAST_MAT",
    "EDU_SDG_STU_L1_G2OR3_MAT",
    "EDU_SDG_STU_L1_GLAST_REA",
    "EDU_SDG_STU_L1_G2OR3_REA",
    "EDUNF_LR_YOUTH",
    "EDUNF_LR_ADULT",
    "EDU_SDG_TRTP_L02",
    "EDU_SDG_TRTP_L1",
    "EDU_SDG_TRTP_L2",
    "EDU_SDG_TRTP_L3",
    "EDU_SDG_QUTP_L02",
    "EDU_SDG_QUTP_L1",
    "EDU_SDG_QUTP_L2",
    "EDU_SDG_QUTP_L3",
    "EDU_SDG_FREE_EDU_L02",
    "EDU_SDG_COMP_EDU_L02",
    "EDUNF_STU_L01_PUB",
    "EDUNF_STU_L02_PUB",
    "EDUNF_STU_L1_PUB",
    "EDUNF_STU_L2_PUB",
    "EDUNF_STU_L3_PUB",
    "EDUNF_STU_L01_PRV",
    "EDUNF_STU_L02_PRV",
    "EDUNF_STU_L1_PRV",
    "EDUNF_STU_L2_PRV",
    "EDUNF_STU_L3_PRV",
    "EDUNF_TEACH_L1",
    "EDUNF_TEACH_L2",
    "EDUNF_TEACH_L3",
    "EDU_FIN_EXP_PT_GDP",
    "EDU_FIN_EXP_PT_TOT",
    "EDU_FIN_EXP_L02",
    "EDU_FIN_EXP_L1",
    "EDU_FIN_EXP_L2",
    "EDU_FIN_EXP_L3",
    "EDU_FIN_EXP_L4",
    "EDU_FIN_EXP_L5T8",
    "EDUNF_PRP_L02",
    "EDUNF_PRP_L1",
    "EDUNF_PRP_L2",
    "EDUNF_PRP_L3",
    # "EDU_PISA_MAT2",
    # "EDU_PISA_REA2",
    # "EDU_PISA_SCI2",
    # "EDU_SDG_GER_L01",
    # "EDUNF_SAP_L02",
    "EDUNF_SAP_L1T3",
    # "EDUNF_SAP_L2",
    # "EDU_CHLD_DISAB_L02",
    # "EDU_CHLD_DISAB_L1",
    # "EDU_CHLD_DISAB_L2",
    # "EDU_CHLD_DISAB_L3",
    "PT_CHLD_1-14_PS-PSY-V_CGVR",
    "PT_CHLD_INRESIDENTIAL",
    "PT_CHLD_DISAB_PUBLIC",
    # "PT_CHLD_NO_PARENTAL_CARE_PUBLIC",
    # "PT_CHLD_NONPUBLIC",
    # "PT_CHLD_INRESIDENTIAL_RATE_A",
    "PT_CHLD_INRESIDENTIAL_RATE_B",
    # "PT_CHLD_NO_PARENTAL_CARE_RATE",
    "PT_CHLD_INCARE_FOSTER",
    # "PT_CHLD_INCARE_FOSTER_RATE",
    "PT_CHLD_CARED_BY_FOSTER",
    "PT_CHLD_DISAB_FOSTER",
    "PT_CHLD_CARED_BY_FOSTER_RATE",
    "PT_CHLD_CARED_GUARDIAN",
    "PT_CHLD_DISAB_CARED_GUARDIAN",
    "PT_CHLD_CARED_GUARDIAN_RATE",
    "PT_CHLD_ENTEREDFOSTER",
    "PT_CHLD_GUARDIAN",
    "PT_CHLD_LEFTRESCARE",
    # "PT_CHLD_LEFTFOSTER",
    # "PT_CHLD_GUARDIAN_LEFT",
    "PT_CHLD_ADOPTION",
    "PT_CHLD_ADOPTION_DISAB",
    # "PT_CHLD_ADOPTION_INTERCOUNTRY",
    # "PT_CHLD_ADOPTION_INTER_COUNTRY_DISAB",
    "PT_CHLD_ADOPTION_AVAILABLE",
    "PT_CHLD_ADOPTION_AVAILABLE_DISAB",
    # "PT_CHLD_ADOPTION_INTERCOUNTRY_RATE",
    "PT_CHLD_ADOPTION_RATE",
    "JJ_CHLD_CRIME",
    "JJ_CHLD_CRIMERT",
    "JJ_CHLD_DETENTION",
    "JJ_CHLD_CONVICTED",
    # "JJ_CHLD_CONVICTED_VIOLENT",
    # "JJ_CHLD_CONVICTED_PROPERTY",
    # "JJ_CHLD_CONVICTED_OTHER",
    "JJ_CHLD_SENTENCERT",
    # "JJ_CHLD_SENTENCE_PRISION",
    # "JJ_CHLD_SENTENCE_CORRECTIONAL",
    # "JJ_CHLD_SENTENCE_PROBATION",
    # "JJ_CHLD_SENTENCE_CUSTODIAL",
    # "JJ_CHLD_SENTENCE_FINANCIAL",
    # "JJ_CHLD_SENTENCE_SERVICE",
    # "JJ_CHLD_SENTENCE_LABOUR",
    # "JJ_CHLD_SENTENCE_OTHER",
    # "JJ_CHLD_PRISION",
    # "JJ_CHLD_PRETRIAL",
    # "JJ_CHLD_PRISION_ADJUDICATION",
    "JJ_CHLD_POLICE",
    "JJ_CHLD_OFFENCE",
    # "JJ_CHLD_CRIME_PERPETRATOR",
    # "JJ_CHLD_CRIME_PERSON",
    # "JJ_CHLD_CRIME_PROPERTY",
    # "JJ_CHLD_CRIME_OTHER",
    # "JJ_CHLD_ARRESTED",
    # "JJ_CHLD_VICTIM",
    # "JJ_CHLD_OFFENDER",
    "JJ_VC_PRS_UNSNT",
    "JJ_PRISIONERS",
    "JJ_PRISIONERS_RT",
    "PT_ADLT_PS_NEC",
    "PT_CHLD_5-17_LBR_ECON",
    "PT_CHLD_5-17_LBR_ECON-HC",
    "PT_CHLD_LEFTRESCARE_ADOPTED",
    "PT_CHLD_LEFTRESCARE_DIED",
    "PT_CHLD_LEFTRESCARE_INDEPENDENT",
    "PT_CHLD_LEFTRESCARE_INFAMILY",
    "PT_CHLD_LEFTRESCARE_OTHER",
    "PT_CHLD_LEFTRESCARE_RETURNED",
    "PT_CHLD_LEFTRESCARE_TRANSFERED",
    "PT_F_15-19_MRD",
    "PT_F_15-49_W-BTNG",
    "PT_F_18-29_SX-V_AGE-18",
    "PT_F_20-24_MRD_U15",
    "PT_F_20-24_MRD_U18",
    "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
    "PT_F_GE15_SX_V_PTNR_12MNTH",
    "PT_M_15-19_MRD",
    "PT_M_15-49_W-BTNG",
    "PT_M_18-29_SX-V_AGE-18",
    "PT_M_20-24_MRD_U18",
    "PT_ST_13-15_BUL_30-DYS",
    "PT_VC_PRR_PHYV",
    "PT_VC_PRR_ROBB",
    "PT_VC_PRR_SEXV",
    "PT_VC_SNS_WALN",
    "PT_VC_VOV_PHYL",
    "PT_VC_VOV_ROBB",
    "PT_VC_VOV_SEXL",
    # adding the new health and nutrition related indicators
    # indicators for health sub-topic-1
    "HT_SH_XPD_CHEX_GD_ZS",
    "HT_SH_XPD_OOPC_CH_ZS",
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
    # indicators for sub-topic-2
    "CME_MRY0T4",
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
    # indicators for sub-topic-3
    "IM_DTP3",
    "HT_SH_ACS_DTP3",
    "HT_SH_ACS_HPV",
    "HT_SH_ACS_MCV2",
    "HT_SH_ACS_PCV3",
    "IM_MCV1",
    "HT_DIST80DTP3_P",
    "HT_COVERAGE_DTP3",
    # indicators for health sub-topic-4
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
    # indicators for health sub-topic-5
    "FT_SP_DYN_ADKL",
    "MT_SDG_SUICIDE",
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
    # indicators for health sub-topic-6
    "HT_SH_HIV_INCD",
    "HVA_PMTCT_ARV_CVG",
    "HT_SH_HIV_0014",
    "HVA_EPI_LHIV_0-19",
    "HVA_EPI_LHIV_15-24",
    "HVA_EPI_INF_RT_0-14",
    "HVA_EPI_INF_RT_10-19",
    "HVA_PED_ART_NUM",
    "HVA_PED_ART_CVG",
    # indicators for health sub-topic-7
    "WS_PPL_W-SM",
    "WS_PPL_S-SM",
    "WS_PPL_H-B",
    "WS_PPS_S-OD",
    "HT_NO_BTH_SHW_FLSH",
    # Indicators of the Poverty Page
    # sub-topic 1
    "PV_SI_POV_EMP1",
    "PV_SI_POV_DAY1",
    "PV_SI_POV_UMIC",
    "PV_SDG_SI_POV_NAHC",
    "PV_WB_SI_POV_NAHC",
    "PV_AROPE",
    "PV_AROPRT",
    "PV_SD_MDP_CSMP",
    "PV_SD_MDP_MUHHC",
    "PV_SD_MDP_MUHC",
    "PV_SI_POV_MDIM",
    "PV_SI_POV_MDIM_17",
    "WS_PPL_W-B",
    "WS_PPL_S-B",
    "PV_SEV_MAT_DPRT",
    # sub-topic 2
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
    # indicators of the participation page
    "PT_CHLD_Y0T4_REG",
    "PP_SG_REG_BRTH90N",
    "PP_SG_REG_DETH75N",
    "PP_SG_NHR_IMPLN",
    "PP_SG_NHR_INTEXSTN",
    "PP_SG_NHR_NOSTUSN",
    "PP_SG_NHR_NOAPPLN",
    "JJ_CHLD_CRIME",
    "JJ_CHLD_CRIMERT",
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
    "PP_ADOL_TVGM",
    "PP_ADOL_INET",
    "PP_ADOL_ITXT",
    "PP_ADOL_WORK_PAID",
    "PP_ADOL_WORK_HOME",
    # indicators for child rights page
    "DM_CHLD_TWO_PRNT",
    "DM_FRATE_TOT",
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
    "EC_SP_GOV_EXP_GDP",
    "EC_SP_GOV_EXP_TOT",
    "EC_NY_GDP_PCAP_PP_CD",
    "EC_NY_GNP_ATLS_CD",
    "EC_NY_GNP_PCAP_CD",
    "EC_GC_DOD_TOTL_GD_ZS",
    "EC_SI_POV_GINI",
    "EC_SL_UEM_TOTL_NE_ZS",
    "EC_SL_UEM_TOTL_ZS",
    "DM_SM_POP_REFG",
    "DM_SM_POP_REFG_OR",
    "DM_ASYL_FRST",
    "DM_ASYL_UASC",
    "MG_INTNL_MG_CNTRY_DEST_PS",
    "CR_VC_DSR_MTMP",
    "CR_VC_DSR_DAFF",
    "CR_SH_STA_AIRP",
    "CR_SH_STA_ASAIRP",
    "CR_EG_EGY_CLEAN",
    "CR_EG_ACS_ELEC",
    "CR_SG_DSR_LGRGSR",
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
]

years = list(range(2010, 2021))

# define the function that will return the values of the selected countries from the dictionary
countries_dict_filter = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])

# a key:value dictionary of countries where the 'key' is the country name as displayed in the selection
# tree whereas the 'value' is the country name as returned by the sdmx list: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/codelist/UNICEF/CL_COUNTRY/1.0
countries_dict = {
    "Albania": "Albania",
    "Andorra": "Andorra",
    "Armenia": "Armenia",
    "Austria": "Austria",
    "Azerbaijan": "Azerbaijan",
    "Belarus": "Belarus",
    "Belgium": "Belgium",
    "Bosnia and Herzegovina": "Bosnia and Herzegovina",
    "Bulgaria": "Bulgaria",
    "Croatia": "Croatia",
    "Cyprus": "Cyprus",
    "Czech Republic": "Czechia",  # we have this one is different
    "Denmark": "Denmark",
    "Estonia": "Estonia",
    "Finland": "Finland",
    "France": "France",
    "Georgia": "Georgia",
    "Germany": "Germany",
    "Greece": "Greece",
    "Holy See": "Holy See",
    "Hungary": "Hungary",
    "Iceland": "Iceland",
    "Ireland": "Ireland",
    "Italy": "Italy",
    "Kazakhstan": "Kazakhstan",
    "Kosovo (UN SC resolution 1244)": "Kosovo",  # we have this one is different
    "Kyrgyzstan": "Kyrgyzstan",
    "Latvia": "Latvia",
    "Liechtenstein": "Liechtenstein",
    "Lithuania": "Lithuania",
    "Luxembourg": "Luxembourg",
    "Malta": "Malta",
    "Monaco": "Monaco",
    "Montenegro": "Montenegro",
    "Netherlands": "Netherlands",
    "North Macedonia": "North Macedonia",
    "Norway": "Norway",
    "Poland": "Poland",
    "Portugal": "Portugal",
    "Romania": "Romania",
    "Republic of Moldova": "Republic of Moldova",
    "Russian Federation": "Russian Federation",
    "San Marino": "San Marino",
    "Serbia": "Serbia",
    "Slovakia": "Slovakia",
    "Slovenia": "Slovenia",
    "Spain": "Spain",
    "Sweden": "Sweden",
    "Switzerland": "Switzerland",
    "Tajikistan": "Tajikistan",
    "Turkey": "Turkey",
    "Turkmenistan": "Turkmenistan",
    "Ukraine": "Ukraine",
    "United Kingdom": "United Kingdom",
    "Uzbekistan": "Uzbekistan",
}

# a key:value dictionary of countries where the 'key' is the country name as displayed in the selection
# tree whereas the 'value' is the country name as returned by the sdmx list: https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/codelist/UNICEF/CL_COUNTRY/1.0
countries_iso3_dict = {
    "Albania": "ALB",
    "Andorra": "AND",
    "Armenia": "ARM",
    "Austria": "AUT",
    "Azerbaijan": "AZE",
    "Belarus": "BLR",
    "Belgium": "BEL",
    "Bosnia and Herzegovina": "BIH",
    "Bulgaria": "BGR",
    "Croatia": "HRV",
    "Cyprus": "CYP",
    "Czech Republic": "CZE",
    "Denmark": "DNK",
    "Estonia": "EST",
    "Finland": "FIN",
    "France": "FRA",
    "Georgia": "GEO",
    "Germany": "DEU",
    "Greece": "GRC",
    "Holy See": "VAT",
    "Hungary": "HUN",
    "Iceland": "ISL",
    "Ireland": "IRL",
    "Italy": "ITA",
    "Kazakhstan": "KAZ",
    "Kosovo (UN SC resolution 1244)": "XKX",  # UNDP defines it as KOS
    "Kyrgyzstan": "KGZ",
    "Latvia": "LVA",
    "Liechtenstein": "LIE",
    "Lithuania": "LTU",
    "Luxembourg": "LUX",
    "Malta": "MLT",
    "Monaco": "MCO",
    "Montenegro": "MNE",
    "Netherlands": "NLD",
    "North Macedonia": "MKD",
    "Norway": "NOR",
    "Poland": "POL",
    "Portugal": "PRT",
    "Republic of Moldova": "MDA",
    "Romania": "ROU",
    "Russian Federation": "RUS",
    "San Marino": "SMR",
    "Serbia": "SRB",
    "Slovakia": "SVK",
    "Slovenia": "SVN",
    "Spain": "ESP",
    "Sweden": "SWE",
    "Switzerland": "CHE",
    "Tajikistan": "TJK",
    "Turkey": "TUR",
    "Turkmenistan": "TKM",
    "Ukraine": "UKR",
    "United Kingdom": "GBR",
    "Uzbekistan": "UZB",
}

countries = [
    "Albania",
    "Andorra",
    "Armenia",
    "Austria",
    "Azerbaijan",
    "Belarus",
    "Belgium",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Cyprus",
    "Czech Republic",  # Czechia
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Georgia",
    "Germany",
    "Greece",
    "Holy See",
    "Hungary",
    "Iceland",
    "Ireland",
    "Italy",
    "Kazakhstan",
    "Kosovo (UN SC resolution 1244)",  # Kosovo
    "Kyrgyzstan",
    "Latvia",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Monaco",
    "Montenegro",
    "Netherlands",
    "North Macedonia",
    "Norway",
    "Poland",
    "Portugal",
    "Republic of Moldova",
    "Romania",
    "Russian Federation",
    "San Marino",
    "Serbia",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "Switzerland",
    "Tajikistan",
    "Turkey",
    "Turkmenistan",
    "Ukraine",
    "United Kingdom",
    "Uzbekistan",
]

unicef_country_prog = [
    "Albania",
    "Armenia",
    "Azerbaijan",
    "Belarus",
    "Bosnia and Herzegovina",
    "Bulgaria",
    "Croatia",
    "Georgia",
    "Greece",
    "Kazakhstan",
    "Kosovo (UN SC resolution 1244)",
    "Kyrgyzstan",
    "Montenegro",
    "North Macedonia",
    "Republic of Moldova",
    "Romania",
    "Serbia",
    "Tajikistan",
    "Turkey",
    "Turkmenistan",
    "Ukraine",
    "Uzbekistan",
]

country_selections = [
    {
        "label": "Eastern Europe and Central Asia",
        "value": [
            {"label": "Caucasus", "value": ["Armenia", "Azerbaijan", "Georgia"]},
            {
                "label": "Western Balkans",
                "value": [
                    "Albania",
                    "Bosnia and Herzegovina",
                    "Croatia",
                    "Kosovo (UN SC resolution 1244)",
                    "North Macedonia",
                    "Montenegro",
                    "Serbia",
                ],
            },
            {
                "label": "Central Asia",
                "value": [
                    "Kazakhstan",
                    "Kyrgyzstan",
                    "Tajikistan",
                    "Turkmenistan",
                    "Uzbekistan",
                ],
            },
            {
                "label": "Eastern Europe",
                "value": [
                    "Bulgaria",
                    "Belarus",
                    "Republic of Moldova",
                    "Romania",
                    "Russian Federation",
                    "Turkey",
                    "Ukraine",
                ],
            },
        ],
    },
    {
        "label": "Western Europe",
        "value": [
            "Andorra",
            "Austria",
            "Belgium",
            "Cyprus",
            "Czech Republic",
            "Denmark",
            "Estonia",
            "Finland",
            "France",
            "Germany",
            "Greece",
            "Holy See",
            "Hungary",
            "Iceland",
            "Ireland",
            "Italy",
            "Latvia",
            "Liechtenstein",
            "Lithuania",
            "Luxembourg",
            "Malta",
            "Monaco",
            "Netherlands",
            "Norway",
            "Poland",
            "Portugal",
            "San Marino",
            "Slovakia",
            "Slovenia",
            "Spain",
            "Sweden",
            "Switzerland",
            "United Kingdom",
        ],
    },
    {
        "label": "By EU Engagement",
        "value": [
            {
                "label": "Central Asia",
                "value": [
                    "Kazakhstan",
                    "Kyrgyzstan",
                    "Tajikistan",
                    "Turkmenistan",
                    "Uzbekistan",
                ],
            },
            {
                "label": "Eastern Partnership",
                "value": [
                    "Armenia",
                    "Azerbaijan",
                    "Belarus",
                    "Georgia",
                    "Republic of Moldova",
                    "Ukraine",
                ],
            },
            {
                "label": "EFTA",
                "value": ["Iceland", "Liechtenstein", "Norway", "Switzerland"],
            },
            {
                "label": "EU Member States",
                "value": [
                    "Andorra",
                    "Austria",
                    "Belgium",
                    "Bulgaria",
                    "Croatia",
                    "Cyprus",
                    "Czech Republic",
                    "Denmark",
                    "Estonia",
                    "Finland",
                    "France",
                    "Germany",
                    "Greece",
                    "Hungary",
                    "Ireland",
                    "Italy",
                    "Latvia",
                    "Lithuania",
                    "Luxembourg",
                    "Malta",
                    "Netherlands",
                    "Poland",
                    "Portugal",
                    "Romania",
                    "Slovakia",
                    "Slovenia",
                    "Spain",
                    "Sweden",
                ],
            },
            {
                "label": "Other",
                "value": [
                    "Andorra",
                    "Monaco",
                    "Holy See",
                    "San Marino",
                ],
            },
            {
                "label": "Pre-accession countries",
                "value": [
                    "Albania",
                    "Bosnia and Herzegovina",
                    "Kosovo (UN SC resolution 1244)",
                    "North Macedonia",
                    "Montenegro",
                    "Serbia",
                    "Turkey",
                ],
            },
            {
                "label": "Russian Federation",
                "value": ["Russian Federation"],
            },
            {
                "label": "United Kingdom (left EU on January 31, 2020)",
                "value": ["United Kingdom"],
            },
        ],
    },
]

data_sources = {
    "CDDEM": "CountDown 2030",
    "ESTAT": "Euro Stat",
    "Helix": " Health Entrepreneurship and LIfestyle Xchange",
    "ILO": "International Labour Organization",
    "WHO": "World Health Organization",
    "Immunization Monitoring (WHO)": "World Health Organization",
    "WB": "World Bank",
    "OECD": "Organisation for Economic Co-operation and Development",
    "SDG": "Sustainable Development Goals",
    "UIS": "UNESCO Institute for Statistics",
    "UNDP": "United Nations Development Programme",
}

# create two dicts, one for display tree and one with the index of all possible selections
selection_index = collections.OrderedDict({"0": countries})
selection_tree = dict(title="Select All", key="0", children=[])
for num1, group in enumerate(country_selections):
    parent = dict(title=group["label"], key=f"0-{num1}", children=[])
    group_countries = []

    for num2, region in enumerate(group["value"]):
        child_region = dict(
            title=region["label"] if "label" in region else region,
            key=f"0-{num1}-{num2}",
            children=[],
        )
        parent.get("children").append(child_region)
        if "value" in region:
            selection_index[f"0-{num1}-{num2}"] = (
                region["value"]
                if isinstance(region["value"], list)
                else [region["value"]]
            )
            for num3, country in enumerate(region["value"]):
                child_country = dict(title=country, key=f"0-{num1}-{num2}-{num3}")
                if len(region["value"]) > 1:
                    # only create child nodes for more then one child
                    child_region.get("children").append(child_country)
                    selection_index[f"0-{num1}-{num2}-{num3}"] = [country]
                group_countries.append(country)
        else:
            selection_index[f"0-{num1}-{num2}"] = [region]
            group_countries.append(region)

    selection_index[f"0-{num1}"] = group_countries
    selection_tree.get("children").append(parent)

programme_country_indexes = [
    next(
        key
        for key, value in selection_index.items()
        if value[0] == item and len(value) == 1
    )
    for item in unicef_country_prog
]

data = pd.DataFrame()
inds = set(codes)

# column data types coerced
col_types = {
    "COVERAGE_TIME": str,
    "OBS_FOOTNOTE": str,
    "OBS_VALUE": str,
    "Frequency": str,
    "Unit multiplier": str,
    # "OBS_VALUE": str,
    "TIME_PERIOD": int,
}


# avoid a loop to query SDMX
try:
    sdmx = pd.read_csv(
        sdmx_url.format("+".join(inds), years[0], years[-1]),
        dtype=col_types,
        storage_options={"Accept-Encoding": "gzip"},
    )
except urllib.error.HTTPError as e:
    raise e


# no need to create column CODE, just rename indicator
sdmx.rename(columns={"INDICATOR": "CODE"}, inplace=True)
data = data.append(sdmx)

# Replace the list of countries by the list of dictionary countries values
# TODO: Replace to static list
data = data.merge(
    right=pd.DataFrame(
        [
            dict(country=country, **geocode_address(country))
            for country in countries_iso3_dict.values()
        ]
    ),
    left_on="REF_AREA",  # was: Geographic area
    right_on="country",
)

# check and drop non-numeric observations, eg: SDMX accepts > 95 as an OBS_VALUE
filter_non_num = pd.to_numeric(data.OBS_VALUE, errors="coerce").isnull()
if filter_non_num.any():
    not_num_code_val = data[["CODE", "OBS_VALUE"]][filter_non_num]
    f"Non-numeric observations in {not_num_code_val.CODE.unique()}\ndiscarded: {not_num_code_val.OBS_VALUE.unique()}"
    data.drop(data[filter_non_num].index, inplace=True)

# convert to numeric
data["OBS_VALUE"] = pd.to_numeric(data.OBS_VALUE)
data = data.round({"OBS_VALUE": 2})
# print(data.columns)

# TODO: calculations for children age population

indicators = data["Indicator"].unique()

# path to excel data dictionary in repo
github_url = "https://github.com/UNICEFECAR/data-etl/raw/proto_API/tmee/data_in/data_dictionary/indicator_dictionary_TM_v8.xlsx"
data_dict_content = requests.get(github_url).content
# Reading the downloaded content and turning it into a pandas dataframe and read Snapshot sheet from excel data-dictionary
snapshot_df = pd.read_excel(BytesIO(data_dict_content), sheet_name="Snapshot")
snapshot_df.dropna(subset=["Source_name"], inplace=True)
snapshot_df["Source"] = snapshot_df["Source_name"].apply(lambda x: x.split(":")[0])
# read indicators table from excel data-dictionary
df_topics_subtopics = pd.read_excel(data_dict_content, sheet_name="Indicator")
df_topics_subtopics.dropna(subset=["Issue"], inplace=True)
df_sources = pd.merge(snapshot_df, df_topics_subtopics, on=["Code"])
df_sources.rename(
    columns={
        "Name_y": "Indicator",
        "Theme": "Sector",
        "Issue": "Subtopic",
    },
    inplace=True,
)
df_sources["Source_Full"] = df_sources["Source"].apply(lambda x: data_sources[x])
df_sources = df_sources.groupby("Source")


def page_not_found(pathname):
    return html.P("No page '{}'".format(pathname))
