from fastapi import FastAPI, HTTPException
from hashlib import sha256
from app.models.customerRequest import CustomerRequest
from app.services.customerService import *
 
import requests

app = FastAPI(title="Customer Service")

# Order Service address
ORDER_SERVICE_URL = "http://order-service:8002"

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
def register_customer(customer: CustomerRequest):
    new_customer = add_new_customer(
        name=customer.name,
        email=customer.email,
        passwordHash=sha256(customer.password.encode()).hexdigest()
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
        passwordHash=sha256(customer.password.encode()).hexdigest()
    )
    if updated_customer:
        return updated_customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
    
@app.delete("/customers/{customer_id}")
def delete_customer_entry(customer_id: int):
    deleted_customer = delete_customer(customer_id)
    if deleted_customer:
        return deleted_customer

    raise HTTPException(
        status_code=404,
        detail="Customer not found"
    )
    
@app.get("/customers/{customer_id}/orders")
def get_customer_orders(customer_id: int):
    customer = fetch_customer_by_id(customer_id)
    if not customer:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )
    try:
        response = requests.get(
            f"{ORDER_SERVICE_URL}/orders/{customer_id}",
            timeout=5
        )
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Order Service is unavailable"
        )
    return response.json()
