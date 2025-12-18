from typing import Optional, Dict, List
from uuid import uuid4

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Pydantic models
class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, example="Keyboard")
    description: Optional[str] = Field(None, max_length=200, example="Mechanical keyboard")
    price: float = Field(..., ge=0, example=49.99)
    in_stock: bool = Field(True, example=True)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    pass  # For PUT, we expect all fields

class Item(ItemBase):
    id: str

app = FastAPI(title="Items API", version="1.0.0")

# In-memory "database"
db: Dict[str, Item] = {}

# Routes
@app.get("/items", response_model=List[Item], tags=["items"])
def list_items():
    return list(db.values())

@app.get("/items/{item_id}", response_model=Item, tags=["items"])
def get_item(item_id: str):
    item = db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["items"])
def create_item(payload: ItemCreate):
    item_id = str(uuid4())
    item = Item(id=item_id, **payload.model_dump())
    db[item_id] = item
    return item

@app.put("/items/{item_id}", response_model=Item, tags=["items"])
def update_item(item_id: str, payload: ItemUpdate):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    updated = Item(id=item_id, **payload.model_dump())
    db[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["items"])
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return None