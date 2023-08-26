from math import *
import statistics
from statistics import *
from collections import Counter

class mth:
    def __init__(self, lst):
        self.lst = lst    
    
    def info(self):
        print("Count:", len(self.lst))
        print('Sum: ', sum(self.lst)) # 744
        print('Min: ', min(self.lst)) # 24
        print('Max: ', max(self.lst)) # 38
        print('Mean: ', mean(self.lst)) # 30
        print('Median: ', median(self.lst)) # 29
        print('Mode: ', mode(self.lst)) # 'mode': 26
        print('Range: ', max(self.lst) - min(self.lst)) # 14
        print('Mode: ', statistics.mode(self.lst)) # 30
        print('Standard Deviation: ', statistics.stdev(self.lst)) # 4.2
        print('Variance: ', statistics.variance(self.lst)) # 18
        print('Frequency Distribution: ', Counter(self.lst).items())


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = set()
        self.expenses = set()

    def total_income(self):
        return sum(income[0] for income in self.incomes)

    def total_expense(self):
        return sum(expense[0] for expense in self.expenses)

    def add_income(self, amount, description):
        self.incomes.add((amount, description))

    def add_expense(self, amount, description):
        self.expenses.add((amount, description))

    def account_balance(self):
        return self.total_income() - self.total_expense()
    
    def account_info(self):
        print("Account Information:")
        print(f"First Name: {self.firstname}")
        print(f"Last Name: {self.lastname}")
        print(f"Total Income: {self.total_income()}")
        print(f"Total Expense: {self.total_expense()}")
        print(f"Account Balance: {self.account_balance()}")




# q no. 1

lst = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
a = mth(lst)
a.info()

# q no. 2

person = PersonAccount("tal", "mzhr")
person.add_income(1000, "Salary")
person.add_income(1000, "Bonus")
person.add_expense(300, "Rent")
person.add_expense(200, "Groceries")
person.account_info()

