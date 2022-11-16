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

    ids = ids

    def __init__(self, aio_id=None, obs_num_per_page=None):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        if obs_num_per_page is None:
            page_action = "none"
            page_size = 0
        else:
            page_action = "native"
            page_size = obs_num_per_page

        dtable = dash_table.DataTable(
            id=self.ids.dataexplorertable_tbl(aio_id),
            data=[],
            columns=[],
            virtualization=True,
            fixed_rows={"headers": True, "data": 0},
            # page_action="none",
            page_action=page_action,
            page_size=page_size,
            style_cell={
                "minWidth": "60px",
                "maxWidth": "250px",
            },
            style_header={"fontWeight": "bold"},
            cell_selectable=False,
            tooltip_data=[],
        )

        div_summary = html.Div(
            id=self.ids.dataexplorertable_summary(aio_id), children=["Summary"]
        )

        super().__init__(children=[div_summary, "DTabel_start", dtable, "DTabel_end"])
