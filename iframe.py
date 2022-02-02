
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa

# existen 3 tipos de frame: iframe - frameset - frame
driver.get("https://the-internet.herokuapp.com/iframe")

# para el cambio, se necesida el frame id o index value
# trabaja con elementos dentro del frame
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.CSS_SELECTOR,"#tinymce").clear()
driver.find_element(By.CSS_SELECTOR,"#tinymce").send_keys("nuevo texto en el frame")

# para utilizar los elementos fuera del frame se debe salir
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)


driver.close()