# Как работать с Файлами:
# Связать файловую переменную с файлом, определив модификатор работы
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие для записи данных
# w+, r+

#with open('file.txt', 'w') as data: # атоматически прекашает дествия - таймер
#    data.write('line 1\n')
#    data.write('line 2\n')


#colors = ['red', 'geen', 'blue']
#data = open('file.txt', 'a')
##data.writelines(colors) # разделителей не будет
#data.write('\nLINE 2\n')
#data.write('LINE 3\n')
#data.close()


#path = 'file.txt'
#data = open(path, 'r')
#for line in data:
#    print(line)
#data.close() # блокировка - прекрашения дейстий

#import hello as h
#print(h.f(1))

# Функции
#def new_string(symbol, count):
#    return symbol * count

#print(new_string('!', 5))  # !!!!!
#print(new_string('!'))     # TypeError missing 1 required ...


#def new_string(symbol, count = 3):
#    return symbol * count

#print(new_string('!', 5))  # !!!!!
#print(new_string('!'))     # !!!
#print(new_string(4))       # 12

#def concatenation(*params):
#    res: str = 0
#    for item in params:
#        res += item
#    return res

#print(concatenatio('a', 's', 'd', 'w')) # asdw
#print(concatenatio('a', '1')) # a1
#print(concatenatio(1,2,3,4)) # TypeError: ...

# Типы:
# str - стороковый тип данных
# int = 0 - чифровой тип данных (Указание не обязательно)

# Рекурсия - вызывает сама себя

#def fib(n):
#    if n in [1,2]:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)

#list =[]
#for e in range(1, 10):
#    list.append(fid(e))
#print(list) # 1 1 2 3 5 8 13 21 34

# Кортежы

#a = (3, 1, 41, 4)
#print(a)
#print(a[-2])
#a[0] = 12 # нельзя добавить таким образом перезаписать (кортеж не изменяемый список)

##print(t[0])       # red
#print(t[2])       # blue
## print(t[10])   # IndexError: tuple index out of range
#print(t[-2])      # green
## print(t[-200]) # IndexError: tuple index out of range

#for e in t:
#    print(e)      # red green blue

#t[0] = 'black'    # TepeError: 'tuple' object does nit suppot i tem assignment

#t = tuple(['red', 'green', 'blue'])
#red, green, blue = t
#print('r:{} g:{} b:{}'.format(red, geen, blue))
## r:red g:green b:blue

# Словари
# Неупорядоченные коллекции произвольных объектов с доступом по ключу

#dictionary = {}
#dictionary = \
#    {
#        'up': '^',
#        'left': '<',
#        'down': '',
#        'right': '>',
#    }
#print(dictionary) # {'up':'^', 'left':'<', 'down':' ', 'right':'>'}
#print(dictionary['left']) # <
## типы ключей могут отличаться

# Множества

#colors = {'red', 'green', 'blue'}

#print(colors) # {'red', 'green', 'blue'}
#colors.add('red') # пытаясь добавить уже суш файл новый не создасться
#print(colors) # {'red', 'green', 'blue'}
#colors.add('gray') # новый не суш файл создасться
#print(colors) # {'red', 'green', 'blue', 'gray'}
#colors.remove('red') # здесь мы удаляем файл
#print(colors) # {'green', 'blue', 'gray'}
## colors.remove('red') # KeyError: 'red' # если файла такого нет выдаст ошибку
#colors.discard('red') # OK
#print(colors) # {'green', 'blue', 'gray'}
#colors.clear()    # { } # очищает  множество чтобы начать заново
#print(colors) # set()


#a = {1, 2, 3, 5, 8}
#b = {2, 5, 8, 13, 21}
#c = a.copy()           # c = {1, 2, 3, 5, 8}
#u = a.union(b)     # u = {1, 2, 3, 5, 8, 13, 21}
#i = a.intersection(b) # i = {8, 2, 5}
#dl = a.difference(b)  # dl = {1, 3}
#dr = b.difference(a)  # dr = {13, 21}

#q = a \
#    .union(b) \
#    .difference(a.intersection(b))
## {1, 21, 3, 13}

#s = frozenset(a)   # замороженое множество - неизменяемое

# Списки

#list1 = [1,2,3,4,5]
#list2 = list1

#for e in list1:
#    print(e)

#print()

#for e in list2:
#    print(e)

# Удаление последенего элемента в списке

#list1 = [1,2,3,4,5]

#print(list1) # Выводит элементы из сипка
##print(list1.insert(2, 11)) # добавляет новый элемент после указанного суш элеммента
##print(list1.append(11)) # добавляет новый элемент в конце списка
##print(list1.pop(2)) # убирает второй элемет из списка отсчет от 0 = 1 элемент в списке
#print(list1.pop()) # убирает  последнй элеммент из списка
#print(list1) # Выводит элементы из спискаа уже с изменениями
