#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:26:38 2023

@author: ChatGPT
"""

class BankAccount:
    
    currency = '€'
    
    VERSION = 1
    
    def __init__(self, holder, account_number, balance):
        self.__holder = holder
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} has been deposited to the account. The new balance is {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Withdrawal amount exceeds the current balance!")
        else:
            self.__balance -= amount
            print(f"{amount} has been withdrawn from the account. The new balance is {self.__balance}")

    def info(self):
        print(f"Holder: {self.__holder}\nAccount Number: {self.__account_number}\nBalance: {self.__balance}")


    @classmethod
    def set_version(cls, version):
        cls.VERSION = version
        
    @staticmethod
    def say_hello():
        return 'hello'
    

# --------------------------------------------------------------------------

# Create an instance of the BankAccount class
account = BankAccount("John Doe", 123456, 1000)

# Call the deposit method
account.deposit(500)

# Call the withdraw method
account.withdraw(200)

# Call the info method
account.info()

print(BankAccount.say_hello())
