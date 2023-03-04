# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

#############

# def packing_person_info(**kwargs):
#     # check the type of kwargs and it is a dict type
#     # print(type(kwargs))
# 	# Printing dictionary items
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="Asabeneh",
#       country="Finland", city="Helsinki", age=250))

##########

# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)

###########

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)
