# for a in range(0, 11):
#     print(a)

# i = 0
# while i < 11:
#     print(i)
#     i = i+1

# for u in reversed(range(0, 11)):
#     print(u)

# b = 10
# while b >= 0:
#     print(b)
#     b = b-1

# import time
# f = 1
# v = 1
# while f <= 7:
#     while v <= f:
#         print("#", end="")
#         v = v+1
#     v = 1
#     f = f+1
#     print("")
#     time.sleep(0.5)

# help(print)

# print("")
# f = 1
# v = 1
# while f <= 7:
#     while v <= 7:
#         print("%", end="")
#         v = v+1
#     v = 1
#     f = f+1
#     print("")

# a = 0
# for i in range(11):
#     a = i
#     b = a * a
#     print(a, " x ", a, " = ", b, end="")
#     print("")

# ist = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
# for i in ist:
#     print(i)

# for n in range(101):
#     if n%2 == 0:
#         print("even: ", n)

# for m in range(101):
#     if m % 2 != 0:
#         print("odd: ", m)

# k = 0
# for h in range(101):
#     k = h + k
# print(k)

# e = 0
# for n in range(101):
#     if n % 2 == 0:
#         e = e + n
# print("even sum: ", e)

# t = 0
# for m in range(101):
#     if m % 2 != 0:
#         t = t + m
# print("odd sum: ", t)

# lit = ['banana', 'orange', 'mango', 'lemon']
# # for i in lit[::-1]:
# # for i in reversed(lit):
# rev = []
# for i in lit:
#     rev = [i] + rev
# print("reverse list: ", rev)

# from countries import countries
# print(countries)
# print(type(countries))
# for i in countries:
#     if "land" in i:
#         print(i)

# f = open("countries.py", "r")
# tst = f.read()
# tst1 = tst.split("\n")
# for i in tst1:
#     if "land" in i:
#         print(i)
# f.close()

"""
working on countries-data.py
"""
p = open("countries-data.py", "r")
lst = eval(p.read())
# print(lst)

"""
total numer of languages
"""
# st = set()
# # print(type(st))
# for x in lst:
#     for key, val in x.items():
#         if key == "languages":
#             # print(key, val)
#             for c in val:
#                 st.add(c)
# print("total no off languages: ", len(st))

"""
10 most spoken language
"""

# lt = []
# lt1 = []
# dt = {}
# lt2 = []
# cont = 0
# for x in lst:
#     for key, val in x.items():
#         if key == "languages":
#             lt.append(val)
# # print(lt)
# for q in lt:
#     for p in q:
#         lt1.append(p)
# result = dict((i, lt1.count(i)) for i in lt1)
# # print(result)
# a = sorted(result.items(), key=lambda x: x[1])
# # print("sorted dict: ", a)
# top_ten = a[-10:]
# print(top_ten)

"""
find word used how many time
"""
# dt1 = {}
# lt = ["a", "b", "a"]
# for i in lt:
#     dt1[i] = (lt.count(i))
# print(dt1)


"""
most populated countries in the world
"""

lt = []
lt1 = []
dt = {}
lt2 = []
cont = 0
for x in lst:
    for key, val in x.items():
        if key == "population":
            dt[x['name']] = x['population']
# print(dt)
a = sorted(dt.items(), key=lambda x: x[1])
# print("sorted dict: ", a)
top_ten = a[-10:]
print(top_ten)

