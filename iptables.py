# save this as app.py
from flask import Flask
from flask import render_template
from flask import jsonify 
import json 

app = Flask(__name__)



@app.route("/")
def start():
    return render_template("start.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("rules_filter.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("rules_nat.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("rules_nat_add.html")

@app.route("/alias")
def affiche_json():
    f = open('static/alias.json')
    data = json.load(f)
    print(data)
    f.close()
    return render_template("alias.html", data=data)
    

@app.route("/template")
def template():
    return render_template("template.html")