from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
# driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa
driver.get("https://rahulshettyacademy.com/AutomationPractice/")                           # pagina para la practica

textoIngresado = "nombre falso"

driver.find_element(By.CSS_SELECTOR, "#name").send_keys(textoIngresado)
driver.find_element(By.ID, "alertbtn").click()
alerta = driver.switch_to.alert                                             # manejo de la alerta
txtAlerta = alerta.text
if textoIngresado in txtAlerta:
    print("el texto se encuentra en la alerta")
else:
    print("no se encuentra el txt en la alerta")

alerta.accept()                                                             # aceptar la alerta
#alerta.dissmis()                                                            # cancelar la alerta
driver.close
