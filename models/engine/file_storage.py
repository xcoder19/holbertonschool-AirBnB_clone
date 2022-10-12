#!/usr/bin/python3

""" FileStorage class"""
from models.base_model import BaseModel


import json


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}
    def all(self):
       return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(new_dict, file)
   
    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
           
                
        except BaseException:
            pass
    
