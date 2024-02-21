coding: 'utf-8'
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Hellel.October_23.lesson_27.src.pages.page_practice_form import PagePracticeForm


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

    # def test_(self):
    #     state = "NCR"
    #     self.page.open()
    #     self.page.set_state_via_input()
    #     self.page.set_state_from_dropdown(state)
    #     self.page.show_filtered_results_in_dropdown(state)
    #     results = self.page.get_result_from_dropdown()
    #     # print(results)
    #
    #     # is_ok = all(["NCRL" in result for result in results])
    #     # assert state in results
    #     assert "NCR" in results[0]
    #     assert "NCR" in srt(results)

    def test_upload_file(self):
        self.page.open()
        upload_button = self.driver.find_element(By.CSS_SELECTOR, "input#uploadPicture")
        upload_button.send_keys("C:\\Testgit\\2.png")
        file_name = upload_button.get_attribute("value")
        # self.driver.save_screenshot("12.png")
        assert "2.png" in file_name


