import pytest


@pytest.fixture(scope="class")
def configuracion():
    print("me ejecuto antes por requerimiento")
    yield 
    print("termino mi tarea")

@pytest.fixture()
def envioDatos():
    print("se envian los datos")
    return ["nombre","Constraseña","Correo"]

@pytest.fixture(params=[("hola","buenas"),("mundo","universo"),("1","2")])
def muchosDatos(request):
    return request.param
