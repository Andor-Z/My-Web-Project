from config import config
from flask import Flask
# from flask import render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
# from flask.ext.bootstrap import Bootstrap
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.moment import Moment


bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # config[config_name].init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
