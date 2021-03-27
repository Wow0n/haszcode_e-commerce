from fastapi import FastAPI
from pydantic import BaseModel
import queries

app = FastAPI()

class Item(BaseModel):
    name: str
    quantity: int
    price: float

@app.post("/warehouse/select", status_code=200)
def warehouse_storage():
    return queries.warehouse_select()

@app.post("/warehouse/insert", status_code=200)
def warehouse_insert(item: Item):
    return queries.warehouse_insert(item)
