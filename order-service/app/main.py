from fastapi import FastAPI, HTTPException
from app.models.orderRequest import OrderRequest
from app.services.orderService import *
import requests

app = FastAPI(title="Customer Service")

# Product Service address
PRODUCT_SERVICE_URL = "http://product-service:8001"

@app.get("/")
def home():
    return {
        "message": "Welcome to Order Service"
    }
    
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "order-service"
    }
  
@app.post("/orders")
def createOrder(order: OrderRequest):
    try:
        response = requests.get(
            f"{PRODUCT_SERVICE_URL}/products/{order.productId}",
            timeout=5
        )

        if response.status_code == 404:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        response.raise_for_status()

        product = response.json()

    except requests.RequestException:
        raise HTTPException(
            status_code=503,
            detail="Product Service is unavailable"
        )
    # Check stock
    if order.quantity <= 0:
        raise HTTPException(
            status_code=400,
            detail="Quantity must be greater than zero"
        )
        
    if order.quantity > product["stock"]:
        raise HTTPException(
            status_code=400,
            detail="Insufficient product stock"
        )
    new_order = add_new_order(
        product_id=product["id"],
        product_name=product["name"],
        unit_price=product["price"],
        quantity=order.quantity
    )
    
    return {

        "message": "Order created successfully",

        "order": new_order

    }


@app.get("/orders")
def getOrders():
    return fetch_all_orders()

@app.get("/orders/batch")
def getOrdersByIds(order_ids: list[int]):
    orders = fetch_orders_by_ids(order_ids)
    if not orders:
        raise HTTPException(
            status_code=404,
            detail="No orders found for the provided IDs"
        )
    return orders

@app.get("/orders/{order_id}")
def getOrder(order_id: int):
    order = fetch_order_by_id(order_id)
    if order:
        return order

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )

@app.put("/orders/{order_id}")
def updateOrderAmount(order_id: int, Amount: int):
    updated_order = update_order(order_id, quantity=Amount)
    if updated_order:
        return updated_order

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )

@app.delete("/orders/{order_id}")
def deleteOrder(order_id: int):
    success = delete_order(order_id)
    if success:
        return {
            "message": "Order deleted successfully"
        }

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )
