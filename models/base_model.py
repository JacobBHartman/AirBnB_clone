#!/usr/bin/python3
"""
     This file contains a class called 'BaseModel' that defines all common
     attributes and methods for other classes.
"""


import uuid
from datetime import datetime
from models.__init__ import storage

class BaseModel:
    """ Defines all common attributes and methods for other classes

    Attributes:
        <go here>

    """

    def __init__(self, *args, **kwargs):
        """ A magic method that initializes an instance of 'BaseModel'

        Args:
            <go here>

        """
        if len(kwargs) > 0:
            for key in kwargs:
                if key is '__class__':
                    kwargs[key] = type(self)
                elif key == 'updated_at' or key == 'created_at':
                    kwargs[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ A magic method that overloads __str__ with custom output """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """ Update the public instance attribute 'updated_at' with the
        current 'datetime' """
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """ Return a dictionary containing all key=value pairs of '__dict__'
        of the instance """
        custom_dict = self.__dict__
        custom_dict['__class__'] = self.__class__.__name__
        for key in custom_dict:
            if key == 'updated_at' or key == 'created_at':
                custom_dict[key] = getattr(self, key).isoformat()
        return custom_dict
