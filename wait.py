import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")                           # pagina para la practica

# ----------------------------- espera tiempo indicado ------------------------------

driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(4)
items = len( driver.find_elements(By.XPATH, "//div[@class='products']/div"))
assert items == 3
botones = len( driver.find_elements(By.XPATH, "//div[@class='product-action']/button"))

for boton in botones:
    boton.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[@text()='PROCEED TO CHECKOUT']").click()

# ----------------------------- espera implicita ------------------------------------



# ----------------------------- espera explicita ------------------------------------

driver.close()