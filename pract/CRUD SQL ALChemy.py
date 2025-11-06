# Crud Operation API - MySQlite
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from fastapi import Depends 
from sqlalchemy.orm import Session  
import models

from database import Base, engine, get_db


app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/items/")
def get_items(db:Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

class Item(BaseModel):
    id : int
    name:str

@app.post("/items/")
def post_items(item:Item, db:Session = Depends(get_db)):
    db_item = models.Item(id=item.id, name = item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id":db_item.id,"message": f"{db_item.name} added successfully!"}
    
@app.put("/items/{id}")
def put_items(id:int,item:Item, db:Session = Depends(get_db)):
    try:
        db_item = db.query(models.Items).filter(models.Item.id == id).first()
        if not db_item:
            raise HTTPException(status_code=404,detail="Item Not Found")
        db_item.name = item.name
        db.commit()
        db.refresh(db_item)
        return {"message":f"Updated the data {item.id} to {item.name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/items/{id}") 
def delete_item(id:int,db:Session = Depends(get_db)):
    try:
        db_item = db.query(models.Item).filter(models.Item.id == id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item Not Found")
        db.delete(db_item)
        db.commit()
        return {"message": f"Item with id {id} deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


