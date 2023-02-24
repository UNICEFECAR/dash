from pydoc import classname
from dash import html, dcc, MATCH
import uuid
import dash_bootstrap_components as dbc
from .downloads_aio import DownloadsAIO

# def fa(className):
# """A convenience component for adding Font Awesome icons"""
# return html.I(className=f"{className} mx-1")


class MapAIO(html.Div):

    _header_style = {"fontWeight": "bold"}

    # A set of functions that create pattern-matching callbacks of the subcomponents
    class ids:
        card = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "card",
            "aio_id": aio_id,
        }

        card_title = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "card_title",
            "aio_id": aio_id,
        }

        ddl = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "ddl",
            "aio_id": aio_id,
        }

        toggle_historical = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "toggle_historical",
            "aio_id": aio_id,
        }

        graph = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "graph",
            "aio_id": aio_id,
        }
        info_icon = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "info_icon",
            "aio_id": aio_id,
        }
        info_text = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "info_text",
            "aio_id": aio_id,
        }
        download_buttons = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "download_buttons",
            "aio_id": aio_id,
        }
        map_timpe_period = lambda aio_id: {
            "component": "MapAIO",
            "subcomponent": "map_timpe_period",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(self, aio_id=None, plot_cfg=None, info_title="", lbl_show_hist = "Show historical data", lbl_excel="Download Excel", lbl_csv="Download CSV"):
        # Allow developers to pass in their own `aio_id` if they're binding their own callback to a particular component.
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        card_header = dbc.CardHeader(
            id=self.ids.card_title(aio_id),
            style=MapAIO._header_style,
            children=[],
        )

        card_body = dbc.CardBody(
            children=[
                dcc.Dropdown(
                    id=self.ids.ddl(aio_id),
                    className="dcc_control",
                    options=[],
                    value="",
                ),
                html.Br(),
                dbc.Checklist(
                    options=[
                        {
                            "label": lbl_show_hist,
                            "value": 1
                        }
                    ],
                    value=[],
                    id=self.ids.toggle_historical(aio_id),
                    switch=True,
                    style={"display": "block"},
                    className="float-left"
                ),
                html.Div(id=self.ids.map_timpe_period(aio_id), className="text-primary font-weight-bold float-right", children=[]),
                html.Br(),
                html.Br(),
                dcc.Loading([dcc.Graph(id=self.ids.graph(aio_id), config=plot_cfg)]),
                html.Br(),
                html.Div(
                    className="fload-left",
                    children=[DownloadsAIO(aio_id, lbl_excel=lbl_excel, lbl_csv=lbl_csv)],
                ),
                # Icon wrapper: a workaround to link the popover that wouldn't work with aio created IDs
                html.Div(
                    id=self.ids.info_icon(aio_id),
                    className="float-right",
                    children=[
                        html.I(
                            id="map_aio_inf_icon_" + aio_id,
                            className="fas fa-info-circle mx-1",
                            style={"padding-right": "30px"},
                        ),
                    ],
                ),
                dbc.Popover(
                    [
                        dbc.PopoverHeader(info_title),
                        dbc.PopoverBody(id=self.ids.info_text(aio_id)),
                    ],
                    id="hover",
                    target="map_aio_inf_icon_" + aio_id,
                    trigger="hover",
                ),
            ]
        )

        # Create the card body
        card = dbc.Card(children=[card_header, card_body])

        # Define the component's layout
        super().__init__(id=self.ids.card(aio_id), children=[card])
