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

    def __init__(self, aio_id=None):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        super().__init__(id=self.ids.dataexplorer_indic_meta(aio_id), children=[])

    @staticmethod
    def render_indicators(indic_profiles_url, indics_code_name):
        if indic_profiles_url is None or indics_code_name is None:
            return None

        if not indic_profiles_url.endswith("/"):
            indic_profiles_url = indic_profiles_url + "/"

        indic_items = []
        for indic in indics_code_name:
            itm = html.Div(
                html.A(
                    className="text-dark indic_prof_link",
                    href=indic_profiles_url + indic["id"],
                    target="_blank",
                    children=[
                        html.I(className="indic_prof_link fas fa-info-circle mx-1 float-right"),
                        indic["name"],
                    ],
                )
            )
            indic_items.append(itm)

        ret = html.Div(
            children=[
                html.Div(
                    className="row p-1 mb-2 mt-4 bg-primary text-white w font-weight-bold",
                    children="Indicators metadata",
                ),
                html.Div(children=indic_items),
            ]
        )

        return ret
