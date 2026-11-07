from app.models.order import Order

db: dict[int, Order] = {}
current_id = 1

def get_order(order_id: int) -> Order | None:
    return db.get(order_id)

def get_all_orders() -> list[Order]:
    return list(db.values())

def create_order(productId: int, productName: str, quantity: int, unitPrice: float) -> Order:
    global current_id
    new_order = Order(
        orderId=current_id, 
        productId=productId,
        productName=productName, 
        quantity=quantity,
        unitPrice=unitPrice
        )
    db[current_id] = new_order
    current_id += 1
    return new_order

def update_order(order_id: int, quantity: int | None = None) -> Order | None:
    order = db.get(order_id)
    if order:
        if quantity is not None:
            order.updateQuantity(quantity)
        return order
    return None

def delete_order(order_id: int) -> bool:
    if order_id in db:
        del db[order_id]
        return True
    return False
