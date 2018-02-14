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

    def test_is_instance(self):
        """ test if an instance is of class 'Review' """
        self.assertIsInstance(self.review, Review)

    def test_place_id(self):
        """ test if the 'place_id' of a 'Review' is a string """
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id(self):
        """ test if the 'user_id' of a 'Review' is a string """
        self.assertIsInstance(self.review.user_id, str)

    def test_text(self):
        """ test if the 'text' of a 'Review' is a string """
        self.assertIsInstance(self.review.text, str)
