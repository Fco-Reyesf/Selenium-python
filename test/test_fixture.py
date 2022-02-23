import pytest

from registroBase import baseLogger


# comando en consola para ejecutar todas las pruebas y crear un reporte
#  py.test -v -s --html=./reportes/reporte_demo4.html        
# esto muestra los registros de las pruebas


@pytest.mark.usefixtures("envioDatos")
class Test_datos(baseLogger):

    def test_mostrarDatos(self, envioDatos):
        print( envioDatos )
        registro = self.getRegistro()
        registro.info(envioDatos[0])
        registro.info(envioDatos[1])
        registro.info(envioDatos[2])