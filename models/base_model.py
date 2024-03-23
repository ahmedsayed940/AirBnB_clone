#!/usr/bin/python3
"""Defines all common attributes/methods for other classes.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for other classes, providing common attributes/methods.

    Attributes:
        id (str): Unique identifier for each instance.
        created_at (datetime): Date and time when the instance was created.
        updated_at (datetime): Date and time when the instance was updated.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a BaseModel instance.

        Args:
            args: Unused
            kwargs: Key-value pairs of attributes
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
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "{} {} {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the current datetime and saves the instance."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the BaseModel instance."""
        obj = self.__dict__.copy()
        obj['class'] = self.__class__.__name__
        obj['created_at'] = self.created_at.isoformat()
        obj['updated_at'] = self.updated_at.isoformat()
        return obj
