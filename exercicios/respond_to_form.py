from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# URL do formulário (substitua com o real)
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScVVRGCOiMp-PJcrc3k9VHWNy5n0HeofJOqfFWBoRHgBvrKwA/viewform?usp=header'

# Configura e abre o navegador com o driver automático
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for i in range(37):
    driver.get(FORM_URL)
    sleep(2)

    try:
        # Marca "Não" nas 3 perguntas (ajuste se necessário)
        for pergunta in range(1, 4):
            xpath = f'(//div[@role="radio" and contains(@aria-label, "Não")])[{pergunta}]'
            driver.find_element(By.XPATH, xpath).click()
            sleep(0.5)

        # Clica no botão enviar
        enviar_btn = driver.find_element(By.XPATH, '//span[text()="Enviar"]')
        enviar_btn.click()
        sleep(2)

        print(f'Resposta {i+1} enviada com sucesso.')

    except Exception as e:
        print(f'Erro na resposta {i+1}: {e}')
        break

driver.quit()
