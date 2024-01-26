coding: 'utf-8'
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("chrome_class")
class TestWaiters:

    # @pytest.mark.skip
    # Кнопка "Visible After 5 Seconds"
    def test_connection(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        visible_invisible_button_loc = (By.CSS_SELECTOR, "#visibleAfter")
        # Встановлює явне очікування протягом 5 секунд на видимість цієї кнопки.
        WebDriverWait(self.driver, timeout=5).until(ec.visibility_of_element_located(visible_invisible_button_loc))
        # Отримується елемент кнопки за допомогою знайденого локатора
        visible_invisible_button = self.driver.find_element(*visible_invisible_button_loc)
        # Здійснюється клік по кнопці.
        visible_invisible_button.click()
        #todo завешити тест на те що кнопка є . _is...
        assert visible_invisible_button.is_displayed(), "Кнопка не з'явилася на сторінці після кліку"

    # Кнопка "Will enable 5 Seconds"
    def test_enable_button(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        enable_button_loc = (By.ID, "enableAfter")
        # Встановлює явне очікування протягом 5 секунд на видимість цієї кнопки.
        WebDriverWait(self.driver, timeout=5).until(ec.presence_of_element_located(enable_button_loc))
        # Отримується елемент кнопки за допомогою знайденого локатора
        enable_button = self.driver.find_element(*enable_button_loc)
        # Здійснюється клік по кнопці.
        enable_button.click()
        assert enable_button.is_displayed(), "Кнопка залишилася доступною після кліку"

    # Кнопка "Color Change"
    def test_connection_color(self):
        self.driver.get("https://demoqa.com/dynamic-properties")
        colored_button_loc = (By.ID, "colorChange")
        # Отримується елемент кнопки за допомогою знайденого локатора
        colored_button: WebElement = self.driver.find_element(*colored_button_loc)
        # Встановлює явне очікування протягом 5 секунд на видимість цієї кнопки.
        WebDriverWait(self.driver, timeout=10).until(
            ec.text_to_be_present_in_element_attribute(colored_button_loc, attribute_='class', text_='text-danger'))
        # Здійснюється клік по кнопці.
        colored_button.click()
        #todo завешити тест на те що кнопка є . _is...
        assert colored_button.is_displayed(), "Кнопка не з'явилася на сторінці після кліку"
