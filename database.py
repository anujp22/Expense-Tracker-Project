import psycopg2
import os
conn = None
cur = None
try:
    conn = psycopg2.connect(
    dbname=os.environ.get("DB_name"),
    user=os.environ.get("DB_user"),
    password=os.environ.get("DB_password"),
    host=os.environ.get("DB_host"),
    port=os.environ.get("DB_port")
)
    cur = conn.cursor()
    
    create_script = '''
    '''
except Exception as error:
        print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

