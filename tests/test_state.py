#!/usr/bin/python3
"""
    this module tests the 'State' class using unittests
"""


import unittest
from models.state import State


class TestStateClass(unittest.TestCase):
    """ This class tests the 'State' class
    """
    def setUp(self):
        """ set up an instance of a 'State' """
        self.state = State()

    def tearDown(self):
        """ delete an instance of a 'State' """
        del self.state
