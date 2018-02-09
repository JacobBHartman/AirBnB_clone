#!/usr/bin/python3
"""
     This file contains a class called 'BaseModel' that defines all common
     attributes and methods for other classes.
"""


import uuid
import datetime

class BaseModel():
    """Defines all common attributes and methods for other classes

    Attributes:
        <go here>

    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """A magic method that initializes an instance of 'BaseModel'

        Args:
            <go here>

        """
        ritenow = datetime.datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = ritenow
        self.updated_at = ritenow

    def __str__(self):
        """A magic method that overloads __str__ with custom output
        """
        return "[{}] ({}) {}".format(str(type(self).__name__), str(self.id), str(self.__dict__))

    def save(self):
        """updates the public instance attribute 'updated_at' with the
        current 'datetime' """
        ritenow = datetime.datetime.now()
        self.updated_at = ritenow

    def to_dict(self):
        """return a dictionary containing all key=value pairs of '__dict__'
        of the instance"""
        custom_dict = {}
        desired_attributes = ['updated_at', 'created_at', 'id', 'my_number', 'name']
        for key in desired_attributes:
            if key is 'updated_at' or key is 'created_at':
                custom_dict[key] = getattr(self, key).isoformat()
            else:
                custom_dict[key] = getattr(self, key)
        custom_dict['__class__'] = self.__class__.__name__
        return custom_dict
