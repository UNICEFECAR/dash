from dash import Dash

# create Dash application

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        {
            "href": "https://fonts.gstatic.com",
            "rel": "preconnect",
        },
        "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap",
    ],
)

# to deploy using WSGI server
server = app.server
# app tittle for web browser
app.title = "TransMonee Dashboard"
app.sub_title = (
    "Monitoring the situation of children and women in Europe and Central Asia"
)
