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

    def empty_line(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
