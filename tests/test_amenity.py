#!/usr/bin/python3
"""
    this module tests the 'Amenity' class using unittests
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
