import io
import sys
import csv
import os
import uuid
import json
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
    redirect,)
import bson




app=Flask(__name__)

# Use PyMongo to establish Mongo connection

try:
    uri = os.environ["REDISCLOUD_URL"]
    
except KeyError:
    uri = "mongodb://localhost:27017/flight"

   
app.config["mongodb://default:e1OnS3VMKFdlTUc8XmYH6yZ3h6zEbYq3@redis-13330.c52.us-east-1-4.ec2.cloud.redislabs.com:13330"] = uri


mongo = PyMongo(app, uri)

# Call the Database and Collection
flight = mongo.db
flightCollection = flight.flightData

#loaded json to Mongo, json created from a df using pandas to clean a csv
jsonpath = os.path.join("data", "airports.json")
with open(jsonpath) as datafile:
    air_data = json.load(datafile)
    if isinstance(air_data, list):
        flightCollection.insert_many(air_data)
    else:
        flightCollection.insert_one(air_data)
        
jsonpathO = os.path.join("data", "Airport_Output.json")
with open(jsonpathO) as datafile:
    airportOut = json.load(datafile)
    if isinstance(airportOut, list):
        flightCollection.insert_many(airportOut)
    else:
        flightCollection.insert_one(airportOut)
        
@app.route("/")
def home():
    flightCollection = list(flight.db.find())
    return render_template("index.html", flightData=flightCollection)
        
# Dump json into Database
@app.route('/users')
def users():
    users = flight.find()
    resp = json.dumps(users)
    return resp

#Pull javascript Data to run with flask
@app.route('/data')
def get_javascript_data(json_from_csv):
    return json.loads(json_from_csv)[0]       


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