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
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import textwrap

from dash_service.pages.transmonee import (
    get_filtered_dataset,
    geo_json_countries,
    get_base_layout,
    make_card,
    indicator_card,
    graphs_dict,
    filters,
    themes,
    aio_options,
    active_button,
    breakdown_options,
    default_compare,
    aio_area_figure,
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
            "graphs": graphs_dict,
            "indicators": [
                "DM_CHLD_POP",
                "DM_CHLD_POP_PT",
                "DM_BRTS",
                "DM_FRATE_TOT",
            ],
            "default_graph": "bar",
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
            "graphs": graphs_dict,
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
            "graphs": graphs_dict,
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
            "graphs": graphs_dict,
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
            "graphs": graphs_dict,
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
            "graphs": graphs_dict,
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
            "default_graph": "map",
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
            "graphs": graphs_dict,
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
    # path_template="/transmonee/<page_slug>",
    path="/transmonee/child-rights",
    title="Child Rights Landscape and Governance",
    # order=1,
)
page_prefix = "crg"
domain_colour = "#562061"
light_domain_colour = "#e7c9ed"
dark_domain_colour = "#44194d"
map_colour = "purp"

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
                    domain_colour=domain_colour,
                ),
            ),
            html.Br(),
        ],
        id="mainContainer",
    )


df = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 1, 5, 6], "c": ["x", "x", "y", "y"]})


@callback(
    Output("download-dataframe-csv", "data"),
    Input("btn_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "mydf.csv")


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
def apply_filters(theme, years_slider, country_selector, programme_toggle, indicator):
    return filters(theme, years_slider, country_selector, programme_toggle, indicator)


@callback(
    Output(f"{page_prefix}-main_title", "children"),
    Output(f"{page_prefix}-themes", "children"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def show_themes(selections, indicators_dict):
    return themes(selections, indicators_dict, page_prefix)


@callback(
    Output({"type": "button_group", "index": f"{page_prefix}-AIO_AREA"}, "children"),
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def set_aio_options(theme, indicators_dict):
    return aio_options(theme, indicators_dict, page_prefix)


@callback(
    Output({"type": f"{page_prefix}-indicator_button", "index": ALL}, "active"),
    Input({"type": f"{page_prefix}-indicator_button", "index": ALL}, "n_clicks"),
    State({"type": f"{page_prefix}-indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_active_button(_, buttons_id):
    return active_button(_, buttons_id)


@callback(
    Output({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    [
        Input({"type": f"{page_prefix}-indicator_button", "index": ALL}, "active"),
        Input({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    ],
    State({"type": f"{page_prefix}-indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_breakdown_options(is_active_button, fig_type, buttons_id):
    return breakdown_options(is_active_button, fig_type, buttons_id, packed_config)


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
    return default_compare(compare_options, selected_type, indicators_dict, theme)


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
def apply_aio_area_figure(
    compare, selections, indicators_dict, buttons_properties, selected_type
):
    return aio_area_figure(
        compare,
        selections,
        indicators_dict,
        buttons_properties,
        selected_type,
        page_prefix,
        packed_config,
        domain_colour,
        map_colour,
    )