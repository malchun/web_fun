import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient(
    host='db',
    port=27017)
db = client.tododb


@app.route('/')
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('test.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description'],
        'time': str(datetime.now().strftime("%A, %d %B %Y %I:%M%p"))
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
