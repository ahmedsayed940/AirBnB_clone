#!/usr/bin/python3
"""Serializes instances to a JSON file and deserializes JSON file to instances.
"""

from models.base_model import BaseModel
import json
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes
    JSON file to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    cls_name = val["class"]
                    del val["class"]
                    obj_id = key.split('.')[1]
                    if cls_name == "BaseModel":
                        self.new(BaseModel(**val))
                    elif cls_name == "User":
                        self.new(User(**val))
        except FileNotFoundError:
            return
