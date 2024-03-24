#!/usr/bin/python3
"""
Defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import json

class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Public instance attributes:
    - id: string - Unique identifier assigned with a UUID when an instance is created.
    - created_at: datetime - Date and time when an instance is created.
    - updated_at: datetime - Date and time when an instance is last updated.

    Public instance methods:
    - __init__(self): Initializes a new instance of BaseModel with a unique id and creation/update timestamps.
    - __str__(self): Returns a string representation of the BaseModel instance.
    - save(self): Updates the 'updated_at' attribute with the current datetime.
    - to_dict(self): Returns a dictionary representation of the BaseModel instance.

    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel with a unique id and creation/update timestamps.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation containing class name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        Returns:
            dict: Dictionary containing all instance attributes with class name, creation/update times.
        """
        obj = self.__dict__.copy()
        obj['__class__'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
