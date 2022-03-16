# Selenium-python
Practica de QA automatizado con Selenium en Python, se encontrará con archivos sueltos “explicativos” sobre la materia de como desarrollar pruebas automatizadas sobre una pagina web, en la carpeta de “test” se encuentra información más avanzada y finalmente un proyecto casi completo que se encuentra en la carpeta proyecto.

# Requisitos previos

Herramientas utilizadas:
- Visual Studio Code con la extensión de Python (para auto completar)
- Python
- Instalar Selenium y Selenium webdriver (utilizando el comando pip install)

## Explicación del contenido

| Tipo de búsqueda | Selenium sintaxis ejemplo  | 
|     :---:      |     :---:   |
| Xpath   | driver.find_element(By.XPATH, "//input[@type='submit']")  |
| Css selector   | driver.find_element(By.CSS_SELECTOR,"input[name='name']") |
| ID   | driver.find_element(By.ID, "texto")     |
| Name   |  driver.find_element(By.NAME, "texto")  |
| Class name  | driver.find_element(By.CLASS_NAME, "texto") |
| Link text   | driver.find_element(By.LINK_TEXT, "Click Here")     |
| Tag name   | driver.find_element(By.TAG_NAME, "h3")     |

## Ejemplo para búsqueda con CSS en la consola del navegador

Sintaxis:
```
$("input[atributo='Valor']")
$("input[name='name']")
```
## Ejemplo para búsqueda con XPATH en la consola del navegador

Sintaxis:
```
$x("//input[@atributo='valor']")
$x("//input[@type='submit']")
```

## Búsqueda superior dentro del CSS de la página utilizando el método de XPATH

Para acceder a una etiqueta superior de la página, se utiliza el comando 
```
parent::etiqueta
```
ejemplo de como recorre hacia arriba pasando por 2 div hasta llegar a un h4.
```
$x("//div[@class='product-action']/button/parent::div/parent::div/h4")
```
## Búsqueda inferior dentro del CSS de la página utilizando el método de XPATH
Para acceder a una etiqueta inferior de la página, se utiliza el comando 
```
"espacio"etiqueta
```
ejemplo de como recorre bajando pasando por 2 etiquetas hasta llegar a un parent.
```
$("table[id='productCartTables'] tbody tr td:nth-child(5) p")
```
# 