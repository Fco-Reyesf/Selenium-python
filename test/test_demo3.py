'''
Para ejecutar una prueba antes que otra ingresar “@pytest.fixture()” 
sobre la función que debe realizarse primero.

fixture : Son usados para crear configuraciones estándar que pueden favorecer el funcionamiento de varias pruebas en general.
Puede ser escrito en un archivo aparte.
'''

import pytest

@pytest.fixture()
def configuracion():
    print("me ejecuto antes por requerimiento")
    yield 
    print("termino mi tarea")


def test_principalDemo(configuracion):
    print("soy la prueba principal, pero necesito una configuración")

