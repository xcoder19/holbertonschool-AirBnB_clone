
import json
from os.path import exists
class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{self.__class__.__name__}.{self.id}"] = obj

    def save(self):
        json_object = json.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(json_object)

    def reload(self):
        file_exists = exists(self.__file_path)
        if file_exists is True:
            with open(self.__file_path,"r") as file:
                self.__objects = json.loads(file)