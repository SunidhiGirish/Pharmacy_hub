import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Chintu@2238',           # your MySQL password
        database='pharmacy_hubs' # your Workbench DB name
    )
