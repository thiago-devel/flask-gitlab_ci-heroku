import os
from flask import Flask
from application.models import db

def drop_db():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)

    with app.app_context():
        db.drop_all()

    return None

if __name__ == '__main__':
    drop_db()
