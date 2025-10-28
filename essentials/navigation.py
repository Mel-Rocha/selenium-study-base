"""
navigation.py
==============

Funções essenciais para navegação com Selenium WebDriver:
✅ Acessar e recarregar páginas
✅ Voltar e avançar no histórico
✅ Trabalhar com abas (tabs)
✅ Obter URL atual
"""

from selenium.webdriver.remote.webdriver import WebDriver


def go_to_url(driver: WebDriver, url: str) -> None:
    """Navega diretamente para a URL informada."""
    driver.get(url)


def refresh_page(driver: WebDriver) -> None:
    """Recarrega a página atual."""
    driver.refresh()


def go_back(driver: WebDriver) -> None:
    """Volta para a página anterior no histórico do navegador."""
    driver.back()


def go_forward(driver: WebDriver) -> None:
    """Avança para a próxima página no histórico do navegador."""
    driver.forward()


def get_current_url(driver: WebDriver) -> str:
    """Retorna a URL atual que o navegador está exibindo."""
    return driver.current_url


def open_new_tab(driver: WebDriver, url: str) -> None:
    """Abre uma nova aba e navega para a URL informada."""
    driver.switch_to.new_window("tab")
    driver.get(url)


def switch_to_tab(driver: WebDriver, tab_index: int) -> None:
    """
    Alterna entre abas abertas pelo índice.

    :param driver:
    :param tab_index: índice da aba iniciando em 0
    """
    driver.switch_to.window(driver.window_handles[tab_index])


def close_current_tab(driver: WebDriver) -> None:
    """Fecha a aba atual e volta para a anterior (se existir)."""
    current_tab = driver.current_window_handle
    driver.close()
    tabs = driver.window_handles
    if tabs:
        driver.switch_to.window(tabs[-1])
