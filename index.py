import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to the app pages
from apps import vgames, global_sales


app.layout = dbc.Container([
                dbc.Row([
                    dbc.Col(html.H3("WELCOME TO MY DASH BOARD",
                            className="text-center text-primary, mb-4"),
                        width=12, style={"textDecoration": "underline", "color":"teal"})
                ]),
                html.Div([
                    dcc.Location(id='url', refresh=False),
                    html.Div([
                        html.H4(dcc.Link('Video Games|', href='/apps/vgames',
                            style={"textDecoration": "none"}
                        )),
                        html.H4(dcc.Link('Other Products', href='/apps/global_sales',
                            style={"textDecoration": "none"}
                        )),
                    ], className="row"),
                    html.Div(id='page-content', children=[])
                ])
            ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/vgames':
        return vgames.layout
    if pathname == '/apps/global_sales':
        return global_sales.layout
    else:
        return "Please click one of the links above to continue"


if __name__ == '__main__':
    app.run_server(debug=True)
