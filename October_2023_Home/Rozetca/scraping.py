coding: 'utf-8'
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}


def collect_products(url="https://hard.rozetka.com.ua/ua/monitors/c80089/"):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        page_count = int(soup.find('div', class_="pagination ng-star-inserted").find_all('li', class_="pagination__item ng-star-inserted")[-1].text.strip())
        print(f"Всього сторінок: {page_count}")
    except (AttributeError, IndexError):
        page_count = 1
        print("Всього сторінок: 1 (або сторінка без навігації)")

    products = []

    for page in range(1, page_count + 1):
        page_url = f"https://hard.rozetka.com.ua/ua/monitors/c80089/{page}/"
        page_response = requests.get(url=page_url, headers=headers)
        page_soup = BeautifulSoup(page_response.text, 'html.parser')
        items = page_soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")

        for item in items:
            title = item.find('a', class_="product-link goods-tile__heading").text.strip()
            try:
                price = item.find('div', class_="goods-tile__price price--red ng-star-inserted").find('p', class_="ng-star-inserted").text.strip()
            except AttributeError:
                price = "Немає"

            products.append({
                "title": title,
                "price": price
            })

            # Змінено: Запис результатів у текстовий файл з кодуванням utf-8
            output_file_path = 'output.txt'  # Замініть на відповідний шлях
            with open(output_file_path, 'w', encoding='utf-8') as file:
                for product in products:
                    file.write(f"Назва: {product['title']}, Ціна: {product['price']}\n")

    return products

# Приклад виклику функції
result = collect_products()
print(result)

# Запис результатів у текстовий файл з кодуванням utf-8
# output_file_path = r'C:\\Testgit\\Hellel\\October_2023_Home\\Home_work_29\\page\\output.txt'  # Замініть на відповідний шлях
with open('output.txt', 'w', encoding='utf-8') as file:
    for product in result:
        file.write(f"Назва: {product['title']}, Ціна: {product['price']}\n")

