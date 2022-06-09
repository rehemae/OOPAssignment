

class Account:
     def __init__(self,amount_withdraw ,account_name, amount_deposited, balance):
        self.amount_withdraw = amount_withdraw
        self.balance=balance
        self.amount_deposited=amount_deposited
        self.account_name=account_name


     def deposit (self):
         return f"Hello {self.account_name}, you have deposited {self.amount_deposited}, your new balance is {self.balance + self.amount_deposited}" 

     def withdraw(self):
         return f" Hello {self.account_name}, you have withdrawn {self.amount_withdraw}, your new blance is {self.amount_deposited - self.amount_withdraw}"


         
         

    