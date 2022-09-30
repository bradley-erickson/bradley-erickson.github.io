# package imports
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO

navbar = dbc.NavbarSimple(
    [
        ThemeSwitchAIO(aio_id="theme", themes=[dbc.themes.FLATLY, dbc.themes.DARKLY])
    ],
    brand='Bradley Erickson',
    brand_href='/',
    color='light'
)
