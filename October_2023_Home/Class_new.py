coding: "utf-8"
# Резюме:
# Інкапсуляція
# Наслудування
# Поліморфіз - це використання + з інтами, виконує математичну дію, з стрічками- відбувається склеювання
# getattr(obj, mane [, default]) - повертає значення атрибутів обєкта -> getattr(Student, 'a', False) або getattr(Student, "name");
# hasattr(obj, mane) - перевіряє на наявність атрибутів name в obj -> hasattr(Student, "prop") або hasattr (a, "name");
# setattr(obj, mane, value) - створює значення атрібута (якщо атрібута немає, то він створюється -> setattr(Student, 'prop', 88);
# delattr(obj, mane) - видаляє фтрібут з імям name -> delattr(Student, "type_pt") або del Student.prop;
# __doc__ - містить стрічку з описом класа -> Student.__doc__;
# __dict__ - містить набір атрібутів екземпляра класа -> Student.__dict__;

# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return (self.x, self.y)
#
# pt = Point()
# pt.set_coords(1,3)
# # print(pt.get_coords())
# f = getattr(pt, "get_coords")
# print(f())

# class Point:
#     color = "red"
#     circle = 2
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return (self.x, self.y)
#
# pt = Point():

class Student:
    name = "Oleg"
    grades = [2, 5]

    # Метод вітання зі студентом
    def say_hello(self):
        print(f"Привіт, {self.name}!")

    # Метод виводу оцінок
    def result_grades(self):
        print(f"Твої оцінки: {self.grades}")

# Створення першого екземпляра
obj_1 = Student()
obj_1.say_hello()
obj_1.result_grades()

# Створення другого екземпляра з власним ім'ям
obj_2 = Student()
obj_2.name = "Ваше_Ім'я"  # Замініть "Ваше_Ім'я" на своє ім'я
obj_2.say_hello()
obj_2.result_grades()
