"""
locators.py
------------

Este módulo apresenta os **principais tipos de localizadores do Selenium** com 1 exemplo cada,
seguindo boas práticas básicas.

Objetivo:
- Ter um cheat sheet rápido para consultas
- Entender prioridade de seletores
- Saber quando usar cada tipo de forma simples
"""

from selenium.webdriver.common.by import By

# ------------------------------------------------
# 1️⃣ By.ID → prioridade máxima se disponível
# - Único e rápido, menos propenso a falhas
# ------------------------------------------------
EXAMPLE_ID = (By.ID, "username")

# ------------------------------------------------
# 2️⃣ By.NAME → útil quando IDs não existem
# - Geralmente confiável para formulários
# ------------------------------------------------
EXAMPLE_NAME = (By.NAME, "password")

# ------------------------------------------------
# 3️⃣ By.CLASS_NAME → bom para elementos comuns
# - Atenção: pode retornar múltiplos elementos
# ------------------------------------------------
EXAMPLE_CLASS_NAME = (By.CLASS_NAME, "btn-primary")

# ------------------------------------------------
# 4️⃣ By.TAG_NAME → raro em automação prática
# - Útil para pegar listas genéricas, ex: todos os <a>
# ------------------------------------------------
EXAMPLE_TAG_NAME = (By.TAG_NAME, "a")

# ------------------------------------------------
# 5️⃣ By.LINK_TEXT → bom para links exatos
# - Funciona apenas quando texto completo é conhecido
# ------------------------------------------------
EXAMPLE_LINK_TEXT = (By.LINK_TEXT, "Esqueci minha senha")

# ------------------------------------------------
# 6️⃣ By.PARTIAL_LINK_TEXT → links parciais
# - Útil quando texto exato pode mudar
# ------------------------------------------------
EXAMPLE_PARTIAL_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Esqueci")

# ------------------------------------------------
# 7️⃣ By.CSS_SELECTOR → muito poderoso, flexível
# - Mais rápido que XPATH
# - Evite seletores muito longos
# ------------------------------------------------
EXAMPLE_CSS_SELECTOR = (By.CSS_SELECTOR, "form.login input[type='text']")

# ------------------------------------------------
# 8️⃣ By.XPATH → último recurso
# - Útil quando não há IDs ou classes confiáveis
# - Tentar manter XPaths curtos e resilientes
# ------------------------------------------------
EXAMPLE_XPATH = (By.XPATH, "//form[@id='login']//input[@type='password']")
