coding: 'utf-8'
import sqlite3
import pprint

connection = sqlite3.connect("../orders.db", isolation_level=None)  # isolation_level=None - потрібен що б відразу комітило
cursor = connection.cursor()

with open('Transaction_1.sql', 'r') as f:
    # Підключення до бази даних
    with sqlite3.connect('Transaction_1_database.db') as db:
        # Створення курсора
        cursor = db.cursor()

    # Читаємо кожен SQL-запит і виконуємо його окремо. Запустити 1-н раз, після того, як створена таблиця в файлі .sql
    #     for sql_statement in f.read().split(';'):
    #         if sql_statement.strip():
    #             cursor.execute(sql_statement)

cursor.execute("select * from Transaction_1;")
pprint.pprint(cursor.fetchall())

# cursor.execute("PRAGMA table_info(Transaction_1);")
# table_info = cursor.fetchall()
# pprint.pprint(cursor.fetchall())


# # Додати дані (дразу 2-ва рядки)
# cursor.execute("INSERT INTO Transaction_1 (Transaction_ID, Service_Id, Total_Cash, Receipt_Date) "
#                "VALUES (100011112, 2200, 500.00, '01.05.2024'), (100011113, 2, 150.00, '02.05.2024');")
# result = cursor.execute("select * from Transaction_1;")
# pprint.pprint(result.fetchall())


# # SQL-запит для видалення більше одного рядка по з ідентифікатору
# delete_query = "DELETE FROM Transaction_1 WHERE id in (2);"
# cursor.execute(delete_query) # Виконання SQL-запиту


# Зберігаємо зміни
db.commit()

# Закриваємо курсор
cursor.close()
