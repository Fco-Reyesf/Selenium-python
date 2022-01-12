
from selenium.webdriver import Edge


driver = Edge(executable_path="C:\\Users\\reyes\\Desktop\\edge_test_python\\edgedriver_win64\\msedgedriver.exe")

# entrar a la pagina web
driver.get("https://rahulshettyacademy.com/#/index")

print(driver.title)
print(driver.current_url)
driver.close()
