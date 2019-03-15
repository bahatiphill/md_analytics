import os
from flask import Flask
from app.settings import ProdConfig


def create_app(config_object=ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return '<h1> welcome to Social Media analytic tool</h1>'

    return app