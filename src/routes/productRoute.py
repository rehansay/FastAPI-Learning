from fastapi import APIRouter , HTTPException
from src.utils.utils import get_all_products, create_product

from src.dtos.productSchema import CreateProduct, UpdateProduct


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

@productRoutes.put("/update/{id}")
def updateProduct(product:UpdateProduct, id:int=None):
    if not id:
        return HTTPException(status_code=400, detail={"error":"Product ID"})


    allProducts=get_all_products()
    for index, p in enumerate(allProducts):
        if p["id"]== id:
            changes={}
            for k ,v in product.model_dump().items():
                if v is not None:
                    changes[k]=v
            allProducts[index]={"id":id, **p, **changes}

            create_product(allProducts)
            return {"message":"roduct Updated Successfully"}
           
    

    return HTTPException(status_code=400, detail={"error":"Product ID Not Found"})



@productRoutes.delete("/delete/{id}")
def deleteProduct(id:int=None):
    if not id:
        return HTTPException(status_code=400, detail={"error":"Product ID"})


    allProducts=get_all_products()
    for index, p in enumerate(allProducts):
        if p["id"]== id:
            

            allProducts.pop(index)
            create_product(allProducts)
            return {"message":"Product Deleted Successfully"}
           
    

    return HTTPException(status_code=400, detail={"error":"Product ID Not Found"})
