'''Implement a class called BankAccount that represents a bank account.  The class should have private 
attributes for account number ,account holder name ,and account balance.  Include methods to deposit money,
withdraw money, and display the account balance.
ensure  that the account balance connont be accessed directly  from outside the class
write program to create an instance of the BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:

   def __init__(self, account_number, account_holder_name, initial_balance=0.0):
     self.__account_number = account_number
     self.__account_holder_name = account_holder_name
     self.__account_balance = initial_balance

   def deposit(self,amount):
     if amount > 0:
       self.__account_balance += amount
       # self.__account_balance = self.__account_balance+amount
       print("deposited ₹{}. new balance: ₹{}".format(amount,
                                                  self.__account_balance))
     else:
       print("invalid deposit amount.")

   def withdraw(self, amount):
     if amount > 0 and amount <= self.__account_balance:
       self.__account_balance -= amount
       #self.__account_balance = self.__account_balancy-amount
       print("Withdrew ₹{}. New balance: ₹{}".format(amount,
                                                  self.__account_balance))        
     else:
       print("Invalid withdrawal amount or insufficient balance.")

   def display_balance(self):
     print("Account balance for {} (account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))


# Create an instance of the BankAccount class
account = BankAccount(account_number="123456789",
                      account_holder_name="abinaya",
                      initial_balance=5000.0)

# Test deposite and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()