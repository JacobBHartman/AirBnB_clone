#!/usr/bin/python3
"""
    This file contains a class 'FileStorage' that serializes instances to a JSON
    file and deserializes JSON file to instances
"""


import json
import os.path

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
        FileStorage.__objects['{}.{}'.format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """ serialize '__objects' to the JSON file (path: '__file_path') """
#        custom_dict = {}
#        for key, obj in FileStorage.__objects.items():
#            value = obj.to_dict()
#            custom_dict[key] = value
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """ deserializes the JSON file to '__objects' (only if the JSON file
        exists; otherwise, do nothing) """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as json_file:
                FileStorage.__objects = json.load(json_file)
#                for objID, objAttr in json_object.items():
#                    FileStorage.__objects[objAttr['id']] = objAttr
