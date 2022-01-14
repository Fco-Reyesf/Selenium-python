
from selenium.webdriver import Edge

# para cambiar el navegador, solo se debe cambiar el driver
driver = Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
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
ingresar en la consola del navegado que se esté utilizando
$("input[name='name']")

ejemplo de uso
driver.find_element_by_css_selector("input[name='name']").send_keys("nombre de prueba")


mostrara la cantidad de elementos que encuentre, si solo muestra uno, entonces, se puede usar como elemento de búsqueda
'''


driver.get("https://rahulshettyacademy.com/angularpractice/")   # pagina para la practica
driver.find_element_by_css_selector("input[name='name']").send_keys("nombre de prueba") # el primer elemento que encuentra es modificado
driver.find_element_by_name("email").send_keys("test@example.com")  # ingresar elemento en etiqueta por nombre name
driver.find_element_by_id("exampleCheck1").click()


driver.close()
