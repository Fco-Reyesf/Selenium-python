import time
from tokenize import String
from test2.PaginaConfirmar import PaginaConfirmar
from test2.PaginaComprobar import PaginaComprobar
from test2.PaginaPrincipal import PaginaPrincipal
from utilities.BaseClass import BaseClass


'''
comando usado para ejecutar.
py.test .\test_main.py -v --browser edge

comando con reporte html.
py.test .\test_main.py -v --browser edge --html=./reportes/reporte_test_main.html
'''

class TestMain(BaseClass):

    def test_inicio(self, muchosDatos):
        # se recomienda crear las instancias en su clase correspondiente, no en la clase principal
        registro = self.getRegistro()
        paginaPrincipal = PaginaPrincipal(self.driver)
        paginaComprobar = PaginaComprobar(self.driver)
        paginaConfirmar = PaginaConfirmar(self.driver)
        paginaPrincipal.elementosTienda()
        registro.info("obtener todas los titulos de tarjetas")
        tarjetas = paginaComprobar.getTitulosTarjetas()
        i = -1
        for tarjeta in tarjetas:
            i = i + 1
            textoTarjeta = tarjeta.text
            #if textoTarjeta == "Blackberry":
            registro.info(textoTarjeta)
            if textoTarjeta == muchosDatos["busqueda"]:
                paginaComprobar.getseleccionarTarjeta()[i].click()

        paginaComprobar.confirmarElementosCarro()
        paginaComprobar.confirmarCompra()
        registro.info("buscando pais que comienza con: " + muchosDatos["buscarPais"])
        paginaConfirmar.getBuscarimput().send_keys(muchosDatos["buscarPais"])
        time.sleep(5)
        self.VerPresenciaLink(muchosDatos["paisEncontrado"])
        paginaConfirmar.verPalabra().click()
        paginaConfirmar.aceptarCondiciones().click()
        paginaConfirmar.confirmarCompra().click()
        textoAlerta = paginaConfirmar.verAlerta().text
        registro.info("texto que se obtiene de la alerta: " + textoAlerta)
        assert ("Success! Thank you!" in textoAlerta)