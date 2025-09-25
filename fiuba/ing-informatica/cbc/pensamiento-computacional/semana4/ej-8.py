# 8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
# a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se
# encuentra.
# b. Guardar las tuplas en una lista.
# c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país
# con el siguiente formato:
# País: <nombre>
# Capital: <capital>
# Continente: <continente>
# Por ejemplo:
# País: Japón
# Capital: Tokio
# Continente: Asia

from typing import List

countries = [
    ("Francia", "Paris", "Europa"),
    ("Argentina", "Buenos Aires", "América del Sur"),
    ("Japón", "Tokio", "Asia"),
    ("Alemania", "Berlin", "Europa"),
    ("Perú", "Lima", "América del Sur"),
]

def show_countries(list_countries: List[tuple[str]]):
    for i in list_countries:
        print(f"País: {i[0]}")
        print(f"Capital: {i[1]}")
        print(f"Continente: {i[2]}")
    

show_countries(countries)