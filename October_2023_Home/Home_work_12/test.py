coding: 'utf-8'
import requests
import pytest

# перевірити поля "icon_url" чи він не пустий + чи це картинка,  - 2 теста
# перевірити чи є ключ "value"  і перевірити його значення - 2 теста
# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

# https://api.chucknorris.io/jokes/random - радномний жарт
# https://api.chucknorris.io/jokes/random?category={category} - відпраити якусь категорію та отримати категорію жартів
# ttps://api.chucknorris.io/jokes/categories - отримати список наших категорій
# https://api.chucknorris.io/jokes/search?query={query} - отримати текстовий запит


# @pytest.mark.usefixtures("fixture_random")
# class TestRandom:
#
#     def test_icon_url_not_empty(self):
#         # Тест 1: Перевірка, чи "icon_url" не порожній
#         assert self.response.json()["icon_url"], "'icon_url' is empty"
#
#     def test_icon_url_is_image(self):
#         # Тест 2: Перевірка, чи "icon_url" є посиланням на зображення
#         icon_url = self.response.json().get("icon_url")
#         image_extensions = [".jpg", ".jpeg", ".png"]
#         assert any(icon_url.endswith(ext) for ext in image_extensions), "'icon_url' is not an image URL"
#
#     def test_value_key_exists(self):
#         # Тест 3: Перевірка, чи існує ключ "value" в об'єкті жарту
#         assert "value" in self.response.json(), "Key 'value' does not exist"
#
#     def test_value_not_empty(self):
#         # Тест 4: Перевірка, чи значення ключа "value" не порожнє
#         assert self.response.json()["value"], "Value of 'value' is empty"
#
#     def test_check_year(self):
#         assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"
#
#     def test_status_code(self):
#         assert self.status_code == 200
#
#
# def test_category():
#     URL = "https://api.chucknorris.io/jokes/categories"
#     response = requests.request(method="GET", url=URL)
#     print(response.json())
#
#
# @pytest.mark.parametrize("category",
#                          requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
# def test_categories(category):
#     URL = f"https://api.chucknorris.io/jokes/random?category={category}"
#     response = requests.request(method="GET", url=URL)
#     assert len(response.json()["id"]) == 22

# class ChuckNorrisJokeSearch:
#     BASE_URL = "https://api.chucknorris.io/jokes/search"
#
#     def __init__(self, query):
#         self.query = query
#
#     def get_jokes(self):
#         response = requests.get(f"{self.BASE_URL}?query={self.query}")
#         return response
#
# # Фікстура для пошуку жарту за конкретним словом
# @pytest.fixture
# def fixture_joke_search():
#     joke_search = ChuckNorrisJokeSearch("Chuck")  # Замініть "python" на ваш запит
#     return joke_search.get_jokes(), joke_search.get_jokes().status_code
#
# # Клас тестів для пошуку жарту за конкретним словом
# class TestJokeSearch:
#
#     @pytest.mark.usefixtures("fixture_joke_search")
#     def test_status_code(self, fixture_joke_search):
#         response, status_code = fixture_joke_search
#
#         # Тест: Перевірка, чи статус код дорівнює 200
#         assert status_code == 200, f"Unexpected status code: {status_code}"
#
# # Виклик класу тестів
# test_joke_search_instance = TestJokeSearch()
# test_joke_search_instance.test_status_code()