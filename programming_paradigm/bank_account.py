class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
       
        
        
    def deposit(self, amount) :
        self.account_balance += amount
        return self.account_balance
        
    def withdraw(self, amount) :
        if amount <= self.account_balance:
            self.account_balance -= amount
            return self.account_balance
        elif amount > self.account_balance:
            amount = None
            return amount
        
            
        
    def display_balance(self) :
        return f"Current Balance: ${self.account_balance}"