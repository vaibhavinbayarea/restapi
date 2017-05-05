from flask import Flask, Blueprint
from flask_restplus import Resource, Api
from restapi.api.restplus import api
from restapi.api.blog.endpoints.categories import ns as blog_categories_namespace
from restapi.database import db


app = Flask(__name__)


def initialize_app(flask_app):
    # configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(blog_categories_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)


def main():
    initialize_app(app)
    app.run()


if __name__ == '__main__':
    main()
