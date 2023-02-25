numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [i for i in numbers if i<1]
print(lst)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lst1 = [c1 for a1 in list_of_lists for b1 in a1 for c1 in b1]
print(lst1)

list_of_tuples = [(i3, 1, i3, i3**2, i3**3, i3**4, i3**5) for i3 in range(11)]
print(list_of_tuples)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

cont4 = [(b4.upper(), b4[:3].upper(), c4.upper()) for a4 in countries for b4, c4 in a4]
print(cont4)


dictionaries = [{"country": b4.upper(), "city":c4.upper()} for a4 in countries for b4, c4 in a4]
print(dictionaries)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat = [" ".join(b5) for a5 in names for b5 in a5]
print(concat)

linear_functions = lambda m6, b6, x6: m6*x6 +b6
print(linear_functions(5,5,8))