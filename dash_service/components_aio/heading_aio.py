from dash import html
import uuid
import dash_bootstrap_components as dbc

# def fa(className):
# """A convenience component for adding Font Awesome icons"""
# return html.I(className=f"{className} mx-1")


class HeadingAIO(html.Div):
    # _value_style = {"textAlign": "center", "color": "#1cabe2"}
    # A set of functions that create pattern-matching callbacks of the subcomponents
    class ids:
        heading = lambda aio_id: {
            "component": "HeadingAIO",
            "subcomponent": "heading",
            "aio_id": aio_id,
        }

        subtitle = lambda aio_id: {
            "component": "HeadingAIO",
            "subcomponent": "subtitle",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        title="",
        subtitle="",
        aio_id=None,
    ):
        # Allow developers to pass in their own `aio_id` if they're binding their own callback to a particular component.
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Create the heading
        ret = html.Div(
            className="heading col-xs-12 p-4",
            children=[
                html.Div(
                    className="heading-content",
                    children=[
                        html.Div(
                            className="heading-panel p4",
                            children=[
                                html.H1(title),
                                html.P(id=self.ids.subtitle(aio_id), children=subtitle),
                            ],
                        )
                    ],
                )
            ],
        )

        # Define the component's layout
        super().__init__(id=self.ids.heading(aio_id), className="row", children=ret)
