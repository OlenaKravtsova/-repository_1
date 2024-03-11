coding: 'utf-8'
import requests
from datetime import datetime

# https://www.youtube.com/watch?v=zzWnmDi4Xzc


def get_exchange_rates():
    """Ця функція використовує бібліотеку requests, щоб виконати GET-запит до API НБУ за вказаним URL.
     Якщо статус відповіді дорівнює 200 (OK), тоді вона повертає вміст відповіді у форматі JSON.
     У протилежному випадку генерується виняток Exception з повідомленням про помилку."""
    URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    response = requests.request(method="GET", url=URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Помилка отримання даних. Код стану: {response.status_code}")


def write_to_file(data, filename="exchange_rates.txt"):
    """Ця функція призначена для запису отриманих курсів валют у текстовий файл.
    Вона створює файл із заданим ім'ям "exchange_rates.txt" і записує дату та час створення запиту.
    Потім для кожної валюти з отриманих даних вона записує рядок у файл, що містить назву валюти та її курс до гривні."""
    with open(filename, "w") as file:
        file.write(f"[дата створення запиту] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for item in data:
            file.write(f"{item['txt']} to UAH: {item['rate']}\n")


def run():
    """Ця функція викликає get_exchange_rates() для отримання курсів валют і передає їх у write_to_file() для запису у файл.
     Якщо виникає помилка типу requests.exceptions.RequestException, виводиться відповідне повідомлення.
     Якщо виникає будь-яка інша помилка, то виводиться загальне повідомлення про помилку."""
    try:
        exchange_rates = get_exchange_rates()
        write_to_file(exchange_rates)
        print("Курси валют успішно записані у файл.")
    except requests.exceptions.RequestException as e:
        print(f"Не вдалося зробити запит для отримання курсів валют. Помилка: {e}")
    except Exception as e:
        print(f"Сталася інша помилка при виконанні програми. Помилка: {e}")


"""Викликається функція безпосередньо, якщо скрипт запущено."""
run()
