#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:01:01 2023

@author: peter
"""

t = input('Voer tekst in: ')

print( t.upper() )
print( t.lower() )
print( t.capitalize() )
print( t.title() )
print( t[:3] )
print( t.endswith('?') )
print( t.lower().replace(' ', '_') )

