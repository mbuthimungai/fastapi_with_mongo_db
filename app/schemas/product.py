from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: str
    weight: float
    unit: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Tomatoes",
                "description": "Fresh from the farm",
                "price": "sh. 29",
                "weight": 30.4,
                "unit": "grams"
            }
        }    
        
class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[str]
    weight: Optional[float]
    unit: Optional[str]
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Tomatoes",
                "description": "Fresh from the farm",
                "price": "sh. 29",
                "weight": 30.4,
                "unit": "grams"
            }
        }    