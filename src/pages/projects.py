# package imports
from dash import html
import dash_bootstrap_components as dbc
import math
import os
import pandas as pd

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'projects.csv')
df = pd.read_csv(file_path_in)
df.sort_values(['end_year', 'start_year'], ascending=False, inplace=True, na_position='first')


def create_project_listing(proj):
    start_year = proj.get('start_year')
    end_year = proj.get('end_year')
    if math.isnan(end_year):
        date_str = f'{start_year} - Present'
    elif start_year == end_year:
        date_str = start_year
    else:
        date_str = f'{start_year} - {end_year}'
    card = dbc.Card(
        [
            html.H4(
                html.A(
                    proj.get('name'),
                    href=proj.get('link'),
                    target='_blank'
                )
            ),
            html.Div(date_str),
            html.Div(proj.get('description'))
        ],
        body=True,
        class_name='border-0'
    )
    return card


projects = [html.H3('Ongoing')]
year = None
for _, proj in df.iterrows():

    start_year = proj.get('start_year')
    end_year = proj.get('end_year')      
    if start_year != year and not math.isnan(end_year):
        if year:
            projects.pop()
        year = start_year
        projects.append(html.H3(year))

    projects.append(create_project_listing(proj))
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
