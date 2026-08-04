from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import sqlite3
import os
from dotenv import load_dotenv
from fastapi import Depends
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import Request
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()
API_KEY = os.getenv("MY_API_KEY")

app = FastAPI()

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
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

#@app.post("/greet")
#def greet_person_post(request: GreetRequest):
#    connection = sqlite3.connect("my_database.db")
#    cursor = connection.cursor()
#    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (request.name, request.age))
#    connection.commit()
#    connection.close()

#    return {"message": f"Hello, {request.name}! You've been saved to the database."}


#@app.post("/greet")
#def greet_person_post(request: GreetRequest, authorized: None = Depends(verify_api_key)):
#    return {"message": f"Hello, {request.name}!"}

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        logging.warning(f"Unauthorized access attempt with key: {x_api_key}")
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.post("/greet")
@limiter.limit("5/minute")
def greet_person_post(request: Request, greet_request: GreetRequest, authorized: None = Depends(verify_api_key)):
    logging.info(f"Greet request received for name={greet_request.name}, age={greet_request.age}")
    return {"message": f"Hello, {greet_request.name}!"}