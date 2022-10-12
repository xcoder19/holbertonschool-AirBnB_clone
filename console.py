#!/usr/bin/python3
"""HBNBCommand class"""



import cmd



class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    def do_quit(self, arg):
        quit()
        
        

    def do_EOF(self, arg):
        pass
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()
