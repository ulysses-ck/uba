# 6. Santiago armó una lista con el pedido de empanadas de su familia pero ahora quiere saber la cantidad
# de gustos diferentes que tiene que pedir.
# Podemos pensar la lista de empanadas como una lista de strings, entonces deberíamos devolver la
# cantidad de strings diferentes que hay en una lista.

from typing import List

def count_unique_flavors(ls: List[str]):
    uniques = []

    for i in ls:
        if i not in uniques:
            uniques.append(i)

    
    return len(uniques)

print(count_unique_flavors(["asd", "bc", "asd", "cd"]))