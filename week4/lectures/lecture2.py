# import random

from random import randint



# num = int(input('Enter your number: '))
# if num < 0:
#     print("Error")

# elif num > 0:
#     factorial = 1 
#     for x in range(1, num+1):       #1,2,3,4,5   x = 1
#         factorial *= x
#     print(factorial)    

# else:
#     print(1)


# for n in [1, 2, 3, 4, 5]:
#     if n % 3:
#         continue
#     print(n)

# users = ["Altynbek", "Jyldyz", "Aktan", "Oleg", "Natasha", "Masha", "Kylych"]
# for user in users:
#     if user == "Oleg":
#         print(user)
#         break


# for x in {"Emina": 95, "Aktilek": 95, "Syimyk": 90, "Atabek": 93}.items():
#     print(x)

# print({"Emina": 95, "Aktilek": 95, "Syimyk": 90, "Atabek": 93}.items())



# for x, y in {"Emina": 95, "Aktilek": 95, "Syimyk": 90, "Atabek": 93}.items():
#     print("Iteracia")
#     print(f'Ключ {x}')
#     print(f'Значение {y}')

# secret_number = randint(1, 101)
# while True:
#     input_number = input("Enter number or 'exit' to end game: ")
#     if input_number.lower() == 'exit':
#         break
#     elif input_number.isdigit():
#         input_number = int(input_number)
#         if input_number == secret_number:
#             print("You win!")
#             break
#         elif input_number > secret_number:
#             print("Less")
#         else:
#             print("More")
#     else:
#         print("There is no such command")


# some_list = list(range(1, 11))
# some_list=[]
# for x in range(1,11):
#     some_list.append(x)
# print(some_list)


# some_list = [x for x in range(1,11) if x % 3 == 0]
# print(some_list)

a = ["Atabek", "Aktan", "Masha", "Amantay"]
some_dict = {item: len(item) for item in a}
print(some_dict)