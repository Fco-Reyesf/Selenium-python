from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa

# existen 3 tipos de frame: iframe - frameset - frame
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

accion = ActionChains(driver)
accion.double_click(driver.find_element(By.ID, "double-click"))
accion.perform()

alerta = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alerta.text
alerta.accept()

# este es el clic izquierdo
accion.context_click(driver.find_element(By.ID, "double-click"))
accion.perform()


driver.close()