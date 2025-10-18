# 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
# para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
# mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
# vio.
# Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
# de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

from typing import TypedDict, List

class Movie(TypedDict):
    name: str
    year_r: int
    score: int

def greather_than_seven(ls: List[Movie]):
    ls2: List[Movie] = []
    for i in ls:
        if i["score"] > 7:
            ls2.append(i)
            
    return ls2

sol_movies: List[Movie] = [
    {
        "name": "El Viaje de Chihiro",
        "year_r": 2001,
        "score": 10
    },
    {
        "name": "Avatar",
        "year_r": 2009,
        "score": 7
    },
    {
        "name": "Interestelar",
        "year_r": 2014,
        "score": 9 
    },
    {
        "name": "Titanic",
        "year_r": 1997,
        "score": 6 
    },
    {
        "name": "Parásitos",
        "year_r": 2019,
        "score": 8 
    }
]

best_movies_for_tomas = greather_than_seven(sol_movies)

print("Todas las películas de Sol:")
print(sol_movies)
print("\nPelículas con puntaje mayor a 7 (las mejores para Tomás):")
print(best_movies_for_tomas)