import pytest
from selenium.webdriver.remote.webelement import WebElement
from Hellel.October_23.lesson_19.DynamicPropertiesPage import PageDynamicProperties
from Hellel.October_23.lesson_19.ElementsPage import ElementsPage

class TestElementsPage:

    def test_page(self, chrome):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert len(elements) == 33
        pass

    # #  todo перевірити відповіді всіх 33 елементів в елементс
    # #  assert elements[2] == "Radio Button"
    #
    # # # Список з елементами, які потрібно перевірити
    # elements_to_check = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links",
    #                      "Broken Links - Images", "Upload and Download", "Dynamic Properties", "", "", "", "", "", "",
    #                      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    #
    # @pytest.mark.parametrize("expected_element", elements_to_check)
    # def test_page(self, chrome, expected_element):
    #     page = ElementsPage(chrome)
    #     page.open()
    #     elements = page.get_elements_page_categories()
    #     assert expected_element in elements

    def test_is_button_enable(self, chrome):
        page = PageDynamicProperties(chrome)
        self.open()
        button: WebElement = page.disable_enable_button()
        button.click()

    def test_is_button_shown(self, chrome):
        page = PageDynamicProperties(chrome).open()  # короткий запис
        button: WebElement = page.button_invisible_visible()
        button.click()










