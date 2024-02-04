import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'C:\Testgit\Hellel\October_23\Hrom\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    s = Service(r'C:\Testgit\Hellel\October_23\Hrom\geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    s = Service(r'C:\Testgit\Hellel\October_23\Hrom\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    yield driver
    driver.quit()

#фікстура яка приймає декілька параметрів.
@pytest.fixture(scope="class", params=['fashion', 'food', 'history'])
def fixture_chuck_category(request):
    category = request.param
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    print(URL)
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    yield response
