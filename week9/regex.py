import re

# . - любой символ, кроме \n 
# \d - любая цифра 0-9
# \D - любой символ, кроме цифр
# \s - любой пробельный символ
# \S - любой непробельный символ
# \w - любой символ, кроме спец.смволов (a-z, A-Z, 0-9, _)
# \W - любая не буква, не цифра, не подчеркивание
# \b - начало либо конец слова
# \В - в середине слова, не в начале и не в конце
# [az2] - любой символ в скобках


# квантификаторы :
# {n} - найти n количество повторений a подряд
# a{2} - 'aa'
# a{m, n} -  найти от m до n повторений а подряд
# a{2, 5} - 'aa', 'aaa', 'aaaa', 'aaaaa'
# a{m, }
# a{, n}




some_str = 'Today is a rainy day. Some say, it\'s not a good day to day hooraay'
# res = re.search('\w+ay', some_str)
# print(res[0])


# res = re.findall('\w+ay', some_str)
# print(res)

# result = re.split('\w+ay', some_str)              
# print(result)

result = re.sub('\w+ay', 'xxxx', some_str)           # заменяет первое значение на второе
print(result)