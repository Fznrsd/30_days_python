it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(it_companies)
print("lenght: ", len(it_companies))

it_companies.add("twiter")
print(it_companies)
st = {"United Sol", "Systems Ltd", "DPL", "Averox", "Emumba"}

it_companies.update(st)
print("after updating: ", it_companies)

it_companies.remove("DPL")
print("after delete: ", it_companies)
'''
This method is different from the remove() method, 
because the remove() method will raise an error 
if the specified item does not exist, 
and the discard() method will not.
'''
it_companies.discard("abc")
print(it_companies)

print(A.intersection(B))
print(A.issubset(B))        # T
print(B.issubset(A))        # F

print(A.isdisjoint(B))      # check there are common items

print(A.union(B))           # join

print("print first: ", A)
print("print snd: ", age)
print(A.difference(age))

del it_companies

print("list: ", age)
age1 = set(age)
print("set: ", age1)
print("check lenght is equal: ", len(age) == len(age1))

c = "I am a teacher and I love to inspire and teach people"
c = c.split()
print(c)
c = set(c)
print(c)

