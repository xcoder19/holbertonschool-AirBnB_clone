#!/usr/bin/python3

"""BaseModel class"""
import uuid
from datetime import datetime
import models
import json


class BaseModel():
    """BaseModel class"""

    def __init__(self, *args, **kwargs):

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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):

        newdic = self.__dict__.copy()
        newdic["created_at"] = self.created_at.isoformat()
        newdic["updated_at"] = self.updated_at.isoformat()
        newdic["__class__"] = self.__class__.__name__
        return newdic
