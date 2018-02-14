#!/usr/bin/python3
"""
    this module contains a class that tests the 'Amenity' class
"""


import unittest
from models.amenity import Amenity


class TestAmenityClass(unittest.TestCase):
    """ This class tests the 'Amenity' class
    """
    def setUp(self):
        """ set up an instance of a 'Amenity' """
        self.amenity = Amenity()

    def tearDown(self):
        """ delete an instance of a 'Amenity' """
        del self.amenity

    def test_is_instance(self):
        """ test if an instance is of 'Amenity' class """
        self.assertIsInstance(self.amenity, Amenity)

    def test_name(self):
        """ test if name of an 'Amenity' instance is a string """
        self.assertIsInstance(self.amenity.name, str)
