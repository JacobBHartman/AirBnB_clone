#!/usr/bin/python3
"""
    This file contains a class 'FileStorage' that serializes instances to a JSON
    file and deserializes JSON file to instances
"""


import json
import os.path
import models

class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON file to
    instances

    Attributes:
        <go here>

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dictionary '__objects' """
        return FileStorage.__objects

    def new(self, obj):
        """ set in '__objects' the obj with key '<obj class name>.id' """
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ serialize '__objects' to the JSON file (path: '__file_path') """
        temp_dict = {}
        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(temp_dict, json_file)

    def reload(self):
        """ deserializes the JSON file to '__objects' (only if the JSON file
        exists; otherwise, do nothing) """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as json_file:
                loaded_dicts = json.load(json_file)

            for key, value in loaded_dicts.items():
                new_instance = models.create_instance[value['__class__']](**value)
                FileStorage.__objects["{}.{}".format(value['__class__'], value['id'])] = new_instance

            # FIND value associated with '__class__' (which is the string 'BaseModel')

            # Create a BaseModel Instance that is mapped to the string 'BaseModel')

            # Once we create a BaseModel instance, we want to pass all the attributes
            # from the loaded_dict into that instance (except for __class__)

#            FileStorage.__objects = loaded_dicts
