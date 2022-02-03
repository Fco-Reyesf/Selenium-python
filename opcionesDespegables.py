
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver import ActionChains

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa

# existen 3 tipos de frame: iframe - frameset - frame
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
accion = ActionChains(driver)
menu = driver.find_element(By.ID, "mousehover")
accion.move_to_element(menu)
accion.perform()
opcionMenu = driver.find_element(By.LINK_TEXT, "Top")
accion.move_to_element(opcionMenu)
accion.click()
accion.perform()

driver.close()