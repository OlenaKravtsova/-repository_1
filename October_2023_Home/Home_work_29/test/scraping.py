from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


def test_web_browser(firefox2):
    driver = firefox2
    driver.get("https://rozetka.com.ua/ua/robototehnika/c4630482/")

    # �������� �������� ������� ������ �� ������� (������'������, ��� ��������)
    # ��������� ������� � ������ �� �����
    show_more_button = driver.find_element(By.CLASS_NAME, 'catalog-pagination__button_show-more')
    show_more_button.click()

    # �������, ���� ������ ������ ����������
    time.sleep(10)  # �� ���������� �����, �������, ��� ����������� ���� ���������� �����
    # TODO: �������������� Selenium Wait ��� ����� `time.sleep(2)`.

    # �������� HTML-��� ������� ���� ������������ ���������� ������
    page_source = driver.page_source

    # ��������� ��'��� BeautifulSoup ��� �������� HTML
    soup = BeautifulSoup(page_source, 'html.parser')

    # �������� �� �������� � ����������� ��� ������
    products = soup.find_all('div', class_='goods-tile')

    # ³�������� ���� ��� ������ �����
    with open('output.txt', 'w', encoding='utf-8') as file:
        # ��������� �� ������� ������ � �������� ����� �� ���� � ����
        for product in products:
            title = product.find('div', class_='goods-tile__title').text.strip()
            price = product.find('span', class_='goods-tile__price-value').text.strip()
            file.write(f"{title}: {price}\n")

    # ������ �� ����� ������� (���� ���� ����)
    next_page_button = driver.find_element(By.CLASS_NAME, 'paginator__direction_type_forward')
    if next_page_button.is_enabled():
        next_page_button.click()
        time.sleep(2)  # �� ���������� �����, �������, ��� ����������� ���� ���������� �����
        # TODO: �������������� Selenium Wait ��� ����� `time.sleep(2)`.

        # ���������� ��� ����� ������ �������� ��� ����� �������
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        products = soup.find_all('div', class_='goods-tile')

        # �������� ���������� ��� ������ �� ����� ������� � ����
        with open('output.txt', 'a', encoding='utf-8') as file:
            for product in products:
                title = product.find('div', class_='goods-tile__title').text.strip()
                price = product.find('span', class_='goods-tile__price-value').text.strip()
                file.write(f"{title}: {price}\n")












