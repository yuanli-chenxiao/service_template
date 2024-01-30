from flask import Flask

from mainapp.routes import test_route


def init(flask_app: Flask):
    flask_app.register_blueprint(test_route.bp, url_prefix="/api/test")
