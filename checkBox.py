from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
driver.maximize_window() # pantalla completa


driver.get("https://rahulshettyacademy.com/AutomationPractice/")                           # pagina para la practica

# -------------------- ejemplo 1 de checkbox ------------------------------------------------

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for box in checkboxes:                                                                      # marcar todas las casillas
    if box.get_attribute("value") == "option2":
        box.click()
        assert box.is_selected()


# -----------------  ejemplo 2 --------------------------------------------------------------

radioBotones = driver.find_elements(By.NAME, "radioButton")         
radioBotones[2].click()
assert radioBotones[2].is_selected()

driver.close()