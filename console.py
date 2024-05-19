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

    def do_update(self, argv):
        """Updates an instance based on the class name and id by adding or
        updating attribute and save it to the JSON file."""
        arg_list = parser_arg(argv)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()


        
if __name__ == "__main__":   
    HBNBCommand().cmdloop() 
