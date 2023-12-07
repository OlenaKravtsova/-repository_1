# docstring   #докстрінг потрібний -  що робить ця функція і як з нею взаємодіяти
def foo(number_1:int, number_2:int) -> int:
    """
    add two numbers
    :param number_1 int: first number
    :param number_2 int: second number
    :return int: result add two number
    """
    result = number_1 + number_2
    return result

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

try:
    print(int("ghjgjkhj"))
except (ZeroDivisionError, ValueError):  # ловимо декілька помилок
    print("На нуль у пайтоні ділити не можна")