#!/usr/bin/python3
"""HBNBCommand class"""



import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    def do_quit(self):
        quit()
        
        

    def do_EOF(self):
        quit()
        
    def emptyline(self):
        return

    def do_create(self,arg):

        args = arg.split('')
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
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
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        objs = storage.all()
        id = f"{args[0]}.{args[1]}"
        
        for key, value in objs.items():
                
            if objs == key:
                print(value)
                return
            
            print("** no instance found **")
    def do_destroy(self, arg):
        
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
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
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        
        
        for value in storage.all().values():
            if len(args) >= 0 and args[0] == value.__class__.__name__:
                list.append(value.__str__())
                print(list)
                return
            print("** no instance found **")
    
    def do_update(self, arg):
        
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
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
        
        for key, value in objs.items():
            if obj == key:
                storage.save()
                setattr(objs[obj], args[2], args[3])
                return
                
            
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
