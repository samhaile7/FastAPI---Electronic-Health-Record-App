from fastapi import FastAPI
import psycopg2
import json

app = FastAPI()

#Connection to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="emrapp",
    user="postgres",
    password="postgres1")

@app.get("api/patients")
def list_all_patients():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient; ")
    return cursor.fetchall()