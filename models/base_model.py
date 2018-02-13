#!/usr/bin/python3
"""
     This file contains a class called 'BaseModel' that defines all common
     attributes and methods for other classes.
"""


import uuid
from datetime import datetime
import models

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
            for key, value in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ A magic method that overloads __str__ with custom output """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """ A magic method that overloads __str__ with custom output """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute 'updated_at' with the
        current 'datetime' """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary containing all key=value pairs of '__dict__'
        of the instance """
        custom_dict = dict(self.__dict__)
        custom_dict['created_at'] = self.created_at.isoformat()
        custom_dict['updated_at'] = self.updated_at.isoformat()
        custom_dict['__class__'] = self.__class__.__name__
        return custom_dict
