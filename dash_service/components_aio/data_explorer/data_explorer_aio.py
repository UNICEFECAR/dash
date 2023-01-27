from dash import html, dcc
import dash_bootstrap_components as dbc
import uuid
import datetime

from .data_explorer_table_aio import DataExplorerTableAIO
from dash_service.components_aio.data_explorer.downloads_tbl_aio import (
    Downloads_tbl_AIO,
)


class DataExplorerAIO(html.Div):
    _CFG_LASTN = "lastnobservations"
    _LAST1OBS_LABEL = "Show latest data only"

    class ids:
        dataexplorer = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "dataexplorer",
            "aio_id": aio_id,
        }
        de_lastnobs = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_lastnobs",
            "aio_id": aio_id,
        }
        de_time_period = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_time_period",
            "aio_id": aio_id,
        }
        de_filters = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_filters",
            "aio_id": aio_id,
        }
        de_pvt_control = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_pvt_control",
            "aio_id": aio_id,
        }
        de_table_title = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_table_title",
            "aio_id": aio_id,
        }
        de_download_data = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_download_data",
            "aio_id": aio_id,
        }

        de_unique_dims = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_unique_dims",
            "aio_id": aio_id,
        }
        de_unique_attribs = lambda aio_id: {
            "component": "DataExplorer",
            "subcomponent": "de_unique_attribs",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(self, aio_id=None, cfg=None, labels={}):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        lastnobs = []
        if cfg is not None:
            if cfg.get(DataExplorerAIO._CFG_LASTN, 0) != 0:
                lastnobs = ["lastn"]

        txt_lastnobs = labels.get(
            DataExplorerAIO._CFG_LASTN, DataExplorerAIO._LAST1OBS_LABEL
        )

        filter_lastnobs = dcc.Checklist(
            id=self.ids.de_lastnobs(aio_id),
            options=[{"label": txt_lastnobs, "value": "lastn"}],
            value=lastnobs,
        )

        back_n_years = 10
        time_min = 2000
        time_max = datetime.datetime.now().year
        time_start = time_max - back_n_years
        time_end = time_max
        if cfg is not None:
            time_min = cfg.get("time_period_filter_start", time_min)
            time_start = datetime.datetime.now().year - cfg.get(
                "start_n_years_back", back_n_years
            )

        filter_time = dcc.RangeSlider(
            time_min,
            time_max,
            1,
            marks={time_min: str(time_min), time_max: str(time_max)},
            value=[time_start, time_end],
            id=self.ids.de_time_period(aio_id),
            className="de_rangeslider",
            allowCross=False,
            tooltip={"placement": "bottom", "always_visible": True},
        )

        left_col = html.Div(
            className="col-sm-12 col-lg-3 bg-light",
            children=[
                html.Div(children=filter_lastnobs),
                html.Div(children=filter_time),
                html.Div(id=self.ids.de_filters(aio_id), children=[]),
                html.Div(id=self.ids.de_pvt_control(aio_id), children=[]),
            ],
        )

        lbl_download_excel = "Download Excel"
        lbl_download_csv = "Download CSV"
        if "download_excel" in labels:
            lbl_download_excel = labels["download_excel"]
        if "download_csv" in labels:
            lbl_download_csv = labels["download_csv"]

        btn_downloads = Downloads_tbl_AIO(
            aio_id, lbl_excel=lbl_download_excel, lbl_csv=lbl_download_csv, additional_classes="float-right"
        )

        table_col = html.Div(
            className="col-sm-12 col-lg-9",
            children=[
                html.H1(
                    id=self.ids.de_table_title(aio_id),
                    children=[],
                    className="row col-sm-12 col-lg-9",
                ),
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="col-sm-9",
                            # style={"backgroundColor": "red"},
                            children=[
                                html.Div(
                                    id=self.ids.de_unique_dims(aio_id), children=[]
                                ),
                                html.Div(
                                    id=self.ids.de_unique_attribs(aio_id), children=[]
                                ),
                            ],
                        ),
                        html.Div(
                            className="col-sm-3",
                            children=[btn_downloads],
                        ),
                    ],
                ),
                DataExplorerTableAIO(aio_id, className="row col-sm-12"),
            ],
        )

        super().__init__(className="row col-sm-12", children=[left_col, table_col])