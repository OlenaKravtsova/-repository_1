coding: 'utf-8'

# Виберіть який з наступних магічних методів і реалізуйте його в простому класі:
# __ne__: To check if two objects are not equal. !=
# __lt__: To check if one object is less than another. <
# __le__: To check if one object is less than or equal to another.
# __gt__: To check if one object is greater than another. >
# __ge__: To check if one object is greater than or equal to another.
# Жодного з цих методів ми не розглядали на уроці, але вони працюють ідентично до метода ___eq__ який ми розглянули на
# уроці. Тобто вам треба буде змінити всього дві букви.
# І написати свою логіку яку ви хочете.
# Створіть два обьєта класа в якому ви це реалізували і зробіть перевірку що все працює

# # __ne__: To check if two objects are not equal.
# # Створення класу
# class Terminal:
#
#     def __init__(self, terminal_id=None, amount_collected=None):
#         """Метод __init__ - створення нового об'єкту класу"""
#         self.terminal_id = terminal_id
#         self.amount_collected = amount_collected
#
# # Магічний метод __en__ -> !=
#     def __ne__(self, other):
#         """Перевірка, чи не рівні об'єкти"""
#         return self.terminal_id != other.terminal_id or self.amount_collected != other.amount_collected
#
#     def calculate_difference(self, other):
#         """Обчислення різниці у сумах коштів"""
#         return abs(self.amount_collected - other.amount_collected)
#
#
# # Створення двох об'єктів класу Terminal
# event1 = Terminal(8746165, 10000)
# event2 = Terminal(8746177, 22000)
#
# # Виведення різниці у сумах коштів
# difference = event1.calculate_difference(event2)
# print(f"Різниця у сумах коштів: {difference} грн")
#
# # Порівняння сум коштів в терміналах
# if event1 != event2:
#     print("Суми коштів в терміналах не рівні.")
# else:
#     print("Суми коштів в терміналах рівні.")





# # __lt__: To check if one object is less than another.
# # Створення класу
# class Terminal:
#     def __init__(self, terminal_id=None, amount_collected=None):
#         self.terminal_id = terminal_id
#         self.amount_collected = amount_collected
#
#     def __lt__(self, other):
#         """Перевірка, чи один об'єкт менший за інший"""
#         return self.amount_collected < other.amount_collected
#
#     def __str__(self):
#         """Представлення об'єкта у текстовому форматі"""
#         return f"Terminal {self.terminal_id}: {self.amount_collected} грн"
#
# # Створення двох об'єктів класу Terminal
# event1 = Terminal(8746176, 9000)
# print(event1)
# event2 = Terminal(8746177, 15000)
# print(event2)
#
# # Порівняння за допомогою <
# if event1 < event2:
#     print("Перший термінал має менше проінкасованих коштів за другий.")
# else:
#     print("Перший термінал має не менше проінкасованих коштів за другий.")



# #__gt__: To check if one object is greater than another.
# # Створення класу
# class Terminal:
#     def __init__(self, terminal_id=None, amount_collected=None):
#         self.terminal_id = terminal_id
#         self.amount_collected = amount_collected
#
#     def __gt__(self, other):
#         """Перевірка, чи один об'єкт більше за інший"""
#         return self.amount_collected > other.amount_collected
#
#     def __str__(self):
#         """Представлення об'єкта у текстовому форматі"""
#         return f"Terminal {self.terminal_id}: {self.amount_collected} грн"
#
# # Створення двох об'єктів класу Terminal
# event1 = Terminal(8746176, 19000)
# print(event1)
# event2 = Terminal(8746177, 15000)
# print(event2)
#
# # Порівняння за допомогою >
# if event1 > event2:
#     print("Перший термінал має більше проінкасованих коштів за другий.")
# else:
#     print("Перший термінал має не більше проінкасованих коштів за другий.")




# # __le__: To check if one object is less than or equal to another -> <=.
# # __ge__: To check if one object is greater than or equal to another -> >=.
# # Створення класу
# class Payments:
#     terminal_id = 8745555
#
#     def __init__(self, id_services, number_of_transactions):
#         self.id_services = id_services
#         self.number_of_transaction = number_of_transactions
#
#     def __le__(self, other):
#         """Порівнює об'єкти за кількістю транзакцій"""
#         return self.number_of_transaction <= 300 and other.number_of_transaction <= 300
#
#     def __ge__(self, other):
#         """Порівнює об'єкти за кількістю транзакцій"""
#         return self.number_of_transaction >= 300 and other.number_of_transaction >= 300
#
#     def __str__(self):
#         """Представлення об'єкта у текстовому форматі"""
#         return f"Payments {self.terminal_id}: {self.id_services}: {self.number_of_transaction} шт."
#
# # Створення двох об'єктів класу Payments
# first_service = Payments(1, 299)
# print(first_service)
# second_service = Payments(2, 300)
# print(second_service)
#
# # Порівняння
# result = first_service <= second_service
# print(result)
#
# # Виведення результату порівняння
# if result:
#     print(f"{first_service} <= {second_service}")
# else:
#     print(f"{first_service} > {second_service}")






