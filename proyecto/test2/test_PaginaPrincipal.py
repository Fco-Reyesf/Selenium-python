from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By



class TestPaginaPrincipal(BaseClass):

    # variables con elementos de la pagina
    tienda = (By.CSS_SELECTOR, "a[href*='shop']")

    def test_shopItems(self):
        return self.driver.find_element(*TestPaginaPrincipal.tienda).click()
