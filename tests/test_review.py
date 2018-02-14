#!/usr/bin/python3
"""
    this module tests the 'Review' class using unittests
"""


import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """ This class tests the 'Review' class
    """
    def setUp(self):
        """ set up an instance of a 'Review' """
        self.review = Review()

    def tearDown(self):
        """ delete an instance of a 'Review' """
        del self.review
