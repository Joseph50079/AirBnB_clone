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
        return None

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
            if objs == '** no instance found **':
                print(objs)
            else:
                all_obj.pop(f"{cls}.{id_n}")
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name.\
        Ex: $ all BaseModel or $ all.
        """

        if arg and arg != 'BaseModel':
            print('** class doesn\'t exist **')
            return

        else:
            list_all = []
            all_objs = storage.all()
            for key in all_objs.keys():
                val = str(all_objs.get(key))
                list_all.append(val)
            print(list_all)

    def do_update(self, arg):
        """update: Updates an instance based on the class name and id by 
            adding or updating attribute (save the change into the JSON file). 
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = parser_arg(arg)

        if not args:
            return

        elif len(args) < 2:
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
                return
            elif len(args) < 3:
                print('** attribute name missing **')
                return
            elif len(args) < 4:
                print('** value missing **')
                return
            else:
                if args[2] in type(objs).__dict__:
                    v_type = type(objs.__class__.__dict__[args[2]])
                    setattr(objs, args[2], v_type(args[3]))
                else:
                    key = f"{cls}.{id_n}"
                    setattr(objs, args[2], args[3])
                storage.save()
                storage.reload()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
