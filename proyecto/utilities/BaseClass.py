import inspect
import logging
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:

    # datos para el registro de actividad
    def getRegistro(self):
        # extraer el nombre de la funcion que esta ejecutando el llamado
        registroNombre = inspect.stack()[1][3]
        registro = logging.getLogger(registroNombre)
        #ubicacion del archivo
        manejoArchivo = logging.FileHandler("./reportes/logFile.log")
        #fomarto de escritura
        formato = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        #fijar formato
        manejoArchivo.setFormatter(formato)
        #agregar formato al archivo
        registro.addHandler(manejoArchivo)
        # escritura en el archivo
        registro.setLevel(logging.DEBUG)
        return registro

    # creacion de metodos genericos
    def VerPresenciaLink(self, txt):
        wait = WebDriverWait(self.driver,10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT,txt)))