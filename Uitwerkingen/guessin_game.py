#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:11:46 2023

@author: peter
"""

import random
secret_number = random.randint(1, 100)

print('Raad een getal tussen 1 en 100.')

number_of_guesses = 0
while True:
    guess = int(input('Wat denk je dat het getal is? '))
    number_of_guesses += 1
    
    if guess < secret_number:
        print('Higher ... ', end = '')
    
    elif guess > secret_number:
        print('Lower ... ', end = '')
    
    else:
        print(f'YEAH!!! You guessed it in {number_of_guesses} guesses. The number was {secret_number}.')
        break
    
