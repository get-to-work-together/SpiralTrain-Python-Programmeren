#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 12:56:40 2023


@author: peter
"""

import random

die1 = random.randint(1, 6)   # not very DRY - Do not Repeat ourself
die2 = random.randint(1, 6)
die3 = random.randint(1, 6)
die4 = random.randint(1, 6)
die5 = random.randint(1, 6)

total = die1 + die2 + die3 + die4 + die5

print('Thrown', die1, die2, die3, die4, die5)
print('Total', die1 + die2 + die3 + die4 + die5)