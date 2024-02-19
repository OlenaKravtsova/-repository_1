import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from Hellel.October_23.lesson_27.src.pages.page_practice_form import PagePracticeForm


@pytest.mark.usefixtures("firefox")
class TestPracticeForm:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PagePracticeForm(driver=self.driver)

    def test_(self):
        self.page.open()
        self.page.set_state_via_input(state="NCR")
        pass

