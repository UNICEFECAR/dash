from dash import html, dcc
import dash_bootstrap_components as dbc
import uuid


class DataExplorerFilterAIO(html.Div):
    class ids:
        dataexplorerfilter = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter",
            "aio_id": aio_id,
        }

        dataexplorerfilter_button = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter_button",
            "aio_id": aio_id,
        }

        dataexplorerfilter_body = lambda aio_id: {
            "component": "DataExplorerFilterAIO",
            "subcomponent": "dataexplorerfilter_body",
            "aio_id": aio_id,
        }

    ids = ids

    def __init__(self, aio_id=None, label="", items=[], expanded=False):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # accordion = html.Div(
        #     className="accordion",
        #     id=self.ids.dataexplorerfilter_accordion(aio_id),
        #     children=[
        #         html.Div(
        #             className="card",
        #             children=[
        #                 html.Div(
        #                     className="card-header",
        #                     id=self.ids.dataexplorerfilter_accordion_h(aio_id),
        #                     children=[
        #                         html.H2(

        #                             children=[
        #                                 html.Button(
        #                                     className="btn btn-link btn-block text-left",
        #                                     type="button",
        #                                     # **{"data-toggle": "collapse",
        #                                     # "data-target":self.ids.dataexplorerfilter_accordion_b(aio_id)},
        #                                     children=[label],
        #                                 )
        #                             ],
        #                         )
        #                     ],
        #                 )
        #             ],
        #         )
        #     ],
        # )

        # accordion = html.Div(
        #     className="row",
        #     children=[
        #         html.A(
        #             href="#",
        #             style={
        #                 "text-decoration": "none",
        #                 "width": "100%",
        #                 "background-color": "red",
        #             },
        #             children=[label],
        #         )
        #     ],
        # )

        # accordion = html.Div(
        #     className="row",
        #     children=[
        #         dbc.Button(
        #             type="button",
        #             color="link",
        #             children=[label],
        #         )
        #     ],
        # )
        accordion = dbc.Button(
            id=self.ids.dataexplorerfilter_button(aio_id),
            type="button",
            color="link",
            className="row col-12",
            children=[label],
        )

        classname = "row col-12"
        if expanded:
            classname = classname + " d-block"
        else:
            classname = classname + " d-none"

        acc_body = html.Div(
            id=self.ids.dataexplorerfilter_body(aio_id),
            className=classname,
            children=["children of " + label],
        )

        # title = html.Div(children=[label])

        super().__init__(children=[accordion, acc_body])
