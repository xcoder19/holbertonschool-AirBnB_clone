#!/usr/bin/python3
"""
uinitest for the city
"""

import unittest

from models.city import City

""" class Test_State"""


class Test_State(unittest.TestCase):
    """ class Test_State"""

    def test(self):
        self.assertEqual(str, type(City.name))

    def test2(self):
        self.assertEqual(str, type(City.state_id))
