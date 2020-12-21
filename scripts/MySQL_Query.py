
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
from MySQL_Add import add_to_database, add_many_database

#Function to connect to the MySQL database and add one record to the database """
pg_user = 'postgres'
pg_password = '$objbml'
db_name = 'project_2'

# connection_string = f"{pg_user}:{pg_password}@localhost:5432/{db_name}"
# engine = create_engine(f'postgresql://{connection_string}')

mydb = (f"{pg_user}:{pg_password}@localhost:5432/{db_name}")
engine = f'postgresql://{mydb}'


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
# def database_connect(engine:
    # mydb = mysql.connector.connect(
    #     host=hostname,
    #     user=username,
    #     passwd=password,
    #     database=database
    # )
    

# Return an object containing the MYSQL connection
# mydb = database_connect(
#     config("MYSQL_HOSTNAME"),
#     config("MYSQL_USERNAME"),
#     config("MYSQL_PASSWORD")
#     )
# print(mydb)

# Create the cursor to manipute databases
# my_cursor = .cursor()
# def database_connect():
    
#      = session.query(f"SELECT * FROM {db_name}.{table_name} ORDER BY id DESC LIMIT 1;")
#     session = Session(mydb)
#     for records in my_cursor:
        
# import database_credentials as dbkeys

# # Create a function to connect to the MYSQL server
# def database_connect(hostname, username, password, database=database_name):
#     my_cursor = mydb.cursor()
#     mydb = mysql.connector.connect(
#         host=hostname,
#         user=username,
#         passwd=password,
#         database=database
#     )
#     return mydb

# # Return an object containing the MYSQL connection
# # mydb = database_connect(
# #     "MYSQL_HOSTNAME",
# #     "MYSQL_USERNAME",
# #     "MYSQL_PASSWORD"
    
    

# # Create the cursor to manipute databases



# # Retrieve data and convert the tuples to a list
def database_connect():
    my_cursor = mydb.cursor()
    my_cursor.execute(f"SELECT * FROM {db_name}.{table_name} ORDER BY id DESC LIMIT 5;")
    results = (f"SELECT * FROM {db_name}.{table_name}")
    # records = results[0]
    for records in results:
        records.append(records)
        print(records)
        print(records[0])
# Convert tuples from database to dataframe
    records = []
    mydb = pd.df(records, columns = [
                                    "id",
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
                                     "position_source"]
                 )

# Set the index to the primary key of the database
# records.set_index('id',inplace=True)
# my_cursor = mydb.cursor()
# Convert the dataframe to dictionary
result_dict = mydb.insert(orient='records')

print(result_dict)