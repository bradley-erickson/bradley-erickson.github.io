# package imports
import dash
from dash import html, dcc, clientside_callback, Output, Input
import dash_bootstrap_components as dbc


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

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page1"', href='/page1'),
    html.Div(id='page-content')
])

page_1 = html.H1('Page 1').to_plotly_json()
home = html.H1('home').to_plotly_json()

clientside_callback(
    f"""
    function(path) {{
        switch (path) {{
            case "/page1":
                child = {page_1};
                break;
            default:
                child = {home};
        }}
        return child
    }}
    """,
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

if __name__ == '__main__':
    app.run_server(debug=False)
