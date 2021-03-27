import psycopg2

mydb = psycopg2.connect(
    host="localhost",
    port="5432",
    user="postgres",
    password="password",
    database="DunderMifflin"
)
