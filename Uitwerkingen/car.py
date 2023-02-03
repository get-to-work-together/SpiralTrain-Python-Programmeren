#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:54:53 2023

@author: peter
"""

class Car:
    
    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage
        
    def info(self):
        return f'My great {self._color} {self._make} {self._model} as done {self._mileage}km.'
    
    def drive(self, distance):
        self._mileage += distance
        
        
# -------------------------------------------------

if __name__ == '__main__':
    
    my_car = Car('Renault', 'Megane', 'brown', 393000)
    
    print(my_car.info())
    
    my_car.drive(1234)
    my_car.drive(1234)

    print(my_car.info())
    