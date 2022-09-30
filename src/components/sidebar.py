# package imports
from dash import html, dcc
import dash_bootstrap_components as dbc
import os

# local imports
from .navbar import links

pic_path = os.path.join('assets', 'woods.png')

sidebar = dbc.Card(
    [
        html.Img(
            src=f'{pic_path}',
            className='w-100'
        ),
        html.P(
            'This is a short bio about me, maybe?'
        ),
        html.Div(links, className='d-md-block d-none mb-3'),
        html.Div(
            [
                html.I(className='fas fa-envelope me-2'),
                'bericks @ ncsu.edu'
            ]
        ),
        html.Div(
            [
                html.I(className='fab fa-github me-2'),
                html.A(
                    [
                        'Github'
                    ],
                    href='https://github.com/bradley-erickson',
                    target='_blank'
                )
            ]
        ),
        # html.Div(
        #     html.A(
        #         [
        #             html.I(className='fas fa-graduation-cap me-2'),
        #             'Google Scholar'
        #         ],
        #         href='https://github.com/bradley-erickson',
        #         target='_blank'
        #     )
        # ),
    ],
    class_name='border-0',
    body=True
)
