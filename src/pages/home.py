# package imports
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Card(
    [
        html.H2('Home'),
        html.P('This is a home page')
    ],
    body=True,
    class_name='border-0'
)

home_tab = dbc.Tab(
    layout,
    label='Home'
)
