#!/usr/bin/python3
"""
uinitest for the amenity
"""

import unittest

from models.amenity import Amenity

""" class Test_amenity"""
class Test_amenity(unittest.TestCase):
    """ class Test_amenity"""

     
    def test(self):
        self.assertEqual(str, type(Amenity.name))

