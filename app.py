from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = 'app/news_aggregator.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    db = get_db()
    cur = db.execute('SELECT title, description, url FROM articles')
    articles = cur.fetchall()
    return render_template('home.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
