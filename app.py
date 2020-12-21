
import pandas as pd
import os
import json
from datetime import date
from pprint import pprint

import requests
import csv

from flask import Flask, redirect, jsonify, render_template, url_for

import pandas as pd

import geopy.distance
import requests
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from api_keys import database_uri


## # Import database user and password
try:
    from api_keys import pg_host
    from api_keys import db_name
    from api_keys import pg_user
    from api_keys import pg_pass
except:
    pass


#Database name and database tables

table_airplanes = "aircraft_data"
airportData = "airportData"



# MySQL specific connection string

connection_string = f"{pg_user}:{pg_pass}@{pg_host}/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')


# Query database for airport data that will be always the same

airport_db = db_name.find(airportData)

jsonpath = os.path.join("data","airports.json")
with open(jsonpath) as f:
    data = json.loads(f.read())
    # print(data[0]['text'])
# if isinstance(data, list):
#     db_name.insert(data)




#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
# Use Flask to create your routes.


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
    
       
        
# if __name__ == "__main__":
#     app.run(debug=True)



# Return a json with the query results for the aircrafts table
@app.route("/api/v1.0/aircrafts-data")
def api_aircrafts():
    # MySQL query to return all table elements that have not 
    # null latitute and have the newest time stamp
    aircraft_df = pd.read_sql(
        f"""
        SELECT
            * 
        FROM 
            {table_airplanes}
        WHERE 
            longitude IS NOT NULL
        AND 
            time = (SELECT MAX(time) 
        FROM 
            {table_airplanes})
        ORDER BY 
            id
        DESC;
        """,
         engine)

    result = aircraft_df.to_json(orient="records")
    parsed = json.loads(result)

    return jsonify(parsed)

# Return a json with the query results for the airports table
@app.route("/api/v1.0/airports-data/<country>")
def api_airports(country):

    if f"{country}" == 'ALL':
        airports_df = airportData
        
    else:
        airports_df = airports_df_all.loc[airportsDatal['Country']==f"{country}"]
    result = airports_df.to_json(orient="records")
    parsed = json.loads(result)

    return jsonify(parsed)

# Return a json with the query results for the aircrafts table for a specific icao24
@app.route("/api/v1.0/aircrafts-data/icao24/<icao24>")
def api_aircrafts_icao24():

    aircraft_df = pd.read_sql(
        f"""
        SELECT 
            *
        FROM
            {table_airplanes}
        WHERE
            longitude IS NOT NULL 
        AND
            icao24 = '{str(icao24)}';
        """,
         engine)

    result = aircraft_df.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)


# Return a json with the query results for the aircrafts table for a specific callsign
@app.route("/api/v1.0/aircrafts-data/callsign/<callsign>")
def api_aircrafts_callsign():

    aircraft_df = pd.read_sql(
        f"""
        SELECT 
            *
        FROM
            {table_airplanes}
        WHERE
            longitude IS NOT NULL
        AND
            callsign = '{str(callsign)}';
        """,
         engine)

    result = aircraft_df.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)


# Return a json with the query results for the aircrafts table for a specific callsign
@app.route("/api/v1.0/aircrafts-data/byhour")
def api_aircrafts_byhour():

    aircraft_hour = pd.read_sql(
        f"""
        SELECT 
            COUNT(*) AS totalDataPoints,
            FROM_UNIXTIME(time, '%Y-%m-%d %H') AS timeData
        FROM
            {table_airplanes}
        WHERE
            longitude IS NOT NULL
        GROUP BY FROM_UNIXTIME(time, '%Y-%m-%d %H');
        """,
         engine)

    result = aircraft_hour.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)

# The server is set to run on the computer IP address on the port 5100
# Go to your http://ipaddress:5100
if __name__ == "__main__":
    app.run(debug=True)

