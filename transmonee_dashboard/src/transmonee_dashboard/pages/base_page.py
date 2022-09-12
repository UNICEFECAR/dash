import textwrap

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_treeview_antd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash.dependencies import ALL, Input, Output, State
from scipy.stats import zscore

from ..app import app
from ..components import fa
from . import (
    countries,
    countries_iso3_dict,
    df_sources,
    dimension_names,
    get_filtered_dataset,
    indicator_names,
    indicators_config,
    programme_country_indexes,
    selection_index,
    selection_tree,
    unicef_country_prog,
    years,
    get_search_countries,
)

# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = px.colors.qualitative.Dark24

colours = [
    "primary",
    "success",
    "warning",
    "danger",
    "secondary",
    "info",
    "success",
    "danger",
]
AREA_KEYS = ["MAIN", "AREA_1", "AREA_2", "AREA_3", "AREA_4", "AREA_5", "AREA_6"]
DEFAULT_LABELS = {
    "Country_name": "Country",
    "TIME_PERIOD": "Year",
    "Sex_name": "Sex",
    "Residence_name": "Residence",
    "Age_name": "Age",
    "Wealth_name": "Wealth Quintile",
}
CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}

EMPTY_CHART = {
    "layout": {
        "xaxis": {"visible": False},
        "yaxis": {"visible": False},
        "annotations": [
            {
                "text": "No data is available for the selected filters",
                "xref": "paper",
                "yref": "paper",
                "showarrow": False,
                "font": {"size": 28},
            }
        ],
    }
}


