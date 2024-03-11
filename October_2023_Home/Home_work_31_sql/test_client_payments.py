coding: 'utf-8'

import sqlite3
import pytest


@pytest.fixture
def db_connection_and_cursor():
    connection = sqlite3.connect('Payments.db')
    cursor = connection.cursor()
    yield cursor
    connection.close()


# Тест для перевірки вибірки даних транзакцій по сервісу 819
def test_service_payments(db_connection_and_cursor):
    select_payments_query = "SELECT Service_Id FROM ClientPayments WHERE Transaction_Id IN (100011111, 100011114);"
    db_connection_and_cursor.execute(select_payments_query)
    result = db_connection_and_cursor.fetchall()
    expected_result = [(819,), (819,)]

    assert result == expected_result


# Тест для перевірки суми платежів за 01.05.2024 більше, ніж за 02.05.2024
def test_payment_sum_comparison(db_connection_and_cursor):
    sum_01_05_query = "SELECT SUM(Total_Cash) FROM ClientPayments WHERE Receipt_Date = '01.05.2024';"
    db_connection_and_cursor.execute(sum_01_05_query)
    sum_01_05 = db_connection_and_cursor.fetchone()[0]

    sum_02_05_query = "SELECT SUM(Total_Cash) FROM ClientPayments WHERE Receipt_Date = '02.05.2024';"
    db_connection_and_cursor.execute(sum_02_05_query)
    sum_02_05 = db_connection_and_cursor.fetchone()[0]

    assert sum_01_05 > sum_02_05