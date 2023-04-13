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

        control = html.Div(
            className="row",
            children=[
                html.Div(className="col-sm-12 col-md-7", children=[label]),
                html.Div(
                    className="col-sm-12 col-md-5 force-inline-controls",
                    children=[html.I(className="fa fa-arrows-alt-h"),
                        dbc.RadioItems(
                            id={"type": "pvt_control", "index": aio_id},
                            value=sel,
                            options=[
                                {"label": "", "value": "R"},
                                {"label": "", "value": "C"},
                            ],
                            style={"display": "inline-block"},
                            inline=True
                        ),
                        
                        html.I(className="fa fa-arrows-alt-v")
                    ],
                ),
            ],
        )

        if visible:
            display = "block"
        else:
            display = "none"

        super().__init__(
            id=self.ids.dataexplorer_pvt(aio_id),
            children=control,
            style={"display": display},
        )

    @staticmethod
    def update_pvt_controls(dimensions, one_elem_dims, selected_pvt_cfg):
        ret = []
        for dim in dimensions:
            visible = True
            if dim["id"] in one_elem_dims:
                visible = False
            on_row = False
            if selected_pvt_cfg[dim["id"]] == "R":
                on_row = True
            pvt_control = DataExplorerPivotAIO(
                aio_id=dim["id"], label=dim["name"], onrow=on_row, visible=visible
            )
            ret.append(pvt_control)
        return ret
