# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def year():
    return render_template('about.html')

@app.route('/borough')
def boro():
    return render_template('micro.html')
app.run(debug=True)
