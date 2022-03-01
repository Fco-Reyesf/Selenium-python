from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utilities.BaseClass import BaseClass

class TestUno(BaseClass):

    def test_e2e(self):
        espera = WebDriverWait(self.driver,10)
        espera.until(ec.presence_of_element_located((By.CSS_SELECTOR,"input[name='name']")))
        self.driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("nombre de prueba") # el primer elemento que encuentra es modificado
        self.driver.find_element(By.NAME, "email").send_keys("tetear@example.com")                   # ingresar elemento en etiqueta por nombre name
        self.driver.find_element(By.ID, "exampleCheck1").click()                                     # click en checkbox
        dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))              # identificar el dropdown
        dropdown.select_by_visible_text("Female")                                               # seleccionar por opciones de texto
        dropdown.select_by_index(0)                                                             # seleccionar por opciones de despliegue en número de posición
        #dropdown.select_by_value(value opcion)                                                 # seleccionar por valor de Value=
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()                        # metodo con xpath 
        mensaje = self.driver.find_element(By.CLASS_NAME, "alert-success").text