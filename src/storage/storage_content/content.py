from google.appengine.ext import db

class Content(db.Model):
	title = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
