import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def chrome():
    s = Service(r'C:\Testgit\Hellel\October_2023_Home\Home_work_18\chromedriver.exe')
    # settings driver for win 64
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()