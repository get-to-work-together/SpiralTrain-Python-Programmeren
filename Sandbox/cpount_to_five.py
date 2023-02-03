#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 15:30:01 2023

@author: peter
"""

from time import time
import matplotlib.pyplot as plt
import statistics

n = 10
n_seconds = 5

results = []
for _ in range(n):
    
    input('Press enter to start.')
    
    t0 = time()
    
    input(f'Press enter when exactly {n_seconds} seconds have passed.')
    
    t1 = time()
    
    dt = t1 - t0
    
    print(f'You pressed the button after {dt:.3f} seconds.')
    
    results.append(dt)


print('Your results are:')
print(f'  mean: {statistics.mean(results):.3f}')
print(f' stdev: {statistics.stdev(results):.3f}')

plt.hist(results)