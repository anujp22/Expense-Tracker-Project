import psycopg2
import os


def connect_to_db():
    try:
        conn = psycopg2.connect(
    dbname=os.environ.get("DB_name"),
    user=os.environ.get("DB_user"),
    password=os.environ.get("DB_password"),
    host=os.environ.get("DB_host_name"),
    port=os.environ.get("DB_port")
)
    except Exception as error:
        print("Unexpected error:", error)
    return conn

def close_db_connection(conn):
    if conn:
        conn.close()