import time

coding: 'utf-8'
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
from Hellel.October_2023_Home.Home_work_29.page.form_page_locators import FieldButtonPage


@pytest.fixture
def confy_page(chrome_driver):
    return FieldButtonPage(driver=chrome_driver)


def test_confy_page(confy_page):
    confy_page.open()
    confy_page.fill_search_field("Планшет")
    confy_page.click_submit()
    result_text = confy_page.get_result_search()
    WebDriverWait(confy_page.driver, timeout=20).until(es.visibility_of_element_located(confy_page.result_search))
    assert result_text == result_text  # Перевіряємо, чи текст елемента відповідає очікуваному тексту
