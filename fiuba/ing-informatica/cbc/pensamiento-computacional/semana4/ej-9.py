# 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la
# siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos
# tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
# Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo.

from typing import List

def count_books(lse: List[str]):
    already_viewed = []

    for book in lse:
        if book in already_viewed:
            continue
        else:
            already_viewed.append(book)
            print(f"cantidad de {book}: {lse.count(book)}")


count_books(["a", "a", "b", "c", "c", "c"])

