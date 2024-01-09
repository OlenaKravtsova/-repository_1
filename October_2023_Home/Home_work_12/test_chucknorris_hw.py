import pytest
import requests


# перевірити поля "icon_url" чи він не пустий + чи це картинка,  - 2 теста
# перевірити чи є ключ "value"  і перевірити його значення - 2 теста
@pytest.mark.usefixtures("fixture_random")
class TestRandom:

    def test_icon_url_not_empty(self):
        # Тест 1: Перевірка, чи "icon_url" не порожній
        assert self.response.json()["icon_url"], "'icon_url' is empty"

    def test_icon_url_is_image(self):
        # Тест 2: Перевірка, чи "icon_url" є посиланням на зображення
        icon_url = self.response.json().get("icon_url")
        image_extensions = [".jpg", ".jpeg", ".png"]
        assert any(icon_url.endswith(ext) for ext in image_extensions), "'icon_url' is not an image URL"

    def test_value_key_exists(self):
        # Тест 3: Перевірка, чи існує ключ "value" в об'єкті жарту
        assert "value" in self.response.json(), "Key 'value' does not exist"

    def test_value_not_empty(self):
        # Тест 4: Перевірка, чи значення ключа "value" не порожнє
        assert self.response.json()["value"], "Value of 'value' is empty"

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



# Зробити окремий клас
# пошук жарту по конретному слову  https://api.chucknorris.io/jokes/search?query={query}
# зробити класому фікстуру
# тест на статус код
# тест на кількість жартів
# тест на сам жарт
# + 3 тести

@pytest.mark.usefixtures("fixture_search")
class TestSearch:

# Тест, пошук жарту по конретному слову "internet"
    def test_search_result_contains_query(self):
        query = "internet"
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert query.lower() in joke["value"].lower(), f"Search result does not contain '{query}'"

# Тест на статус код
    def test_search_status_code(self):
        assert self.status_code == 200

 # Тест, чи кількість жартів у відповіді співпадає зі значенням "total"
 # у відповіді https://api.chucknorris.io/jokes/search?query=jokes
    def test_number_of_search_results_with_keyword(self):
        query = "jokes"
        data = self.response.json()
        # Отримання фактичної кількості жартів у відповіді
        actual_number_of_jokes = len(data["result"])
        # Отримання кількості жартів, вказаної в полі "total" у відповіді
        expected_number_of_jokes = data["total"]
        # Перевірка, чи кількість жартів співпадає зі значенням "total"
        assert actual_number_of_jokes == expected_number_of_jokes


# Перевірка, чи конкретний жарт присутній в результатах пошуку
    def test_specific_joke_present(self):
        specific_joke = "Chuck Norris tells black jokes without looking over his shoulder"
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert any(specific_joke.lower() in joke["value"].lower() for joke in
                        jokes), "Specific joke is not present in the search results"

# Тест, чи кожен жарт має ідентифікатор (ключ "id")
    def test_each_joke_has_id(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "id" in joke, "Joke does not have an 'id' key"


# Тест, чи кожен жарт має категорії (ключ "categories")
    def test_each_joke_has_categories(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "categories" in joke, "Joke does not have a 'categories' key"


# Тест, чи кожен жарт має URL (ключ "url")
    def test_each_joke_has_url(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "url" in joke, "Joke does not have a 'url' key"
