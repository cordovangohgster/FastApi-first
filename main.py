# Python
from typing import Optional # Sirve para definir tipos de datos en python y volver a python como un lenguaje de programación estatico

#Pydantic
from pydantic import BaseModel # Sirve para definir los modelos de datos que se usaran en la aplicacion

# FastAPI
from fastapi import FastAPI  # Sirve para definir la API de la aplicacion
from fastapi import Body, Query, Path # Sirve para definir el tipo de dato que se usara en la API


app = FastAPI()

#models
class Location(BaseModel):
    city : str
    state: str
    country:str


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


# Validations: Request body parameters
@app.put("/person/{person_id}")
def show_person(
    person_id: int = '..., gt=0, title="Person id", description="then person id"',
    person: Person = Body(...),
    location: Location = Body(...)
):
    #Varias manera de concatenar dependiendo necesidad
    #result = Person.dic() #En version anterior que ya no funciona en esta
    #result.update(Location.dic())
    
    #result = dict(person) #junta todo en uno solo sin nodos
    #result.update(dict(location))
    #return result
    
    #return  {**dict(person),**dict(location)} #junta todo sin nodos como el anterior

    #return { #junta todo con los dos nodos por separado
    #    "person": person,
    #    "location": location
    #}

    return person.dict() | location.dict() #junta todo también

    
