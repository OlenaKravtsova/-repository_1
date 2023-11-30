# багато домашки, ні не багато
# пробіл в кінці коду POSIX, git merge, компілятор


# формат і ф стрінг
# Ще одне форматування з відсотками
# name, mid_name, balance = 'Ігор', 'Васильович', 32.56
# text = "Шановний %s %s, баланс вашого рахунку складає %s грн." %(name, mid_name, balance)
# print(text)


# range що б сформувати список, щоб в форі пройти певну кількість кроків.
# range_1 = range(2, 11, 2)
# print(range_1)
# print(list(range_1))

# case 1 range
# number = int(input("введіть до скількох ви хочте порахувати"))
# for i in range(number):
#     print(i + 1)

# list_a = [0, 30, 2]

# for i in range(*list_a):  # в майбутньому розберемо
#     print(i)

# a = 2; b = 16; c = 2
# for i in range(a, b, c):  # підставляємо зміні
#     print(i)

# list_a = [777, 30, 21, 43, 13, 23, 43]

# замісь цього
# for i in range(7):  # Не використовуємо рендж коли проходимось по індексам
#     print(list_a[i])

# пиши це
# for i, j in enumerate(list_a):
#     print(f"{i=}, {j=}")

# коли треба назначити елемент але його не використовувати пишемо нижнє підкреслення(_)
# list_a = [777, 30, 21, 43, 13, 23, 43]
# for _, j in enumerate(list_a):
#     print(j)

# for i in for, while, чого не можна на ходу міняти ліст, else != break
# list_a = [2, 34, 45, 65, 765, 88, 5, 66]
# for i in list_a:
#     if i == 5:
#         print("we find it", i)
#         break
#     else:
#         print(i)
# else:
#     print("ми не знайшли 5")

# counter = 0
# while counter < 20:
#     if counter == 5:
#         print("we find it", counter)
#         break
#     else:
#         print(counter)
#     counter += 2 # якщо вказати 1 - то 5-ку знайде
# else:
#     print(counter, " - не знайдено")

# це впринципі нормально але будь ласка уникайте такого
# list_a = [2, 34, 45, 65, 765, 88, 5, 66]
# print(list_a)
# for index, value  in enumerate(list_a):
#     list_a[index] = value * 2
# print(list_a)

# МИ НЕ ВЗАЄМОДІЄМО З ТИМ СПИСКОМ ПО ЯКОМУ ПРОХОДИМОСЬ, якщо треба то записуємо в новий список.
# Приклад 1 - Неправильний
# list_a = [2, 34, 45, 65, 765, 88, 5, 66]
# print(list_a)
# for i in list_a:
#     if i % 2 == 1:
#         list_a.append(i*3)

# Приклад 2 - Правильний
# list_a = [2, 34, 45, 65, 765, 88, 5, 66]
# print(list_a)
# list_b = []
# for i in list_a:
#     if i % 2 == 1:
#         list_a.append(i*2)
#     else:
#         list_b.append(i)
# print(list_b)

# приклад 2  - Правильний
# a = ["a", "b", "c", "d", "e", "y"]
# b = a[:]
# for i in b:
#     del_item = a.pop(0)
#     print(del_item)
#     print(a, i)


# set - приймає тільки не зміні типи даних. Зміний тип даних. SET - mutable, FROZENSET - immutable
# set_a = {3, 4, 5, 6, 6, 3, 4, 5, (3,4,5), 90}
# print(set("djfjdsjkdshfkdjshfdkjhkd fdfdsfh dkjfhds"))
# print(set_a, type(set_a))
# # empty_set = set()
# # list_a = [3, 4, 5, 6, 6, 3, 4, 5]
# # print(list(set(list_a)))  # єдиний варіант запису
#
#
# list_a = [3, 4, 5]
# tuple_a = (3, 4, 5)
# set_a = {3, 4, 5}
#
# #  __sizeof__() - скільки займає памяті
# print(list_a.__sizeof__())  # 72 - кількість методів
# print(tuple_a.__sizeof__())  # 48 - кількість методів
# print(set_a.__sizeof__())  # 200 - кількість методів
#
# # dir - подивитись методи
# print(dir(list_a))
# print(dir(tuple_a))
# print(dir(set_a))


# цикл в циклі
# for i in range(2, 10):
#     for j in range(2, 10):
#         print(f"{i}*{j}={i*j}", end=" ")
#     print()


# KISS - keep it simple - пишемо просто, не пишемо зайвого


# DICT записати. Ліва частина це ключ "Павло" (він хешується) не змінний тип данних (tuple, set) не мо,
# права частина це значення (може бути зміний або не змінний тип данних (str,int,dict, set)
# dict_1 = {}
# dict_2 = dict()
# dict_3 = dict(city="Odesa", village="Myrne")
# dict_4 = dict([(1, 2), ("key", "value")])
# dict_5 = dict.fromkeys([3,4,5], "None")
# dict_6 = {"Павло":["AQA", "Python"], "Dmytro":["DevOps", "bash"]}  # найпоширеніший
# dict_6.update(dict(height='720', blah='blah-blah'))                # можливість добавти деклька ключів і елементів в існуючий словник
# dict_6 ["Олена"] = "table_addition"

# print(dict_1, type(dict_1))
# print(dict_2, type(dict_2))
# print(dict_3, type(dict_3))
# print(dict_4, type(dict_4))
# print(dict_5, type(dict_5))
# print(dict_6, type(dict_6))


# dict_6 = {"Павло":["AQA", "Python"], "Dmytro":["DevOps", "bash"]}
# print(dict_6["Павло"])
# print(dict_6.get("Павло", "немає такого"))  # краще перевіряти так, що б ваша программа не впала з помилкою
# print(dict_6.get("Dmytro2", "немає такого"))  # краще перевіряти так, що б ваша программа не впала з помилкою
# print(dict_6)
# dict_6["Павло"].append("AWS")  # додавання в значення
# print(dict_6)
# dict_6["Павло"] = ["PM"]  # зміна зміної (перезапис)
# print(dict_6)
# dict_6["Dmytro"][1] = "AWS"  # зміна значення в списку
# print(dict_6)



# # hash - може бути використаний тільки для не змінних типів даних.
# list_a = "[]"
# print(hash(list_a))
# !!! Чи може бути ключом set - відповідб ні, не може, так як має змінний тип даних
# !!! Чи може бути значення set-том - відповідб так
# !!! Чи може бути стрічка ключом у словнику - відповідб так
# !!! Чи може бути ліст ключом у словнику - відповідб ні, тому що він змінний тип даних
# !!! Чи може бути dict значенням ключа - відповідь так
# !!! Чи може бути dict ключем у словнику - відповідь ні
# !!! Які типи данних в пайтоні є - змінні і незмінні
# Які змінні типи данних - це лист, сет, дікт
