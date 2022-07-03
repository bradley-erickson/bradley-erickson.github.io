# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[
        dbc.themes.MINTY,
        dbc.icons.FONT_AWESOME,
        dbc_css
    ],
    title='Static Site',
    suppress_callback_exceptions=True
)

def serve_layout():

    navitems = [
        dbc.NavItem(
            dbc.NavLink(
                page['name'],
                href=page['path'],
                class_name='text-light'
            )
        ) for page in dash.page_registry.values()
        if page['module'] != 'pages.not_found_404'
    ]
    navitems.insert(
        0,
        dbc.NavbarBrand(
            'Static Site',
            href='/'
        )
    )

    return html.Div(
        [
            dbc.Navbar(
                dbc.Container(
                    navitems
                ),
                sticky='fixed',
                color='primary',
                dark=True
            ),
            dbc.Container(
                dash.page_container,
                class_name='my-2'
            )
        ],
        className='dbc'
    )

app.layout = serve_layout

if __name__ == '__main__':
    app.run_server(debug=True)
