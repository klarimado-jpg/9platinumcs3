class BankAccount: # creates the class
    
    def __init__(self, account_number, balance): # constructor that will run when a Bankaccount is created
        self.set_account_number(account_number) # calls the setter to store account number
        self.set_balance(balance) # calls the setter to store the balance
        

def get_account_number(self): #gets the account number
    return self.__account_number #makes the attribute private

def set_account_number(self, account_number): # creates method to set the account number
    self.__account_number = account_number # stores the account number in a private attribute

def get_balance(self): # gets the balance 
    return self.__balance # returns the balance private

def set_balance(balance): # creates a method to set the balance
    if balance < 0: # checks if the balance is less than 0
        print ("The balance must not be a negative number.") # displays an error message if the balance is negative
    else: # will run if the balance is zero or positive
        self.__balance = float(balance) #makes the value float

@property #returns an object of the property class
def balance(self): # creates the balance property
    return self.get_balance() # returns the balance using getter

@balance.setter #sets the balance amount
def balance(self, value): # creates the setter for balance property
    self.set_balance(value) # calls set_balance() to update balance

def display(self): # creates the method to display account info
    print(f"Account Number {self.get_account_number()} Balance{self.get_alance():.2f}") # prints the account number and balance with 2 decimal places

print("BankAccount 12345 1000") # prints a heading which shows the sample acc info
account1 = BankAccount("12345", 1000) # creates BankAccount object with number 12345 and balance of 1000

print("Account 1") # prints a label for the first acc
account1.display() # calls display() to show the acc info

print("\nUpdate Balance to -100") # prints a message to indicate that the balance will be changed to -100
account1.balance = -100 # changes rhe balance to -100, but the setter will reject it because it is negative

account1.display() # displays the acc info 
