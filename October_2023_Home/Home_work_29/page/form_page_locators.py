coding: 'utf-8'
from selenium.webdriver.common.by import By


class FieldButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_field = (By.CSS_SELECTOR, "input#search[data-testid='search-input'][placeholder='Що шукаєте?']")
        self.submit_button = (By.XPATH, "//button[@data-testid='search-submit']")
        self.result_search = (By.XPATH, "//h6[@class='css-16v5mdi er34gjf0']")
        self.pagination = (By.XPATH, "//a[text()='2']")
        self.cookies_overlay = (By.CSS_SELECTOR, "div[data-testid='cookies-overlay__container']")
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

    def click_pagination_2(self) -> None:
        self.driver.find_element(*self.pagination).click()

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")

    def close_cookies_overlay(self) -> None:
        try:
            cookies_overlay_element = self.driver.find_element(*self.cookies_overlay)
            if cookies_overlay_element.is_displayed():
                cookies_overlay_element.find_element(By.TAG_NAME, "button").click()
        except:
            pass
