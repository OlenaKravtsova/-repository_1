# -*- coding: utf-8 -*-
coding: 'utf-8'

import random
import string


def generate_password_and_print():
    print("Виберіть типи символів для паролю:")
    print("1. Кирилиця (тільки малі літери)")
    print("2. Кирилиця (тільки великі літери)")
    print("3. Латиниця (тільки малі літери)")
    print("4. Латиниця (тільки великі літери)")
    print("5. Цифри")
    print("6. Великі та малі літери Кирилиця/Латиниця")

    user_choice = input("Введіть номери вибраних типів символів (без пробілів): ")
    length = int(input("Введіть довжину паролю: "))

    alphabet = ""
    if '1' in user_choice:
        alphabet += ''.join([chr(i) for i in range(1072, 1104)])  # кирилиця (тільки малі літери)
    if '2' in user_choice:
        alphabet += ''.join([chr(i) for i in range(1040, 1072)])  # кирилиця (тільки великі літери)
    if '3' in user_choice:
        alphabet += string.ascii_lowercase  # латиниця (тільки малі літери)
    if '4' in user_choice:
        alphabet += string.ascii_uppercase  # латиниця (тільки великі літери)
    if '5' in user_choice:
        alphabet += string.digits  # цифри
    if '6' in user_choice:
        alphabet += ''.join([chr(i) for i in range(1040, 1104)]) + string.ascii_letters  # великі та малі літери Кирилиця/Латиниця

    if not alphabet:
        print("Виберіть хоча б один тип символів.")
        return

    password = ''.join(random.choice(alphabet) for _ in range(length))
    print("Згенерований пароль:", password)

generate_password_and_print()
