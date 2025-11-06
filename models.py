from database import Base
from sqlalchemy import Column, Integer, String

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer,primary_key = True,index = True)
    name = Column(String,nullable= False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True,index = True)
    username = Column(String,unique=True,nullable= False)
    hashed_password = Column(String,nullable= False)