from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import  Manager
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from config import config


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)