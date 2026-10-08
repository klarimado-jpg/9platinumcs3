class BankAccount: #creates the class
    
    def __init__(self, account_number, balance):
        self.set__account_number(account_number)
        self.set__balance(balance)
        

def get_account_number(self): #gets the account number
    return self.__account_number #makes the attribute private

def set_account_number(self, account_number):
    self.__account_number = account_number

def get_balance(self): #gets the balance 
    return self.__balance

def set_balance(balance):
    if balance < 0:
        print ("The balance must not be a negative number.")
    else:
        self.__balance = float(balance) #makes the value float

@property #returns an object of the property class
def balance(self):
    return self.get_balance()

@balance.setter #sets the balance amount
def balance(self, value):
    self.set_balance(value) 

def display(self):
    print(f"Account Number {self.get_account_number()} Balance{self.get_alance():.2f}")

print("BankAccount 12345 1000")
account1 = BankAccount("12345", 1000)

print("Account 1")
account1.display()

print("\nUpdate Balance to -100")
account1.balance = -100

account1.display()
