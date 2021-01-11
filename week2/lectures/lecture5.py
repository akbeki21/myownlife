# a = set()
# print(type(a)

# a = set('string')
# print(a)          

# a = set([2, 1, 2, 3, 'a', 'a', 'b'])
# print(a)

# a = {'a', 'b', 'c', 'd'}
# a.add('d')                                        add only one element
# a.update({'d', 'f', 'l'}, {'h', 'r'})             adds many elements
# a.remove('a')                                     delete element, but there amy be error
# a.discard('a')                                    deletes elements
# a.pop()                                           deletes randomly, and returns deleted element
# lenght = len(a)
# print('a' not in a)                               False
# print('a' in a)                                   True


# a = {'a', 'b', 'c', 'd'}
# if 'd' in a:
#     a.remove('d')
# print(a)


# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# a = dancing.intersection(singing)                  shows common elements
# print(a)


# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing.difference(singing)                      shows the difference of one set fron another
# print(x)


# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing.symmetric_difference(singing)              shows all different elements                  
# print(x)


# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing.union(singing)                               shows all elements in one set
# print(x)

# print(dir(dancing))



# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha'}
# print(dancing.issuperset(singing))
# print(singing.issubset(dancing))

# '-' - difference
# '^' - symmetric difference
# '&' - intersection
# '|' - union

# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing|singing                               
# print(x)

# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing-singing                               
# print(x)

# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing^singing                               
# print(x)

# dancing  ={'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# singing = {'Syimyk', 'Masha', 'Adilet'}
# x = dancing&singing                               
# print(x)


# krujok1 = {'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# krujok2 = {'Syimyk', 'Masha', 'Adilet'}
# krujok3 = {'Mirbek', 'Dastan', 'Nikita'}
# x = krujok1 - krujok2 - krujok3
# print(x)


# krujok1 = {'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# krujok2 = {'Syimyk', 'Masha', 'Adilet'}
# krujok3 = {'Mirbek', 'Dastan', 'Nikita'}
# x = krujok3 & krujok1
# x = krujok1 ^ krujok2 ^ krujok3
# x = krujok1 | krujok2 | krujok3
# print(x)


# krujok1 = {'Masha', 'Sasha', 'Nikita', 'Syimyk', 'Aiperi'}
# krujok2 = {'Syimyk', 'Masha', 'Adilet'}
# krujok3 = {'Mirbek', 'Dastan', 'Nikita'}
# frozen_krujok1 = frozenset(krujok1)
# print(type(frozen_krujok1))



# even_numbers = {i for i in range(10) if i % 2 == 0}
# odd_numbers = {i for i in range(10) if i % 2 == 1}

# if even_numbers.isdisjoint(odd_numbers):
#     print(True)



# fibonacci_numbers = {0, 1, 2, 3, 34, 5, 8, 13, 21, 55, 89}
# natural_numbers = set(range(100))

# if fibonacci_numbers.issubset(natural_numbers):
#     print("Подмножество!")

# if natural_numbers.issuperset(fibonacci_numbers):
#     print("Надмножество!")



# В каком случае не создастся множетство?
# 1. a = {}
# 2. a = {1}
# 3. a = set(list(tuple([1]*10)))
# 4. a = {(1,), (2,)}
# 5. a ={
# 
# 
# 1, 2}




# Что выводит этот код?
print(set('abc') ^ set('bcd'))
1. set()
2. {'d', 'a'}
3. {'a', 'b', 'c', 'd'}
4. Будет ошибка