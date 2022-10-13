#!/usr/bin/python3
""" class Test_User """
import unittest
from models.user import User

class Test_User(unittest.TestCase):
    """test user class"""
     
    def test1(self):
        self.assertEqual(str, type(User.email))

    def test2(self):
        self.assertEqual(str, type(User.password))

    def test3(self):
        self.assertEqual(str, type(User.first_name))

    def test4(self):
        self.assertEqual(str, type(User.last_name)) 