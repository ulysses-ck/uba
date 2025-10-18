# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia
# tupla y guarda en ella a todos los que quiere invitar.

# 8. Si alguien cancela tienen que sacarlo de la tupla.
# Hacer una función que reciba la tupla y un nombre, y devuelva una nueva tupla sin el nombre pasado
# por parámetro.
# Las tuplas son inmutables, entonces ¿Cómo podemos hacer para “eliminar” un elemento de una tupla?
# Recordemos que las tuplas tienen definido el operador +, pero no el operador -.

from typing import Tuple

def remove_invitee(ls: Tuple[str], invitee: str):
    new_tuple = []
    for i in ls:
        if i != invitee:
            new_tuple.append(i)

    return tuple(new_tuple)

print(remove_invitee(("aa", "bb", "cc", "dd", "vv"), "bb"))