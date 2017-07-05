import webapp2
from app.handler.router import Router


router = Router()
routes = router.routes
app = webapp2.WSGIApplication(routes, debug=True)
