coding: 'utf-8'
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Hellel.October_2023_Home.Home_work_29.page.form_page_locators import FieldButtonPage


@pytest.fixture
def confy_page(chrome_driver):
    return FieldButtonPage(driver=chrome_driver)


def test_confy_page(confy_page):
    confy_page.open()
    confy_page.fill_search_field("Планшети")
    confy_page.click_submit()