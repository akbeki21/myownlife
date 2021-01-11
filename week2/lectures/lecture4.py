# Bishkek = {
#     Universities:{
#         Groups:{
#             Students:{

#             }
#         }
#     }
# }


# students = {
#     'name': 'Bakyt', 
#     'surname': 'Bakytov', 
#     'age': 20, 
#     'languages': ['English', 'Russian', 'Kyrgyz'],
#     'smokes': False,
#     'other_dict': {1: 'one', 2: 'two'},
#     (1, 2, 3): "HEllO"
#     }

# print(students)
# print(students[(1, 2, 3)])
# print(students['other_dict'] [2])


# print(len(students))
# print(students['name'])
# students['name'] = 'Askat'
# print(students['name'])


# del students['name']
# print(students)
# surname = students.get('surname')
# print(surname)
# name = students.get('name')
# print(name)


# students = {}
# print(type(students))
# students = dict((("winter", 1), ("sping", 2), ("fall", 3)))
# print(students)


# dict_ = dict(one = 1, two = 2, three = 3)
# tpl = [("one", 1), ("two", 2), ("three", 3)]
# dict_ = dict(tpl)
# print(dict_)


# days = [1, 2, 3]
# days_names = ['Mon', 'Tue', 'Wed']
# one_more = [5, 6, 7]
# dict_days = zip(days, days_names, one_more)
# print(dict_days)


# students = {
#     'name': 'Bakyt', 
#     'surname': 'Bakytov', 
#     'age': 20, 
#     'languages': ['English', 'Russian', 'Kyrgyz'],
#     'smokes': False,
#     'other_dict': {1: 'one', 2: 'two'},
#     (1, 2, 3): "HEllO"
#     }

# students.clear()
# print(students)


# new_student = students.copy()
# print(new_student)


# print(students.items())


# for item in students.items():
#     print(item)


# print(students.keys())
# for item in students.keys():
#     print(item)


# print(students.values())
# for item in students.values():
#    print(item)

# new_item = students.pop('name')
# print(new_item)
# print(students)

# new_item = students.popitem()
# print(new_item)
# print(students)

# students.setdefault(10, "DEFAULT")
# print(students)

# students.update([("Black": 6), ("White": 8)])
# print(students)                            *****


# students = dict.fromkeys([1, 2, 3], "Makers")
# print(students)