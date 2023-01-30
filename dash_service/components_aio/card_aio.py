from dash import html
import uuid
import dash_bootstrap_components as dbc

# def fa(className):
# """A convenience component for adding Font Awesome icons"""
# return html.I(className=f"{className} mx-1")


class CardAIO(dbc.Card):
    _value_style = {"textAlign": "center", "color": "#1cabe2"}
    # A set of functions that create pattern-matching callbacks of the subcomponents
    class ids:
        card = lambda aio_id: {
            "component": "CardAIO",
            "subcomponent": "card",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        value="-",
        suffix="",
        aio_id=None,
        info_head="",
        info_body="",
        time_period="",
        lbl_time_period="Time period",
    ):
        # Allow developers to pass in their own `aio_id` if they're binding their own callback to a particular component.
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        # Create the card body

        card_body = dbc.CardBody(
            [
                html.H1(
                    value,
                    className="display-4",
                    style=CardAIO._value_style,
                ),
                html.H4(suffix, className="card-title"),
            ],
            style={"textAlign": "center"},
        )

        card_children = [card_body]

        card_footer = []

        if time_period != "":
            time_p = html.Div(
                lbl_time_period + ": " + time_period,

                className="text-primary font-weight-bold float-left",
            )
            card_footer.append(time_p)

        # if there is an info body add the "i" icon and the popup window
        if info_body is not None and info_body != "":
            popover_icon = html.Div(
                html.I(className="fas fa-info-circle mx-1 float-right"),
                id=f"card-info_icon{aio_id}",

            )
            card_footer.append(popover_icon)

            popover_window = dbc.Popover(
                [
                    dbc.PopoverHeader(info_head),
                    dbc.PopoverBody(info_body),
                ],
                target=f"card-info_icon{aio_id}",
                trigger="hover",
            )

            card_footer.append(popover_window)

        if len(card_footer) > 0:
            card_children.append(html.Div(className="container", children=card_footer))

        # Define the component's layout
        super().__init__(
            id=self.ids.card(aio_id),
            color="primary",
            outline=True,
            children=card_children,
        )
