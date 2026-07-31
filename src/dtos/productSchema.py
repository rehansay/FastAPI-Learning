from pydantic import BaseModel

class CreateProduct(BaseModel):
    name:str
    price:int=0
    category:str
    stock:int=0