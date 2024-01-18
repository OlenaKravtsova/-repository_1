import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'C:\Testgit\Hellel\October_23\lesson_19\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()