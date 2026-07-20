from fastapi import APIRouter
from src.utils.utils import get_all_products

productRoutes=APIRouter()


@productRoutes.get("/")
def getAllProducts():
    return get_all_products()

@productRoutes.get("/{id}")
def getOneProducts(id:int):
    print(id)
    allproducts=get_all_products()

    for product in allproducts:
        if product["id"]==id:
            return product


    return {"message": "Product Not Found"}


@productRoutes.post("/create")
def createNewProducts():
    return[]