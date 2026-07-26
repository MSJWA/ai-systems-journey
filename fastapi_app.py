from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world"}

@app.get("/greet/{name}")
def greet_person(name: str):
    return {"message": f"Hello, {name}!"}

class GreetRequest(BaseModel):
    name : str
    age: int

#@app.post("/greet")
#def greet_person_post(request: GreetRequest):
#    return {"message" : f"Hello, {request.name}! You are {request.age} years old."}

@app.post("/greet")
def greet_person_post(request: GreetRequest):
    connection = sqlite3.connect("my_database.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (request.name, request.age))
    connection.commit()
    connection.close()

    return {"message": f"Hello, {request.name}! You've been saved to the database."}
