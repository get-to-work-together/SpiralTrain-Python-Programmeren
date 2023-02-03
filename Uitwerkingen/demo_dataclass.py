#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:36:07 2023

@author: peter
"""

from dataclasses import dataclass

@dataclass
class Vector:
    x: float = 0
    y: float = 0
    
# -------------


v1 = Vector(2, 3)

print(v1)
    