import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_work_20\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_work_20\geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(5) #затримка на 5 сек - імплісіті вейт
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_work_20\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    yield driver
    driver.quit()
