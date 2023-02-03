#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:13:25 2023

@author: peter
"""

class Vector:
    
    def __init__(self, x, y):
        self._x = x
        self._y = y
        
    def __str__(self) -> str:
        return f'[{self._x}, {self._y}]'
    
    def __repr__(self) -> str:
        return f'Vector({self._x}, {self._y})'
    
    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)
    
    def length(self) -> float:
        return (self._x ** 2 + self._y ** 2) ** 0.5
    
    def __eq__(self, other):
        return self.length() == other.length()
    def __ne__(self, other):
        return self.length() != other.length()
    def __lt__(self, other):
        return self.length() < other.length()
    def __le__(self, other):
        return self.length() <= other.length()
    def __gt__(self, other):
        return self.length() > other.length()
    def __ge__(self, other):
        return self.length() >= other.length()
    
    def __hash__(self):
        return hash((self._x, self._y))
        
# ----------------

v1 = Vector(4, 6)
v2 = Vector(2, 16)


print(v1)
print(v2)

v3 = v1 + v2

v3 = v1.__add__(v2)

print(v3)

print(v1.length())

