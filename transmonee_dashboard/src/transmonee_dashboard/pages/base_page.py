import textwrap
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_treeview_antd
import numpy as np
from scipy.stats import zscore
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash.dependencies import Input, Output, State, ClientsideFunction, MATCH, ALL
import textwrap

from . import (
    mapbox_access_token,
    unicef_country_prog,
    programme_country_indexes,
    selection_index,
    selection_tree,
    countries,
    years,
    data,
    countries_dict_filter,
    countries_iso3_dict,
    gender_indicators,
    adolescent_age_groups,
    adolescent_codes,
    geo_json_countries,
    df_sources,
)
from ..app import app, cache
from ..components import fa

# set defaults
pio.templates.default = "plotly_white"
px.defaults.color_continuous_scale = px.colors.sequential.BuGn
px.defaults.color_discrete_sequence = [
    "#1cabe2",
    "#80bd41",
    "#dda63a",
    "#e34e09",
    "#c5effc",
]
px.set_mapbox_access_token(mapbox_access_token)

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
DEFAULT_LABELS = {"Geographic area": "Country", "TIME_PERIOD": "Year"}
CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}


def make_area(area_name):
    area = dbc.Card(
        [
            dbc.CardHeader(
                id={"type": "area_title", "index": area_name},
            ),
            dbc.CardBody(
                [
                    dcc.Dropdown(
                        id={"type": "area_options", "index": area_name},
                        className="dcc_control",
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_types", "index": area_name},
                        # TODO: read chart types from config when we add more types
                        options=[
                            {"label": "Line", "value": "line"},
                            {"label": "Bar", "value": "bar"},
                        ],
                        inline=True,
                    ),
                    dcc.Graph(
                        id={"type": "area", "index": area_name},
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
                            "index": area_name,
                        },
                        switch=True,
                        style={
                            "paddingLeft": 20,
                        },
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_breakdowns", "index": area_name},
                        inline=True,
                    ),
                    html.Div(
                        fa("fas fa-info-circle"),
                        id=f"{area_name.lower()}_info",
                        className="float-right",
                    ),
                    dbc.Popover(
                        [
                            dbc.PopoverHeader("Sources"),
                            dbc.PopoverBody(
                                id={"type": "area_sources", "index": area_name},
                            ),
                        ],
                        id="hover",
                        target=f"{area_name.lower()}_info",
                        trigger="hover",
                    ),
                ]
            ),
        ],
        id={"type": "area_parent", "index": area_name},
    )
    return area


