# 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
# la siguiente información:
# ● Nombre
# ● Apellido
# ● Intento
# ● Nota
# Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
# primer recuperatorio y 3 si es el segundo recuperatorio.
# Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
# primera oportunidad que rindieron los alumnos.
# ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
# solamente sirve para el intento 1, sino que también pueda servir para los demás.

# rta: pasar un parámetro con el número de intento que se quiere evaluar, sea 1, 2 o 3

from typing import List, TypedDict

class Note(TypedDict):
    name: str
    surname: str
    n_try: int
    qual: int

def return_avg_notes_greather_than_try_one(ls: List[Note]) -> float:
    total = 0

    for i in ls:
        if(i['n_try'] == 1):
            total += i['qual']
    
    return total / len(ls)

notes: List[Note] = [
    {
        "n_try": 2,
        "name": "A",
        "qual": 10,
        "surname": "AA"
    },
    {
        "n_try": 1,
        "name": "B",
        "qual": 10,
        "surname": "AA"
    },
    {
        "n_try": 1,
        "name": "C",
        "qual": 10,
        "surname": "AA"
    },
    {
        "n_try": 1,
        "name": "D",
        "qual": 10,
        "surname": "AA"
    }
]

print(return_avg_notes_greather_than_try_one(notes))