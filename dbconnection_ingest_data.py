import pandas as pd
import csv
import decimal
import datetime
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.2',
                              database='carbon_emission_db')

print (cnx)

cursor = cnx.cursor

sql = "CREATE DATABASE carbon_emission_db"

cursor.execute(sql)

sql2 = "CREATE TABLE product_emissions (pcf_id VARCHAR(25), year INTEGER, product_name VARCHAR(50), company VARCHAR(50), country VARCHAR(50), industry_group VARCHAR(50),weight_kg INTEGER, carbon_footprint_pcf INTEGER, upstream_percent_total_pcf VARCHAR(50), operations_percent_total_pcf VARCHAR(50), downstream_percent_total_pcf VARCHAR(50))"

cursor.execute(sql2)

cnx.commit()

cnx.close()

# defining logging options
import logging
import time
import mysql.connector

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

# Also log to a file
file_handler = logging.FileHandler("cpy-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 

def connect_to_mysql(config, attempts=3, delay=2):
    attempt = 1
    # Implement a reconnection routine
    while attempt < attempts + 1:
        try:
            return mysql.connector.connect(**config)
        except (mysql.connector.Error, IOError) as err:
            if (attempts is attempt):
                # Attempts to reconnect failed; returning None
                logger.info("Failed to connect, exiting without a connection: %s", err)
                return None
            logger.info(
                "Connection failed: %s. Retrying (%d/%d)...",
                err,
                attempt,
                attempts-1,
            )
            # progressive reconnect delay
            time.sleep(delay ** attempt)
            attempt += 1
    return None

# defining error options
import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root',
                                database='carbon_emissions_db')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
