import psycopg2

mydb = psycopg2.connect(
    host="host.docker.internal",
    port="5432",
    user="postgres",
    password="password",
    database="DunderMifflin"
)
