from dash import (
    html,
    dcc,
    callback_context,
    ALL,
    Input,
    Output,
    State,
    register_page,
    callback,
)
import dash_bootstrap_components as dbc

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import textwrap

from dash_service.pages.transmonee import (
    geo_json_countries,
    get_base_layout,
    fa,
    unicef_country_prog,
    programme_country_indexes,
    countries,
    selection_index,
    years,
    countries_iso3_dict,
    get_filtered_dataset,
    df_sources,
    indicator_names,
    indicators_config,
    EMPTY_CHART,
    DEFAULT_LABELS,
    dimension_names,
    get_card_popover_body,
    colours,
)

min_max_card_suffix = "min - max values"

page_config = {
    "DEM": {
        "NAME": "Demographics",
        "CARDS": [
            {
                "name": "",
                "indicator": "DM_CHLD_POP",
                "suffix": "children",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "DM_CHLD_POP_PT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "DM_BRTS",
                "suffix": "births",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "DM_FRATE_TOT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "DM_CHLD_POP",
                "DM_CHLD_POP_PT",
                "DM_BRTS",
                "DM_FRATE_TOT",
            ],
            "default_graph": "line",
            "default": "DM_CHLD_POP",
        },
    },
    "PLE": {
        "NAME": "Political economy",
        "CARDS": [
            {
                "name": "",
                "indicator": "EC_HDI",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_TEC_GRL_GOV_EXP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_NY_GDP_PCAP_PP_CD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_NY_GNP_PCAP_CD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_SL_UEM_TOTL_ZS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_EAP_RT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "EC_HDI",
                "EC_TEC_GRL_GOV_EXP",
                "EC_NY_GDP_PCAP_PP_CD",
                "EC_NY_GNP_PCAP_CD",
                "EC_SL_UEM_TOTL_ZS",
                "EC_EAP_RT",
            ],
            "default_graph": "bar",
            "default": "EC_HDI",
        },
    },
    "MIG": {
        "NAME": "Migration and displacement",
        "CARDS": [
            {
                "name": "",
                "indicator": "DM_POP_NETM",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "DM_ASYL_FRST",
                "suffix": "persons",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "MG_INTNL_MG_CNTRY_DEST_PS",
                "suffix": "persons",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "DM_POP_NETM",
                "DM_ASYL_FRST",
                "MG_INTNL_MG_CNTRY_DEST_PS",
            ],
            "default_graph": "map",
            "default": "DM_POP_NETM",
        },
    },
    "CRG": {
        "NAME": "Child rights governance",
        "CARDS": [
            {
                "name": "",
                "indicator": "PP_SG_NHR_NOAPPLN",
                "suffix": "countries with 'D' status",
                "min_max": False,
                "data_provided": True,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        color="OBS_VALUE",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                    "trace_options": dict(width=0.8),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": ["packed_CRG"],
            "default_graph": "bar",
            "default": "packed_CRG",
        },
    },
    "SPE": {
        "NAME": "Public spending on children",
        "CARDS": [
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_PT_GDP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_GHED_GD_ZS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_SP_GOV_EXP_GDP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "EDU_FIN_EXP_PT_GDP",
                "HT_SH_XPD_GHED_GD_ZS",
                "EC_SP_GOV_EXP_GDP",
            ],
            "default_graph": "bar",
            "default": "EDU_FIN_EXP_PT_GDP",
        },
    },
    "DTA": {
        "NAME": "Data on children",
        "CARDS": [
            {
                "name": "",
                "indicator": "CR_IQ_SCI_OVRL",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_FPOS",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_REG_CENSUSN",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_CAPTY",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_NSDSFND",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_NSDSIMPL",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_NSDSFDGVT",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_NSDSFDDNR",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CR_SG_STT_NSDSFDOTHR",
                "suffix": "countries",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "CR_IQ_SCI_OVRL",
                "CR_SG_STT_FPOS",
                "CR_SG_REG_CENSUSN",
                "CR_SG_STT_CAPTY",
                "CR_SG_STT_NSDSFND",
                "CR_SG_STT_NSDSIMPL",
                "CR_SG_STT_NSDSFDGVT",
                "CR_SG_STT_NSDSFDDNR",
                "CR_SG_STT_NSDSFDOTHR",
            ],
            "default_graph": "bar",
            "default": "CR_IQ_SCI_OVRL",
        },
    },
    "REM": {
        "NAME": "Right to remedy",
        "CARDS": [
            {
                "name": "",
                "indicator": "JJ_CHLD_VICTIM_CRIME_RATE",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": {
                "bar": {
                    "options": dict(
                        x="Country_name",
                        y="OBS_VALUE",
                        barmode="group",
                        text="OBS_VALUE",
                        hover_name="TIME_PERIOD",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        height=500,
                    ),
                    "layout_options": dict(
                        xaxis_title={"standoff": 0},
                        margin_t=30,
                        margin_b=0,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={
                            "OBS_FOOTNOTE": "Footnote",
                            "DATA_SOURCE": "Primary Source",
                        },
                        hover_data=["OBS_FOOTNOTE", "DATA_SOURCE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
                    "layout_options": dict(
                        xaxis_title={"standoff": 10},
                        margin_t=40,
                        margin_b=0,
                    ),
                },
                "map": {
                    "options": dict(
                        locations="REF_AREA",
                        featureidkey="id",
                        color="OBS_VALUE",
                        color_continuous_scale=px.colors.sequential.GnBu,
                        mapbox_style="carto-positron",
                        geojson=geo_json_countries,
                        zoom=2,
                        center={"lat": 59.5381, "lon": 32.3200},
                        opacity=0.5,
                        labels={
                            "OBS_VALUE": "Value",
                            "Country_name": "Country",
                            "TIME_PERIOD": "Year",
                            "REF_AREA": "ISO3 Code",
                            "OBS_FOOTNOTE": "Footnote",
                        },
                        hover_data={
                            "OBS_VALUE": True,
                            "REF_AREA": False,
                            "Country_name": True,
                            "TIME_PERIOD": True,
                            "OBS_FOOTNOTE": True,
                            "DATA_SOURCE": True,
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "JJ_CHLD_VICTIM_CRIME_RATE",
            ],
            "default_graph": "bar",
            "default": "JJ_CHLD_VICTIM_CRIME_RATE",
        },
    },
}

# customization of plots requested by Siraj
packed_config = {
    "packed_CRG": {
        "indicators": [
            "PP_SG_NHR_IMPLN",
            "PP_SG_NHR_INTEXSTN",
            "PP_SG_NHR_NOSTUSN",
            "PP_SG_NHR_NOAPPLN",
        ],
        "card_key": "PP_SG_NHR_NOAPPLN",
        "mapping": {
            "CODE": {
                "OBS_VALUE": {
                    "PP_SG_NHR_IMPLN": "A",
                    "PP_SG_NHR_INTEXSTN": "B",
                    "PP_SG_NHR_NOSTUSN": "C",
                    "PP_SG_NHR_NOAPPLN": "D",
                }
            },
            "Unit_name": {"Unit_name": {"Yes/No": "Status"}},
        },
        "agg": {
            "bar": "data.groupby('REF_AREA', as_index=False).agg('last')",
            "map": "data.groupby('REF_AREA', as_index=False).agg('last')",
        },
        "yaxis": ["D", "C", "B", "A"],
    }
}

register_page(
    __name__,
    path_template="/transmonee/<page_slug>",
    path="/transmonee/child-rights",
    title="Child Rights Landscape and Governance",
    # order=1,
)
page_prefix = "crg"

# configure the Dash instance's layout
def layout(page_slug=None, **query_parmas):
    return html.Div(
        [
            html.Br(),
            dcc.Store(id=f"{page_prefix}-store"),
            dbc.Container(
                fluid=True,
                children=get_base_layout(
                    indicators=page_config,
                    main_subtitle="Child Rights Landscape and Governance",
                    page_prefix=page_prefix,
                ),
            ),
            html.Br(),
        ],
        id="mainContainer",
    )


def make_card(
    name,
    suffix,
    indicator_sources,
    source_link,
    indicator_header,
    numerator_pairs,
):
    card = [
        dbc.CardBody(
            [
                html.H1(
                    indicator_header,
                    className="display-5",
                    style={
                        "textAlign": "center",
                        "color": "#1cabe2",
                    },
                ),
                html.H4(suffix, className="card-title"),
                html.P(name, className="lead"),
                html.Div(
                    fa("fas fa-info-circle"),
                    id=f"{page_prefix}-indicator_card_info",
                    style={
                        "position": "absolute",
                        "bottom": "10px",
                        "right": "10px",
                    },
                ),
            ],
            style={
                "textAlign": "center",
            },
        ),
        dbc.Popover(
            [
                dbc.PopoverHeader(
                    html.A(
                        html.P(f"Sources: {indicator_sources}"),
                        href=source_link,
                        target="_blank",
                    )
                ),
                dbc.PopoverBody(
                    dcc.Markdown(get_card_popover_body(numerator_pairs)),
                    style={
                        "height": "200px",
                        "overflowY": "auto",
                        "whiteSpace": "pre-wrap",
                    },
                ),
            ],
            id=f"{page_prefix}-hover",
            target=f"{page_prefix}-indicator_card_info",
            trigger="hover",
        ),
    ]

    return card


@callback(
    Output(f"{page_prefix}-store", "data"),
    Output(f"{page_prefix}-country_selector", "checked"),
    Output(f"{page_prefix}-collapse-years-button", "label"),
    Output(f"{page_prefix}-collapse-countries-button", "label"),
    [
        Input(f"{page_prefix}-theme", "hash"),
        Input(f"{page_prefix}-year_slider", "value"),
        Input(f"{page_prefix}-country_selector", "checked"),
        Input(f"{page_prefix}-programme-toggle", "value"),
    ],
    State(f"{page_prefix}-indicators", "data"),
)
def apply_filters(
    theme,
    years_slider,
    country_selector,
    programme_toggle,
    indicators,
):
    ctx = callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    if programme_toggle and "programme-toggle" in selected:
        countries_selected = unicef_country_prog
        country_selector = programme_country_indexes
    # Add the condition to know when the user unchecks the UNICEF country programs!
    elif not country_selector or (
        not programme_toggle and "programme-toggle" in selected
    ):
        countries_selected = countries
        # Add this to check all the items in the selection tree
        country_selector = ["0"]
    else:
        for index in country_selector:
            countries_selected.update(selection_index[index])
            if countries_selected == countries:
                # if all countries are all selected then stop
                break

    countries_selected = list(countries_selected)
    country_text = f"{len(countries_selected)} Selected"
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0] : years_slider[1] + 1]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    countries_selected_codes = [
        countries_iso3_dict[country] for country in countries_selected
    ]
    current_theme = theme[1:].upper() if theme else next(iter(indicators.keys()))
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
        count_names=countries_selected,
    )

    return (
        selections,
        country_selector,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def indicator_card(
    selections,
    name,
    numerator,
    suffix,
    absolute=False,
    average=False,
    min_max=False,
    sex_code=None,
    age_group=None,
    data_provided=None,
):
    indicators = numerator.split(",")

    # TODO: Change to use albertos config
    # lbassil: had to change this to cater for 2 dimensions set to the indicator card like age and sex
    breakdown = "TOTAL"
    # define the empty dimensions dict to be filled based on the card data filters
    dimensions = {}
    if age_group is not None:
        dimensions["AGE"] = [age_group]
    if sex_code is not None:
        dimensions["SEX"] = [sex_code]

    filtered_data = (
        get_filtered_dataset(
            indicators,
            selections["years"],
            selections["countries"],
            breakdown,
            dimensions,
            latest_data=True,
        )
        if data_provided is None
        else data_provided
    )

    df_indicator_sources = df_sources[df_sources["Code"].isin(indicators)]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    indicator_sources = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )
    source_link = (
        df_indicator_sources["Source_Link"].unique()[0]
        if len(unique_indicator_sources) > 0
        else ""
    )
    # lbassil: add this check because we are getting an exception where there is no data; i.e. no totals for all dimensions mostly age for the selected indicator
    if filtered_data.empty:
        indicator_header = "No data"
        indicator_sources = "NA"
        suffix = ""
        numerator_pairs = []
        return make_card(
            name,
            suffix,
            indicator_sources,
            source_link,
            indicator_header,
            numerator_pairs,
        )

    # select last value for each country
    indicator_values = (
        filtered_data.groupby(
            [
                "Country_name",
                "TIME_PERIOD",
            ]
        ).agg({"OBS_VALUE": "sum", "CODE": "count"})
    ).reset_index()

    numerator_pairs = (
        indicator_values[indicator_values.CODE == len(indicators)]
        .groupby("Country_name", as_index=False)
        .last()
        .set_index(["Country_name", "TIME_PERIOD"])
    )

    if "countries" in suffix.lower():
        # this is a hack to accomodate small cases (to discuss with James)
        if "FREE" in numerator or "COMP" in numerator:
            # trick to filter number of years of free education
            indicator_sum = (numerator_pairs.OBS_VALUE >= 1).to_numpy().sum()
            sources = numerator_pairs.index.tolist()
            numerator_pairs = numerator_pairs[numerator_pairs.OBS_VALUE >= 1]
        elif "status" in suffix.lower():
            # CRG D status coung
            indicator_sum = (numerator_pairs.OBS_VALUE == "D").to_numpy().sum()
            numerator_pairs = numerator_pairs[numerator_pairs.OBS_VALUE == "D"]
            sources = numerator_pairs.index.tolist()
        elif absolute:
            # trick cards data availability among group of indicators and latest time_period
            # doesn't require filtering by count == len(numors)
            numerator_pairs = indicator_values.groupby(
                "Country_name", as_index=False
            ).last()
            max_time_filter = (
                numerator_pairs.TIME_PERIOD < numerator_pairs.TIME_PERIOD.max()
            )
            numerator_pairs.drop(numerator_pairs[max_time_filter].index, inplace=True)
            numerator_pairs.set_index(["Country_name", "TIME_PERIOD"], inplace=True)
            sources = numerator_pairs.index.tolist()
            indicator_sum = len(sources)
        else:
            # trick to accomodate cards for admin exams (AND for boolean indicators)
            # filter exams according to number of indicators
            indicator_sum = (
                (numerator_pairs.OBS_VALUE == len(indicators)).to_numpy().sum()
            )
            sources = numerator_pairs.index.tolist()
            numerator_pairs = numerator_pairs[
                numerator_pairs.OBS_VALUE == len(indicators)
            ]

    else:
        indicator_sum = numerator_pairs["OBS_VALUE"].to_numpy().sum()
        sources = numerator_pairs.index.tolist()
        if average and len(sources) > 1:
            indicator_sum = indicator_sum / len(sources)

    # define indicator header text: the resultant number except for the min-max range
    if min_max and len(sources) > 1:
        min_val = numerator_pairs["OBS_VALUE"].min()
        max_val = numerator_pairs["OBS_VALUE"].max()
        # string format for cards: thousands separator and number of decimals
        min_format = (
            "{:,."
            + (
                "0"
                if np.isnan(min_val) or "." not in str(min_val)
                else (
                    "0"
                    if str(min_val)[::-1][0] == "0"
                    else str(str(min_val)[::-1].find("."))
                )
            )
            + "f}"
        )
        max_format = (
            "{:,."
            + (
                "0"
                if np.isnan(max_val) or "." not in str(max_val)
                else (
                    "0"
                    if str(max_val)[::-1][0] == "0"
                    else str(str(max_val)[::-1].find("."))
                )
            )
            + "f}"
        )
        indicator_min = min_format.format(min_val)
        indicator_max = max_format.format(max_val)
        indicator_header = f"{indicator_min} - {indicator_max}"
    else:
        # string format for cards: thousands separator and number of decimals
        sum_format = (
            "{:,."
            + (
                "0"
                if np.isnan(indicator_sum) or "." not in str(indicator_sum)
                else (
                    "0"
                    if str(indicator_sum)[::-1][0] == "0"
                    else str(str(indicator_sum)[::-1].find("."))
                )
            )
            + "f}"
        )
        indicator_header = sum_format.format(indicator_sum)

    return make_card(
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
    )


@callback(
    Output(f"{page_prefix}-main_title", "children"),
    Output(f"{page_prefix}-themes", "children"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def show_themes(selections, indicators_dict):

    title = indicators_dict[selections["theme"]].get("NAME")
    url_hash = "#{}".format((next(iter(selections.items())))[1].lower())
    # hide the buttons when only one option is available
    if len(indicators_dict.items()) == 1:
        return title, []
    buttons = [
        dbc.Button(
            value["NAME"],
            id=key,
            color=colours[num],
            className="theme mx-1",
            href=f"#{key.lower()}",
            active=url_hash == f"#{key.lower()}",
        )
        for num, (key, value) in enumerate(indicators_dict.items())
    ]
    return title, buttons


@callback(
    Output({"type": "button_group", "index": f"{page_prefix}-AIO_AREA"}, "children"),
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def set_aio_options(theme, indicators_dict):

    area = "AIO_AREA"
    area_types = []
    current_theme = theme["theme"]
    if area in indicators_dict[current_theme]:
        indicators = indicators_dict[current_theme][area].get("indicators")
        area_indicators = indicators.keys() if indicators is dict else indicators

        default_option = (
            indicators_dict[current_theme][area].get("default")
            if area in indicators_dict[current_theme]
            else ""
        )

        area_butons = [
            dbc.Button(
                indicator_names[code],
                id={"type": f"{page_prefix}-indicator_button", "index": code},
                color="info",
                className="my-1",
                active=code == default_option if default_option != "" else num == 0,
            )
            for num, code in enumerate(area_indicators)
        ]

        area_types = [
            {
                "label": name.capitalize(),
                "value": name,
            }
            for name in indicators_dict[current_theme][area].get("graphs", {}).keys()
        ]

    default_graph = (
        indicators_dict[current_theme][area].get("default_graph")
        if area in indicators_dict[current_theme]
        else ""
    )

    return area_butons, area_types, default_graph


@callback(
    Output({"type": f"{page_prefix}-indicator_button", "index": ALL}, "active"),
    Input({"type": f"{page_prefix}-indicator_button", "index": ALL}, "n_clicks"),
    State({"type": f"{page_prefix}-indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_active_button(_, buttons_id):

    # figure out which button was clicked
    ctx = callback_context
    button_code = eval(ctx.triggered[0]["prop_id"].split(".")[0])["index"]

    # return active properties accordingly
    return [button_code == id_button["index"] for id_button in buttons_id]


@callback(
    Output({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    [
        Input({"type": f"{page_prefix}-indicator_button", "index": ALL}, "active"),
        Input({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    ],
    State({"type": f"{page_prefix}-indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def breakdown_options(is_active_button, fig_type, buttons_id):

    indicator = [
        ind_code["index"]
        for ind_code, truth in zip(buttons_id, is_active_button)
        if truth
    ][0]

    # check if indicator is a packed config
    indicator = (
        indicator
        if indicator not in packed_config
        else packed_config[indicator]["card_key"]
    )

    options = [{"label": "Total", "value": "TOTAL"}]
    # lbassil: change the disaggregation to use the names of the dimensions instead of the codes
    all_breakdowns = [
        {"label": "Sex", "value": "SEX"},
        {"label": "Age", "value": "AGE"},
        {"label": "Residence", "value": "RESIDENCE"},
        {"label": "Wealth Quintile", "value": "WEALTH_QUINTILE"},
    ]
    dimensions = indicators_config.get(indicator, {}).keys()
    # disaggregate only bar charts
    if dimensions and fig_type == "bar":
        for breakdown in all_breakdowns:
            if breakdown["value"] in dimensions:
                options.append(breakdown)
    return options


@callback(
    Output({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    Input({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    [
        State({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
        State(f"{page_prefix}-indicators", "data"),
        State(f"{page_prefix}-store", "data"),
    ],
    prevent_initial_call=True,
)
def set_default_compare(compare_options, selected_type, indicators_dict, theme):

    area = "AIO_AREA"
    current_theme = theme["theme"]

    config = indicators_dict[current_theme][area]["graphs"][selected_type]
    default_compare = config.get("compare")

    return (
        "TOTAL"
        if selected_type != "bar" or default_compare is None
        else default_compare
        if default_compare in compare_options
        else compare_options[1]["value"]
        if len(compare_options) > 1
        else compare_options[0]["value"]
    )


@callback(
    [
        Output({"type": "area", "index": f"{page_prefix}-AIO_AREA"}, "figure"),
        Output(f"{page_prefix}-aio_area_area_info", "children"),
        Output(f"{page_prefix}-indicator_card", "children"),
        Output(f"{page_prefix}-aio_area_data_info", "children"),
        Output(f"{page_prefix}-no-data-hover-body", "children"),
    ],
    Input({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    [
        State(f"{page_prefix}-store", "data"),
        State(f"{page_prefix}-indicators", "data"),
        State({"type": "button_group", "index": f"{page_prefix}-AIO_AREA"}, "children"),
        State({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    ],
    prevent_initial_call=True,
)
def aio_area_figure(
    compare,
    selections,
    indicators_dict,
    buttons_properties,
    selected_type,
):

    # assumes indicator is not empty
    indicator = [
        but_prop["props"]["id"]["index"]
        for but_prop in buttons_properties
        if but_prop["props"]["active"] is True
    ][0]

    area = "AIO_AREA"
    default_graph = indicators_dict[selections["theme"]][area].get(
        "default_graph", "line"
    )

    fig_type = selected_type if selected_type else default_graph
    fig_config = indicators_dict[selections["theme"]][area]["graphs"][fig_type].copy()
    options = fig_config.get("options")
    traces = fig_config.get("trace_options")
    layout_opt = fig_config.get("layout_options")
    dimension = False if fig_type in ["line", "map"] or compare == "TOTAL" else compare
    indicator_name = str(indicator_names.get(indicator, ""))

    if indicator not in packed_config:

        # query one indicator
        data = get_filtered_dataset(
            [indicator],
            selections["years"],
            selections["countries"],
            compare,
            latest_data=False if fig_type == "line" else True,
        )

    else:

        # query packed indicators
        data = get_filtered_dataset(
            packed_config[indicator]["indicators"],
            selections["years"],
            selections["countries"],
            compare,
            latest_data=False if fig_type == "line" else True,
        )
        # map columns
        if "mapping" in packed_config[indicator]:
            for key_col in packed_config[indicator]["mapping"]:
                map_col = next(iter(packed_config[indicator]["mapping"][key_col]))
                data[map_col] = data[key_col].map(
                    packed_config[indicator]["mapping"][key_col][map_col]
                )
        if "agg" in packed_config[indicator]:
            # aggregation depends in different plot types
            if fig_type in packed_config[indicator]["agg"]:
                data = eval(packed_config[indicator]["agg"][fig_type])

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, "", [], []
    else:
        data.sort_values(
            "OBS_VALUE",
            ascending=False if data.OBS_VALUE.dtype.kind in "iufc" else True,
            inplace=True,
        )

    # indicator card
    card_key = (
        indicator
        if indicator not in packed_config
        else packed_config[indicator]["card_key"]
    )
    card_config = [
        elem
        for elem in indicators_dict[selections["theme"]]["CARDS"]
        if elem["indicator"] == card_key
    ]

    ind_card = (
        []
        if not card_config or "CARDS" not in indicators_dict[selections["theme"]]
        else indicator_card(
            selections,
            card_config[0]["name"],
            card_config[0]["indicator"],
            card_config[0]["suffix"],
            card_config[0].get("absolute"),
            card_config[0].get("average"),
            card_config[0].get("min_max"),
            card_config[0].get("sex"),
            card_config[0].get("age"),
            data if card_config[0].get("data_provided") else None,
        )
    )

    # lbassil: was UNIT_MEASURE
    name = (
        data[data["CODE"] == card_key]["Unit_name"].astype(str).unique()[0]
        if len(data[data["CODE"] == card_key]["Unit_name"].astype(str).unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == card_key]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    source = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )
    source_link = (
        df_indicator_sources["Source_Link"].unique()[0]
        if len(unique_indicator_sources) > 0
        else ""
    )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name

    # set the chart title, wrap the text when the indicator name is too long
    chart_title = textwrap.wrap(
        indicator_name,
        width=74,
    )
    chart_title = "<br>".join(chart_title)

    # set the layout to center the chart title and change its font size and color
    layout = go.Layout(
        title=chart_title,
        title_x=0.5,
        font=dict(family="Arial", size=12),
        legend=dict(x=1, y=0.5),
        xaxis={
            "categoryorder": "total descending",
            "tickangle": -45,
            "tickmode": "linear",
            "tickfont_size": 10,
        },
    )
    if layout_opt:
        layout.update(layout_opt)

    # Add this code to avoid having decimal year on the x-axis for time series charts
    if fig_type == "line":
        data.sort_values(by=["TIME_PERIOD", "Country_name"], inplace=True)
        layout["xaxis"] = dict(
            tickmode="linear",
            tick0=selections["years"][0],
            dtick=1,
            categoryorder="total ascending",
        )
        if data.OBS_VALUE.dtype.kind not in "iufc":
            layout["yaxis"] = dict(
                categoryorder="array", categoryarray=packed_config[indicator]["yaxis"]
            )

    if dimension:
        # lbassil: use the dimension name instead of the code
        dimension_name = str(dimension_names.get(dimension, ""))
        options["color"] = dimension_name

        # sort by the compare value to have the legend in the right ascending order
        data.sort_values(by=[dimension], inplace=True)

    # rename figure_type 'map': 'choropleth' (plotly express)
    if fig_type == "map":
        fig_type = "choropleth_mapbox"
        options["range_color"] = [data.OBS_VALUE.min(), data.OBS_VALUE.max()]
    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)
    if traces:
        fig.update_traces(**traces)

    # countries not reporting
    not_rep_count = np.setdiff1d(selections["count_names"], data.Country_name.unique())
    # number of countries from selection
    count_sel = len(selections["countries"])

    return (
        fig,
        [
            html.Div(
                [
                    html.P(
                        "Source: ",
                        style={
                            "display": "inline-block",
                            "textDecoration": "underline",
                            "fontWeight": "bold",
                        },
                    ),
                    html.A(
                        f" {source}",
                        href=source_link,
                        target="_blank",
                        id={
                            "type": "area_sources",
                            "index": f"{page_prefix}-AIO_AREA",
                        },
                        className="alert-link",
                    ),
                ],
            )
        ],
        ind_card,
        [
            html.Div(
                [
                    html.P(
                        "Countries without data: ",
                        style={
                            "display": "inline-block",
                            "textDecoration": "underline",
                            "fontWeight": "bold",
                        },
                    ),
                    html.P(
                        f" {len(not_rep_count)} / {count_sel}",
                        style={
                            "display": "inline-block",
                            "fontWeight": "bold",
                            "color": "#1cabe2",
                            "whiteSpace": "pre",
                        },
                    ),
                ]
            )
        ],
        dcc.Markdown(["- " + "\n- ".join(sorted(not_rep_count, key=str.lower))]),
    )
