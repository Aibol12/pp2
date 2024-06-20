class BankAccount:
    def __init__(self,owner='',balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,take):
        self.balance+=take
    def withdraw(self,take):
        if(self.balance>=take):
            self.balance-=take
            print(self.balance)
        else:
            print('deposit is not sufficient')
myAccount=BankAccount('Orynbay Aruzha',balance=15000)
myAccount.withdraw(take=1000)