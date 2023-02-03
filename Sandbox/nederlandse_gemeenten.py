#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:02:49 2023

@author: peter
"""

import pandas as pd

url = 'https://nl.wikipedia.org/wiki/Lijst_van_Nederlandse_gemeenten'

tables = pd.read_html(url)

df = tables[0]

print(df.iloc[:-2, 0])

df.iloc[:-2,0].to_csv('gemeenten.txt', index = False, header = False)