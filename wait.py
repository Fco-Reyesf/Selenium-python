import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")                           # pagina para la practica

# ----------------------------- espera tiempo indicado ------------------------------

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
items = len( driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert items == 3
botones =  driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
time.sleep(2)
for boton in botones:
    boton.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

# ----------------------------- espera explicita ------------------------------------

# Funcionamiento de la espera explicita: espera hasta que la acción acordada se pueda realizar, 
# en el mismo caso que en implícita (lea la siguiente parte), 
# a esta espera también se le entrega un tiempo máximo de espera.

espera = WebDriverWait(driver,10)
espera.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

espera.until(ec.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promobtn").click()

# ----------------------------- espera implicita ------------------------------------

# Funcionamiento de la espera implícita: según el tiempo dado (en este caso 10s), 
# el código se detiene en la sección de la espera hasta un tiempo máximo de 10s mientras no pueda ejecutar las siguientes líneas de código, 
# en caso de poder realizar la siguiente sección de código, corta el tiempo asignado y continua. 
# Por ejemplo, lleva esperando 5s y revisa que puede continuar en el código, este continua y los segundos restantes quedan anulados.

driver.implicitly_wait(10)          
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)


driver.close()