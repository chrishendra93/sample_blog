import webapp2
from template.jinja_env import JinjaEnv


class BaseHandler(webapp2.RequestHandler):
    def __init__(self, uri=""):
        self.uri = uri
        self.jinja_env = JinjaEnv()

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        return self.jinja_env.render(template, params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
