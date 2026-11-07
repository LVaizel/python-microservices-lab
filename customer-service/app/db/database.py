from app.models.customer import Customer

db: dict[int, Customer] = {}
current_id = 1

def get_customer(customer_id: int) -> Customer | None:
    return db.get(customer_id)

def get_all_customers() -> list[Customer]:
    return list(db.values())

def create_customer(name: str, email: str, passwordHash: str) -> Customer:
    global current_id
    new_customer = Customer(id=current_id, name=name, email=email, passwordHash=passwordHash)
    db[current_id] = new_customer
    current_id += 1
    return new_customer

def update_customer(customer_id: int, name: str | None = None, email: str | None = None, passwordHash: str | None = None) -> Customer | None:
    customer = db.get(customer_id)
    if customer:
        if name is not None:
            customer.name = name
        if email is not None:
            customer.email = email
        if passwordHash is not None:
            customer.passwordHash = passwordHash
        return customer
    return None

def delete_customer(customer_id: int) -> bool:
    if customer_id in db:
        del db[customer_id]
        return True
    return False
