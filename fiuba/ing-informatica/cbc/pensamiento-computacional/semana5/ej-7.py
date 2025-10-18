# 7. Manuel y su pareja armaron una lista numerada con las actividades de mantenimiento de la casa.
# Decidieron dividirse las tareas, a Manuel le tocó hacer todas las actividades con número par, por eso
# necesitamos hacer una función que reciba una lista de enteros, y devuelva otra lista que solamente
# contenga números pares, que vienen a ser las tareas de Manuel.

from typing import List

def return_even_nums(ls: List[int]):
    ls2 = []
    for i in ls:
        if i % 2 == 0:
            ls2.append(i)

    return ls2

print(return_even_nums([1,2,3,4]))