def get_base_layout(**kwargs):
    indicators_dict = kwargs.get("indicators")
    main_title = kwargs.get("main_title")

    # I changed this to correctly read the hash as you were reading the name which is different
    url_hash = (
        kwargs.get("hash")
        if kwargs.get("hash")
        else "#{}".format((next(iter(indicators_dict.items())))[0].lower())
    )
    return html.Div(
        [
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
            dcc.Store(id="indicators", data=indicators_dict),
            dcc.Location(id="theme"),
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
                                    dbc.DropdownMenu(
                                        label=f"Countries: {len(countries)}",
                                        id="collapse-countries-button",
                                        className="m-2",
                                        color="info",
                                        # block=True,
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
                                    dbc.FormGroup(
                                        [
                                            dbc.Checkbox(
                                                id="programme-toggle",
                                                className="custom-control-input",
                                            ),
                                            dbc.Label(
                                                "UNICEF Country Programmes",
                                                html_for="programme-toggle",
                                                className="custom-control-label",
                                                color="primary",
                                            ),
                                        ],
                                        className="custom-control custom-switch m-2",
                                        check=True,
                                        inline=True,
                                    ),
                                ],
                                id="filter-row",
                                no_gutters=True,
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
                    dbc.CardDeck(
                        id="cards_row",
                        className="mt-3",
                    ),
                ],
                justify="center",
            ),
            html.Br(),
            # start filter controls row
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Card(
                            [
                                dbc.CardHeader(
                                    id={"type": "area_title", "index": "MAIN"},
                                ),
                                dbc.CardBody(
                                    [
                                        dcc.Dropdown(
                                            id={
                                                "type": "area_options",
                                                "index": "MAIN",
                                            },
                                            style={
                                                "zIndex": "11",
                                            },
                                        ),
                                        dbc.FormGroup(
                                            [
                                                dbc.Checkbox(
                                                    id="latest-data-toggle",
                                                    className="custom-control-input",
                                                ),
                                                dbc.Label(
                                                    "Show latest year",
                                                    html_for="latest-data-toggle",
                                                    className="custom-control-label",
                                                    color="primary",
                                                ),
                                            ],
                                            className="custom-control custom-switch m-2",
                                            check=True,
                                            inline=True,
                                        ),
                                        dcc.Graph(id="main_area"),
                                        html.Div(
                                            fa("fas fa-info-circle"),
                                            id="main_area_info",
                                            className="float-right",
                                        ),
                                        dbc.Popover(
                                            [
                                                dbc.PopoverHeader("Sources"),
                                                dbc.PopoverBody(id="main_area_sources"),
                                            ],
                                            id="hover",
                                            target="main_area_info",
                                            trigger="hover",
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ),
                ],
            ),
            # end filter controls row
            html.Br(),
            dbc.CardDeck(
                [make_area(area) for area in ["AREA_1", "AREA_2"]],
            ),
            html.Br(),
            dbc.CardDeck(
                [make_area(area) for area in ["AREA_3", "AREA_4"]],
            ),
            html.Br(),
            dbc.CardDeck(
                [make_area(area) for area in ["AREA_5", "AREA_6"]],
            ),
            html.Br(),
        ],
    )


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
    Output({"type": "area_parent", "index": MATCH}, "hidden"),
    Input("theme", "hash"),
    [
        State("indicators", "data"),
        State({"type": "area_parent", "index": MATCH}, "id"),
    ],
)
def display_areas(theme, indicators_dict, id):
    area = id["index"]
    theme = theme[1:].upper() if theme else next(iter(indicators_dict.keys()))
    return area not in indicators_dict[theme]


@cache.memoize()  # will cache based on years and countries combo
def get_filtered_dataset(theme, indicators_dict, years, countries, is_adolescent):
    print("CACHE BREAK!!!")
    indicators = []
    for area in AREA_KEYS:
        if area in indicators_dict[theme]:
            indicators.extend(indicators_dict[theme][area]["indicators"])

    # add card indicators
    for card in indicators_dict[theme]["CARDS"]:
        indicators.extend(card["indicator"].split(","))

    # keep only the indicators that have gender/sex disaggregation
    if is_adolescent:
        return data[
            (data["TIME_PERIOD"].isin(years))
            & (data["REF_AREA"].isin(countries))
            & (
                (
                    data["CODE"].isin(indicators)
                    & data["CODE"].isin(adolescent_codes)
                    & data["AGE"].isin(adolescent_age_groups)
                )
                | (data["CODE"].isin(indicators) & ~data["CODE"].isin(adolescent_codes))
            )
        ]

    # Use the ref area that contains the countries ISO3 codes to filter the selected countries data
    return data[
        (data["TIME_PERIOD"].isin(years))
        & (data["REF_AREA"].isin(countries))
        & (data["CODE"].isin(indicators))
    ]


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
    ],
    [
        State("indicators", "data"),
    ],
)
def apply_filters(
    theme,
    years_slider,
    country_selector,
    programme_toggle,
    indicators,
):
    ctx = dash.callback_context
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

    country_text = f"{len(list(countries_selected))} Selected"
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0] : years_slider[1] + 1]
    # selected_years = years[slice(*years_slider)]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    countries_selected = countries_dict_filter(countries_iso3_dict, countries_selected)
    # cache the data based on selected years and countries
    selections = dict(
        theme=theme[1:].upper() if theme else next(iter(indicators.keys())),
        indicators_dict=indicators,
        years=selected_years,
        countries=list(countries_selected.values()),
        is_adolescent=("ADOLESCENT" in indicators),
    )

    get_filtered_dataset(**selections)
    return (
        selections,
        country_selector,
        # Fix the condition after using the dict of name/iso for countries
        list(countries_selected.keys()) == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
    )


