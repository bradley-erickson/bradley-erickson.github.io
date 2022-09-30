# package imports
from dash import html
import dash_bootstrap_components as dbc
import os
import pandas as pd
import platform

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'papers.csv')
df = pd.read_csv(
    file_path_in,
    parse_dates=['date']
)
date_format = '%B %#d, %G' if platform.system() == 'Windows' else '%B %-d, %G'
df.sort_values('date', ascending=False, inplace=True)

def create_publication_listing(pub):
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

publications = []
year = None
for _, pub in df.iterrows():

    publish_date = pub.get('date')
    if publish_date.year != year:
        if year:
            publications.pop()
        year = publish_date.year
        publications.append(html.H3(year))

    publications.append(create_publication_listing(pub))
    publications.append(html.Hr())
publications.pop()

id = 'publications'
layout = dbc.Card(
    [
        html.H2('Publications'),
        html.Div(
            publications
        )
    ],
    id=id,
    body=True,
)
