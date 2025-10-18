# 7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
# todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
# puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
# a. Crear el diccionario que represente esta situación.
# AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
# maratonista, entonces 
# ¿Qué tipo de dato debería ser el campo que guarda todas las
# maratones?
# rta: Lista
# ¿Y qué tipo de dato es la maratón en sí?
# rta: diccionario

# b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
# c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una
# de forma ascendente.


from typing import TypedDict, List
from operator import itemgetter
from pprint import pprint

class Marathon(TypedDict):
    name: str
    year: str
    pos: int
    time_finished: int

class Player(TypedDict):
    name:str
    dni: int
    all_m: List[Marathon]

ls = [
    {
        "name": "Pedro Gómez",
        "dni": 32145678,
        "all_m": [
            {
                "name": "Maratón de Buenos Aires",
                "year": "2023",
                "pos": 15,
                "time_finished": 11445  
            },
            {
                "name": "Maratón de Berlín",
                "year": "2022",
                "pos": 8,
                "time_finished": 10530  
            }
        ]
    },
    {
        "name": "Ana García",
        "dni": 40987654,
        "all_m": [
            {
                "name": "Media Maratón de New York",
                "year": "2024",
                "pos": 3,
                "time_finished": 5100   
            },
            {
                "name": "Maratón de Londres",
                "year": "2023",
                "pos": 12,
                "time_finished": 11110  
            },
            {
                "name": "Maratón de Buenos Aires",
                "year": "2021",
                "pos": 1,
                "time_finished": 10085  
            }
        ]
    },
    {
        "name": "Carlos Ruiz",
        "dni": 28765432,
        "all_m": [
            {
                "name": "Maratón de Tokio",
                "year": "2023",
                "pos": 50,
                "time_finished": 14575  
            }
        ]
    }
]

ls2: List[Player] = sorted(ls, key=itemgetter("name"))
print("ls2")
pprint(ls2)
print()

ls3 = []
for i in ls2:
    i["all_m"] = sorted(i["all_m"], key=itemgetter("time_finished"))
    ls3.append(i)
print("ls3")
pprint(ls3)