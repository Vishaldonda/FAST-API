# Crud Operation API - MySQlite
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session 
from jose import JWTError, jwt

import models, auth
from database import Base, engine, get_db
from schemas import Item
from utils import SECRET_KEY, ALGORITHM


app = FastAPI()

# Create DB Tabels
Base.metadata.create_all(bind=engine)

# Authentication router
app.include_router(auth.router)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Helper function
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(models.User).filter(models.User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/items/")
def get_items(db:Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    items = db.query(models.Item).all()
    return items


@app.post("/items/")
def post_items(item:Item, db:Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_item = models.Item(id=item.id, name = item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"id":db_item.id,"message": f"{db_item.name} added successfully!"}
    
@app.put("/items/{id}")
def put_items(id:int,item:Item, db:Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    try:
        db_item = db.query(models.Item).filter(models.Item.id == id).first()
        if not db_item:
            raise HTTPException(status_code=404,detail="Item Not Found")
        db_item.name = item.name
        db.commit()
        db.refresh(db_item)
        return {"message":f"Updated the data {item.id} to {item.name}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/items/{id}") 
def delete_item(id:int,db:Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    try:
        db_item = db.query(models.Item).filter(models.Item.id == id).first()
        if not db_item:
            raise HTTPException(status_code=404, detail="Item Not Found")
        db.delete(db_item)
        db.commit()
        return {"message": f"Item with id {id} deleted successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


