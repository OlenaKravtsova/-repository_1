from Hellel.October_2023_Home.Home_work_18.TextBoxPage import (TextBoxPage)


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

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Olena")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Olena"

    def test_email_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_email_field("email@gmail.com")
        page.scroll_down()
        page.click_submit()
        email_field = page.get_result_email()
        assert email_field.replace("Email:", "") == "email@gmail.com"

    def test_curr_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_current_address_field("current address")
        page.scroll_down()
        page.click_submit()
        curr_addr_field = page.get_result_current_address()
        assert curr_addr_field.replace("Current Address :", "") == "current address"

    def test_perm_addr_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_permanent_address_field("permanent address")
        page.scroll_down()
        page.click_submit()
        perm_addr_field = page.get_result_permanent_address()
        assert perm_addr_field.replace("Permananet Address :", "") == "permanent address"



