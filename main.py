from itertools import count
from fastapi import Depends,FastAPI
from models import product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

app = FastAPI()

# Create tables in the database
database_model.Base.metadata.create_all(bind=engine)

# Initial in-memory products
products = [
    product(id=1, name="Laptop", description="A high-performance laptop", price=999.99, quantity=10),
    product(id=2, name="Smartphone", description="A latest model smartphone", price=699.99, quantity=25),
    product(id=3, name="Headphones", description="Noise-cancelling headphones", price=199.99, quantity=50),
    product(id=4, name="Monitor", description="4K UHD Monitor", price=399.99, quantity=15),
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
    
def init_db():
    db = session()
    try:
        # If there is already data, don't insert again
        count = db.query(database_model.Product).count()
        if count > 0:
            return
        # Insert initial products into the DB if they are not already there
        for p in products:
            db.add(
                database_model.Product(
                    id=p.id,
                    name=p.name,
                    description=p.description,
                    price=p.price,
                )
            )
        db.commit()
    finally:
        db.close()


init_db()


@app.get("/")
def greet():
    return {"message": "Hi sharana how are you?"}


@app.get("/products")
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()

    return db_products


@app.get("/product/{id}")
def get_product_by_id(id: int, db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(p: product):
    products.append(p)
    return p


@app.put("/product")
def update_product(id: int, p: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = p
            return "Product updated successfully"

    return {"error": "Product not found"}


@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return {"error": "Product not found"}