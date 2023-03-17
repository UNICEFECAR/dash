from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import uuid
import datetime


class DataExplorerIndicatorMetaAIO(html.Div):
    class ids:
        dataexplorer_indic_meta = lambda aio_id: {
            "component": "dataexplorer_indic_meta",
            "subcomponent": "dataexplorer_indic_meta",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(
        self,
        aio_id=None,
        indicators=None,
        visible=False
    ):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        ret = html.Div(children=[
            html.Div(className="font-weight-bold", children="Indicators metadata")
        ])
            
        super().__init__(children=[ret])
