# package imports
import dash
from dash import html, clientside_callback, Output, Input
import dash_bootstrap_components as dbc

# local imports
from pages import home, publications, education, projects
from components import navbar, sidebar


dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.FLATLY,
        dbc.icons.FONT_AWESOME,
        dbc_css
    ],
    title='Bradley Erickson',
    suppress_callback_exceptions=True
)

app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            dbc.Row(
                [
                    dbc.Col(
                        sidebar,
                        md=4,
                        lg=3
                    ),
                    dbc.Col(
                        [
                            home.layout,
                            publications.layout,
                            education.layout,
                            projects.layout
                        ],
                        md=8,
                        lg=9
                    )
                ]
            )
        ),
    ]
)

clientside_callback(
    """
    function(hash) {
        let a = Array(4).fill('d-none');
        const class_name = 'section-card';
        console.log(a);
        if (hash === '#publications') {
            a[1] = class_name;
        } else if (hash === '#education') {
            a[2] = class_name;
        } else if (hash === '#projects') {
            a[3] = class_name;
        } else {
            a[0] = class_name;
        }
        console.log(a);

        return a
    }
    """,
    Output(home.id, 'class_name'),
    Output(publications.id, 'class_name'),
    Output(education.id, 'class_name'),
    Output(projects.id, 'class_name'),
    Input('location', 'hash')
)

if __name__ == '__main__':
    app.run_server(debug=True)
