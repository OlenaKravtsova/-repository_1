from Hellel.October_23.lesson_18.TextBoxPage import TextBoxPage


class TestTextBox:

    def test_username_fill_and_check(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
        page.fill_full_name_field("Olena")
        page.scroll_down()
        page.click_submit()
        name_field = page.get_result_fullname()
        assert name_field.replace("Name:", "") == "Olena"

    def test_email_fill_and_check(self, chrome):
        pass

    def test_curr_addr_fill_and_check(self, chrome):
        pass

    def test_perm_addr_fill_and_check(self, chrome):
        pass
