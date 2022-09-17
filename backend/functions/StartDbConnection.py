import psycopg2
import os

def startConnection():
    dbUrl = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(dbUrl)
    return conn
