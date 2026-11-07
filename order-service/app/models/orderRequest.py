from pydantic import BaseModel
class OrderRequest(BaseModel):
    customerId : int = 0
    productId : int = 0
    quantity : int = 0
        
    @classmethod
    def fromDict(cls, data: dict):
        return cls(
            productId=data.get("productId", 0),
            quantity=data.get("quantity", 0)
        )
        
    @classmethod
    def new(cls):
        return cls(
            productId=0,
            quantity=0
        )
        
    def __str__(self):
        return f"OrderRequest(productId={self.productId}, quantity={self.quantity})"
    
    def __repr__(self):
        return self.__str__()

    def toDict(self):
        return {
            "productId": self.productId,
            "quantity": self.quantity
        }
