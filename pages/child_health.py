from cProfile import label
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

import plotly.express as px
import plotly.graph_objects as go
import textwrap

from . import (
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
)

min_max_card_suffix = "min - max values"

page_config = {
    "HSM": {
        "NAME": "Health System",
        "CARDS": [
            {
                "name": "",
                "indicator": "HT_SH_XPD_CHEX_GD_ZS",
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
                "indicator": "HT_SH_XPD_GHED_GE_ZS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_GHED_PP_CD",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_SH_XPD_OOPC_CH_ZS",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "HT_INS_COV",
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
                        hover_data=["OBS_FOOTNOTE"],
                        height=500,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
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
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "HT_SH_XPD_CHEX_GD_ZS",
                "HT_SH_XPD_GHED_GD_ZS",
                "HT_SH_XPD_GHED_GE_ZS",
                "HT_SH_XPD_GHED_PP_CD",
                "HT_SH_XPD_OOPC_CH_ZS",
                "HT_INS_COV",
            ],
            "default_graph": "line",
            "default": "HT_SH_XPD_CHEX_GD_ZS",
        },
    },
    "MNH": {
        "NAME": "Maternal, newborn and child health",
        "CARDS": [
            {
                "name": "",
                "indicator": "CME_MRM0",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CME_MRY0T4",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "CME_TMY0T4",
                "suffix": "number of deaths",
                "min_max": False,
            },
            {
                "name": "",
                "indicator": "CME_SBR",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "MNCH_SAB",
                "suffix": min_max_card_suffix,
                "min_max": True,
            },
            {
                "name": "",
                "indicator": "MNCH_CSEC",
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
                        hover_data=["OBS_FOOTNOTE"],
                        height=500,
                    ),
                },
                "line": {
                    "options": dict(
                        x="TIME_PERIOD",
                        y="OBS_VALUE",
                        color="Country_name",
                        hover_name="Country_name",
                        labels={"OBS_FOOTNOTE": "Footnote"},
                        hover_data=["OBS_FOOTNOTE"],
                        line_shape="spline",
                        render_mode="svg",
                        height=500,
                    ),
                    "trace_options": dict(mode="lines+markers"),
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
                        },
                        height=500,
                    ),
                    "layout_options": dict(margin={"r": 0, "t": 30, "l": 2, "b": 1}),
                },
            },
            "indicators": [
                "CME_MRM0",
                "CME_MRY0T4",
                "CME_TMY0T4",
                "CME_SBR",
                "MNCH_SAB",
                "MNCH_CSEC",
            ],
            "default_graph": "bar",
            "default": "CME_MRM0",
        },
    },
}

register_page(__name__, path="/child-health", title="Health and Nutrition")

# configure the Dash instance's layout
layout = html.Div(
    [
        html.Br(),
        dcc.Store(id="store"),
        dbc.Container(
            fluid=True,
            children=get_base_layout(
                indicators=page_config, main_subtitle="Health and Nutrition"
            ),
        ),
        html.Button(
            id="btnScroll",
            title="Scroll to top",
            className="btn btn-dark scroll-top",
            children=[
                fa("fas fa-chevron-up"),
            ],
            style={
                "position": "fixed",
                "right": 20,
                "bottom": 20,
                "width": 50,
                "height": 50,
                "padding": 12,
                "border": 0,
                "display": "none",
            },
        ),
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
                    id="indicator_card_info",
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
                dbc.PopoverBody(dcc.Markdown(get_card_popover_body(numerator_pairs))),
            ],
            id="hover",
            target="indicator_card_info",
            trigger="hover",
        ),
    ]

    return card


def get_card_popover_body(sources):
    """This function is used to generate the list of countries that are part of the card's
        displayed result; it displays the countries as a list, each on a separate line

    Args:
        sources (_type_): _description_

    Returns:
        _type_: _description_
    """
    country_list = []
    # lbassil: added this condition to stop the exception when sources is empty
    if len(sources) > 0:
        for index, source_info in sources.sort_values(by="OBS_VALUE").iterrows():
            country_list.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
        card_countries = "\n".join(country_list)
        return card_countries
    else:
        return "NA"


@callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
        Input("programme-toggle", "value"),
    ],
    State("indicators", "data"),
)
def apply_filters(
    years_slider,
    country_selector,
    programme_toggle,
    indicators,
):
    ctx = callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    if programme_toggle and selected == "programme-toggle":
        countries_selected = unicef_country_prog
        country_selector = programme_country_indexes
    # Add the condition to know when the user unchecks the UNICEF country programs!
    elif not country_selector or (
        not programme_toggle and selected == "programme-toggle"
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
    current_theme = [*indicators][0]
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
    )

    return (
        selections,
        country_selector,
        # countries_selected == unicef_country_prog,
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

    filtered_data = get_filtered_dataset(
        indicators,
        selections["years"],
        selections["countries"],
        breakdown,
        dimensions,
        latest_data=True,
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

    if suffix.lower() == "countries":
        # this is a hack to accomodate small cases (to discuss with James)
        if "FREE" in numerator:
            # trick to filter number of years of free education
            indicator_sum = (numerator_pairs.OBS_VALUE >= 1).to_numpy().sum()
            sources = numerator_pairs.index.tolist()
            numerator_pairs = numerator_pairs[numerator_pairs.OBS_VALUE >= 1]
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
        # use string general format
        indicator_min = "{:g}".format(numerator_pairs["OBS_VALUE"].min())
        indicator_max = "{:g}".format(numerator_pairs["OBS_VALUE"].max())
        indicator_header = f"{indicator_min} - {indicator_max}"
    else:
        # use string general format
        indicator_header = "{:g}".format(indicator_sum)

    return make_card(
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
    )


@callback(
    Output({"type": "button_group", "index": "AIO_AREA"}, "children"),
    Output({"type": "area_types", "index": "AIO_AREA"}, "options"),
    Output({"type": "area_types", "index": "AIO_AREA"}, "value"),
    Input("indicators", "data"),
)
def set_aio_options(indicators_dict):

    area = "AIO_AREA"
    theme = [*indicators_dict][0]

    area_types = []
    if area in indicators_dict[theme]:
        indicators = indicators_dict[theme][area].get("indicators")
        area_indicators = indicators.keys() if indicators is dict else indicators

        default_option = (
            indicators_dict[theme][area].get("default")
            if area in indicators_dict[theme]
            else ""
        )

        area_butons = [
            dbc.Button(
                indicator_names[code],
                id={"type": "indicator_button", "index": code},
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
            for name in indicators_dict[theme][area].get("graphs", {}).keys()
        ]

    default_graph = (
        indicators_dict[theme][area].get("default_graph")
        if area in indicators_dict[theme]
        else ""
    )

    return area_butons, area_types, default_graph


@callback(
    Output({"type": "indicator_button", "index": ALL}, "active"),
    Input({"type": "indicator_button", "index": ALL}, "n_clicks"),
    State({"type": "indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_active_button(_, buttons_id):

    # figure out which button was clicked
    ctx = callback_context
    button_code = eval(ctx.triggered[0]["prop_id"].split(".")[0])["index"]

    # return active properties accordingly
    return [button_code == id_button["index"] for id_button in buttons_id]


@callback(
    Output({"type": "area_breakdowns", "index": "AIO_AREA"}, "options"),
    [
        Input({"type": "indicator_button", "index": ALL}, "active"),
        Input({"type": "area_types", "index": "AIO_AREA"}, "value"),
    ],
    State({"type": "indicator_button", "index": ALL}, "id"),
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
    Output({"type": "area_breakdowns", "index": "AIO_AREA"}, "value"),
    Input({"type": "area_breakdowns", "index": "AIO_AREA"}, "options"),
    [
        State({"type": "area_types", "index": "AIO_AREA"}, "value"),
        State("indicators", "data"),
    ],
)
def set_default_compare(compare_options, selected_type, indicators_dict):

    area = "AIO_AREA"
    theme = [*indicators_dict][0]

    config = indicators_dict[theme][area]["graphs"][selected_type]
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
        Output({"type": "area", "index": "AIO_AREA"}, "figure"),
        Output({"type": "area_sources", "index": "AIO_AREA"}, "children"),
        Output("indicator_card", "children"),
    ],
    [
        Input("store", "data"),
        Input({"type": "area_breakdowns", "index": "AIO_AREA"}, "value"),
    ],
    [
        State("indicators", "data"),
        State({"type": "button_group", "index": "AIO_AREA"}, "children"),
        State({"type": "area_types", "index": "AIO_AREA"}, "value"),
    ],
)
def aio_area_figure(
    selections,
    compare,
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
    fig_config = indicators_dict[selections["theme"]][area]["graphs"][fig_type]
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
        latest_data=False if fig_type in ["line", "map"] else True,
    ).sort_values("OBS_VALUE", ascending=False)

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
        )
    )

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, "", ind_card

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
        xaxis={"categoryorder": "total descending"},
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
    fig_type = "choropleth_mapbox" if fig_type == "map" else fig_type
    fig = getattr(px, fig_type)(data, **options)
    fig.update_layout(layout)
    if traces:
        fig.update_traces(**traces)

    return fig, html.A(html.P(source), href=source_link, target="_blank"), ind_card
