from base_handler import BaseHandler


class MainPageHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self, '/')

    def render_page(self):
        self.render('mainpage.html')

    def get(self):
        self.render_page()
