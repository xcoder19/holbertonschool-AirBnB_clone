#!/usr/bin/python3
"""Test_BaseModel"""

import unittest

from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """Test_BaseModel"""

    def test1(self):
        
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
    
    