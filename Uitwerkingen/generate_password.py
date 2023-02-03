#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 14:44:26 2023

@author: peter
"""

import random
import string

def generate_password(length = 8, 
                      n_uppercase = 3, 
                      n_lowercase = 3, 
                      n_digits = 1, 
                      n_special = 1):
    
    
    uppercase = random.sample('ABCDEFGHJKLMNPQRSTUVWXYZ', k = n_uppercase)  # removed I, O
    lowercase = random.sample('abcdefghijkmnopqrstuvwxyz', k = n_lowercase) # removed l
    digits = random.sample(string.digits, k = n_digits)
    special = random.sample('@#$%&*()', k = n_special)
    
    n_extra = length - n_uppercase - n_lowercase - n_digits - n_special
    extra = random.sample(string.digits, n_extra)
    
    characters = uppercase + lowercase + digits + special + extra
    
    random.shuffle(characters)
    
    password = ''.join(characters)
    
    return password


# -----------------------------------------------------

if __name__ == '__main__':
    
    users = ['Peter', 'Job', 'Chakir', 'Wouter']
    
    passwords = {user: generate_password() for user in users}
    
    print(passwords)


