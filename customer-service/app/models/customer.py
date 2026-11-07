from pydantic import BaseModel
class Customer(BaseModel):
    id: int
    name: str
    email: str
    passwordHash: str
    orderIds: list[int] = []
    
    def addOrderId(self, orderId: int):
        self.orderIds.append(orderId)
        
    @classmethod
    def fromDict(cls, data: dict):
        customer = cls(
            id=data.get("id", 0),
            name=data.get("name", ""),
            email=data.get("email", ""),
            passwordHash=data.get("passwordHash", "")
        )
        customer.orderIds = data.get("orderIds", [])
        return customer
    
    @classmethod
    def new(cls):
        return cls(
            id=0,
            name="",
            email="",
            passwordHash=""
        )
    
    def __str__(self):
        return f"Customer(id={self.id}, name='{self.name}', email='{self.email}', orderIds={self.orderIds})"
    
    def __repr__(self):
        return self.__str__()
    
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "passwordHash": self.passwordHash,
            "orderIds": self.orderIds
        }    