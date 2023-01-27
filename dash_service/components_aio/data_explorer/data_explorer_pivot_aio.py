from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import uuid
import datetime


class DataExplorerPivotAIO(html.Div):
    class ids:
        dataexplorer_pvt = lambda aio_id: {
            "component": "dataexplorer_pvt",
            "subcomponent": "dataexplorer_pvt",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
        self,
        aio_id=None,
        label="",
        onrow=True,
        lblRow="Row",
        lblCol="Column",
        visible=True,
    ):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        sel = "C"
        if onrow:
            sel = "R"

        control = [
            html.Div(className="row", children=[label]),
            dcc.RadioItems(
                [{"label": lblRow, "value": "R"}, {"label": lblCol, "value": "C"}],
                sel,
                id={"type": "pvt_control", "index": aio_id},
                inline=True,
                className="row col-12",
                style={
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "center",
                },
            ),
        ]

        if visible:
            display = "block"
        else:
            display = "none"
            
        super().__init__(
            id=self.ids.dataexplorer_pvt(aio_id),
            children=control,
            style={"display": display},
        )
