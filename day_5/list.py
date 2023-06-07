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

full_stack = list3[:]
full_stack[full_stack.index('Redux')+1:full_stack.index('Redux')+1] = ['Python', 'SQL']

print(full_stack)

# level 2
# q no. 1

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
min_age = ages[0]
max_age = ages[-1]

ages.append(min_age)
ages.append(max_age)

if len(ages) % 2 == 1:
    median_age = ages[len(ages) // 2]
else:
    median_age = (ages[len(ages) // 2] + ages[len(ages) // 2 - 1]) / 2

average_age = sum(ages) / len(ages)

range_of_ages = max_age - min_age

min_to_average = abs(min_age - average_age)
max_to_average = abs(max_age - average_age)

print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Range of ages:", range_of_ages)
print("Min to average:", min_to_average)
print("Max to average:", max_to_average)

# q no. 2
from countries import countries

if len(countries) % 2 == 0:
    middle_countries = [middle_country, countries[len(countries) // 2 - 1]]
    print("The middle countries are:", middle_countries)

else:
    middle_country = countries[len(countries) // 2]
    print("The middle country is:", middle_country)

# q no. 2
middle_index = len(countries) // 2

if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]

else:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]

print("The first half of the list is:", first_half)
print("The second half of the list is:", second_half)

# q no. 3

countr = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpack the first three countries
first_three_countries, scandic_countr = countr[:3], countr[3:]

print("The first three countries are:", first_three_countries)
print("The scandic countries are:", scandic_countr)
