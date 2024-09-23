import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Função para abrir o navegador e enviar o comando F9
def open_site_and_send_f9():
    # Configurando as opções do Chrome
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    chrome_options.add_argument("--kiosk-printing")  # Ativa a impressão em modo quiosque
    chrome_options.add_argument("--window-size=1920x1080")  # Define o tamanho da janela (opcional)
    
    # Coloca o navegador fora da tela (simulando "headless")
    chrome_options.add_argument("--window-position=-10000,0")  # Posiciona a janela fora da tela visível

    # Usando o ChromeDriverManager para baixar e configurar o ChromeDriver automaticamente
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)  # Configurando o navegador usando o webdriver-manager
    driver.get("http://localhost/gerar_senha/")  # Substitua pelo URL do site que você quer abrir
    
    time.sleep(3)  # Espera o site carregar

    # Enviar o comando F9 para a página
    body = driver.find_element("tag name", 'body')
    body.send_keys(Keys.F9)
    print("Processo de impressão iniciado...")

    # Esperar um tempo antes de fechar (por exemplo, 10 segundos)
    print("Aguardando Impressão...")
    time.sleep(10)  # Ajuste o tempo conforme necessário

    # Após o tempo de espera, o navegador é fechado
    driver.quit()
    print("Impressão Realizada.")

# Função que detecta a tecla F9 e executa a ação
def detect_f9_key():
    while True:  # Loop infinito
        print("Aguardando a tecla F9...")
        keyboard.wait('F9')
        open_site_and_send_f9()

# Executa o detector de tecla F9
detect_f9_key()
