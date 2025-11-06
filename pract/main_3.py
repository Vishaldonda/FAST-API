from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def func(db: Session = Depends(get_db)):
    items = db.query(models.Item).all()
    return items

@app.get("/items/{id}/")
def get_id(id : int,q:str | None = None):
    return {"item_id": id,"q":q}

class Item(BaseModel):
    name :str

@app.post("/items/")
def create_item(item:Item,db: Session = Depends(get_db)):
    db_item = models.Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id": db_item.id, "name": db_item.name}
