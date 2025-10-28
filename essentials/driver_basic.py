"""
driver_basic.py
----------------

Este módulo fornece a forma mais simples e correta de inicializar o Selenium WebDriver em 2025.

Por que isso é importante no teste RPA?
- Mostrar que você sabe configurar o Selenium SEM baixar driver manual.
- Demonstrar que entende o ciclo de vida do navegador (abrir e fechar).
- Ter segurança para começar qualquer script de automação.

✔ Compatível com Chrome, usando Selenium Manager automaticamente
✔ Ideal para testes técnicos e scripts rápidos

Como usar:
-----------
from essentials.driver_basic import create_driver

driver = create_driver()
driver.get("https://www.google.com")

# ... seu código aqui ...

driver.quit()
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def create_driver():
    """
    Cria e retorna uma instância do Chrome WebDriver usando Selenium Manager.

    Returns:
        WebDriver: Instância do navegador pronta para uso.
    """
    # ✅ Service() sem argumentos = Selenium Manager encontra o ChromeDriver automaticamente
    service = Service()

    # ✅ Inicializa o Chrome WebDriver
    driver = webdriver.Chrome(service=service)

    # ✅ Ajusta a janela
    driver.maximize_window()

    return driver


if __name__ == "__main__":
    # Teste rápido se rodar este arquivo diretamente
    driver = create_driver()
    driver.get("https://www.google.com")
    input("Pressione ENTER para fechar...")
    driver.quit()
