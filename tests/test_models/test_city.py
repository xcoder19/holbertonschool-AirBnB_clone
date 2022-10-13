#!/usr/bin/python3
"""
uinitest for the city
"""

import unittest

from models import city

""" class Test_State"""
class Test_State(unittest.TestCase):
    """ class Test_State"""

     
    def test(self):
        self.assertEqual(str, type(city.name))

    def test2(self):
        self.assertEqual(str, type(city.state_id))
