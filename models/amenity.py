#!/usr/bin/python3
"""Moudle of State inherit from BaseModel.
"""

from models import BaseModel


class Amenity(BaseModel):
    """Class State that inherits from BaseModel.
    
    Attributes:
        name (str): The name of the amenity.
    """
    name = ""