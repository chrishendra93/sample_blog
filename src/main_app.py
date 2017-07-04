import webapp2
from storage.content_storage import ContentStorage
from handler.handler_manager import HandlerManager


class MainApp:
    def __init__(self):
        self.content_storage = ContentStorage()
        self.HandlerManager = HandlerManager()
        self.app = webapp2.WSGIApplication(routes=HandlerManager.get_routes(),
                                           debug=True)

    def run(self):
        self.app.run()
