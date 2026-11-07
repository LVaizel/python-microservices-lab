class Order:
    orderId: int
    productId: int
    productName: str
    quantity: int
    unitPrice: float
    totalPrice: float
    
    def __init__(self, orderId: int, productId: int, productName: str, quantity: int, unitPrice: float):
        self.orderId = orderId
        self.productId = productId
        self.productName = productName
        self.quantity = quantity
        self.unitPrice = unitPrice
        self.totalPrice = unitPrice * quantity
    
    def updateQuantity(self, new_quantity: int):
        self.quantity = new_quantity
        self.totalPrice = self.unitPrice * new_quantity
        
    @classmethod
    def fromDict(cls, data: dict):
        return cls(
            orderId=data.get("orderId", 0),
            productId=data.get("productId", 0),
            productName=data.get("productName", ""),
            quantity=data.get("quantity", 0),
            unitPrice=data.get("unitPrice", 0.0)
        )
    
    @classmethod
    def new(cls):
        return cls(
            orderId=0,
            productId=0,
            productName="",
            quantity=0,
            unitPrice=0.0
        )
    
    def __str__(self):
        return f"Order(orderId={self.orderId}, productId={self.productId}, productName='{self.productName}', quantity={self.quantity}, unitPrice={self.unitPrice}, totalPrice={self.totalPrice})"
    
    def __repr__(self):
        return self.__str__()
    
    def toDict(self):
        return {
            "orderId": self.orderId,
            "productId": self.productId,
            "productName": self.productName,
            "quantity": self.quantity,
            "unitPrice": self.unitPrice,
            "totalPrice": self.totalPrice
        }
