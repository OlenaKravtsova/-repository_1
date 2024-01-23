import pytest
from Hellel.October_23.lesson_20.TextBoxPage import TextBoxPage


class TestTextBox:

    def test_test_box(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Olena")
        page.fill_full_email_field("Sallita@i.ua")
        page.fill_current_address_field("test")
        page.fill_permanent_address_field("test_1")
        page.scroll_down()
        page.click_submit()
        pass

    @pytest.mark.parametrize("email", ["i@meta", "wrong email"])
    def test_email_fill_and_check_negative(self, chrome, email):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_email_field("email")
        page.scroll_down()
        page.click_submit()
        class_of_field = page.get_email_field_element().get_attribute("class")
        assert "error" in class_of_field

    # def test_curr_addr_fill_and_check(self, chrome):
    #     pass
    #
    # def test_perm_addr_fill_and_check(self, chrome):
    #     pass
