#!/usr/bin/python3
"""
    this module defines a class called 'User' that inherits from
    'BaseModel' and defines users
"""


import models
from models.base_model import BaseModel


class User(BaseModel):
    """
        this class defines a user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
