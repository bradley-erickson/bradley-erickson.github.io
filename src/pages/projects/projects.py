# package imports
from dash import html
import dash_bootstrap_components as dbc
from datetime import date
import os
import frontmatter
import platform

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'projects', 'project_descriptions')
date_format = '%B %#d, %G' if platform.system() == 'Windows' else '%B %-d, %G'


def create_project_listing(pub):
    date_str = pub.get('date').strftime(date_format)
    card = dbc.Card(
        [
            html.H4(
                html.A(
                    pub.get('title'),
                    href=pub.get('link'),
                    target='_blank'
                )
            ),
            html.Div(f'{pub.get("venue")} - {date_str}'),
            html.Div(pub.get('author'))
        ],
        body=True,
        class_name='border-0'
    )
    return card


projects = []
project_names = os.listdir(file_path_in)
project_names.reverse()  # reverse the list so the article show up properly
year = None

for pub_name in project_names:
    # read in contents of a given article
    pub_path = os.path.join(file_path_in, pub_name)
    with open(pub_path, 'r', encoding='utf-8') as f:
        pub = frontmatter.load(f)

    publish_date = pub.get('date')

    # skip articles that aren't published yet or are the sample files
    if publish_date > date.today() or pub_name.startswith('sample'):
        continue

    if publish_date.year != year:
        if year:
            projects.pop()
        year = publish_date.year
        projects.append(html.H3(year))

    projects.append(create_project_listing(pub))
    projects.append(html.Hr())
projects.pop()

layout = dbc.Card(
    [
        html.H2('Projects'),
        html.Div(
            projects
        )
    ],
    body=True,
    class_name='border-0'
)

projects_tab = dbc.Tab(
    layout,
    label='Projects'
)
