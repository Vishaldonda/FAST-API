from pydantic import BaseModel


# User schemas
class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
    
# Item schema
class Item(BaseModel):
    id: int
    name: str
