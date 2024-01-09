import pytest
import requests


# ��������� ���� "icon_url" �� �� �� ������ + �� �� ��������,  - 2 �����
# ��������� �� � ���� "value"  � ��������� ���� �������� - 2 �����
@pytest.mark.usefixtures("fixture_random")
class TestRandom:

    def test_icon_url_not_empty(self):
        # ���� 1: ��������, �� "icon_url" �� �������
        assert self.response.json()["icon_url"], "'icon_url' is empty"

    def test_icon_url_is_image(self):
        # ���� 2: ��������, �� "icon_url" � ���������� �� ����������
        icon_url = self.response.json().get("icon_url")
        image_extensions = [".jpg", ".jpeg", ".png"]
        assert any(icon_url.endswith(ext) for ext in image_extensions), "'icon_url' is not an image URL"

    def test_value_key_exists(self):
        # ���� 3: ��������, �� ���� ���� "value" � ��'��� �����
        assert "value" in self.response.json(), "Key 'value' does not exist"

    def test_value_not_empty(self):
        # ���� 4: ��������, �� �������� ����� "value" �� ������
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



# ������� ������� ����
# ����� ����� �� ���������� �����  https://api.chucknorris.io/jokes/search?query={query}
# ������� ������� ��������
# ���� �� ������ ���
# ���� �� ������� �����
# ���� �� ��� ����
# + 3 �����

@pytest.mark.usefixtures("fixture_search")
class TestSearch:

# ����, ����� ����� �� ���������� ����� "internet"
    def test_search_result_contains_query(self):
        query = "internet"
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert query.lower() in joke["value"].lower(), f"Search result does not contain '{query}'"

# ���� �� ������ ���
    def test_search_status_code(self):
        assert self.status_code == 200

 # ����, �� ������� ����� � ������ ������� � ��������� "total"
 # � ������ https://api.chucknorris.io/jokes/search?query=jokes
    def test_number_of_search_results_with_keyword(self):
        query = "jokes"
        data = self.response.json()
        # ��������� �������� ������� ����� � ������
        actual_number_of_jokes = len(data["result"])
        # ��������� ������� �����, ������� � ��� "total" � ������
        expected_number_of_jokes = data["total"]
        # ��������, �� ������� ����� ������� � ��������� "total"
        assert actual_number_of_jokes == expected_number_of_jokes


# ��������, �� ���������� ���� �������� � ����������� ������
    def test_specific_joke_present(self):
        specific_joke = "Chuck Norris tells black jokes without looking over his shoulder"
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert any(specific_joke.lower() in joke["value"].lower() for joke in
                        jokes), "Specific joke is not present in the search results"

# ����, �� ����� ���� �� ������������� (���� "id")
    def test_each_joke_has_id(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "id" in joke, "Joke does not have an 'id' key"


# ����, �� ����� ���� �� ������� (���� "categories")
    def test_each_joke_has_categories(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "categories" in joke, "Joke does not have a 'categories' key"


# ����, �� ����� ���� �� URL (���� "url")
    def test_each_joke_has_url(self):
        jokes = self.response.json()["result"]
        for joke in jokes:
            assert "url" in joke, "Joke does not have a 'url' key"
