# 1) додайте requirements.txt на ваш гіт
# 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел
# зробіть три числа і протестуйте її всіма трьома методами
# 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює

# # 2) Виберіть будь-яку помилку яка вам подобається і зробіть функцію яка перевіряє на цю помилку(в функції try except)
#
# Функція для множення двох чисел
def multiply_numbers(number_1: str, number_2: str) -> int:
    """
    Перемножує два числа.
    Параметри:
    - number_1 (str): Перше число для множення.
    - number_2 (str): Друге число для множення.
    Повертає:
    int: Результат множення.
    """
    result = int(number_1) * int(number_2)
    return result

# Функція для створення рядка із результатом
def create_result_string(result: int) -> str:
    """
    Створює рядок із результатом множення.
    Параметри:
    - result (int): Результат множення.
    Повертає:
    str: Рядок із результатом.
    """
    new_string_1 = f"ваш добуток {result}"
    return new_string_1

# Обробки можливих помилок.
try:
    # Введення двох чисел
    result_mult = multiply_numbers(input("Enter your first number: "), input("Enter your second number: "))
    new_string = create_result_string(result_mult)
    print(result_mult)
except ValueError:
    print("Помилка: Будь ласка, введіть числа.")



# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел
# зробіть три числа і протестуйте її всіма трьома методами

# Pytest parametrize
def add_three_numbers(number_1:int|float, number_2:int|float, number_3: int|float) -> int|float:
    result = number_1 + number_2 + number_3
    return result


# # 4) перепишіть декоратор який заміряє час з уроку в домашку, можете його поклацати, як він працює
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
