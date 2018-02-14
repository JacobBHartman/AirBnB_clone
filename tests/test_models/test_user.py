#!/usr/bin/python3
"""
    this module tests the 'User' class using unittests
"""


import unittest
from models.user import User


class TestUserClass(unittest.TestCase):
    """ This class tests the 'User' class
    """
    def setUp(self):
        """ set up an instance of a 'User' """
        self.user = User()

    def tearDown(self):
        """ delete an instance of a 'User' """
        del self.user

    def test_is_instance(self):
        """ test if an instance is of class 'User' """
        self.assertIsInstance(self.user, User)

    def test_email(self):
        """ test if the 'email' of a 'User' is a string """
        self.assertIsInstance(self.user.email, str)

    def test_password(self):
        """ test if the 'password' of a 'User' is a string """
        self.assertIsInstance(self.user.password, str)

    def test_first_name(self):
        """ test if the 'first_name' of a 'User' is a string """
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name(self):
        """ test if the 'last_name' of a 'User' is a string """
        self.assertIsInstance(self.user.last_name, str)
