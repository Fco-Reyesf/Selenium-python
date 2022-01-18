from selenium import webdriver
from selenium.webdriver.common.by import By


# para cambiar el navegador, solo se debe cambiar el driver
driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
driver.maximize_window() # pantalla completa


'''
# entrar a la pagina web
driver.get("https://rahulshettyacademy.com/#/index")
print(driver.title)
print(driver.current_url)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # cambio de pagina

driver.minimize_window()

driver.back() # volver a la pagina anterior
driver.refresh() # recargar pagina
'''


# para verificar que solo existe un elemento característico.
'''
-------------------------------------------------------------------------------------------------------------------------
[metodo con css_selector]

ingresar en la consola del navegado que se esté utilizando

donde input es el tipo de entrada y name es la referencia

$("input[name='name']") 

ejemplo de uso
driver.find_element_by_css_selector("input[name='name']").send_keys("nombre de prueba")

mostrara la cantidad de elementos que encuentre, si solo muestra uno, entonces, se puede usar como elemento de búsqueda

-------------------------------------------------------------------------------------------------------------------------
[metodo con xpath]

ingrsar en la consola del navegador 

$"//input[@type='submit']"

como resultado mostrara la cantidad de elementos existentes
'''

driver.get("https://rahulshettyacademy.com/angularpractice/")   # pagina para la practica
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("nombre de prueba") # el primer elemento que encuentra es modificado
driver.find_element(By.NAME, "email").send_keys("tetear@example.com")  # ingresar elemento en etiqueta por nombre name
driver.find_element(By.ID, "exampleCheck1").click()  # click en checkbox
driver.find_element(By.XPATH, "//input[@type='submit']").click()   # metodo con xpath 
print(driver.find_element(By.CLASS_NAME, "alert-success").text)    # busqueda por clase   ---   Corroborar que la ejecución de la prueba termina correctamente



driver.close()
