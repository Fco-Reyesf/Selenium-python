'''
Ejercicio.
Desde la página principal se debe ir a la sección de compras, 
luego agregar el producto BlackBerry al carro de compras, 
dirigirse al carro de compras, 
verificar que el producto se encuentre y finalizar el resto de la compra.

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/angularpractice/")                           # pagina para la practica


driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
productos = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for producto in productos:
    nombreProducto = producto.find_element(By.XPATH, "div/h4/a").text
    if nombreProducto == "Blackberry":
        producto.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

wait = WebDriverWait(driver,10)
wait.until(ec.presence_of_element_located((By.CLASS_NAME,"alert-success")))
print(driver.find_element(By.CLASS_NAME,"alert-success").text)



driver.close()

