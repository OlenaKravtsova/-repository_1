import pytest
from selenium.webdriver.remote.webelement import WebElement
from Hellel.October_23.lesson_20.DynamicPropertiesPage import PageDynamicProperties
from Hellel.October_23.lesson_20.ElementsPage import ElementsPage

class TestElementsPage:

    def test_page(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33
        pass
