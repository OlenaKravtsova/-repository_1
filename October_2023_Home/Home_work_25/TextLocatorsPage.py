coding: 'utf-8'
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class HyperskillAutomation:
    def __init__(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Встановлення неявного очікування на 10 секунд

    def sign_in(self):
        self.driver.get('https://hyperskill.org/')
        sign_in_button = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//a[div='Sign in']")))
        time.sleep(2)
        sign_in_button.click()
        time.sleep(3)

    def fill_email_field(self, email):
        email_field = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        email_field.send_keys(email)
        time.sleep(2)
        email_field.clear()
        time.sleep(3)

    def fill_password_field(self, password):
        password_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
        password_field.send_keys(password)
        time.sleep(1)

    def click_sign_in_button(self):
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-cy='submitButton']")
        time.sleep(1)
        sign_in_button.click()
        time.sleep(2)

    def reset_password(self):
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Password']")
        time.sleep(1)
        password_field.send_keys("ghtyju666gkb!")
        time.sleep(2)

        sign_in_button = self.driver.find_element(By.XPATH, "//button[@data-cy='submitButton']")
        time.sleep(1)
        sign_in_button.click()

        reset_password_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Reset password')]")
        reset_password_button.click()
        time.sleep(3)

        email_address_field = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="email"]')
        email_address_field.send_keys("Sallita@i.ua")
        time.sleep(1)
        email_address_field.click()
        time.sleep(2)

        reset_button = self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary[value='Reset My Password']")
        reset_button.click()
        time.sleep(3)

        message_page = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located((By.XPATH, "//div[@class='mt-3']")))
        message_text = message_page.text
        print(message_text)
        time.sleep(5)

    def close_browser(self):
        self.driver.quit()


# Використання класу HyperskillAutomation для автоматизації дій на сайті
automation = HyperskillAutomation()
automation.sign_in()
automation.fill_email_field("akravtsova@i.ua")
automation.fill_password_field("123456712!gh")
automation.click_sign_in_button()
automation.reset_password()
automation.close_browser()

