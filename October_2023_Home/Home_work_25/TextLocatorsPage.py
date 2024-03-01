coding: 'utf-8'
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://hyperskill.org/')
sign_in_button = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, "//a[div='Sign in']")))
time.sleep(2)
sign_in_button.click()
time.sleep(3)

email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
email_field.send_keys("akravtsova@i.ua")
time.sleep(2)
email_field.clear()
time.sleep(3)

email_field = driver.find_element(By.XPATH, "//input[@placeholder='E-mail']")
email_field.send_keys("Sallita@i.ua")
time.sleep(3)

password_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
password_field .send_keys("123456712!gh")
time.sleep(1)

sign_in_button = driver.find_element(By.CSS_SELECTOR, "button[data-cy='submitButton']")
time.sleep(1)
sign_in_button.click()
time.sleep(2)

password_field.clear()
password_field = driver.find_element(By.XPATH, "//input[@type='password' and @placeholder='Password']")
time.sleep(1)
password_field.send_keys("ghtyju666gkb!")
time.sleep(2)

sign_in_button = driver.find_element(By.XPATH, "//button[@data-cy='submitButton']")
time.sleep(1)
sign_in_button.click()

reset_password_button = driver.find_element(By.XPATH, "//a[contains(text(),'Reset password')]")
reset_password_button.click()
time.sleep(3)

email_address_field = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="email"]')
email_address_field.send_keys("Sallita@i.ua")
time.sleep(1)
email_address_field.click()
time.sleep(2)

reset_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary[value='Reset My Password']")
reset_button.click()
time.sleep(3)

message_page = WebDriverWait(driver, 5).until(
    ec.visibility_of_element_located((By.XPATH, "//div[@class='mt-3']")))
message_text = message_page.text
print(message_text)
time.sleep(5)

driver.quit()

