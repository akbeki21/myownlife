# print('Hello world')
# input()
# len()                возвращает количество элементов обьекта
# range()              диапазон чисел
# dir()                возвращает список свойств и методов обьекта
# id()
# int(), str(), tuple(), set(), list(), float()
# type()               возвращает тип обьекта
# sorted()             возвращает отсортированный список, не изменяя исходный обьект
# bool()



# all()           Проверяет все ли обьекты True, влзвращает булевое значение
# nums = [12, 5, 3, 56, 8, 3]
# print(all(nums))


# any()           Проверяет есть ли хотя бы одна истинна, возвращает булевое значение           
# nums = [12, 5, 3, 56, 8, 3]
# Print(any(nums))
 

# abs()           Возвращает модуль числа
# number = -5
# print(abs(number))


# nums = [12, 5, 3, 56, 8, 3]
# def any_custom(iterable_obj):
#     for x in iterable_obj:
#         if x:
#             return True
#         return False
    
# print(any_custom(nums))


# nums = [12, 5, 3, 56, 8, 3]
# def any_custom(iterable_obj):
#     print(x)
#     for x in iterable_obj:
#          if not x:
#             return False
#         return True
    
# print(any_custom(nums))



# min()
# nums =[1, 2, 3, 4, 5, -1]
# print(min(nums))

# max()
# nums =[1, 2, 3, 4, 5, -1]
# print(max(nums))



# ord()          возвращает значение из таблицы ASCI
# print(ord('d'))


# chr()          обратная функция ord
# print(chr(100))


# sum()
# print(sum((1, 4, 3)))


# divmod()              возвращает tuple: частное и остаток от деления
# print(divmod(7, 3))




# def func(num):
#     res = divmod(num, 30)
#     fiftith = res[0]
#     res = divmod(res[1], 10)
#     tenth = res[0]
#     ones = res[1]
#     return f"Argument - {num},\nfiftith - {fiftith},\ntenth - {tenth}, \nones - {ones}"

# print(func(88))



# eval()                  преобразует строку в питоновский код
# str_ = '2 + 2'
# print(eval(str_))



# enumerate()             возвращает итератор
# some_string = 'Hello world'
# for x, y in enumerate(some_string, 1):
#     print(x, y)


# index = 0
# for x in range(len(some_string)):
    # print(x, some_string[x])


# zip()
# some_string = 'abcd'
# some_list = [1, 2, 3]
# res = dict(zip(some_string, some_list))
# print(res)





def count_valleys(step, path):
    position = 0
    valleys = 0
    for x in range(step):
        if position == -1 and path[x]  'U'