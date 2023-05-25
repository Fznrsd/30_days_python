import math 

age = int(25)
height = float(6.8)
complx = 3+5j
print(age)
print(height)
print(complx)

print('enter base: ')
b = input()
b = int(b)
print('enter height: ')
h = int(input())
area = (0.5*b*h)
print("The area of the triangle is: ", area)

l = int(input('length of a rectangle: '))
w = int(input('width of a rectangle: '))
area = l * w
p = 2*(l+w)
print('the area of rectangular: ', area)
print('the perimeter of rectangular: ', p)

# q.no 5
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)


pi = float(3.14)
r = float(input('radius: '))
area = pi * r * r
c = 2 * pi * r
print('the area of circle: ', area)
print('the circumference of circle: ', p)

# q.no 8
x = int(input('y-intercept enter x value: '))
y = 2 * x - 2
print('y-intercept is:', y)

# q.no 9
p = [2, 2]
q = [6, 10]
print('Euclidean distance:', math.dist(p, q))
s1 = int(math.dist(p, q))

# q.no 10
print('Compare the slopes:', s1 == y)


print('Calculate the value of y (y = x^2 + 6x + 9)')
x = int(input('enter value of x: '))
y = print('the value of y: ', x**2 + 6*x + 9) 

a = 'python'
b = 'dragon'
print('length of python: ', len(a))
print('length of dragon: ', len(b))
print('length are not equal: ', len(a) != len(b))

print('chech \'on\' is in python and dragon using \'and\' gate: ', 'on' in a and 'on' in b)

# q.no 14
sentence = "I hope this course is not full of jargon."
if "jargon" in sentence:
    print("The word 'jargon' is present in the sentence.")
else:
    print("The word 'jargon' is not present in the sentence.")


l = len(a)
print('float: ', float(l))
print('string: ',str(l))

print('number is even=\'true\' or not=\'fales\': ')
num = float(input('enter a number; ' ))
print(num%2 == 0)

a = '10'
b = 10
#a = int(a)
#b = str(b)
print(type(a) == type(b))

print(1, 1**0, 1**1, 1**2, 1**3, "\n",
      2, 2**0, 2**1, 2**2, 2**3, "\n",
      3, 3**0, 3**1, 3**2, 3**3, "\n",
      4, 4**0, 4**1, 4**2, 4**3, "\n",
      5, 5**0, 5**1, 5**2, 5**3 )



ex = 123
ex = int(ex)
print(ex)


lst = ['apple', 'orange', 'banana']
lst1 = ['apple', 'orange', 'banana']
print(len(lst) == len(lst1))


# Q.no 18
result = 7 // 3
value = int(2.7)
print(value)
print(result)
if result == value:
    print("The floor division of 7 by 3 is equal to the integer value of 2.7.")
else:
    print("The floor division of 7 by 3 is not equal to the integer value of 2.7.")


# q.no 20

value = int(9.8)

if value == 10:
    print("The integer value of '9.8' is equal to 10.")
else:
    print("The integer value of '9.8' is not equal to 10.")


# q.no 21
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))

pay = hours * rate_per_hour
print("Your weekly earning is:", pay)

# q.no 22
years = int(input("Enter number of years you have lived: "))
seconds_of_a_year = 365 * 24 * 60 * 60  # Number of seconds in a year
total_seconds = years * seconds_of_a_year

print("You have lived for", total_seconds, "s")

