from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def test_web_browser(firefox2):
    driver = firefox2
    driver.get("https://rozetka.com.ua/ua/robototehnika/c4630482/")

    # Завдання збільшити кількість товарів на сторінці (необов'язково, але допоможе)
    # Знаходимо елемент і клікаємо на нього
    show_more_button = driver.find_element(By.CLASS_NAME, 'catalog-pagination__button_show-more')
    show_more_button.click()

    # Очікуємо, доки товари будуть завантажені
    time.sleep(10)  # Це тимчасовий захід, можливо, вам знадобиться більш ефективний підхід
    # TODO: Використовуйте Selenium Wait для заміни `time.sleep(2)`.

    # Отримуємо HTML-код сторінки після завантаження додаткових товарів
    page_source = driver.page_source

    # Створюємо об'єкт BeautifulSoup для парсингу HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # Отримуємо всі елементи з інформацією про товари
    products = soup.find_all('div', class_='goods-tile')

    # Відкриваємо файл для запису даних
    with open('output.txt', 'w', encoding='utf-8') as file:
        # Проходимо по кожному товару і записуємо назву та ціну в файл
        for product in products:
            title = product.find('div', class_='goods-tile__title').text.strip()
            price = product.find('span', class_='goods-tile__price-value').text.strip()
            file.write(f"{title}: {price}\n")

    # Клікаємо на другу сторінку (якщо вона існує)
    next_page_button = driver.find_element(By.CLASS_NAME, 'paginator__direction_type_forward')
    if next_page_button.is_enabled():
        next_page_button.click()
        time.sleep(2)  # Це тимчасовий захід, можливо, вам знадобиться більш ефективний підхід
        # TODO: Використовуйте Selenium Wait для заміни `time.sleep(2)`.

        # Повторюємо той самий процес парсингу для другої сторінки
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        products = soup.find_all('div', class_='goods-tile')

        # Дописуємо інформацію про товари на другій сторінці в файл
        with open('output.txt', 'a', encoding='utf-8') as file:
            for product in products:
                title = product.find('div', class_='goods-tile__title').text.strip()
                price = product.find('span', class_='goods-tile__price-value').text.strip()
                file.write(f"{title}: {price}\n")












