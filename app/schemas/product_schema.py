# app/schemas/product_schema.py
from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    id: int
    title: str

class ProductListResponse(BaseModel):
    produtos: List[Product]
