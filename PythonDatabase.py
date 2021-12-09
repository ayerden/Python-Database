import mysql.connector
from mysql.connector import Error
import pandas as pd


#A function to connect to our MySQL Server
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

def main():
    connection = create_server_connection("127.0.0.1", "root", "test")
    create_database_query = "CREATE DATABASE school"
    create_database(connection, create_database_query)

if __name__ == "__main__": 
    main()