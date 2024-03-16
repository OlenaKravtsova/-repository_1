coding: 'utf-8'
import csv
from bs4 import BeautifulSoup as BS
import requests


def get_content_first_page(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "text/html, application/xhtml+xml, application/xml;q=0.9, image/avif, image/webp,*/*;q=0.8"
    }
    resp = requests.get(url, headers=header)
    rows = []

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
            tmp = {'Назва': title_text, 'Ціна грн.': price_str, 'Ціна': price}
            rows.append(tmp)
    return rows


def parse_content_first_page():
    # url = 'https://www.olx.ua/uk/list/q-%D0%BF%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82/'
    url = 'https://www.olx.ua/uk/list/q-%D0%9F%D0%BB%D0%B0%D0%BD%D1%88%D0%B5%D1%82/?page={}'
    rows = []
    for i in range(1, 3):
        _url = url.format(i)
        rows += get_content_first_page(_url)

    csv_title = ['Назва', 'Ціна грн.', 'Ціна']
    with open('olx.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=csv_title, delimiter=';')
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    parse_content_first_page()