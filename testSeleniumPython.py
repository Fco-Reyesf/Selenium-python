
from selenium.webdriver import Edge


driver = Edge(executable_path=".\\edge_driver_selenium\\edgedriver_win64\\msedgedriver.exe")

# entrar a la pagina web
driver.get("https://rahulshettyacademy.com/#/index")

print(driver.title)
print(driver.current_url)
driver.close()
