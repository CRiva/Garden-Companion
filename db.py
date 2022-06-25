from flask import current_app, g
from flask.cli import with_appcontext
from flask_pymongo import PyMongo


def get_db():
    if 'db' not in g:
        current_app.config['MONGO_URI'] = "mongodb://localhost:27017/companion_planting"
        g.db = PyMongo(current_app)

    return g.db
