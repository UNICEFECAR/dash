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

from . import (
    years,
    cl_ref_areas,
    sel_ref_areas,
    selection_tree
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

                                            # dcc.Dropdown(
                                            #     id="country_profile_selector",
                                            #     options=get_search_countries(False),
                                            #     value="ALB",
                                            #     multi=False,
                                            #     placeholder="Select a country...",
                                            #     className="m-2",
                                            #     style=country_dropdown_style,
                                            # ),
                                            dbc.DropdownMenu(
                                                label=f"Countries: {len(sel_ref_areas)}",
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

@app.callback(
    Output()
)


@app.callback(
    Output("store", "data"),
    Output("country_selector", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
    ],
    State("indicators", "data"),
)
def apply_filters(
        theme,
        years_slider,
        country_selector,
        indicators,
):
    ctx = dash.callback_context
    selected = ctx.triggered[0]["prop_id"].split(".")[0]
    print("selected")
    print(selected)
    print("selected end")
    # countries_selected = set()
    current_theme = theme[1:].upper() if theme else next(iter(indicators.keys()))


    # if selected=="country_selector":
    #     if

    print("country_selector")
    print(country_selector)
    print("country_selector END")

    # for index in country_selector:
    #
    #     # print(index)
    #     print(index)
    #     print(country_selector[index])
        # countries_selected.update(selection_index[index])
        # if countries_selected == countries:
        #     if all countries are all selected then stop
        # break


    # countries_selected = list(countries_selected)
    country_text = f"{len(country_selector)} Selected"
    # need to include the last selected year as it was exluded in the previous method
    selected_years = years[years_slider[0]: years_slider[1] + 1]
    # selected_years = years[slice(*years_slider)]

    # Use the dictionary to return the values of the selected countries based on the SDMX ISO3 codes
    # countries_selected_codes = [
    #     countries_iso3_dict[country] for country in countries_selected
    # ]

    # print("countries_selected")
    # print(countries_selected)
    print("country_text")
    print(country_text)
    print("selected_years")
    print(selected_years)
    print("countries_selected_codes")
    # print(countries_selected_codes)
    selections = dict(
        theme=current_theme,
        indicators_dict=indicators,
        years=selected_years,
        # countries=countries_selected_codes,
        countries=[]
        # is_adolescent=("ADOLESCENT" in indicators),
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
