coding: 'utf-8'
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'/Hellel/October_23_Home/Home_chrome/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    # якщо використовуємо драйвер менеджер, то нам не потрібно викачувати мануально наш драйвер
    # s = Service(r'/Hellel/October_23/Chrom/geckodriver.exe')
    # driver = webdriver.Firefox(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def firefox2(request):
    # якщо використовуємо драйвер менеджер, то нам не потрібно викачувати мануально наш драйвер
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_chrome\geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture
def firefox(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    # якщо використовуємо драйвер менеджер, то нам не потрібно викачувати мануально наш драйвер
    # s = Service(r'/Hellel/October_23/Chrom/geckodriver.exe')
    # driver = webdriver.Firefox(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(5)
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


@pytest.fixture
def chrome_driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()