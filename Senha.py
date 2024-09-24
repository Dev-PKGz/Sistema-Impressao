import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

driver = None
last_f9_press_time = 0  
block_time = 5  # Intervalo mínimo entre dois cliques em F9 (aumentado para 5 segundos)

def open_site_and_send_f9():
    global driver

    if driver is None:
        chrome_options = Options()
        chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        chrome_options.add_argument("--kiosk-printing")
        chrome_options.add_argument("--window-size=1920x1080")
        chrome_options.add_argument("--window-position=-10000,0")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("http://192.168.0.137/gerar_senha/")
        time.sleep(3)
    else:
        driver.refresh()

    body = driver.find_element("tag name", 'body')
    body.send_keys(Keys.F9)
    print("Processo de impressão iniciado...")

    print("Aguardando Impressão...")
    time.sleep(10)  # Aumentado para 10 segundos

    # Fechar a aba após a impressão
    print("Fechando aba de impressão...")
    driver.close()  
    driver = None  # Reseta o driver

def detect_f9_key():
    global last_f9_press_time
    while True:
        print("Aguardando a tecla F9...")
        keyboard.wait('F9')

        current_time = time.time()  
        if current_time - last_f9_press_time >= block_time:
            open_site_and_send_f9()  
            last_f9_press_time = current_time
        else:
            print(f"F9 bloqueado, aguarde {block_time} segundos antes de tentar novamente.")

detect_f9_key()