coding: 'utf-8'
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Hellel.October_2023_Home.Home_work_24.src.pages.page_buttons import PageButtons


@pytest.mark.usefixtures("chrome_class")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_doubleclick_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        # Встановлює явне очікування протягом 5 секунд на видимість елемента
        # WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.page.button_doubleclick_message_loc))
        assert self.page.get_button_doubleclick_message() == "You have done a double click"

    def test_right_click_button(self):
        self.page.open()
        self.page.button_right_click().right_click()
        # Встановлює явне очікування протягом 5 секунд на видимість елемента
        # WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located(self.page.button_right_click_message_loc))
        assert self.page.get_button_right_click_message() == "You have done a right click"

    def test_dynamic_id_click_button(self):  #кнопка Click Me
        self.page.open()
        self.page.button_dynamic_id_click().click()
        assert self.page.get_button_dynamic_id_click_message() == "You have done a dynamic click"