def indicator_card(
    selections,
    card_id,
    name,
    numerator,
    suffix,
    denominator=None,
    absolute=False,
    sex_code="Total",
    average=False,
    min_max=False,
    age_group=None,
):

    # indicator could be a list --> great use of " in " instead of " == " !!!
    query = "CODE in @indicator"

    numors = numerator.split(",")

    # use filtered chached dataset
    filtered_data = get_filtered_dataset(**selections)

    # build the (target + rest total) query
    # target code is Total unless is not None
    sex_code = sex_code if sex_code else "Total"
    # use one of the numerators if more than one --> assume all have the same disaggregation
    # other possibility could be to generalize more get_target_query function ...
    dimension = "Age" if age_group else "Sex"
    target_code = age_group if age_group else sex_code
    target_and_total_query = get_target_query(
        filtered_data, numors[0], dimension, target_code
    )
    query = query + " & " + target_and_total_query

    # query = "CODE in @indicator & SEX in @sex_code & RESIDENCE in @total_code & WEALTH_QUINTILE in @total_code"
    indicator = numors
    df_indicator_sources = df_sources[df_sources["Code"].isin(indicator)]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    indicator_sources = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )

    df_indicator_sources = df_sources[df_sources["Code"].isin(indicator)]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    indicator_sources = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )

    # select last value for each country
    indicator_values = (
        filtered_data.query(query)
        .groupby(
            [
                "Geographic area",
                "TIME_PERIOD",
            ]
        )
        .agg({"OBS_VALUE": "sum", "CODE": "count"})
    ).reset_index()

    numerator_pairs = (
        indicator_values[indicator_values.CODE == len(numors)]
        .groupby("Geographic area", as_index=False)
        .last()
        .set_index(["Geographic area", "TIME_PERIOD"])
    )
    # check for denominator
    if denominator:
        # select the available denominators for countries in selected years
        indicator = [denominator]
        # reset the query for denominator
        query = "CODE in @indicator"

        # so far denominator is thought to be a single one right?
        # possibly --> generalize to more than one --> as numerator
        # build the query for denominator, naturally --> uses same sex_code
        target_and_total_query = get_target_query(data, denominator, "Sex", sex_code)
        query = query + " & " + target_and_total_query

        denominator_values = filtered_data.query(query).set_index(
            ["Geographic area", "TIME_PERIOD"]
        )
        # select only those denominators that match available indicators
        index_intersect = numerator_pairs.index.intersection(denominator_values.index)

        denominators = denominator_values.loc[index_intersect]["OBS_VALUE"]

        indicator_sum = (
            numerator_pairs.loc[index_intersect]["OBS_VALUE"].to_numpy().sum()
            / denominators.to_numpy().sum()
            * 100
            if absolute
            else (
                numerator_pairs["OBS_VALUE"]
                * denominators
                / denominators.to_numpy().sum()
            )
            .dropna()  # will drop missing countries
            .to_numpy()
            .sum()
        )
        sources = index_intersect.tolist()

    elif suffix.lower() == "countries":
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
                "Geographic area", as_index=False
            ).last()
            max_time_filter = (
                numerator_pairs.TIME_PERIOD < numerator_pairs.TIME_PERIOD.max()
            )
            numerator_pairs.drop(numerator_pairs[max_time_filter].index, inplace=True)
            numerator_pairs.set_index(["Geographic area", "TIME_PERIOD"], inplace=True)
            sources = numerator_pairs.index.tolist()
            indicator_sum = len(sources)
        else:
            # trick to accomodate cards for admin exams (AND for boolean indicators)
            # filter exams according to number of indicators
            indicator_sum = (numerator_pairs.OBS_VALUE == len(numors)).to_numpy().sum()
            sources = numerator_pairs.index.tolist()

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

    card = dbc.Card(
        [
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
                        id=f"{card_id}_info",
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
                    dbc.PopoverHeader(f"Sources: {indicator_sources}"),
                    dbc.PopoverBody(
                        dcc.Markdown(get_card_popover_body(numerator_pairs))
                    ),  # replace the tooltip with the desired bullet list layout),
                ],
                id="hover",
                target=f"{card_id}_info",
                trigger="hover",
            ),
        ],
        color="primary",
        outline=True,
        id=card_id,
    )
    return card


