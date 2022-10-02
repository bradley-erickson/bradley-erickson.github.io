# package imports
from dash import html
import dash_bootstrap_components as dbc
import json
import os

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'projects.json')
with open(file_path_in, 'r') as f:
    data = json.load(f)

def create_proj_info(proj):
    start = proj.get('start_date')
    end = proj.get('end_date', 'present')
    timeline = f'{start} - {end}' if start != end else start
    title =  html.A(
        proj.get('title'),
        href=proj.get('link'),
        target='_blank'
    ) if proj.get('link', False) else proj.get('title')
    card = dbc.Card(
        [
            html.H4(title),
            html.Div(
                [
                    html.Div(timeline),
                    html.P(proj.get('description')),
                    html.Span(
                        [
                            dbc.Badge(
                                tag,
                                color='white',
                                text_color='dark',
                                class_name='border me-1'
                            ) for tag in proj.get('tags', [])
                        ]
                    )
                ],
                className='ms-3'
            )
        ],
        body=True,
        class_name='border-0'
    )
    return card


projects = []
for d in data:
    projects.append(create_proj_info(d))
    projects.append(html.Hr())
projects.pop()

id = 'projects'
layout = dbc.Card(
    [
        html.H2('Projects'),
        html.Div(
            projects
        )
    ],
    id=id,
    body=True,
)
