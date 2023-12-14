import pytest
import requests


@pytest.mark.usefixtures("fixture_random")
class TestRandom:
    # ��������� ���� "icon_url" �� �� �� ����� + �� �� ��������,  - 2 �����
    # ��������� �� � ���� "value"  � ��������� ���� �������� - 2 �����
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