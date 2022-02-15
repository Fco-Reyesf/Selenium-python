import pytest


@pytest.fixture()
def configuracionGlobal():
    print("me ejecuto antes por requerimiento")
    yield 
    print("termino mi tarea")