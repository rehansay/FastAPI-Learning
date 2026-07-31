from fastapi import APIRouter , HTTPException
from src.utils.utils import get_all_products, create_product

from src.dtos.productSchema import CreateProduct


productRoutes=APIRouter()


@productRoutes.get("/")
def getAllProducts(product_id:int=None):
    allProducts=get_all_products()

    if not product_id:
        return allProducts
    
    for product in allProducts:
        if product["id"]==product_id:
            return product
    return HTTPException(status_code=400,
                         detail={"error:Product not found for this ID."})






@productRoutes.get("/{id}")
def getOneProducts(id:int):

    allProducts=get_all_products()
    for product in allProducts:
        if product["id"]==id:
            return product
    return HTTPException(status_code=400,
                         detail={"error:Product not found for this ID."})




@productRoutes.post("/create")
def createNewProducts(product:CreateProduct):
    products=get_all_products()

    product=product.model_dump()
    
    next_id=max([p["id"] for p in products])+1
    product["id"]=next_id

    print(product)

    products.append(product)

    create_product(products)

    return {"message":"New Product Created Successfully"}
