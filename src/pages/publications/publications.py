# package imports
from dash import html
import dash_bootstrap_components as dbc
from datetime import date
import os
import frontmatter
import platform

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'publications', 'papers')
date_format = '%B %#d, %G' if platform.system() == 'Windows' else '%B %-d, %G'


def create_publication_listing(pub):
    date_str = pub.get('date').strftime(date_format)
    card = dbc.Card(
        [
            html.H4(
                html.A(
                    pub.get('title'),
                    href=pub.get('link')
                )
            ),
            html.Div(f'{pub.get("venue")} - {date_str}'),
            html.Div(pub.get('author'))
        ],
        body=True,
        class_name='border-0'
    )
    return card


publications = []
publication_names = os.listdir(file_path_in)
publication_names.reverse()  # reverse the list so the article show up properly
year = None

for pub_name in publication_names:
    # read in contents of a given article
    pub_path = os.path.join(file_path_in, pub_name)
    with open(pub_path, 'r', encoding='utf-8') as f:
        pub = frontmatter.load(f)

    publish_date = pub.get('date')

    # skip articles that aren't published yet or are the sample files
    if publish_date > date.today() or pub_name.startswith('sample'):
        continue

    if publish_date.year != year:
        year = publish_date.year
        publications.append(html.H3(year))

    publications.append(create_publication_listing(pub))
    publications.append(html.Hr())
publications.pop()

layout = dbc.Card(
    [
        html.H2('Publications'),
        html.Div(
            publications
        )
    ],
    body=True,
    class_name='border-0'
)

publications_tab = dbc.Tab(
    layout,
    label='Publications'
)
