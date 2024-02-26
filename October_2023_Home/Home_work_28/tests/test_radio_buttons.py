import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait
from Hellel.October_2023_Home.Home_work_28.src.pages.page_radio_buttons import RadioButtonPage


@pytest.mark.usefixtures("chrome_class")
class TestRadioButtons:

    def setup_method(self):
        self.driver = self.driver
        self.radio_button_page = RadioButtonPage(driver=self.driver)

    def test_activate_yes_radio_1(self):
        """Перший спосіб. Активує радіокнопку "Yes", після активації отримує текст та його порівнює"""
        self.radio_button_page.open("https://demoqa.com/radio-button")
        self.radio_button_page.select_yes_radio()
        (WebDriverWait(self.driver, timeout=2).until
         (es.visibility_of_element_located(self.radio_button_page.radio_button_output_result)))
        result_text = self.radio_button_page.get_output_result_text()
        assert result_text == "Yes"

    def test_activate_yes_radio_2(self):
        """Другий спосіб. Активує радіокнопку "Yes" і перевіряє, чи вона активована"""
        self.radio_button_page.open("https://demoqa.com/radio-button")
        self.radio_button_page.select_yes_radio()
        (WebDriverWait(self.driver, timeout=2).until
         (es.visibility_of_element_located(self.radio_button_page.radio_button_output_result)))
        assert self.radio_button_page.is_yes_radio_selected

    def test_get_radio_buttons_info(self):
        """Визначає дані про радіокнопки та перевіряє, чи вони коректні та активні"""
        self.radio_button_page.open("https://demoqa.com/radio-button")
        radio_buttons_info = {}

        # Перевірка для кнопки 'Yes'
        self.radio_button_page.select_yes_radio()
        is_yes_enabled = self.radio_button_page.is_radio_button_enabled('yes')
        radio_buttons_info['yes'] = {
            'Name': 'Yes',
            'IsEnabled': is_yes_enabled,
            'IsSelected': self.radio_button_page.is_radio_button_selected('yes'),
        }
        output_yes = self.radio_button_page.get_output_result_text()
        assert output_yes.lower() == 'yes', f"Expected 'yes', but got '{output_yes.lower()}'"

        # Перевірка для кнопки 'Impressive'
        self.radio_button_page.select_impressive_radio()
        is_impressive_enabled = self.radio_button_page.is_radio_button_enabled('impressive')
        radio_buttons_info['impressive'] = {
            'Name': 'Impressive',
            'IsEnabled': is_impressive_enabled,
            'IsSelected': self.radio_button_page.is_radio_button_selected('impressive'),
        }
        output_impressive = self.radio_button_page.get_output_result_text()
        assert output_impressive.lower() == 'impressive', f"Expected 'impressive', but got '{output_impressive.lower()}'"

        # Перевірка для кнопки 'No'
        self.radio_button_page.select_no_radio()
        WebDriverWait(self.driver, timeout=2).until(
            es.visibility_of_element_located(self.radio_button_page.radio_button_output_result)
        )
        is_no_enabled = self.radio_button_page.is_radio_button_enabled('no')
        is_no_selected = self.radio_button_page.is_radio_button_selected('no')
        radio_buttons_info['no'] = {
            'Name': 'No',
            'IsEnabled': is_no_enabled,
            'IsSelected': is_no_selected
        }
        # try:
        #     WebDriverWait(self.driver, timeout=10).until(
        #         es.text_to_be_present_in_element(self.radio_button_page.radio_button_output_result)
        #     )
        # except TimeoutException:
        #     print(f"TimeoutException: Text '{'no'}' not found in element.")
        # except Exception as e:
        #     print(f"An error occurred: {str(e)}")
        # output_no = self.radio_button_page.get_output_result_text()
        # assert output_no.lower() == 'no', f"Expected 'no', but got '{output_no.lower()}'"

        # Виведення інформації
        for choice_name, info in radio_buttons_info.items():
            print(f"Button: {info['Name']}, Enabled: {info['IsEnabled']}, Selected: {info['IsSelected']}")
