from selenium.webdriver.common.by import By


class RadioButtonPage:

    def __init__(self, driver):
        self.driver = driver
        self.radio_button_yes = (By.CSS_SELECTOR, "label[for='yesRadio']")
        self.radio_button_impressive = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
        self.radio_button_no = (By.CSS_SELECTOR, "label[for='noRadio']")
        self.radio_button_output_result = (By.CSS_SELECTOR, "p span[class='text-success']")

        # self.radio_button_yes = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Yes']")
        # self.radio_button_impressive = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Impressive']")
        # self.radio_button_no = (By.XPATH, "//label[contains(@class, 'custom-control-label')][contains(@class, 'disabled')]")
        # self.radio_button_output_result = (By.XPATH, "//p[contains(text(), 'You have selected')]/span[@class='text-success']")

    def open(self, url):
        self.driver.get(url)

    def select_yes_radio(self):
        self.driver.find_element(*self.radio_button_yes).click()

    def select_impressive_radio(self):
        self.driver.find_element(*self.radio_button_impressive).click()

    def select_no_radio(self):
        self.driver.find_element(*self.radio_button_no).click()

    def is_yes_radio_selected(self):
        return self.driver.find_element(*self.radio_button_yes).is_selected()

    def get_output_result_text(self):
        return self.driver.find_element(*self.radio_button_output_result).text

    def click_on_the_radio_button(self, choice_name):
        choice = {'yes': self.radio_button_yes, 'impressive': self.radio_button_impressive, 'no': self.radio_button_no}
        self.driver.find_element(*choice[choice_name]).click()

    def is_radio_button_enabled(self, choice_name):
        choice = {'yes': self.radio_button_yes, 'impressive': self.radio_button_impressive, 'no': self.radio_button_no}
        return self.driver.find_element(*choice[choice_name]).is_enabled()

    def is_radio_button_selected(self, choice_name):
        choice = {'yes': self.radio_button_yes, 'impressive': self.radio_button_impressive, 'no': self.radio_button_no}
        return self.driver.find_element(*choice[choice_name]).is_selected()


