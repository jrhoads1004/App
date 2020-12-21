
import json
from flask import Flask, jsonify, render_template, url_for
from sqlalchemy import create_engine
import pandas as pd
import os
import json
import geopy.distance
import requests
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
from api_keys import database_uri
from Opensky_API_Data import database_connect

#Function to connect to the MySQL database and add one record to the database """
pg_user = 'postgres'
pg_password = '$objbml'
db_name = 'project_2'

connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
engine = create_engine(f'postgresql://{connection_string}')

Base = automap_base()
Base.prepare(engine, reflect=False)
Base.classes.keys()

# aircraft_Data = Base.classes.aircraft_data
# airport_Data = Base.classes.airport_data
# Database variables:
# database_name = "project_2"  # the name of the target database
table_name = "aircraft_data"

# import database_credentials as dbkeys
# with open("api_keys.py") as config_file:
#     config = json.load(config_file)

# Create a function to connect to the MYSQL server
# def database_connect():
mydb = (f"{pg_user}:{pg_password}@localhost:5432/{db_name}")
engine = f'postgresql://{mydb}'

       
    
    

# Return an object containing the MYSQL connection
# mydb = database_connect(
#     config("MYSQL_HOSTNAME"),
#     config("MYSQL_USERNAME"),
#     config("MYSQL_PASSWORD")
#     )
# print(mydb)

# Create the cursor to manipute databases

def database_connect(engine):
    my_cursor = mydb.cursor()
    session = my_cursor(engine)
    results = session.query(f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT 1;")
    for records in results:
        print(records)
        print(records[0])


# Create place holders records to insert into the table
sqlStuff = f"""INSERT INTO {table_name} (icao24, 
                                        callsign,
                                        origin_country,
                                        time_position,
                                        last_contact,
                                        longitude,
                                        latitude,
                                        baro_altitude,
                                        on_ground,
                                        velocity,
                                        true_track,
                                        vertical_rate,
                                        sensors,
                                        geo_altitude,
                                        squawk,
                                        spi,
                                        position_source,
                                        time)"""
            # VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """


# Save the record to the database 
# single element at the time
def add_to_database():
    try:
        # Add records to the database
        my_cursor = mydb.cursor()
        #session = my_cursor(engine)
        my_cursor.insert(sqlStuff)

        # Commit changes to the database
        my_cursor.commit()

        print('Record Added to DB')
    except:
        print('Error Saving to DB')



# Save the record to the database with 
# multiple records at the same time
def add_many_database():
    try:
        my_cursor = mydb.cursor()
        # Add records to the database
        my_cursor.insert_many(sqlStuff)

        # Commit changes to the database
        my_cursor.commit()

        print('Record Added to DB')
    except:
        print('Error Saving to DB')