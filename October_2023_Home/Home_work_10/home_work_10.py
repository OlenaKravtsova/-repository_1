# Оцінюються:
# Задача 1
# 1) Напишіть 10 тестів(можна що б просто повертали Тру(щоб проходили)) імена тестів повині йти підряд
# test_1, test_2 ... . Повішайти на них три декоратора old, main, new. кожен декоратор повинен бути на 3 функціях
# на одній з функцій повино бути повішано два декоратора old i main.
# додайти їх в python.ini що б були правильні виводи
#
# Зробіть такі прогони
# 1) всі тексти де немає лейби old
# py -m pytest -m "not old" -v
# 2) тест де пересікаються old i main.
# py -m pytest -m "old and main" -v
# 3) тести з маркерами main, new
# py -m pytest -m "old or main" -v
# З домашкою здайте скріншоти з прогонами, на скріншотах повино бути
# видно який саме тест прогнався(використовуйте прапор verbose).


# Задача 2
# Візьміть задачу з минулого уроку(
# 3) зробіть функцію як ми робили з додаванням тільки замість двох чисел зробіть три числа і протестуйте її всіма трьома методами
# ) модернізуйте її так що кожний раз коли ми її запускаємо те що ми туди передаєм та результат повинно записуватись в файл log.txt
# Зверніть увагу на те що в файл повинно дозаписуватись, а не затератись.
# Уявіть що ця функція являється легасі кодом і ви її не можете змінювати,
# тому потрібно використовувати декоратор. Я хотів би бачити таку реалізацію в домашці три функції:
# функція з минулого уроку
# функція що записую текст
# і декоратор

# Декоратор для логування
from datetime import datetime

def log_to_file(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("log.txt", "a") as log_file:  #, encoding='utf-8'
            log_file.write(f"Вхід: {args}, Результат: {result}, Час: {datetime.now()}\n")
        return result
    return wrapper

# Декоратор для виводу часу виконання функції
def func_wrapper_time(func):
    def wrapper(*args, **kwargs):
        log_file = datetime.now()
        result = func(*args, **kwargs)
        delta_time = datetime.now() - log_file
        print("Час виконання функції, такий: ", delta_time)
        return result
    return wrapper

# Застосовуємо обидва декоратори до функції add_three_numbers_and_log
@log_to_file
@func_wrapper_time
# Pytest parametrize
def add_three_numbers_and_log(number_1:int|float, number_2:int|float, number_3: int|float) -> int|float:
    result = number_1 + number_2 + number_3
    return result

# Не оцінюється
# Напишіть рекурсивну функцію яка приймає число і повертає добуток всіх чисел якщо віднімати мінус
# 1. тобто якщо передати в функцію 4 то в нас буде 4+3+2+1 = 10.
# def product_minus_one(number: int) -> int:
#     if number <= 1:
#         return 1
#     return number + product_minus_one(number - 1)
#
# print(product_minus_one(4))