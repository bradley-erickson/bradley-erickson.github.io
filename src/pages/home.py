from dash import html

layout = html.Div(
    [
        html.H1('Home'),
        html.P('This is a home page')
    ]
)
page = {
    'path': '/',
    'layout': layout,
    'name': 'Home'
}
