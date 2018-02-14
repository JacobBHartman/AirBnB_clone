#!/usr/bin/python3
"""
    this module tests the 'FileStorage' class using unittests
"""


import unittest
import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    """ This class tests the FileStorage class using unit-tests
    """
    def setUp(self):
        """ set up an instance of a 'BaseModel' """
        self.storage = FileStorage()

    def tearDown(self):
        """ delete an instance of a 'BaseModel' """
        del self.storage

#   def test_file_path(self):
#       """ test the file path to the JSON string """
#       self.assertIsInstance(self.storage.__file_path, str)

#   def test_objects_dict(self):
#       """ test the objects dict where objects are stored """
#       self.assertIsInstance(self.storage.objects, dict)

    def test_all(self):
        """ test whether the all method works """
        test_dict = self.storage.all()
        self.assertIsInstance(test_dict, dict)

    def test_new(self):
        """ test the new method of 'FileStorage' class """
        base = BaseModel()
        self.storage.new(base)
        test_str = "{}.{}".format(base.__class__.__name__, base.id)
        test_dict = self.storage.all()
        self.assertIn(test_str, test_dict)

#    def test_save
#
#    def test_reload

    def test_storage_type(self):
        """ test the type of the storage object made in this file's setUp """
        self.assertIsInstance(self.storage, type(FileStorage()))

#    def test_init_storage_Type(self):
#        """ test the type of the stroage object made in the __init__ of models
#        folder
#        """
#        self.assertIsInstance #COMPLETE

    def test_save_and_reload(self):
        """ test save and reload methods of FIleStorage classs """
        base = BaseModel()
        temp_id = base.id
        self.storage.new(base)
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.storage.reload()
        temp_dict = self.storage.all()
        self.assertIsInstance(temp_dict["BaseModel." + temp_id], type(base))
