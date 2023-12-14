# docstring   #докстрінг потрібний -  що робить ця функція і як з нею взаємодіяти
# def foo(number_1:int, number_2:int) -> int:
#     """
#     add two numbers
#     :param number_1 int: first number
#     :param number_2 int: second number
#     :return int: result add two number
#     """
#     result = number_1 + number_2
#     return result

# use default only when your func need it. Не ставимо дефолт і не використовуємо інпут в оголошенні функції!
# def foo(number_2:int, number_1:int = input("")) -> int: - так неможна!!!

# ENV and requirements.txt - коли беремо новий проект дивимося його релізи на pypi.org
#Відкриваємо пуск вказуємо cdm -> pip freeze -> вигружаються бібліотекі, які є, якщо немає якойсь бібліотеки,
# то треба вказати команду -> pip install requests -> дочекатися, коли інсталюється і повторно запустити ->
# pip freeze -> з'явиться бібліотека requests==2.31.0
# https://pypi.org/project/selenium/ -це сайт де можна знайти пакети для скачування та встановити бібліотекі по віртуалці

# Exceptions
# print(40/0)  # - отримаємо помилку -> ZeroDivisionError: division by zero
# try:
#     print(40/0)
# except ZeroDivisionError:
#     print("На нуль у пайтоні ділити не можна")

# try:
#     print(int("ghjgjkhj"))
# except (ZeroDivisionError, ValueError):  # ловимо декілька помилок
#     print("На нуль у пайтоні ділити не можна")

# Ми можемо ловити ексершени вверх по гіту

# value_1 = "0"
# value_2 = "jkfvhdj"
# try:
#     print(5/int(value_1))
# except ZeroDivisionError:
#     print("На 0 не ділиться в пайтоні")
# except ValueError:
#     print("Не можна зробити числом")

# value_1 = "0"
# value_2 = "jkfvhdj"
# try:
#     print(5/0)
# except Exception as e:
#     print("На 0 не ділиться в пайтоні")
#     print(f"we get error -> {e} <-")

# Pytest parametrize
def add_two_numbers(number_1:int|float, number_2:int|float) -> int|float:
    result = number_1 +number_2
    return result

type_1 = (1, 2, 3)
print(type(type_1), type_1)

type_2 = 1, 2, 3
print(type(type_2), type_2)

# decorator python
# def func_wrapper(func):
#     def wrapper(*arg, **kwargs):
#         print("before")
#         result = func(*arg, **kwargs)
#         print("after")
#         return result
#     return wrapper
# @func_wrapper
# def bar(*arg, **kwargs):
#     print("hello", arg, kwargs)

# # для розуміння
# wrapper_func = func_wrapper(bar)
# wrapper_func()

# випадок номер 2
# @func_wrapper
# def bar_1(*arg, **kwargs):
#     print("hello", arg, kwargs)
# @func_wrapper
# def bar_2(*arg, **kwargs):
#     print("hello", arg, kwargs)
#
# bar_1(333)
# bar_2(333)

# # Декоратор по часу
# from datetime import datetime
# def func_wrapper_time(func):
#     def wrapper(*arg, **kwargs):
#         start = datetime.now()
#         print(start)
#         result = func(*arg, **kwargs)
#         delta_time = datetime.now() - start
#         print("Час виконання функції, такий: ", delta_time)
#         return result
#     return wrapper
#
# import time
# @func_wrapper_time
# def foo_1(*args, **kwargs):
#     print("foo_1")
#     time.sleep(1)
#
# @func_wrapper_time
# def foo_2(*args, **kwargs):
#     print("foo_2")
#     time.sleep(2)
#
# foo_1()
# foo_2()