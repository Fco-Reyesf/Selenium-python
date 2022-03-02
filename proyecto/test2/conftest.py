import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# funcion para recibir parametros en la consola.
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_seleccionado = request.config.getoption("browser")
    if browser_seleccionado == "chrome":
        driver = webdriver.Chrome(service=Service("ruta para el driver"))
    elif browser_seleccionado == "firefox":
        driver = webdriver.Firefox(service=Service("ruta para el driver"))
    elif browser_seleccionado == "edge":
        driver = webdriver.Edge(service=Service("..\\..\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()