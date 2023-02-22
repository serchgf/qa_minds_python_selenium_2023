"""
Escribe un script que dado el día,mes y año de nacimiento de una persona determine lo siguiente:
Cuántos años tiene.
Si en lo que va del año ya cumplio o no.
Determinar a qué generación pertenece:
La generación silenciosa. Nacidos entre 1920 y 1939.
Los baby boomers. Nacidos entre 1940 y 1959.
Generación X. Nacidos entre 1960 y 1979.
Generación Y o millennials. Nacidos entre 1980 y 1989.
Generación Z. Nacidos entre 1990 en adelante.
"""
from datetime import datetime
day = input("Que dia naciste: ")
month = input("Que mes naciste: ")
year = input("En que año naciste: ")
day= int(day)
month= int(month)
year= int(year)

current_year = int(datetime.now().strftime('%Y'))
current_month = int(datetime.now().strftime('%m'))
current_day = int(datetime.now().strftime('%d'))


if current_day<day and current_month<month:
    print("aun no cumples años")
if current_day>=day and current_month>=month:
    print("ya cumpliste años")

if year>=1920 and year<=1939:
    print("generación silenciosa")
if year>=1940 and year<=1959:
    print("generación baby boomers")
if year>=1960 and year<=1979:
    print("Generación X")
if year>=1980 and year<=1989:
    print("Generación Y o millennials")
if year >= 1990:
    print("Generación z")
