dog = {}
print(type(dog))

dog.update({"name": "tommy",
            "color": "brown",
            "breed": "yes",
            "legs": "four",
            "age": "5"
            })
print("dog dictionary: ", dog)

student = {}
student.update({"first_name": "faizan",
                "last_name": "rashid",
                "gender": "M",
                "age": "26",
                "marital_status": "no",
                # "skills": ["programer", "gaimer"],
                "skills": "programer",
                "country": "Pakistan",
                "city": "Rawalpindi",
                "address": "dhokh_khabba"
                })

print("data type", type(student["skills"]))
tmp = student["skills"]
tmp = tmp.split()
# print("data type tmp", type(tmp))
tmp.append("gaimer")            # adding new value in a list
student["skills"] = tmp
print("student data: ", student)


print("student lenght of data: ", len(student))

print("values as a list: ", student.values())
print("keys as a list: ", student.keys())

print("skills value: ", student["skills"])
print("skills value using get: ", student.get('skils'))        # give none if key not exist

itm = student.items()
print("dictionary to a list of tuples: ", itm)

del student["age"]
print(student)

del dog

