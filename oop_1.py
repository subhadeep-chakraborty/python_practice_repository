'''
Object Oriented Programming Challenge:
For this challenge, create a bank account class that has two attributes:

owner
balance
and two methods:

deposit
withdraw
As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.


======================================================================================================================================================================================
======================================================================================================================================================================================
'''

class Account:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        print(f"Account created for Mr {self.owner} with balance ${self.balance}")

    def __str__(self):
        return f'Account Owner: {self.owner}\nAccount Balance: ${self.balance}'
        

    def withdraw(self,amount):
        if amount > self.balance:
            return f'Balance not available for withdrawl. Current balance is ${self.balance}'
        else:
            self.balance = self.balance - amount
            return f'Amount ${amount} withdrawn successfully\nRemaining Balance = ${self.balance}'

    def deposit(self,amount):
        self.balance = self.balance + amount
        return f'Amount ${amount} deposited successfully\nCurrent Account Balance = ${self.balance}'


'''
======================================================================================================================================================================================
======================================================================================================================================================================================

Test Suite : 

1. Instantiate the class
  acct1 = Account('Jose',100)        Passed

2. Print the object
  print(acct1)                       Passed

3.Make a series of deposits and withdrawals
acct1.deposit(50)                    Passed

4.Make a withdrawal that exceeds the available balance
acct1.withdraw(500)                   Passed
'''
