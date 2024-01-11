import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor
cur = conn.cursor()

# Execute SQL queries

# Close the cursor and connection
cur.close()
conn.close()
