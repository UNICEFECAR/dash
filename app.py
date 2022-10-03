from dash import Dash, page_container
import dash_bootstrap_components as dbc

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

# App Layout is only the page container
app.layout = dbc.Container(
    [
        page_container
        # dcc.Loading(
        #     children=page_container,
        #     id="loading-page",
        #     type="circle",
        #     fullscreen=True,
        # ),
    ],
    fluid=True,
)

# to deploy using WSGI server
server = app.server
# app tittle for web browser
app.title = "TransMonee Dashboard"
app.sub_title = (
    "Monitoring the situation of children and women in Europe and Central Asia"
)

# Run app
if __name__ == "__main__":
    app.run_server(debug=True)
