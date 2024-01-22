import pytest
from Hellel.October_2023_Home.Home_work_19.ElementsPage import ElementsPage


class TestElementsPage:

    # def test_page(self, chrome):
    #     page = ElementsPage(chrome)
    #     page.open()
    #     elements = page.get_elements_page_categories()
    #     assert len(elements) == 33
    #     pass

    # #  todo перевірити відповіді всіх 33 елементів в елементс
    # #  assert elements[2] == "Radio Button"

    # # Список з елементами, які потрібно перевірити
    expected_element = ["Text Box", "Check Box", "Radio Button", "Web Tables", "Buttons", "Links",
                         "Broken Links - Images", "Upload and Download", "Dynamic Properties", "", "", "", "", "", "",
                         "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    @pytest.mark.parametrize("expected_element, result", [
        (0, "Text Box"),
        (1, "Check Box"),
        (2, "Radio Button"),
        (3, "Web Tables"),
        (4, "Buttons"),
        (5, "Links"),
        (6, "Broken Links - Images"),
        (7, "Upload and Download"),
        (8, "Dynamic Properties")
    ] + [(x, "") for x in range(9, 33)])
    def test_page_parametrize(self, chrome, expected_element, result):
        page = ElementsPage(chrome)
        page.open()
        elements = page.get_elements_page_categories()
        assert elements[expected_element] == result












