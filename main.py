#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

app = FastAPI()

#models

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_colo: Optional[str] = None
    is_married: Optional[bool] = None 

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
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50,
        title="Person Name", # solo para documentación
        Description="The person name" # solo para documentación
        ),
    #age: Optional[int] = Query()
    age: str = Query(
        ..., 
        title="Person Age", 
        description="The age of the person"
        ) # como ejemplo se pide que sea obligatorio pero los qry params son opcionales
):
    return {name : age}

# vAlidations path parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = '..., gt=0'
):
    return {person_id : "it exits"}
