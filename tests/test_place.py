#!/usr/bin/python3
"""
    this module tests the 'Place' class using unittests
"""


import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ This class tests the 'Place' class
    """
    def setUp(self):
        """ set up an instance of a 'Place' """
        self.place = Place()

    def tearDown(self):
        """ delete an instance of a 'Place' """
        del self.place
