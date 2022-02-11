'''
Para ejecutar una prueba antes que otra ingresar “@pytest.fixture()” 
sobre la función que debe realizarse primero.
'''

import pytest

@pytest.fixture()
def configuracion():
    print("me ejecuto antes por requerimiento")
    yield 
    print("termino mi tarea")


def test_principalDemo(configuracion):
    print("soy la prueba principal, pero necesito una configuración")

