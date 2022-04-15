import tornado
from tornado.web import Application
from tornado.httpserver import HTTPServer
from tornado.options import define, options
from tornado_sqlalchemy import SQLAlchemy

from .urls import urlpatterns
from .settings import settings
from .models import db

define('port',default=8888,help='host port')
define("debug", default=True, help="run in debug mode")

def make_app():
    return Application(
        handlers=urlpatterns,
        db = db,
        **settings
    )


app = HTTPServer(make_app())
app.listen(options.port)
tornado.ioloop.IOLoop.current().start()