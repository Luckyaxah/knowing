import os
import click

from apiflask import APIFlask  # step one
from knowing.settings import config
from knowing.blueprints.example import example_bp
from knowing.blueprints.auth import auth_bp
from knowing.blueprints.knowledge import knowledge_bp
from knowing.models import User
from knowing.extensions import db, migrate
import knowing.fakes as fakes

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = APIFlask('knowing')
    app.config.from_object(config[config_name])
    register_routes(app)
    register_blueprints(app)
    register_extensions(app)
    register_shell_context(app)
    register_commands(app)
    return app

def register_routes(app):
    @app.get('/')
    def say_hello():
        # returning a dict equals to use jsonify()
        return {'message': 'Hello!'}

def register_blueprints(app):
    app.register_blueprint(example_bp, url_prefix='/example')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(knowledge_bp, url_prefix='/knowledge')

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(
            db=db,
            User = User,
            fakes = fakes
            )

def register_commands(app):
    pass