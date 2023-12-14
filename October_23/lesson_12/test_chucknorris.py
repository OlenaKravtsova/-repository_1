import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # перев≥рити пол€ "icon_url" чи в≥н не пусти + чи це картинка,  - 2 теста
    # перев≥рити чи Ї ключ "value"  ≥ перев≥рити його значенн€ - 2 теста
    def test_check_year(self):
        assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"

    def test_status_code(self):
        assert self.status_code == 200



def test_category():
    URL = "https://api.chucknorris.io/jokes/categories"
    response = requests.request(method="GET", url=URL)
    print(response.json())

@pytest.mark.parametrize("category",
                         requests.request(method="GET", url="https://api.chucknorris.io/jokes/categories").json())
def test_categories(category):
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    response = requests.request(method="GET", url=URL)
    assert len(response.json()["id"]) == 22

# «робити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому ф≥кстуру
# тест на статус код
# тест на к≥льк≥сть жарт≥в
# тест на сам жарт
# + 3 тести