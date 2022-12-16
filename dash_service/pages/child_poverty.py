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
    "SPS": {
        "NAME": "Social protection system",
        "CARDS": [
            {
                "name": "",
                "indicator": "PV_SI_COV_BENFTS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SI_COV_CHLD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SI_COV_DISAB",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SI_COV_MATNL",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SI_COV_VULN",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PV_SI_COV_BENFTS",
                "PV_SI_COV_CHLD",
                "PV_SI_COV_DISAB",
                "PV_SI_COV_MATNL",
                "PV_SI_COV_VULN",
            ],
            "default_graph": "bar",
            "default": "PV_SI_COV_BENFTS",
        },
    },
    "MAT": {
        "NAME": "Child poverty and material deprivation",
        "CARDS": [
            {
                "name": "",
                "indicator": "PV_SI_POV_UMIC",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SDG_SI_POV_NAHC",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_AROPE",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SD_MDP_CSMP",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SEV_MAT_DPRT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "PV_SEV_MAT_SOC_DPRT",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "PV_SI_POV_UMIC",
                "PV_SDG_SI_POV_NAHC",
                "PV_AROPE",
                "PV_SD_MDP_CSMP",
                "PV_SEV_MAT_DPRT",
                "PV_SEV_MAT_SOC_DPRT",
            ],
            "default_graph": "bar",
            "default": "PV_SI_POV_UMIC",
        },
    },
    "WSH": {
        "NAME": "Water, sanitation and hygiene",
        "CARDS": [
            {
                "name": "",
                "indicator": "WS_PPL_W-SM",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "WS_PPL_S-SM",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_NO_BTH_SHW_FLSH",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
        ],
        "AIO_AREA": {
            "graphs": graphs_dict,
            "indicators": [
                "WS_PPL_W-SM",
                "WS_PPL_S-SM",
                "HT_NO_BTH_SHW_FLSH",
            ],
            "default_graph": "bar",
            "default": "WS_PPL_W-SM",
        },
    },
}

register_page(
    __name__,
    # path_template="/transmonee/<page_slug>",
    path="/transmonee/child-poverty",
    title="Poverty and Social Protection",
    # order=3,
)
page_prefix = "pov"

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
                    main_subtitle="Poverty and Social Protection",
                    page_prefix=page_prefix,
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

    data = get_filtered_dataset(
        [indicator],
        selections["years"],
        selections["countries"],
        compare,
        latest_data=False if fig_type == "line" else True,
    )

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, "", [], [], []
    else:
        data.sort_values("OBS_VALUE", ascending=False, inplace=True)

    # indicator card
    card_config = [
        elem
        for elem in indicators_dict[selections["theme"]]["CARDS"]
        if elem["indicator"] == indicator
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
            page_prefix,
        )
    )

    # lbassil: was UNIT_MEASURE
    name = (
        data[data["CODE"] == indicator]["Unit_name"].astype(str).unique()[0]
        if len(data[data["CODE"] == indicator]["Unit_name"].astype(str).unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == indicator]
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
