import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
from datetime import datetime

from test2.data.testMain_Data import testMainData

driver = None

# funcion para recibir parametros en la consola.
def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge"
    )

@pytest.fixture(params=testMainData.test_main_data)
def muchosDatos(request):
    return request.param

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

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="./imagenes/%s" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'%file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(".\\reportes\\imagenes\\" + name)