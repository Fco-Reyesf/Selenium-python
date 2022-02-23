
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

class pruebaUno:

    def test_e2e(self):
        driver = webdriver.Edge(service=Service(".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe"))
        # driver = webdriver.Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window() # pantalla completa

        # existen 3 tipos de frame: iframe - frameset - frame
        driver.get("https://the-internet.herokuapp.com/iframe")