from app.handler.handlers.base_handler import BaseHandler
from app.storage.storage_content.content import Content


class CreatePageHandler(BaseHandler):
    uri = '/create_page'

    def render_page(self, title="", content="", error=""):
        self.render('create_page.html')

    def get(self):
        return self.render_page()

    def post(self):
        title, content = self.get_attributes()
        if not title or not content:
            self.fail_to_submit(title, content)
        else:
            self.save_content(title, content)
            self.redirect('/')

    def get_attributes(self):
        title = self.request.get('title')
        content = self.request.get('content')
        return title, content

    def save_content(self):
        title = self.request.get('title')
        content = self.request.get('content')
        Content(title, content).put()

    def fail_to_submit(self, title, content, error):
        error_message = "please fill in both title and content"
        self.render_page(title=title, content=content, error=error_message)
