#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:52:04 2023

@author: peter
"""

import math

r = float(input('Geef de straal van een cirkel: '))

circumference = 2 * math.pi * r
area = math.pi * r ** 2

print('Een cirkel met straal', r)
print('Omtrek', circumference)
print('Oppervlakte', area)