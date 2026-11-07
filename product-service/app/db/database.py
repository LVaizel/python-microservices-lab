from app.models.product import Product

db: dict[int, Product] = {}
current_id = 1

def get_product(product_id: int) -> Product | None:
    return db.get(product_id)

def get_all_products() -> list[Product]:
    return list(db.values())

def create_product(name: str, price: float, stock: int = 0) -> Product:
    global current_id
    new_product = Product(id=current_id, name=name, price=price, stock=stock)
    db[current_id] = new_product
    current_id += 1
    return new_product

def update_product(product_id: int, name: str | None = None, price: float | None = None, stock: int | None = None) -> Product | None:
    product = db.get(product_id)
    if product:
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if stock is not None:
            product.stock = stock
        return product
    return None
