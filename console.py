#!/usr/bin/python3
"""HBNBCommand class"""



import cmd



class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = '(hbnb) '
    def do_quit(self, arg):
        self.close()
        
        

    def do_EOF(self, arg):
        self.close()
        




if __name__ == '__main__':
    HBNBCommand().cmdloop()
