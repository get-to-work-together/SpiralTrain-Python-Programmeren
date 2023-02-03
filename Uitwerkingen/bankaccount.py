

class BankAccount:
    
    def __init__(self, balance, holder):
        self._balance = balance
        self._holder = holder
        
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
        
    def info(self):
        return f'The account balance is {self._balance} of holder {self._holder}.'


# --------------------------------------------------------------------------

if __name__ == '__main__':
    
    b = BankAccount(1000, 'Wouter')
    
    b.deposit(1000)
    b.withdraw(12)
    b.withdraw(102)
    b.deposit(1000)

    print(b.info())
