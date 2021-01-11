# 1
# users = ["Aybek baymatov", "Azat", "Nurgul", "ermek", "bakyt"]
# titled_users = []
# for user in users:
#     user_ = user.title()
#     titled_users.append(user_)
# print(titled_users)



# users = ["Aybek baymatov", "Azat", "Nurgul", "ermek", "bakyt"]
# titled_users = list(map(lambda user: user.title(), users))
# print(titled_users)



# 2
# def farenheit(temp):
#     return((float(9)/5)*temp + 32)


# def celcuis(temp):
#     return((float(5)/9)*(temp-32))

# temps = [36.6, 37, 37.5, 38, 39]
# f = map(farenheit, temps)
# print(list(f))



# 3
# users = {
#     'users': {'name': 'Askat', 'age': 24},
#     'user2': {'name': 'Bakyt', 'age': 21},
#     'user3':{'name': 'Ermek', 'age': 30}
# }

# def my_func(my_dict):
#     if my_dict[1]['age'] >= 25:
#         print(my_dict[1]['name'], "SENDING MESSAGE")
#     else: 
#         print("You are too young")

# result = list(map(my_func, users.items()))


# 4
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []

# for num in list_:
#     if num % 2 == 0:
#         new_list.append(num)
#     else:
#         pass

# print(new_list)



# 5
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def even_func(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# even_list = list(filter(even_func, list_))
# # even_list = list(filter(lambda num: num % 2 == 0, list_))
# print(even_list)



# 6
# users = [
#     {'name': 'Askat', 'age': 24, 'confirmed': True},
#     {'name': 'Bakyt', 'age': 21, 'confirmed': False},
#     {'name': 'Ermek', 'age': 30, 'confirmed': True}
#     ]

# def is_confirmed(user):
#     if user['confirmed']:
#         return True
#     return False

# result = list(filter(is_confirmed, users))




# 7
# from functools import reduce

# numbers = [3, 4, 2, 5, 6, 1, 12, 6]

# def my_sum(first, second):
#     return first - second

# result = reduce(lambda num1, num2: num1 + num2, numbers)
# result = reduce(my_sum, numbers, 100)
# print(result)



# 8
# nums = [1, 2, 3, -5, 0, -7, 4, -1]
# positive_nums = list(map(lambda x: 0 if x < 0 else 1, nums))
# print(positive_nums)