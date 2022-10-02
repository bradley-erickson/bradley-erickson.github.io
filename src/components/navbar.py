# package imports
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

links = html.Span(
    [
        dbc.NavLink('Home', href='/'),
        dbc.NavLink('Education', href='#education'),
        dbc.NavLink('Experience', href='#experience'),
        dbc.NavLink('Projects', href='#projects'),
        dbc.NavLink('Publications', href='#publications'),
        dbc.NavLink(
            [
                html.I(className='fab fa-github'),
                html.Span(
                    'Github',
                    className='d-md-inline d-none ms-1'
                )
            ],
            href='https://github.com/bradley-erickson',
            target='_blank'
        )
        # google scholar?
    ]
)

navbar = dbc.NavbarSimple(
    [
        dcc.Location(id='location'),
        ThemeSwitchAIO(aio_id='theme', themes=[dbc.themes.FLATLY, dbc.themes.DARKLY]),
        html.Div(links, className='d-md-none')
    ],
    brand='Bradley Erickson',
    brand_href='/',
    color='light'
)
