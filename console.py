#!/usr/bin/python3
"""HBNBCommand class"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    types = ["BaseModel",
             "User",
             "State",
             "City",
             "Amenity",
             "Place",
             "Review"]

    def do_quit(self, arg):
        quit()

    def do_EOF(self):
        quit()

    def emptyline(self):
        return

    def do_create(self, arg):

        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.types:
            print("** class doesn't exist **")
            return
        obj = eval(f"{args[0]}()")
        obj.save()
        print(obj.id)

    def do_show(self, arg):

        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.types:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        objs = storage.all()
        id = f"{args[0]}.{args[1]}"
        flag = False
        for key, value in objs.items():

            if objs[id] == key:
                flag = True
                print(value)
                return

        if flag is False:
            print("** no instance found **")

    def do_destroy(self, arg):

        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.types:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            obj = f"{args[0]}.{args[1]}"
            objs = storage.all()
            for key in objs.keys():
                if obj == key:
                    del objs[obj]
                    storage.save()
                    return

                print("** no instance found **")

    def do_all(self, arg):

        list = []
        args = arg.split(" ")
        if args[0] not in self.types:
            print("** class doesn't exist **")
            return

        for value in storage.all().values():
            if len(args) >= 0 and args[0] == value.__class__.__name__:
                list.append(value.__str__())
                print(list)
                return
            elif len(arg) == 0:
                list.append(value.__str__())
                print(list)

            print("** no instance found **")

    def do_update(self, arg):

        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.types:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) != 4:
            return

        obj = f"{args[0]}.{args[1]}"
        objs = storage.all()
        flag = False
        for key, value in objs.items():
            if obj == key:
                flag = True
                storage.save()
                setattr(objs[obj], args[2], args[3])
                return
        if flag is False:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
