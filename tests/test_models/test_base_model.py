#!/usr/bin/python3
"""
    this module tests the 'BaseModel' class using unittests
"""


import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """ This class tests the 'BaseModule' class
    """
    def setUp(self):
        """ set up an instance of a 'BaseModel' """
        self.base = BaseModel()

    def tearDown(self):
        """ delete an instance of a 'BaseModel' """
        del self.base

    def test_instance_exists(self):
        """ test if instance is a 'BaseModel' """
        self.assertIsInstance(self.base, BaseModel)

    def test_instance_type(self):
        """ tests type of a 'BaseModel' instance """
        self.assertEqual(type(self.base), type(BaseModel()))

    def test_id(self):
        """ test if id is assigned correctly to a 'BaseModel' """
        self.assertIsInstance(self.base.id, str)
        base_2 = BaseModel()
        self.assertNotEqual(self.base.id, base_2.id)

    def test_created_at(self):
        """ test created_at datetime object """
        self.assertIsInstance(self.base.created_at, datetime.date)

    def test_updated_at(self):
        """ test updated_at datetime object """
        self.assertIsInstance(self.base.updated_at, datetime.date)

    def test_dunder_str(self):
        """ test magic method str of 'BaseModel' """
        str1 = self.base.__class__.__name__
        str2 = self.base.id
        str3 = self.base.__dict__
        self.assertIsInstance(str1, str)
        self.assertIsInstance(str2, str)
        self.assertIsInstance(str3, dict)

    def test_save(self):
        """ test public instance method 'save' """
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_to_dict(self):
        """ test public instance method 'to_dict' """
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual('BaseModel', base_dict['__class__'])
        self.assertIsInstance(base_dict['updated_at'], str)
        self.assertIsInstance(base_dict['created_at'], str)

    def test_from_dict_to_instance(self):
        base_dict = self.base.to_dict()
        new_base = BaseModel(base_dict)
        self.assertIsInstance(new_base, type(BaseModel()))
        self.assertIsInstance(new_base.created_at, datetime.date)
        self.assertIsInstance(new_base.updated_at, datetime.date)
