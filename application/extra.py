from flask_marshmallow import Marshmallow
from flask_heroku import Heroku
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

def get_migrate(app, db):
    migrate = Migrate(app, db)
    return migrate

def get_manager(app):
    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return manager

def get_heroku(app):
    heroku = Heroku(app)
    return heroku

def get_ma(app):
    ma = Marshmallow(app)
    return ma