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
from . import (
    # countries,
    # countries_iso3_dict,
    # df_sources,
    # dimension_names,
    geo_json_countries,
    # get_filtered_dataset,
    # indicator_names,
    # indicators_config,
    # programme_country_indexes,
    # selection_index,
    # selection_tree,
    # unicef_country_prog,
    years,
    get_selection_tree,
    # get_dataflow_struct,
    get_dataset,
    get_search_countries,
    # get_indicator_name,
    get_codelist
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
# DEFAULT_LABELS = {
#     "Country_name": "Country",
#     "TIME_PERIOD": "Year",
#     "Sex_name": "Sex",
#     "Residence_name": "Residence",
#     "Age_name": "Age",
#     "Wealth_name": "Wealth Quintile",
# }
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


def make_area(area_name):
    area_id = {"type": "area", "index": area_name}
    popover_id = {"type": "area_sources", "index": area_name}
    historical_data_style = {"display": "none"}
    exclude_outliers_style = {"paddingLeft": 20, "display": "block"}
    breakdowns_style = {"display": "block"}

    # TODO: still differentiating main area id from other areas ids because the call backs are still not unified
    if area_name == "MAIN":
        area_id = f"{area_name.lower()}_area"
        popover_id = f"{area_name.lower()}_area_sources"
        historical_data_style = {"display": "block"}
        exclude_outliers_style = {"display": "none"}
        breakdowns_style = {"display": "none"}

    # lbassil: unifying both main and figure area generations by tweaking the ids and styles
    area = dbc.Card(
        [
            dbc.CardHeader(
                id={"type": "area_title", "index": area_name},
                style={"fontWeight": "bold"},
            ),
            dbc.CardBody(
                [
                    dcc.Dropdown(
                        id={"type": "area_options", "index": area_name},
                        className="dcc_control",
                    ),
                    html.Br(),
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
                            "index": area_name,
                        },
                        switch=True,
                        style=historical_data_style,
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_types", "index": area_name},
                        inline=True,
                    ),
                    dcc.Loading([dcc.Graph(id=area_id)]),
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
                        style=exclude_outliers_style,
                    ),
                    html.Br(),
                    dbc.RadioItems(
                        id={"type": "area_breakdowns", "index": area_name},
                        inline=True,
                        style=breakdowns_style,
                    ),
                    html.Div(
                        fa("fas fa-info-circle"),
                        id=f"{area_name.lower()}_area_info",
                        className="float-right",
                    ),
                    dbc.Popover(
                        [
                            dbc.PopoverHeader("Sources"),
                            dbc.PopoverBody(id=popover_id),
                        ],
                        id="hover",
                        target=f"{area_name.lower()}_area_info",
                        trigger="hover",
                    ),
                ]
            ),
        ],
        id={"type": "area_parent", "index": area_name},
    )
    return area


