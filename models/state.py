#!/usr/bin/python3
"""Module defining the State class, inheriting from BaseModel."""

from models import BaseModel


class State(BaseModel):
    """A class to represent a state.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
