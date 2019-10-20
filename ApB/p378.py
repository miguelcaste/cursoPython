# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""
from bs4 import BeautifulSoup
import requests

pagina = requests.get("http://www.aemet.es/es/eltiempo/prediccion/municipios/jaen-id23050")
soup = BeautifulSoup(pagina.text, 'html.parser')
prob = soup.find(attrs={'id': 'tabla_prediccion'}).find_all("tr")[3].find_all("td")[1].get_text()
print("La probabilidad de precipitación en Jaén hoy es del", prob
