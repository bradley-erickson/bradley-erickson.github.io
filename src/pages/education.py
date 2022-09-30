# package imports
from dash import html
import dash_bootstrap_components as dbc

id = 'education'
layout = dbc.Card(
    [
        html.H2('Education'),
        dbc.Table(
            html.Tbody(
                [
                    html.Tr([html.Td(), html.Td()]),
                    html.Tr(
                        [
                            html.Td('2020 - '),
                            html.Td('PhD, Computer Science, North Carolina State University')
                        ]
                    ),
                    html.Tr(
                        [
                            html.Td('2016 - 2020'),
                            html.Td(
                                [
                                    html.Strong('Winona State University'),
                                    html.Br(),
                                    'Bachelor of Science, Computer Science',
                                    html.Br(),
                                    'Bachelor of Science, Data Science',
                                    html.Br(),
                                    'Bachelor of Art, Mathematics'
                                ]
                            )
                        ]
                    )
                ]
            )
        )
    ],
    id=id,
    body=True,
)
