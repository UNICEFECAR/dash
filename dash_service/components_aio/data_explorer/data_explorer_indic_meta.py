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

    def __init__(self, aio_id=None, indicators=None, visible=False):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        ret = html.Div(
            children=[
                html.Div(className="font-weight-bold", children="Indicators metadata"),
                html.Div(id=self.ids.dataexplorer_indic_meta(aio_id)),
            ]
        )

        super().__init__(children=[ret])

    @staticmethod
    def render_indicators(indics_code_name):
        if indics_code_name is None:
            return None
        indic_items = []
        for indic in indics_code_name:
            itm = html.Div([indic["name"], html.I(className="fas fa-info-circle mx-1 float-right")])
            indic_items.append(itm)
        # html_items = [html.Div(indic["name"] ) for indic in indics_code_name]
        ret = html.Div(children=indic_items)
        return ret
    
    
