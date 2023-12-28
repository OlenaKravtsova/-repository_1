coding: "utf-8"

# Методи класу
# class Point:
#     color = 'red'  # атребут класа
#     circle = 2     # атребут класа
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point()
# pt.set_coords(1, 2)
# print(pt.__dict__)
# print(pt.get_coords())
# f = getattr(pt, "get_coords")
# print(f())


# Ініціфлизатор __init__ і філінізатор __del__

# class Point():
#     color = "red"
#     circle = 2
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# pt = Point(10, 20)
# print(pt.__dict__)

# # __new__
# class Point:
#     def __new__(cls, *args, **kwargs):
#         print("визвати __new__ для " + str(cls))
#         return super().__new__(cls)
#
#     def __int__(self, x=0, y=0):
#         print("визвати __init__ для " + str(self))
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 4)
# print(pt)

# Ініціалізація - початкові значення
# class DataBase:
#     __instance = None # силка на екземпляр класу
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#         return cls.__instance
#     def __del__(self):
#        DataBase.__instance = None
#
#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
#
#     def connect(self):
#         print(f"зєднання з БД: {self.user}, {self.psw}, {self.port}")
#
#     def close(self):
#         print("зачинене зєднання з БД")
#
#     def read(self):
#         return "дані з БД"
#
#     def write (self, data):
#         print(f"запис в БД {data}")
#
# db = DataBase("root", "1234", 80)
# db_2 = DataBase("root2", "15678", 40)
# # print(id(db), id(db_2))  # 26144744                         # 26144744
# db.connect()               # зєднання з БД: root2, 15678, 40  # зєднання з БД: root2, 15678, 40
# db_2.connect()


# class MyClass:
#     def __init__(self, value):
#         self.value = value
#
#     def __le__(self, other):
#         # Реалізація магічного методу __le__
#         return self.value <= other.value
#
# # Створення двох об'єктів класу MyClass
# obj1 = MyClass(5)
# obj2 = MyClass(10)
#
# # Перевірка за допомогою магічного методу __le__
# result = obj1 <= obj2
#
# # Виведення результату
# print(f"obj1 <= obj2: {result}")


# class Terminal:
#
#     def __init__(self, id_terminal, cashouts):
#         self.id_terminal = id_terminal
#         self.cashouts = cashouts
#
#     def __gt__(self, other):
#         return self.cashouts > other.cashouts
#
#     def __str__(self):
#         return f"Terminal {self.id_terminal}: {self.cashouts} грн"
#
# a1 = Terminal(1, 77)
# b1 = Terminal(2, 99)
# print(a1)
# print(b1)
#
# if a1 > b1:
#     print("В перешому терміналі проінкасована сума більша за суму другого трміналу")
# else:
#     print("В першому терміналі проінкасована сума Не більша за суму другого трміналу")






