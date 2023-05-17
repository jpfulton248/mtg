from flask import Flask
import datetime
import os
from models import db
from dotenv import load_dotenv

load_dotenv()

def create_app():
	app = Flask(__name__, instance_relative_config=True)
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.permanent_session_lifetime = datetime.timedelta(minutes=2)
	app.config['APP_ROOT'] = os.path.abspath(os.path.dirname(__file__))

	# register blueprints
	register_blueprints(app)
	db.init_app(app)
	return app

#helper functions
def register_blueprints(app):
	from app.crud.routes import crud
	app.register_blueprint(crud)