from dash import html
import uuid


class DataExplorer(html.Div):
    class ids:
        dataexplorer = lambda aio_id: {
            "component": "DataEplorer",
            "subcomponent": "dataexplorer",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(self, aio_id=None):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

    super(children="Data explorer")
