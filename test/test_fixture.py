import pytest


@pytest.mark.usefixtures("envioDatos")
class Test_datos:

    def test_mostrarDatos(self, envioDatos):
        print( envioDatos )