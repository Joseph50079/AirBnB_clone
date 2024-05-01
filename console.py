#!/usr/bin/python3

"""Console.py file the entry point of the command interpreter"""

import cmd

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


if __name__ == '__main__':
     HBNBCommand().cmdloop()