# This function is used to generate the list of countries that are part of the card's displayed result;
# it displays the countries as a list, each on a separate line...
def get_card_popover_body(sources):
    countries = []
    for index, source_info in sources.sort_values(by="OBS_VALUE").iterrows():
        countries.append(f"- {index[0]}, {source_info[0]} ({index[1]})")
    card_countries = "\n".join(countries)
    return card_countries


@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("cards_row", "children"), State("indicators", "data")],
)
def show_cards(selections, current_cards, indicators_dict):
    cards = [
        indicator_card(
            selections,
            f"card-{num}",
            card["name"],
            card["indicator"],
            card["suffix"],
            card.get("denominator"),
            card.get("absolute"),
            card.get("sex"),
            card.get("average"),
            card.get("min_max"),
            card.get("age"),
        )
        for num, card in enumerate(indicators_dict[selections["theme"]]["CARDS"])
    ]
    return cards


# Added this function to add the button group and set the correct active button
@app.callback(
    # Output("main_title", "children"),
    Output("subtitle", "children"),
    [
        Input("store", "data"),
    ],
    [State("indicators", "data")],
)
def show_header_titles(theme, indicators_dict):
    subtitle = indicators_dict[theme["theme"]].get("NAME")
    return subtitle


# Added this function to add the button group and set the correct active button,
# TODO: This can be replaced by a generic callback to set the active button on click
@app.callback(
    Output("themes", "children"),
    [
        Input("store", "data"),
    ],
    [State("themes", "children"), State("indicators", "data")],
)
def show_themes(selections, current_themes, indicators_dict):

    url_hash = "#{}".format((next(iter(selections.items())))[1].lower())
    # hide the buttons when only one options is available
    if len(indicators_dict.items()) == 1:
        return []
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
    return buttons


