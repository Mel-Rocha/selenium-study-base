"""
Teste Técnico Simulado 🧪 - Login + Scraping
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


# Inicializa navegador com Selenium Manager
service = Service()
driver = webdriver.Chrome(service=service)

# Acessar o site de login
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Preencher login (credenciais fornecidas pelo próprio site)
username = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

username.send_keys("standard_user")
password.send_keys("secret_sauce")
password.send_keys(Keys.ENTER)
time.sleep(3)

# Raspar produtos da página
produtos = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

print("Produtos encontrados:")
for p in produtos:
    print("-", p.text)

time.sleep(5)
driver.quit()
