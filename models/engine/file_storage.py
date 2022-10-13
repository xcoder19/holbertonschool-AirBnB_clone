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
        obj = {}
        obj = self.__objects.copy()
        json_data = json.dumps(obj)
        with open(self.__file_path, "w") as file:
            file.write(json_data)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)

        except BaseException:
            pass
