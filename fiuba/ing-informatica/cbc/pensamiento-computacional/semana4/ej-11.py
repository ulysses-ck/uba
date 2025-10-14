# 11. Se tiene la siguiente lista de palabras: [entender, pueden, humanos, los, que, código,
# escriben, programadores, buenos, Los, “entiende.”, “computadora”, “una”, “que”, “código”,
# “escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
# las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar
# la frase. (ver funciones de listas y strings).

from typing import List

def join_words(lse: List[str]):
    a = ""
    lse.reverse()
    for idx, v in enumerate(lse):
        space = " "
        if len(lse) - 1 == idx:
            space = ""

        a += v + space

    return a


data = ['entender', 'pueden', 'humanos', 'los', 'que', 'código','escriben', 'programadores', 'buenos', 'Los', 'entiende.', 'computadora', 'una', 'que', 'código', 'escribe', 'tonto', 'Cualquier'] 
print(
    join_words(data)
)

