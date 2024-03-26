#!/usr/bin/python3
"""Module for console."""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""
    prompt = "(hbnb)"
    valid_classes = {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(cmds[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in objs:
                print("** no instance found **")
            else:
                print(objs[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in objs:
                print("** no instance found **")
            else:
                del objs[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objs = storage.all()
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            for key, value in objs.items():
                print(str(value))
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objs.items():
                if key.split('.')[0] == cmds[0]:
                    print(str(value))

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        cmds = shlex.split(arg)

        if len(cmds) == 0:
            print("** class name missing **")
        elif cmds[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(cmds) < 2:
            print("** instance id missing **")
        elif len(cmds) < 3:
            print("** attribute name missing **")
        elif len(cmds) < 4:
            print("** value missing **")
        else:
            objs = storage.all()

            key = "{}.{}".format(cmds[0], cmds[1])
            if key not in objs:
                print("** no instance found **")
            else:
                obj = objs[key]

                attr_name = cmds[2]
                attr_value = cmds[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)

                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

