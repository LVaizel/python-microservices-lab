from fastapi import FastAPI, HTTPException
from app.models.product import Product
from app.services.productService import *
from app.db import database

app = FastAPI(title="Product Service")

# Sample product database
database.create_product(name="Laptop", price=10.99, stock=100)
database.create_product(name="Keyboard", price=15.49, stock=50)
database.create_product(name="Mouse", price=7.99, stock=200)
database.create_product(name="Monitor", price=12.99, stock=75)

@app.get("/")
def home():
    return {
        "message": "Welcome to Product Service"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "product-service"
    }


@app.get("/products")
def get_products():
    return database.get_all_products()


@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = database.get_product(product_id)
    if product:
        return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
    
@app.post("/products")
def create_product(product: Product):
    new_product = add_new_product(product)
    return new_product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    updated_product = database.update_product(
        product_id=product_id,
        name=product.name,
        price=product.price,
        stock=product.stock
    )
    if updated_product:
        return updated_product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
