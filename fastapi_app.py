from fastapi import FastAPI
from pydantic import BaseModel

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

@app.post("/greet")
def greet_person_post(request: GreetRequest):
    return {"message" : f"Hello, {request.name}! You are {request.age} years old."}


