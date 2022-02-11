'''
comando para ejecutar en terminal y ver salidas por pantalla, 
esto se debe realizar dentro de la carpeta donde se encuentran las pruebas.
En este caso dentro de: ./test
PD: se ejecutan todos los archivos que encuentre.

py.test -v -s

Para ejecutar solo archivos en específico, se debe ingresar el nombre del archivo:

py.test “nombreArchivo.py” -v -s

para ejecutar pruebas en específico, se debe agregar el parámetro “-k” y escribir un distintivo que tengan varias pruebas en común (independiente del archivo del que proviene). En este caso buscara en todos los archivos y ejecutara solo las pruebas que tengan en el nombre “resta”.
py.test  -k resta -v -s

También se pueden ejecutar las pruebas que se encuentran con marcas, en este caso en el archivo de “test_demo.py” una prueba cuenta con la marca “ejecutar”.
py.test  -m ejecutar -v -s

Para no ejecutar ciertas pruebas se puede usar una marca de “skip”, se encuentra comentado en el archivo de “test_demo.py”

------------------------------------------------------------------------
'''

import pytest


@pytest.mark.ejecutar
# @pytest.mark.skip
def test_restaConDecimal():
    print("soy resta con decimal")