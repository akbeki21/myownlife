# LEGB = local >- enclosed >- global >- built-in
# 
#  1
# second_num = 5
# def outer():
#     first_num = 1

#     def inner():
#         second_num = 2
#         print('First number from outer - ', first_num)
#         print('Second num from inner - ', second_num)

#     inner()
#     print('Second num from global - ', second_num)

# outer()



# 2
# name = 'Bob'

# def func1():
#     global name
#     name = 'John'

#     def func2():
#         # nonlocal name
#         name = 'Sara'
#         print(locals())
#         print(name)

#     func2()
#     print(locals())
#     print(name)

# func1()
# print(globals())
# print(name)



# 3
# def factorial (num):
#     if num == 0:
#         return 1
    
#     return num * factorial(num - 1)

# print(factorial(4))


# 4.1
# def fib(num):
#     if num<= 1:
#         return num
#     a = 0
#     b = 1

#     for _ in range(num):
#         temp = a            # 0 1 1 2 3
#         a = b               # 1 1 2 3 5
#         b = b + temp        # 1 2 3 5 8 13
#     return a

# print(fib(8))


# 4.2
# def fib_rec(num):
#     if num <= 1:
#         return num
    
#     return fib_rec(num - 1) + fib_rec(num - 2)

# print(fib_rec(9))



# 5
# def sum_rec(num):
    # if num == 1:
    #     return num 
    # return num + sum_rec(num - 1)

# print(sum_rec(21))


