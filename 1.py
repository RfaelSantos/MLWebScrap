from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


#config
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#driver
driver = webdriver.Chrome(options=options, service=service)
driver.get('https://www.google.com')
search = driver.find_element(By.ID, "APjFqb").send_keys("Corinthians")
search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "btnK"))).click()
