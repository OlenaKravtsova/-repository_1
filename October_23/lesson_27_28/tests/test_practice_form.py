import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from Hellel.October_23.lesson_27_28.src.pages.page_practice_form import PagePracticeForm


@pytest.mark.usefixtures("firefox")
class TestPracticeForm:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PagePracticeForm(driver=self.driver)

# Закомітили і зробили поіншому
    # def test_(self):
    #     self.page.open()
    #     self.page.set_state_via_input(state="NCR")
    #     results = self.page.get_result_from_dropdown()
    #     is_ok = all([result for result in results])
    #     assert is_ok

    def test_(self):
        self.page.open()
        state = "NC"
        self.page.set_state_via_input(state=state)
        results = self.page.get_result_from_dropdown()

        # is_ok = all(["NCRL" in result for result in results])
        assert state in results


