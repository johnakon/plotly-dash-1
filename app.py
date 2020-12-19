import dash
import dash_auth
import dash_bootstrap_components as dbc

USERNAME_PASSWORD_PAIRS = [
    ['john', '001']
]
# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

server = app.server
