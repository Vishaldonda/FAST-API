from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/",tags=["Home"])
def func():
    return {"sssss":"ds"}

@app.get("/items/{id}")
def get_id(id : int,q:str | None = None):
    return {"item_id": id,"q":q}

class Item(BaseModel):
    name :str

@app.post("/items/")
def create_item(name:Item):
    return {"message":f"Item '{name}' created successfully"}

