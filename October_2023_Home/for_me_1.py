# 1. �� ��������� ��������� * �� ������ ���������� �� ��������� �-�� �� ���������� ��������
# �� ������ ������*
# *a, b, c = [True, 7, "hello", 9, 54, 8]
# print(a, b, c)

# *a, b, c = [2, 3]
# print(a, b, c)

# s = [4, 10]
# print(list(range(1, 5))) # [1, 2, 3, 4] - �������� ������
# # print(list(range(s)))    # - �������� ������� "TypeError: 'list' object cannot be interpreted as an integer"
# print(list(range(*s)))   # [4, 5, 6, 7, 8, 9] - �������� ������

# def f(a,b,c,d):
#     print(a,b,c,d)
# f(1,2,3,4)
# a = ("hello", True, 78, [3,4,5,9])
# f(*a)             # ��������� -> hello True 78 [3, 4, 5, 9]

# def f(*args):
#     print(args, type(args))
# f(1,2,3,4,5,6,7,8)  # ��������� -> ����������� � ������ ������� (1, 2, 3, 4, 5, 6, 7, 8)

# ���������� ���� ��� �����.
# def f(*args):
#     s = 0
#     for i in args:
#         s+=i
#     return s
# print(f(1, 2, 6))

# 2. �� ��������� ��������� ** �� ������ ���������� �� ��������� �-�� ���������� ��������
# def f(** kwargs):
#     print(kwargs)
# f(a=1, b=2, c=3) # ��������� -> ������������ �� ������ {'a': 1, 'b': 2, 'c': 3} �� ���� � ��������

# def f(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# f(a=1, b=2, c=3, name=89)
# ���������, �� ���� � ��������-> ������������ �� ������
# a 1
# b 2
# c 3
# name 89

# 3. ����� ��������������� 2-�� �������
# def f(*args,**kwargs):
#          print(args,kwargs)
# f(5,4,3,5,7,7,a=5,b=8,d=11,m="hello")
# # ��������� -> 5, 4, 3, 5, 7, 7) {'a': 5, 'b': 8, 'd': 11, 'm': 'hello'}

# �����������
# a = [3,5,7,8,9,1,0,5]
# print(*a)

#################################################################
# ���������
from datetime import datetime
# def func_wrapper_time(func):
#     def wrapper(*arg, **kwargs):
#         start = datetime.now()
#         result = func(*arg, **kwargs)
#         delta_time = datetime.now() - start
#         print("��� ��������� ������� ��� �����: ", delta_time)
#         return result
#     return wrapper()
#
# import time
# @func_wrapper_time
# def foo_1(*args, **kwargs):
#     print("foo_1")
#     time.sleep(1)
#
# @func_wrapper_time
# def foo_2(*arg, **kwargs):
#     print("foo_2")
#     time.sleep(2)
# foo_1()
# foo_2()
