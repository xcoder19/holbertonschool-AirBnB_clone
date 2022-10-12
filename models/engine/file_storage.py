#!/usr/bin/python3

import json
class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        
        
        with open(self.__file_path, "w") as file:
            json.dump(self.__objects,file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                 self.__objects = json.load(file)
            
        except BaseException:
            pass
