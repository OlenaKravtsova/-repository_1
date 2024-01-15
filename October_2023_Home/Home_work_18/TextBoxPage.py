coding: 'utf-8'

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        # self.full_name_field = (By.XPATH, '// input[ @ id ="userName"]') #���������� ������� �� userName ����� XPATH
        self.full_email_field - (By.ID, "#userEmail")
        self.full_current_text_area_field = (By.ID, "currentAddress")
        self.full_permanent_text_area_field = (By.CSS_SELECTOR, "text#permanentAddress")
        self.submit_btn = (By.ID, "submit")

    def open(self) -> "TestBoxPage":
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    # ����������(����� clear and fill) ��� ���� Email, Current Address, Permanent Address
    # ������ �� ������ ������ �� ����� ����� �������(�� ���������)

    def clear_full_email_field(self) -> None:
        self.driver.find_element(*self.full_email_field).clear()

    def fill_full_email_field(self, text: str) -> None:
        self.driver.find_element(*self.full_email_field).send_keys(text)

    def clear_full_current_text_area_field(self) -> None:
        self.driver.find_element(*self.full_current_text_area_field).clear()

    def fill_full_current_text_area_field(self, text: str) -> None:
        self.driver.find_element(*self.full_current_text_area_field).send_keys(text)

    def clear_full_permanent_text_area_field(self) -> None:
        self.driver.find_element(*self.full_permanent_text_area_field).clear()

    def fill_full_permanent_text_area_field(self, text: str) -> None:
        self.driver.find_element(*self.full_permanent_text_area_field).send_keys(text)

    def clic_sudmit(self) -> None:
        self.driver.find_element(*self.submit_btn).click()