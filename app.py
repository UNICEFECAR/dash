from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc
from components import fa

# create Dash application

app = Dash(
    __name__,
    external_stylesheets=[
        {
            "href": "https://fonts.gstatic.com",
            "rel": "preconnect",
        },
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap",
    ],
    use_pages=True,
)

# to deploy using WSGI server
server = app.server
# app tittle for web browser
app.title = "TransMonee Dashboard"
app.sub_title = (
    "Monitoring the situation of children and women in Europe and Central Asia"
)

# configure the Dash instance's layout
app.layout = html.Div(
    [
        # make_header(),
        html.Br(),
        dcc.Store(id="store"),
        dbc.Container(
            fluid=True,
            children=page_container,
        ),
        # make_footer(),
        html.Button(
            id="btnScroll",
            title="Scroll to top",
            className="btn btn-dark scroll-top",
            children=[
                fa("fas fa-chevron-up"),
            ],
            style={
                "border-radius": 50,
                "position": "fixed",
                "right": 20,
                "bottom": 20,
                "z-index": 1101,
                "width": 50,
                "height": 50,
                "padding": 12,
                "border": 0,
                "display": "none",
            },
        ),
    ],
    id="mainContainer",
)

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