def get_base_layout(**kwargs):
    # indicators_dict = kwargs.get("indicators")
    cfg = kwargs.get("cfg")
    main_title = cfg["main_title"]
    selection_tree = get_selection_tree(cfg["ddl_ref_areas_cl"])

    '''
    
    
    ddl_ref_areas_cl
    
    
    
    '''
    # is_country_profile = kwargs.get("is_country_profile")
    country_dropdown_style = {"display": "none"}
    themes_row_style = {"verticalAlign": "center", "display": "flex"}
    countries_filter_style = {"display": "block"}
    programme_toggle_style = {"display": "block"}
    main_area_style = {"display": "block"}

    return html.Div(
        [
            dcc.Store(id="page_cfg", data=cfg),
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
                                        label=f"Countries: {'len(countries)'}",
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
                                                    # checked=["0"],
                                                    checked=selection_tree["checked"],
                                                    # selected=[],
                                                    expanded=["0"],
                                                    # data=[]
                                                    data=selection_tree["data"],
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
            dbc.CardDeck(
                [make_area(area) for area in ["MAIN"]],
                style=main_area_style,
            ),
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
    Output({"type": "area_parent", "index": MATCH}, "hidden"),
    Input("theme", "hash"),
    [
        State("page_cfg", "data"),
        State({"type": "area_parent", "index": MATCH}, "id"),
    ],
)
def display_areas(theme, page_cfg, id):
    area = id["index"]
    theme = theme[1:].upper() if theme else next(iter(page_cfg["THEMES"].keys()))
    return area not in page_cfg["THEMES"][theme]


@app.callback(
    Output("store", "data"),
    # Output("country_selector", "checked"),
    Output("collapse-years-button", "label"),
    Output("collapse-countries-button", "label"),
    [
        Input("theme", "hash"),
        Input("year_slider", "value"),
        Input("country_selector", "checked"),
    ],
    State("page_cfg", "data"),
)
def apply_filters(
        theme,
        years_slider,
        country_selector,
        # selected_country,
        # indicators,
        store_page_cfg
):
    print("Apply filters")
    # ctx = dash.callback_context
    # selected = ctx.triggered[0]["prop_id"].split(".")[0]
    # print("theme")
    # print(theme)
    # print("years_slider")
    # print(years_slider)
    # print("country_selector")
    # print(country_selector)
    # print("selected_country")
    # print(selected_country)
    # print("indicators")
    # print(indicators)

    # selections = dict(
    #     theme=current_theme,
    #     indicators_dict=indicators,
    #     years=selected_years,
    #     countries=countries_selected_codes,
    #     is_adolescent=("ADOLESCENT" in indicators),
    # )

    theme = theme[1:].upper() if theme else next(iter(store_page_cfg["THEMES"].keys()))

    selected_years = years[years_slider[0]: years_slider[1] + 1]
    sel_country_codes = [c for c in country_selector if c != "0"]  # Exclude the Select all code

    selections = dict(
        theme=theme,
        # indicators_dict=indicators,
        years=selected_years,
        countries=sel_country_codes,
        # is_adolescent=("ADOLESCENT" in indicators),
    )

    return (
        selections,
        # country_selector,
        # countries_selected == unicef_country_prog,
        f"Years: {selected_years[0]} - {selected_years[-1]}",
        # "Countries: {}".format(country_text),
        # "Countries: {}".format("UPDATED"),
        f"Countries: {str(len(sel_country_codes))} selected",
    )


def indicator_card(
        selections,
        card_id,
        name,
        numerator,
        suffix,
        cfg,
        denominator=None,
        absolute=False,
        average=False,
        min_max=False,
        sex_code=None,
        age_group=None,
):
    df_vals = get_dataset(cfg)
    card_value = ""
    if len(df_vals) > 0:
        card_value = df_vals.iloc[0]["OBS_VALUE"]

    return make_card(
        card_id,
        name,
        suffix,
        "Indicator sources",
        "Source link",
        card_value,
        []
        # indicator_sources,
        # source_link,
        # indicator_header,
        # numerator_pairs,
    )


@app.callback(
    Output("cards_row", "children"),
    [
        Input("store", "data"),
    ],
    # [State("cards_row", "children"), State("indicators", "data")],
    [State("cards_row", "children"), State("page_cfg", "data")],
)
# def show_cards(selections, current_cards, indicators_dict):
def show_cards(selections, current_cards, page_cfg):
    print("Show cards")
    cards = [
        indicator_card(
            selections,
            f"card-{num}",
            card["name"],
            card["indicator"],
            card["suffix"],
            card["data"],
            card.get("denominator"),
            card.get("absolute"),
            card.get("average"),
            card.get("min_max"),
            card.get("sex"),
            card.get("age"),
        )
        # for num, card in enumerate(indicators_dict[selections["theme"]]["CARDS"])
        for num, card in enumerate(page_cfg["THEMES"]["PARTICIPATION"]["CARDS"])
    ]

    return cards


@app.callback(
    Output("subtitle", "children"),
    Output("themes", "children"),
    [
        Input("store", "data"),
    ],
    State("page_cfg", "data"),
)
def show_themes(selections, cfg):
    print("Show themes")
    if selections is None or selections["theme"] is None or selections["theme"].strip() == "":
        theme_key = list(cfg["THEMES"].keys())[0]
        theme = cfg["THEMES"][theme_key]
    else:
        theme_key = selections["theme"]
        theme = cfg["THEMES"][selections["theme"]]

    subtitle = theme.get("NAME")

    # hide the buttons when only one option is available
    if len(cfg["THEMES"].items()) == 1:
        return subtitle, []

    buttons = [
        dbc.Button(
            value["NAME"],
            id=key,
            color=colours[num],
            className="theme mx-1",
            href=f"#{key.lower()}",
            active=theme_key == key,
        )
        for num, (key, value) in enumerate(cfg["THEMES"].items())
    ]
    return subtitle, buttons


@app.callback(
    Output({"type": "area_title", "index": MATCH}, "children"),
    Output({"type": "area_options", "index": MATCH}, "options"),
    Output({"type": "area_types", "index": MATCH}, "options"),
    Output({"type": "area_options", "index": MATCH}, "value"),
    Output({"type": "area_types", "index": MATCH}, "value"),
    Input("store", "data"),
    [
        State("page_cfg", "data"),
        State({"type": "area_options", "index": MATCH}, "id"),
    ],
)
def set_options(selection, cfg, id):
    print("Set options")
    # print("print id")
    # print(id)
    # print(cfg)
    # print("selection")
    # print(selection)

    area = id["index"]

    area_options = area_types = []

    cl_indicators = get_codelist("BRAZIL_CO", "CL_BRAZILCO_INDICATORS")
    # for c in cl_indicators:
    #     print(c)

    if area in cfg["THEMES"][selection["theme"]]:
        api_params = cfg["THEMES"][selection["theme"]][area].get("data")
        indic_info = []
        for ap in api_params:
            # indic_name = get_indicator_name(ap, ap["dq"]["INDICATOR"])
            indic = next(item for item in cl_indicators if item["id"] == ap["dq"]["INDICATOR"])
            indic_info.append((ap["dq"]["INDICATOR"], indic["name"]))

        area_options = [
            {
                "label": i[1],
                "value": i[0],
            }
            for i in indic_info]

        # indicators = indicators_dict[theme["theme"]][area].get("indicators")
        # area_indicators = indicators.keys() if indicators is dict else indicators
        # area_options = [
        #     {
        #         "label": indicator_names[code],
        #         "value": code,
        #     }
        #     for code in area_indicators
        # ]

    #     area_types = [
    #         {
    #             "label": name.capitalize(),
    #             "value": name,
    #         }
    #         for name in indicators_dict[theme["theme"]][area].get("graphs", {}).keys()
    #     ]
    #
    # name = (
    #     indicators_dict[theme["theme"]][area].get("name")
    #     if area in indicators_dict[theme["theme"]]
    #     else ""
    # )
    # default_option = (
    #     indicators_dict[theme["theme"]][area].get("default")
    #     if area in indicators_dict[theme["theme"]]
    #     else ""
    # )
    # default_graph = (
    #     indicators_dict[theme["theme"]][area].get("default_graph")
    #     if area in indicators_dict[theme["theme"]]
    #     else ""
    # )

    default_option = "default_option"
    default_graph = "default_graph"
    name = "NAME"

    return name, area_options, area_types, default_option, default_graph


'''
@app.callback(
    Output("main_area", "figure"),
    Output("main_area_sources", "children"),
    [
        Input({"type": "area_options", "index": "MAIN"}, "value"),
        Input({"type": "historical_data_toggle", "index": "MAIN"}, "value"),
        Input("store", "data"),
    ],
    [
        State("page_cfg", "data"),
    ],
)
'''


def main_figure(indicator, show_historical_data, selections, cfg):
    latest_data = not show_historical_data

    options = cfg["THEMES"][selections["theme"]]["MAIN"]["options"]
    series = cfg["THEMES"][selections["theme"]]["MAIN"]["data"]
    time_period = [min(selections["years"]), max(selections["years"])]
    ref_areas = selections["countries"]

    if latest_data:
        df_data = get_dataset(series[0], time_period, ref_areas)
    else:
        df_data = get_dataset(series[0], time_period, ref_areas)

    # check if the dataframe is empty meaning no data to display as per the user's selection
    if df_data.empty:
        return EMPTY_CHART, ""

    '''

    # lbassil: replace UNIT_MEASURE by Unit_name to use the name of the unit instead of the code
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
    options["labels"]["text"] = "OBS_VALUE"
    options["geojson"] = geo_json_countries
    if latest_data:
        # remove the animation frame and show all countries at once
        options.pop("animation_frame")
        # add the year to show on hover
        options["hover_name"] = "TIME_PERIOD"

    main_figure = px.choropleth_mapbox(data, **options)
    main_figure.update_layout(margin={"r": 0, "t": 1, "l": 2, "b": 1})

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
    '''
    source = ""
    source_link = ""
    return main_figure, html.A(html.P(source), href=source_link, target="_blank")
