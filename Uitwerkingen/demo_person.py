#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 09:54:39 2023

@author: peter
"""

class Person:
    
    def __init__(self, name, residence):
        self._name = name.upper()
        self._residence = residence
        
    def __str__(self):
        return f'Person - {self._name} at {self._residence}'
    
    def __repr__(self):
        return f'Person("{self._name}", "{self._residence}")'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name.upper()
        
    def tell(self):
        return f'I am {self._name} from {self._residence}'

    def relocate(self, new_residence):
        self._residence = new_residence


class Student(Person):
    
    def __init__(self, name, residence, studienr):
        super().__init__(name, residence)
        self._studienr = studienr

    def __str__(self):
        return f'Student - {self._name} at {self._residence}'
    
    def __repr__(self):
        return f'Student("{self._name}", "{self._residence}")'
    
    def tell(self):
        return f'I am {self._name} a student with nr. {self._studienr} from {self._residence}'


# ----------------------------------------------------------------------------------

p = Person('AlBeRT', 'Amsterdam')

print( p.tell() )


s2 = Student('Pietje', 'Den Haag', '8765547')
print( s2.tell() )

s2.relocate('Wageningen')
print( s2.tell() )

