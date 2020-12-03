import io
import os
import uuid
import json
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import pymongo
import flask_pymongo
from flask_pymongo import PyMongo
from pymongo import MongoClient
from pprint import pprint
import datetime
import flask
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app=Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/flight")


#create flight_data collection into flight_db


@app.route("/" )
def home():
    flightData = mongo.db.flightData
    return render_template("index.html", flightData=flightData)
    
def javascript_data():
    jsdata = request.form['flightData']
    unique_id = create_csv(jsdata)
    params = { 'uuid' : unique_id }
    return params

def create_csv(text):
    unique_id = str(uuid.uuid4())
    with open('images/'+unique_id+'.csv', 'a') as file:
        file.write(text[1:-1]+"\n")
    return unique_id    

def get_file_content(uuid):
    with open(uuid+'.csv', 'r') as file:
        return file.read()
    

    return redirect("/", code=302)

if __name__=="__main__":
    app.run(debug=True)
#Update results (insert or append if existing)
    #flight_data.update({},flight_results, upsert=True)
    
    #Save data into a listing
    

    #Render results into html
    #return render_template("index.html", mars_data=mars_data)


