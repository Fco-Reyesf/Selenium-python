import logging

'''
Niveles de logs:

debug - Info - warning - error - critical

dependiendo del nivel, solo imprime desde el nivel hacia la derecha,
por ejemplo, si el nivel es info, no imprime debug.
si el nivel es warning, no imprime debug e info
'''


def test_registro():
    registro = logging.getLogger(__name__)
    #ubicacion del archivo
    manejoArchivo = logging.FileHandler("./reportes/logFile.log")
    #fomarto de escritura
    formato = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    #fijar formato
    manejoArchivo.setFormatter(formato)
    #agregar formato al archivo
    registro.addHandler(manejoArchivo)
    # escritura en el archivo
    registro.setLevel(logging.ERROR)
    registro.debug("ejecutando como debug")
    registro.info("informacion del estado")
    registro.warning("algo esta en modo de advertencia")
    registro.error("algo tiene un error")
    registro.critical("problema critico")

