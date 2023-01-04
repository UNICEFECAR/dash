from dash import html, dcc
import uuid
import dash_bootstrap_components as dbc


class DownloadsAIO_dll(dbc.ButtonGroup):
    # _value_style = {"textAlign": "center", "color": "#1cabe2"}
    # A set of functions that create pattern-matching callbacks of the subcomponents
    class ids:

        btn_down_group = lambda aio_id: {
            "component": "DownloadsAIO_dll",
            "subcomponent": "btn_down_group",
            "aio_id": aio_id,
        }
        btn_down_excel = lambda aio_id: {
            "component": "DownloadsAIO_dll",
            "subcomponent": "btn_down_excel",
            "aio_id": aio_id,
        }

        btn_down_csv = lambda aio_id: {
            "component": "DownloadsAIO_dll",
            "subcomponent": "btn_down_csv",
            "aio_id": aio_id,
        }

        dcc_down_excel = lambda aio_id: {
            "component": "DownloadsAIO_dll",
            "subcomponent": "dcc_down_excel",
            "aio_id": aio_id,
        }

        dcc_down_csv = lambda aio_id: {
            "component": "DownloadsAIO_dll",
            "subcomponent": "dcc_down_csv",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        aio_id=None,
        lbl_download="Download",
        lbl_excel="Download Excel",
        lbl_csv="Download CSV",
    ):
        # Allow developers to pass in their own `aio_id` if they're binding their own callback to a particular component.
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Create the card body
        ret = [
            html.Div(
                className="dropdown",
                children=[
                    html.Button(
                        className="btn btn-primary dropdown-toggle",
                        type="button",
                        id=self.ids.btn_down_group(aio_id),
                        **{
                            "data-toggle": "dropdown",
                            "aria-haspopup": "true",
                            "aria-expanded": "false",
                        },
                        children=[lbl_download]
                    ),
                    html.Div(
                        className="dropdown-menu",
                        **{"aria-labelledby": self.ids.btn_down_group(aio_id)},
                        children=[
                            html.A(
                                className="dropdown-item",
                                href="#",
                                children=[lbl_excel],
                            ),
                            html.A(
                                className="dropdown-item",
                                href="#",
                                children=[lbl_csv],
                            ),
                        ]
                    ),
                ],
            ),
            dcc.Download(id=self.ids.dcc_down_excel(aio_id)),
            dcc.Download(id=self.ids.dcc_down_csv(aio_id)),
        ]

        # Define the component's layout
        super().__init__(id=self.ids.btn_down_group(aio_id), children=ret)
