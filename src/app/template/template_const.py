import os
import jinja2

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
MAIN_PAGE = os.path.join(TEMPLATE_DIR, 'mainpage.html')
JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader
                               (TEMPLATE_DIR), autoescape=True)
