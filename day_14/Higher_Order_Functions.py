"""
The map() function executes a specified function for each item in an iterable. 
The item is sent to the function as a parameter.
hint (always used with list)
"""
# def dev_team(a):
#   return len(a)

# x = map(dev_team, ('talha', 'mazhar', 'faizan'))
# print(x) # print only address
# #convert the map into a list, for readability:
# print(list(x))

#################
"""
The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
return boolean value for each iterable.  
hint (print with list or for loop) 
"""
# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)
# # print(list(adults))
# for x in adults:
#   print(x)

#############
"""
Apply function of two arguments cumulatively to the items of iterable, 
from left to right, so as to reduce the iterable to a single value. 
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
calculates ((((1+2)+3)+4)+5).
"""
# from functools import reduce
# ages = [5, 12, 17, 18, 24, 32]
# multiply = lambda x,y: x+y
# print(reduce(multiply, ages))

#############
"""
Properties of higher-order functions:

    A function is an instance of the Object type.
    You can store the function in a variable.
    You can pass the function as a parameter to another function.
    You can return the function from a function.
    You can store them in data structures such as hash tables, lists,
"""
#############
"""
Python Closures

Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

"""
# def add_ten():
#     ten = 2
#     def add(num):
#         return num + ten
#     return add

# closure_result = add_ten()
# print(closure_result(4))  # 15
# print(closure_result(3))  # 20

##############
'''
Decorator
A decorator is a design pattern in Python that allows a user to add new 
functionality to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate.

'''

# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper
    
# @uppercase_decorator
# def greeting():
#     return 'Welcome to Python'

# # greeting = uppercase_decorator(greeting)
# print(greeting()) 

##############

# def pnt(lst1):
#     a1 = [d1 for b1 in lst1 for c1, d1 in b1.items() if c1 == "name"]
#     return a1

# fle = open("countries-data.py", "r")
# lst1 = eval(fle.read())
# e1 = pnt(lst1)
# print(e1)

###########


# from countries import countries

# def upper_case(countries):
#     return countries.upper()

# a2 = map(upper_case, countries)
# print(list(a2))

############

# numbers = [1, 2, 3, 4, 5]

# def square(number):
#     return number * number

# a2 = map(square, numbers)
# print(list(a2))

############

# def uper(name):
#     return name.upper()

# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# a3 = map(uper, names)
# print(list(a3))

############

# from countries import countries

# def case_land(countries):

#     if "land" in countries:
#         return countries

# a2 = filter(case_land, countries)
# print(list(a2))

############

# from countries import countries

# def case_6(countries):

#     if len(countries) == 6:
#         return countries

# a2 = filter(case_6, countries)
# print(list(a2))


############

# from countries import countries

# def case_6_more(countries):

#     if len(countries) >= 6:
#         return countries

# a2 = filter(case_6_more, countries)
# print(list(a2))


############

# from countries import countries

# def case_e(countries):

#     if countries[0] == "E":
#         return countries

# a2 = filter(case_e, countries)
# print(list(a2))


############

# def get_string_lists(lst):
#     lst1 = " ".join(lst)
#     return lst1

# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# lst2 = get_string_lists(names)
# print(lst2)
# print(type(lst2))

############

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add = lambda x,y: x+y
print(reduce(add, numbers))

##########