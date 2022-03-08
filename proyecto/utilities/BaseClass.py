import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class BaseClass:

    # creacion de metodos genericos
    def VerPresenciaLink(self, txt):
        wait = WebDriverWait(self.driver,10)
        wait.until(ec.presence_of_element_located((By.LINK_TEXT,txt)))