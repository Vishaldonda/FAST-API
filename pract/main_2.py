from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Mock data (in-memory list)
mock_items = [
    {"id": 1, "name": "Book"},
    {"id": 2, "name": "Laptop"},
    {"id": 3, "name": "Phone"}
]

# Pydantic model for input validation
class Item(BaseModel):
    name: str

# Home route
@app.get("/", tags=["Home"])
def home():
    return {"message": "Welcome to FastAPI with Mock Data!"}

# Get all items
@app.get("/items/", tags=["Items"])
def get_all_items():
    return {"items": mock_items}

# Get item by ID
@app.get("/items/{id}", tags=["Items"])
def get_item(id: int):
    for item in mock_items:
        if item["id"] == id:
            return item
    return {"message": "Item not found"}

# Create a new item
@app.post("/items/", tags=["Items"])
def create_item(item: Item):
    new_id = len(mock_items) + 1
    new_item = {"id": new_id, "name": item.name}
    mock_items.append(new_item)
    return {"message": f"Item '{item.name}' added successfully", "item": new_item}
