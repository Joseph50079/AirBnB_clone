#!/usr/bin/python3

"""Console.py file the entry point of the command interpreter"""
import datetime
import cmd
from models.base_model import BaseModel
from models import storage


def parser_arg(arg):
    if not arg:
        print("** class name missing **")

        return None

    args = arg.split()

    if len(args) == 0:
        return None
        
    elif args[0] != 'BaseModel':
        print('** class doesn\'t exist **')

    return args
        

class HBNBCommand(cmd.Cmd):
    """HBNBCommand is a command interpreter class
        contains all the required command to 
        manage this models
    """

    prompt = '(hbnb) '

    def emptyline(self):
        """emptyline method for handling emptyline
        when key <ENTER> is clicked\n
        """
        pass

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""

        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""

        return True
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id

        """


        args = parser_arg(arg)
        if not args:
            return

        else:
            arg = BaseModel()
            print(arg.id)
            print(arg)
            storage.new(arg)
            storage.save()
            return
    

    def do_show(self, arg):
        """
        Prints the string representation of an instance 
        based on the class name and id

        """
        args = parser_arg(arg)

        if not args:
            return
            
        elif len(args) != 2:
            print('** instance id missing **')
            return

        else:
            l = args
            cls = l[0]
            id_n = l[1]
            all_obj = storage.all()
            objs = all_obj.get(f"{cls}.{id_n}", '** no instance found **')
            print(objs)


    def do_destroy(self, arg):
        """destroy: Deletes an instance based on the class name and 
        id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = parser_arg(arg)

        if not arg:
            return

        elif len(args) != 2:
            print('** instance id missing **')
            return

        else:
            l = args
            cls = l[0]
            id_n = l[1]
            all_obj = storage.all()
            objs = all_obj.get(f"{cls}.{id_n}", '** no instance found **')
            if objs == '** no instance found **':
                print(objs)
            else:
                all_obj.pop(f"{cls}.{id_n}")

        
if __name__ == "__main__":   
    HBNBCommand().cmdloop() 