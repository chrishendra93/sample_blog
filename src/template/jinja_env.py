import jinja2
from common.singleton import Singleton
from template_const import TEMPLATE_DIR


class JinjaEnv(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.template_dir = TEMPLATE_DIR
        self.jinja_env = jinja2.Environment(loader=jinja2
                                            .FileSystemLoader(TEMPLATE_DIR),
                                            autoescape=True)

    def render(self, template, **params):
        t = self.jinja_env.get_template(template)
        return t.render(params)
