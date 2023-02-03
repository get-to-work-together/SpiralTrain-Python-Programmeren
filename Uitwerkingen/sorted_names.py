#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:52:37 2023

@author: peter
"""

import random

aantal_namen = int(input('Hoeveel namen wil je invoeren?'))

d = dict()
for _ in range(aantal_namen):
    name = input('Enter a name: ')

    password = (name.
                replace('e','3').
                replace('a','4').
                replace('e','3').
                replace('u','7').
                replace('o','0').
                swapcase() +
                str(random.randint(1000, 9999)))[::-1]

    d[name] = password
    
    
print(d)
    
for name in d.keys():
    print(f'{name:16}: {d[name]}')
