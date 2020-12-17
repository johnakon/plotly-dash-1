import dash
import dash_auth
USERNAME_PASSWORD_PAIRS = [
    ['akonya', '001'],['ozzy', '002']
]
# meta_tags are required for the app layout to be mobile responsive
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
auth = dash_auth.BasicAuth(app,USERNAME_PASSWORD_PAIRS)

server = app.server
