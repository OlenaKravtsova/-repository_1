coding: "utf-8"
# ����������� �������� � ���� ����� �� ������� ����
# word = "������"
# l_word = [1,23,4]
# print(word[::-1])
#
# # pop index del
# lis2 = ["dsfd", "fsdfds", "fdsf"]
# print(lis2)
# lis2.pop(1)
# print(lis2)


# # ������� � �������
# import copy
# product_list = [32,43,43]
# product_list_2 = copy.deepcopy(product_list)
# add_product = "few"
# product_list_2.append(add_product)
# print(f"Your purchase was updated: {product_list_2.append(add_product)}")  # �� ����� ���


# # ID
# list_a = [3,4]
# list_b = [3,4]
# print(id(list_a)) # 4506399488
# print(id(list_b)) # 4506399490


# # extend - ��������� ������ � ������ (�������� �� ������ ������)
# list_a = [0,1]
# list_b = ["fdfs", "fds"]
# list_a.append(list_b) # [0, 1, ['fdfs', 'fds']]
# list_a.extend(list_b) # [0, 1, 'fdfs', 'fds']
# print(list_a)
# list_12 = []
# list_22 = []
# list_12.append("�����")  # ['�����']
# list_22.extend("�����")  # ['�', '�', '�', '�', '�', '�']
# print(list_12)
# print(list_22)


# # remove ��������� �������� �� ����������� �������
# list_products = [3,"gh",5,"UI", "gh"]
# print(list_products)
# list_products.remove("gh")
# print(list_products)
# ����� �����ߪ Ҳ���� ������ ��������� ������� � Ͳ�� �� ������


# import math
# print(math.ceil(0.0001))
# print(math.floor(1.999))
# print(math.ceil(0.0001) == math.floor(1.999))
# print(abs(-10))  # �� ������


# ��������� - �������
# person_age = 10
# PENSION = 60


# a = "fdsf 2 dsfds 2 fdsf 2 fff"
# b = a.split("2")
# print(b)


# for in (break, continue), ���� ������ �� ����.
# for i in [1,2,3]:
#     print(i)
# print("finish")

# for i in "�����, �� ������?"[::2]:

# for i in "�����, �� ������?"[::2]:
#     print(i.upper())
# list_a = [12, 323, True, 545, "hfd", 6546, False, 654, 400.01, "hfd"]
# new_number_list = []
# print(list_a)
# for element in list_a:
#     element = str(element)
#     if element.isdigit():
#         new_number_list.append(int(element)/100)
#     elif element.isalpha():
#         if element == "True":
#             continue  # �������� �������� � ��� �� ���������� ��������
#         elif element == "False":
#             break  # ����� ���� �������
#         print(f"��� ������� = {element}")
# print(new_number_list)

list_a = [12, 323, True, 545, "hfd", 6546, 654, "hfd", 400.01]
new_number_list = []
print(list_a)
for element in list_a:
    if isinstance(element, (int, float)):
        new_number_list.append(element/100)
    elif isinstance(element, str):
        print(f"��� ������� = {element}")
# print(new_number_list)
#

# # todo ��� ����������� tuple �� list
# # tuple
# list_i = [3,4,5]
# tuple_i = (3,4,5)
# for i in tuple_i:
#     print(i)
# tuple_2 = tuple(list_i)
# print(tuple_i, type(tuple_i))
# print(tuple_2, type(tuple_2))
# list_b = list_i
# list_b = list(tuple(list_i))  #
# print(id(list_i))
# print(id(tuple_2))

import time

# while True:  # ��� Ͳ���� �� ������
#     time.sleep(1)
#     print(1)


# n = 0
# while n < 12:
#     n += 1  # equal n = n + 1
#     if n in (4, 5, 6):  # n == 4 or n == 5 ...
#         continue
#     print(f"{n} =  {n ** 2}")


# new_string = "+".join("����� �� � ���� ������")
# print(new_string)
# print(list_b)
# list_a = ["������", "������", "�������"]
# string_from_list = " ".join(list_a)
# print(string_from_list)


# �� �� ������� https://github.com/Pasha-lt/study/blob/main/format_and_join.py
# name = "�����"
# mid_name = "���������"
# balance = 15000000

# text = """�������� {0} {1}, ������ ������ ������� ������ {2} ���.""".format(name, mid_name, balance)
# print(text)

# text = """�������� {name} {mid_name}, ������ ������ ������� ������
# {name} ���.""".format(name=name, mid_name=mid_name, balance=balance)
# print(text)

# ������ DRY = don't repeat your self
# linkedin ���������. ����������� ���� ������ � ����.