# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
#
# def user_info(name,age,city):
#     return (f'{name},{age} лет,проживает в городе {city}')
#
#
# # Задание - 2
# # Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них
#
# def my_max(a,b,c):
#     if a > b and a > c:
#         max_number = a
#     elif b > a and b > c:
#         max_number = b
#     else:
#         max_number = c
#     return max_number
#
# def my_max(a,b,c):
#     max_number = a
#     for i in (a,b,c):
#         if i > max_number: max_number = i
#     return max_number


# Задание - 3
# Создайте функцию, принимащую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
def my_func(*args):
    return (max(args,key=len))





print(my_func('dsdsdsss','dsd','2232412313123','dsfsdfggdjsdsag'))

