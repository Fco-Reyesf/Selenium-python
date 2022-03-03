from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class PaginaConfirmar:

    def __init__(self, driver):
        self.driver = driver

    buscarImput = (By.ID, "country")
    muestraPalabra = (By.LINK_TEXT, "India")
    botonCondiciones = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    botonConfirmarCompra = (By.CSS_SELECTOR, "[type='submit']")
    textoAlerta = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getBuscarimput(self):
        return self.driver.find_element(*PaginaConfirmar.buscarImput)

    def verPalabra(self):
        wait = WebDriverWait(self.driver,10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT,"India")))
        return self.driver.find_element(*PaginaConfirmar.muestraPalabra)

    def aceptarCondiciones(self):
        return self.driver.find_element(*PaginaConfirmar.botonCondiciones)
    
    def confirmarCompra(self):
        return self.driver.find_element(*PaginaConfirmar.botonConfirmarCompra)

    def verAlerta(self):
        return self.driver.find_element(*PaginaConfirmar.textoAlerta)