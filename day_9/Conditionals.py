
a = input("Enter your age: ")
a = int(a)
if a >= 18:
    print("You are old enough to drive")
else:
    b = 18 - a
    print("You need ", b, " more years to learn to drive")

c = int(input("Enter your age: "))
d = int(input("Enter my age: "))

if c > 0 and d > 0:
    if c > d:
        e = c-d
        print("You are", e, "years older than me")
    elif c < d:
        e = d-c
        print("You are", e, "years younger than me")
    elif c == d:
        print("You are equal")
else:
    print("enter a positive integer")

a = int(input("Enter your no.: "))
b = int(input("Enter my no.: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less b")
else:
    print("Number are equal")

g = int(input("Enter your exam No.: "))
if 80 <= g <= 100:
    print("your grade is A")
elif 70 <= g < 80:
    print("your grade is B")
elif 60 <= g < 70:
    print("your grade is C")
elif 50 <= g < 60:
    print("your grade is D")
elif 0 <= g < 50:
    print("your grade is F")

season = input("Enter a month to check the season exp[October]: ")
if season == "September" or season == "October" or season == "November":
    print("the season is Autumn")
elif season == "December" or season == "January" or season == "February":
    print("the season is Winter")
elif season == "March" or season == "April" or season == "May":
    print("the season is Spring")
elif season == "June" or season == "July" or season == "August":
    print("the season is Summer")

fruits = ['banana', 'orange', 'mango', 'lemon']
frt = input("input fruit name: ")
if frt in fruits:
    print("the fruit exists: ", fruits)
else:
    fruits.append(frt)
    print("a fruit doesn't exist in the list, we add the fruit to the list", fruits)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

dic = input("input key: ")
skill = person.get(dic)
# print(skill)
if skill is None:
    print("we do not have key name: ", dic)
else:
    length = len(person.get(dic))
    mid = length//2
    print("mid skill: ", person.get(dic)[mid])

check = person['skills']
if "Python" in check:
    num = person['skills'].index("Python")
    print("python in skills: ", person['skills'][num])

if "JavaScript" in check and "React" in check:
    print('He is a front end developer')
    if "Node" in check and "Node" in check and "MongoDB" in check:
        print('He is a backend developer')
        if " React" in check and "Node" in check and "MongoDB" in check:
            print('He is a fullstack developer')
else:
    print('unknown title')

if person['is_marred'] == True and person['country'] == 'Finland':
    print(person['first_name'], person['last_name'], "lives in", person['country'], "He is married.")

