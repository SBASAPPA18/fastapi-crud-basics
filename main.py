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
                    quantity=p.quantity,
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
def add_product(p: product, db:Session = Depends(get_db)):
    db.add(
        database_model.Product(
            id=p.id,
            name=p.name,
            description=p.description,
            price=p.price,
            quantity=p.quantity,
        )
    )
    db.commit()
    return p


@app.put("/product")
def update_product(id: int, p: product,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name =p.name
        db_product.description = p.description
        db_product.price = p.price
        db_product.quantity = p.quantity
        db.commit()
        return "Product updated successfully"
    
    else:
        return {"error": "Product not found"}


@app.delete("/product")
def delete_product(id: int,db:Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    else:
        return {"error": "Product not found"}