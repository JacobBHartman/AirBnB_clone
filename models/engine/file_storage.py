#!/usr/bin/python3
"""
    This file contains a class 'FileStorage' that serializes instances to a JSON
    file and deserializes JSON file to instances
"""


import json
import os.path
from models.base_model import BaseModel

class FileStorage(BaseModel):
    """ serializes instances to a JSON file and deserializes JSON file to
    instances

    Attributes:
        <go here>

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary '__objects' """
        return self.__objects

    def new(self, obj):
        """ set in '__objects' the obj with key '<obj class name>.id' """
        self.__objects[self.__class__.__name__+ self.id] = obj

    def save(self):
        """ serialize '__objects' to the JSON file (path: '__file_path') """
        with open(self.__file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """ deserializes the JSON file to '__objects' (only if the JSON file
        exists; otherwise, do nothing) """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as json_file:
                return json.load(json_file)
