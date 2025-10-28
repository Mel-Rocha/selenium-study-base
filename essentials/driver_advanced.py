"""
driver_advanced.py
-------------------

Este módulo demonstra como inicializar o Chrome WebDriver com configurações avançadas
utilizando ChromeOptions. Isso é muito útil em automações reais de RPA.

Quando usar?
- Ambientes de produção (sem GUI / headless)
- Sites que exigem persistência de login (user-data-dir)
- Para reduzir falhas relacionadas à segurança ou logs do Chrome
- Customizações de User-Agent para parecer mais "humano"

Ainda usando Selenium Manager (não precisa baixar ChromeDriver!)
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def create_advanced_driver(
    headless: bool = False,
    user_data_dir: str | None = None,
    user_agent: str | None = None,
):
    """
    Cria e retorna um WebDriver Chrome com opções avançadas configuráveis.

    Args:
        headless (bool): Se True, roda o Chrome sem interface gráfica.
        user_data_dir (str | None): Caminho para um perfil persistente de usuário.
        user_agent (str | None): User-Agent customizado.

    Returns:
        WebDriver: Instância configurada do navegador pronta para automação.
    """
    options = Options()

    # Headless moderno
    if headless:
        options.add_argument("--headless=new")
        # evita layout mobile e elementos escondidos!
        options.add_argument("--window-size=1920,1080")
    else:
        # somente para execução com GUI
        options.add_argument("--start-maximized")

    # Para reduzir logs de debug do Chrome
    options.add_argument("--log-level=3")
    options.add_argument("--disable-logging")

    # Ignora erros SSL (sites com certificados incompletos)
    options.add_argument("--ignore-certificate-errors")

    # Perfil persistente (mantém login)
    if user_data_dir:
        options.add_argument(f"--user-data-dir={user_data_dir}")

    # User-Agent customizado
    if user_agent:
        options.add_argument(f"--user-agent={user_agent}")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)

    return driver


if __name__ == "__main__":
    d = create_advanced_driver(
        headless=False,
        # Exemplo para persistir login do Chrome local:
        # user_data_dir="/home/seuusuario/.config/google-chrome/Default"
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/123.0"
    )
    d.get("https://www.whatismybrowser.com")
    input("Pressione ENTER para fechar...")
    d.quit()
