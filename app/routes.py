from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Hugo Hadden')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', title='Contacts')