import random
# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
right = len(max(fruits, key=len))
number_list = list(enumerate(fruits, start=1))
# print(number_list)
for i, fruit in number_list:
    print(f'{i}.{fruit}'.rjust(right))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list_a = random.sample(range(100),10)
list_b = random.sample(range(100),10)
for i in list_b:
    while i in list_a:
        list_a.remove(i)
print(list_a)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

# my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = random.sample(range(100), 10)
print(my_list)
for i in my_list:
    if i % 2 == 0:
        print(i / 4)
    else:
        print(i * 2)
