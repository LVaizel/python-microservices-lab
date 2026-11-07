from fastapi import FastAPI, HTTPException
from app.models.customerRequest import CustomerRequest
from app.services.customerService import *
from hashlib import sha256 

import requests

app = FastAPI(title="Order Service")

# Product Service address
PRODUCT_SERVICE_URL = "http://product-service:8001"

@app.get("/")
def home():
    return {
        "message": "Welcome to Customer Service"
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "customer-service"
    }

@app.post("/customers")
def create_customer(customer: CustomerRequest):
    new_customer = add_new_customer(
        name=customer.name,
        email=customer.email,
        passwordHash=sha256(customer.passwordHash.encode(), True).hexdigest()
    )
    return new_customer

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    customer = fetch_customer_by_id(customer_id)
    if customer:
        return customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
    
@app.get("/customers")
def get_customers():
    return fetch_all_customers()

@app.put("/customers/{customer_id}")
def update_customer_details(customer_id: int, customer: CustomerRequest):
    updated_customer = update_customer(
        customer_id=customer_id,
        name=customer.name,
        email=customer.email,
        passwordHash=sha256(customer.passwordHash.encode(), True).hexdigest()
    )
    if updated_customer:
        return updated_customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
