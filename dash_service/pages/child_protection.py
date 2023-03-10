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
    make_card,
    indicator_card,
    graphs_dict,
    filters,
    themes,
    aio_options,
    breakdown_options,
    active_button,
    default_compare,
    aio_area_figure,
    fig_options,
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
    "VIO": {
        "NAME": "Violence against children and women",
        "CARDS": [
            {
                "name": "",
                "indicator": "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_ADLT_PS_NEC",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_F_18-29_SX-V_AGE-18",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_ST_13-15_BUL_30-DYS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PT_CHLD_1-14_PS-PSY-V_CGVR",
                "PT_ADLT_PS_NEC",
                "PT_F_GE15_PS-SX-EM_V_PTNR_12MNTH",
                "PT_F_18-29_SX-V_AGE-18",
                "PT_ST_13-15_BUL_30-DYS",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_1-14_PS-PSY-V_CGVR",
        },
    },
    "CPC": {
        "NAME": "Children in alternative care",
        "CARDS": [
            {
                "name": "",
                "indicator": "PT_CHLD_INRESIDENTIAL",
                "suffix": "children",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "PT_CHLD_CARED_BY_FOSTER",
                "suffix": "children",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "PT_CHLD_ADOPTION",
                "suffix": "adoptions",
                "min_max": False,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PT_CHLD_INRESIDENTIAL",
                "PT_CHLD_CARED_BY_FOSTER",
                "PT_CHLD_ADOPTION",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_INRESIDENTIAL",
        },
    },
    "JUS": {
        "NAME": "Justice for children",
        "CARDS": [
            {
                "name": "",
                "indicator": "JJ_CHLD_DETENTION_RATE",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "JJ_CHLD_PRE_SENTENCE_DETENTION_RATE",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "JJ_CHLD_POST_SENTENCE_DETENTION_RATE",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "JJ_VC_PRS_UNSNT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "JJ_CHLD_DETENTION_RATE",
                "JJ_CHLD_PRE_SENTENCE_DETENTION_RATE",
                "JJ_CHLD_POST_SENTENCE_DETENTION_RATE",
                "JJ_VC_PRS_UNSNT",
            ],
            "default_graph": "bar",
            "default": "JJ_CHLD_DETENTION_RATE",
        },
    },
    "MAR": {
        "NAME": "Child marriage and other harmful practices",
        "CARDS": [
            {
                "name": "",
                "indicator": "PT_F_20-24_MRD_U18",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_M_20-24_MRD_U18",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_F_15-19_MRD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_M_15-19_MRD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PT_F_20-24_MRD_U18",
                "PT_M_20-24_MRD_U18",
                "PT_F_15-19_MRD",
                "PT_M_15-19_MRD",
            ],
            "default_graph": "bar",
            "default": "PT_F_20-24_MRD_U18",
        },
    },
    "LAB": {
        "NAME": "Child exploitation",
        "CARDS": [
            {
                "name": "",
                "indicator": "PT_CHLD_5-17_LBR_ECON-HC",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PT_CHLD_5-17_LBR_ECON",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PT_CHLD_5-17_LBR_ECON-HC",
                "PT_CHLD_5-17_LBR_ECON",
            ],
            "default_graph": "bar",
            "default": "PT_CHLD_5-17_LBR_ECON-HC",
        },
    },
}

packed_config = {}

register_page(
    __name__,
    # path_template="/transmonee/<page_slug>",
    path="/transmonee/child-protection",
    title="Family Environment and Protection",
    # order=6,
)
page_prefix = "chp"
domain_colour = "#e5ae4c"
light_domain_colour = "#f4daaf"
dark_domain_colour = "#9c6b16"
map_colour = "YlOrBr"


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
                    main_subtitle="Family Environment and Protection",
                    page_prefix=page_prefix,
                    domain_colour=domain_colour,
                ),
            ),
            html.Br(),
        ],
        id="mainContainer",
    )


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
        light_domain_colour,
        dark_domain_colour,
        map_colour,
    )
