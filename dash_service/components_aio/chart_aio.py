from dash import html, dcc, MATCH
import uuid
import dash_bootstrap_components as dbc
from .downloads_aio import DownloadsAIO


class ChartAIO(html.Div):
    _header_style = {"fontWeight": "bold"}

    class ids:
        card = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "card",
            "aio_id": aio_id,
        }

        card_title = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "card_title",
            "aio_id": aio_id,
        }

        ddl = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "ddl",
            "aio_id": aio_id,
        }

        chart_types = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "chart_types",
            "aio_id": aio_id,
        }

        chart = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "chart",
            "aio_id": aio_id,
        }

        info_icon = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "info_icon",
            "aio_id": aio_id,
        }
        info_text = lambda aio_id: {
            "component": "ChartAIO",
            "subcomponent": "info_text",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    def __init__(
        self,
        aio_id=None,
        plot_cfg=None,
        info_title="",
        lbl_excel="Download Excel",
        lbl_csv="Download CSV",
    ):

        if aio_id is None:
            aio_id = str(uuid.uuid4())

        card_header = dbc.CardHeader(
            id=self.ids.card_title(aio_id),
            style=ChartAIO._header_style,
            children=[],
        )

        card_body = dbc.CardBody(
            children=[
                html.Div(
                    className="row my-2",
                    children=[
                        dcc.Dropdown(id=self.ids.ddl(aio_id), className="dcc_control")
                    ],
                ),
                html.Div(
                    className="row my-2 force-inline-controls",
                    children=[
                        dbc.RadioItems(
                            id=self.ids.chart_types(aio_id),
                            options=[],
                            inline=True
                        )
                    ],
                ),
                dcc.Loading([dcc.Graph(id=self.ids.chart(aio_id), config=plot_cfg)]),
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="col-9",
                            children=[
                                DownloadsAIO(
                                    aio_id, lbl_excel=lbl_excel, lbl_csv=lbl_csv
                                )
                            ],
                        ),
                        html.Div(
                            id=self.ids.info_icon(aio_id),
                            className="col-3",
                            children=[
                                html.I(
                                    id="chart_aio_inf_icon_" + aio_id,
                                    className="fas fa-info-circle mx-1 float-end ",
                                    style={"padding-right": "30px"},
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    children=[
                        dbc.Popover(
                            [
                                dbc.PopoverHeader(info_title),
                                dbc.PopoverBody(id=self.ids.info_text(aio_id)),
                            ],
                            id="hover",
                            target="chart_aio_inf_icon_" + aio_id,
                            trigger="hover",
                        )
                    ],
                ),
            ]
        )

        card = dbc.Card(children=[card_header, card_body])

        # Define the component's layout
        super().__init__(
            id=self.ids.card(aio_id),
            className="col",
            style={"margin-bottom": "20px"},
            children=[card],
        )
