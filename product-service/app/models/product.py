from pydantic import BaseModel

class Product(BaseModel):
    id : int = 0
    name : str = ""
    price : float = 0.0
    stock : int = 0
            
    @classmethod
    def fromDict(cls, data: dict):
        return cls(
            id=data.get("id", 0),
            name=data.get("name", ""),
            price=data.get("price", 0.0),
            stock=data.get("stock", 0)
        )
        
    @classmethod
    def new(cls):
        return cls(
            id=0,
            name="Default Product",
            price=0.0,
            stock=0
        )
        
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})"
    
    def __repr__(self):
            return self.__str__()
        
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
        
