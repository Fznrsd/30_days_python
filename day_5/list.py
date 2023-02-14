lst = []
lst.append('Tomato')
print(lst)

lst1 = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
print(len(lst1))

print(lst1[0])
print(lst1[-1])
a = len(lst1)
int(a)
b = a//2
print(b)
print(lst1[b])

lst2 = ["Faizan", 25, 6.8, "marital not", "Rawalpindi"]
print(lst2)
print(type(lst2))

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle",  "Amazon"]
print(it_companies)

print("number of companies: ", len(it_companies))
print(it_companies[0])
print(it_companies[-1])
a = len(it_companies)
int(a)
mid = a//2
print(mid)
print(it_companies[mid])

it_companies[2] = "orange"
print(it_companies)

it_companies.insert(2, "orange")
print(it_companies)

a = len(it_companies)
int(a)
mid = a//2
it_companies.insert(mid, "convergence")
print(it_companies)

it_companies[4] = it_companies[4].upper()
print(it_companies)

print('#; '.join(it_companies))

print("IBM" in it_companies)

it = it_companies
print(it)
# its = sorted(it)
# print(its)
it.sort()
print(it)

it.reverse()
print("reverce: ", it)

print(it[:3])
print(it[-3:])
print(it[mid])

del it[0]
print(it)
del it[mid]
print(it)

last = len(it)
g = last-1
del it[g]
print(it)
it.clear()
print(it)
del it

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
list3 = front_end + back_end
print(list3)

#ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]






