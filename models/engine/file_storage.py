#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances.
"""


import json
import models


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj._class.name_, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = getattr(models, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass