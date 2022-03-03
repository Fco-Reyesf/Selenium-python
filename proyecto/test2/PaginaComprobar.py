from selenium.webdriver.common.by import By

class PaginaComprobar:

    def __init__(self, driver):
        self.driver = driver
    
    tituloTarjeta = (By.CSS_SELECTOR, ".card-title a")
    botonSeleccionarTarjeta = (By.CSS_SELECTOR, ".card-footer button")
    botonConfirmarCarro = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    botonConfirmarCompra = (By.XPATH, "//button[@class='btn btn-success']")

    def getTitulosTarjetas(self):
        return self.driver.find_elements(*PaginaComprobar.tituloTarjeta)

    def getseleccionarTarjeta(self):
        return self.driver.find_elements(*PaginaComprobar.botonSeleccionarTarjeta)

    def confirmarElementosCarro(self):
        return self.driver.find_element(*PaginaComprobar.botonConfirmarCarro).click()

    def confirmarCompra(self):
        return self.driver.find_element(*PaginaComprobar.botonConfirmarCompra).click()
        
        #confirmPage = ConfirmPage(self.driver)
        #return confirmPage