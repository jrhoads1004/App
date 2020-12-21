import requests
import time
from datetime import datetime
import json
from flask import Flask, jsonify, render_template, url_for
from sqlalchemy import create_engine
import pandas as pd
import os
import json
import geopy.distance
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from api_keys import database_uri
#from MySQL_Add import add_to_database, add_many_database

pg_user = 'postgres'
pg_password = '$objbml'
db_name = 'project_2'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

Base = automap_base()
Base.prepare(engine, reflect=False)
Base.classes.keys()


table_name = "aircraft_data"


""" Query the live aircraft data from Opensky API  
and add record to the MySQL database """
try:
    # Save config information.
    url = "https://opensky-network.org/api/states/all"

    # Build partial query URL
    query_url = f"{url}"

    #  Perform a request for data
    response = requests.get(query_url).json()

    list_records = []
    # Test for null and strip spaces in case not null
    for i in range(len(response["states"])):
        aircraft_live_data = list(range(0,18))
        if response["states"][i][0]:
            aircraft_live_data[0] = response["states"][i][0].strip()
        else:
            aircraft_live_data[0] = response["states"][i][0]
        if response["states"][i][1]:
            aircraft_live_data[1] = response["states"][i][1].strip()
        else:
            aircraft_live_data[1] =  response["states"][i][1]
        if response["states"][i][2]:
            aircraft_live_data[2] =  response["states"][i][2].strip()
        else:
            aircraft_live_data[2] =  response["states"][i][2]
        aircraft_live_data[3] =  response["states"][i][3]
        aircraft_live_data[4] =  response["states"][i][4]
        aircraft_live_data[5] =  response["states"][i][5]
        aircraft_live_data[6] =  response["states"][i][6]
        aircraft_live_data[7] =  response["states"][i][7]
        aircraft_live_data[8] =  response["states"][i][8]
        aircraft_live_data[9] =  response["states"][i][9]
        aircraft_live_data[10] =  response["states"][i][10]
        aircraft_live_data[11] =  response["states"][i][11]
        aircraft_live_data[12] =  response["states"][i][12]
        aircraft_live_data[13] =  response["states"][i][13]
        if response["states"][i][14]:
            aircraft_live_data[14] =  response["states"][i][14].strip()
        else:
            aircraft_live_data[14] =  response["states"][i][14]
        aircraft_live_data[15] =  response["states"][i][15]
        aircraft_live_data[16]  = response["states"][i][16]
        aircraft_live_data[17] = response["time"]

        records = (aircraft_live_data[0], 
                    aircraft_live_data[1],
                    aircraft_live_data[2],
                    aircraft_live_data[3],
                    aircraft_live_data[4],
                    aircraft_live_data[5],
                    aircraft_live_data[6],
                    aircraft_live_data[7],
                    aircraft_live_data[8],
                    aircraft_live_data[9],
                    aircraft_live_data[10],
                    aircraft_live_data[11],
                    aircraft_live_data[12],
                    aircraft_live_data[13],
                    aircraft_live_data[14],
                    aircraft_live_data[15],
                    aircraft_live_data[16],
                    aircraft_live_data[17]
                    )

                    # add_to_database(record1)

        # create a list of tuples to be added to the database
        
    def database_connect():
        my_cursor = engine.cursor()
        session = my_cursor(engine)
        results = session.query(f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1;")
        for records in results:
            print(records)
            print(records[0])
            list_records.append(records)

    # add multiple records to the database at the same time
        
        aircraft_live_data.append(list_records)
    


    print("---------------------")
    dt_object = datetime.fromtimestamp(response["time"])
    print(f"At: {dt_object} | Total data points retrieved: {len(response['states'])}")


except:
    print("Failed to retrieve data")
