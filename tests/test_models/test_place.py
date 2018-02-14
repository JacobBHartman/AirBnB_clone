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

    def test_is_instance(self):
        """ test if an instance is of class 'Place' """
        self.assertIsInstance(self.place, Place)

    def test_city_id(self):
        """ test if 'city_id' of a 'Place' is a string """
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id(self):
        """ test if 'user_id' of a 'Place' is a string """
        self.assertIsInstance(self.place.user_id, str)

    def test_name(self):
        """ test if 'name' of a 'Place' is a string """
        self.assertIsInstance(self.place.name, str)

    def test_description(self):
        """ test if 'description' of a 'Place' is a string """
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms(self):
        """ test if 'number_rooms' of a 'Place' is an int """
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms(self):
        """ test if 'number_bathrooms' of a 'Place' is an int """
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest(self):
        """ test if 'max_guest' of a 'Place' is an int """
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night(self):
        """ test if 'price_by_night' of a 'Place' is an int """
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude(self):
        """ test if 'latitude' of a 'Place' is a float """
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude(self):
        """ test if 'longitude' of a 'Place' is a float """
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids(self):
        """ test if 'amenity_ids' of a 'Place' is a list """
        self.assertIsInstance(self.place.amenity_ids, list)
