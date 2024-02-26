from selenium.webdriver.common.by import By

from Hellel.October_23.lesson_23.RadioButtonPage import RadioButton


def test_radio(chrome):
    chrome.get("https://demoqa.com/radio-button")
    ra_yes = RadioButton(driver=chrome, locator=(By.XPATH, "//label[.='{}']//ancestor::div[contains(@class, 'radio')]"), name="Yes")
    ra_yes.select()
    pass