@app.callback(
    Output({"type": "area_options", "index": MATCH}, "options"),
    Input("store", "data"),
    [
        State("indicators", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def set_options(theme, indicators_dict, id):
    area = id["index"]
    if area in indicators_dict[theme["theme"]]:
        area_indicators = indicators_dict[theme["theme"]][area]["indicators"]
        area_options = [
            {
                "label": item["Indicator"],
                "value": item["CODE"],
            }
            for item in data[data["CODE"].isin(area_indicators)][["CODE", "Indicator"]]
            .drop_duplicates()
            .to_dict("records")
        ]
        return area_options
    return []


# TODO: the three fuctions below are similar and can be combined into one
@app.callback(
    Output({"type": "area_title", "index": MATCH}, "children"),
    Input("store", "data"),
    [
        State("indicators", "data"),
        State({"type": "area_title", "index": MATCH}, "id"),
    ],
)
def set_areas_titles(theme, indicators_dict, id):

    area = id["index"]
    return (
        indicators_dict[theme["theme"]][area].get("name")
        if area in indicators_dict[theme["theme"]]
        else ""
    )


@app.callback(
    Output({"type": "area_options", "index": MATCH}, "value"),
    Input("store", "data"),
    [
        State("indicators", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def set_default_values(theme, indicators_dict, id):

    area = id["index"]
    return (
        indicators_dict[theme["theme"]][area].get("default")
        if area in indicators_dict[theme["theme"]]
        else ""
    )


@app.callback(
    Output({"type": "area_types", "index": MATCH}, "value"),
    Input("store", "data"),
    [
        State("indicators", "data"),
        State({"type": "area_types", "index": MATCH}, "id"),
    ],
)
def set_default_chart_types(theme, indicators_dict, id):

    area = id["index"]
    return (
        indicators_dict[theme["theme"]][area].get("default_graph")
        if area in indicators_dict[theme["theme"]]
        else ""
    )


# does this function assume dimension is a disaggregation?
# should we call it only if dimension is a disaggregation?
def get_disag_total(data, indicator, dimension, default_total="Total"):

    data_disag_col = data[data["CODE"] == indicator][dimension]
    max_val_count = data_disag_col.value_counts().idxmax()

    # return max_val_count only if Total not in dimension
    return [default_total if default_total in data_disag_col.values else max_val_count]


# this could be a potential function to be decorated per indicator in each area?
# area_1 breakdown does the first part of this
def get_total_query(data, indicator, neq=False, dimension=None):

    dimensions = ["Sex", "Age", "Residence", "Wealth Quintile"]
    disag = []

    for item in dimensions:
        if len(data[data["CODE"] == indicator][item].unique()) > 1:
            disag.append(item)

    if not disag:
        return None
    elif neq:
        query_dim = " & ".join(
            f"`{dimension}` != '{total}'"
            for total in get_disag_total(data, indicator, dimension)
        )

        query_item = []
        for item in disag:
            if item != dimension:
                item_total = []
                # realized loop below could be replaced with query like:
                # f"`{item}` in @total" --> great use of this !!!
                for total in get_disag_total(data, indicator, item):
                    item_total.append(f"`{item}` == '{total}'")
                query_item.append(f"({' | '.join(item_total)})")
        query_rest = " & ".join(query_item)
        # return " & ".join(query_item)

        # query_rest = " & ".join(
        #     f"`{item}` == '{total}'"
        #     for item in disag
        #     for total in get_disag_total(data, indicator, item)
        #     if item != dimension
        # )

        return (query_dim + " & " + query_rest) if query_rest else query_dim

    else:

        query_item = []
        for item in disag:
            item_total = []
            for total in get_disag_total(data, indicator, item):
                item_total.append(f"`{item}` == '{total}'")
            query_item.append(f"({' | '.join(item_total)})")
        return " & ".join(query_item)

        # return " & ".join(
        #     f"({' | '.join([f"`{item}` == '{total}'"])})"
        #     for item in disag
        #     for total in get_disag_total(data, indicator, item)
        # )


# targets one dimension to a code and the remaining total
# assumes previous knowledge ON the EXISTANCE of the target_code for the dimension
def get_target_query(data, indicator, dimension="Sex", target_code="Total"):
    dimensions = ["Sex", "Age", "Residence", "Wealth Quintile"]
    disag = [
        item
        for item in dimensions
        if (
            (len(data[data["CODE"] == indicator][item].unique()) > 1)
            & (item != dimension)
        )
    ]
    query_dim = f"`{dimension}` == '{target_code}'"

    if not disag:
        return query_dim
    else:
        query_item = []
        for item in disag:
            item_total = []
            disag_total = get_disag_total(data, indicator, item)
            for total in disag_total:
                item_total.append(f"`{item}` == '{total}'")
            query_item.append(f"({' | '.join(item_total)})")
        return query_dim + " & " + " & ".join(query_item)


@app.callback(
    Output({"type": "area_breakdowns", "index": MATCH}, "options"),
    Input({"type": "area_options", "index": MATCH}, "value"),
    [
        State({"type": "area_breakdowns", "index": MATCH}, "id"),
    ],
)
def breakdown_options(indicator, id):

    options = [{"label": "Total", "value": "Total"}]
    all_breakdowns = [
        {"label": "Sex", "value": "Sex"},
        {"label": "Age", "value": "Age"},
        {"label": "Residence", "value": "Residence"},
        {"label": "Wealth Quintile", "value": "Wealth Quintile"},
    ]
    for item in all_breakdowns:
        if len(data[data["CODE"] == indicator][item["value"]].unique()) > 1:
            options.append(item)
    return options


@app.callback(
    Output({"type": "area_breakdowns", "index": MATCH}, "value"),
    [
        Input("store", "data"),
        Input({"type": "area_breakdowns", "index": MATCH}, "options"),
        Input({"type": "area_types", "index": MATCH}, "value"),
    ],
    [
        State("indicators", "data"),
        State({"type": "area_breakdowns", "index": MATCH}, "id"),
    ],
)
def set_default_compare(
    selections, compare_options, selected_type, indicators_dict, id
):
    area = id["index"]
    if area in indicators_dict[selections["theme"]]:
        default = indicators_dict[selections["theme"]][area]["default_graph"]
        fig_type = selected_type if selected_type else default
        config = indicators_dict[selections["theme"]][area]["graphs"][fig_type]
        default_compare = config.get("compare")

        return (
            "Total"
            if fig_type == "line" or default_compare is None
            else default_compare
            if default_compare in compare_options
            else compare_options[1]["value"]
            if len(compare_options) > 1
            else compare_options[0]["value"]
        )


@app.callback(
    Output("main_area", "figure"),
    Output("main_area_sources", "children"),
    [
        Input({"type": "area_options", "index": "MAIN"}, "value"),
        Input("latest-data-toggle", "checked"),
        Input("store", "data"),
    ],
    [
        State("indicators", "data"),
    ],
)
def main_figure(indicator, latest_data, selections, indicators_dict):

    options = indicators_dict[selections["theme"]]["MAIN"]["options"]
    # compare = "Sex"

    data = get_filtered_dataset(**selections)

    # total = "Total"  # potentially move to this config
    query = "CODE == @indicator"
    total_if_disag_query = get_total_query(data, indicator)
    query = (query + " & " + total_if_disag_query) if total_if_disag_query else query

    name = (
        data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
        if len(data[data["CODE"] == indicator]["Unit of measure"].unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == indicator]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    source = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )

    df = (
        data.query(query)
        .groupby(["CODE", "Indicator", "REF_AREA", "Geographic area", "TIME_PERIOD"])
        .agg({"OBS_VALUE": "last"})
        .sort_values(
            by=["TIME_PERIOD"]
        )  # Add sorting by Year to display the years in proper order
        .reset_index()
    )

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if df.empty:
        return {
            "layout": {
                "xaxis": {"visible": False},
                "yaxis": {"visible": False},
                "annotations": [
                    {
                        "text": "No data is available for selected filters",
                        "xref": "paper",
                        "yref": "paper",
                        "showarrow": False,
                        "font": {"size": 28},
                    }
                ],
            }
        }, ""

    if latest_data:
        # remove the animation frame to be able to show more than one year in the map
        options.pop("animation_frame")
        # add the year to show on hover
        options["hover_name"] = "TIME_PERIOD"
        # keep only the latest value of every country
        df = df.sort_values(["Geographic area", "TIME_PERIOD"]).drop_duplicates(
            "Geographic area", keep="last"
        )

    options["labels"] = DEFAULT_LABELS.copy()
    options["labels"]["OBS_VALUE"] = name
    options["geojson"] = geo_json_countries

    main_figure = px.choropleth_mapbox(df, **options)
    main_figure.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    if latest_data:
        # hide the year range slider and the animation buttons
        main_figure["layout"].pop("sliders")
        main_figure["layout"].pop("updatemenus")

    # check if this area's config has an animation frame and hence a slider
    if len(main_figure.layout["sliders"]) > 0:
        # set last frame as the active one; i.e. select the max year as the default displayed year
        main_figure.layout["sliders"][0]["active"] = len(main_figure.frames) - 1
        # assign the data of the last year to the map; without this line the data will show the first year;
        main_figure = go.Figure(
            data=main_figure["frames"][-1]["data"],
            frames=main_figure["frames"],
            layout=main_figure.layout,
        )
    return main_figure, source


@app.callback(
    Output({"type": "area", "index": MATCH}, "figure"),
    Output({"type": "area_sources", "index": MATCH}, "children"),
    [
        Input("store", "data"),
        Input({"type": "area_options", "index": MATCH}, "value"),
        Input({"type": "area_breakdowns", "index": MATCH}, "value"),
        Input({"type": "area_types", "index": MATCH}, "value"),
        Input({"type": "exclude_outliers_toggle", "index": MATCH}, "value"),
    ],
    [
        State("indicators", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def area_figure(
    selections,
    indicator,
    compare,
    selected_type,
    exclude_outliers,
    indicators_dict,
    id,
):
    # print(id["index"])
    # only run if indicator not empty
    if not indicator:
        return {}, {}

    area = id["index"]
    default = indicators_dict[selections["theme"]][area]["default_graph"]
    fig_type = selected_type if selected_type else default
    config = indicators_dict[selections["theme"]][area]["graphs"][fig_type]
    options = config.get("options")
    traces = config.get("trace_options")
    compare = False if compare == "Total" else compare

    columns = ["CODE", "Indicator", "Geographic area"]
    aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
    query = "CODE == @indicator"

    data = get_filtered_dataset(**selections)

    if compare:
        columns.append(compare)
        total_if_disag_query = get_total_query(data, indicator, True, compare)
    else:
        total_if_disag_query = get_total_query(data, indicator)
    query = (query + " & " + total_if_disag_query) if total_if_disag_query else query

    indicator_name = (
        data[data["CODE"] == indicator]["Indicator"].unique()[0]
        if len(data[data["CODE"] == indicator]["Indicator"].unique()) > 0
        else ""
    )
    name = (
        data[data["CODE"] == indicator]["Unit of measure"].unique()[0]
        if len(data[data["CODE"] == indicator]["Unit of measure"].unique()) > 0
        else ""
    )
    df_indicator_sources = df_sources[df_sources["Code"] == indicator]
    unique_indicator_sources = df_indicator_sources["Source_Full"].unique()
    source = (
        "; ".join(list(unique_indicator_sources))
        if len(unique_indicator_sources) > 0
        else ""
    )

    data_cached = data.query(query)

    # toggle time-series selection based on figure type
    if fig_type == "bar":
        # get rid of time-series for bar plot
        aggregates = {"TIME_PERIOD": "last", "OBS_VALUE": "last"}
        df = data_cached.groupby(columns).agg(aggregates).reset_index()
    else:
        # line plot: uses query directly keeping time series
        df = data_cached

    # check if the exclude outliers checkbox is checked
    if exclude_outliers:
        # filter the data to the remove the outliers
        # (df < df.quantile(0.1)).any() (df > df.quantile(0.9)).any()
        df["z_scores"] = np.abs(zscore(df["OBS_VALUE"]))  # calculate z-scores of df
        # filter the data entries to remove the outliers
        df = df[(df["z_scores"] < 3) | (df["z_scores"].isnull())]

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if df.empty:
        return {
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
        }, ""
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
        legend=dict(x=0.9, y=0.5),
        xaxis={"categoryorder": "total descending"},
    )

    if compare:
        options["color"] = compare
        if compare == "Wealth Quintile":
            wealth_dict = {
                "Lowest": 0,
                "Second": 1,
                "Middle": 2,
                "Fourth": 3,
                "Highest": 4,
            }
            df.sort_values(by=[compare], key=lambda x: x.map(wealth_dict), inplace=True)
        else:
            # sort by the compare value to have the legend in the right ascending order
            df.sort_values(by=[compare], inplace=True)

    fig = getattr(px, fig_type)(df, **options)
    if traces:
        fig.update_traces(**traces)
    # Add this code to avoid having decimal year on the x-axis for time series charts
    if fig_type == "line":
        fig.update_layout(
            xaxis=dict(tickmode="linear", tick0=selections["years"][0], dtick=1)
        )

        # fig.update_layout(xaxis=dict(tickmode="linear", tick0=2010, dtick=1))

    # fig.update_xaxes(categoryorder="total descending")
    fig.update_layout(layout)
    return fig, source
