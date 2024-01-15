from Hellel.October_23.lesson_18.TextBoxPage import TextBoxPage

class TestTextBox:

    def test_text_box(self, chrome):
        page = TextBoxPage(chrome)
        page.open()
