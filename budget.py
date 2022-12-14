"""
Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, 
and entertainment. These objects should allow for depositing and withdrawing funds from each category, 
as well computing category balances and transferring balance amounts between categories”

Considerations: this is a very interesting project as it allows not only to comprehend how a class is initialized 
and used, but also represented and used as input to other functions. You will learn how to add methods to your classes
and print them in a way that allows complex representation of your class object at different points in the program. 

Approach: define the purpose and flexibility of a class object; build its class methods using a modular approach 
and develop an understanding for how different instances of the same class can interact.

Key concepts: Class initialization, instance methods and instance representation. Defining and using functions that take
class instances as input parameters
"""

# Budget superclass
class Budget:
    # class constructor
    def __init__(self, balance, category):
        self.balance = balance
        self.category = category

    # function to return the object representation in string format
    def __repr__(self):
        return f"The balance for {self.category} is {self.balance}"

    # function to add money
    def deposit(self, amount):
        self.balance += amount
        return amount

    # function to withdraw money
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds."

    # function to get balance
    def getBalance(self):
        return self.balance
