#!/usr/bin/python3
"""Module defining the City class, inheriting from BaseModel."""

from models.base_model import BaseModel


class City(BaseModel):
    """A class to represent a city.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
