from . import home, page1
from .blog import blog

pages = [home.page, page1.page, blog.page]
pages.extend(blog.articles)
