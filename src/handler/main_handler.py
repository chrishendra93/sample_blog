from base_handler import BaseHandler


class MainHandler(BaseHandler):
    def render_page(self):
        self.render('mainpage.html')

    def get(self):
        self.render_page()
