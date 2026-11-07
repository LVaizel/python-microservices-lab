from fastapi import FastAPI, HTTPException
from app.models.product import Product
from app.services.productService import *

app = FastAPI(title="Product Service")

# Sample product database
add_new_product(productName="Laptop", unitPrice=10.99, stock=100)
add_new_product(productName="Keyboard", unitPrice=15.49, stock=50)
add_new_product(productName="Mouse", unitPrice=7.99, stock=200)
add_new_product(productName="Monitor", unitPrice=12.99, stock=75)

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
    return fetch_all_products()


@app.get("/products/{product_id}")
def get_product(product_id: int):

    product = fetch_product_by_id(product_id)
    if product:
        return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
    
@app.post("/products")
def create_product(product: Product):
    new_product = add_new_product(product.name, product.price, product.stock)
    return new_product

@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):
    updated_product = update_product_by_id(
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
