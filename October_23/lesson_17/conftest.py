coding: 'utf-8'
import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="C:\Testgit\Hellel\October_23\lesson_17\tests\chromedriver")
    yield driver
    driver.quit()
