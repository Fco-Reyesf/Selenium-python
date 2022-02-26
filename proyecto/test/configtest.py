import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Edge(service=Service("..\\..\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
    driver.get("https://rahulshettyacademy.com/#/index")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()