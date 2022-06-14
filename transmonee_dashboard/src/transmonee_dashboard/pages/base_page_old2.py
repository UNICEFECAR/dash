import textwrap

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_treeview_antd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from dash.dependencies import MATCH, ClientsideFunction, Input, Output, State
from scipy.stats import zscore

from ..app import app
from ..components import fa

'''
from . import (
    countries,
    countries_iso3_dict,
    df_sources,
    dimension_names,
    geo_json_countries,
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
'''

from . import (
    years,
    countries,
    get_search_countries,
    selection_tree,
    selection_index,
    countries_iso3_dict
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
    themes_row_style = {"verticalAlign": "center", "display": "flex"}
    country_dropdown_style = {"display": "none"}
    countries_filter_style = {"display": "block"}

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
                                            # dbc.FormGroup(
                                            #     [
                                            #         dbc.Checkbox(
                                            #             id="programme-toggle",
                                            #             className="custom-control-input",
                                            #         ),
                                            #         dbc.Label(
                                            #             "UNICEF Country Programmes",
                                            #             html_for="programme-toggle",
                                            #             className="custom-control-label",
                                            #             color="primary",
                                            #         ),
                                            #     ],
                                            #     className="custom-control custom-switch m-2",
                                            #     check=True,
                                            #     inline=True,
                                            #     style=programme_toggle_style,
                                            # ),
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
                ],
            ),
        ]
    )


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


def make_card(
        card_id,
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
):
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
                    dbc.PopoverHeader(
                        html.A(
                            html.P(f"Sources: {indicator_sources}"),
                            href=source_link,
                            target="_blank",
                        )
                    ),
                    dbc.PopoverBody(
                        dcc.Markdown(get_card_popover_body(numerator_pairs))
                    ),
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


@app.callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    # Output("programme-toggle", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
        # Input("programme-toggle", "checked"),
        # Input("country_profile_selector", "value"),
    ],
    State("indicators", "data"),
)
def apply_filters(
        theme,
        years_slider,
        country_selector,
        # programme_toggle,
        # selected_country,
        indicators,
):
    print("apply_filters called")
    ctx = dash.callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    countries_selected = set()
    current_theme = theme[1:].upper() if theme else next(iter(indicators.keys()))
    # check if it is the country profile page
    is_country_profile = current_theme == "COUNTRYPROFILE"
    # check if the user clicked on the generate button in the country profile page
    '''
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
    '''
    for index in country_selector:
        countries_selected.update(selection_index[index])
        if countries_selected == countries:
            # if all countries are all selected then stop
            break
    countries_selected = list(countries_selected)
    country_text = f"{len(countries_selected)} Selected"
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0]: years_slider[1] + 1]
    # selected_years = years[slice(*years_slider)]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    countries_selected_codes = [
        countries_iso3_dict[country] for country in countries_selected
    ]

    print("countries_selected")
    print(countries_selected)
    print("country_text")
    print(country_text)
    print("selected_years")
    print(selected_years)
    print("countries_selected_codes")
    print(countries_selected_codes)
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        countries=countries_selected_codes,
        is_adolescent=("ADOLESCENT" in indicators),
    )

    print("SELECTION")
    print(selections)

    return (
        selections,
        country_selector,
        # countries_selected == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        "Countries: {}".format(country_text),
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


def indicator_card(
    selections,
    card_id,
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
        numerator_pairs = []
        return make_card(
            card_id,
            name,
            indicator_header,
            indicator_sources,
            source_link,
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
        else:
            # trick to accomodate cards for admin exams (AND for boolean indicators)
            # filter exams according to number of indicators
            indicator_sum = (
                (numerator_pairs.OBS_VALUE == len(indicators)).to_numpy().sum()
            )
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

    return make_card(
        card_id,
        name,
        suffix,
        indicator_sources,
        source_link,
        indicator_header,
        numerator_pairs,
    )

@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    [State("cards_row", "children"), State("indicators", "data")],
)
def show_cards(selections, current_cards, indicators_dict):
    cards = []

    cards = [
        indicator_card(
            selections,
            f"card-{num}",
            card["name"],
            card["indicator"],
            card["suffix"],
            card.get("denominator"),
            card.get("absolute"),
            card.get("average"),
            card.get("min_max"),
            card.get("sex"),
            card.get("age"),
        )
        for num, card in enumerate(indicators_dict[selections["theme"]]["CARDS"])
    ]

    return cards
