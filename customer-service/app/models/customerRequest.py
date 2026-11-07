from pydantic import BaseModel

class CustomerRequest(BaseModel):
    name: str = ""
    email: str = ""
    password: str = ""
    
    @classmethod
    def fromDict(cls, data: dict):
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            password=data.get("password", "")
        )
        
    @classmethod
    def new(cls):
        return cls(
            name="",
            email="",
            password=""
        )
        
    def __str__(self):
        return f"CustomerRequest(name='{self.name}', email='{self.email}', password='{self.password}')"
    
    def __repr__(self):
        return self.__str__()

    def toDict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
          