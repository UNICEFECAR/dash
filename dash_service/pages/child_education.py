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
    fa,
    unicef_country_prog,
    countries,
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
    "ESY": {
        "NAME": "Education system",
        "CARDS": [
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_PT_GDP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_L02",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_L1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_L2",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_FIN_EXP_L3",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_FREE_EDU_L02",
                "suffix": "countries guaranteeing at least one year",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_COMP_EDU_L02",
                "suffix": "countries guaranteeing at least one year",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "EDUNF_ADMIN_L1_GLAST_MAT",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "EDUNF_ADMIN_L1_GLAST_REA",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "EDUNF_ADMIN_L2_MAT",
                "suffix": "countries",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "EDUNF_ADMIN_L2_REA",
                "suffix": "countries",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "EDU_FIN_EXP_PT_GDP",
                # taking these indicators out for the moment as they are no longer being published
                # "EDU_FIN_EXP_L02",
                # "EDU_FIN_EXP_L1",
                # "EDU_FIN_EXP_L2",
                # "EDU_FIN_EXP_L3",
                "EDU_SDG_FREE_EDU_L02",
                "EDU_SDG_COMP_EDU_L02",
                "EDUNF_ADMIN_L1_GLAST_MAT",
                "EDUNF_ADMIN_L1_GLAST_REA",
                "EDUNF_ADMIN_L2_MAT",
                "EDUNF_ADMIN_L2_REA",
            ],
            "default_graph": "bar",
            "default": "EDU_FIN_EXP_PT_GDP",
        },
    },
    "EPA": {
        "NAME": "Education access and participation",
        "CARDS": [
            {
                "name": "",
                "indicator": "EDUNF_CR_L1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_CR_L2",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_CR_L3",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_ROFST_L1_UNDER1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_ROFST_L1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_ROFST_L2",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_ROFST_L3",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_NERA_L1_UNDER1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_SCH_L1",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_SCH_L2",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_SDG_SCH_L3",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDUNF_ESL_L1",
                "suffix": "children",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "EDUNF_CR_L1",
                "EDUNF_CR_L2",
                "EDUNF_CR_L3",
                "EDUNF_ROFST_L1_UNDER1",
                "EDUNF_ROFST_L1",
                "EDUNF_ROFST_L2",
                "EDUNF_ROFST_L3",
                "EDUNF_NERA_L1_UNDER1",
                "EDU_SDG_SCH_L1",
                "EDU_SDG_SCH_L2",
                "EDU_SDG_SCH_L3",
            ],
            "default_graph": "bar",
            "default": "EDUNF_CR_L1",
        },
    },
    "EQU": {
        "NAME": "Learning quality and skills",
        "CARDS": [
            {
                "name": "",
                "indicator": "EDU_PISA_LOW_ACHIEVE_MAT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_PISA_LOW_ACHIEVE_REA",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "EDU_PISA_LOW_ACHIEVE_SCI",
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
            {
                "name": "",
                "indicator": "EDU_SDG_YOUTH_NEET",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "EDU_PISA_LOW_ACHIEVE_MAT",
                "EDU_PISA_LOW_ACHIEVE_REA",
                "EDU_PISA_LOW_ACHIEVE_SCI",
                "EDU_SDG_STU_L2_GLAST_MAT",
                "EDU_SDG_STU_L2_GLAST_REA",
                "EDU_SDG_YOUTH_NEET",
            ],
            "default_graph": "bar",
            "default": "EDU_PISA_LOW_ACHIEVE_MAT",
        },
    },
    "ELE": {
        "NAME": "Leisure and culture",
        "CARDS": [
            {
                "name": "",
                "indicator": "PP_ADOL_TVGM",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PP_ADOL_INET",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PP_ADOL_TVGM",
                "PP_ADOL_INET",
            ],
            "default_graph": "bar",
            "default": "PP_ADOL_TVGM",
        },
    },
}

packed_config = {}

# register_page(
#     __name__,
#     # path_template="/transmonee/<page_slug>",
#     path="/transmonee/child-education",
#     title="Education and Leisure",
#     # order=5,
# )
page_prefix = "edu"
page_path = "child-education"
domain_colour = "#37568f"
light_domain_colour = "#bdcbe5"
dark_domain_colour = "#1d2c49"
map_colour = "ice_r"


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
                    main_subtitle="Education, Leisure and Culture",
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
