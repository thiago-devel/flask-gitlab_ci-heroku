from application.shared import db, app
from application.extra import get_manager, get_migrate, get_heroku

manager = get_manager(app)
migrate = get_migrate(app, db)
heroku = get_heroku(app)

if __name__ == '__main__':
    manager.run()