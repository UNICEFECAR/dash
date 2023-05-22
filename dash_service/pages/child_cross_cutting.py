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
    geo_json_countries,
    get_base_layout,
    make_card,
    indicator_card,
    graphs_dict,
    selections,
    themes,
    aio_options,
    active_button,
    breakdown_options,
    default_compare,
    aio_area_figure,
    fig_options,
    download_data,
    update_country_selection,
)


min_max_card_suffix = "min - max values"
min_max_girls_suffix = "min - max values for girls"

page_config = {
    "ECD": {
        "NAME": "Early childhood development",
        "CARDS": [
            {
                "name": "",
                "indicator": "ECD_CHLD_36-59M_LMPSL",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CME_MRM0",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "NT_BF_EXBF",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "ECD_CHLD_36-59M_ADLT_SRC",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_NERA_L1_UNDER1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "ECD_CHLD_36-59M_LMPSL",
                "CME_MRM0",
                "NT_BF_EXBF",
                "ECD_CHLD_36-59M_ADLT_SRC",
                "EDUNF_NERA_L1_UNDER1",
            ],
            "default_graph": "bar",
            "default": "ECD_CHLD_36-59M_LMPSL",
        },
    },
    "GND": {
        "NAME": "Gender",
        "CARDS": [
            {
                "name": "",
                "indicator": "EC_GDI",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EC_GII",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SE_AGP_CPRA_L3",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "FT_SP_DYN_ADKL",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_F_20-24_MRD_U18",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "EC_GDI",
                "EC_GII",
                "EDU_SE_AGP_CPRA_L3",
                "FT_SP_DYN_ADKL",
                "PT_F_20-24_MRD_U18",
            ],
            "default_graph": "bar",
            "default": "EC_GDI",
        },
    },
    "ODA": {
        "NAME": "Adolescents",
        "CARDS": [
            {
                "name": "",
                "indicator": "FT_SP_DYN_ADKL",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_YOUTH_NEET",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_STU_L2_GLAST_MAT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_STU_L2_GLAST_REA",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "FT_SP_DYN_ADKL",
                "EDU_SDG_YOUTH_NEET",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
            ],
            "default_graph": "bar",
            "default": "FT_SP_DYN_ADKL",
        },
    },
    "ENV": {
        "NAME": "Environment and climate change",
        "CARDS": [
            {
                "name": "",
                "indicator": "CR_CCRI",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_CCRI_EXP_CESS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_CCRI_VUL_ES",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_EG_EGY_CLEAN",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SH_STA_ASAIRP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SH_HAP_ASMORT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SH_AAP_ASMORT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SDG_PM25",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "CR_CCRI",
                "CR_CCRI_EXP_CESS",
                "CR_CCRI_VUL_ES",
                "CR_EG_EGY_CLEAN",
                "CR_SH_STA_ASAIRP",
                "CR_SH_HAP_ASMORT",
                "CR_SH_AAP_ASMORT",
                "HT_SDG_PM25",
            ],
            "default_graph": "bar",
            "default": "CR_CCRI",
        },
    },
    "DCD": {
        "NAME": "Disaster, conflict and displacemnent",
        "CARDS": [
            {
                "name": "",
                "indicator": "CR_INFORM",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_VC_DSR_MTMP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_VC_DSR_DAFF",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CR_SG_DSR_LGRGSR",
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
                "indicator": "DM_ASYL_UASC",
                "suffix": "persons",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "CR_INFORM",
                "CR_VC_DSR_MTMP",
                "CR_VC_DSR_DAFF",
                "CR_SG_DSR_LGRGSR",
                "DM_ASYL_FRST",
                "DM_ASYL_UASC",
            ],
            "default_graph": "bar",
            "default": "CR_INFORM",
        },
    },
}

packed_config = {}

# register_page(
#     __name__,
#     # path_template="/transmonee/<page_slug>",
#     path="/transmonee/child-cross-cutting",
#     title="Cross-Cutting",
#     # order=7,
# )
page_prefix = "cci"
page_path = "child-cross-cutting"
domain_colour = "#ec5e24"
light_domain_colour = "##f7b9a1"
dark_domain_colour = "#5e2008"
map_colour = "Oranges"


