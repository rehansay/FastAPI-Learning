from fastapi import FastAPI
from src.routes.productRoute import productRoutes

app=FastAPI(
    title="FastAPI crash course",
    description="We are going to learn important topic of fastapi"
)

@app.get("/home")
def home():
    return{
        "message":"welcom to your fastapi learning journey" 
    }


app.include_router(productRoutes, prefix="/products")


### CRUD APISs -Products - Json File
## https://localhost:8000/products/get-all
## https://localhost:8000/products/create


