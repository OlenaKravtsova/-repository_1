coding: 'utf-8'

import sqlite3
import pytest


@pytest.fixture
def db_connection():
    connection = sqlite3.connect('Payments.db')
    yield connection
    connection.close()


# Тест для перевірки вибірки даних транзакцій по сервісу 819
def test_service_payments(db_connection):
    cursor = db_connection.cursor()

    select_payments_query = "SELECT Service_Id FROM ClientPayments WHERE Transaction_Id IN (100011111, 100011114);"
    cursor.execute(select_payments_query)
    result = cursor.fetchall()
    expected_result = [(819,), (819,)]

    assert result == expected_result

    cursor.close()


# Тест для перевірки суми платежів за 01.05.2024 більше, ніж за 02.05.2024
def test_payment_sum_comparison(db_connection):
    cursor = db_connection.cursor()

    sum_01_05_query = "SELECT SUM(Total_Cash) FROM ClientPayments WHERE Receipt_Date = '01.05.2024';"
    cursor.execute(sum_01_05_query)
    sum_01_05 = cursor.fetchone()[0]

    sum_02_05_query = "SELECT SUM(Total_Cash) FROM ClientPayments WHERE Receipt_Date = '02.05.2024';"
    cursor.execute(sum_02_05_query)
    sum_02_05 = cursor.fetchone()[0]

    assert sum_01_05 > sum_02_05

    cursor.close()