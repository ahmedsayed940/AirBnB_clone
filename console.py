#!/usr/bin/python3
"""Moudle for console.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand."""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program."""
        return True


if _name_ == '_main_':
    HBNBCommand().cmdloop()
