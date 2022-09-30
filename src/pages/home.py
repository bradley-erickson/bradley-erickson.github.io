# package imports
from dash import html
import dash_bootstrap_components as dbc

id = 'home'
layout = dbc.Card(
    [
        html.H2('Home'),
        html.P('This is a home page')
    ],
    id=id,
    body=True,
)
