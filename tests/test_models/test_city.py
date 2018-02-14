#!/usr/bin/python3
"""
    this module tests the 'City' class using unittests
"""


import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    """ This class tests the 'City' class
    """
    def setUp(self):
        """ set up an instance of a 'City' """
        self.city = City()

    def tearDown(self):
        """ delete an instance of a 'City' """
        del self.city

    def test_is_instance(self):
        """ test if an instance is of class 'City' """
        self.assertIsInstance(self.city, City)

    def test_state_id(self):
        """ test if 'state_id' of a 'City' instnce is a string """
        self.assertIsInstance(self.city.state_id, str)

    def test_name(self):
        """ test if 'name' of a 'City' instance is a string """
        self.assertIsInstance(self.city.name, str)
