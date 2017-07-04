from common.singleton import Singleton
from handlers.main_page_handler import MainPageHandler


class HandlerManager:
    __metaclass__ = Singleton

    def __init__(self):
        self.routes = self.get_routes()

    def get_routes(self):
        routes = []
        self.add_main_page_handler(routes)
        return routes

    def add_main_page_handler(self, routes):
        main_handler = MainPageHandler()
        uri = main_handler.uri
        routes.append((main_handler, uri))
