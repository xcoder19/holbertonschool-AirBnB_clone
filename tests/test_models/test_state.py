#!/usr/bin/python3
"""
uinitest for the State
"""

import unittest

from models.state import State

""" class Test_State"""


class Test_State(unittest.TestCase):
    """ class Test_State"""

    def test(self):
        self.assertEqual(str, type(State.name))
