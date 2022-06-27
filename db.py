from flask import current_app, g
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


def get_db():
    if 'db' not in g:
        current_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/garden_companion'
        sqlalchemy = SQLAlchemy(current_app)
        Migrate(current_app, sqlalchemy)
        g.db = sqlalchemy

    return g.db
