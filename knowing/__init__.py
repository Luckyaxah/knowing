import os

from apiflask import APIFlask  # step one
from knowing.settings import config
from knowing.blueprints.example import example_bp


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = APIFlask('knowing')
    app.config.from_object(config[config_name])
    register_routes(app)
    register_blueprints(app)
    return app

def register_routes(app):
    @app.get('/')
    def say_hello():
        # returning a dict equals to use jsonify()
        return {'message': 'Hello!'}

def register_blueprints(app):
    app.register_blueprint(example_bp, url_prefix='/example')
