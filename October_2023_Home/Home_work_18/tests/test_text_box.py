from Hellel.October_2023_Home.Home_work_18.TextBoxPage import (TextBoxPage)


class TestTextBox:

    # def test_test_box(self, chrome):
    #     page = TextBoxPage(chrome)
    #     page.open()
    #     page.fill_full_name_field("Olena")
    #     page.fill_full_email_field("Sallita@i.ua")
    #     page.fill_current_address_field("test")
    #     page.fill_permanent_address_field("test_1")
    #     page.scroll_down()
    #     page.click_submit()
    #     pass

    # def test_username_fill_and_check(self, chrome):
    #     page = TextBoxPage(chrome)
    #     page.open()
    #     page.fill_full_name_field("Olena")
    #     page.scroll_down()
    #     page.click_submit()
    #     name_field = page.get_result_fullname()
    #     assert name_field.replace("Name:", "") == "Olena"
    #
    # def test_email_fill_and_check(self, chrome):
    #     page = TextBoxPage(chrome)
    #     page.open()
    #     page.fill_full_email_field("Sallita@i.ua")
    #     page.scroll_down()
    #     page.click_submit()
    #     email_field = page.get_result_email()
    #     assert email_field.replace("Email:", "") == "Sallita@i.ua"

    # def test_curr_addr_fill_and_check(self, chrome):
    #     page = TextBoxPage(chrome)
    #     page.open()
    #     page.fill_current_address_field("Test current address")
    #     page.scroll_down()
    #     page.click_submit()
    #     current_address_field = page.get_result_current_address()
    #     assert current_address_field == "Test current address"

        def test_curr_addr_fill_and_check(self, chrome):
            page = TextBoxPage(chrome)
            page.open()
            page.fill_current_address_field("Test current address")
            page.scroll_down()
            page.click_submit()
            current_address_field = page.get_result_current_address()
            assert "Test current address" in current_address_field

    # def test_perm_addr_fill_and_check(self, chrome):
    #     page = TextBoxPage(chrome)
    #     page.open()
    #     page.fill_permanent_address_field("Test permanent address")
    #     page.scroll_down()
    #     page.click_submit()
    #     permanent_address_field = page.get_result_permanent_address
    #     assert permanent_address_field == "Test permanent address"

