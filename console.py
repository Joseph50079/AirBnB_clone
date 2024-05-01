#!/usr/bin/python3

"""Console.py file the entry point of the command interpreter"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a command interpreter class
        contains all the required command to 
        manage this models
    """

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the program."""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""

        return True
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id

        """


        if not arg:
            print("** class name missing **")

        elif arg != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            arg = BaseModel()
            print(arg.id)
        
if __name__ == '__main__':
     HBNBCommand().cmdloop()