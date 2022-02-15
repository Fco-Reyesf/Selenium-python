import pytest


@pytest.mark.usefixtures("configuracionGlobal")
class PruebasFixture:
    
    def test_fixture( self ):
        print("soy el principal, pero necesito una configuración")
    
    
    def test_principal_Demo(configuracion):
        print("soy la prueba principal, pero necesito una configuración")