# configure the Dash instance's layout
def layout(page_slug=None, **query_parmas):
    return html.Div(
        [
            html.Br(),
            dcc.Store(id=f"{page_prefix}-store"),
            dcc.Store(id=f"{page_prefix}-data-store"),
            dbc.Container(
                fluid=True,
                children=get_base_layout(
                    indicators=page_config,
                    main_subtitle="Cross-Cutting",
                    page_prefix=page_prefix,
                    page_path=page_path,
                    domain_colour=domain_colour,
                ),
            ),
            html.Br(),
        ],
        id="mainContainer",
    )


# callback to navigate to different domain
@callback(
    Output(f"{page_prefix}-theme", "pathname"),
    Output(f"{page_prefix}-theme", "hash"),
    [Input(f"{page_prefix}-topic-dropdown", "value")],
    prevent_initial_call=True,
)
def update_url(value):
    return f"/transmonee/{value}", ""


@callback(
    Output(f"{page_prefix}-store", "data"),
    Input(f"{page_prefix}-theme", "hash"),
    State(f"{page_prefix}-indicators", "data"),
)
def apply_selections(theme, indicator):
    return selections(theme, indicator)


@callback(
    Output(f"{page_prefix}-main_title", "children"),
    Output(f"{page_prefix}-info-tooltip", "children"),
    Output(f"{page_prefix}-themes", "children"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def show_themes(selections, indicators_dict):
    return themes(selections, indicators_dict, page_prefix)


@callback(
    Output({"type": "button_group", "index": f"{page_prefix}-AIO_AREA"}, "children"),
    Input(f"{page_prefix}-store", "data"),
    State(f"{page_prefix}-indicators", "data"),
    prevent_initial_call=True,
)
def set_aio_options(theme, indicators_dict):
    return aio_options(theme, indicators_dict, page_prefix)


@callback(
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "options"),
    Output({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    [Input({"type": f"{page_prefix}-indicator_button", "index": ALL}, "active")],
    State({"type": f"{page_prefix}-indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_fig_options(is_active_button, buttons_id):
    return fig_options(is_active_button, buttons_id, packed_config)


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
    Output(f"{page_prefix}-download-csv-info", "data"),
    Input(f"{page_prefix}-download_btn", "n_clicks"),
    State(f"{page_prefix}-data-store", "data"),
    prevent_initial_call=True,
)
def apply_download_data(n_clicks, data):
    return download_data(n_clicks, data)


@callback(
    Output(f"{page_prefix}-country-filter", "options"),
    Output(f"{page_prefix}-country-filter", "value"),
    [
        Input(f"{page_prefix}-country-group", "value"),
        Input(f"{page_prefix}-country-filter", "value"),
    ],
    prevent_initial_call=True,
)
def apply_update_country_selection(country_group, country_selection):
    return update_country_selection(country_group, country_selection)


@callback(
    [
        Output(f"{page_prefix}-collapse-years-button", "label"),
        Output({"type": "area", "index": f"{page_prefix}-AIO_AREA"}, "figure"),
        Output(f"{page_prefix}-aio_area_area_info", "children"),
        Output(f"{page_prefix}-indicator_card", "children"),
        Output(f"{page_prefix}-aio_area_data_info_rep", "children"),
        Output(f"{page_prefix}-data-hover-body", "children"),
        Output(f"{page_prefix}-aio_area_data_info_nonrep", "children"),
        Output(f"{page_prefix}-no-data-hover-body", "children"),
        Output(f"{page_prefix}-aio_area_graph_info", "children"),
        Output(f"{page_prefix}-data-store", "data"),
    ],
    [
        Input({"type": "area_breakdowns", "index": f"{page_prefix}-AIO_AREA"}, "value"),
        Input(f"{page_prefix}-year_slider", "value"),
        Input(f"{page_prefix}-country-filter", "value"),
        Input(f"{page_prefix}-country-group", "value"),
    ],
    [
        State(f"{page_prefix}-store", "data"),
        State(f"{page_prefix}-indicators", "data"),
        State({"type": "button_group", "index": f"{page_prefix}-AIO_AREA"}, "children"),
        State({"type": "area_types", "index": f"{page_prefix}-AIO_AREA"}, "value"),
    ],
    prevent_initial_call=True,
)
def apply_aio_area_figure(
    compare,
    years_slider,
    countries,
    country_group,
    selections,
    indicators_dict,
    buttons_properties,
    selected_type,
):
    return aio_area_figure(
        compare,
        years_slider,
        countries,
        country_group,
        selections,
        indicators_dict,
        buttons_properties,
        selected_type,
        page_prefix,
        packed_config,
        domain_colour,
        light_domain_colour,
        dark_domain_colour,
        map_colour,
    )
