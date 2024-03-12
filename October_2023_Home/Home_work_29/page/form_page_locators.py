coding: 'utf-8'
from selenium.webdriver.common.by import By


class FieldButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.CSS_SELECTOR, "input#search[data-testid='search-input'][placeholder='Що шукаєте?']")
        self.submit_button = (By.XPATH, "//button[@data-testid='search-submit']")
        self.result_search = (By.CSS_SELECTOR, "span[data-testid='total-count']")
        self.url = "https://www.olx.ua/uk/"

    def open(self) -> "FieldButtonPage":
        self.driver.get(self.url)
        return self

    def clear_search_field(self) -> None:
        self.driver.find_element(*self.search_field).clear()

    def fill_search_field(self, text: str) -> None:
        self.driver.find_element(*self.search_field).send_keys(text)

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_button).click()

    def get_result_search(self):
        return self.driver.find_element(*self.result_search).text

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")


