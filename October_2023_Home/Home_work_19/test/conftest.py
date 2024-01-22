import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_work_19\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()