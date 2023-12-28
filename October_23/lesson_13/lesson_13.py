coding: 'utf-8'
# # Наслідування
# class User:
#     name = "Taras"
#     _phone = "0931234567"  # protected
#
#     def say_hello(self):
#         return f"імя {self.name} телефон - {self._phone}"
#
# class Developer(User): # наслідування класу
#     program_language = "HTML"
#     english_level = "C1"
#
#     def say_hello(self):
#         return f"імя {self.name} телефон - {self._phone} Я багато заробляю"
#
# class Admin(User):
#     program_language = "Bash"
#
# class ThirdClass(Developer, Admin): # від першого наслідника візьмуться основні речі.
#     pass
#
#
# user_1 = User()
# user_2 = Developer()
#
# print(user_1.name)
# print(user_2.name)
# print(user_2.english_level)
# # print(user_1.english_level) # отримаємо помилку
# print(user_1.say_hello())
# print(user_2.say_hello())
#
# user_3 = ThirdClass()
# print(user_3.name)
# print(user_3.english_level)
# print(user_3.program_language)


# ПЕРЕЗАВАНТАЖЕННЯ МЕТОДІВ, тобто перезаписи
#
# class User2:
#     def __init__(self, name, age):
#         self.name = self.fix_name(name)
#         self.age = age
#
#     def fix_name(self, name):
#         self.name = name.title()
#         return self.name
#
#     def say_hello(self):
#         return f" привіт, я {self.name}"
#
# user_1_1 = User2("irina", 32)
# print(user_1_1.say_hello())
#
# user_1_2 = User2("Igor", 33)
# print(user_1_2.say_hello())

# todo init - це конструктор класу, в конструктор класу ще входить __prepare__, __new__, __init__

# class User2:
#     def __init__(self, name, age):
#         self.name = self.fix_name(name)
#         self.age = age
#
#     def fix_name(self, name):
#         self.name = name.title()
#         return self.name
#
#     def say_hello(self):
#         return f" привіт, я {self.name}"
#
#     def __str__(self): # те що потрібно для прінта print(user_1_1)
#         return f"я обєкт класу User2, моє імя {self.name}"
#
#     def __repr__(self): # це один метод виводу, який наглядно демонструє що все не треба вчити
#         return f"Моє імя {self.name}, Це не вчить"
#
# user_1_1 = User2("irina", 32)
# print(user_1_1.say_hello())
#
# user_1_2 = User2("Igor", 33)
# print(user_1_2.say_hello())
#
# print(user_1_1)


# Вилавлювати російські літери
# class WrongLang(Exception):
#     def __str__(self):
#         print("Ми не використовуємо рус мову.")
#
# class TextCreatоr():
#     def __init__(self, text):
#         self.text = text
#         for i in text:
#             if ord(i) in (1099, 1105, 1098, 1101):
#                 raise WrongLang
#
#     def __str__(self):
#         return f"{'*'*20} \n\n {self.text} \n {'*'*20}"
#
# test_1 = TextCreatоr("привіт, мене звуть Павло я займаюсь автоматизацією на Pthon")
# print(test_1)
# test_2 = TextCreatоr("привет, это Павел я занимаюсь автоматизацией на Pthon")
# print(test_2)


# Векторна математика

# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         self.x = x_coord
#         self.y = y_coord
#
# point_1 = Point(0, 1)
# point_2 = Point(10, 15)
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
# line_1 = Line(point_1, point_2)
#
# print(line_1.end.x)
# print(line_1.end.y)


# # Другий приклад
# class Point:
#     x = None
#     y = None
#
#     def __init__(self, x_coord, y_coord):
#         self.x = x_coord
#         self.y = y_coord
#
# point_1 = Point(0, 1)
# point_2 = Point(10, 15)
#
# class Line:
#     begin = None
#     end = None
#
#     def __init__(self, begin_point, end_point):
#         self.begin = begin_point
#         self.end = end_point
#
#     def __str__(self):
#         return (f"Наша лінія з початковими координатами {self.begin.x}:{self.begin.y}"
#                 f" та кінцевими координатами {self.end.x}:{self.end.y}")
#
# line_1 = Line(point_1, point_2)
#
# print(line_1)

# # Трансформувати bool в тип даних
# class A:
#     def __init__(self, text):
#         self.text = text
#
#     def __bool__(self):
#         print(len(self.text))
#         if len(self.text) < 20:
#
#             return False
#         return True
#
# a_1 = A("привіт")
# print(bool(a_1))
#
# a_2 = A("привіт, мене звуть Павло бла бла бла бла бла бла бла")
# print(bool(a_2))


# # Порівняння
# class A:
#     def __init__(self, text):
#         self.text = text
#
#     def __bool__(self):
#         print(len(self.text))
#         if len(self.text) < 20:
#
#             return False
#         return True
#
#     def __eq__(self, other): # ==
#         if not isinstance(other, type(self)):
#             raise TypeError
#
#
# # print((67 == 7))
# a = A("привіт")
# print(a == 7)


# Магічний спосіб  __eq__, abs, isinstance
# class A:
#     def __init__(self, text):
#         self.text = text
#
#     def __bool__(self):
#         print(len(self.text))
#         if len(self.text) < 20:
#
#             return False
#         return True
#
#     def __eq__(self, other): # ==
#         print(abs(len(self.text) - len(other.text)))
#         if not isinstance(other, type(self)):
#             raise TypeError
#         elif abs(len(self.text) - len(other.text)) < 10:
#             return True
#         else:
#             return False
#
# a = A("привіт")
# a_2 = A("привіт, мене звуть Павло бла бла бла бла бла бла бла бла")
# a_3 = A("привіт, мене звуть Павло бла бла бла бла бла бла бла")
# print(a == a_2)
# print(a_2 == a_3)

