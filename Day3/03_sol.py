class BankAccount:
    total_account = 0;
    
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        BankAccount.total_account+=1
        
    def deposit(self, amount):
        if( amount < 0):
            print("Invalid No")
            return
        
        self.amount+=amount;
        print("Amount added")
        
    def withdraw(self, amount):
        if( amount < 0 or amount > self.amount):
            print("Invalid No")
            return
            
        self.amount-=amount;
        # print("Amount added")
        
    def check_balance(self):
        print(self.amount)
            
    
        