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

#uvicorn main:app --reload
#Terminal command to run server with fast reload ON

@app.get("/")
async def home():
    return "PrimeEHR - The BEST electronic health record system"


@app.get("/patients")
def list_all_patients():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient; ")
    return cursor.fetchall()