from app.handler.handlers.base_handler import BaseHandler


class MainPageHandler(BaseHandler):
    uri = '/'

    def render_page(self):
        self.render('welcome.html')

    def get(self):
        self.render_page()
