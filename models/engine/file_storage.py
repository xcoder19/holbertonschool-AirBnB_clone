#!/usr/bin/python3

""" FileStorage class"""
from models.base_model import BaseModel
import models
import os


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
        dict = {}
        try:
            for x, v in self.__objects.items():
                dict[x] = v.to_dict()

            json_data = json.dumps(dict)
            with open(self.__file_path, "w") as file:
                file.write(json_data)
        except BaseException:
            pass

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                obj = json.load(file)
            for key, value in obj.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)

        except BaseException:
            pass
