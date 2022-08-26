#Python
from curses import noecho
from pickle import NONE
from types import NoneType
from typing import Optional
from unicodedata import name
from winreg import QueryInfoKey

#Pydantic
from pydantic import BaseModel

#OpenApi
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_colo: Optional[str] = NONE
    is_married: Optional[bool] = NONE 

@app.get("/")
def home():
    return {"Home":"My first OpenApi"}

# Request and response body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

# Validations Query Params

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    #age: Optional[int] = Query()
    age: str = Query(...) # como ejemplo se pide que sea obligatorio pero los qry params son opcionales
):
    return {name : age}