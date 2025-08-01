class BankAccount:
    """this is an example class"""
    def __init__(self,number,name,curbal): # constructor called at the time of creating instance
        self.number = number
        self.name = name
        self.curbal = curbal

    def deposit(self,amount):
        self.curbal += amount
    def withdraw(self,amount):
        self.curbal -= amount
    def getCurbal(self):
        return self.curbal 


account1 = BankAccount(12345,'bob',1000)
account2 = BankAccount(12346,'pat',1200)
account3 = BankAccount(12347,'sam',1500)


account1.deposit(1000) # account1.deposit(account1,1000)

print(account1.getCurbal())  # account.getCurbal(account1)
