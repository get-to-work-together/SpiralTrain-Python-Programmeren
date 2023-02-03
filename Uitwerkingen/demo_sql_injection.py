#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:43:40 2023

@author: peter
"""

name = "peter"

name = 'hacked"; DROP DATABASE;--'

name = 'hacked" or 1==1;--'


sql = f'SELECT * FROM table WHERE name = '

execute(sql, name)

print(sql)