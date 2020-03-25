from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import Blueprint
from flask import jsonify

app_views = Blueprint('app_views', __name__)

@app_views.route('/')
def index():
    return jsonify({'message': 'ok'}), 200