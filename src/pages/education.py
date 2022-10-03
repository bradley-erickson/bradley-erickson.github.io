# package imports
from dash import html
import dash_bootstrap_components as dbc

id = 'education'
layout = dbc.Card(
    [
        html.H2('Education'),
        dbc.Card(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4('North Carolina State Univsersity'),
                            html.Div(
                                [
                                    html.Div('Anticipated Dec. 2022, Raleigh, NC'),
                                    html.Div('GPA: 3.92/4.0'),
                                    html.Strong('Masters of Computer Science'),
                                ],
                                className='ms-3'
                            )
                        ],
                        xs=8,
                        sm=8,
                        md=9,
                        lg=10,
                        xxl=10
                    ),
                    dbc.Col(
                        dbc.CardImg(
                            src='/assets/ncsu.png',
                            class_name='img-fluid rounded-start'
                        ),
                        xs=4,
                        sm=4,
                        md=3,
                        lg=2,
                        xxl=2
                    )
                ]
            ),
            class_name='border-0',
            body=True
        ),
        html.Hr(),
        dbc.Card(
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4('Winona State Univserity'),
                            html.Div(
                                [
                                    html.Div('Class of May 2020, Winona, MN'),
                                    html.Strong('Bachelor of Science in Computer Science'),
                                    html.Br(),
                                    html.Strong('Bachelor of Science in Data Science'),
                                    html.Br(),
                                    html.Strong('Bachelor of Arts in Mathematics'),
                                    html.Div('Minor in Statistics')
                                ],
                                className='ms-3'
                            )
                        ],
                        xs=8,
                        sm=8,
                        md=9,
                        lg=10,
                        xxl=10
                    ),
                    dbc.Col(
                        dbc.CardImg(
                            src='/assets/wsu.png',
                            class_name='img-fluid rounded-start'
                        ),
                        xs=4,
                        sm=4,
                        md=3,
                        lg=2,
                        xxl=2
                    )
                ]
            ),
            class_name='border-0',
            body=True
        )
    ],
    id=id,
    body=True,
)
