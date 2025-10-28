"""
waits.py

Este módulo fornece funções utilitárias para gerenciar técnicas de espera
no Selenium WebDriver, garantindo que os elementos estejam disponíveis
antes de interagir com eles. Ele encapsula o uso de esperas implícitas
e explícitas, reduzindo falhas por carregamento assíncrono e aumentando
a estabilidade dos testes automatizados.

Tipos de espera disponíveis:

- Implicit Wait:
    Configura um tempo de espera padrão para todas as buscas de elementos.
    Deve ser utilizada com cautela, pois afeta todo o WebDriver.

- Explicit Wait:
    Especificada para um elemento ou condição específica do DOM,
    como visibilidade, clique ou presença na página.

As funções deste módulo são pensadas para uso direto em casos de teste,
padronizando comportamentos e melhorando a legibilidade do código.
"""

from typing import Optional, Tuple
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Padrão de espera utilizado no framework como fallback
DEFAULT_TIMEOUT: int = 10


def set_implicit_wait(driver: WebDriver, timeout: int = DEFAULT_TIMEOUT) -> None:
    """
    Configura a espera implícita para todas as buscas de elementos.

    :param driver: Instância do WebDriver em uso.
    :param timeout: Tempo máximo de espera em segundos.
    """
    driver.implicitly_wait(timeout)


def wait_for_element_visible(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = DEFAULT_TIMEOUT
) -> WebElement:
    """
    Aguarda até que o elemento esteja visível na página.

    Visível significa que o elemento:
    - Está presente no DOM
    - Está com o atributo `displayed` igual a True

    :param driver: WebDriver em execução.
    :param locator: Localizador do elemento (By, selector).
    :param timeout: Tempo máximo de espera em segundos.
    :return: WebElement encontrado.
    :raises TimeoutException: Caso o elemento não se torne visível.
    """
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_element_clickable(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = DEFAULT_TIMEOUT
) -> WebElement:
    """
    Aguarda até que o elemento esteja clicável.

    Útil para elementos presentes, porém ainda bloqueados ou invisíveis.

    :param driver: WebDriver em execução.
    :param locator: Localizador do elemento (By, selector).
    :param timeout: Tempo máximo de espera em segundos.
    :return: WebElement pronto para clique.
    :raises TimeoutException
    """
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )


def wait_for_presence(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = DEFAULT_TIMEOUT
) -> WebElement:
    """
    Aguarda somente a presença do elemento no DOM.

    ✔ Mais rápido que visibilidade
    ✘ Não garante que esteja visível na tela

    :param driver: WebDriver em execução.
    :param locator: Localizador do elemento.
    :param timeout: Tempo máximo de espera em segundos.
    :return: WebElement encontrado.
    """
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(locator)
    )


def wait_for_invisibility(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = DEFAULT_TIMEOUT
) -> bool:
    """
    Aguarda até que o elemento deixe de ser visível ou renderizado.

    :param driver: WebDriver em execução.
    :param locator: Localizador do elemento.
    :param timeout: Tempo máximo de espera em segundos.

    :return: True se desaparecer dentro do timeout, False caso contrário.
    """
    try:
        result = WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
        return bool(result)  # força retorno bool
    except TimeoutException:
        return False


def wait_and_fallback(
    driver: WebDriver,
    locator: Tuple[str, str],
    timeout: int = DEFAULT_TIMEOUT
) -> Optional[WebElement]:
    """
    Tenta localizar o elemento com espera explícita,
    porém retorna None caso o elemento não exista ou demore demais.

    ✅ Ótimo para elementos opcionais
    ✅ Evita que o teste quebre à toa

    :param driver: WebDriver em execução.
    :param locator: Localizador do elemento.
    :param timeout: Tempo máximo de espera em segundos.

    :return: WebElement encontrado ou None em caso de timeout.
    """
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    except TimeoutException:
        return None
