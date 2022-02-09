'''
Cuando selenium modifica algo en la página, no se puede rescatar normalmente, 
por lo que, hay que ingresar comandos js DOM, estos comando permiten acceder a cualquier elemento de la pagina.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/angularpractice/")                           # pagina para la practica

driver.find_element(By.NAME, "name").send_keys("quueeee pasa")
# no imprime el texto que se ecuentra en el elemento
print(driver.find_element(By.NAME, "name").text)

# si imprime el texto del elemento
print(driver.find_element(By.NAME, "name").get_attribute("value"))


'''
Obtener elementos por js DOM en consola del navegador:
document.getElementsByName("name")

Ejemplo de imprime el texto que se encuentra en el elemento
document.getElementsByName("name")[0].value
'''

print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# clic en boton que no es perteciente de la pagina actual. 
# algo no perteneciente puede ser un menù
boton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", boton)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

driver.close()
