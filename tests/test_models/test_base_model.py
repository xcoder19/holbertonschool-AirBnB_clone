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
    
    def test2(self):
       
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.to_dict(), obj2.to_dict())

    def test3(self):
        
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.__str__(), obj2.__str__())

    def test4(self):
        
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.save(), obj2.save())
 
    def test4(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.created_at, obj2.created_at)
 