def get_base_layout(**kwargs):
    indicators_dict = kwargs.get("indicators")
    main_title = kwargs.get("main_title")
    is_country_profile = kwargs.get("is_country_profile")
    country_dropdown_style = {"display": "none"}
    themes_row_style = {"verticalAlign": "center", "display": "flex"}
    countries_filter_style = {"display": "block"}
    programme_toggle_style = {"display": "block"}
    main_area_style = {"display": "block"}

    if is_country_profile:
        country_dropdown_style = {
            "minWidth": 400,
            "maxWidth": 600,
            "paddingRight": 4,
            "verticalAlign": "center",
            "display": "visible",
        }
        themes_row_style = {"display": "none"}
        countries_filter_style = {"display": "none"}
        programme_toggle_style = {"display": "none"}
        main_area_style = {"display": "none"}

    return html.Div(
        [
            dcc.Store(id="indicators", data=indicators_dict),
            dcc.Location(id="theme"),
            html.Div(
                className="heading",
                style={"padding": 36},
                children=[
                    html.Div(
                        className="heading-content",
                        children=[
                            html.Div(
                                className="heading-panel",
                                style={"padding": 20},
                                children=[
                                    html.H1(
                                        main_title,
                                        id="main_title",
                                        className="heading-title",
                                    ),
                                    html.P(
                                        id="subtitle",
                                        className="heading-subtitle",
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            dbc.Row(
                children=[
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.ButtonGroup(
                                        id="themes",
                                    ),
                                ],
                                id="theme-row",
                                # width=4,
                                className="my-2",
                                # no_gutters=True,
                                justify="center",
                                style=themes_row_style,
                            ),
                            dbc.Row(
                                [
                                    dbc.DropdownMenu(
                                        label=f"Years: {years[0]} - {years[-1]}",
                                        id="collapse-years-button",
                                        className="m-2",
                                        color="info",
                                        # block=True,
                                        children=[
                                            dbc.Card(
                                                dcc.RangeSlider(
                                                    id="year_slider",
                                                    min=0,
                                                    max=len(years) - 1,
                                                    step=None,
                                                    marks={
                                                        index: str(year)
                                                        for index, year in enumerate(
                                                            years
                                                        )
                                                    },
                                                    value=[0, len(years) - 1],
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                    "minWidth": "500px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                    dcc.Dropdown(
                                        id="country_profile_selector",
                                        options=get_search_countries(False),
                                        value="ALB",
                                        multi=False,
                                        placeholder="Select a country...",
                                        className="m-2",
                                        style=country_dropdown_style,
                                    ),
                                    dbc.DropdownMenu(
                                        label=f"Countries: {len(countries)}",
                                        id="collapse-countries-button",
                                        className="m-2",
                                        color="info",
                                        style=countries_filter_style,
                                        children=[
                                            dbc.Card(
                                                dash_treeview_antd.TreeView(
                                                    id="country_selector",
                                                    multiple=True,
                                                    checkable=True,
                                                    checked=["0"],
                                                    # selected=[],
                                                    expanded=["0"],
                                                    data=selection_tree,
                                                ),
                                                style={
                                                    "maxHeight": "250px",
                                                    # "maxWidth": "300px",
                                                },
                                                className="overflow-auto",
                                                body=True,
                                            ),
                                        ],
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                dbc.Checkbox(
                                                    id="programme-toggle",
                                                    className="custom-control-input",
                                                )
                                            ),
                                            dbc.Col(
                                                dbc.Label(
                                                    "UNICEF Country Programmes",
                                                    html_for="programme-toggle",
                                                    className="custom-control-label",
                                                    color="primary",
                                                )
                                            ),
                                        ],
                                        className="custom-control custom-switch m-2",
                                        # check=True,
                                        # inline=True,
                                        style=programme_toggle_style,
                                    ),
                                ],
                                id="filter-row",
                                # no_gutters=True,
                                justify="center",
                            ),
                        ]
                    ),
                ],
                # sticky="top",
                className="sticky-top bg-light",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        id="cards_row",
                        className="mt-3",
                    ),
                ],
                justify="center",
            ),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader(
                                id={"type": "area_title", "index": "AIO_AREA"},
                                style={"fontWeight": "bold"},
                            ),
                            dbc.CardBody(
                                [
                                    dbc.Container(
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    html.Div(
                                                        [
                                                            dbc.ButtonGroup(
                                                                id={
                                                                    "type": "button_group",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                vertical=True,
                                                                style={
                                                                    "marginBottom": "20px"
                                                                },
                                                            ),
                                                            html.Br(),
                                                            dbc.Card(
                                                                id="indicator_card",
                                                                color="primary",
                                                                outline=True,
                                                            ),
                                                        ],
                                                    ),
                                                    width=4,
                                                ),
                                                dbc.Col(
                                                    html.Div(
                                                        [
                                                            dbc.Checklist(
                                                                options=[
                                                                    {
                                                                        "label": "Show historical data",
                                                                        "value": 1,
                                                                    }
                                                                ],
                                                                value=[],
                                                                id={
                                                                    "type": "historical_data_toggle",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                switch=True,
                                                                style={
                                                                    "display": "none"
                                                                },
                                                            ),
                                                            html.Br(),
                                                            dbc.RadioItems(
                                                                id={
                                                                    "type": "area_types",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                inline=True,
                                                            ),
                                                            dcc.Loading(
                                                                [
                                                                    dcc.Graph(
                                                                        id={
                                                                            "type": "area",
                                                                            "index": "AIO_AREA",
                                                                        }
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Checklist(
                                                                options=[
                                                                    {
                                                                        "label": "Exclude outliers ",
                                                                        "value": 1,
                                                                    }
                                                                ],
                                                                value=[1],
                                                                id={
                                                                    "type": "exclude_outliers_toggle",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                switch=True,
                                                                style={
                                                                    "paddingLeft": 20,
                                                                    "display": "block",
                                                                },
                                                            ),
                                                            html.Br(),
                                                            dbc.RadioItems(
                                                                id={
                                                                    "type": "area_breakdowns",
                                                                    "index": "AIO_AREA",
                                                                },
                                                                inline=True,
                                                                style={
                                                                    "display": "block"
                                                                },
                                                            ),
                                                            html.Div(
                                                                fa(
                                                                    "fas fa-info-circle"
                                                                ),
                                                                id="aio_area_area_info",
                                                                className="float-right",
                                                            ),
                                                            dbc.Popover(
                                                                [
                                                                    dbc.PopoverHeader(
                                                                        "Sources"
                                                                    ),
                                                                    dbc.PopoverBody(
                                                                        id={
                                                                            "type": "area_sources",
                                                                            "index": "AIO_AREA",
                                                                        }
                                                                    ),
                                                                ],
                                                                id="hover",
                                                                target="aio_area_area_info",
                                                                trigger="hover",
                                                            ),
                                                        ],
                                                    ),
                                                    width=8,
                                                ),
                                            ],
                                            justify="evenly",
                                            align="start",
                                        ),
                                        fluid=True,
                                    ),
                                ]
                            ),
                        ],
                        id={"type": "area_parent", "index": "AIO_AREA"},
                    )
                )
            ),
            html.Br(),
        ],
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
                    className="display-4",
                    style={
                        # "fontSize": 50,
                        "textAlign": "center",
                        "color": "#1cabe2",
                    },
                ),
                html.H4(suffix, className="card-title"),
                html.P(name, className="lead"),
                html.Div(
                    fa("fas fa-info-circle"),
                    id="indicator_card_info",
                    # className="float-right",
                    style={
                        "position": "absolute",
                        "bottom": "10px",
                        "right": "10px",
                    },
                ),
            ],
            style={
                # "fontSize": 50,
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
    countries = []
    # lbassil: added this condition to stop the exception when sources is empty
    if len(sources) > 0:
        for index, source_info in sources.sort_values(by="OBS_VALUE").iterrows():
            countries.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
        card_countries = "\n".join(countries)
        return card_countries
    else:
        return "NA"


# TODO: Move to client side call back
@app.callback(
    Output("collapse-years", "is_open"),
    Output("collapse-countries", "is_open"),
    Output("collapse-engagements", "is_open"),
    [
        Input("collapse-years-button", "n_clicks"),
        Input("collapse-countries-button", "n_clicks"),
        Input("collapse-engagements-button", "n_clicks"),
    ],
    [
        State("collapse-years-button", "is_open"),
        State("collapse-countries-button", "is_open"),
        State("collapse-engagements-button", "is_open"),
    ],
)
def toggle_collapse(n1, n2, n3, is_open1, is_open2, is_open3):
    ctx = dash.callback_context

    if not ctx.triggered:
        return False, False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "collapse-years-button" and n1:
        return not is_open1, False, False
    elif button_id == "collapse-countries-button" and n2:
        return False, not is_open2, False
    elif button_id == "collapse-engagements-button" and n3:
        return False, False, not is_open3
    return False, False, False


@app.callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    Output("programme-toggle", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
        Input("programme-toggle", "checked"),
        Input("country_profile_selector", "value"),
    ],
    State("indicators", "data"),
)
def apply_filters(
    theme,
    years_slider,
    country_selector,
    programme_toggle,
    selected_country,
    indicators,
):
    ctx = dash.callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    current_theme = theme[1:].upper() if theme else next(iter(indicators.keys()))
    # check if it is the country profile page
    is_country_profile = current_theme == "COUNTRYPROFILE"
    # check if the user clicked on the generate button in the country profile page
    if is_country_profile:
        key_list = list(countries_iso3_dict.keys())
        val_list = list(countries_iso3_dict.values())
        # get the name of the selected country in the dropdown to filter the data accordingly
        countries_selected = (
            [key_list[val_list.index(selected_country)]] if selected_country else []
        )
    elif programme_toggle and selected == "programme-toggle":
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
    # selected_years = years[slice(*years_slider)]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    countries_selected_codes = [
        countries_iso3_dict[country] for country in countries_selected
    ]
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
        is_adolescent=("ADOLESCENT" in indicators),
    )

    return (
        selections,
        country_selector,
        countries_selected == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def indicator_card(
    selections,
    name,
    numerator,
    suffix,
    denominator=None,
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
        indicator_min = "{:,.1f}".format(numerator_pairs["OBS_VALUE"].min())
        indicator_max = "{:,.1f}".format(numerator_pairs["OBS_VALUE"].max())
        indicator_header = f"[{indicator_min} - {indicator_max}]"
    else:
        indicator_header = "{:,.0f}".format(indicator_sum)

    return make_card(
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
    )


@app.callback(
    Output({"type": "area_title", "index": "AIO_AREA"}, "children"),
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

    name = (
        indicators_dict[theme][area].get("name")
        if area in indicators_dict[theme]
        else ""
    )

    default_graph = (
        indicators_dict[theme][area].get("default_graph")
        if area in indicators_dict[theme]
        else ""
    )

    return name, area_butons, area_types, default_graph


@app.callback(
    Output({"type": "indicator_button", "index": ALL}, "active"),
    Input({"type": "indicator_button", "index": ALL}, "n_clicks"),
    State({"type": "indicator_button", "index": ALL}, "id"),
    prevent_initial_call=True,
)
def set_active_button(n_clicks, buttons_id):

    # figure out which button was clicked
    ctx = dash.callback_context
    button_code = eval(ctx.triggered[0]["prop_id"].split(".")[0])["index"]

    # return active properties accordingly
    return [button_code == id_button["index"] for id_button in buttons_id]


@app.callback(
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


@app.callback(
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


@app.callback(
    [
        Output({"type": "area", "index": "AIO_AREA"}, "figure"),
        Output({"type": "area_sources", "index": "AIO_AREA"}, "children"),
        Output("indicator_card", "children"),
    ],
    [
        Input("store", "data"),
        Input({"type": "area_breakdowns", "index": "AIO_AREA"}, "value"),
        Input({"type": "exclude_outliers_toggle", "index": "AIO_AREA"}, "value"),
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
    exclude_outliers,
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
    # check if the dataframe is empty meaning no data to display as per the user's selection
    if data.empty:
        return EMPTY_CHART, ""

    # check if the exclude outliers checkbox is checked
    if exclude_outliers:
        # filter the data to the remove the outliers
        # (df < df.quantile(0.1)).any() (df > df.quantile(0.9)).any()
        data["z_scores"] = np.abs(zscore(data["OBS_VALUE"]))  # calculate z-scores of df
        # filter the data entries to remove the outliers
        data = data[(data["z_scores"] < 3) | (data["z_scores"].isnull())]

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
            card_config[0].get("denominator"),
            card_config[0].get("absolute"),
            card_config[0].get("average"),
            card_config[0].get("min_max"),
            card_config[0].get("sex"),
            card_config[0].get("age"),
        )
    )

    return fig, html.A(html.P(source), href=source_link, target="_blank"), ind_card
