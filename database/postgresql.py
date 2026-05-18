import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="people_db",
    user="admin",
    password="password",
    port=5432
)

cursor = conn.cursor()
