#!/usr/bin/python3

"""Console.py file the entry point of the command interpreter"""
import datetime
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import re

Class = [
    'BaseModel',
    'User',
    'State',
    'City',
    'Place',
    'Review',
    'Amenity'
]

Not_attr = ['id', 'created_at', 'updated_at']


def parser_arg(arg):
    if not arg:
        print("** class name missing **")

        return None

    args = arg.split()

    if len(args) == 0:
        return None

    elif args[0] not in Class:
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

    def default(self, arg):
        """Default function of onecmd of console"""
        action_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update,
            "create": self.do_create
        }

        args = arg.split('.')
        if args[0] in Class:
            if len(args) != 2:
                return
            else:
                match = re.search(r"\((.*?)\)", args[1])
                if match:
                    match = match.group(1)
                    command = match.strip(',"')
                    if args[1].split("(")[0] in action_map.keys():
                        call = "{} {}".format(args[0], command)
                        return action_map[args[1].split("(")[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False

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
            arg = eval(args[0])()
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
            cls = args[0]
            id_n = args[1]
            all_obj = storage.all()
            objs = all_obj.get(f"{cls}.{id_n}", '** no instance found **')
            print(objs)

    def do_destroy(self, arg):
        """destroy: Deletes an instance based on the class name and
        id (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        args = parser_arg(arg)

        if not args:
            return

        elif len(args) != 2:
            print('** instance id missing **')
            return

        else:
            cls = args[0]
            id_n = args[1]
            all_obj = storage.all()
            objs = all_obj.get(f"{cls}.{id_n}", '** no instance found **')
            if objs == '** no instance found **':
                print(objs)
            else:
                all_obj.pop(f"{cls}.{id_n}")
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
          based or not on the class name.\
        Ex: $ all BaseModel or $ all.
        """
        arg_list = split(arg)
        objects = storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in Class:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

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
            cls = args[0]
            id_n = args[1]
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

            elif args[2].strip('"') in Not_attr:
                return
            else:
                args[2] = args[2].strip('"')
                args[3] = args[3].strip('"')
                if args[2] in type(objs).__dict__:
                    v_type = type(objs.__class__.__dict__[args[2]])
                    setattr(objs, args[2], v_type(args[3]))
                else:
                    key = f"{cls}.{id_n}"
                    setattr(objs, args[2], args[3])
                storage.save()
                storage.reload()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        arg1 = parser_arg(arg)
        count = 0
        for obj in storage.all().values():
            if arg1[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
