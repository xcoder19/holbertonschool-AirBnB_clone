#!/usr/bin/python3
"""
uinitest for the city
"""

import unittest

from models.review import Review

""" class Test_State"""


class Test_State(unittest.TestCase):
    """ class Test_State"""

    def test(self):
        self.assertEqual(str, type(Review.place_id))

    def test2(self):
        self.assertEqual(str, type(Review.user_id))
