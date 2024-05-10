from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicialize o WebDriver (neste caso, vamos usar o Chrome)
driver = webdriver.Chrome()

# Abra a página do site
driver.get("https://www.photoacompanhantes.com")

driver.find_element(By.ID, "search-location").send_keys("São Paulo")

# Aguarde até que o botão de procurar esteja presente na página
search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Procurar')]")))

# Clique no botão de procurar
search_button.click()

# Após clicar no botão de procurar, você pode fazer outras operações com os resultados da pesquisa, se houver

# Feche o navegador após a conclusão
driver.quit()
