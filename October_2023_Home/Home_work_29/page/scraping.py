coding: 'utf-8'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver.get("https://comfy.ua/ua/plane-table-computer/")


class ConfyParse:

    def __init__(self, url:str, items:list, count:int=2):
        self.url = url
        self.items = items
        self.count = count

    def set_up(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://comfy.ua/ua/plane-table-computer/")

    def paginator(self):
            pass

    def parse_page(self):
            pass

    def parse(self):
            pass





