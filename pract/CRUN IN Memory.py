# Crud Operation API - In Memory

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lst = []
@app.get("/items/")
def get_items():
    return lst

class Item(BaseModel):
    id : int
    name:str

@app.post("/items/")
def post_items(item:Item):
    if item:
        lst.append({item.id:item.name})
        return {"id":item.id,"message": f"{item.name} added successfully!"}
    else:
        return {"id":{item.id},"message": "No valid parameters"}
    
@app.put("/items/{id}/")
def put_items(id:int,item:Item):
    for data in lst:
        if data["id"] == id:
            data[id] = item.name
            return {"message":f"Updated the data {item.id} to {item.name}"}
    
    return {"message" : "Item Not Found"}

@app.delete("/items/{id}") 
def delete_item(id:int):
    for data in lst:
        if id in data:
            lst.remove(data)
            return {"message": f"Item with id {id} deleted successfully!"}
    return {"message": "Item Not Found"}



#-------------------------------------------------------------------------------


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lst = []
@app.get("/items")
def get_items():
    return lst

class Item(BaseModel):
    id :int
    name : str

@app.post("/items")
def post_items(item:Item):
    lst.append({"id":item.id,"name":item.name})
    return {"message": f"{item.name} added successfully!"}

@app.put("/items/{id}")
def put_items(id:int,item:Item):
    for data in lst:
        if id == data["id"]:
            data["name"] = item.name
            return {"message" : "updated sucessfully"}
    
    return {"message" : "Item Not Found"}

@app.delete("/items/{id}") 
def delete_item(id:int):
    for data in lst:
        if id == data["id"]:
            lst.remove(data)
            return {"message": f"Item with id {id} deleted successfully!"}
    return {"message": "Item Not Found"}
