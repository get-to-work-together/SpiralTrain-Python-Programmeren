#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:35:07 2023

@author: peter
"""
import os

filename_in = 'data.txtX'
filename_out = 'uit.txt'

class CustomException(Exception):
    pass

try:
    if not os.path.exists(filename_in):
        raise CustomException()
        
    with open(filename_in, encoding = 'utf_8') as f_in:
        with open(filename_out, mode = 'a', encoding = 'utf_8') as f_out:
            header = [s.strip() for s in f_in.readline().rstrip('\n').split(', ')]
            for regel in f_in:
                regel = [s.strip() for s in regel.rstrip('\n').split(', ')]
                d = dict(zip(header, regel))
                if int(d['aantal']) >= 4:
                    print(d['naam'], d['klasse'], file = f_out)

except FileNotFoundError:
    print('Cannot open file', filename_in)

except CustomException:
    print('MYEXCEPTION ! Error opening file', filename_in)

except:
    pass
    