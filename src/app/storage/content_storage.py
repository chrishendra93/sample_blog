from app.common.singleton import Singleton
from app.storage.storage_content.content import Content
from google.appengine.ext import db


class ContentStorage:
    __metaclass__ = Singleton

    def load(self):
        contents = db.GqlQuery("SELECT * FROM Content ORDER BY created DESC")

    def save(self, title, content):
        content = Content(title, content)
        content.put()
