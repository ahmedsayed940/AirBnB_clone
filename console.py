#!/usr/bin/python3
"""Moudle for console.
"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""
    prompt = "(hbnb)"
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist**")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist**")
        elif len(cmds) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()

        key = "{}.{}".format(cmds[0], cmds[1])
        if key not in objs:
            print("** no instance found **")
        else:
            print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
    def do_update(self, arg):
        """pdates an instance based on the class name and id
        by adding or updating attribute."""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
