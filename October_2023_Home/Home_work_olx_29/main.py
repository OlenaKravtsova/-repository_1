coding: 'utf-8'
import csv
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import requests


def get_content_first_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp,*/*;q=0.8"
    }
    resp = requests.get(url, headers=header)
    rows = []

    # def parse_content_first_page(url):
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     url = 'https://www.olx.ua/uk/'
    #     get_content_first_page(url)

    if resp.status_code == 200:
        page = BS(resp.text, "html.parser")
        table = page.find('div', class_='css-oukcj3')
        tr_list = table.find_all('div', attrs={'class': 'css-1sw7q4x'})

        for tr in tr_list:
            title = tr.find('h6')
            title_text = title.text.strip().replace('\n', '')
            td_price = tr.find('p')
            price_str = td_price.text.replace('\n', '')
            price = int(''.join(c for c in price_str if c.isdigit()))
            tmp = {'title': title_text, 'price_str': price_str, 'price': price}
            # print(tmp)
            #print(title_text, price_str, price)
            rows.append(tmp)
    csv_title = ['title', 'price_str', 'price']
    with open('olx.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)


# def parse_content_first_page():
#     url = 'https://www.olx.ua/uk/list/q-%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82/'
#     get_content_first_page(url)
def parse_content_first_page():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    url_first_page = 'https://www.olx.ua/uk/'
    get_content_first_page(url_first_page)

# Відкриваємо першу сторінку
    def open_olx():
        driver.get(url_first_page)

# Очікуємо завантаження сторінки
    def find_element(locator):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-cy='l-card']")))



# def get_content_second_page(url):
#     header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
#         "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp,*/*;q=0.8"
#     }
#     resp = requests.get(url, headers=header)
#     rows = []
#
#     if resp.status_code == 200:
#         page = BS(resp.text, "html.parser")
#         table = page.find('div', class_='css-oukcj3')
#         tr_list = table.find_all('div', attrs={'class': 'css-1sw7q4x'})
#
#         for tr in tr_list:
#             title = tr.find('h6')
#             title_text = title.text.strip().replace('\n', '')
#             td_price = tr.find('p')
#             price_str = td_price.text.replace('\n', '')
#             price = int(''.join(c for c in price_str if c.isdigit()))
#             tmp = {'title': title_text, 'price_str': price_str, 'price': price}
#             # print(tmp)
#             #print(title_text, price_str, price)
#             rows.append(tmp)
#     csv_title = ['title', 'price_str', 'price']
#     with open('olx.csv', 'w', encoding='utf-8', newline='') as f:
#         writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
#         writer.writeheader()
#         writer.writerows(rows)
#
#
# def parse_content_second_page():
#     url = 'https://www.olx.ua/uk/list/q-%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82/'
#     get_content_second_page(url)


if __name__ == '__main__':
    parse_content_first_page()
    # parse_content_second_page()
