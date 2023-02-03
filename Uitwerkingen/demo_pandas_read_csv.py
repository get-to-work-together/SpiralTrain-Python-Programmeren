#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 13:49:18 2023

@author: peter
"""

import pandas as pd

df = pd.read_csv('data.csv', decimal=',', sep=';', skiprows=3)