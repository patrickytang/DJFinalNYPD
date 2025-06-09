# flask --app data_server run
from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/data.json", "r")
    dater = json.load(f)
    f.close()
    return render_template('index.html', data=dater)


@app.route('/about')
def year():
    return render_template('about.html')

@app.route('/borough')
def yurr():
    print(isinstance(request.args["borough"],str))
    f = open("data/data.json", "r")

    dater = json.load(f)
    f.close()
    return render_template('micro.html',borough = request.args["borough"],data=dater)
app.run(debug=True)
