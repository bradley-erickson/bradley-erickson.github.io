# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
from pages import home, publications
from components.navbar import navbar


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        dbc.icons.FONT_AWESOME,
        dbc_css
    ],
    title='Static Site',
    suppress_callback_exceptions=True
)

app.layout = html.Div([
    navbar,
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    [
                        'Image and socials here'
                    ],
                    md=3
                ),
                dbc.Col(
                    dbc.Tabs(
                        [
                            home.home_tab,
                            publications.publications_tab
                        ],
                        class_name='my-3'
                    ),
                    md=9
                )
            ]
        )
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
