# package imports
from dash import html
import dash_bootstrap_components as dbc

# local imports
from components.sidebar import sidebar, pic_path, links

id = 'home'
layout = dbc.Card(
    [
        dbc.Card(
            [
                dbc.CardImg(
                    src=f'{pic_path}',
                    class_name='w-50'
                ),
                html.P(
                    'Hey y\'all, I\'m Brad Erickson'
                ),
                html.Div(links, className='mb-3'),
                html.Div(
                    [
                        html.I(className='fas fa-envelope me-2'),
                        'bericks @ ncsu.edu'
                    ]
                )
            ],
            class_name='d-md-none border-0',
            body=True
        ),
        dbc.Card(
            'Check out the links on the left!',
            class_name='d-none d-md-inline border-0',
            body=True
        )
    ],
    id=id
)
