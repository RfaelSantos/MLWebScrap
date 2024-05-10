from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


class MercadoLivreScraper:
    def __init__(self):
        self.driver = None

    def create_dataframe(self, names, prices, links):
        data = {'Name': names, 'Price': prices, 'Link': links}
        return pd.DataFrame(data)

    def connect(self):
        self.driver = webdriver.Chrome(service=self.create_service(), options=self.create_options())
        self.driver.get('https://www.mercadolivre.com.br/')

    def create_service(self):
        return Service(ChromeDriverManager().install())

    def create_options(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        return options

    def search_product(self, search):
        self.driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys(search)
        self.driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/button').click()

        links = [link.get_attribute('href') for link in  self.driver.find_elements(By.CLASS_NAME, 'ui-search-link__title-card')]
        names = [title.text for title in self.driver.find_elements(By.CLASS_NAME, 'ui-search-item__title')]
        div_prices = self.driver.find_elements(By.CLASS_NAME, 'ui-search-price__second-line')
        prices_d = [div_preco.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text for div_preco in div_prices]

        prices = [price for index, price in enumerate(prices_d) if index % 2 == 0]

        return names, prices, links
