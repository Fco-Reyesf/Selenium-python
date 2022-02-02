
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(1)
# Cuando se abre una ventana nueva se numeran en el orden de izquierda a derecha, 
# en este caso queda la ventana principal en posición 0 y la secundaria en posición 1.
driver.switch_to.window(driver.window_handles[1])
# imprime el texto de la segunda ventana
print(driver.find_element(By.TAG_NAME,"h3").text)
# cierre de ventana secundaria
driver.close()
driver.switch_to.window(driver.window_handles[0])
#imprime el texto de la primera ventana
print(driver.find_element(By.TAG_NAME,"h3").text)


driver.close()