import io
import sys
import csv
import os
import uuid
import csv
import json
import pymongo
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
from bson.json_util import dumps




# Use PyMongo to establish Mongo connection

# try:
#     uri = os.environ["MONGODB_URI"]
    



#Import database user and password




# Database name and database tables

 

# MySQL specific connection string



# Create the engine to connect to the database
###############################################
# Flask Setup
#################################################
conn = ['MONGO_URI']
client = pymongo(conn)

# Use PyMongo to establish Mongo connection

db = client.flight
flightData = db.flight
# cursor = collection.find({})
# with open('collection.json', 'w') as file:
#         file.write('[')
#         for document in cursor:
#             file.write(load(document))



# flight = mongo.db
# flightData = flight.create_collection


#################################################
# Flask Routes
#################################################
# Use Flask to create your routes.

# Route
# jsonpath = os.path.join("collection.json")
# with open(jsonpath, 'r') as datafile:
#     data = json.loads(datafile)
#     if isinstance(data, list):
#         flightData.insert_many(data)
#     else:
#         flightData.insert_one(data)



#################################################
# Flask Setup
#################################################
app = Flask(__name__)
# app.wsgi_app = ProxyFix(app.wsgi_app)


#################################################
# Flask Routes
#################################################
# Use Flask to create your routes.
@app.route('/users')
def users():
        user = db.flightData.find()
        resp = dumps(user)
        return resp

# Home page.
@app.route("/")
def index():
    return render_template("index_Josh_v5.html")
@app.route("/Josh")
def home():
    return render_template("index_Josh_v6.html")
@app.route("/api")
def api():
    return render_template("index_api.html")
@app.route("/radar")
def radar():
    return render_template("indexradar.html")
@app.route("/test")
def test():
    return render_template("index_Josh_v5.html")
@app.route("/weather")
def weather():
    return redirect('http://localhost:5001', code=301)

# Return the APIs route available
@app.route("/api/v1.0")
def airports_url():
    api_airports = ("data", "airports.json")
    
    list_records = []
    for records in api_airports:
        Data = list_records.append(records)
        
        parsed = json.dumps(Data)
        print(records)
        return jsonify(parsed)
    
# Return a json with the query results for the airports table
@app.route("/api/v1.0/airports-data")
def api_airports():
    api_airports = ("collection.json")
    
    list_records = []
    for records in api_airports:
        Data = list_records.append(records)
        
        parsed = json.dumps(Data)
        print(records)
        return jsonify(parsed)


# Return a json with the query results for the aircrafts table for a specific icao24
@app.route("/api/v1.0/flightData/icao24/<icao24>")
def api_aircrafts_icao24(icao24):

    # Create place holders records to insert into the table
                           
                    MongoStuff =       {"id"                   ,
                                        "icao24",
                                        "callsign",
                                        "origin_country",
                                        "time_position",
                                        "last_contact",
                                        "longitude",
                                        "latitude",
                                        "baro_altitude",
                                        "on_ground",
                                        "velocity",
                                        "true_track",
                                        "vertical_rate",
                                        "sensors",
                                        "geo_altitude",
                                        "squawk",
                                        "spi",
                                        "position_source",
                                        "time"}
           


# Save the record to the database
# single element at the time
def add_to_database(flight):
    try:
        # Add records to the database
        flight.execute(MongoStuff, flightData)

        # Commit changes to the database
        db.commit()

        # print('Record Added to DB')
    except:
        print('Error Saving to DB')



# Save the record to the database with
# multiple records at the same time
def add_many_database(flightData):
    try:
        # Add records to the database
        my_cursor.executemany(MongoStuff, data)

        # Commit changes to the database
        db.commit()

        print('Record Added to DB')
    except:
        print('Error Saving to DB')
        
if __name__ == "__main__":
    app.run(debug=True)

# try:
#     # Save config information.
#     url = "https://opensky-network.org/api/states/all?time=1458564121&icao24=3c6444"


#     # Build partial query URL
#     # query_url = f"{url}"

#     #  Perform a request for data
    
#     response = requests.get(url).json()
#     return response
#     list_records = []
#     # Test for null and strip spaces in case not null
#     for i in range(len(response["states"])):
#         aircraft_live_data = list(range(0,18))
#         if response["states"][i][0]:
#             aircraft_live_data[0] = response["states"][i][0].strip()
#         else:
#             aircraft_live_data[0] = response["states"][i][0]
#         if response["states"][i][1]:
#             aircraft_live_data[1] = response["states"][i][1].strip()
#         else:
#             aircraft_live_data[1] =  response["states"][i][1]
#         if response["states"][i][2]:
#             aircraft_live_data[2] =  response["states"][i][2].strip()
#         else:
#             aircraft_live_data[2] =  response["states"][i][2]
#         aircraft_live_data[3] =  response["states"][i][3]
#         aircraft_live_data[4] =  response["states"][i][4]
#         aircraft_live_data[5] =  response["states"][i][5]
#         aircraft_live_data[6] =  response["states"][i][6]
#         aircraft_live_data[7] =  response["states"][i][7]
#         aircraft_live_data[8] =  response["states"][i][8]
#         aircraft_live_data[9] =  response["states"][i][9]
#         aircraft_live_data[10] =  response["states"][i][10]
#         aircraft_live_data[11] =  response["states"][i][11]
#         aircraft_live_data[12] =  response["states"][i][12]
#         aircraft_live_data[13] =  response["states"][i][13]
#         if response["states"][i][14]:
#             aircraft_live_data[14] =  response["states"][i][14].strip()
#         else:
#             aircraft_live_data[14] =  response["states"][i][14]
#         aircraft_live_data[15] =  response["states"][i][15]
#         aircraft_live_data[16]  = response["states"][i][16]
#         aircraft_live_data[17] = response["time"]

#         record1 = (aircraft_live_data[0], 
#                     aircraft_live_data[1],
#                     aircraft_live_data[2],
#                     aircraft_live_data[3],
#                     aircraft_live_data[4],
#                     aircraft_live_data[5],
#                     aircraft_live_data[6],
#                     aircraft_live_data[7],
#                     aircraft_live_data[8],
#                     aircraft_live_data[9],
#                     aircraft_live_data[10],
#                     aircraft_live_data[11],
#                     aircraft_live_data[12],
#                     aircraft_live_data[13],
#                     aircraft_live_data[14],
#                     aircraft_live_data[15],
#                     aircraft_live_data[16],
#                     aircraft_live_data[17]
#                     )
#         list_records.append(record1)
    
#     print("---------------------")
#     dt_object = datetime.fromtimestamp(response["time"])
#     print(f"At: {dt_object} | Total data points retrieved: {len(response['states'])}")


# except:
#     print("Failed to retrieve data")

# Return a json with the query results for the aircrafts table for a specific callsign
# @app.route("/api/v1.0/aircrafts-data/callsign/<callsign>")
# def api_aircrafts_callsign(callsign):

    # list_records = []
    # for records in collection:
    # Data = list_records.append(records)
        
        
    # parsed = json.dumps(Data)
    # print(records)
    # return jsonify(parsed)




# The server is set to run on the computer IP address on the port 5100
# Go to your http://ipaddress:5100
