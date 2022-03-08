from selenium.webdriver.common.by import By

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
        return self.driver.find_element(*PaginaConfirmar.muestraPalabra)

    def aceptarCondiciones(self):
        return self.driver.find_element(*PaginaConfirmar.botonCondiciones)
    
    def confirmarCompra(self):
        return self.driver.find_element(*PaginaConfirmar.botonConfirmarCompra)

    def verAlerta(self):
        return self.driver.find_element(*PaginaConfirmar.textoAlerta)