from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import uuid
import datetime


class DataExplorerTableAIO(html.Div):
    class ids:
        dataexplorertable = lambda aio_id: {
            "component": "dataexplorertable",
            "subcomponent": "dataexplorertable",
            "aio_id": aio_id,
        }

        dataexplorertable_tbl = lambda aio_id: {
            "component": "dataexplorertable",
            "subcomponent": "dataexplorertable_tbl",
            "aio_id": aio_id,
        }

        dataexplorertable_summary = lambda aio_id: {
            "component": "dataexplorertable",
            "subcomponent": "dataexplorertable_summary",
            "aio_id": aio_id,
        }

        dataexplorertable_summary2 = lambda aio_id: {
            "component": "dataexplorertable",
            "subcomponent": "dataexplorertable_summary2",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(self, aio_id=None):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        dtable = dash_table.DataTable(
            id=self.ids.dataexplorertable_tbl(aio_id),
            data=[],
            columns=[],
            virtualization=True,
            # fixed_rows={"headers": True, "data": 0},
            page_action="none",
            style_cell={
                "minWidth": "50px",
                "maxWidth": "190px",
                "overflow": "hidden",
                "textOverflow": "ellipsis",
            },
            style_header={"display": "none"},
            fixed_rows={"headers": False},
            cell_selectable=False,
            tooltip_data=[],
            style_data_conditional=[],
        )

        div_summary = html.Div(
            id=self.ids.dataexplorertable_summary(aio_id), children=["Summary"]
        )
        div_summary2 = html.Div(
            id=self.ids.dataexplorertable_summary2(aio_id), children=["Summary2"]
        )

        super().__init__(children=[div_summary, div_summary2, dtable])
