coding: 'utf-8'
import pytest
from home_work_15 import Calculator
import datetime

# 3) Напишіть тестовий клас який буде тестити попередній калькулятор тільки додавання і ділення.
#  до кожної математичної дії зробіть 5 тестів(використовуйте параметрайз, не пишіть руками зайвого).
#  Зробіть класову фікстуру(класметод) для сетапа і тердауна сетпа буде писати повідомлення в файл коли ми запустили тест
#  та текстове повідомлення що ми стартанули. Тердаун буде писати повідомлення що ми закінчили і також час коли закінчили
#  використайте вже відому вам бібліотеку дататайм

# Фікстура для встановлення початкового часу перед запуском тестів
# та виведення повідомлення про старт тестів.
@pytest.fixture(scope="class")
def setup_teardown(request):
    start_time = datetime.datetime.now()
    print(f"\nStart time: {start_time}", end='\n')

# Тердаун для виведення часу завершення тестів та загального часу їх виконання.
    def teardown():
        end_time = datetime.datetime.now()
        print(f"\nEnd time: {end_time}")
        print(f"Total time: {end_time - start_time}", end='\n')
    request.addfinalizer(teardown)


@pytest.mark.usefixtures("setup_teardown")
class TestCalculator:

# Тести для додавання
    @pytest.mark.parametrize("value1, value2, expected_result", [
        (2, 3, 5),
        (-6, 4, -2),
        (-4, -4, -8),
        (5, 7, 12),
        (8, -8, 0),
    ]
                             )
    def test_addition(self, value1, value2, expected_result):
        calc = Calculator(value1, value2)
        result = calc.add()
        assert result == expected_result, f"Error in addition. Expected: {expected_result}, Got: {result}"


# Тести для ділення
    @pytest.mark.parametrize("value1, value2, expected_result", [
        (6, 3, 2),
        (-8, 4, -2),
        (16, 4, 4),
        (-25, -5, 5),
        (81, -9, -9)
    ]
                             )
    def test_division(self, value1, value2, expected_result):
        calc = Calculator(value1, value2)
        result = calc.divide()
        assert result == expected_result, f"Error in division. Expected: {expected_result}, Got: {result}"
