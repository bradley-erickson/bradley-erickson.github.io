# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
from pages import home, publications, education, projects
from components import navbar, sidebar


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
    title='Bradley Erickson',
    suppress_callback_exceptions=True
)

app.layout = html.Div([
    navbar,
    dbc.Container(
        dbc.Row(
            [
                dbc.Col(
                    sidebar,
                    md=3
                ),
                dbc.Col(
                    [
                        home.layout,
                        publications.layout,
                        education.layout,
                        projects.layout
                    ],
                    md=9
                )
            ]
        )
    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
