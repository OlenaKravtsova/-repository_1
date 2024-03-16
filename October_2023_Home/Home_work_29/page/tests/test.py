coding: 'utf-8'

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Hellel.October_2023_Home.Home_work_29.page.form_page_locators import FieldButtonPage


@pytest.fixture
def olx_page(chrome_driver):
    return FieldButtonPage(driver=chrome_driver)


# Перевіряємо, чи текст елемента відповідає очікуваному тексту
def test_olx_page(olx_page):
    olx_page.open()
    olx_page.fill_search_field("Планшет")
    olx_page.click_submit()
    result_text = olx_page.get_result_search()
    WebDriverWait(olx_page.driver, timeout=5).until(ec.visibility_of_element_located(olx_page.result_search))
    assert result_text == result_text


# Перевіряємо, чи працює функція прокручування сторінки вниз
def test_scroll_down(olx_page):
    olx_page.open()
    initial_position = olx_page.driver.execute_script("return window.pageYOffset;")
    olx_page.scroll_down()
    new_position = olx_page.driver.execute_script("return window.pageYOffset;")
    assert new_position > initial_position


# Перевіряємо, клік на пагінаторі кнопки "2"
def test_pagination(olx_page):
    olx_page.open()
    olx_page.fill_search_field("Планшети")
    olx_page.click_submit()
    WebDriverWait(olx_page.driver, 10).until(ec.visibility_of_element_located(olx_page.result_search))
    olx_page.scroll_down()
    olx_page.close_cookies_overlay()
    olx_page.click_pagination_2()
    WebDriverWait(olx_page.driver, 10).until(ec.visibility_of_element_located(olx_page.result_search))
    assert "page=2" in olx_page.driver.current_url
