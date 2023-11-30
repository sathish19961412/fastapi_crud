from fastapi import FastAPI
# from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Request(BaseModel):
     name:str
     age:int
     email:str

@app.post('/')
def index(request:Request):
    return{'data':request}