coding: 'utf-8'
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as BS



class ParseOlxPages:
    def __init__(self):
        self.service = Service(executable_path=ChromeDriverManager().install())  # Ініціалізція сервіса
        self.driver = webdriver.Chrome(service=self.service)  # Ініціалізція веб-драйвера з використанням сервісу
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)  # Встановлення неявного очікування на 10 секунд

    def get_content(self):
        rows = []

        # Отримуємо HTML-сторінку
        page = BS(self.driver.page_source, "html.parser")
        div_list = page.find_all('div', attrs={'data-testid': 'listing-grid', 'class': 'css-oukcj3'})

        # Перевіряємо, чи знайдено потрібний елемент
        if div_list:
            for div in div_list:
                item_list = div.find_all('div', class_='css-1sw7q4x')

                # Парсимо дані зі сторінки
                for item in item_list:
                    h_goods = item.find('h6')
                    title_text = h_goods.text.strip().replace('\n', '')
                    ad_price = item.find('p')
                    price_str = ad_price.text.replace('\n', '')
                    price = int(''.join(c for c in price_str if c.isdigit()))
                    tmp = {'Назва': title_text, 'Ціна грн.': price_str, 'Ціна': price}
                    rows.append(tmp)
        else:
            print("Елементів не знайдено")

        return rows

    def scrape_olx_pages(self):
        # Оголошуємо список для зберігання даних
        all_rows = []

        # Відкриваємо початкову сторінку
        self.driver.get('https://www.olx.ua/uk/')

        # Виконуємо пошук та клік по кнопці на першій сторінці
        search_field = self.driver.find_element(By.CSS_SELECTOR, "input#search[data-testid='search-input'][placeholder='Що шукаєте?']")
        search_field.send_keys("Планшет")
        submit_button = self.driver.find_element(By.XPATH, "//button[@data-testid='search-submit']")
        submit_button.click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "h6.css-16v5mdi.er34gjf0")))

        # Отримуємо контент з першої сторінки і додаємо його до загального списку
        all_rows += self.get_content()

        # Якщо є вікно кукі, закриваємо його
        try:
            cookies_overlay_element = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='cookies-overlay__container']")
            if cookies_overlay_element.is_displayed():
                cookies_overlay_element.find_element(By.TAG_NAME, "button").click()
        except:
            pass

        # Отримуємо дані з другої сторінки
        pagination_button = self.driver.find_element(By.XPATH, "//a[text()='2']")
        pagination_button.click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, "//h6[@class='css-16v5mdi er34gjf0']")))

        # Отримуємо контент з другої сторінки і додаємо його до загального списку
        current_page_content = self.get_content()
        all_rows += current_page_content
        print(f"Загальна кількість записів після зчитування другої сторінки: {len(all_rows)}")

        self.driver.quit()


        # Записуємо дані в файл
        csv_title = ['Назва', 'Ціна грн.', 'Ціна']
        with open('olx.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
            writer.writeheader()
            writer.writerows(all_rows)


if __name__ == '__main__':
    parser = ParseOlxPages()
    parser.scrape_olx_pages()