"""
interactions.py
================

Funções reutilizáveis para interações com Selenium:
✅ Click com espera explícita
✅ Envio de texto com limpeza opcional
✅ Obtenção de texto e atributos do elemento
✅ Scroll até elemento
"""

from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver

from essentials.waits import (
    wait_for_presence,
    wait_for_element_clickable,
    wait_for_element_visible,
)


def click_element(driver: WebDriver, locator: Tuple[str, str]) -> None:
    """Clica em um elemento assim que estiver clicável."""
    element = wait_for_element_clickable(driver, locator)
    element.click()


def send_keys_to_element(
    driver: WebDriver,
    locator: Tuple[str, str],
    text: str,
    clear: bool = False
) -> None:
    """Digita texto no elemento (com opção de limpar antes)."""
    element = wait_for_presence(driver, locator)
    if clear:
        element.clear()
    element.send_keys(text)


def get_element_text(driver: WebDriver, locator: Tuple[str, str]) -> str:
    """Retorna o texto visível do elemento."""
    element = wait_for_element_visible(driver, locator)
    return element.text


def get_attribute(driver: WebDriver, locator: Tuple[str, str], attribute: str) -> str:
    """Retorna o valor de um atributo específico do elemento."""
    element = wait_for_presence(driver, locator)
    return element.get_attribute(attribute)


def scroll_to_element(driver: WebDriver, locator: Tuple[str, str]) -> None:
    """Faz scroll até o elemento estar visível na tela."""
    element = wait_for_element_visible(driver, locator)
    driver.execute_script("arguments[0].scrollIntoView();", element)
