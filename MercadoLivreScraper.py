from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import openpyxl


class MercadoLivreScraper:
    def __init__(self):
        self.driver = None

    def save_excel(self, names, prices, links, search):
        df = pd.DataFrame({'Name': names, 'Price': prices, 'Link': links})
        df.to_excel(f'{search}_results.xlsx', index=False)
        return True

    def connect(self, service, options):
        self.driver = webdriver.Chrome(options=options, service=service)
        self.driver.get('https://www.mercadolivre.com.br/')

    def search_product(self, search):
        self.driver.find_element(By.XPATH, '//*[@id="cb1-edit"]').send_keys(search)
        self.driver.find_element(By.XPATH, '/html/body/header/div/div[2]/form/button').click()

        links = [link.get_attribute('href') for link in  self.driver.find_elements(By.CLASS_NAME, 'ui-search-link__title-card')]
        names = [title.text for title in self.driver.find_elements(By.CLASS_NAME, 'ui-search-item__title')]
        div_prices = self.driver.find_elements(By.CLASS_NAME, 'ui-search-price__second-line')
        prices_d = [div_preco.find_element(By.CLASS_NAME, 'andes-money-amount__fraction').text for div_preco in div_prices]

        prices = [price for index, price in enumerate(prices_d) if index % 2 == 0]

        return names, prices, links


if __name__ == '__main__':
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    mercado_livre_scraper = MercadoLivreScraper()

    search = input("Product: ")

    mercado_livre_scraper.connect(service, options)

    names, prices, links = mercado_livre_scraper.search_product(search)

    if names and prices:
        if mercado_livre_scraper.save_excel(names, prices, links, search):
            print('The Excel file was saved successfully!')
            mercado_livre_scraper.driver.quit()
