import pytest


@pytest.mark.usefixtures("configuracion")
class Test_Fixture_Demo:
    
    def test_principal_fixture( self ):
        print("soy el principal, pero necesito una configuración")
    
    
    def test_secundario_fixture( self ):
        print("soy la prueba principal, pero necesito una configuración")