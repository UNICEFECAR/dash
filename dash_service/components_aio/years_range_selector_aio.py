from dash import html
import uuid
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import datetime


class YearsRangeSelectorAIO(html.Div):
    # _value_style = {"textAlign": "center", "color": "#1cabe2"}
    # A set of functions that create pattern-matching callbacks of the subcomponents
    class ids:
        years_range_sel_ddl = lambda aio_id: {
            "component": "YearsRangeSelectorAIO",
            "subcomponent": "years_range_sel_ddl",
            "aio_id": aio_id,
        }

    # Make the ids class a public class
    ids = ids

    # Define the arguments of the All-in-One component
    def __init__(
        self,
        year_min=2000,
        year_max=None,
        sel_year_min=2000,
        sel_year_max=None,
        years_label="Years",
        aio_id=None,
    ):
        # Allow developers to pass in their own `aio_id` if they're binding their own callback to a particular component.
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        if year_max is None:
            year_max = datetime.datetime.now().year
        if sel_year_max is None:
            sel_year_max = min(year_max, datetime.datetime.now().year)

        years = list(range(year_min, year_max))

        # ret = dbc.DropdownMenu(
        #     label=f"{years_label}: {sel_year_min} - {sel_year_max}",
        #     id=self.ids.years_range_sel_ddl(aio_id),
        #     color="info",
        #     children=[
        #             html.Div(
        #                 style={"minWidth": "500px"},
        #                 className="overflow-auto",
        #                 children=dcc.RangeSlider(
        #                     id="year_slider",
        #                     min=0,
        #                     max=year_max - year_min - 1,
        #                     step=None,
        #                     marks={
        #                         index: str(year) for index, year in enumerate(years)
        #                     },
        #                     value=[
        #                         0,
        #                         len(years) - 1,
        #                     ],
        #                 ),
        #             )
        #         ]
        # )

        ret = dcc.RangeSlider(
            id="year_slider",
            min=year_min,
            max=year_max,
            step=1,
            #marks={index: str(year) for index, year in enumerate(years)},
            marks={i: '{}'.format(i) for i in range(year_min, year_max)},
            value=[
                sel_year_min,
                sel_year_max,
            ],
            tooltip={"placement": "bottom", "always_visible": True}
        )

        # Define the component's layout
        super().__init__(
            #className="d-flex justify-content-center",
            children=ret,
        )
