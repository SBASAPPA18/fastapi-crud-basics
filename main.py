from fastapi import FastAPI
from sqlalchemy import engine
from models import product
from database import session,engine
import database_model

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return {"message": "Hi sharana how are you?"}

products = [
    product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    product(id=2, name="Smartphone", description="A latest model smartphone", price=699.99, quantity=25),
    product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50),
    product(id=4, name="Monitor", description="4K UHD Monitor", price=399.99, quantity=15),
]

@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: product):
    products.append(product)
    return product


@app.put("/poduct")
def update_product(id : int, product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
        
    return {"error": "Product not found"}

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id  == id:
            del products[i]
            return "product deleted successfully"
    
    return {"error": "Product not found"}