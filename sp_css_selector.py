from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# para cambiar el navegador, solo se debe cambiar el driver
driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
driver.maximize_window() # pantalla completa
driver.get("https://login.salesforce.com/?locale=es")   # pagina para la practica

'''
--> Se puede localizar elementos más rápido utilizando la búsqueda por CSS
En el “inspeccionar” del navegador ingresar:

$('.username') || $('#username')

 --> Recordatorio xpath, ingresar en consola del navegador:

$x("//input[@Value='Cancelar']")

-------------------------------------------------------------------------------------------------------

busqueda por elementos agrupados (mecanismo padre e hijo) con las referencias del HTML
utilizando el xpath:

$x("//div[@id='theloginform']/form/div[1]/div/input[1]")


busqueda por elementos agrupados (mecanismo padre e hijo) con las referencias del HTML
utilizando el css:

$("div[id='theloginform'] form div div")

'''

driver.find_element(By.CSS_SELECTOR ,"#username").send_keys("testName")
driver.find_element(By.XPATH, "//div[@id='theloginform']/form/div[1]/div/input[1]").clear()
driver.find_element(By.CSS_SELECTOR, ".password").send_keys("testPass")
driver.find_element(By.CSS_SELECTOR, ".password").clear()
driver.find_element(By.LINK_TEXT, "¿Olvidó la contraseña?").click()
driver.find_element(By.XPATH, "//input[@Value='Cancelar']").click()



driver.close()