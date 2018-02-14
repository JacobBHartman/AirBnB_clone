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
