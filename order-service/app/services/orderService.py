from app.db import database
from app.models.order import Order

def add_new_order(product_id: int, product_name: str, unit_price: float, quantity: int) -> Order:
    return database.create_order(productId=product_id, productName=product_name, unitPrice=unit_price, quantity=quantity)

def fetch_order_by_id(order_id: int) -> Order | None:
    return database.get_order(order_id)

def fetch_all_orders() -> list[Order]:
    return database.get_all_orders()

def update_order(order_id: int, quantity: int | None = None) -> Order | None:
    return database.update_order(order_id, quantity=quantity)

def delete_order(order_id: int) -> bool:
    if order_id in database.db:
        del database.db[order_id]
        return True
    return False
