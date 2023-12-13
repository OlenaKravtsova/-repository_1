# Декораторів на функції можна вішати багато.
# Exception part 2
#На нуль у пайтоні ділити не можна
# try:
#     print(40/0)
# except:
#     print("На нуль у пайтоні ділити не можна")
# else:
#     print("Все ок")
#
# # Все ок
# try:
#     print(40/1)
# except:
#     print("На нуль у пайтоні ділити не можна")
# else:
#     print("Все ок")
# print("Все ок_2")

# try:
#     print(40/0)
# except:
#     print("На нуль у пайтоні ділити не можна")
#     exit()
# finally: #завжди відпрацює
#     print("finally")

# def foo(a: int) -> int:
#     if isinstance(a, int):
#         result = a ** 2
#         return result
#     else:
#         raise TypeError("В нашій програмі ми працюємо тільки з цілими числами")
# print(foo(3.17))
# # Результат:
# #     raise TypeError("В нашій програмі ми працюємо тільки з цілими числами")
# # TypeError: В нашій програмі ми працюємо тільки з цілими числами

# Якщо не хочемо отримати помилки, то треба добавити тип даних float
# def foo(a: int| float) -> int:
#     if isinstance(a, (int, float)):
#         result = a ** 2
#         return result
#     else:
#         raise TypeError("В нашій програмі ми працюємо тільки з цілими числами")
# print(foo(3.17))
# # Результат:
# #     raise TypeError("В нашій програмі ми працюємо тільки з цілими числами")
# # TypeError: В нашій програмі ми працюємо тільки з цілими числами

# Рекурсія - це функція яка визиває сама себе, у неї повинен бути 0 крок

# Вона рекурсивно викликає сама себе до тих пір, поки number не буде менше або рівне 1,
# і потім повертає добуток чисел від 1 до number.
# Приклад з фактаріалом
# def my_factorial(number: int) -> int:
#     if number <= 1:
#         return 1
#     return number * my_factorial(number - 1)
# print(my_factorial(5))
#
# # Метод фібаначі
# import functools
# @functools.lru_cache() # Зберігає попередні обрахунки і їх не потрібно ще раз обраховувати.
# def fib_res(number: int) -> int:
#     if number in (1, 2):
#         return 1
#     return fib_res(number - 1) + fib_res(number - 2)
# print(fib_res(6))

# list_a = [1,2,3,["f", "b",["434", 78]], 2, 5, 10, [12, 34, 54]]
# list_a2 = [1,2,3, 2, 5, 10, [12, 34, 54]]
# def dig_info_list(my_list: list) -> None:
#     for list_item in my_list:
#         if isinstance(list_item, list):
#             dig_info_list(list_item)
#         else:
#             print(list_item, end=" ")
# dig_info_list(list_a)
# print()
# dig_info_list(list_a2)
# print()
# dig_info_list([34, 43, 432])

# import
import lesson_10_import
# print(lesson_10_import.name) # Це результат  виводу з файла lesson-10_import

import random   # Вся бібліотека най пріоритетніший
# random.randint


from random import randint  #Імпорт конкретної функції
# randint

from random import randint as rrandint # Є можливість переїменувати функцію
# rrandint

from random import * # Імпортує всі функції == так не робіть

# Взаємодія з файлами
# file = open("text.txt", "r") # читання файла
# for i in file:
#     print(i)
#     print("---")
# file.close()

# with open("text.txt", "r") as file: #контекстний менеджер сам закриває. Краще закривати цим методом
#     for i in file:
#         print(i)
#         print("---")

# with open("text.txt", "w") as file:  # w- write затирає старий файл
#     file.write("Hello")

# with open("text.txt", "a") as file:  # a - дозаписати файл
#     file.write("\n")
#     file.write("++-+-=")

# Функціональне програмування
# map -
# a, b = map(int, input("введіть ціни: ").split()) # використовується, для то щоб користувач вніс всі ціни в одному запиті
# print(a, type(a))

# zip - зшиває, склеює пару
# list_1 = [1, 23, 4, 6, 43]
# list_2 = [0, 43, 4, 7]
# zipped = list(zip(list_1, list_2)) #[(1, 0), (23, 43), (4, 4), (6, 7)] <class 'list'>
# print(zipped, type(zipped))
#
# for i in zipped:
#     print(i)
#
# for i, j in zipped:
#     print(i,j)

# filter - Фільтр
list_1 = [1, 23, 4, 6, 43, 500, 1000, 999]
filtered = filter(lambda x: x%2 == 0, list_1)
print(type(filtered))
print(list(filtered))


