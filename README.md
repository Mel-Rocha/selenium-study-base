# Rodando o projeto ⚙️
## Dependências do projeto

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

# Recursos Úteis para Estudo Selenium 📝

Documentação oficial: https://www.selenium.dev/documentation/

Exploração interativa com Python:
Para descobrir métodos, atributos e opções de qualquer objeto do Selenium:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Listar atributos e métodos
dir(By)
dir(Options)

# Obter ajuda detalhada (docstrings)
help(By)
help(Options)

```
1. Use help() para entender o que cada classe ou método faz.

2. Use dir() para inspecionar atributos e métodos disponíveis.

3. Consulte a doc oficial rapidamente para verificar argumentos ou opções não documentadas pelo help do Python, por exemplo:

```
--headless=new
--start-maximized
```

Combine conhecimento do Python (como help(), dir(), type()) com leitura da documentação oficial para resolver dúvidas pontuais sem travar.

---