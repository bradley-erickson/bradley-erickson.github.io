# package imports
import dash
from dash import html, dcc, clientside_callback, Output, Input
import dash_bootstrap_components as dbc
import json

# local imports
from pages import pages
from utils.page_converter import convert_layout


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.MINTY,
        dbc.icons.FONT_AWESOME,
        dbc_css
    ],
    title='Static Site',
    suppress_callback_exceptions=True
)

navbar = dbc.NavbarSimple(
    dbc.Container(
        [
            dbc.NavItem(
                dbc.NavLink(page['name'], href=page['path']),
                class_name='d-inline-block'
            ) for page in pages if len(page['path'].split('/')) < 3
        ]
    ),
    brand='Static Site',
    brand_href='/',
    color='primary',
    dark=True
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content'),
])


not_found = html.Div(
    [
        html.H1('Page not found'),
        html.A(
            'Return home',
            href='/'
        )
    ]
)

page_layouts = ''.join(
    [
        f'case "{page["path"]}":child={json.dumps(convert_layout(page["layout"]))};break;'
        for page in pages
    ]
)

clientside_callback(
    f"""
    function(path) {{
        switch (path) {{
            {page_layouts}
            default:
                child = {json.dumps(convert_layout(not_found))};
        }}
        return child
    }}
    """,
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

if __name__ == '__main__':
    app.run_server(debug=False)
