Práctica 1: Web scraping

Descripción
Esta práctica se ha realizado bajo el contexto de la asignatura Tipología y ciclo de vida de los datos,
En ella, se aplican técnicas de web scraping mediante el lenguaje de programación Python para extraer así datos de la web Top500 y generar un dataset.

Ficheros del código fuente
Top500Computers.py 

# Top500 Computers Scrapper
## Español

Extrae el listado de los 500 computadores mas potentes
(https://www.top500.org/list/2019/06/?page={}) 

Para ejecutar el script es necesario instalar la siguientes bibliotecas:
```
import csv
import requests
from bs4 import BeautifulSoup
```

El script se debe ejecutar de la siguiente manera:
```
python Top500Computers.py
```

