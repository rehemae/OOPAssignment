from datetime import datetime

class Account:
    def __init__(self,name,account_number):
        self.balance=0
        self.name=name
        self.account_number=account_number
        self.deposits = []
        self.withdrawals =[]
        self.loan_balance = 0
        self.transactions = 100
        
        
    def deposit(self,amount):
        if amount<=0:
            return f"Deposit amount should be more than zero"
        else:
            self.balance += amount
            details={"date":datetime.now().strftime("%d,%m,%y"), "amount":amount,"narration":f"Thank you for depositing {amount} on {datetime.now()}"}
            self.deposits.append(details)
            self.deposits.append(f"You have deposited{amount}")
            return f"You have deposited {amount}. Your new balance is {self.balance}"  

    def withdraw(self,amount):
        if amount>self.balance:
             return f"Your balance is {self.balance}, you cannot withdraw the {amount}" 
        elif amount<=0:
            return f"Amount must be greater than zero" 
        else:
            balances={"date":datetime.now().strftime("%d,%m,%y"), "amount":amount, "narration" :f"You have withdraw {amount} on {datetime.now()}"}
            self.withdrawals.append(balances)
            self.balance-=amount + self.transactions
            self.withdrawals.append(f"you have withdrawn {amount}")
            return f"you have withdraw {amount} your balance is {self.balance}"
    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for staments in self.withdrawals:
            print(staments)
    def current_balance(self):
        balance = self.balance
        print(balance)

    def full_statement(self):
        x=self.deposits + self.withdrawals  
        for i in x:
            print(i)

    def borrow(self,amount):
        if len(self.deposits)<10:
            return f"Add more deposits"
        if amount <100:
            return f"Inqure for mor than 100 loan" 
        for x in self.deposit:
            sum = 0
            sum +=x["amount"]  
        if amount>sum/3:
            return f"Dear {self.name} you can borrow money up to {sum/3}"
        if self.balance!=0:
            return f"Dear {self.name} you still  have balance of {self.balance} you can't borrow" 
        if self.loan_balance >0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}, hence repay to borrow" 
        else:
            interest= amount*0.03
            self.loan_balance+=amount+interest
            return f"Dear {self.name} you have borrowed {self.loan_balance} and your balance is {self.balance}"

    def loan_repayment(self,amount):
        if amount<0:
            return f"Amount is invald"
        if amount > self. loan_balance:
            self.balance += amount-self.loan_balance
            return f"Dear {self.name} thank you for repaying your load of {amount-self.loan_balance} and your account  balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"
    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.deposit(amount)
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.name} and your new balance is {self.balance}"
            
   
        
            
                   






       
 
    






 
