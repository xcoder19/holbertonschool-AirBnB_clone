#!/usr/bin/python3

"""BaseModel class"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = str(value)
                elif key == "created_at":
                    self.created_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
          
            models.storage.new(self)

    def __str__(self):

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        dic = self.__dict__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
