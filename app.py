from flask import Flask, render_template, request, redirect, Response, send_file, abort
import datetime
import json
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    data = get_static_json("static/assets/json/data_projects.json")['projects']
    for i in data:
        print("Data =  ",i)
    return render_template('index.html', projects = data)

@app.route('/portfolio-detail')
def projects():
    data = get_static_json("static/assets/json/data_projects.json")['projects']
    return render_template("portfolio-details.html", projects=data)

@app.route('/portfolio-detail/<id>')
def project(id):
    data = get_static_json("static/assets/json/data_projects.json")['projects']
    
    selected = next((p for p in data if p['id'] == id), None)
    print(selected)
    return render_template("portfolio-details.html", project = selected)

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)

def get_static_json(path):
    return json.load(open(get_static_file(path)))

if __name__ == "__main__":
    print("running py app") 
    app.run(port=4000 , debug=True)