coding: "utf-8"

class Student:
    def __init__(self, name="Oleg", grades=[2, 5]):
        self.name = name
        self.grades = grades

    def say_hello(self):
        print(f"Привіт, {self.name}!")

    def result_grades(self):
        print(f"Твої оцінки: {', '.join(map(str, self.grades))}")

# Створення двох екземплярів класу
obj_1 = Student()  # Залишаємо ім'я за замовчуванням ("Oleg")
obj_2 = Student(name="Olena")  # Змінюємо ім'я на "YourName"

# Виклик методів для обох екземплярів
obj_1.say_hello()
obj_1.result_grades()

obj_2.say_hello()
obj_2.result_grades()
