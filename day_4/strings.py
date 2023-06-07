a = "Thirty"
b = "Days"
c = "of"
d = "python"
e = " "
concat = a + e + b + e + c + e + d
print(concat)

a, b, c, d = 'Coding', 'For' , 'All', " "
concat = a + d + b + d +c
print(concat)
print(type(concat))

company = "Coding For All"
print(company)
print("length", len(company))

print("upper: ", company.upper())
print("lower: ", company.lower())

print("capitalize: ", company.capitalize())
print("title: ", company.title())
print("swapcase: ", company.swapcase())

sli = company[0:7]
print("slice: ", sli)

print("Coding" in company)
print("index number: ", company.index('Coding'))

print(company.replace('Coding', 'python')) 

print(company.split())


new_line = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(new_line.split(", "))

print(company[0])
print(company[-1])
print(company[10])

ut = str(company)
ut = ut.title()
text = ut.split()
print(text)
f = ""
for i in text:
    f = f+str(i[0])
print(f)

challenge = '    Coding For All    '
print(challenge.find('o'))  
print(challenge.rfind('o'))

sentence = 'You cannot end a sentence with because because because is a conjuntion'
print("index number: ", sentence.index('because'))
print("index number: ", sentence.rfind('because'))

m = sentence.index('because')
n = sentence.rfind('because')
print(sentence[:m] + sentence[n:])


print(challenge.startswith('Coding'))   # True
print(challenge.endswith('coding')) # False

print(challenge.strip())

q = '30DaysOfPython'
w = 'thirty_days_of_python'
print(q.isidentifier())
print(w.isidentifier())


libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
l = "# ".join(libraries)
print(l)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("I am\tenjoying this\tchallenge.\nI just\twonder what\tis next.")

radius = 10
area = 3.14 * radius ** 2
a = "The area of a circle with radius {} is {} meters square.".format(radius, area)
i
print(a)

a = 8
b = 6
c = a+b
print("{} + {} = {}".format(a, b ,c))
c = a-b
print("{} - {} = {}".format(a, b ,c))
c = a*b
print("{} * {} = {}".format(a, b ,c))
c = a/b
print("{} / {} = {}".format(a, b ,c))
c = a//b
print("{} // {} = {}".format(a, b ,c))
c = a%b
print("{} % {} = {}".format(a, b ,c))
c = a**b
print("{}^{} = {}".format(a, b ,c))

# q = 18
acronym = []
name ='Python For Everyone'
for word in name.split():
    acronym.append(word[0])
print("".join(acronym))

# q no. 34
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")


