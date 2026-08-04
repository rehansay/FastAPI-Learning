from fastapi import FastAPI
from src.routes.productRoute import productRoutes
from src.routes.userRoute import userRoute
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
app.include_router(userRoute, prefix="/users")


### CRUD APISs -Products - Json File
## https://localhost:8000/products/get-all
## https://localhost:8000/products/create


