# package imports
from dash import html, dcc
import dash_bootstrap_components as dbc
import os

# local imports
from .navbar import links

pic_path = os.path.join('assets', 'me.png')

sidebar = dbc.Card(
    [
        dbc.CardImg(
            src=f'{pic_path}',
        ),
        html.P(
            'Hey y\'all, I\'m Brad Erickson'
        ),
        html.Div(links, className='mb-3'),
        html.Div(
            [
                html.I(className='fas fa-envelope me-2'),
                'bbwe24 @ gmail.com'
            ]
        ),
    ],
    class_name='border-0 d-md-block d-none',
    body=True
)
