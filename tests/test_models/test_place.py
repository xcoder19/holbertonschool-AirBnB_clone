#!/usr/bin/python3
"""
uinitest for the amenity
"""

import unittest

from models.place import Place

""" class Test_amenity"""


class Test_amenity(unittest.TestCase):
    """ class Test_amenity"""

    def test(self):
        self.assertEqual(str, type(Place.name))

    def test1(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test2(self):
        self.assertEqual(str, type(Place.city_id))

    def test3(self):
        self.assertEqual(float, type(Place.latitude))

    def test4(self):
        self.assertEqual(float, type(Place.longitude))
