from selenium.webdriver.common.by import By

class PaginaPrincipal:

    def __init__(self, driver):
        self.driver = driver

    # variables con elementos de la pagina
    tienda = (By.CSS_SELECTOR, "a[href*='shop']")

    def elementosTienda(self):
        return self.driver.find_element(*PaginaPrincipal.tienda).click()
