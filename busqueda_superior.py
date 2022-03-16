import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

lista_productos = []
carro_compra = []

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")                           # pagina para la practica


driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(2)

# ------------------------------------- explicacion -----------------------------------------------------------------
'''
Para buscar en HTML hacia arriba usar el comando:
/parent::{etiqueta}

ejemplo ingresado en consola de navegador:
"//div[@class='product-action']/button/parent::div/parent::div/h4"

entonces, baja con "/div" y sube con "parent::div"

'''

# verificar si los elementos seleccionados para comprar se encuentran en
# en carro de compras


botones =  driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
time.sleep(2)
for boton in botones:
    lista_productos.append(boton.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    boton.click()

print(lista_productos)


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

espera = WebDriverWait(driver,10)
espera.until(ec.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")))
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

time.sleep(2)
vegetales = driver.find_elements(By.CSS_SELECTOR, "p.product-name")

for vegetal in vegetales:
    carro_compra.append(vegetal.text)


print(carro_compra)

assert carro_compra == lista_productos

# -------------- verificar si el descuento se aplica ------------------------------------------

monto_original = driver.find_element(By.CSS_SELECTOR, "span.totAmt").text
espera.until(ec.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promobtn").click()

driver.implicitly_wait(10)          
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)
monto_c_descuento = driver.find_element(By.CSS_SELECTOR, "span.discountAmt").text

assert float(monto_c_descuento) < int(monto_original)


valores = driver.find_elements(By.XPATH, "//tr/td[5]/p")
contador = 0

for valor in valores:
    contador = contador + int(valor.text)

assert contador == int(monto_original)

print("LA PRUEBA FINALIZO CON EXITO")

driver.close()