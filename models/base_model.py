import uuid
from datetime import datetime
"""BaseModel Class"""
class BaseModel:
    """BaseModel Class"""
    
    def __init__(self, *args, **kwargs):
        
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = str(value)
                elif key == "created_at":
                    self.created_at = datetime.now().isoformat()
                elif key == "updated_at":
                    self.updated_at =  datetime.now().isoformat()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        var = (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
        return (str(var))
    def save(self):
        """save func"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """to_dict func"""
        dic = self.__dict__
        dic["__class__"] = str(self.__class__.__name__)
        dic["created_at"] =  self.created_at.isoformat()
        dic["updated_at"] =  self.updated_at.isoformat() 
        return dic
