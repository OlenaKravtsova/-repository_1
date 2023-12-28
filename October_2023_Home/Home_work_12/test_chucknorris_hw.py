import pytest
import requests


# ��������� ���� "icon_url" �� �� �� ������ + �� �� ��������,  - 2 �����
# ��������� �� � ���� "value"  � ��������� ���� �������� - 2 �����
# @pytest.mark.usefixtures("fixture_random")
# class TestRandom:
#
#     def test_icon_url_not_empty(self):
#         # ���� 1: ��������, �� "icon_url" �� �������
#         assert self.response.json()["icon_url"], "'icon_url' is empty"
#
#     def test_icon_url_is_image(self):
#         # ���� 2: ��������, �� "icon_url" � ���������� �� ����������
#         icon_url = self.response.json().get("icon_url")
#         image_extensions = [".jpg", ".jpeg", ".png"]
#         assert any(icon_url.endswith(ext) for ext in image_extensions), "'icon_url' is not an image URL"
#
#     def test_value_key_exists(self):
#         # ���� 3: ��������, �� ���� ���� "value" � ��'��� �����
#         assert "value" in self.response.json(), "Key 'value' does not exist"
#
#     def test_value_not_empty(self):
#         # ���� 4: ��������, �� �������� ����� "value" �� ������
#         assert self.response.json()["value"], "Value of 'value' is empty"

#     def test_check_year(self):
#         assert int(self.response.json()["created_at"][:4]) > 1990, "All our jokes were created until 1990"
#
#     def test_status_code(self):
#         assert self.status_code == 200
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



# ������� ������� ����
# ����� ����� �� ���������� �����  https://api.chucknorris.io/jokes/search?query={query}
# ������� ������� ��������
# ���� �� ������ ���
# ���� �� ������� �����
# ���� �� ��� ����
# + 3 �����



class ChuckNorrisJokeSearch:
    BASE_URL = "https://api.chucknorris.io/jokes/search"

    def __init__(self, query):
        self.query = query

    def search_joke(self):
        response = requests.get(f"{self.BASE_URL}?query={self.query}")
        return response

# ������������ ����� ��� ������ �����
search_instance = ChuckNorrisJokeSearch("python")  # ������ "python" �� ��� �����
search_result = search_instance.search_joke()

# ��������� ���������� ������
print(search_result.json())

# # Գ������ ��� ������ ����� �� ���������� ������
# @pytest.fixture
# def fixture_joke_search():
#     joke_search = ChuckNorrisJokeSearch("internet")  # ������ "python" �� ��� �����
#     return joke_search.get_jokes(), joke_search.get_jokes().status_code

# ���� ����� ��� ������ ����� �� ���������� ������
# class TestJokeSearch:
#
#     @pytest.mark.usefixtures("fixture_joke_search")
#     def test_status_code(self, fixture_joke_search):
#         response, status_code = fixture_joke_search
#
#         # ���� 1: ��������, �� ������ ��� ������� 200
#         assert status_code == 200, f"Unexpected status code: {status_code}"
#
#     @pytest.mark.usefixtures("fixture_joke_search")
#     def test_number_of_jokes(self, fixture_joke_search):
#         response, _ = fixture_joke_search
#
#         # ���� 2: ��������, �� ������� ����� �� �������
#         assert response.json()["total"] > 0, "Number of jokes is empty"
#
#     @pytest.mark.usefixtures("fixture_joke_search")
#     def test_joke_content(self, fixture_joke_search):
#         response, _ = fixture_joke_search
#
#         # ���� 3: ��������, �� ��� ���� �� �������
#         assert response.json()["result"][0]["value"], "Joke content is empty"
#
# # ������ ����� �����
# test_joke_search_instance = TestJokeSearch()
# test_joke_search_instance.test_status_code()
# test_joke_search_instance.test_number_of_jokes()
# test_joke_search_instance.test_joke_content()







