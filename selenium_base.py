"""
Script base de estudo para Teste Técnico - Desenvolvedora RPA Jr

Funcionalidades:
- Abre o Chrome
- Acessa um site
- Localiza um elemento
- Imprime conteúdo
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Usando Selenium Manager (não precisa baixar ChromeDriver manualmente!)
service = Service()
driver = webdriver.Chrome(service=service)

driver.get("https://example.com/")

# Busca um elemento
titulo = driver.find_element(By.TAG_NAME, "h1").text
print("Título da página:", titulo)

input("Pressione ENTER para fechar o navegador...")  # permite visualizar no teste
driver.quit()
