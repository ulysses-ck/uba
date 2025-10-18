# Un matrimonio está organizando una fiesta y tiene que armar una lista de invitados. Cada uno tiene su propia
# tupla y guarda en ella a todos los que quiere invitar.

# 9. Cuando ya tienen a todos los invitados tienen que juntar sus tuplas, para eso se necesita una función
# que a partir de dos tuplas cree una sola que sea la combinación de ambas tuplas.

from typing import Tuple

def sum_tuples(t1: Tuple[str], t2: Tuple[str]):
    return t1 + t2

print(sum_tuples((1, 2), (3, 4)))