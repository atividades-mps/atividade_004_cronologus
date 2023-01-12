import sqlite3

from flask import g

DATABASE = "db/cronologusdb.db"
DATABASE_INIT_FILE = "db/init.sql"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db(app):
    with app.app_context():
        db = get_db()
        with app.open_resource(DATABASE_INIT_FILE, mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()