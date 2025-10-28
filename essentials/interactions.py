"""
interactions.py
================

Guia básico de interações com Selenium:
✅ Click
✅ Enviar texto
✅ Limpar campo
✅ Submeter formulário
✅ Obter texto e atributos
✅ Scroll até elemento
✅ Esperas simples

"""

from selenium.webdriver.support.ui import WebDriverWait  # para esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # condições para waits


def click_element(driver, locator):
    """Clica em um elemento assim que ele estiver clicável."""
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(locator)
    )
    element.click()


def send_keys_to_element(driver, locator, text, clear=False):
    """Digita texto no elemento (com opção de limpar antes)."""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    if clear:
        element.clear()
    element.send_keys(text)


def get_element_text(driver, locator):
    """Retorna o texto visível do elemento."""
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(locator)
    )
    return element.text


def get_attribute(driver, locator, attribute):
    """Retorna um atributo específico do elemento (ex: href, value)."""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    return element.get_attribute(attribute)


def scroll_to_element(driver, locator):
    """Faz scroll até o elemento estar visível na viewport."""
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(locator)
    )
    driver.execute_script("arguments[0].scrollIntoView();", element)
