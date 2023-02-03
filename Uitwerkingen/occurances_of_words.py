#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 11:01:55 2023

@author: peter
"""

s = """Logius is een baten-lastendienst van het ministerie van Binnenlandse Zaken en Koninkrijksrelaties en beheert generieke ICT-voorzieningen. Logius levert diensten aan andere overheidsorganisaties en organisaties met een publieke taak. Voorbeelden van diensten zijn DigiD, Digipoort, MijnOverheid en eHerkenning. Het bureau Forum Standaardisatie is een onderdeel van Logius. Tevens is Logius de PA van PKIoverheid."""

import string
s = s.lower().translate(str.maketrans('', '', string.punctuation))

words = s.split()

unique_words = set(words)

d = dict()
for word in unique_words:
    d[word] = words.count(word)
    
for word, n in sorted(d.items()):
    print(f'{word:32}: {n} {n * "*"}')

# import operator
# for word, n in sorted(d.items(), key = operator.itemgetter(1), reverse = True):
#     print(f'{word:32}: {n}')

# for word, n in sorted(d.items(), key = lambda item: item[1], reverse = True):
#     print(f'{word:32}: {n}')








# from collections import Counter

# counter = Counter(words)
# print(counter)