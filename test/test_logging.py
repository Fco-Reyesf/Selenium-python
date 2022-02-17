import logging

'''
Niveles de logs:

debug - Info - warning - error - critical

dependiendo del nivel, solo imprime desde el nivel hacia la derecha,
por ejemplo, si el nivel es info, no imprime debug.
si el nivel es warning, no imprime debug e info
'''


def test_logging():
    login = logging.getLogger(__name__)
    #ubicacion del archivo
    manejoArchivo = logging.FileHandler("./test/reportes/logFile.log")
    #fomarto de escritura
    formato = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #fijar formato
    manejoArchivo.setFormatter(formato)
    #agregar formato al archivo
    login.addHandler(manejoArchivo)
    # escritura en el archivo
    login.setLevel(logging.ERROR)
    login.debug("ejecutando como debug")
    login.info("informacion del estado")
    login.warning("algo esta en modo de advertencia")
    login.error("algo tiene un error")
    login.critical("problema critico")

