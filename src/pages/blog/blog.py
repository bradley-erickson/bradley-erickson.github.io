# package imports
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from datetime import date
import os
import frontmatter
import platform

# set file location
cwd = os.getcwd()
file_path_in = os.path.join(cwd, 'pages', 'blog', 'articles')
date_format = '%B %#d, %G' if platform.system() == 'Windows' else '%B %-d, %G'


def create_article_card(post):
    '''Create clickable card to navigate to the article'''
    date_str = post.get('date').strftime(date_format)
    card = dbc.Card(
        html.A(
            [
                dbc.CardImg(src=f'{post.get("image")}', top=True),
                dbc.CardBody(
                    [
                        html.H4(
                            f'{post.get("title")}',
                            className='card-title'
                        ),
                        html.P(
                            f'{post.get("description")}',
                            className='card-text'
                        )
                    ]
                ),
                dbc.CardFooter(
                    f'{post.get("author")} - {date_str}',
                    class_name='mb-0'
                )
            ],
            href=post.get('permalink'),
            className='text-decoration-none text-body h-100 d-flex flex-column align-items-stretch'
        ),
        class_name='article-card h-100'
    )
    return card


def create_article_page(post):
    '''Create the layout of the article page'''
    date_str = post.get('date').strftime(date_format)

    image = post.get("image")
    layout = html.Div(
        dbc.Row(
            dbc.Col(
                [
                    html.Img(
                        src=f'{image}',
                        className='w-100'
                    ),
                    html.H1(f'{post.get("title")}'),
                    html.Hr(),
                    html.P(f'{post.get("author")} - {date_str}'),
                    html.Hr(),
                    dcc.Markdown(
                        post.content,
                        className='markdown'
                    )
                ],
                lg=10,
                xl=8
            )
        ),
        className='mb-4'
    )
    return layout


# iterate over items in article page
articles = []
article_cards = []
article_files = os.listdir(file_path_in)
article_files.reverse()  # reverse the list so the article show up properly

for article_name in article_files:
    # read in contents of a given article
    article_path = os.path.join(file_path_in, article_name)
    with open(article_path, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)

    publish_date = post.get('date')

    # skip articles that aren't published yet or are the sample files
    if publish_date > date.today() or article_name.startswith('sample'):
        continue

    # register the specific page for the article
    page = {
        'path': post.get("permalink"),
        'layout': create_article_page(post),
        'name': post.get("title")
    }
    articles.append(page)
    # create the article card and add it to the list of cards
    article_cards.append(create_article_card(post))


layout = html.Div(
    [
        html.H2('Blog section'),
        dbc.Row(
            [
                dbc.Col(
                    c,
                    md=6,
                    lg=4,
                    align='stretch'
                ) for c in article_cards
            ],
            class_name='g-3 my-1'
        )
    ]
)

page = {
    'path': '/blog',
    'layout': layout,
    'name': 'Blog'
}
