import time
from test2.PaginaConfirmar import PaginaConfirmar
from test2.PaginaComprobar import PaginaComprobar
from test2.PaginaPrincipal import PaginaPrincipal
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestMain(BaseClass):

    def test_inicio(self):
        paginaPrincipal = PaginaPrincipal(self.driver)
        paginaComprobar = PaginaComprobar(self.driver)
        paginaConfirmar = PaginaConfirmar(self.driver)
        paginaPrincipal.elementosTienda()
        tarjetas = paginaComprobar.getTitulosTarjetas()
        i = -1
        for tarjeta in tarjetas:
            i = i + 1
            textoTarjeta = tarjeta.text
            if textoTarjeta == "Blackberry":
                paginaComprobar.getseleccionarTarjeta()[i].click()

        paginaComprobar.confirmarElementosCarro()
        paginaComprobar.confirmarCompra()

        paginaConfirmar.getBuscarimput().send_keys("ind")
        time.sleep(5)
        paginaConfirmar.verPalabra().click()
        paginaConfirmar.aceptarCondiciones().click()
        paginaConfirmar.confirmarCompra().click()
        textoAlerta = paginaConfirmar.verAlerta().text

        assert ("Success! Thank you!" in textoAlerta)