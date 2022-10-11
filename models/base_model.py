import uuid
import datetime
"""BaseModel Class"""
class BaseModel:
    """BaseModel Class"""
    id = str(uuid.uuid4())
    created_at = datetime.datetime
    updated_at = datetime.datetime

    def __str__(self):
        print(f"[{self.name}] ({self.id}) {self.__dict__}")
    def save(self):
        """save func"""
        self.updated_at = datetime.datetime
    def to_dict(self):
        """to_dict func"""
        dic = self.__dict__
        dic["__class__"] = str(self.name)
        dic["created_at"] =  self.created_at.isoformat()
        dic["updated_at"] =  self.updated_at.isoformat() 
        return dic
