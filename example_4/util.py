# util.py

import psycopg2
from psycopg2 import Error

def connect_to_db(username='postgres', password='password', host='127.0.0.1', port='5432', database='db01'):
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        print("Connected to the database")
        return cursor, connection
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None, None

def disconnect_from_db(connection, cursor):
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
        print("Connection does not exist.")

def run_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        return True, None  # Success
    except (Exception, Error) as error:
        print("Error while executing the SQL command:", error)
        return False, str(error)

def run_and_fetch_sql(cursor, sql_string=""):
    try:
        cursor.execute(sql_string)
        record = cursor.fetchall()
        return True, record
    except (Exception, Error) as error:
        print("Error while fetching data:", error)
        return False, str(error)
