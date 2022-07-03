from dash import html

import dash

dash.register_page(
    __name__,
    path='/page1'
)

layout = html.H1('Page 1')
