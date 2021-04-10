from pydantic import BaseModel


class ItemInsert(BaseModel):
    name: str
    quantity: int
    price: float


class ItemUpdate(BaseModel):
    id: int
    name: str
    quantity: int
    price: float
