import inspect
import logging

# usado con la clase test_fixture.py para prueba de uso.

class baseLogger:
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