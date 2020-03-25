import os
from flask import Flask
from application.models import db

def create_db():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return None

if __name__ == '__main__':
    create_db()