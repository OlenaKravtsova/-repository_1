coding: 'utf-8'

import sqlite3

with sqlite3.connect('Payments.db') as db:
    cursor = db.cursor()

    create_table_query = """CREATE TABLE IF NOT EXISTS ClientPayments (
            Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            Terminal_Id INTEGER,
            Transaction_Id INTEGER,
            Service_Id INTEGER,
            Total_Cash FLOAT,
            Receipt_Date Date);"""
    cursor.execute(create_table_query)

    insert_data_queries = [
    "INSERT INTO ClientPayments (Terminal_Id, Transaction_Id, Service_Id, Total_Cash, Receipt_Date) VALUES"
    " (8746133, 100011111, 819, 100.00, '01.05.2024');",
    "INSERT INTO ClientPayments (Terminal_Id, Transaction_Id, Service_Id, Total_Cash, Receipt_Date) VALUES"
    " (8746133, 100011112, 2200, 500.00, '01.05.2024');",
    "INSERT INTO ClientPayments (Terminal_Id, Transaction_Id, Service_Id, Total_Cash, Receipt_Date) VALUES"
    " (8746133, 100011113, 2, 150.00, '02.05.2024');",
    "INSERT INTO ClientPayments (Terminal_Id, Transaction_Id, Service_Id, Total_Cash, Receipt_Date) VALUES"
    " (8746133, 100011114, 819, 150.00, '01.05.2024');"
    ]

    for requests in insert_data_queries:
        cursor.execute(requests)

    db.commit()
cursor.close()