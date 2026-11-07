from app.db import database
from app.models.customer import Customer

def add_new_customer(name: str, email: str, passwordHash: str) -> Customer:
    return database.create_customer(name=name, email=email, passwordHash=passwordHash)

def fetch_customer_by_id(customer_id: int) -> Customer | None:
    return database.get_customer(customer_id)

def fetch_all_customers() -> list[Customer]:
    return database.get_all_customers()

def delete_customer(customer_id: int) -> bool:
    return database.delete_customer(customer_id)

def update_customer(customer_id: int, name: str | None = None, email: str | None = None, passwordHash: str | None = None) -> Customer | None:
    return database.update_customer(customer_id, name=name, email=email, passwordHash=passwordHash)

def fetch_customer_orders(customer_id: int) -> list[int]:
    customer = database.get_customer(customer_id)
    if customer and len(customer.orders) > 0:
        return customer.orders
    return []
