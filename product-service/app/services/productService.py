from app.db import database
from app.models.product import Product

def add_new_product(productName: str, unitPrice: float, stock: int) -> Product:
    # Here you could add business logic, e.g., checking if the name already exists
    return database.create_product(name=productName, price=unitPrice, stock=stock)

def fetch_product_by_id(product_id: int) -> Product | None:
    return database.get_product(product_id)

def fetch_all_products() -> list[Product]:
    return database.get_all_products()

def update_product_by_id(product_id: int, name: str | None = None, price: float | None = None, stock: int | None = None) -> Product | None:
    return database.update_product(product_id, name=name, price=price, stock=stock)

