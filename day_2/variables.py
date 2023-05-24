print('Day 2: 30 Days of python programming')

fst_name = "faizan"
snd_name = "rashid"
full_name = "faizan rashid"
country = "pakistan"
city = "rawalpindi"
age = 26
year = "2023-01-07"
is_married = True
is_true = 2<3
is_light_on = True

print('First name: ', fst_name)
print('First name length: ', len(fst_name))
print('Last name: ', snd_name)
print('Last name length: ', len(snd_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)

# multi = fst_name, snd_name, full_name, country, city, age, year
# print(multi)

#  Level 1: Q13 
var1, var2, var3 = 10, "Hello", 3.14
print(var1)

help('False')


# level 2

# Q.No 1
first_name = 'programer'     # str
last_name = 'backend'       # str
country = 'abc'         # str
city= 'xyz'            # str
age = 123                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Programer'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(5 + 5j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'programer','age':123, 'is_married':"yes"}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # zip

# q.no 2
print(len(first_name))

# q.no 3
if len(first_name) > len(last_name):
    print("The first name is longer.")
elif len(first_name) < len(last_name):
    print("The last name is longer.")
else:
    print("The first name and last name have the same length.")

# q.no 4
num_one = 5
num_two = 4
total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one * num_two
print(product)

division = num_one / num_two
print(division)

remainder = num_two % num_one
print("The remainder is:", remainder)

exp = num_one ** num_two
print("The result is:", exp)

floor_division = num_one // num_two
print("The floor division is:", floor_division)

radius = 30
pi = 3.14
area_of_circle = pi * radius ** 2
print("The area of the circle is:", area_of_circle)

circum_of_circle = 2 * pi * radius
print("The circumference of the circle is:", circum_of_circle)


radi = float(input("Enter the radius of the circle: "))
area_of_circle = pi * radi ** 2
print("The area of the circle is:", area_of_circle)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")
age = int(age)
# Print the values
print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

