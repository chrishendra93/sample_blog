from app.common.singleton import Singleton
from app.handler.handlers.main_page_handler import MainPageHandler
from app.handler.handlers.create_page_handler import CreatePageHandler


class Router:
    __metaclass__ = Singleton

    def __init__(self):
        self.routes = self.get_routes()

    def get_routes(self):
        routes = []
        self.add_main_page_handler(routes)
        self.add_create_page_handler(routes)
        return routes

    def add_main_page_handler(self, routes):
        routes.append((MainPageHandler.uri, MainPageHandler))

    def add_create_page_handler(self, routes):
        routes.append((CreatePageHandler.uri, CreatePageHandler))
