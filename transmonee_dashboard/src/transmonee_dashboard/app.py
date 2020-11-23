import plotly.io as pio
from mapbox import Geocoder
from flask_caching import Cache

from . import create_flask, create_dash
from .layouts import main_layout_header, main_layout_sidebar, main_default_layout


mapbox_access_token = "pk.eyJ1IjoiamNyYW53ZWxsd2FyZCIsImEiOiJja2NkMW02aXcwYTl5MnFwbjdtdDB0M3oyIn0.zkIzPc4NSjLZvrY-DWrlZg"

sdmx_url = "https://sdmx.data.unicef.org/ws/public/sdmxapi/rest/data/ECARO,TRANSMONEE,1.0/.{}....?format=csv"

geocoder = Geocoder(access_token=mapbox_access_token)

pio.templates.default = "plotly_white"

# The Flask instance
server = create_flask()

# The Dash instance
app = create_dash(server)

# define a cache instance
#TODO: Move configuration to settings
cache = Cache(app.server, config={
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory'
})


# Push an application context so we can use Flask's 'current_app'
with server.app_context():
    # load the rest of our Dash app
    from . import index

    # configure the Dash instance's layout
    app.layout = main_default_layout()
