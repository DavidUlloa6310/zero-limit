from zero_limit.models import location
from flask import render_template
from zero_limit import app

@app.route('/home')
@app.route('/')
def home():
    return render_template('index.html', title='Zer0-Limit')

@app.route('/store')
def store():
    return render_template('store.html', location = location)

@app.route('/about')
def about():
    return render_template('about.html')