import pytest
from selenium.webdriver.remote.webelement import WebElement
from Hellel.October_23.lesson_21.DynamicPropertiesPage import PageDynamicProperties
from Hellel.October_23.lesson_21.ElementsPage import ElementsPage


class TestElementsPage:

    def test_page(self, firefox):
        page = ElementsPage(firefox)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33
        pass

    # def test_is_button_enabled(self, chrome):
    #     page = PageDynamicProperties(chrome)
    #     page.open()
    #     button: WebElement = page.disable_enable_button()
    #     button.click()
    #
    # def test_is_button_shown(self, chrome):
    #     page = PageDynamicProperties(chrome).open()  #скорочений запис
    #     button: WebElement = page.button_invisible_visible()
    #     button.click()