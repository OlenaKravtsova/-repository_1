import time

import pytest


def test_sleep_1():
    print("� ��� ����� �� 1 �������")
    time.sleep(1)


def test_wait_1():
    print("� �������� ����� 1 �������")
    time.sleep(1)


def test_sleep_2():
    print("� ��� ����� �� 1 �������")
    time.sleep(1)


def test_wait_2():
    print("� �������� ����� 1 �������")
    time.sleep(1)


def test_wait_3():
    print("� �������� ����� 1 �������")
    time.sleep(1)


def test_close_value():
    assert 3.1 == pytest.approx(3.1000001)


def test_close_value_2():
    assert 0.1 + 0.2 == pytest.approx(0.3)

#  pytest -m "smoke or regression" -v     ������ � �� � ��
#  pytest -m "smoke and regression" -v    ������ ���� �������� ������
#  pytest -m "not smoke" -v               ������ �� ���� smoke
#  pytest -k "wait" lesson_11/test_lesson_11.py  ������ �� ��������� �����
# pytest -s lesson_11/test_lesson_11.py ����� � �������

# pytest lesson_11/test_lesson_11.py -v -n=auto ������ � ����� ������ � ������������� ������� ������.
# pytest lesson_11/test_lesson_11.py -v -n=4   ��������� ������� ������.
# python3 -m pytest lesson_11/test_lesson_11.py -n=4 - �� ���� ������ ������ ���� ���� ������������,
# �������������� ���� ��������� �� ������.

# pytest -k "wait" lesson_11/test_lesson_11.py -v -n=3  - ����������

# flake8
# flake8 lesson_11/test_lesson_11.py ������ ���� �� ��������
# flake8 --ignore=E501 lesson_11/test_lesson_11.py - �������� ������� --ignore=E501